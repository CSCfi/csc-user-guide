!!! error "Edistynyt taso"
    Sinulla tulee olla Linuxin, Dockerin, Docker Composen ja Komposen tuntemus. Python-osaaminen on plussaa.  
    Rahtin osalta suosimme OpenShift CLI -työkalun [oc](../usage/cli.md) käyttöä.

# Kuinka ottaa 4cat käyttöön Rahtissa { #how-to-deploy-4cat-in-rahti }

Tämä opas on pitkämuotoinen ja selittää kaikki vaiheet, jotka olivat tarpeen [4cat_fi](https://github.com/uh-dcm/4cat_fi)-sovelluksen käyttöönottoon Rahtissa. Tarkoituksena on kertoa tarina siitä, miten eri ongelmat löydettiin ja ratkaistiin. Jokaisella ongelmalla on oma lukunsa, ja toivottavasti ratkaisu on helppo soveltaa muihin samankaltaisiin sovelluksiin. Jätämme pois joitain vääriä johtolankoja ja ratkaisuja, joita seurasin alun perin yrittäessäni ottaa tämän sovelluksen käyttöön, jotta opas ei kasvaisi eksponentiaalisesti. Muista kuitenkin, että tällaiset prosessit ovat harvoin suoraviivaisia, ja ratkaisun löytämiseksi löytyy yleensä paljon ei-ratkaisuja.

4Cat on keruu- ja analyysityökalu. Yllä linkatulta Github-sivulta selviää, että työkalua käytetään sosiaalisen median alustojen analysoimiseen, ja että yksi asennustavoista on docker compose. Tämä on hyvää uutista, koska:

1. Voimme testata sovelluksen käyttöönottoa docker composella ja nähdä, miltä se näyttää.
1. Meidän ei tarvitse luoda docker-konttia tyhjästä.
1. Voimme käyttää docker compose -käyttöönottoa pohjana ja mukauttaa sen Kubernetes-käyttöönotoksi [komposella](https://kompose.io). Tämä työkalu on suunniteltu erityisesti tällaisia muunnoksia varten. Heidän sivustoltaan: "Our conversions are not always 1:1 from Docker Compose to Kubernetes, but we will help get you 99% of the way there!". Se säästääkin paljon työlästä muunnosaikaa, mutta se ei vielä ratkaise kaikkea.

!!! warning "Linux 🐧 on käytössä kaikissa esimerkeissä"
    Olemme valmistelleet tämän oppaan Linux-koneella. Periaatteessa pienellä sovittamisella kaikki komennot toimivat myös Windowsissa ja Macissa, mutta jos olet epävarma, suosittelen [asentamaan pienen VM:n Poutaan](../../pouta/launch-vm-from-web-gui.md) ja käyttämään sitä oppaan seuraamiseen. Tämä on hyödyllistä myös Linux-käyttäjille, sillä voit asennella, poistaa ja vaihtaa ohjelmistoja ilman riskiä rikkoa paikallista asennusta.

## Docker Compose { #docker-compose }

1. Ennen jatkamista tarvitsemme asennettuna dockerin ja docker compose -liitännäisen. Löydät ohjeet docker composen asennukseen täältä:

    - <https://docs.docker.com/compose/install/>

    Debianissa ja Ubuntussa voit asentaa sen näin:

    ```sh
    sudo apt-get update
    sudo apt-get install docker.io docker-compose
    ```

    !!! Info "Vaihtoehdot Dockerille 🐋"
        Voit käyttää sen sijaan podman composea tai vastaavaa, mutta käytämme tässä dockeria, koska se on yleisin työkalu.

1. Kun docker compose on asennettu, otetaan 4cat käyttöön ja katsotaan, miltä se näyttää ja toimii. Tarvitset repositorion kloonauksen ja docker-composen ajon kloonatussa kansiossa:

    ```sh
    git clone https://github.com/uh-dcm/4cat_fi
    cd 4cat_fi
    sudo docker compose up
    ```

    Tämä käynnistää sovelluksen käyttöönoton koneelle. Kestää jonkin aikaa hakea imaget ja konfiguroida sovellus. Jos painat `Ctrl+C`, sovellus sulkeutuu. Jos haluat ajaa sen taustalla, lisää `-d` tai `--detach` docker-compose-komentoon.

    ![docker-compose-tuloste](../../img/4cat-docker-compose.png)

    Hetken kuluttua sovellus on saatavilla portissa `80` (`PUBLIC_PORT`):

    ![4cat ensimmäinen ajo](../../img/4cat.png)

### Analyysi { #analysis }

[docker-compose.yml](https://github.com/digitalmethodsinitiative/4cat/blob/master/docker-compose.yml) -tiedosto on seuraava:

```yaml
services:
  db:
    container_name: 4cat_db
    image: postgres:${POSTGRES_TAG}
    restart: unless-stopped
    environment:
      - POSTGRES_USER=${POSTGRES_USER}
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
      - POSTGRES_DB=${POSTGRES_DB}
      - POSTGRES_HOST_AUTH_METHOD=${POSTGRES_HOST_AUTH_METHOD}
    volumes:
      - 4cat_db:/var/lib/postgresql/data/
    healthcheck:
      test: [ "CMD-SHELL", "pg_isready -U $${POSTGRES_USER}" ]
      interval: 5s
      timeout: 5s
      retries: 5

  backend:
    image: digitalmethodsinitiative/4cat:${DOCKER_TAG}
    container_name: 4cat_backend
    restart: unless-stopped
    env_file:
      - .env
    depends_on:
      db:
        condition: service_healthy
    ports:
      - ${PUBLIC_API_PORT}:4444
    volumes:
      - 4cat_data:/usr/src/app/data/
      - 4cat_config:/usr/src/app/config/
      - 4cat_logs:/usr/src/app/logs/
    entrypoint: docker/docker-entrypoint.sh

  frontend:
    image: digitalmethodsinitiative/4cat:${DOCKER_TAG}
    container_name: 4cat_frontend
    restart: unless-stopped
    env_file:
      - .env
    depends_on:
      - db
      - backend
    ports:
      - ${PUBLIC_PORT}:500
      - ${TELEGRAM_PORT}:443
    volumes:
      - 4cat_data:/usr/src/app/data/
      - 4cat_config:/usr/src/app/config/
      - 4cat_logs:/usr/src/app/logs/
    command: ["docker/wait-for-backend.sh"]

volumes:
  4cat_db:
    name: ${DOCKER_DB_VOL}
  4cat_data:
    name: ${DOCKER_DATA_VOL}
  4cat_config:
    name: ${DOCKER_CONFIG_VOL}
  4cat_logs:
    name: ${DOCKER_LOGS_VOL}
```

Katsotaan myös [.env](https://github.com/uh-dcm/4cat_fi/blob/master/.env) -tiedosto:

```ini
# 4CAT Version: Update with latest release tag or 'latest'
# https://hub.docker.com/repository/docker/digitalmethodsinitiative/4cat/tags?page=1&ordering=last_updated
DOCKER_TAG=stable
# You can select Postrgres Docker image tags here to suit your needs: https://hub.docker.com/_/postgres
POSTGRES_TAG=latest

# Database setup
POSTGRES_USER=fourcat
POSTGRES_PASSWORD=supers3cr3t
POSTGRES_DB=fourcat
POSTGRES_HOST_AUTH_METHOD=trust
# POSTGRES_HOST should correspond with the database container name set in docker-compose.yml
POSTGRES_HOST=db
POSTGRES_PORT=5432  # Docker postgres image uses port 5432

# Server information
# SERVER_NAME is only used on first run; afterwards it can be set in the frontend
SERVER_NAME=localhost
PUBLIC_PORT=80

# Backend API
# API_HOST is used by the frontend; in Docker it should be the backend container name
# (or "localhost" if front and backend are running together in one container
API_HOST=backend
PUBLIC_API_PORT=4444

# Telegram apparently needs its own port
TELEGRAM_PORT=443

# Docker Volume Names
DOCKER_DB_VOL=4cat_4cat_db
DOCKER_DATA_VOL=4cat_4cat_data
DOCKER_CONFIG_VOL=4cat_4cat_config
DOCKER_LOGS_VOL=4cat_4cat_logs

# Gunicorn settings
worker_tmp_dir=/dev/shm
workers=4
threads=4
worker_class=gthread
log_level=debug
```

Kuten näet, `docker-compose.yml` on [YAML](https://en.wikipedia.org/wiki/YAML)-tiedosto, jossa on kaksi pääosaa: `services` ja `volumes`. `Services`-kohteita on 3 ja `volumes`-kohteita 4. Kuberneteksessa tämä tarkoittaa 3 `Deploymentia` ja 4 `PersistentVolumeClaimia` (PVC). Palvelun tärkeimmät kentät ovat:

- `image` on image, jonka docker noutaa ja ajaa jokaiselle palvelulle. Meillä on kaksi eri imagea: `postgres` (tunnettu tietokanta) ja `4cat_fi`. `Frontend` ja `backend` käyttävät samaa imagea, mutta niillä on eri komento/entrypoint. Koska docker compose toimii, tiedämme, että molemmat imaget ovat olemassa ja noudettavissa ilman ongelmia.
- `environment` ja `env_file` määrittelevät ympäristömuuttujat, joilla palvelut konfiguroidaan. Esimerkiksi `POSTGRES_PASSWORD` välittää salasanan tietokannalle.
- `volumes` kertoo dockerille, mitkä volumet liitetään palveluun ja mihin kansioon ne liitetään.
- `ports` määrittelee julkiset portit, sisäiset portit ja niiden välisen kytkennän. Merkintä on `<ulkoinen_portti>:<sisäinen_portti>`.
- `entrypoint` ja `command` ovat komentoja, jotka suoritetaan, kun image käynnistetään. Postgresilla ei ole kumpaakaan, koska käytämme imagen oletus-`command`ia/`entrypoint`ia.

Volumes-osio on yksinkertaisempi ja sisältää vain listan nimiä. Docker composen "volume" on tavallinen docker-volume eikä sisällä kokoa. Tämä johtuu siitä, että se käyttää paikallista levyä, ja koko on paikallisen levyn kapasiteetin rajoissa. Kubernetesin volymit sen sijaan määritellään kooltaan, ja se on huomioitava muunnoksessa.

`.env`-tiedosto sisältää oletusarvot sovelluksen käyttöönottoa varten, esimerkiksi `PUBLIC_PORT`, joka on asetettu arvoon `80`.

## Kompose { #kompose }

Kompose mahdollistaa `docker-compose.yaml`-tiedoston muuntamisen joukoksi Kubernetesin YAML-tiedostoja.

1. Meillä tulee olla [kompose](https://kompose.io/) asennettuna. Seuraa ohjeita täällä:

    - <https://kompose.io/installation/>

    Koska docker on jo asennettuna, voimme käyttää docker-menetelmää, joka rakentaa imagen lähdekoodista:

    ```sh
    sudo docker build -t kompose https://github.com/kubernetes/kompose.git\#main
    ```

1. Aja kompose (ollessasi edelleen 4cat_fi-kansiossa):

    ```sh
    $ docker run --rm -it -v $PWD:/opt kompose sh -c "cd /opt && kompose convert"
    WARN The "DOCKER_CONFIG_VOL" variable is not set. Defaulting to a blank string.
    WARN The "DOCKER_LOGS_VOL" variable is not set. Defaulting to a blank string.
    WARN The "DOCKER_DB_VOL" variable is not set. Defaulting to a blank string.
    WARN The "DOCKER_DATA_VOL" variable is not set. Defaulting to a blank string.
    WARN The "PUBLIC_PORT" variable is not set. Defaulting to a blank string.
    WARN The "TELEGRAM_PORT" variable is not set. Defaulting to a blank string.
    WARN The "DOCKER_TAG" variable is not set. Defaulting to a blank string.
    WARN The "POSTGRES_TAG" variable is not set. Defaulting to a blank string.
    WARN The "POSTGRES_USER" variable is not set. Defaulting to a blank string.
    WARN The "POSTGRES_PASSWORD" variable is not set. Defaulting to a blank string.
    WARN The "POSTGRES_DB" variable is not set. Defaulting to a blank string.
    WARN The "POSTGRES_HOST_AUTH_METHOD" variable is not set. Defaulting to a blank string.
    WARN The "PUBLIC_API_PORT" variable is not set. Defaulting to a blank string.
    WARN The "DOCKER_TAG" variable is not set. Defaulting to a blank string.
    WARN Restart policy 'unless-stopped' in service frontend is not supported, convert it to 'always'
    WARN Restart policy 'unless-stopped' in service db is not supported, convert it to 'always'
    WARN Restart policy 'unless-stopped' in service backend is not supported, convert it to 'always'
    WARN File don't exist or failed to check if the directory is empty: stat :/usr/src/app/data: no such file or directory
    WARN File don't exist or failed to check if the directory is empty: stat :/usr/src/app/config: no such file or directory
    WARN File don't exist or failed to check if the directory is empty: stat :/usr/src/app/logs: no such file or directory
    WARN Service "db" won't be created because 'ports' is not specified
    WARN File don't exist or failed to check if the directory is empty: stat :/var/lib/postgresql/data: no such file or directory
    WARN File don't exist or failed to check if the directory is empty: stat :/usr/src/app/data: no such file or directory
    WARN File don't exist or failed to check if the directory is empty: stat :/usr/src/app/config: no such file or directory
    WARN File don't exist or failed to check if the directory is empty: stat :/usr/src/app/logs: no such file or directory
    INFO Kubernetes file "backend-service.yaml" created
    INFO Kubernetes file "frontend-service.yaml" created
    INFO Kubernetes file "backend-deployment.yaml" created
    INFO Kubernetes file "env-configmap.yaml" created
    INFO Kubernetes file "4cat-data-persistentvolumeclaim.yaml" created
    INFO Kubernetes file "4cat-config-persistentvolumeclaim.yaml" created
    INFO Kubernetes file "4cat-logs-persistentvolumeclaim.yaml" created
    INFO Kubernetes file "db-deployment.yaml" created
    INFO Kubernetes file "4cat-db-persistentvolumeclaim.yaml" created
    INFO Kubernetes file "frontend-deployment.yaml" created
    ```

1. Sinulla pitäisi olla muutamia uusia tiedostoja:

    - "backend-service.yaml"
    - "frontend-service.yaml"
    - "backend-deployment.yaml"
    - "env-configmap.yaml"
    - "4cat-data-persistentvolumeclaim.yaml"
    - "4cat-config-persistentvolumeclaim.yaml"
    - "4cat-logs-persistentvolumeclaim.yaml"
    - "db-deployment.yaml"
    - "4cat-db-persistentvolumeclaim.yaml"
    - "frontend-deployment.yaml"

### Analyysi { #analysis }

Työkalu loi neljää tyyppiä olevia tiedostoja: `service`, `deployment`, `configmap` ja `persistentvolumeclaim`. Aloitetaan yksinkertaisimmista:

- `persistentvolumeclaim`-tiedostot määrittelevät volumet. Jokaiselle docker compose -tiedoston `volume`-määrittelylle on yksi tiedosto. Katsotaan esimerkki ja oleelliset rivit:

    ```yaml
    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
      labels:
        io.kompose.service: 4cat-logs
      name: 4cat-logs
    spec:
      accessModes:
        - ReadWriteOnce
      resources:
        requests:
          storage: 100Mi
    ```

    Näemme, että `name` on säilytetty compose-määrittelystä (löytyy kohdasta `metadata > name`). `accessMode` on `ReadWriteOnce`, eli volume voidaan liittää vain kerran. Lopuksi koko on oletusarvoisesti `100Mi` (löytyy kohdasta `spec > resources > request > storage`).

- `configmap`-tiedosto(t) varastoivat konfiguraatioita. Meidän tapauksessa `.env`:in (ei-docker-compose-spesifit) muuttujat on käännetty tiedostoon `env-configmap.yaml`. `name` on `env` ja muuttujat ovat `data`-kohdassa.

- `service`-tiedostot määrittelevät "vakaat verkkoidentiteetit", jotka toimivat kuormantasaajina. Kullekin `deploymentille` luodaan service, ja se vie ulos kaikki deploymentin tarjoamat portit. Esimerkiksi `frontend-service.yaml`:

    ```yaml
    apiVersion: v1
    kind: Service
    metadata:
      annotations:
        kompose.cmd: kompose convert
        kompose.version: 1.34.0 (cbf2835db)
      labels:
        io.kompose.service: frontend
      name: frontend
    spec:
      ports:
        - name: "5000"
          port: 5000
          targetPort: 5000
        - name: "443"
          port: 443
          targetPort: 443
      selector:
        io.kompose.service: frontend
    ```

    Kaksi oleellista osaa ovat `selector` ja `ports`. Ensimmäinen kytkee servicen `deploymentiin`, ja jälkimmäinen listaa portit, joita service tarjoaa. Katso lisätietoja kohdasta [Services](../networking.md#services).

- `deployment` on monimutkaisin konfiguraatio. Voimme yrittää kartoittaa `docker-compose.yaml`:in asetukset näihin tiedostoihin. Käytetään esimerkiksi lyhintä tuotettua tiedostoa:

    ```yaml
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      annotations:
        kompose.cmd: kompose convert
        kompose.version: 1.34.0 (cbf2835db)
      labels:
        io.kompose.service: db
      name: db
    spec:
      replicas: 1
      selector:
        matchLabels:
          io.kompose.service: db
      strategy:
        type: Recreate
      template:
        metadata:
          annotations:
            kompose.cmd: kompose convert
            kompose.version: 1.34.0 (cbf2835db)
          labels:
            io.kompose.service: db
        spec:
          containers:
            - env:
                - name: POSTGRES_DB
                - name: POSTGRES_HOST_AUTH_METHOD
                - name: POSTGRES_PASSWORD
                - name: POSTGRES_USER
              image: 'postgres:'
              livenessProbe:
                exec:
                  command:
                    - pg_isready -U ${POSTGRES_USER}
                failureThreshold: 5
                periodSeconds: 5
                timeoutSeconds: 5
              name: 4cat-db
              volumeMounts:
                - mountPath: /var/lib/postgresql/data
                  name: 4cat-db
          restartPolicy: Always
          volumes:
            - name: 4cat-db
              persistentVolumeClaim:
                claimName: 4cat-db
    ```

    - `image` on kohdassa `spec > template > spec > containers > image`, tässä tapauksessa `postgres:`. Tämä on virhe, koska tagi `latest` puuttuu; korjaamme tämän myöhemmin.
    - `environment` on kohdassa `spec > template > spec > containers > env`, eikä arvoja ole asetettu.
    - `volumes` on kohdissa `spec > template > spec > volumes` ja `spec > template > spec > containers > volumeMounts`.
    - `ports` ovat kohdassa `spec > template > spec > containers > ports` sekä vastaavissa `service`-tiedostoissa.
    - Lopuksi `command` on `spec > template > spec > containers > command` (katso esimerkki `backend-deployment.yaml`).

    Kuten huomaat, tuotetut YAML-tiedostot eivät ole täydellisiä, mutta ne kelpaavat pohjaksi käyttöönoton jatkamiseksi.

## Käyttöönotto Rahtissa { #deployment-to-rahti }

Otamme nykyiset muokkaamattomat YAML-tiedostot ja viemme ne yksi kerrallaan. Asenna ensin [oc](../usage/cli.md#the-command-line-tools-page-in-the-rahti-web-ui) ja [kirjaudu Rahtiin](../usage/cli.md#how-to-login-with-oc). Sitten sinun tulee [luoda Rahti-projekti](../usage/projects_and_quota.md#creating-a-project). Varmista lopuksi, että olet oikeassa projektissa: `oc project <project_name>`.

### Volumet, ConfigMapit ja Servicet { #volumes-configmaps-and-services }

Nämä kolme tyyppiä ovat suoraviivaisia, eikä niiden pitäisi aiheuttaa ongelmia.

1. Aloitetaan luomalla `volumes` yksi kerrallaan:

     ```sh
     $ oc create -f 4cat-config-persistentvolumeclaim.yaml
     persistentvolumeclaim/4cat-config created

     $ oc create -f 4cat-data-persistentvolumeclaim.yaml
     persistentvolumeclaim/4cat-data created

     $ oc create -f 4cat-db-persistentvolumeclaim.yaml
     persistentvolumeclaim/4cat-db created

     $ oc create -f 4cat-logs-persistentvolumeclaim.yaml
     persistentvolumeclaim/4cat-logs created
     ```

    Tämä luo 4 volumea tilaan `Pending`. Ne pysyvät `Pending`-tilassa, kunnes viemme `deploymentit`. Tämä on odotettua.

1. Luodaan myös `configMap`:

    ```sh
    $ oc create -f env-configmap.yaml
    configmap/env created

    $ oc get cm
    NAME                       DATA   AGE
    env                        22     5s
    kube-root-ca.crt           1      5m45s
    openshift-service-ca.crt   1      5m45s
    ```

    Nämä kaksi muuta riviä (`kube-root-cs.crt` ja `openshift-service-ca.crt`) ovat ennalta luotuja Kubernetesin ja Openshiftin perus-configmapeja.

1. Emme odota virheitä `servicejen` luonnissa (db-servicen luonti puuttuu, koska docker compose -tiedostossa ei ollut määritelty portteja — luomme sen itse myöhemmin):

    ```sh
    $ oc create -f frontend-service.yaml
    service/frontend created

    $ oc create -f backend-service.yaml
    service/backend created

    $ oc get service
    NAME       TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)            AGE
    backend    ClusterIP   172.30.109.120   <none>        4444/TCP           21h
    frontend   ClusterIP   172.30.139.56    <none>        5000/TCP,443/TCP   21h
    ```

    Backendin osalta tulos on odotettu, kytkentä oli `4444:4444`. Frontendin osalta ei, koska siellä kytkentä oli `80:5000`. Tämä ei ole iso ongelma, koska Rahtin ulkopuolelle pääsyä varten käytämme `Routea`, joka voi muuntaa ja julkaista minkä tahansa portin standardeihin 80/443-portteihin. Jätämme sen toistaiseksi näin.

### DB-deploymentit { #db-deployments }

Lopuksi luomme deploymentit. Meillä on 3 deploymentia, ja aloitamme tietokannan deploymentista.

1. Luodaan nykyinen versio:

    ```sh
    $ oc create -f db-deployment.yaml
    deployment.apps/db created

    $ oc get pods
    NAME                  READY   STATUS             RESTARTS   AGE
    db-66db46fb89-vzqrz   0/1     InvalidImageName   0          26s
    ```

1. Tämä on odotettua, koska `latest`-tagi puuttuu imagen nimestä. Korjataan se ja yritetään uudelleen. Muokkaa `db-deployment.yaml`, lisää `latest` imagen arvoon, eli: `postgres:latest`,

    ```diff
                 - name: POSTGRES_USER
    -          image: 'postgres:'
    +          image: 'postgres:latest'
               livenessProbe:
                 exec:
    ```

    ja luo/korvaa deployment:

    ```sh
    $ oc replace -f db-deployment.yaml
    deployment.apps/db replaced

    $ oc get pods
    NAME                  READY   STATUS              RESTARTS   AGE
    db-76fcbdc9d8-dgmqr   0/1     CrashLoopBackOff    1 (1s ago)   24s
    ```

    !!! Info "YAML-tiedostot"
        Teemme muutokset `YAML`-tiedostoihin, jotta voimme luoda koko käyttöönoton uudelleen myöhemmin. Voit myös lisätä tiedostot Git-repositorioon ja tehdä commitin jokaisesta muutoksesta, jolloin muutosten historia ja syyt ovat selkeästi nähtävissä commit-historiassa.

1. Deploy ei toimi, mutta eri syystä. Katsotaan miksi:

    ```sh
    $ oc logs db-76fcbdc9d8-dgmqr
    chmod: changing permissions of '/var/lib/postgresql/data': Operation not permitted
    chmod: changing permissions of '/var/run/postgresql': Operation not permitted
    Error: Database is uninitialized and superuser password is not specified.
           You must specify POSTGRES_PASSWORD to a non-empty value for the
           superuser. For example, "-e POSTGRES_PASSWORD=password" on "docker run".

           You may also use "POSTGRES_HOST_AUTH_METHOD=trust" to allow all
           connections without a password. This is *not* recommended.

           See PostgreSQL documentation about "trust":
           https://www.postgresql.org/docs/current/auth-trust.html
    ```

    Tässä on kahdenlaisia virheitä: kansio-oikeuksiin liittyviä ja puuttuvia muuttujia. Yritetään toistaa virhe paikallisesti koneella. Komento:

    ```sh
    docker run -it --rm -u 1000 postgres:latest
    chmod: changing permissions of '/var/lib/postgresql/data': Operation not permitted
    chmod: changing permissions of '/var/run/postgresql': Operation not permitted
    Error: Database is uninitialized and superuser password is not specified.
           You must specify POSTGRES_PASSWORD to a non-empty value for the
           superuser. For example, "-e POSTGRES_PASSWORD=password" on "docker run".

           You may also use "POSTGRES_HOST_AUTH_METHOD=trust" to allow all
           connections without a password. This is *not* recommended.

           See PostgreSQL documentation about "trust":
           https://www.postgresql.org/docs/current/auth-trust.html
    ```

    Yllä lisäsimme `-u 1000` vaihtaaksemme UID:n ei-root UID:ksi, jotta voimme toistaa saman virheen, jonka Rahti näyttää. Voidaan käyttää mitä tahansa satunnaista UID:tä; näin Rahti ajaa imaget (satunnaisilla UID:illa). Toistetaan määrittelemällä `POSTGRES_PASSWORD`-muuttuja, kuten ehdotettiin:

    ```sh
    $ podman run -it --rm -u 1000 -e  POSTGRES_PASSWORD=password postgres:latest
    WARN[0000] Error validating CNI config file /home/galvaro/.config/cni/net.d/4cat_default.conflist: [plugin firewall does not support config version "1.0.0"]
    chmod: changing permissions of '/var/lib/postgresql/data': Operation not permitted
    chmod: changing permissions of '/var/run/postgresql': Operation not permitted
    The files belonging to this database system will be owned by user "1000".
    This user must also own the server process.

    The database cluster will be initialized with locale "en_US.utf8".
    The default database encoding has accordingly been set to "UTF8".
    The default text search configuration will be set to "english".

    Data page checksums are disabled.

    fixing permissions on existing directory /var/lib/postgresql/data ... initdb: error: could not change permissions of directory "/var/lib/postgresql/data": Operation not permitted
    ```

    Tässä näemme, että tämä container-image ei toimi Rahtissa, koska sen pitäisi pystyä muuttamaan kansio-oikeuksia. Onneksi Rahti/Openshift tarjoaa PostgreSQL-mallin, joka on saatavilla Developer Catalogissa.

    ![Developer Catalog](../../img/db-developer-catalog.png)

    Mallin kuvauksessa on linkki Github-sivulle <https://github.com/sclorg/postgresql-container/>. Sieltä löytyy lista saatavilla olevista imageista. Valitsemme [quay.io/sclorg/postgresql-15-c9s](https://quay.io/repository/sclorg/postgresql-15-c9s), koska se on uusin versio ja pohjautuu CentOS 9:ään.

1. Kun kuvan (`postgres:latest`) korvaa `quay.io/sclorg/postgresql-15-c9s:latest`:lla, lokit ovat:

    ```sh
    $ oc logs db-747df6885c-sh289
    For general container run, you must either specify the following environment
    variables:
      POSTGRESQL_USER  POSTGRESQL_PASSWORD  POSTGRESQL_DATABASE
    Or the following environment variable:
      POSTGRESQL_ADMIN_PASSWORD
    Or both.

    To migrate data from different PostgreSQL container:
      POSTGRESQL_MIGRATION_REMOTE_HOST (hostname or IP address)
      POSTGRESQL_MIGRATION_ADMIN_PASSWORD (password of remote 'postgres' user)
    And optionally:
      POSTGRESQL_MIGRATION_IGNORE_ERRORS=yes (default is 'no')

    Optional settings:
      POSTGRESQL_MAX_CONNECTIONS (default: 100)
      POSTGRESQL_MAX_PREPARED_TRANSACTIONS (default: 0)
      POSTGRESQL_SHARED_BUFFERS (default: 32MB)

    For more information see /usr/share/container-scripts/postgresql/README.md
    within the container or visit https://github.com/sclorg/postgresql-container.
    ```

    Muuttujien nimet ovat erilaisia, mutta helposti käännettävissä. Otamme arvot `env`-`configMapista`:

    ```diff
           containers:
             - env:
    -            - name: POSTGRES_DB
    -            - name: POSTGRES_HOST_AUTH_METHOD
    -            - name: POSTGRES_PASSWORD
    -            - name: POSTGRES_USER
    -          image: 'postgres:'
    +          - name: POSTGRESQL_DATABASE
    +            valueFrom:
    +              configMapKeyRef:
    +                key: POSTGRES_DATABASE
    +                name: env
    +          - name: POSTGRESQL_PASSWORD
    +            valueFrom:
    +              configMapKeyRef:
    +                key: POSTGRES_PASSWORD
    +                name: env
    +          - name: POSTGRESQL_USER
    +            valueFrom:
    +              configMapKeyRef:
    +                key: POSTGRES_USER
    +                name: env
    +          image: 'quay.io/sclorg/postgresql-15-c9s'
               livenessProbe:
                 exec:
    ```

    Tämä viimeinen muutos tepsi, ja podi on nyt käynnissä odotetusti:

    ```sh
    $ oc get pods
    NAME                  READY   STATUS    RESTARTS   AGE
    db-58947cf497-p4vnq   1/1     Running   0          66s
    ```

### Backend-deployment { #backend-deployment }

Tämä deployment vaatii myös muutamia muutoksia. Käydään ne läpi hieman ketterämmin:

1. Korjaa imagen nimi. Virhe:

    ```sh
    $ oc get pods
    NAME                       READY   STATUS             RESTARTS   AGE
    backend-7f47d4c5d4-zrxjp   0/1     InvalidImageName   0          41s
    ```

    Ratkaisu:

    ```diff
                       key: workers
                       name: env
    -          image: 'digitalmethodsinitiative/4cat:'
    +          image: 'digitalmethodsinitiative/4cat:stable'
               name: 4cat-backend
               ports:
    ```

1. Lisää DB-service tämän virheen ratkaisemiseksi:

    ```sh
    db: forward host lookup failed: Unknown host
    ```

    Tämä edellyttää db-servicen luontia:

    ```sh
    $ oc expose deploy/db --port 5432
    service/db exposed
    ```

1. Seuraava virhe koskee salasana-autentikointia:

    ```
    Password for user fourcat:
    psql: error: connection to server at "db" (172.30.154.239), port 5432 failed: fe_sendauth: no password supplied
    ```

    Tämä johtuu siitä, että vaikka määrittelemme `POSTGRESQL_PASSWORD`, sovellus odottaa `PGPASSWPRD`-muuttujaa. Korjaus on:

    ```diff
                       key: POSTGRES_HOST_AUTH_METHOD
                       name: env
    -            - name: POSTGRES_PASSWORD
    +            - name: PGPASSWORD
                   valueFrom:
                     configMapKeyRef:
    ```

1. Backend-podin tuloste on nyt paljon pidempi, mutta päättyy tähän virheeseen:

    ```py
    During handling of the above exception, another exception occurred:

    Traceback (most recent call last):
      File "helper-scripts/migrate.py", line 336, in <module>
        finish(args, logger, no_pip=pip_ran)
      File "helper-scripts/migrate.py", line 122, in finish
        check_for_nltk()
      File "helper-scripts/migrate.py", line 74, in check_for_nltk
        nltk.download('punkt_tab', quiet=True)
      File "/usr/local/lib/python3.8/site-packages/nltk/downloader.py", line 774, in download
        for msg in self.incr_download(info_or_id, download_dir, force):
      File "/usr/local/lib/python3.8/site-packages/nltk/downloader.py", line 642, in incr_download
        yield from self._download_package(info, download_dir, force)
      File "/usr/local/lib/python3.8/site-packages/nltk/downloader.py", line 698, in _download_package
        os.makedirs(download_dir, exist_ok=True)
      File "/usr/local/lib/python3.8/os.py", line 223, in makedirs
        mkdir(name, mode)
    PermissionError: [Errno 13] Permission denied: '/nltk_data'
    ```

    Meidän on tehtävä kansiosta `/nltk_data` kirjoitettavissa oleva sovellusta ajavalle käyttäjälle. Palataan docker composeen — tätä kansiota ei ole mainittu. Koska kontit ovat tilattomia, kaikki tähän kansioon kirjoitettu data ei säily konttia käynnistettäessä uudelleen. Helpoin tapa on liittää [ephemeral storage](../storage/ephemeral.md) -kansio (eli `emptyDir`). Tämä on nopea tilapäinen tallennus, joka poistetaan, kun podi päättyy, sama käytös kuin docker composessa. Muutos on:

    ```diff
                   protocol: TCP
               volumeMounts:
    +            - mountPath: /nltk_data
    +              name: nltk-data
                 - mountPath: /usr/src/app/data
                   name: 4cat-data
    @@ -151,4 +153,6 @@
           restartPolicy: Always
           volumes:
    +        - name: nltk-data
    +          emptyDir: {}
             - name: 4cat-data
               persistentVolumeClaim:
    ```

1. Seuraava virhe liittyy taas ympäristömuuttujiin:

    ```py
    Creating config/config.ini file
    Traceback (most recent call last):
      File "/usr/local/lib/python3.8/runpy.py", line 194, in _run_module_as_main
        return _run_code(code, main_globals, None,
      File "/usr/local/lib/python3.8/runpy.py", line 87, in _run_code
        exec(code, run_globals)
      File "/usr/src/app/docker/docker_setup.py", line 88, in <module>
        update_config_from_environment(CONFIG_FILE, config_parser)
      File "/usr/src/app/docker/docker_setup.py", line 35, in update_config_from_environment
        config_parser['DATABASE']['db_password'] = os.environ['POSTGRES_PASSWORD']
      File "/usr/local/lib/python3.8/os.py", line 675, in __getitem__
        raise KeyError(key) from None
    KeyError: 'POSTGRES_PASSWORD'
    ```

    Tämä ympäristömuuttuja on kovakoodattu sovelluksen lähteeseen. Voisimme paikata koodin, mutta silloin pitäisi rakentaa image uudelleen ja paikata jokaisessa uudessa versiossa. Kustannustehokkain ratkaisu on määritellä muuttuja kahdesti. Muistat ehkä, että tämän luvun vaiheessa 3 vaihdoimme muuttujan nimen toista koodiosaa varten.

    ```diff
                       key: POSTGRES_PASSWORD
                       name: env
    +            - name: POSTGRES_PASSWORD
    +              valueFrom:
    +                configMapKeyRef:
    +                  key: POSTGRES_PASSWORD
    +                  name: env
                 - name: POSTGRES_PORT
                   valueFrom:
    ```

1. Etenemme, mutta emme ole vielä perillä. Uusi virhe:

    ```sh
    $ oc logs backend-7f9c9dbfbb-78sh8 -f
    Waiting for postgres...
    PostgreSQL started
    Database already created

               4CAT migration agent
    ------------------------------------------
    Interactive:             no
    Pull latest release:     no
    Pull branch:             no
    Restart after migration: no
    Repository URL:          https://github.com/digitalmethodsinitiative/4cat.git
    .current-version path:   config/.current-version
    Current Datetime:        2024-12-12 07:00:22

    WARNING: Migration can take quite a while. 4CAT will not be available during migration.
    If 4CAT is still running, it will be shut down now (forcibly if necessary).

    - No PID file found, assuming 4CAT is not running
    - Version last migrated to: 1.46
    - Code version: 1.46
      ...already up to date.

    Migration finished. You can now safely restart 4CAT.

    Creating config/config.ini file
    Created config/config.ini file

    Starting app
    4CAT is accessible at:
    http://localhost

    Starting 4CAT Backend Daemon...
    ...error while starting 4CAT Backend Daemon (pidfile not found).
    tail: cannot open 'logs/backend_4cat.log' for reading: No such file or directory
    tail: no files remaining

    ```

    Tämän ratkaisuun on kaksi tietä: voimme arvailla tai käyttää `oc debug` -työkalua. `oc debug` antaa käynnistää epäonnistuneen podin interaktiivisena sessioina ilman, että podin alkuperäinen komento käynnistetään.

    ```sh
    $ oc debug backend-7f9c9dbfbb-78sh8
    Starting pod/backend-7f9c9dbfbb-78sh8-debug-vcb6f, command was: docker/docker-entrypoint.sh
    Pod IP: 10.129.12.120
    If you don't see a command prompt, try pressing enter.

    $ ls logs
    4cat.stderr  lost+found  migrate-backend.log
    $ df -h
    Filesystem      Size  Used Avail Use% Mounted on
    overlay         1.2T  435G  766G  37% /
    tmpfs            64M     0   64M   0% /dev
    shm              64M     0   64M   0% /dev/shm
    tmpfs            22G   91M   22G   1% /etc/passwd
    /dev/sda4        90G   17G   73G  19% /nltk_data
    /dev/sdr        974M   24K  958M   1% /usr/src/app/data
    /dev/sds        974M   36K  958M   1% /usr/src/app/config
    /dev/sdq        974M  168K  958M   1% /usr/src/app/logs
    tmpfs           1.0G   24K  1.0G   1% /run/secrets/kubernetes.io/serviceaccount
    devtmpfs        4.0M     0  4.0M   0% /proc/keys
    $
    ```

    Näemme, että `logs`-kansio on persistent volume, eikä siellä ole lokitiedostoa. Ratkaisu voisi olla luoda tiedosto interaktiivisessa debug-istunnossa:

    ```sh
    $ touch logs/backend_4cat.log
    ```

    On erikoista, että sovellus ei itse luo tiedostoa ja että tämä ei ollut ongelma compose-lähestymistavassa. Se on epäilyttävää, mutta jatkamme ja katsomme, tuleeko siitä myöhemmin ongelma. Jotta nähdään, auttoiko korjaus, podi täytyy poistaa, jolloin uusi luodaan:

    ```sh
    $ oc get pods
    NAME                       READY   STATUS    RESTARTS        AGE
    backend-7f9c9dbfbb-78sh8   1/1     Running   7 (7m49s ago)   21m
    db-545945c9b8-tkbwc        1/1     Running   0               17h

    $ oc delete pod backend-7f9c9dbfbb-78sh8
    pod "backend-7f9c9dbfbb-78sh8" deleted

    ```

1. Katsotaan, epäonnistuuko podi yhä:

    ```sh
    $ oc get pods
    NAME                       READY   STATUS    RESTARTS   AGE
    backend-7f9c9dbfbb-sznxl   1/1     Running   0          3m22s
    db-545945c9b8-tkbwc        1/1     Running   0          17h
    ```

    Se on ollut käynnissä muutaman minuutin kaatumatta, mikä on hyvä. Mutta lokissa on uusi virhe, mikä ei ole hyvä:

    ```sh
    $ oc logs backend-7f9c9dbfbb-sznxl
    [...]
    Starting 4CAT Backend Daemon...
    ...error while starting 4CAT Backend Daemon (pidfile not found).
    ```

    Oletamme, että sovellus yrittää kirjoittaa PID-tiedoston (prosessi-ID:n sisältävä tiedosto, tyypillinen Unix-käytäntö) kansioon, johon voi kirjoittaa vain `root`. Tämä on tyypillinen virhe tällaisissa muunnoksissa. Lokissa ei kerrota, mihin PID-tiedosto pitäisi kirjoittaa, joten meidän on selvitettävä se itse. Koska podi on käynnissä, voimme käyttää `oc rsh` -komentoa avatakseen shellin käynnissä olevaan podiin:

    ```sh
    $ oc rsh deploy/backend
        $ grep 'pidfile not' -C 4 -nR *
        4cat-daemon.py-144-            else:
        4cat-daemon.py-145-                time.sleep(0.1)
        4cat-daemon.py-146-
        4cat-daemon.py-147-        if not pidfile.is_file():
        4cat-daemon.py:148:            print("...error while starting 4CAT Backend Daemon (pidfile not found).")
        4cat-daemon.py-149-            return False
        4cat-daemon.py-150-
        4cat-daemon.py-151-        else:
        4cat-daemon.py-152-            with pidfile.open() as infile:

        $ grep pidfile 4cat-daemon.py
        pidfile = config.get('PATH_ROOT').joinpath(config.get('PATH_LOCKFILE'), "4cat.pid")  # pid file location
        if pidfile.is_file():
            with pidfile.open() as infile:
    ```

    !!! Info "Grep-työkalu"
        Käytimme `grep`-työkalua virheviestin löytämiseksi koodista ja sitten uudelleen nähdäksemme, missä ja miten `pidfile`-muuttuja määriteltiin. Olisimme voineet käyttää myös paikallista tekstieditoria tai GitHub-hakua. `grep` on mielestäni erinomainen työkalu, josta jokainen hyötyy.

    Nyt tiedämme, että PID-tiedosto tallennetaan kansioon, jonka määrittää `PATH_LOCKFILE`-muuttuja. Tarkistetaan `config.ini`:

    ```sh
    $ oc rsh deploy/backend
        $ grep path -i config/config.ini
        [PATHS]
        path_images = data
        path_data = data
        path_lockfile = backend
        path_sessions = config/sessions
        path_logs = logs/
        $ ls -alh backend
        total 24K
        drwxr-xr-x. 1 root root  108 Oct 14 10:52 .
        drwxr-xr-x. 1 root root   30 Dec 12 07:22 ..
        -rw-r--r--. 1 root root  919 Oct 14 10:52 README.md
        -rw-r--r--. 1 root root   92 Oct 14 10:52 __init__.py
        -rw-r--r--. 1 root root 3.4K Oct 14 10:52 bootstrap.py
        -rw-r--r--. 1 root root 4.7K Oct 14 10:52 database.sql
        drwxr-xr-x. 2 root root  157 Oct 14 10:52 lib
        drwxr-xr-x. 2 root root 4.0K Oct 14 10:52 workers
    ```

    Tämä oli luultavasti monimutkaisimpia korjauksia ja vaati eniten arvausta. Ratkaisuna muutamme ensin konfiguraatiossa `path_lockfile`-arvoksi jonkin muun, esimerkiksi `pid`, joka kuvaa kansiota hyvin. Koska `config.ini` on volumessa, voimme muuttaa arvoa suoraan podissa (`sed -i 's#path_lockfile = backend#path_lockfile = pid#' config/config.ini`) tai kopioida tiedoston paikalliselle koneelle (katso `oc cp`), muokata sitä editorilla ja kopioida takaisin. Toiseksi lisäämme `pid`-kansion `emptyDir`:inä:

    ```diff
    @@ -150,4 +150,6 @@
                 - mountPath: /nltk_data
                   name: nltk-data
    +            - mountPath: /usr/src/app/pid
    +              name: pid
                 - mountPath: /usr/src/app/data
                   name: 4cat-data
    @@ -160,4 +162,6 @@
             - name: nltk-data
               emptyDir: {}
    +        - name: pid
    +          emptyDir: {}
             - name: 4cat-data
               persistentVolumeClaim:
    ```

1. Seuraava virhe on:

    ```sh
    $ oc logs backend-65cb8dc8dd-8thwg

    12-12-2024 12:40:44 | INFO at api.py:54: Could not open port 4444 yet ([Errno 99] Cannot assign requested address), retrying in 10 seconds
    12-12-2024 12:40:54 | INFO at api.py:54: Could not open port 4444 yet ([Errno 99] Cannot assign requested address), retrying in 10 seconds
    12-12-2024 12:41:04 | INFO at api.py:54: Could not open port 4444 yet ([Errno 99] Cannot assign requested address), retrying in 10 seconds
    12-12-2024 12:41:14 | INFO at api.py:54: Could not open port 4444 yet ([Errno 99] Cannot assign requested address), retrying in 10 seconds
    12-12-2024 12:41:24 | INFO at api.py:54: Could not open port 4444 yet ([Errno 99] Cannot assign requested address), retrying in 10 seconds
    12-12-2024 12:41:34 | INFO at api.py:54: Could not open port 4444 yet ([Errno 99] Cannot assign requested address), retrying in 10 seconds
    ```

    Tässä saamme tiedoston ja rivin, jossa virhe tapahtuu, `app.py` rivi 54. [app.py](https://github.com/uh-dcm/4cat_fi/blob/master/backend/workers/api.py#L50) oleelliset kohdat:

    ```py linenums="18"
      host = config.get('API_HOST')
      port = config.get('API_PORT')
    ```

    ```py linenums="47"
    while has_time:
			has_time = start_trying > time.time() - 300  # stop trying after 5 minutes
			try:
				server.bind((self.host, self.port))
				break
			except OSError as e:
				if has_time and not self.interrupted:
					self.manager.log.info("Could not open port %i yet (%s), retrying in 10 seconds" % (self.port, e))
					time.sleep(10.0)  # wait a few seconds before retrying
					continue
				self.manager.log.error("Port %s is already in use! Local API not available. Check if a residual 4CAT process may still be listening at the port." % self.port)
				return
			except ConnectionRefusedError:
				self.manager.log.error("OS refused listening at port %i! Local API not available." % self.port)
				return
    ```

    Rivi `50`:llä funktio yrittää sitoa portin annettuun isäntänimeen. Compose-lähestymistavassa hostname on `backend`, mutta Kubernetesissa podien nimet ovat (osittain) satunnaisia. Voisimme vaihtaa konfiguraation `backend` -> `0.0.0.0`, jolloin backend toimisi. Valitettavasti samaa config-tiedostoa käyttää myös frontend, ja ne jakavat saman volumen.

    !!! Error "Konfiguraatiot volumeissa"
        Konfiguraatioiden tallentaminen volumeen ja jakaminen eri deploymenttien kesken on huono käytäntö. Konfiguraatiotiedostoja ei tulisi muuttaa lennossa, ja eri deploymenteilla voi olla erilaiset konfiguraatiotarpeet.

    Tällaisissa sovelluksissa valitettavasti paras on muuttaa mahdollisimman vähän, jotta upstream-päivitykset pysyvät käytettävissä. Tässä yritämme kaksintaa config-volumen, yhden frontendille ja toisen backendille (ja "teeskentelemme, ettemme nähneet sitä"):

    ```sh
    $ cp 4cat-config-persistentvolumeclaim.yaml 4cat-config-front-persistentvolumeclaim.yaml

    $ diff 4cat-config-persistentvolumeclaim.yaml 4cat-config-front-persistentvolumeclaim.yaml -U 2
    --- 4cat-config-persistentvolumeclaim.yaml	2024-12-10 15:48:29.123813479 +0200
    +++ 4cat-config-front-persistentvolumeclaim.yaml	2024-12-12 15:55:41.207227320 +0200
    @@ -4,5 +4,5 @@
       labels:
         io.kompose.service: 4cat-config
    -  name: 4cat-config
    +  name: 4cat-config-front
     spec:
       accessModes:

    $ oc create -f 4cat-config-front-persistentvolumeclaim.yaml
    persistentvolumeclaim/4cat-config-front created
    ```

    Meidän on myös muokattava `env`-`configMapia`, koska backend ylikirjoittaa `config.ini`-tiedoston configMapista käynnistyessään (tästäkään en pidä):

    ```diff
     apiVersion: v1
     data:
    -  API_HOST: backend
    +  API_HOST: 0.0.0.0
       DOCKER_CONFIG_VOL: 4cat_4cat_config
       DOCKER_DATA_VOL: 4cat_4cat_data
    ```

    ```sh
    $ oc replace -f env-configmap.yaml
    configmap/env replaced

    ```

Tämän pitäisi olla kaikki tarvittavat muutokset backendiin:

  ```sh
  12-12-2024 14:03:30 | INFO at api.py:65: Local API listening for requests at 0.0.0.0:4444
  ```

### Frontend-deployment { #frontend-deployment }

Tämä on viimeinen palanen korjattavaksi.

1. Ennen frontendin deployausta vaihdetaan deployment-tiedostoon uusi volume:

    ```diff
    @@ -158,5 +168,5 @@
             - name: 4cat-config
               persistentVolumeClaim:
    -            claimName: 4cat-config
    +            claimName: 4cat-config-front
             - name: 4cat-logs
               persistentVolumeClaim:
    ```

1. Deployataan frontend ja katsotaan tulos:

    ```sh
    $ oc create -f frontend-deployment.yaml
    deployment.apps/frontend created

    $ oc get pods
    NAME                        READY   STATUS             RESTARTS   AGE
    backend-7f9c9dbfbb-sznxl    1/1     Running            0          125m
    db-545945c9b8-tkbwc         1/1     Running            0          19h
    frontend-6b99c94fff-fv5wd   0/1     InvalidImageName   0          2s
    ```

    ... tuttu virhe, tunnettu ratkaisu:

    ```diff
                       key: workers
                       name: env
    -          image: 'digitalmethodsinitiative/4cat:'
    +          image: 'digitalmethodsinitiative/4cat:stable'
               name: 4cat-frontend
               ports:
    ```

1. Nyt podi käynnistyy, mutta epäonnistuu yhdistämään backendiin:

    ```sh
    $ oc replace -f frontend-deployment.yaml
    deployment.apps/frontend replaced

    $ oc get pods
    NAME                       READY   STATUS    RESTARTS   AGE
    backend-7f9c9dbfbb-sznxl   1/1     Running   0          127m
    db-545945c9b8-tkbwc        1/1     Running   0          19h
    frontend-9ffbcf6b-wfg98    1/1     Running   0          4s

    $ oc logs frontend-9ffbcf6b-wfg98 -f
    Backend has not started - sleeping
    Backend has not started - sleeping
    Backend has not started - sleeping
    Backend has not started - sleeping
    Backend has not started - sleeping
    Backend has not started - sleeping
    Backend has not started - sleeping
    Backend has not started - sleeping
    Backend has not started - sleeping
    Backend has not started - sleeping
    Backend has not started - sleeping
    Backend has not started - sleeping
    ```

    Jos katsotaan frontendin config-kansiota (`/usr/src/app/config/`), se on tyhjä. Tämä on helppo korjata: kopioidaan config-tiedosto backend-kansiosta `oc cp`:llä:

    ```sh
    $ oc cp backend-65cb8dc8dd-nxq6p:config/config.ini config.ini
    ```

    Muokkaa tiedostoa korvaamalla `api_host` servicen nimellä:

    ```diff
         [API]
     api_port = 4444
    -api_host = 0.0.0.0
    +api_host = backend

     [PATHS]
    ```

    Kopioi muokattu tiedosto uuteen kansioon:

    ```sh
    $ oc cp config.ini frontend-79864b8548-pvh8z:config/
    ```

1. Tämän jälkeen saamme saman virheen kuin backendissä:

    ```py
    During handling of the above exception, another exception occurred:

    Traceback (most recent call last):
      File "/usr/local/lib/python3.8/runpy.py", line 185, in _run_module_as_main
        mod_name, mod_spec, code = _get_module_details(mod_name, _Error)
      File "/usr/local/lib/python3.8/runpy.py", line 111, in _get_module_details
        __import__(pkg_name)
      File "/usr/src/app/helper-scripts/migrate.py", line 336, in <module>
        finish(args, logger, no_pip=pip_ran)
      File "/usr/src/app/helper-scripts/migrate.py", line 122, in finish
        check_for_nltk()
      File "/usr/src/app/helper-scripts/migrate.py", line 74, in check_for_nltk
        nltk.download('punkt_tab', quiet=True)
      File "/usr/local/lib/python3.8/site-packages/nltk/downloader.py", line 774, in download
        for msg in self.incr_download(info_or_id, download_dir, force):
      File "/usr/local/lib/python3.8/site-packages/nltk/downloader.py", line 642, in incr_download
        yield from self._download_package(info, download_dir, force)
      File "/usr/local/lib/python3.8/site-packages/nltk/downloader.py", line 698, in _download_package
        os.makedirs(download_dir, exist_ok=True)
      File "/usr/local/lib/python3.8/os.py", line 223, in makedirs
        mkdir(name, mode)
    PermissionError: [Errno 13] Permission denied: '/nltk_data'
    ```

    Tämä ratkeaa samalla tavalla:

    ```diff
    @@ -145,4 +155,6 @@
                   protocol: TCP
               volumeMounts:
    +            - mountPath: /nltk_data
    +              name: nltk-data
                 - mountPath: /usr/src/app/data
                   name: 4cat-data
    @@ -153,4 +165,6 @@
           restartPolicy: Always
           volumes:
    +        - name: nltk-data
    +          emptyDir: {}
             - name: 4cat-data
               persistentVolumeClaim:
    ```

1. Lopulta frontend käynnistyy. Näemme, että se kuuntelee porttia `5000`, kuten odotettu:

    ```sh
    [2024-12-13 05:53:41 +0000] [35] [INFO] Starting gunicorn 23.0.0
    [2024-12-13 05:53:41 +0000] [35] [DEBUG] Arbiter booted
    [2024-12-13 05:53:41 +0000] [35] [INFO] Listening at: http://0.0.0.0:5000 (35)
    [2024-12-13 05:53:41 +0000] [35] [INFO] Using worker: gthread
    [2024-12-13 05:53:41 +0000] [37] [INFO] Booting worker with pid: 37
    [2024-12-13 05:53:41 +0000] [39] [INFO] Booting worker with pid: 39
    [2024-12-13 05:53:41 +0000] [41] [INFO] Booting worker with pid: 41
    [2024-12-13 05:53:41 +0000] [43] [INFO] Booting worker with pid: 43
    [2024-12-13 05:53:41 +0000] [35] [DEBUG] 4 workers
    ```

1. Mutta pian tulee käyttöoikeusvirhe:

    ```py
    PermissionError: [Errno 13] Permission denied: '/usr/src/app/webtool/static/css/colours.css'
    ```

    Kansiossa `/usr/src/app/webtool/static/css/` on oikeudet `drwxr-xr-x`. Tämä tarkoittaa, että vain omistaja (`root`) voi _kirjoittaa_ sinne. `emptyDir`-kikka ei toimi tällä kertaa, koska kansio ei ole tyhjä alkuperäisessä imagessa:

    ```sh
    root@5878384231b
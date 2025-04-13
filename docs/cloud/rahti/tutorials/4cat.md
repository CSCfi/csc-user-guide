Here is the translated content from English to Finnish, applying the requested guidelines:

```markdown
!!! error "Edistynyt taso"
    Sinun on hallittava Linux, Docker, Docker Compose ja Kompose. Python-osaaminen on plussaa. 
    Rahtin osalta suosimme OpenShift CLI -työkalun [oc](../usage/cli.md) käyttöä.

# Kuinka käyttää 4catia Rahtissa {#how-to-deploy-4cat-in-rahti}

Tässä opetusohjelmassa on kyse pitkästä muodosta: se selittää kaikki eri vaiheet, jotka tarvittiin [4cat_fi](https://github.com/uh-dcm/4cat_fi) -sovelluksen käyttöönottoon Rahtissa. Ideana on selittää, miten eri ongelmat löydettiin ja ratkaistiin. Jokaisella ongelmalla on oma kappaleensa ja toivottavasti ratkaisu on helppo soveltaa mihin tahansa muuhun sovellukseen samanlaisin oirein. Jätämme pois joitakin vääriä ratkaisuja ja johtolankoja, joita seurasin, kun yritin alun perin asentaa sovelluksen, jotta tämä opetusohjelma ei kasvaisi eksponentiaalisesti. Mutta pidä mielessä, että tällaiset prosessit ovat harvoin suoraviivaisia ja että ratkaisun löytämiseksi löydät yleensä paljon ei-ratkaisuja.

4Cat on tallennus- ja analyysityökalu. Yllä linkitetyn GitHub-sivun mukaan opimme, että työkalua käytetään sosiaalisen median alustojen analysointiin ja että yksi asennusmenetelmistä on docker compose. Tämä on hyvä uutinen, koska:

1. Voimme testata sovelluksen käyttöönottoa docker compose avulla ja nähdä miltä se näyttää.
1. Meidän ei tarvitse luoda docker-konttia alusta alkaen.
1. Voimme käyttää docker compose käyttöönottoa pohjana ja mukauttaa sen Kubernetes-käyttöön [kompose](https://kompose.io)-työkalun avulla. Tämä työkalu on erityisesti suunniteltu tekemään nämä muunnokset. Heidän verkkosivustoltaan: "Muunnot eivät aina ole 1:1 Docker Composesta Kubernetesiin, mutta autamme pääsemään 99% sinne!". Ja se todella säästää meille paljon vaivalloista muunnosaikaa, mutta ei lopettaa sitä tähän.

!!! warning "Linux 🐧 käytetään kaikissa esimerkeissä"
    Olemme valmistaneet tämän opetusohjelman käyttämällä Linux-konetta. Periaatteessa, pienellä mukautuksella kaikki nämä komennot toimivat myös Windowsissa ja Macissä, mutta jos olet ymmällä, suosittelen asentamaan pienen VM:n Poutaan](../../pouta/launch-vm-from-web-gui.md) ja käyttämään sitä opetusohjelman seuraamisessa. Tämä on hyödyllistä jopa Linux-käyttäjille, sillä pystyt asentamaan, poistamaan tai muuttamaan ohjelmistoa vaarantamatta paikallista asennustasi.

## Docker compose {#docker-compose}

1. Ennen jatkamista tarvitsemme dockerin ja docker compose pluginin asennettuna. Löydät ohjeet docker composen asentamiseen täältä:

    - <https://docs.docker.com/compose/install/>

    Debian- ja Ubuntu-käyttöjärjestelmiin voit asentaa sen seuraavasti:

    ```sh
    sudo apt-get update
    sudo apt-get install docker.io docker-compose
    ```

    !!! Info "Vaihtoehdot dockerille 🐋"
        Voit käyttää myös podman composea tai vastaavaa, mutta me käytämme dockeria, sillä se on yleisin työkalu.

1. Kun docker compose on asennettu, otetaan 4cat käyttöön ja katsotaan, miltä se näyttää ja miten se toimii. Sinun tulee kloonata arkisto ja ajaa docker-compose kloonatussa kansiossa:

    ```sh
    git clone https://github.com/uh-dcm/4cat_fi
    cd 4cat_fi
    sudo docker compose up
    ```

    Tämä käynnistää sovelluksen käyttöönoton koneella. Voi viedä jonkin aikaa ladattavaksi kuvat ja konfiguroitava sovellus. Jos painat `Ctrl+C`, sovellus sulkeutuu. Jos haluat käyttää sitä taustalla, sinun on vain lisättävä `-d` tai `--detach` docker-compose-komentoon.

    ![docker-compose tuloste](../../img/4cat-docker-compose.png)

    Jonkin ajan kuluttua sovellus on käytettävissä portissa `80` (`PUBLIC_PORT`):

    ![4cat ensimmäinen ajo](../../img/4cat.png)

### Analyysi {#analysis}

[docker-compose.yml](https://github.com/digitalmethodsinitiative/4cat/blob/master/docker-compose.yml) tiedosto on seuraava:

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
      - ${PUBLIC_PORT}:5000
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

Käydään myös läpi [.env](https://github.com/uh-dcm/4cat_fi/blob/master/.env) tiedosto:

```ini
# 4CAT Versio: Päivitä viimeisimmällä julkaisusivutäkillä tai 'latest'
# https://hub.docker.com/repository/docker/digitalmethodsinitiative/4cat/tags?page=1&ordering=last_updated
DOCKER_TAG=stable
# Voit valita Postrgres Docker-kuvamerkinnät täältä tarpeidesi mukaan: https://hub.docker.com/_/postgres
POSTGRES_TAG=latest

# Tietokannan asetus
POSTGRES_USER=fourcat
POSTGRES_PASSWORD=supers3cr3t
POSTGRES_DB=fourcat
POSTGRES_HOST_AUTH_METHOD=trust
# POSTGRES_HOST tule olla tietokantapalvelimen nimi, joka on asetettu docker-compose.yml-tiedostossa
POSTGRES_HOST=db
POSTGRES_PORT=5432  # Docker postgres-kuva käyttää porttia 5432

# Palvelininformaatio
# SERVER_NAME käytetään vain ensimmäisellä käynnistyksellä; sen jälkeen sen voi asettaa frontendissä
SERVER_NAME=localhost
PUBLIC_PORT=80

# Backend API
# API_HOST käyttää frontend; Dockerissa sen tulisi olla backend-palvelimen nimi
# (tai "localhost", jos front- ja backend toimivat yhdessä yksi kontissa)
API_HOST=backend
PUBLIC_API_PORT=4444

# Telegram tarvitsee ilmeisesti oman porttinsa
TELEGRAM_PORT=443

# Docker-tilauksen nimiä
DOCKER_DB_VOL=4cat_4cat_db
DOCKER_DATA_VOL=4cat_4cat_data
DOCKER_CONFIG_VOL=4cat_4cat_config
DOCKER_LOGS_VOL=4cat_4cat_logs

# Gunicorn-asetukset
worker_tmp_dir=/dev/shm
workers=4
threads=4
worker_class=gthread
log_level=debug
```

Kuten näette, tämä `docker-compose.yml`-tiedosto on [YAML](https://en.wikipedia.org/wiki/YAML) -tiedosto, joka sisältää kaksi pääosaa: `services` ja `volumes`. Palveluita on 3 ja volyymia 4. Kubernetesissa tämä tarkoittaa 3 `Deployments` -sovellusta ja 4 `PersistentVolumeClaim`-ratkaisua (PVC). Palvelun tärkeimmät kentät ovat:

- `image` on kuva, joka dockerin täytyy ladata ja ajaa jokaiselle palvelulle. Meidän tapauksessa meillä on kaksi erilaista kuvaa, `postgres` (tunnettu tietokanta) ja `4cat_fi`. `Frontend` ja `backend` käyttävät samaa kuvaa, mutta niillä on eri komento/käynnistyskohta. Koska docker compose toimii, tiedämme, että molemmat kuvat ovat olemassa ja voidaan ladata ilman ongelmia.
- `environment` ja `env_file` määrittelevät ympäristömuuttujat, jotka konfiguroivat palvelut. Esimerkiksi `POSTGRES_PASSWORD` käytetään tietokannan salasanan välittämiseen.
- `volumes`-kohta kertoo dockerille, mitkä volyymit tulee liittää palveluun ja mihin kansioon ne pitää kiinnittää.
- `ports` kertoo meille julkiset portit, sisäiset portit ja kartoituksen niiden välillä. Merkintä on `<ulkoportti>:<sisäportti>`.
- `entrypoint` ja `command` ovat komennot, jotka suoritetaan, kun kuva käynnistetään. Postgres ei ole esitteen niiden puuttuessa, koska käytämme oletus `commands`/`entrypoints` joka on määritelty kuvaan.

Volyymit-osio on yksinkertaisempi ja sisältää vain nimiä. Docker compose `volume` on normaali docker-volyymi eikä sisällä kokoa. Tämä johtuu siitä, että se käyttää paikallista levyä, ja koko on paikallisen levyn rajoitus. Kubernetesissa volyymit ovat määritelty kokoa ja meidän täytyy ottaa se huomioon, kun teemme muunnoksia.

`env`-tiedosto sisältää oletusarvot sovelluksen käyttöönotolle. Esimerkiksi `PUBLIC_PORT` on asetettu `80`:lle.

## Kompose {#kompose}

Kompose sallii meille `docker-compose.yaml`-tiedoston kääntämisen joukkoon Kubernetes-YAML-tiedostoja.

1. Meidän täytyy asentaa [kompose](https://kompose.io/). Seuraa ohjeita täältä:

    - <https://kompose.io/installation/>

    Koska meillä on jo docker asennettuna, voimme seurata docker-metodia, joka rakentaa kuvan lähdekoodista:

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

1. Sinulla pitäisi olla muutamia uusia tiedostoja luotuna:

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

### Analyysi {#analysis-kompose}

Työkalu on luonut neljäntyyppisiä tiedostoja: `service`, `deployment`, `configmap` ja `persistentvolumeclaim`. Aloitetaan yksinkertaisimmista:

- `persistentvolumeclaim`-tiedostot ovat volyymien määritelmiä. Jokaiselle `docker-compose.yml`-tiedoston määrittelylle on olemassa yksi tiedosto. Katsotaanpa esimerkkiä ja merkityksellisiä rivejä:

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

    Voimme nähdä, että `name` on pidetty samanlaisena kuin compose-määritelmässä (löytyy `metadata > name`). `accessMode` on asetettu arvolle `ReadWriteOnce`, mikä tarkoittaa, että volyymi voidaan kiinnittää vain kerran. Lopuksi koko on asetettu oletukselle `100Mi` (löytyy `spec > resources > request > storage`).

- `configmap`-tiedosto(t) säilyttävät konfiguraation. Meidän tapauksessamme (ei docker compose -spesifiset) .env-määritellyt muuttujat on käännetty `env-configmap.yaml`-tiedostoksi. `name` on asetettu arvoon `env` ja muuttujat on määritelty kohdassa `data`.

- `service`-tiedostot määrittelevät "vakaita verkkotunnisteita", jotka toimivat kuormantasaajana. Palvelu luodaan jokaiselle `deployment`-sovellukselle, ja se julkaisee kaikki portit, jotka käyttöön otettu sovellus tarjoaa. Esimerkiksi tiedostossa `frontend-service.yaml`:

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

    Kaksi tärkeää osaa ovat `selector` ja `ports`. Ensimmäinen yhdistää palvelun käyttöönottotiedostoon ja toinen listaa, mitkä portit tämä palvelu julkaisee. Lisätietoa [palveluista](../networking.md#services).

- `deployment` on monimutkaisin luotu kokoonpano. Voimme yrittää kartoittaa `docker-compose.yaml`-tiedoston kokoonpanoa näihin tiedostoihin. Esimerkiksi lyhimmän luodun:

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

    - `image` on määritelty kohdassa `spec > template > spec > containers > image`, tässä tapauksessa `postgres:`. Tämä on virhe, sillä tunniste `latest` puuttuu, korjaamme tämän myöhemmin.
    - `environment` on määritelty kohdassa `spec > template > spec > containers > env`, arvot myös puuttuvat.
    - `volumes` on määritelty kohdassa `spec > template > spec > volumes` ja `spec > template > spec > containers > volumeMounts`.
    - `ports` ovat määritettyinä vastaavissa `service`-tiedostoissa ja `spec > template > spec > containers > ports`.
    - Lopuksi `command` on määritelty kohdassa `spec > template > spec > containers > command` (näet sen esimerkiksi kohdassa `backend-deployment.yaml`).

    Kuten huomaat, luodut YAML-tiedostot eivät ole täydellisiä, mutta soveltuvat pohjaksi käytön jatkamiseen.

## Käyttöönotto Rahtiin {#deployment-to-rahti}

Käytämme kaikkia nykyisiä muuttumattomia YAML-tiedostoja ja otamme ne käyttöön yksi kerrallaan. Ensinnäkin sinun pitäisi [asentaa oc](../usage/cli.md#how-to-install-the-oc-tool) ja [kirjautua Rahtiin](../usage/cli.md#how-to-login-with-oc). Sitten sinun täytyy [luoda Rahti-projekti](../usage/projects_and_quota.md#creating-a-project). Varmista lopuksi, että olet oikeassa projektissa: `oc project <project_name>`.

### Volyymit, ConfigMaps ja Palvelut {#volumes-configmaps-and-services}

Nämä 3 tyyppiä ovat suoraviivaisia ja niiden ei pitäisi aiheuttaa ongelmia.

1. Voimme aloittaa luomalla `volumes` yksi kerrallaan:

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

    Tämä luo 4 volyymiä tilassa `Pending`. Ne pysyvät `Pending`-tilassa, kunnes otamme käyttöön `deployments`. Tämä on odotettua.

1. Luomme myös `configMap`-ohjelman:

    ```sh
    $ oc create -f env-configmap.yaml
    configmap/env created

    $ oc get cm
    NAME                       DATA   AGE
    env                        22     5s
    kube-root-ca.crt           1      5m45s
    openshift-service-ca.crt   1      5m45s
    ```

    Muut kaksi merkintää (`kube-root-cs.crt` ja `openshift-service-ca.crt`) ovat valmiiksi luotuja Kubernetes- ja Openshift-pohjaisia config-map:ja.

1. Emme odota mitään virheitä luodessamme `services`-tiedostoja (db-palvelu puuttuu, koska docker compose -tiedostossa ei mainittu mitään portteja, ja meidän täytyy luoda se manuaalisesti myöhemmin):

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

    Tulos on odotettu backendille, kartoitus oli `4444:4444`. Kuitenkin frontendille se oli `80:5000`. Tämä ei ole iso asia, koska Rahtista ulospääsyyn käytämme `Route`-ohjelmaa, ja `Route` sallii minkä tahansa portin muuttamisen standardiksi 80/443-portiksi. Annamme sen olla sellaisenaan.

### DB-käyttöönpanot {#db-deployments}

Lopulta luomme käyttöönpanot. Meillä on 3 käyttöönpanoa ja aloitamme DB-käyttöönpanolla.

1. Luodaan nykyinen mitä meillä on:

    ```sh
    $ oc create -f db-deployment.yaml
    deployment.apps/db created

    $ oc get pods
    NAME                  READY   STATUS             RESTARTS   AGE
    db-66db46fb89-vzqrz   0/1     InvalidImageName   0          26s
    ```

1. Tämä on odotettua, sillä tunniste `latest` puuttui kuvan nimestä. Korjataan se ja yritetään uudelleen. Muokataan `db-deployment.yaml`-tiedostoa ja lisätään `latest` kuvan arvoon niin, että se näyttää seuraavalta: `postgres:latest`,

    ```diff
                 - name: POSTGRES_USER
    -          image: 'postgres:'
    +          image: 'postgres:latest'
               livenessProbe:
                 exec:
    ```

    ja luodaan/korvataan käyttöönotto:

    ```sh
    $ oc replace -f db-deployment.yaml
    deployment.apps/db replaced

    $ oc get pods
    NAME                  READY   STATUS              RESTARTS   AGE
    db-76fcbdc9d8-dgmqr   0/1     CrashLoopBackOff    1 (1s ago)   24s
    ```

    !!! Info "YAML-tiedostot"
        Teemme muutoksia `YAML`-tiedostoihin, jotta voimme luoda koko käyttöönoton jälkeenpäin uudelleen. Voit myös lisätä tiedostot Git-arkistoon ja liittää jokaista muutosta, jotta myöhemmin muutokset ja niiden syyt ovat historian ja syiden suhteen selkeitä.

1. Käyttöönotto ei toimi, mutta eri syystä. Katsotaan miksi:

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

    Tämä osoittaa kahdenlaista virhettä: kansion käyttöoikeusvirheet ja puuttuvat muuttujat. Yritetään toistaa virhe omalla koneellamme. Komento tulee olemaan:

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

    Esimerkissä lisäsimme `-u 1000` muuttaaksemme käyttäjätunnusta satunnaiseksi, ja samalla jäljittelemme samaa virhettä, jota Rahti näyttää meille. Mikä tahansa satunnaistunnus voi toimia, sillä Rahti ajaa kuvia (ajaen ne satunnaisilla tunnuksilla). Kokeillaan uudelleen määrittämällä muuttuja `POSTGRES_PASSWORD` esitettynä:

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

    Tässä tapauksessa näemme, että tämä konttikuvan ei koskaan tule toimimaan Rahtissa, koska sen täytyy pystyä muuttamaan kansio-oikeuksia. Onneksi Rahti/Openshift tarjoaa PostgreSQL-mallin, joka on saatavilla kehittäjäkatalogista.

    ![Kehittäjäkatalogi](../../img/db-developer-catalog.png)

    Kuvauksen perusteella näemme linkin sivustolle <https://github.com/sclorg/postgresql-container/>. Sivulta saatavilla olevien kuvien listalukemisella valitsemme [quay.io/sclorg/postgresql-15-c9s](https://quay.io/repository/sclorg/postgresql-15-c9s), sillä se on uusin saatavilla oleva versio ja käyttää Centos 9 ohjelmapohjana.

1. Kuvan korvaamisen jälkeen (`postgres:latest` korvataan `quay.io/sclorg/postgresql-15-c9s:latest`) lokit ovat seuraavat:

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

    Muuttujanimet ovat erilaiset, mutta helppo kääntää. Käytämme myös `env` `configMap`-arvoja:

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

    Tämä viimeinen muutos toimi ja Pod on nyt käynnissä odotetusti:

    ```sh
    $ oc get pods
    NAME                  READY   STATUS    RESTARTS   AGE
    db-58947cf497-p4vnq   1/1     Running   0          66s
    ```

### Backend-käyttöönotto {#backend-deployment}

Tämä käyttöönotto tarvitsee myös muutamia muutoksia. Käydään läpi ne toivottavasti nopeammin:

1. Korjaus kuvan nimelle. Virhe:

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

1. Lisää DB-palvelu tämän ongelman ratkaisemiseksi:

    ```sh
    db: forward host lookup failed: Unknown host
    ```

    Tämä vaatii meitä luomaan db-palvelun:

    ```sh
    $ oc expose deploy/db --port 5432
    service/db exposed
    ```

1. Seuraava virhe liittyy salasanan käyttöön:

    ```
    Password for user fourcat:
    psql: error: connection to server at "db" (172.30.154.239), port 5432 failed: fe_sendauth: no password supplied
    ```

    Tämä johtuu siitä, että samalla kun määrittelemme `POSTGRESQL_PASSWORD`, sovellus odottaa `PGPASSWPRD`:ia. Tämä tarkoittaa, että ratkaisu on:

    ```diff
                       key: POSTGRES_HOST_AUTH_METHOD
                       name: env
    -            - name: POSTGRES_PASSWORD
    +            - name: PGPASSWORD
                   valueFrom:
                     configMapKeyRef:
    ```

1. Backend-podin tulostus on nyt paljon pidempi, mutta se päätyy tähän virheeseen:

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

    Meidän on tehtävä kansio `/nltk_data` kirjoitettavaksi käyttäjälle, joka ajaa sovellusta. Jos palaamme tarkastamaan docker compose -tiedoston, tätä kansiota ei mainittu. Koska kontit ovat tilattomia, tämä tarkoittaa, että kaikki tiedot, jotka kirjoitetaan kansioon, eivät selviä kontin uudelleenkäynnisty
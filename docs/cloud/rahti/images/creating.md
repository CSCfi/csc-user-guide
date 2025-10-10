On useita syitä tehdä oma Docker-kuva, mutta yleisimmin kaksi. Joko haluamallesi sovellukselle ei ole saatavilla Docker-kuvaa, tai kuva on saatavilla, mutta se ei toimi OpenShiftissä. Koska OpenShift on suunniteltu jaetuksi klusteriksi, jossa eri tiimien käyttäjät ajavat sovelluksia samalla laitteistolla, OpenShift joutuu asettamaan rajoituksia ja toimimaan eri tavalla kuin tavallinen Kubernetes-klusteri.

Rahtin rekisterissä on 5 Gt:n kokoraja kuville. Mitä suurempi kuva on, sitä huonompi on käyttökokemus sen kanssa. Sen noutaminen kestää kauemmin, ja se täyttää solmun kuvavälimuistin nopeammin. Yli 1 Gt:n kuvaa pidetään jo erittäin suurena. Katso artikkeli aiheesta [keeping docker images small](keeping_docker_images_small.md)

## Kuvien rakentaminen paikallisesti { #building-images-locally }

Tässä esimerkissä käytämme [virallista nginx-kuvaa](https://hub.docker.com/_/nginx), joka on rakennettu [Alpine Linux](https://www.alpinelinux.org/) -jakelun päälle, ja teemme tarvittavat muutokset, jotta se toimii OpenShiftissä.

Paikallisesti kuvan rakentamiseen tarvitaan kolme vaihetta.

* Ensin on kirjoitettava `Dockerfile`, esimerkiksi tällainen:

```Dockerfile
FROM nginx:alpine

# support running as arbitrary user which belongs to the root group
RUN chmod g+rwx /var/cache/nginx /var/run /var/log/nginx && \
    chown nginx.root /var/cache/nginx /var/run /var/log/nginx && \
    # users are not allowed to listen on privileged ports
    sed -i.bak 's/listen\(.*\)80;/listen 8081;/' /etc/nginx/conf.d/default.conf && \
    # Make /etc/nginx/html/ available to use
    mkdir -p /etc/nginx/html/ && chmod 777 /etc/nginx/html/ && \
    # comment user directive as master process is run as user in OpenShift anyhow
    sed -i.bak 's/^user/#user/' /etc/nginx/nginx.conf

WORKDIR /usr/share/nginx/html/
EXPOSE 8081

USER nginx:root
```

Tämä `Dockerfile`:

 1. Antaa kirjoitusoikeudet `root`-ryhmälle (ei `root`-käyttäjälle) useisiin kansioihin, joihin nginxin on kirjoitettava (/var/cache/nginx, /var/run, /var/log/nginx ja /etc/nginx/html/). Sovelluksia ajetaan satunnaisella käyttäjällä ja `root`-ryhmällä.
 2. Muuttaa portin, jota nginx kuuntelee, sillä vain root saa kuunnella etuoikeutettuja portteja (<1024).
 3. Ja lopuksi kommentoi `user`-määritysdirektiivin.

 Alkuperäisessä `nginx:alpine`-kuvassa on 5 kerrosta, ja lisäämme uuden (`RUN`).

Yksinkertaisempi `Dockerfile`-esimerkki voisi olla:

```Dockerfile
FROM alpine

RUN apk add git
```

Tämä vain asentaa gitin Alpineen ja lisää samalla uuden kerroksen.

Katso [Dockerfile](https://docs.docker.com/engine/reference/builder/)-viitedokumentaatio.

Seuraavalla komennolla rakennetaan kuva `docker.io/user/name:tag`:

```bash
docker build . -t docker.io/user/name:tag
```

Ja lopuksi kuvan julkaisu:

```bash
docker push docker.io/user/name:tag
```

## Rahtin käyttäminen konttikuvien rakentamiseen { #using-rahti-to-build-container-images }

Alla olevat menetelmät käyttävät Rahtia kuvien rakentamiseen.

### Paikallisen kansion käyttäminen rakentamiseen { #using-a-local-folder-for-building }

Tällä menetelmällä voi rakentaa kuvan käyttämällä paikallista kansiota, joka sisältää Dockerfilen ja muut projektissa tarvittavat tiedostot. Tämä on hyödyllistä, kun Rahtin ei ole mahdollista tai tarkoituksenmukaista kloonata repositoriota suoraan.

Tämä edellyttää, että olet valtuuttanut Rahti-komentorivisession ja luonut projektin Rahtiin. Ohjeet tähän löytyvät luvusta [Command line tool usage](../usage/cli.md#cli-cheat-sheet).

Steps:

Luo Rahti-kohtaiset määritykset `oc new-build` -komennolla. Varmista, ettet ole git-versionhallinnan alaisessa hakemistossa:

```bash
$ oc new-build --to=my-hello-image:devel --name=my-hello --binary
    * A Docker build using binary input will be created
      * The resulting image will be pushed to image stream tag "my-hello-image:devel"
      * A binary build was created, use 'start-build --from-dir' to trigger a new build

--> Creating resources with label build=my-hello ...
    imagestream.image.openshift.io "my-hello-image" created
    buildconfig.build.openshift.io "my-hello" created
--> Success
```

Tarvitset sitten `Dockerfile`-tiedoston; voit käyttää mitä tahansa aiemmista esimerkeistä tai jotain muuta sopivaa. Kertoaksesi OpenShiftille, että kuva pitää rakentaa, siirry (`cd`) kansioon, jossa `Dockerfile` sijaitsee, ja käynnistä rakentaminen `oc start-build` -komennolla. Se ottaa mukaan kaikki nykyisen hakemiston tiedostot ja tulostaa rakennusprosessin paikalliseen terminaaliin:

```bash
oc start-build my-hello --from-dir=./ -F
```

Kuva on nähtävissä internetissä osoitteessa
`image-registry.apps.2.rahti.csc.fi/<project-name>/my-hello-image:devel` docker-yhteensopiville asiakkaille, mutta sinun on ensin todennettava, jotta voit noutaa sen.

Komentorivikäytössä docker-yhteensopivien asiakkaiden kanssa docker-repositorion salasanana toimii käyttöoikeustunnus, joka näytetään Rahti-komentorivisession valtuutuksen yhteydessä, ja käyttäjänimi voi olla `unused`.

```sh
docker login -u g -p $(oc whoami -t) image-registry.apps.2.rahti.csc.fi
```

### Source to Image -mekanismin käyttäminen { #using-the-source-to-image-mechanism }

OpenShift mahdollistaa koodin rakentamisen ja käyttöönoton ilman `Dockerfilea`. Tätä kutsutaan Source to Imageksi eli `s2i`:ksi. Sitä käytetään ajamalla `oc new-app URL#branch`, jossa `#branch` on valinnainen. Esimerkiksi käytä virallista python-esimerkkikoodia:

```bash
$ oc new-app https://github.com/CSCfi/nodejs-16-rahti-example.git
--> Found Docker image 9d200cd (7 weeks old) from Docker Hub for "node:16.15.0"

    * An image stream tag will be created as "node:16.15.0" that will track the source image
    * A Docker build using source code from https://github.com/CSCfi/nodejs-16-rahti-example.git will be created
      * The resulting image will be pushed to image stream tag "nodejs-16-rahti-example:latest"
      * Every time "node:16.15.0" changes a new build will be triggered
    * This image will be deployed in deployment config "nodejs-16-rahti-example"
    * Port 8080/tcp will be load balanced by service "nodejs-16-rahti-example"
      * Other containers can access this service through the hostname "nodejs-16-rahti-example"
    * WARNING: Image "node:16.15.0" runs as the 'root' user which may not be permitted by your cluster administrator

--> Creating resources ...
    imagestream.image.openshift.io "node" created
    imagestream.image.openshift.io "nodejs-16-rahti-example" created
    buildconfig.build.openshift.io "nodejs-16-rahti-example" created
    deploymentconfig.apps.openshift.io "nodejs-16-rahti-example" created
    service "nodejs-16-rahti-example" created
--> Success
    Build scheduled, use 'oc logs -f bc/nodejs-16-rahti-example' to track its progress.
    Application is not exposed. You can expose services to the outside world by executing one or more of the commands below:
     'oc expose svc/nodejs-16-rahti-example' 
    Run 'oc status' to view your app.
```

Tee sitten kuten ehdotetaan ja julkaise uusi sovellus ulkomaailmaan:

```bash
$ oc expose svc/nodejs-16-rahti-example
route.route.openshift.io/nodejs-16-rahti-example exposed
```

Saat uuden reitin isäntänimen komennolla:

```bash
oc get route nodejs-16-rahti-example
```

Jos syötät isäntänimen selaimeen, näet "Hello World!" -viestin.

Uuden rakennuksen voi käynnistää komentoriviltä:

```bash
oc start-build nodejs-16-rahti-example
```

Tai käyttämällä [webhooks](../tutorials/webhooks.md)

### Inline-Dockerfile-menetelmän käyttäminen { #using-the-inline-dockerfile-method }

On mahdollista luoda uusi build käyttäen komentorivillä annettua Dockerfilea. Tällöin itse `Dockerfile` upotetaan Build-objektiin, joten erillistä Git-repositoriota ei tarvita.

```bash
oc new-build -D $'FROM almalinux:10'
```

Tässä esimerkissä rakennamme kuvan, joka on kopio `AlmaLinux 10`:stä.

On myös mahdollista luoda build annetusta `Dockerfile`-tiedostosta:

```bash
cat Dockerfile | oc new-build -D -
```

### Tuonti Gitistä (yksityiset repositoriot) Web-käyttöliittymällä { #import-from-git-private-repositories-using-the-web-gui }

Yksityisen Git-repositorion käyttöönotto Rahtiin edellyttää tarvittavan todennuksen asettamista, jotta pääsy yksityiseen repositorioosi onnistuu. Ilman asianmukaista todennusta näet virheen "URL is valid but cannot be reached" (näkyy alla olevissa kuvissa). Näin ratkaiset ongelman kahdella todennusmenetelmällä:

![oie_1671443U3OLpFT1](https://github.com/user-attachments/assets/a844e224-769e-4d9f-bba2-043ad5c9b258)

#### Vaihtoehto 1: Tokenin käyttäminen Git-todennukseen { #option-1-using-a-token-for-git-authentication }

1. Luo henkilökohtainen käyttöoikeustunnus (Personal Access Token):

    - GitHub:
         - Siirry GitHub-tilisi asetuksiin.
         - Valitse "Developer settings" > "Personal access tokens".
         - Napsauta "Generate new token".
         - Valitse tarvitut oikeudet (tyypillisesti tarvitset `repo`-oikeuden yksityisiin repositorioihin).
         - Luo token ja kopioi se.

    - GitLab:
         - Siirry GitLab-profiilisi asetuksiin.
         - Valitse "Access Tokens".
         - Anna tokenille nimi, valitse tarvittavat oikeudet (esim. `api`, `read_repository`) ja luo token.
         - Kopioi token.

3. Lisää token Rahtiin:
    - Kohdassa "Source Secret" valitse "Create new Secret"
    - Nimeä salaisuus, kohdassa "Authentication type" valitse "Basic Authentication"
    - Liitä token ja luo

![oie_1672121lETtYQ6J](https://github.com/user-attachments/assets/4bd9450f-170b-4a9e-ae8c-df4700fb0be4)

#### Vaihtoehto 2: Yksityisen SSH-avaimen käyttäminen Git-todennukseen { #option-2-using-a-private-ssh-key-for-git-authentication }

1. Luo SSH-avainpari (jos sinulla ei vielä ole sellaista):

    - Avaa terminaali ja suorita seuraava komento luodaksesi uuden SSH-avainparin:
         ```sh
         ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
         ```
    - Tämä luo kaksi tiedostoa: yksityisen avaimen (`id_rsa`) ja julkisen avaimen (`id_rsa.pub`).

2. Lisää julkinen avaimesi Git-palveluun:

    - GitHub:
        - Siirry GitHub-tilisi asetuksiin.
        - Valitse "SSH and GPG keys".
        - Napsauta "New SSH key" ja liitä `id_rsa.pub` -tiedoston sisältö.

    - GitLab:
        - Siirry GitLab-profiilisi asetuksiin.
        - Valitse "SSH Keys".
        - Lisää uusi SSH-avain ja liitä `id_rsa.pub` -tiedoston sisältö.

4. Lisää yksityinen SSH-avain Rahtiin:
    - Kohdassa "Source Secret" valitse "Create new Secret"
    - Nimeä salaisuus, kohdassa "Authentication type" valitse "SSH Key"
    - Liitä yksityisen SSH-avaimesi (`id_rsa`) sisältö ja luo
    - 
![oie_16720584BbbOspb](https://github.com/user-attachments/assets/b1d47511-0ce6-4980-a732-895193895780)

### Tuonti Gitistä (yksityiset repositoriot) CLI:n avulla { #import-from-git-private-repositories-using-the-cli }

Tämä olettaa, että käyttäjät ovat luoneet SSH-avaimet ja rekisteröineet julkisen avaimensa GitHubiin.

[Kirjaudu OpenShift CLI:hin (`oc`)](../usage/cli.md#how-to-login-with-oc):

```bash
oc login <cluster-url>
```

[Luo uusi projekti](../usage/projects_and_quota.md#creating-a-project):

```bash
oc new-project <project-name> --display-name=<display-name> --description="csc_project:<project-id>"
```

Luo SSH Key Secret:

```bash
oc create secret generic <secret-name> --from-file=ssh-privatekey=<path-to-private-key> --type=kubernetes.io/ssh-auth
```

Linkitä salaisuus builder-palvelutiliin:

```bash
oc secrets link builder <secret-name>
```

Ota sovellus käyttöön:

```bash
oc new-app <repository-url> --name=<application-name>
```

Seuraa buildia:

- lokien seuranta
  ```bash
  oc logs -f buildconfig.build.openshift.io/<application-name>
  ```

- Alkuperäinen build todennäköisesti epäonnistuu todennusongelmien takia, aseta build-salaisuus eksplisiittisesti:
  ```bash
  oc set build-secret --source bc/<application-name> <secret-name>
  ```

- Käynnistä uusi build:
  ```bash
  oc start-build <application-name> --follow
  ```

Julkaise sovellus:

```bash
oc expose deployment <application-name> --name=<service-name> --port=<port> --target-port=<target-port>
oc expose svc/<service-name>
```

Käytä sovellusta:

- Käytä osoitetta, jonka saat komennolla:
    ```bash
    oc get route <application-name>
    ```

## Vianetsintä { #troubleshooting }

Jos buildisi epäonnistuu Rahtissa, se voi tarkoittaa, että sovelluksesi tarvitsee enemmän muistia kuin oletusarvoisesti on varattu. Valitettavasti resursseja (limits ja requests) ei voi asettaa suoraan CLI:stä sovellusta käyttöönotettaessa. Sinun on käytettävä YAML-määritystiedostoa tai web-käyttöliittymää näiden asetusten määrittelyyn.

Voit luoda yaml-tiedoston ja soveltaa sitä komennolla `oc apply -f {your_yaml_file}.yaml` tai muokata nykyistä `BuildConfig`-objektiasi Rahtin web-käyttöliittymässä.
Ylläpitäjänäkymässä siirry kohtaan `Builds > BuildConfigs` ja napsauta BuildConfigiasi. Valitse `YAML`-välilehti.

Kohdan `spec` alla näet `resources: {}`. Lisää tähän `limits.cpu`, `limits.memory`, `requests.cpu` ja `requests.memory`:
```yaml
resources:
  limits:
    cpu: 1
    memory: 8Gi
  requests:
    cpu: 200m
    memory: 1600Mi
```

Huomaa, että niiden välinen ero ei voi olla yli 5-kertainen (oletussuhde, lisätietoa [täällä](../usage/projects_and_quota.md#default-pod-resource-limits)).

Tallenna ja aja build uudelleen. Jos se onnistuu, tarkista metriikat ja katso, kuinka paljon muistia käytettiin. Voit säätää muistirajan noin 10–20 % suuremmaksi kuin käytetty määrä.
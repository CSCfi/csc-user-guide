TÄRKEITÄ OHJEITA SISÄISTEN LINKKIEN SÄILYTTÄMISEKS:
1. Asiakirjan otsikoihin viittaavien linkkien on toimittava, vaikka teksti on käännetty.
2. Jokaiselle käännetylle otsikolle lisätään alkuperäinen englanninkielinen ankkuri ID, joka on lisättävä.
3. Esimerkki:
   Alkuperäinen: ## Installation Guide
   Käännetty: ## Asennusopas {#installation-guide}
4. ID-muodon tulisi olla alkuperäisen englanninkielisen otsikon teksti pienillä kirjaimilla, korvaten välilyönnit tavuviivoilla.
5. Huomaa, että tavuviivoja ei koskaan pidä olla kahta peräkkäin, esimerkiksi otsikolla "A & B" on ankkuri englanniksi A-B (ei A--B, vaikka siinä olisi kaksi välilyöntiä).

Lisäohjeet:
4. Säilytä kaikki Markdown-muotoilu ja rakenne
5. Säilytä kaikki linkit ja niiden URL-osoitteet
6. Jätä koodilohkot ja niiden sisältö kääntämättä
7. Säilytä kaikki HTML-tagit ja niiden attribuutit
8. Älä käännä muuttujien nimiä tai koodikatkelmia
9. Älä käännä kuvien tiedostonimiä tai polkuja

Tässä sisältö, joka käännetään:

On useita syitä luoda oma docker-kuva, mutta yleensä niitä on kaksi. Sovellukselle, jonka haluat suorittaa, ei ole saatavilla docker-kuvaa, tai käytettävissä oleva kuva ei toimi OpenShiftissä. Koska OpenShift on suunniteltu jaetuksi klusteriksi, jossa eri tiimien käyttäjät suorittavat sovelluksia samalla laitteistolla, OpenShiftin on lisättävä rajoituksia ja suoritettava asioita eri tavalla kuin tavallisessa Kubernetes-klusterissa.

Rahti-rekisterin kuvakoko on rajoitettu 5 Gt:n. Mitä suurempi kuva on, sitä huonompi kokemus sen kanssa työskentelystä on. Sen hakemisessa kestää kauemmin, ja se täyttää solmun kuvan välimuistin nopeammin. Yli 1 Gt:n kuvaa pidetään jo erittäin suurena. Katso artikkeli [pienien docker-kuvien ylläpitämisestä](keeping_docker_images_small.md).

## Kuvien rakentaminen paikallisesti {#building-images-locally}

Tässä esimerkissä käytämme [virallista nginx-kuvaa](https://hub.docker.com/_/nginx), joka on rakennettu [Alpine Linux](https://www.alpinelinux.org/) -jakelun päälle, ja teemme tarvittavat muutokset, jotta se toimisi OpenShiftissä.

Kolme vaihetta tarvitaan kuvan rakentamiseen paikallisesti tietokoneella.

* Ensiksi kirjoitetaan `Dockerfile`, esimerkiksi näin:

```Dockerfile
FROM nginx:alpine

# tuki mielivaltaiselle käyttäjälle, joka kuuluu root-ryhmään
RUN chmod g+rwx /var/cache/nginx /var/run /var/log/nginx && \
    chown nginx.root /var/cache/nginx /var/run /var/log/nginx && \
    # käyttäjät eivät saa kuunnella privilegoiduilla porteilla
    sed -i.bak 's/listen\(.*\)80;/listen 8081;/' /etc/nginx/conf.d/default.conf && \
    # Tee /etc/nginx/html/ käyttöön
    mkdir -p /etc/nginx/html/ && chmod 777 /etc/nginx/html/ && \
    # kommentoi käyttäjädirektiivi, sillä pääprosessi ajetaan joka tapauksessa käyttäjänä OpenShiftissä
    sed -i.bak 's/^user/#user/' /etc/nginx/nginx.conf

WORKDIR /usr/share/nginx/html/
EXPOSE 8081

USER nginx:root
```

`Dockerfile` on:

1. Antaa kirjoitusoikeudet `root`-ryhmälle (ei `root`-käyttäjälle) useille kansioille, joihin nginxin täytyy kirjoittaa (/var/cache/nginx, /var/run, /var/log/nginx ja /etc/nginx/html/). Sovellukset ajetaan satunnaisena käyttäjänä ja `root`-ryhmänä.
2. Muuttaa portin, jolla nginx kuuntelee, koska vain root saa kuunnella privilegoiduilla porteilla (<1024).
3. Ja lopuksi kommentoida käyttäjän konfiguraatiodirektiivi.

Alkuperäisellä `nginx:alpine`-kuvalla on 5 kerrosta, ja lisäämme uuden (`RUN`).

Yksinkertaisempi esimerkki `Dockerfilesta` voisi olla:

```Dockerfile
FROM alpine

RUN apk add git
```

Tämä vain asentaa gitin `alpineen` ja lisää myös uuden kerroksen.

Katso [Dockerfileen](https://docs.docker.com/engine/reference/builder/) liittyvät viiteasiakirjat.

Seuraavaksi käytetään seuraavaa komentoa kuvan rakentamiseen `docker.io/user/name:tag`:

```bash
docker build . -t docker.io/user/name:tag
```

Ja lopuksi kuvan julkaisuun:

```bash
docker push docker.io/user/name:tag
```

## Konttikuvien rakentaminen Rahdissa {#using-rahti-to-build-container-images}

Alla olevat menetelmät käyttävät Rahtia kuvien rakentamiseen.

### Rakentaminen paikallisesta kansiosta {#using-a-local-folder-for-building}

Tämä menetelmä mahdollistaa kuvan rakentamisen paikallisesta kansiosta, joka sisältää Dockerfilen ja muut tarvittavat projektitiedostot. Se on hyödyllinen, kun ei ole mahdollista tai ei ole tarkoituksenmukaista sallia Rahdin kopioida repositoriota suoraan.

Tämä edellyttää, että olet valtuuttanut Rahti-komentorivisession ja luonut projektin Rahdissa. Ohjeet tähän löytyvät luvusta [Komentorivityökalun käyttö](../usage/cli.md#cli-cheat-sheet).

**Vaiheet:**

Luo Rahti-spesifiset määritelmät komennolla `oc new-build`. Ole varovainen, ettet ole kansiossa, joka on git-versionhallinnan alaisuudessa:

```bash
$ oc new-build --to=oma-hello-kuva:devel --name=oma-hello --binary
    * Docker-rakennus, joka käyttää binaarisyötettä, luodaan
      * Tuloksena oleva kuva työnnetään kuva-virtatagiin "oma-hello-kuva:devel"
      * Binaarinen rakennus luotiin, käytä 'start-build --from-dir' laukaistaksesi uuden rakennuksen

--> Luodaan resursseja tunnisteella build=oma-hello ...
    imagestream.image.openshift.io "oma-hello-kuva" luotu
    buildconfig.build.openshift.io "oma-hello" luotu
--> Onnistuminen
```

Tarvitset sitten `Dockerfile`:n, voit käyttää mitä tahansa aiemman esimerkin `Dockerfilea` tai jotain muuta, mikä sinulla on. Kertoaksesi OpenShiftille rakentamaan kuvan, siirry kansioon, jossa `Dockerfile` sijaitsee, ja käynnistä rakennus komennolla `oc start-build`, se ottaa kaikki tiedostot nykyisestä hakemistosta ja tulostaa rakennusprosessin paikalliseen päätelaitteeseen:

```bash
oc start-build oma-hello --from-dir=./ -F
```

Kuva on internetissä näkyvissä osoitteessa `image-registry.apps.2.rahti.csc.fi/<project-name>/oma-hello-kuva:devel` docker-yhteensopiville asiakkaille, mutta sinun on ensin todistettava henkilöllisyytesi saadaksesi sen.

Komentorivin käyttö docker-yhteensopivilla asiakkailla, docker-rekisteri-salasana on käyttöoikeustunnus, joka näytetään valtuuttaessasi Rahti-komentorivisession ja käyttäjänimeksi voi laittaa `unused`.

```sh
docker login -u g -p $(oc whoami -t) image-registry.apps.2.rahti.csc.fi
```

### Source to Image -mekanismin käyttö {#using-the-source-to-image-mechanism}

OpenShift mahdollistaa koodin rakentamisen ja käyttöönoton ilman `Dockerfile`:n kirjoittamista. Tätä kutsutaan Source to Image:ksi tai `s2i`:ksi. Se tehdään suorittamalla `oc new-app URL#branch`, jossa `#branch` on optionalinen. Esimerkiksi, käytä virallista python-esimerkkikoodia:

```bash
$ oc new-app https://github.com/CSCfi/nodejs-16-rahti-example.git
--> Löydettiin Docker-kuva 9d200cd (7 viikkoa vanha) Docker Hubista "node:16.15.0":lle

    * Luodaan kuvan virtatagi "node:16.15.0", joka seuraa lähdekuvaa
    * Docker-rakennus käyttäen lähdekoodia osoitteesta https://github.com/CSCfi/nodejs-16-rahti-example.git luodaan
      * Tuloksena oleva kuva työnnetään kuva-virtatagiin "nodejs-16-rahti-example:latest"
      * Joka kerta kun "node:16.15.0" muuttuu, uusi rakennus laukaistaan
    * Tämä kuva otetaan käyttöön käyttöönoton konfiguraatiossa "nodejs-16-rahti-example"
    * Portti 8080/tcp tasapainotetaan palvelimen "nodejs-16-rahti-example" kautta
      * Muut säiliöt voivat käyttää tätä palvelua isäntänimen "nodejs-16-rahti-example" kautta
    * VAROITUS: Kuva "node:16.15.0" toimii 'root'-käyttäjänä, mikä ei ehkä ole sallittua klusterin valvojan toimesta

--> Resurssien luominen ...
    imagestream.image.openshift.io "node" luotu
    imagestream.image.openshift.io "nodejs-16-rahti-example" luotu
    buildconfig.build.openshift.io "nodejs-16-rahti-example" luotu
    deploymentconfig.apps.openshift.io "nodejs-16-rahti-example" luotu
    service "nodejs-16-rahti-example" luotu
--> Onnistuminen
    Rakennuksen määritys tehty, käytä 'oc logs -f bc/nodejs-16-rahti-example' seuraa sen etenemistä.
    Sovellusta ei ole julkaistu. Voit julkaista palveluja ulkomaailmaan suorittamalla yhden tai useamman seuraavista komennoista:
     'oc expose svc/nodejs-16-rahti-example'
    Suorita 'oc status' nähdäksesi sovelluksesi.
```

Tee sitten ehdotetun mukaisesti ja paljasta uusi sovellus ulkomaailmaan:

```bash
$ oc expose svc/nodejs-16-rahti-example
route.route.openshift.io/nodejs-16-rahti-example paljastettu
```

Hanki uuden reitin isäntänimi seuraavasti:

```bash
oc get route nodejs-16-rahti-example
```

Jos syötät isäntänimen selaimeen, näet "Hello World!" -viestin.

Uuden rakennuksen voi laukaista komentoriviltä:

```bash
oc start-build nodejs-16-rahti-example
```

Tai käyttämällä [webhookkeja](../tutorials/webhooks.md).

### Inline Dockerfile -menetelmän käyttö {#using-the-inline-dockerfile-method}

On mahdollista luoda uusi rakennus käyttäen Dockerfilea, joka on annettu komentorivillä. Tällöin itse `Dockerfile` liitetään rakenteessa olevaan Build-objektiin, joten ulkoista Git-repositoriota ei tarvita.

```bash
oc new-build -D $'FROM centos:7'
```

Tässä esimerkissä rakennamme kuvaa, joka on kopio `CentOS 7`:stä.

On myös mahdollista luoda rakennus olemassa olevasta `Dockerfile`:stä:

```bash
cat Dockerfile | oc new-build -D -
```

### Tuonti Gitistä (yksityiset tietovarastot) käyttämällä Web GUI:ta {#import-from-git-private-repositories-using-the-web-gui}

Yksityisen Git-repositorion käyttöönotto Rahdille edellyttää tarvittavien todennusten asettamista yksityiseen repositorioosi pääsemiseksi. Ilman asianmukaista todennusta saat virheilmoituksen "URL on kelvollinen mutta ei saavutettavissa" (näkyvä alla olevissa kuvissa). Tässä on kaksi ratkaisematapaa:

![oie_1671443U3OLpFT1](https://github.com/user-attachments/assets/a844e224-769e-4d9f-bba2-043ad5c9b258)

#### Vaihtoehto 1: Tokenin käyttö Git-todennukseen {#option-1-using-a-token-for-git-authentication}

1. **Luo henkilökohtainen käyttöoikeustoken:**

    - **GitHub:**
         - Siirry GitHub-tilisi asetuksiin.
         - Mene kohtaan "Developer settings" > "Personal access tokens".
         - Klikkaa "Generate new token".
         - Valitse tarpeelliset käyttöoikeudet (tyypillisesti `repo` yksityisille repositorioille).
         - Luo token ja kopioi se.

    - **GitLab:**
         - Siirry GitLab-profiilin asetuksiin.
         - Siirry kohtaan "Access Tokens".
         - Anna tokenille nimi, valitse tarvittavat käyttöoikeudet (esim. `api`, `read_repository`) ja luo token.
         - Kopioi token.

3. **Lisää Token Rahdille:**
    - Kohdassa "Source Secret" valitse "Create new Secret"
    - Nimeä salaisuus, valitse "Authentication type" kohdasta "Basic Authentication"
    - Liitä token ja luo

![oie_1672121lETtYQ6J](https://github.com/user-attachments/assets/4bd9450f-170b-4a9e-ae8c-df4700fb0be4)

#### Vaihtoehto 2: Yksityisen SSH-avaimen käyttö Git-todennukseen {#option-2-using-a-private-ssh-key-for-git-authentication}

1. **Luo SSH-avainpari (jos sinulla ei ole vielä):**

    - Avaa terminaali ja suorita seuraava komento luodaksesi uuden SSH-avainparin:
         ```sh
         ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
         ```
    - Tämä luo kaksi tiedostoa: yksityisen avaimen (`id_rsa`) ja julkisen avaimen (`id_rsa.pub`).

2. **Lisää julkinen avaimesi Git-hosting palveluun:**

    - **GitHub:**
        - Mene GitHub-tilisi asetuksiin.
        - Siirry kohtaan "SSH and GPG keys".
        - Klikkaa "New SSH key" ja liitä `id_rsa.pub`-tiedostosi sisältö.

    - **GitLab:**
        - Siirry GitLab-profiilin asetuksiin.
        - Mene kohtaan "SSH Keys".
        - Lisää uusi SSH-avain ja liitä `id_rsa.pub`-tiedostosi sisältö.

4. **Lisää yksityinen SSH-avaimesi Rahdille:**
    - Kohdassa "Source Secret" valitse "Create new Secret"
    - Nimeä salaisuus, valitse "Authentication type" kohdasta "SSH Key"
    - Liitä yksityisen SSH-avaimesi (`id_rsa`) sisältö ja luo 
    - 
![oie_16720584BbbOspb](https://github.com/user-attachments/assets/b1d47511-0ce6-4980-a732-895193895780)

### Tuonti Gitistä (yksityiset tietovarastot) käyttämällä CLI {#import-from-git-private-repositories-using-the-cli}

Tämä edellyttää, että käyttäjät ovat luoneet SSH-avaimia ja rekisterineet julkisen avaimen GitHubiin.

**[Kirjaudu sisään OpenShift CLI:hin (`oc`)](../usage/cli.md#how-to-login-with-oc)**:

```bash
oc login <cluster-url>
```

**[Luo uusi projekti](../usage/projects_and_quota.md#creating-a-project)**:

```bash
oc new-project <project-name> --display-name=<display-name> --description="csc_project:<project-id>"
```

**Luo SSH-avaimen salaisuus**:

```bash
oc create secret generic <secret-name> --from-file=ssh-privatekey=<path-to-private-key> --type=kubernetes.io/ssh-auth
```

**Linkitä salaisuus Builder Service Accountiin**:

```bash
oc secrets link builder <secret-name>
```

**Käytä sovellusta**:

```bash
oc new-app <repository-url> --name=<application-name>
```

**Seuraa rakennusta**:

- seuraa lokit
  ```bash
  oc logs -f buildconfig.build.openshift.io/<application-name>
  ```

- Alkurakennus todennäköisesti epäonnistuu todennusongelmien vuoksi, aseta rakennussalaisuus nimenomaisesti:
  ```bash
  oc set build-secret --source bc/<application-name> <secret-name>
  ```

- Käynnistä uusi rakennus:
  ```bash
  oc start-build <application-name> --follow
  ```

**Julkaise sovellus**:

```bash
oc expose deployment <application-name> --name=<service-name> --port=<port> --target-port=<target-port>
oc expose svc/<service-name>
```

**Käytä sovellusta**:

- Käytä URL-osoitetta, joka on annettu:
    ```bash
    oc get route <application-name>
    ```

## Vianetsintä {#troubleshooting}

Jos rakennuksesi epäonnistuu Rahdissa, se voi tarkoittaa, että sovelluksesi tarvitsisi enemmän muistia kuin oletusarvoisesti on tarjolla. Valitettavasti resurssirajojen ja -pyyntöjen asettaminen suoraan CLI:stä ei ole mahdollista, kun sovellus otetaan käyttöön. Sinun tulee käyttää YAML-määritystiedostoa tai web-käyttöliittymää näiden asetusten määrittämiseen.

Voit luoda yaml-tiedoston ja sitten soveltaa sitä komennolla `oc apply -f {your_yaml_file}.yaml` tai muokata nykyistä `BuildConfig`:ia Rahti-web-käyttöliittymässä.
Ylläpitäjänäkymässä navigoi kohtaan `Rakennukset > BuildConfigs` ja klikkaa BuildConfigiasi. Valitse `YAML`-välilehti.

`spec`-kohdan alla sinun pitäisi nähdä `resources: {}`. Täältä lisää `limits.cpu`, `limits.memory`, `requests.cpu` ja `requests.memory`:

```yaml
resources:
  limits:
    cpu: 1
    memory: 8Gi
  requests:
    cpu: 200m
    memory: 1600Mi
```

Huomaa, että ne eivät voi olla yli viisikertaisia toisistaan (oletusarvoinen suhde, enemmän tietoa [täältä](../usage/projects_and_quota.md#default-pod-resource-limits)).

Tallenna ja suorita rakennus uudelleen, ja jos se onnistuu, tarkista metrikkat ja katso, kuinka paljon muistia käytettiin. Voit säätää muistirajaa 10-20% enemmän kuin mitä käytettiin.
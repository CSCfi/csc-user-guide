# Miksi Rahti ei löydä tätä Docker-kuvaa? { #why-rahti-cannot-find-this-docker-image }

!!! error "Kuvien noutaminen DockerHubista"
    Viimeisimmän käyttöön otetun Rahti-version (OpenShift 4.17) myötä kuvien noutamiseen tuli konfiguraatiomuutos. Jotkin kuvat on kovakoodattu noudettaviksi tietyistä rekistereistä (kuten JFrogista).
    Vaikutusten minimoimiseksi ja virheiden välttämiseksi DockerHubista kuvia noudettaessa käytä täysin määriteltyä kuvan nimeä.

    Esimerkiksi sen sijaan, että käyttäisit `image: mongo:latest`, käytä `image: docker.io/library/mongo:latest`.

    Tämä toiminta korjataan OpenShift 4.18:ssa. Arvioitua valmistumisaikaa (ETA) ei toistaiseksi ole.

![Kuvaa ei voitu ladata](img/Could_not_load_image_metadata.png)

Usein tähän ongelmaan on yksinkertaisia syitä. Ehkä kuvan nimessä on kirjoitusvirhe, tai kuva on poistettu sen jälkeen, kun se on viimeksi onnistuneesti noudettu. Nämä kaksi ongelmaa ovat yleisiä, joten kuvan lähde kannattaa tarkistaa huolellisesti.

![Kuvan nouto epäonnistui](img/Failed_to_pull_image.png)

## Yksityinen kuva { #private-image }

Toinen syy voi olla, että kuva on yksityinen. Tällöin on tarpeen määrittää `docker-registry`-salaisuus tilitunnuksella, jolla on vaaditut oikeudet kuvan noutamiseen. Esimerkiksi Docker Hubissa sijaitsevaa kuvaa varten:

```bash
oc create secret docker-registry <SECRET-NAME> \
      --docker-username=<USERNAME> \
      --docker-server=docker.io \
      --docker-email=<EMAIL> \
      --docker-password=<PASSWORD>
```

```bash
oc secrets link default <SECRET-NAME> --for=pull
```

**Huomautus**: Korvaa paikkamerkit todellisella käyttäjätunnuksella, salasanalla, sähköpostilla ja salaisuudelle sopivalla nimellä (ilman <>-merkkejä).

Lisätietoja löydät artikkelista [Kuinka lisätä Docker Hub -tunnukset projektiin](docker_hub_login.md).

## Ei tuettu kuvamuoto { #unsupported-image-format }

Hankalampi ongelma on, kun kuvan formaattia ei tueta nykyisessä Rahti-versiossa (v3.11), joka käyttää vanhaa docker-asiakasta. Tällä hetkellä on kaksi docker-kuvaformaattia, docker (`application/vnd.docker.container.image.v1+json`) ja OCI (`application/vnd.oci.image.manifest.v1+json`); nykyinen Rahti-versio tukee vain `docker`-formaattia.

Kun vanhaa asiakasta käytetään yrittämään noutaa uudemmassa formaatissa olevaa kuvaa, asiakas ei löydä sitä ja palauttaa virheen `repository does not exist` tai `Error response from daemon: missing signature key`. Helpoin tapa tarkistaa kuvan `mediaType` on käyttää komentoa `docker manifest inspect <image>:<tag>`. Tämä komento näyttää kuvan ja sen kerrosten mediatyypin.

## Väliaikaiset ratkaisut { #workarounds }

* Yksinkertainen korjaus on noutaa kuva yhteensopivalla asiakkaalla, merkitä se uudelleen ja puskea se Rahtin sisäiseen rekisteriin. Tämä uusi, rekisteriin työnnetty kuva käyttää vanhaa docker-formaattia. Ohje: [Kuinka välimuistittaa kuvia käsin Rahtin rekisteriin](../../cloud/rahti/images/Using_Rahti_integrated_registry.md).

* Jos tiimisi rakensi kuvan, [buildah](https://buildah.io)-työkalua voidaan käyttää. Sen avulla voi rakentaa docker-kuvia ilman `docker build` -komennon edellyttämiä lisäoikeuksia, ja vaikka oletuksena se rakentaa kuvan `OCI`-formaattiin, siinä on valitsin, jolla voi käyttää `docker`-formaattia:

```bash
buildah bud -t image/name:tag --format=docker
```

* [Skopeo](https://github.com/containers/skopeo) on apuohjelma, joka suorittaa erilaisia toimintoja konttikuville ja kuvavarastoille.
Sitä voi käyttää kopioimaan DockerHubista Rahtin sisäiseen rekisteriin, ja se muuntaa kuvan automaattisesti `docker`-formaattiin. Esimerkki:  

Ensin sinun täytyy olla yhteydessä Rahtiin. Yhteyden jälkeen suorita tämä komento kopioidaksesi Docker-kuvan DockerHubista Rahtin sisäiseen rekisteriin:    

```
skopeo copy docker://publisher/image:tag --dest-creds $(oc whoami):$(oc whoami -t) docker://docker-registry.rahti.csc.fi/project/image:tag
```
_Korvaa 'project' Rahti-projektillasi, 'image' halutulla kuvan nimellä ja 'tag' halutulla tagilla_
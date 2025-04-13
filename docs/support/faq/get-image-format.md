
# Miksi Rahti ei löydä tätä docker-kuvaa? {#why-rahti-cannot-find-this-docker-image}

![Could not load image](img/Could_not_load_image_metadata.png)

Usein tälle ongelmalle on yksinkertaisia syitä. Ehkä kuvassa on kirjoitusvirhe, tai kuva on saatettu poistaa sen jälkeen, kun se viimeksi vedettiin onnistuneesti. Nämä kaksi ongelmaa ovat yleisiä, ja siksi on syytä tarkistaa kuvalähde kaksoiskuittauksella.

![Failed to pull image](img/Failed_to_pull_image.png)

## Yksityinen kuva {#private-image}

Toinen syy voi olla se, että kuva on yksityinen. Tässä tapauksessa on tarpeen määrittää `docker-registry`-salaisuus käyttäjätilillä, jolla on tarvittavat oikeudet vetää kuva. Esimerkiksi, kun kuva on tallennettu Docker-hubiin:

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

**Huom**: Korvaa paikkamerkit oikealla käyttäjänimellä, salasanalla, sähköpostilla ja sopivalla nimellä salaisuudelle (ilman <>).

Löydät lisätietoja artikkelista [How to add docker hub credentials to a project](docker_hub_login.md).

## Ei tuettu kuvamuoto {#unsupported-image-format}

Tavallista harvinaisempi ongelma on, kun kuvan muoto ei ole tuettu Rahtin nykyisessä versiossa (v3.11), joka käyttää vanhentunutta Docker-clienttä. Tällä hetkellä on kaksi Docker-kuvamuotoa, docker (`application/vnd.docker.container.image.v1+json`) ja OCI (`application/vnd.oci.image.manifest.v1+json`), joista Rahtin nykyinen versio tukee vain `docker`-muotoa.

Kun vanhaa clienttiä käytetään yrittäen vetää uudempaa muotoa olevaa kuvaa, ei clientti löydä sitä ja palauttaa virheen `repository does not exist` tai `Error response from daemon: missing signature key`. Helpoin tapa tarkistaa kuvan `mediaType` on käyttää komentoa `docker manifest inspect <image>:<tag>`. Tämä komento näyttää kuvan mediatyypin ja kunkin sen kerroksen tyypin.

## Kierratysratkaisut {#workarounds}

* Yksinkertainen ratkaisu on vetää kuva yhteensopivaa clienttiä käyttäen, uudelleen-tägätä se ja puskea Rahtin sisäiseen rekisteriin. Tämä äsken pushaettu kuva käyttää vanhaa docker-muotoa. Seuraa linkkiä saadaksesi ohjeen [How to manually cache images in Rahti's registry](../../cloud/rahti/images/Using_Rahti_integrated_registry.md).

* Jos kuva on tiimisi rakentama, voit käyttää [buildah](https://buildah.io)-työkalua. Sen avulla voi rakentaa docker-kuvia ilman ylimääräisiä oikeuksia, joita `docker build` vaatii, ja vaikka oletuksena se rakentaa OCI-muotoisen kuvan, sillä on vaihtoehto käyttää docker-muotoa:

```bash
buildah bud -t image/name:tag --format=docker
```

* [Skopeo](https://github.com/containers/skopeo) on työkalu, joka suorittaa erilaisia toimintoja konttikuville ja kuva-rekistereille.
Voit käyttää sitä kopioimaan DockerHubista Rahtin sisäiseen rekisteriin, ja se muuntaa kuvan automaattisesti `docker`-muotoon. Tässä on esimerkki:

Ensin sinun täytyy olla yhteydessä Rahtiin. Kun olet yhteydessä, kirjoita tämä komento kopioidaksesi Docker-kuva DockerHubista Rahtin sisäiseen rekisteriin:

```
skopeo copy docker://publisher/image:tag --dest-creds $(oc whoami):$(oc whoami -t) docker://docker-registry.rahti.csc.fi/project/image:tag
```

_Vaihda 'project' Rahti-projektillasi, 'image' haluamallasi kuvalla ja 'tag' haluamallasi tägillä_


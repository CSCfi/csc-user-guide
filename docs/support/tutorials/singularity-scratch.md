
# Apptainer-konttien rakentaminen alusta alkaen {#building-apptainer-containers-from-scratch}

CSC-alustoilla on kaksi tapaa luoda
[Apptainer-kontteja](https://apptainer.org/) (aiemmin tunnettu nimellä Singularity).
Voit:

1. [Muuntaa Docker-kontteja Apptainer-kuvatiedostoiksi](../../computing/containers/creating.md#converting-a-docker-container),
   tai
2. Rakentaa Apptainer-kuvan täysin alusta alkaen.

Tämä opas keskittyy jälkimmäiseen tapaukseen, ja lisätietoja on saatavilla
[Apptainer-verkkosivustolla](https://apptainer.org/docs/user/main/build_a_container.html).

## Kontit erillisinä ympäristöinä {#containers-as-distinct-environments}

Yksi voi ajatella konteista erillisinä ympäristöinä. Esimerkiksi
kontissa käytetty Linux-jakelu voi erota isäntäympäristöstä, jossa
kontti suoritetaan. Apptainer-kuvilla on myös sisäinen tiedostojärjestelmä,
joka ei ole näkyvissä konttien ulkopuolella. Samoin suurin osa
isäntäympäristöstä ei ole näkyvissä kontille, ellei sitä ole
erikseen määritelty. Valitut isännän kansiot voidaan altistaa kontille
käyttämällä
[bind mountseja](https://apptainer.org/docs/user/main/bind_paths_and_mounts.html).

Kun suunnittelet Apptainer-kontin sisältöä ja konfigurointia, on tehtävä päätös
siitä, pitäisikö tietyt asennukset tehdä konttiin vai lisätä bind mountseina.
Esimerkiksi tietyt riippuvuudet voivat olla jo olemassa isännässä.
Kontin Linux-jakelu vaikuttaa luonnollisesti tähän päätökseen.

Usein kontissa käytetyt ympäristömuuttujat *verrattuna* isäntäympäristöön
tulevat myös eroamaan (lisätietoja alla).

## Määrittelytiedoston valmistelu {#preparing-a-definition-file}

Määrittelytiedosto (pääte `.def`) sisältää komennot, jotka
vaaditaan kontin rakentamiseen. Esimerkkejä CSC:n
laskentaympäristössä käytetyistä määrittelytiedostoista löytyvät
[singularity-recipes-repositoriosta](https://github.com/CSCfi/singularity-recipes).

Määrittelytiedosto on jaettu eri tarkoituksiin palveleviin osiin
([katso tarkemmat tiedot täältä](https://apptainer.org/docs/user/main/definition_files.html)).
Tiedoston yläosassa on annettava otsikko, joka sisältää bootstrap-avainsanan
ja Linux-jakelun. Esimerkiksi Ubuntu 22.04 -kontin otsikon luomiseksi
kirjoitetaan:

```dockerfile
Bootstrap: docker
From: ubuntu:22.04
```

Linux-jakelun valinta määrittää komentosarjassa käytetyt
komennot. Esimerkiksi CentOS-kontti käyttäisi komentoja kuten
`yum -y install`, kun taas Ubuntu-kontti käyttäisi komentoja kuten
`apt-get -y install`.

Muita osioita, joita voi käyttää, ovat esimerkiksi:

* `%labels` (esim. kuvan ylläpitäjän nimi ja yhteystiedot).
* `%files` (komennot ulkoisten tiedostojen kopioimiseksi tiettyyn paikkaan
  kontissa).
* `%post` (osio ohjelmistojen asennuskomentoja varten).
* `%environment` (ympäristömuuttujat, jotka määritellään kontin käynnistyessä).

Huomaa, että eri osioita voidaan lisätä tai jättää pois tarpeidesi mukaan.
Esimerkiksi, jos sinulla ei ole ulkoisia tiedostoja lisättävänä konttiin,
ei ole tarpeen lisätä `%files`-osaa.

### Muutama sana ympäristömuuttujista {#a-few-words-on-environment-variables}

Ympäristömuuttujat voidaan määritellä sekä `%post`- että `%environment`-osioissa.
Ensimmäiseen osioon määritellyt voivat olla hyödyllisiä ohjelmistojen
asentamisessa, mutta toisin kuin `%environment`-osiossa määritellyt muuttujat,
ne eivät ole näkyvissä kontin käynnistyessä.

Jos haluat määritellä ympäristömuuttujia isäntäympäristössä niin, että ne ovat
näkyvissä kontin sisällä, niiden on alettava `APPTAINERENV_`.
Ilman tätä etuliitettä olevia muuttujia ei siirretä kontille.

## Kontin rakentaminen {#building-a-container}

Apptainer-kontin rakentaminen vaatii root-oikeuksia (`sudo`).
CSC:n supertietokoneilla, missä käyttäjillä ei ole
root-oikeuksia, voit käyttää
[fakeroot](https://apptainer.org/docs/user/main/fakeroot.html)-ominaisuutta
kiertääksesi tämän vaatimuksen (muutamin rajoituksin).
[Katso dokumentaatiomme konttien luomisesta lisätietoja varten](../../computing/containers/creating.md#building-a-container-without-sudo-access-on-puhti-and-mahti).

Vaihtoehtoisesti voit käyttää omaa tietokonettasi tai järjestelmäkonetta,
jossa sinulla on root-oikeudet, kontin kuvan rakentamiseen. Yksi
vaihtoehto on käyttää
[Pouta-virtuaalikonetta](../../cloud/pouta/index.md). Tämä mahdollistaa
määrittelemäsi ympäristön tyypin, jota käytetään kuvan rakentamiseen.
Useimmiten ympäristö, joka käytetään kontin rakentamiseen, ei ole
merkityksellinen verrattuna kontin ja isännän yhteneväisyyteen, mutta tietyt
asennukset (esim.
[Nvidia CUDA -ajurit](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html))
vaativat tarkkoja versioita ytimien otsikoille, mikä tarkoittaa, että
työn alustana käytettävä jakelu on sovitettava vastaamaan.

Määrittelytiedostoa käyttäen kontin rakentaminen voidaan suorittaa ajamalla:

```bash
sudo apptainer build container.sif recipe.def
```

tai ilman `sudo` käyttämällä `--fakeroot`-vaihtoehtoa:

```bash
apptainer build --fakeroot container.sif recipe.def
```

!!! info "Huomautus"
    Vanhoissa Linux-versioissa komento voi olla `singularity` `apptainer`:n
    sijaan.

Jos kaikki suoritetaan onnistuneesti, lopputuloksena on kontin kuva
(`.sif`-tiedosto), joka voidaan siirtää valitsemaasi
laskentaympäristöön. Kuvan tiedosto on *muuttumaton*, tarkoittaen, että
sitä ei voi muokata rakentamisen jälkeen. On myös mahdollista luoda
[kirjoitettavia sandbox-hakemistoja](https://apptainer.org/docs/user/main/build_a_container.html#creating-writable-sandbox-directories)
joita voidaan käyttää testaamiseen (ja voidaan myöhemmin muuntaa Apptainer
kuviksi).

## Kontin suorittaminen {#running-a-container}

On useita tapoja suorittaa Apptainer-kontteja CSC:n
laskentaympäristössä. Yksityiskohtaisia ohjeita varten, katso dokumentaatiomme 
[konttien suorittamisesta](../../computing/containers/run-existing.md).

Vaihtoehdot ovat:

* `apptainer exec`
* `apptainer_wrapper exec` (kääreskripti, joka yhdistää usein käytetyt
  paikalliset hakemistot, esim. `$TMPDIR`)

Monet CSC:n laskentaympäristön kontit ovat saatavilla valituille komennoille
tarkoitetuilla kääreskripteillä, joiden ansiosta ne voidaan suorittaa
ilman tarvetta yllä mainituille komennoille. On myös mahdollista
valmistella kääreskriptejä alusta alkaen rakennetuille konteille, vaikka
tämä vaatii jonkin verran Bash-skriptaamisen tuntemusta. Tarjoamme
myös [konttikääretyökalun "Tykky"](../../computing/containers/tykky.md), jota
voidaan käyttää konttien helppoon luomiseen ja kääreiden luomiseen
Python-ympäristöille.

## Konttien siirtäminen CSC:n laskentaympäristöön {#moving-containers-to-cscs-computing-environment}

### Puhti, Mahti ja LUMI {#puhti-mahti-and-lumi}

Apptainer-kuvatiedostoja voidaan siirtää Puhtiin, Mahtiin tai LUMIin esim.
[`scp`, `rsync` tai graafista tiedostonsiirto-ohjelmaa](../../data/moving/index.md) käyttäen.

### CSC Sensitive Data Desktop {#csc-sensitive-data-desktop}

Jos haluat käyttää itse rakennettua konttia
[CSC Sensitive Data Desktopilla](../../data/sensitive-data/sd_desktop.md),
siirrä ensin kuvatiedosto Puhtiin. Seuraa sitten ohjeitamme
[konttien siirtämisestä SD Desktopille Allasin avulla](../../data/sensitive-data/sd-desktop-singularity.md).

## Lisätietoja {#more-information}

* [Konttien käyttö CSC:n laskentaympäristössä](../../computing/containers/overview.md)
* [Konttien luominen Tykyllä](../../computing/containers/tykky.md)

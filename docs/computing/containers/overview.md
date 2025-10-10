---
description: Instructions for building and running Apptainer containers in CSC supercomputers.
description_fi: Ohjeet Apptainer-konttien rakentamiseen ja ajamiseen CSC:n superkoneilla.
---

# Apptainer-kontit { #apptainer-containers }

Tässä osiossa annetaan ohjeet konttien rakentamiseen ja ajamiseen [Apptainerilla](https://apptainer.org/) CSC:n superkoneilla.
Vaikka keskitymme CSC:lle tyypillisiin käyttötapoihin ja parhaisiin käytäntöihin, virallinen [Apptainer-dokumentaatio](https://apptainer.org/docs/user/main/index.html) toimii kattavana yleisviitteenä.
Käytännön ohjeita varten katso [Esimerkit](./examples.md)-osio, jossa on CSC-järjestelmiin räätälöityjä konkreettisia esimerkkejä.

Huomaa, että Apptainer tunnettiin aiemmin nimellä Singularity, ja saatat edelleen törmätä vanhaan nimeen ohjelmiston sisäosissa ja vanhassa dokumentaatiossa.
Projekti nimettiin uudelleen, kun se siirtyi Sylabsilta Linux Foundationille, mutta ydinominaisuudet pysyivät samoina.
Sylabs ylläpitää projektin haarautusta nimeltä SingularityCE.

## Motivaatio { #motivation }

Apptainer-konttikuva on yksi pakattu tiedosto, joka sisältää kaiken sovelluksen ajamiseen tarvittavan.
Tämä muuttumaton tiedosto sisältää täydellisen juuritiedostojärjestelmän, mukaan lukien kaikki sovellukset, kirjastot ja riippuvuudet, sekä metatiedot, kuten ympäristömuuttujat ja ajoaikaiset asetukset.
Apptainer käyttää kuvilleen Singularity Image Format -muotoa (SIF), jonka tiedostopääte on `.sif`.

Apptainer-kontit mahdollistavat minkä tahansa Linux-jakelun valitsemisen pohjakuvaksi, kuten Ubuntun, Rocky Linuxin tai OpenSUSEn, ja sen oman paketinhallinnan hyödyntämisen ohjelmistojen asennukseen kyseisessä ympäristössä.
Konttien rakentamisessa CSC:n superkoneilla on kuitenkin tiettyjä rajoituksia, erityisesti jos valittu pohjakuva poikkeaa isäntäjärjestelmän Linux-jakelusta.
Näitä ongelmia ja niiden ratkaisuja käsitellään myöhemmin tarkemmin.

Ohjelmiston ajaminen Apptainer-kontista voi merkittävästi parantaa käynnistysaikoja ja vähentää I/O-pullonkauloja [Lustre](../lustre.md)-rinnakkaistiedostojärjestelmässä.
Tämä on erityisen hyödyllistä sovelluksille, jotka sisältävät paljon tiedostoja tai lataavat käynnistyksen aikana lukuisia jaettuja kirjastoja.
Python-ympäristöt ovat tästä kuuluisa esimerkki laajojen moduuliriippuvuuksien ja dynaamisen latauskäyttäytymisen vuoksi.

Apptainer-kontit varmistavat toistettavan suorituksen, koska niiden kuvat ovat muuttumattomia.
Kun konttikuva on rakennettu, se pysyy muuttumattomana ja takaa yhtenäisen toiminnan eri järjestelmissä ja ajankohdissa.
Lisäksi Apptainerin määrittelytiedostot dokumentoivat tarkat vaiheet, paketit ja asetukset, joilla kontti on luotu, mikä tekee koko rakennusprosessista läpinäkyvän ja toistettavan.

Konttikuvilla on olennainen rajoitus: niitä ei voi yhdistellä.
Toisin kuin perinteiset paketinhallinnat, joissa ohjelmistoja voidaan lisätä järjestelmään vaiheittain, et voi yksinkertaisesti yhdistää olemassa olevia kontteja luodaksesi uuden.
Esimerkiksi yksi kontti, jossa on Python, ja toinen, jossa on R, eivät yhdessä tarjoa pääsyä molempiin ympäristöihin samanaikaisesti.
Jos haluat käyttää molempia työkaluja yhdessä, sinun on luotava uusi konttikuva, joka sisältää sekä Pythonin että R:n asennukset alusta alkaen.

## Konttien ajaminen { #running-containers }

### Apptainerin käyttäminen suoraan { #using-apptainer-directly }

Oletetaan, että meillä on konttikuva nimeltä `container.sif`.
Voimme suorittaa mielivaltaisen komennon (korvaa `mycommand`) kontin sisällä komennolla `apptainer exec` seuraavasti:

```bash
apptainer exec container.sif mycommand
```

Voimme tuoda isäntäkoneen hakemistoja kontin sisään bind-kiinnityksillä.
Puhtissa ja Mahtissa voimme bind-kiinnittää eri [levyalueet](../disk.md) konttiin seuraavasti:

```bash
apptainer exec --bind="/users,/projappl,/scratch,$TMPDIR,$LOCAL_SCRATCH" container.sif mycommand
```

Voimme lisätä Nvidian GPU-tuen `--nv`-lipulla seuraavasti:

```bash
apptainer exec --nv container.sif mycommand
```

Samat liput toimivat myös `apptainer run`- ja `apptainer shell` -komennoissa.

### Apptainer-wrapperin käyttö { #using-apptainer-wrapper }

Moniin CSC:n tarjoamiin kontteja hyödyntäviin ohjelmistoympäristöihin pääsee `apptainer_wrapper`-skriptin kautta.
Wrapperi käyttää ympäristömuuttujia löytääkseen konttikuvan polun (`SING_IMAGE`) ja välittääkseen liput (`SING_FLAGS`), kuten `--nv`.
Wrapper-skripti lisää automaattisesti liput yleisille bind-kiinnityksille.
Voimme suorittaa komentoja kontista seuraavasti:

```bash
export SING_IMAGE=/path-to/container.sif
export SING_FLAGS=""
apptainer_wrapper exec mycommand
```

Myös `apptainer_wrapper run`- ja `apptainer_wrapper shell` -alikomennot ovat käytettävissä.

## Konttikuvien rakentaminen { #building-container-images }

Tässä osiossa kerrotaan, miten Apptainerilla muunnetaan olemassa olevia Docker- ja OCI-kuvia SIF-kuviksi, miten uusia SIF-kuvia rakennetaan määrittelytiedostoista sekä miten kontteja kehitetään interaktiivisesti muokattavana (ch)root-hakemistona sandboxin avulla.
Käsittelemme myös, miten asettaa sopiva rakennusympäristö ja resurssit, kuten muisti, rakentamista varten Puhtissa ja Mahtissa.

### Linux-jakelun valinta pohjakuvaksi { #choosing-a-linux-distribution-as-a-base-image }

Pohjakuvaksi valittaessa käytettävissä on useita Linux-jakeluja, joilla on omat paketinhallintansa.
Red Hat Enterprise Linux (RHEL) -perheeseen kuuluville, DNF-paketinhallintaa käyttäville jakeluille suosittuja vaihtoehtoja ovat [RedHat Universal Base Images (UBI)](https://catalog.redhat.com/en/software/base-images), joita on saatavilla nimillä [redhat/ubi8](https://hub.docker.com/r/redhat/ubi8) ja [redhat/ubi9](https://hub.docker.com/r/redhat/ubi9), sekä yhteisövaihtoehdot kuten [rockylinux](https://hub.docker.com/r/rockylinux/rockylinux) ja [almalinux](https://hub.docker.com/_/almalinux).
Jos suosit SUSE-pohjaisia järjestelmiä, jotka käyttävät Zypperiä, [opensuse/leap](https://hub.docker.com/r/opensuse/leap) tarjoaa vakaan pohjan. Debian-pohjaisille jakeluille, jotka käyttävät APTia, sekä [debian](https://hub.docker.com/_/debian) että [ubuntu](https://hub.docker.com/_/ubuntu) tarjoavat hyvin ylläpidettyjä pohjakuvia laajoilla pakettivarastoilla.

Vaikka Apptainer sallii konttien rakentamisen minkä tahansa Linux-jakelun pohjakuvaa käyttäen, rakentamisessa CSC:n superkoneilla on rajoituksia, koska Apptaineria käytetään fakeroot-tilassa ilman unprivileged user namespace -tukea.
Tässä ympäristössä tietyt etuoikeutetut komennot, joita suoritetaan usein pakettien asennuksen yhteydessä, epäonnistuvat.
Esimerkiksi paketinhallinnat suorittavat usein etuoikeutettuja komentoja, kuten `useradd` ja `groupadd`, osana asennusskriptejään, ja nämä epäonnistuvat fakeroot-ympäristössä.

Käyttämällä isäntäjärjestelmän kanssa samaan perheeseen kuuluvaa pohjakuvaa vähennämme fakeroot-tilasta johtuvia ongelmia kontteja rakentaessa.
Jos käytät pohjakuvaa, joka ei ole isäntäjärjestelmän kanssa samasta perheestä, varaudu siihen, että useampien pakettien asennus epäonnistuu.
Paras tapa selvittää tilanne on yrittää rakentaa kontti.

Voit tunnistaa isäntäjärjestelmäsi Linux-jakelun seuraavasti:

```bash
cat /etc/os-release
```

```text title="stdout"
NAME="Rocky Linux"
VERSION="8.10 (Green Obsidian)"
ID="rocky"
ID_LIKE="rhel centos fedora"
VERSION_ID="8.10"
...
```

Lisäksi voimme korvata ongelmia aiheuttavat komennot valetoteutuksilla, jotka onnistuvat aina:

```bash
cp /usr/bin/true /usr/sbin/useradd
cp /usr/bin/true /usr/sbin/groupadd
```

Tällä tavalla pakettien asennukset saadaan vietyä läpi ohittamalla oikeuksiin liittyvät virheet.

### Ohjelmiston asentaminen konttiin { #installing-software-into-the-container }

Tyypillinen malli ohjelmistojen asentamiseen konttiin on aloittaa järjestelmän paketinhallinnalla, kuten DNF, APT tai Zypper, ja asentaa “järjestelmä”-ohjelmistot hakemistoon `/usr`, minkä jälkeen asennetaan ohjelmistoja käyttäjätilan paketinhallinnalla, kuten Pip, Conda tai Spack, tai asennetaan käsin hakemistoon `/usr/local` tai omaan hakemistoon `/opt`-puun alle.

### Rakennuspaikka { #build-location }

Voimme rakentaa kontteja millä tahansa solmulla, jolla on [paikallista levytilaa](../disk.md#temporary-local-disk-areas).
Kirjautumissolmuilta löytyy paikallinen levy oletuksena.
Laskentasolmulla rakentamista varten voimme varata Slurm-työn paikallisella levyllä.
Esimerkiksi interaktiivisen työn paikallisella levyllä (`--tmp`) voi varata näin:

```bash
sinteractive --cores 4 --mem 4000 --tmp 10 --time 0:15:00
```

### Väliaikaishakemisto { #temporary-directory }

Ympäristömuuttujan `TMPDIR` on osoitettava paikalliselle levylle.
Apptainer käyttää sitä väliaikaishakemistonaan konttia rakennettaessa.
Puhti- ja Mahti-klusterit asettavat `TMPDIR`-muuttujan automaattisesti kirjautumissolmuille, joilla on paikallinen levy oletuksena, sekä laskentasolmuille silloin, kun paikallinen levy on varattu.
Lustre-rinnakkaistiedostojärjestelmää ei voi (eikä pidä) käyttää väliaikaishakemistona.

### Välimuistihakemisto { #cache-directory }

Apptainer välimuistittaa kerroksia ja blob-tietoja, kuten pohjakuvia, välimuistihakemistoon.
Oletussijainti on kotihakemistossa (`$HOME/.apptainer`), jossa kiintiö on Puhtissa ja Mahtissa rajallinen.
Siksi välimuistin sijainti kannattaa ohjata scratch-alueelle, jotta kotihakemisto ei täyty (muokkaa `project_id` omaa projektiasi vastaavaksi).

```bash
export APPTAINER_CACHEDIR=/scratch/project_id/$USER/.apptainer
```

Välimuistin voi myös siivota tarvittaessa:

```bash
apptainer cache clean
```

### Virtuaalimuistin raja { #virtual-memory-limit }

Kirjautumissolmujen virtuaalimuistin raja Puhtissa ja Mahtissa on melko pieni (10 GiB), ja sitä voidaan nostaa kovarajaan saakka (24 GiB).
Rajan ylittäminen aiheuttaa muistivirheitä rakentamisen aikana.
Voit kysyä nykyisen virtuaalimuistin rajan komennolla `ulimit -v` ja kovarajan komennolla `ulimit -Hv`.
Voimme asettaa virtuaalimuistin rajan kovarajaksi näin:

```bash
ulimit -v $(ulimit -Hv)
```

Jos rakentaminen loppuu virtuaalimuistiin kirjautumissolmulla, kannattaa käyttää interaktiivista työtä, jossa virtuaalimuisti on rajattu varatun muistin määrään.

### Väliaikaishakemiston bind-kiinnitys { #bind-mounting-temporary-directory }

Oletuksena Apptainer bind-kiinnittää isännän `/tmp`:n `/tmp`:ksi rakennusympäristössä.
Puhtissa ja Mahtissa `/tmp` on kuitenkin kooltaan rajallinen, joten bind-kiinnitämme paikallisen levyn (`$TMPDIR`) hakemistoon `/tmp`, jotta levytila ei lopu kesken, seuraavasti: `--bind="$TMPDIR:/tmp"`.

### SIF-kuvan rakentaminen olemassa olevasta Docker- tai OCI-kuvasta { #building-sif-image-from-existing-docker-or-oci-image }

Voimme noutaa olemassa olevia konttikuvia rekisteristä vetämällä ne.
Apptainer muuntaa ne Docker- tai OCI-muodosta Singularity Image Format (SIF) -muotoon.

```bash
apptainer build rockylinux.sif docker://docker.io/rockylinux/rockylinux:8.10
```

### SIF-kuvan rakentaminen määrittelytiedostosta { #building-sif-image-from-definition-file }

Apptainerin määrittelytiedostojen tiedostopääte on `.def`.
Tässä on yksinkertainen esimerkki konttimäärittelystä:

```sh title="container.def"
Bootstrap: docker
From: docker.io/rockylinux/rockylinux:8.10

%post
    # Replace the failing commands with always succeeding dummies.
    cp /usr/bin/true /usr/sbin/useradd
    cp /usr/bin/true /usr/sbin/groupadd

    # Continue to install software into the container normally.
    dnf -y update  # would fail without the dummies
```

Voimme pyytää Apptaineria rakentamaan kontin (`container.sif`) määrittelytiedostosta (`container.def`) fakeroot-tilassa seuraavasti:

```bash
apptainer build --fakeroot --bind="$TMPDIR:/tmp" container.sif container.def
```

Katso lisää esimerkkejä Apptainerin määrittelytiedostoista kohdasta [Esimerkit](./examples.md).

### Interaktiivinen kehitys sandboxin kanssa { #developing-with-interactive-sandbox }

Voimme rakentaa myös Apptainer-sandboxeja fakeroot-tilassa.
Sandboxit ovat hyödyllisiä konttien interaktiiviseen kehittämiseen.
Sandbox on luotava paikalliselle levylle (`$TMPDIR`), ei Lustre-rinnakkaistiedostojärjestelmään.

Voimme alustaa sandboxin pohjakuvasta näin:

```bash
apptainer build --fakeroot --sandbox "$TMPDIR/rockylinux" docker://docker.io/rockylinux/rockylinux:8.10
```

Tämän jälkeen voimme käynnistää shellin sandboxissa ja asentaa sinne ohjelmistoja:

```bash
apptainer shell --fakeroot --writable --contain --cleanenv --bind="$TMPDIR:/tmp" "$TMPDIR/rockylinux"
```

Voimme käyttää samoja niksejä epäonnistuvien komentojen korvaamiseen sandboxissa:

```bash
cp /usr/bin/true /usr/sbin/useradd
cp /usr/bin/true /usr/sbin/groupadd
```

Nyt voidaan asentaa ohjelmistoja normaalisti:

```bash
dnf -y update
```

## Aineistojen lukeminen SquashFS-tiedostosta { #reading-datasets-from-squashfs-file }

Voimme välttää I/O-pullonkauloja myös aineistoissa, jotka koostuvat suuresta määrästä pieniä tiedostoja, kokoamalla ne yhdeksi SquashFS-tiedostoksi.
SquashFS-tiedosto voidaan bind-kiinnittää kontin sisään ja käyttää vain luku -tilassa.
Seuraavassa esimerkissä puretaan aineisto paikalliselle levylle, luodaan aineistosta SquashFS-tiedosto ja siirretään se takaisin scratch-alueelle:

```bash
# Extract individual files to local drive
cd $TMPDIR
tar xf /scratch/project_id/mydataset.tar

# Create squashfs file
mksquashfs mydataset mydataset.sqfs -processors 4

# Move the resulting squashfs file back to the shared drive
mv mydataset.sqfs /scratch/project_id/
```

Nyt voimme bind-kiinnittää aineiston seuraavasti:

```bash
apptainer exec --bind=/scratch/project_id/mydataset.sqfs:/data:image-src=/ container.sif mycommand
```

Data on saatavilla polussa `/data` kontin sisällä.

## Konttikäärimet { #container-wrappers }

[Tykky](./tykky.md)-konttikäärin on käytettävissä kontitetuille Pip- ja Conda-asennuksille wrapper-skriptien kanssa.
Jos Tykky on sinulle entuudestaan tuttu, voit jatkaa sen käyttöä, mutta suosittelemme konttien rakentamista ja ajamista suoraan, kuten edellisissä osioissa on selitetty.
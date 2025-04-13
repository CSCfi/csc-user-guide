
# Containerien luominen {#creating-containers}

CSC:n supertietokoneet Puhti ja Mahti tukevat [Apptainer-containereiden](https://apptainer.org/) (entiseltä nimeltään Singularity) käyttöä. Jos haluat käyttää container-pohjaista sovellusta, tarkista ensin [sovellussivut](../../apps/index.md) nähdäksesi, onko esiasennettu container jo saatavilla. Katso myös [dokumentaatiomme konttien käytöstä](run-existing.md).

Jos et löydä valmista containeria, yksi vaihtoehto on rakentaa oma. Jos Docker container -kuva on jo olemassa, voit usein vain muuntaa sen Apptainer-containeriksi. Toinen vaihtoehto on rakentaa oma container alusta alkaen. Molempia lähestymistapoja käsitellään alla. Kuten aina, jos sinulla on ongelmia tai kysyttävää, älä epäröi ottaa yhteyttä [CSC:n palvelupisteeseen](../../support/contact.md).

## Docker-containerin muuntaminen {#converting-a-docker-container}

Jos sinulla on jo olemassa oleva Docker-container, monissa tapauksissa se voidaan helposti muuntaa Apptainer-kuvaksi. Docker-container -kuvia löytyy julkisista arkistoista, kuten [Docker Hubista](https://hub.docker.com/), mutta **muista käyttää vain hyvämaineisista lähteistä ladattuja kuvia**, sillä nämä kuvat voivat helposti olla tietoturvariskejä tai jopa sisältää haitallista koodia.

GPU-optimoituja containereita löytyy myös [NVIDIAn GPU-pilvestä (NGC)](https://catalog.ngc.nvidia.com/). Nämä containerit ovat NVIDIAn valmistelemia ja siten turvallisia.

Lisätietoa [Docker-containerien muuntamisesta löytyy Apptainer-dokumentaatiosta](https://apptainer.org/docs/user/main/docker_and_oci.html).

Tässä on esimerkki Apptainer-kuvan rakentamisesta Puhtissa [NVIDIAn PyTorch Docker -kuvasta](https://catalog.ngc.nvidia.com/orgs/nvidia/containers/pytorch). Käytämme `sinteractive`, sillä raskasta käsittelyä ei pitäisi tehdä kirjautumissolmuissa.

```bash
# Aloitetaan 1 tunnin interaktiivinen työ riittävällä muistilla ja paikallisella raaputusalueella
sinteractive --account <project> --time 1:00:00 -m 16G --tmp 64

# Käytetään nopeaa paikallista asemaa tilapäiseen tallennukseen
export APPTAINER_TMPDIR=$LOCAL_SCRATCH
export APPTAINER_CACHEDIR=$LOCAL_SCRATCH

# Tämä on vain ärsyttävien varoitusten välttämiseksi
unset XDG_RUNTIME_DIR

# Vaihdetaan hakemistoon, johon haluat tallentaa kuvan
cd /projappl/<project>

# Suoritetaan varsinainen muuntaminen
# HUOM: Docker-kuva ladataan suoraan NGC:stä
apptainer build pytorch_22.09-py3.sif docker://nvcr.io/nvidia/pytorch:22.09-py3
```

Huomaa, että Apptainer-kuvien `.sif`-tiedostot voivat helposti olla useita gigatavuja suuria, joten niitä ei pitäisi tallentaa kotihakemistoosi, vaan esimerkiksi projektin hakemistoon [projappl](../../computing/disk.md).

Katso myös [dokumentaatiomme konttien käytöstä](run-existing.md).

## Containerin rakentaminen alusta asti {#build-a-container-from-scratch}

Voit myös rakentaa oman containerisi alusta alkaen. Tämä on vaihtoehto kokeneemmille käyttäjille, ja tärkein tietolähteesi on [virallinen Apptainer-dokumentaatio containerien rakentamisesta](https://apptainer.org/docs/user/main/build_a_container.html).

Voit löytää apua myös tutustumalla [ohjeeseemme Apptainer-containerien rakentamisesta alusta asti](../../support/tutorials/singularity-scratch.md).

## Containerin rakentaminen ilman sudo-oikeuksia Puthissa ja Mahtissa {#building-a-container-without-sudo-access-on-puhti-and-mahti}

Juuretason pääsy Puthiin ja Mahtiin ei ole sallittu. Nimitilat on myös poistettu käytöstä niihin liittyvien tietoturvaongelmien vuoksi. Kuitenkin muutamin rajoituksin, Apptaineria voi silti käyttää oikeudeton käyttäjä rakentamaan containeria käyttämällä [fakeroot](https://apptainer.org/docs/user/main/fakeroot.html)-ominaisuutta.

Apptainer mahdollistaa `--fakeroot`-lipun oletusarvoisesti containerien rakentamisessa, jos `sudo` tai nimitilat eivät ole saatavilla, mikä saa käyttäjän näyttämään `root:root`-käyttäjältä containeria rakentaessaan, mikä mahdollistaa sellaisten kuvien rakentamisen, jotka vaativat juuritiedostojen oikeuksia esimerkiksi pakettien asentamiseen `apt`:n kautta. Tämä saa kuitenkin vain käyttäjän *näyttämään* root-käyttäjältä, isäntäjärjestelmässä käyttäjällä ei ole lisää oikeuksia. Yksinään fakeroot ei aina riitä, ja joissain tapauksissa joitain containereita ei voida rakentaa erilaisten syiden vuoksi. Lisätietoja löytyy [virallisesta Apptainer-dokumentaatiosta](https://apptainer.org/docs/user/main/fakeroot.html).

Seuraava yksinkertainen määrittelytiedosto (tallennettuna nimellä `ubuntu.def`) luo kuvan, joka perustuu Ubuntu 22.04:ään yhden paketin kanssa.

```text title="ubuntu.def"
Bootstrap: docker
From: ubuntu:22.04
%post
	apt-get update
	apt-get install -y cowsay
```

Kuva voidaan rakentaa komennolla `apptainer build ubuntu.sif ubuntu.def` ja suorittaa komennolla `apptainer shell ubuntu.sif`. Nyt asennettua pakettia voidaan käyttää avaamalla komentoikkuna komennolla `echo hello | /usr/games/cowsay`. Huomaa, että `sudo` ei vaadita näiden komentojen suorittamiseen.

Alla on taulukko yleisistä docker-pohjakuvista ja niiden yhteensopivuudesta yksinkertaisten pakettien asentamiseen jakelun oletuspakettien hallintaohjelmalla Puthissa ja Mahtissa:

|Image|Tag|Works|
|-----|---|-----|
|alpine|3.6-3.19|ei|
|almalinux|8-9|kyllä|
|debian|buster-trixie|kyllä|
|centos|7|kyllä|
|opensuse/leap|15.0,15.6|ei|
|opensuse/leap|15.1-15.5|kyllä|
|redhat/ubi|8-9|kyllä|
|ubuntu|16.04-22.04|kyllä|

Joihinkin ongelmiin liittyen esimerkiksi glibc:hen, fakerootiin, tiedostojen oikeuksiin ja vanhoihin etätiedostoihin on usein vaikea löytää ratkaisu, joten muutaman erilaisen pohjakuvan kokeileminen voi olla hyvä idea ennen kuin käytät paljon aikaa vianmääritykseen.

## GPU:n käyttäminen containereista interaktiivisissa sessioissa Puthissa {#using-gpu-from-containers-in-interactive-sessions-in-puhti}

### Olemassa olevien kuvien ajaminen {#running-existing-images}

Ajaaksesi ohjelmia [kiihdytetyllä visualisoinnilla](../webinterface/accelerated-visualization.md), jotka [käyttävät GPU:ta](https://apptainer.org/docs/user/latest/gpu.html), käytä `--nv` lippua containerin käynnistykseen: `apptainer run --nv /path_to_image/image.sif`. Käyttääksesi graafista näyttöä [VirtualGL](https://virtualgl.org/)-ohjelmistolla, on myös asetettava muutamia ympäristömuuttujia. CSC:n GPU-käyttöön tarjoamissa peruskuvissa nämä ovat asetettu automaattisesti, kun container käynnistetään. Huomaa, että jos suoritat `apptainer shell` komennon sijaan `apptainer run`, `%runscript` ei suoriteta eikä tarpeellisia vgl-ympäristömuuttujia aseteta, sinun täytyy silloin asettaa ne manuaalisesti, katso [peruskuvauksien määrittelytiedostot](https://github.com/CSCfi/singularity-recipes/tree/main/visualization) lisätietoja varten.

Ohjelman helppo käynnistys voidaan tehdä luomalla `.desktop` [pikakuvaketiedosto](https://specifications.freedesktop.org/desktop-entry-spec/desktop-entry-spec-latest.html#recognized-keys) hakemistoon `$HOME/Desktop` Puhtissa. Kuvake ilmestyy sitten työpöydälle, joka käynnistää ohjelman containerissa.

Esimerkki `blender.desktop`-tiedostosta, joka käynnistää seuraavassa osiossa tarjotun esimerkkikontainerin.
```
[Desktop Entry]
Type=Application
Name=Blender
Terminal=true
Exec=apptainer run --nv /path_to_image/vgl_blender.sif
```

### Oman kuvan rakentaminen {#building-your-own-images}

Jos haluat rakentaa containereita VGL-sovelluksille itse, voit käyttää CSC:n tarjoamia peruskuvia pohjana. Näissä kuvissa on sekä grafiikkaohjain että VirtualGL valmiiksi asennettuna, jotka ovat tarpeen GPU:n käyttämiseen etänä ajettavissa graafisissa sovelluksissa.

Saatavilla olevat peruskuvat löytyvät polusta `/appl/opt/vis/vgl-base-images/` Puthissa.

Lisätietoja peruskuvien toiminnasta, katso niiden [määrittelytiedostot](https://github.com/CSCfi/singularity-recipes/tree/main/visualization).

Tässä on kommentoitu esimerkkitiedosto, joka asentaa blenderin peruskuvan päälle.

```
Bootstrap: localimage
From: /appl/opt/vis/vgl-base-images/ubuntu/22.04.sif 

%environment
	# Määritä polku binääriin, joka halutaan suorittaa aloitushetkellä
	export VGL_APPLICATION=/opt/blender-3.6.0/blender
%post
	# Kun rakennetaan fakerootilla ilman nimitiloja, emme voi muokata käyttäjiä tai ryhmiä asennuksen aikana, joten korvataan ongelmalliset binäärit dummyeilla ja toivotaan, että kaikki toimii
	cp /usr/bin/true /usr/sbin/groupadd
	cp /usr/bin/true /usr/sbin/useradd

	# Asenna blenderin riippuvuudet, selvitä mitkä kirjastot ovat tarpeen käyttämällä ldd:tä, lue virheviestejä jne.
	apt-get install -y libxi6 libxrender1 libxkbcommon0 \
	                   libxkbcommon-x11-0 libsm6 libice6

	# Asenna Blender-binääri
	cd /opt
	BLENDER_VERSION=3.6.0
	wget https://ftp.halifax.rwth-aachen.de/blender/release/Blender$(echo "$BLENDER_VERSION" | cut -d. -f1,2)/blender-$BLENDER_VERSION-linux-x64.tar.xz
	tar xf blender-$BLENDER_VERSION-linux-x64.tar.xz
	mv blender-$BLENDER_VERSION-linux-x64 /opt/blender-$BLENDER_VERSION
	rm blender-$BLENDER_VERSION-linux-x64.tar.xz
```

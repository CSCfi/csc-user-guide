
# Laajenna SD Desktop -ohjelmistoympäristö omilla Apptainer-konteillasi {#extending-sd-desktop-software-environment-with-your-own-apptainer-containers}

Tässä opetusohjelmassa käytämme cPoutaa Luodaksemme Apptainer-kontteja tuodaksemme uutta ohjelmistoa SD Desktopille.

**Vaiheet 1 ja 2** kuvaavat, kuinka asennat oman virtuaalikoneesi Apptainer-ympäristön cPoutaan. Tämä ei ole ainoa vaihtoehto, ja jos sinulla on jo Apptainer asennettuna muualla, voit ohittaa nämä vaiheet ja käyttää omaa Apptainer-ympäristöäsi.

**Vaihe 3** kuvaa, kuinka voit rakentaa oman ohjelmistokonttisi.

**Vaihe 4** esittää, kuinka kontti ladataan Allakseen.

**Vaihe 5** kuvaa, kuinka konttiin asennettavaa ohjelmistoa voidaan käyttää SD Desktopilla.

## 1. Oman Apptainer-työpenkin luominen cPoutaan {#1-creating-your-own-apptainer-workbench-to-cpouta}

Jotta voit hyödyntää kaikkia Apptainerin ominaisuuksia, sinun täytyy suorittaa se ympäristössä, missä sinulla on ylläpitäjän oikeudet. CSC:llä voit saada ylläpitäjän oikeudet virtuaalikoneille, jotka toimivat cPoutassa. cPoutan käyttöllä rakentamisprosessissa on hieman ylimääräisiä vaiheita: sinun täytyy tietää, miten käynnistää ja käyttää virtuaalikoneita cPoutassa. Toisaalta cPoutan yhteys Allas-palveluun on nopea, mikä helpottaa valmiiden konttien importtaamista SD Desktopille.

Ensimmäiseksi käynnistä virtuaalikone cPoutassa, kuten cPouta-käyttäjäoppaassa on kuvattu:

* [Virtuaalikoneen käynnistäminen cPouta-käyttöliittymän kautta](../../cloud/pouta/launch-vm-from-web-gui.md)

ja esimerkiksi nämä opetusvideot:

* [Virtuaalikoneen käynnistäminen](https://www.youtube.com/watch?v=CvoN4pv0RJQ) ja yhdistäminen siihen paikallisella macOS-läppärillä
* [Virtuaalikoneen luominen cPoutaan](https://www.youtube.com/watch?v=CIO8KRbgDoI) webinaaritallenne.

Tässä opetusohjelmassa käytämme virtuaalikonetta, joka on käynnistetty käyttämällä:

* Tyyppi: **Standard.medium**
* Instanssin Käynnistyslähde: **Kuva**
* Kuvan Nimi: **Ubuntu-22.04**

## 2. Singularityn ja Allas-työkalujen asentaminen Ubuntu 22.04 palvelimelle {#2-installing-singularity-and-allas-tools-to-ubuntu-22-04-server}

Tässä aloitetaan tilanteesta, jossa olemme kirjautuneet juuri luotuun virtuaalikoneeseemme ensimmäistä kertaa. Valmisteluvaiheina meidän täytyy asentaa virtuaalikoneeseemme **Apptainer** uusien ohjelmistokonttien luomista varten ja **allas-tools** ladataksemme luomiemme kontit Allakseen.

Singularityn asennus tehdään komennoilla:

```text
sudo apt update
sudo apt install -y software-properties-common
sudo apt-get install apt-utils
sudo add-apt-repository -y ppa:apptainer/ppa
sudo apt update
sudo apt install -y apptainer
```

Tämän jälkeen Allas-työkalut voidaan asentaa komennolla:

```text
sudo apt install python3-pip python3-dev
sudo apt-get install python3-setuptools
sudo pip3 install python-openstackclient
sudo apt install python3-swiftclient
curl https://rclone.org/install.sh | sudo bash
git clone https://github.com/CSCfi/allas-cli-utils
```

Huomaa, että tämä asennusprosessi tarvitsee tehdä vain kerran virtuaalikoneelle.

## 3. Apptainer-kontin luominen {#3-creating-an-apptainer-container}

Apptainer-kontteja voi luoda monella tapaa. Voit luoda kontin luomalla _sandboxing_-ympäristön, johon kirjaudut ja lisäät sisältöjä komentosarjoilla. Vaihtoehtoisesti voit automatisoida asennusprosessin kokoamalla kaikki komennot ja asetukset Apptainerin _määrittelytiedostoon_, joka ohjaa asennusprosessia. Yksityiskohtainen katsaus kontin rakentamiseen löytyy [Apptainer-käyttäjäoppaasta](https://apptainer.org/docs/user/main/build_a_container.html).

Täällä käytämme näiden kahden lähestymistavan yhdistelmää. Ensin käytämme yksinkertaista määrittelytiedostoa luodaksemme uuden kontin hiekkalaatikon, joka sisältää joukon työkaluja ohjelmistoasennuksia varten. Sitten avaamme komentorivisession kontin hiekkalaatikkoon ja teemme varsinaiset ohjelmistoasennukset manuaalisesti.

### 3.1 Määrittelytiedosto {#3-1-definition-file}

Avaa ensin uusi tiedosto nimeltä `ubuntu_with_inst_tools.def` komennolla:

```text
nano ubuntu_with_inst_tools.def
```

Ja kopioi-liitä uuteen tiedostoon sisältö alla olevasta esimerkkimäärittelytiedostosta:

```text
Bootstrap: docker
From: ubuntu:20.04
Stage: build

%environment
export TZ=Europe/Helsinki
export LC_ALL=C
export LC_NUMERIC=en_GB.UTF-8
export PATH="/opt/miniconda/bin:$PATH"

%help
Container based on unbuntu containing miniconda.

%runscript
# sample runscript: bamtools passing all arguments from cli: $@
# exec /opt/miniconda/bin/bamtools "$@"

%post
#commands to help installation processes
ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
apt update
apt install -y wget bzip2 git autoconf automake build-essential 
apt install -y zlib1g-dev pkg-config nano

#install conda
cd /opt
rm -fr miniconda
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh  -O miniconda.sh
bash miniconda.sh -b -p /opt/miniconda
mkdir -p /opt/tools
export PATH="/opt/tools/bin:/opt/miniconda/bin:$PATH"
conda config --add channels bioconda
conda config --add channels conda-forge
conda config --set channel_priority strict
```

### 3.2 Hiekkalaatikon luominen ja käyttö {#3-2-creating-and-using-sandbox}

Seuraavaksi käytämme tätä määrittelytiedostoa luodaksemme uuden Apptainer-hiekkalaatikon

```text
sudo apptainer build --sandbox sd_sandbox_1 ubuntu_with_inst_tools.def
```

Kun hiekkalaatikko on valmis, avaamme siihen komentorivisession. Valitsin `-w` antaa meille mahdollisuuden kirjoittaa hiekkalaatikkoon:

```text
sudo apptainer shell -w sd_sandbox_1
```

Nyt olemme sisällä Apptainer-hiekkalaatikossa ja voimme aloittaa tarvitsemiemme ohjelmistojen asennukset. Meillä on jo Conda käytettävissä, joka tarjoaa kätevän tavan asentaa monia ohjelmistotyökaluja. Esimerkiksi seuraavat komennot asentavat _bamtoolsin_ Conda-ympäristöön nimeltä _biotools_.

```text
conda init bash
bash
conda create -n biotools
conda activate biotools
conda install bamtools
```

Voisimme myös käyttää tavanomaisia asennusmenetelmiä Condan sijaan. Esimerkiksi sen sijaan, että käytämme `conda install vcftools`, voisimme tehdä vcftoolsin asennuksen komennoilla:

```text
cd /opt/tools
git clone https://github.com/vcftools/vcftools
cd vcftools/
autoreconf -i
./configure --prefix=/opt/tools
make
make install
```

Uudempi versio samtoolsista voidaan asentaa komennolla:

```text
apt install samtools
```

Pipin avulla voidaan lisätä Python-moduuleja:

```text
pip install pyhdfe
```

Kun olet valmis ohjelmistoasennusten kanssa, voit poistua hiekkalaatikosta komennolla:

```text
exit
```

Huomaa: Jos olet käynnistänyt bash-session Conda-asennuksia varten, sinun tulee antaa kaksi exit-komentoa

### 3.3 Apptainer-kuvatiedoston luominen {#3-3-creating-an-apptainer-image-file}

Nyt olemme takaisin perusvirtuaalikoneessa. Seuraavaksi muutamme hiekkalaatikon Apptainer-kuvatiedostoksi komennolla:

```text
sudo apptainer build sd_tools_1.sif sd_sandbox_1
```

Tämän jälkeen tiedostoluettelo (`ls -lh`) näyttää, että nykyinen hakemisto sisältää hiekkalaatikkohakemiston ja Apptainer-kuvatiedoston

```text
drwxr-xr-x. 18 root   root   4.0K Sep 27 12:56 sd_sandbox_1
-rwxr-xr-x   1 ubuntu ubuntu 419M Sep 27 13:43 sd_tools_1.sif
```

Huomaa, että sekä hiekkalaatikkohakemisto että Apptainer-kuvatiedosto voidaan käyttää suorittamaan äsken asentamiamme komentoja. Esimerkiksi voimme tulostaa _samtoolsin_ ohjeen molemmilla alla olevilla komennoilla:

```text
apptainer exec sd_sandbox_1 samtools 
apptainer exec sd_tools_1.sif samtools
```

## 4. Kontin lataaminen Allas/SD Connectiin {#4-uploading-container-to-allas-sd-connect}

Jotta Apptainer-konttia voidaan käyttää SD-työpöydällä, meidän täytyy salata se CSC:n julkisella avaimella ja ladata se Allakseen. Jos haluat käyttää samaa konttia myös muissa paikoissa, esimerkiksi Puhtissa ja Mahtissa, sinun tulee ladata toinen, salaamaton versio Allakseen.

Latausprosessissa käytämme Allas-työkaluja, jotka asensimme vaiheessa 2, jossa asensimme Allas-työkalut hakemistoon `$HOME/allas-cli-utils`. Ensin lisäämme tämän hakemiston komentopolkuun:

```text
export PATH=${HOME}/allas-cli-utils:${PATH}
```

Seuraavaksi avaamme yhteyden Allakseen `allas_conf`-skriptin avulla. Huomaa, että sinun pitää määritellä CSC-käyttäjätilisi `-u your-csc-account` op-kennan avulla. Tässä oletetaan, että käyttäjätili on `kkayttaj`.

```text
source ${HOME}/allas-cli-utils/allas_conf -u kkayttaj
```

Yllä oleva komento kysyy CSC-käyttäjätilin salasanan ja sen jälkeen listaa Allas-projektit, joita käyttäjätilillä on käytettävissä. Tässä tapauksessa valitsemme numeron, joka määrittää projektin _project_2000123_. Tämän jälkeen Allas-yhteydet valittuun projektiin ovat aktiivisia seuraavat kahdeksan tuntia.

Nyt voimme käyttää Allasta [a-tools](../Allas/using_allas/a_commands.md) tai [rclone](../Allas/using_allas/rclone.md) avulla. Seuraavaksi lataamme juuri luomamme konttikuvan Allakseen komennolla:

```text
a-put --sdx sd_tools_1.sif -b 2000123_apptainer_sd -m "SD Compatible. Contains bamtools, samtools and vcftools."
```

Yllä olevassa komennossa valitsin `--sdx` käytetään salataksesi kontin CSC:n julkisella avaimella. Salattu kontti tallennetaan hakemistoon `2000123_apptainer_sd`. Tässä hakemiston nimi sisältää projektinumeron (2000123) ainutlaatuisuuden varmistamiseksi ja _sd_ osoittaa, että tämä hakemisto sisältää SD Desktopille yhteensopivaa dataa. Valitsin `-m` käytetään lisäämään metatietokohteen kuvauksen, jonka a-put luo.

## 5. Apptainer-konttien käyttäminen SD Desktopilla {#5-using-apptainer-containers-in-sd-desktop}

Jotta voit käyttää luomaasi apptainer-konttia, sinun täytyy ensin ladata kontista kopio SD Desktopille _Tietoportti_-työkalulla. Kirjaudu ensin [SD Desktopille](https://sd-desktop.csc.fi) ja yhdistä siihen virtuaaliseen työpöytään, jota haluat käyttää. Avaa Tietoportti, navigoi oikeaan projektiin (`project_2000123`) ja hakemistoon (`2000123_apptainer_sd`), ja lataa Apptainer-kuvatiedosto (`sd_tools_1.sif`) SD Desktopille.

Sen jälkeen, avaa Linux-terminali SD Desktopilla. Terminalissa siirrä Apptainer-tiedosto haluamaasi paikkaan. Tässä esimerkissä se voitaisiin tehdä komennolla:

```text
cp /home/kkayttaj/Projects/SD-connect/project_2000123/2000123_apptainer_sd/sd_tools_1.sif ./
```

Nyt voisimme suorittaa esimerkiksi samtools-komennon, joka on jo asennettu konttiin.

```text
apptainer exec sd_tools_1.sif samtools
```

Yllä oleva komento tulostaa samtoolsin version 1.10 ohjeen, joka on konttiin asennettu. Huomaa, että toinen versio samtoolsista, versio 1.9, on asennettu SD Desktopilla, joten myös alla oleva komento toimisi, mutta se tulostaisi vanhemman samtools-version ohjeen:

```text
samtools --help
```

Kun käytät Apptainer-konttia, on hyvä huomata, että sillä on oma tiedostojärjestelmänsä, joka on kirjoitussuojattu. Tämän staattisen tiedostojärjestelmän lisäksi Apptainer liittää valitut isäntäjärjestelmän hakemistot konttiympäristöön. Näitä kytkentöjä voidaan käyttää datan tuomiseen konttiin ja ne ovat myös ainoita paikkoja, joihin uutta dataa voidaan kirjoittaa.

Oletuksena Apptainer liittää **kotihakemiston** (`/home/$USER`), `/tmp`, ja **työskentelyhakemiston** (`$PWD`) konttiisi ajon aikana. Jos tarvitset lisähakemistoja liitettäviksi, sinun on määriteltävä ne singularity-optiolla `-B lähdehakemisto:kohdehakemisto`.

Esimerkiksi, jos meillä on tulotiedosto `input_bam.bam` nykyisessä työskentelyhakemistossa, se on automaattisesti käytettävissä komennolle, joka suoritetaan kontin sisällä. Mutta jos tarvitsemme myös toisen tulotiedoston `reference.bed`, joka sijaitsee hakemistossa `/data`, meidän tulisi lisätä kyseinen hakemisto kytkettävien hakemistojen listalle. Esimerkiksi:

```text
apptainer -B /data:/data exec sd_tools_1.sif samtools depth -a -b /data/refrence.bed input_bam.bam > result.depth
```


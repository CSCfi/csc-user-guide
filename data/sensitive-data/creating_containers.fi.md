# SD Desktop -ohjelmistoalustan laajentaminen omilla Apptainer-konttien avulla {#extending-sd-desktop-software-environment-with-your-own-apptainer-containers}

Tässä ohjeessa käytämme cPoutaa Apptainer-konttien luomiseen, jotta voimme tuoda uutta ohjelmistoa SD Desktop -ympäristöön.

**Vaiheet 1 ja 2** kuvaavat, miten luot oman virtuaalikoneen Apptainer-ympäristöllä cPoutaan. Tämä ei ole ainoa vaihtoehto, ja jos sinulla on jo Apptainer asennettuna muualla, voit ohittaa nämä vaiheet ja käyttää omaa Apptainer-ympäristöäsi.

**Vaiheessa 3** kuvataan yksi tapa omien ohjelmistokonttien rakentamiseen.

**Vaiheessa 4** näytetään, kuinka kontti ladataan Allakseen.

**Vaiheessa 5** kerrotaan, miten konttiin asennettuja ohjelmistoja voidaan käyttää SD Desktopissa.

## 1. Oman Apptainer-työpöydän luominen cPoutaan {#1-creating-your-own-apptainer-workbench-to-cpouta}

Jotta voit hyödyntää Apptainerin kaikkia ominaisuuksia, tulee käyttää sitä ympäristössä, jossa sinulla on järjestelmänvalvojan oikeudet. CSC:llä tällaiset oikeudet saat virtuaalikoneisiin, jotka pyörivät cPoutassa. cPoutan käyttäminen rakentamiseen tuo prosessiin hieman lisävaiheita: sinun täytyy hallita virtuaalikoneiden käynnistäminen ja niihin kirjautuminen cPoutassa. Toisaalta cPoutalla on nopea yhteys Allas-palveluun, jota käytetään valmiiden konttien tuomiseen SD Desktopiin.

Ensimmäinen askel on käynnistää virtuaalikone cPoutassa cPoutan käyttäjäohjeen mukaisesti:

*  [Virtuaalikoneen käynnistäminen cPoutan verkkokäyttöliittymästä](../../cloud/pouta/launch-vm-from-web-gui.md)

sekä esimerkiksi näiden opetusvideoiden avulla:

*  [Virtuaalikoneen käynnistäminen](https://www.youtube.com/watch?v=CvoN4pv0RJQ) ja yhdistäminen siihen paikalliselta macOS-läppäriltä
*  [Virtuaalikoneen luominen cPoutassa](https://www.youtube.com/watch?v=CIO8KRbgDoI) - webinaaritallenne

Tässä ohjeessa käytämme virtuaalikonetta, joka on käynnistetty seuraavilla asetuksilla:

*  Flavor: **Standard.medium**
*  Instance Boot Source: **Image**
*  Image Name: **Ubuntu-22.04**

## 2. Singularityn ja Allas-työkalujen asentaminen Ubuntu 22.04 palvelimelle {#2-installing-singularity-and-allas-tools-to-ubuntu-22-04-server}

Tässä lähdemme tilanteesta, jossa olemme kirjautuneet vasta käynnistettyyn virtuaalikoneeseen ensimmäistä kertaa. Alkuvaiheessa tulee asentaa virtuaalikoneeseen **Apptainer** uusien ohjelmistokonttien luomiseksi sekä **allas-tools**, jotta luodut kontit voidaan ladata Allakseen.

Singularityn asennus tehdään komennoilla:

```text
sudo apt update
sudo apt install -y software-properties-common
sudo apt-get install apt-utils
sudo add-apt-repository -y ppa:apptainer/ppa
sudo apt update
sudo apt install -y apptainer
```

Tämän jälkeen Allas-työkalut asennetaan komennoilla:

```text
sudo apt install python3-pip python3-dev
sudo apt-get install python3-setuptools
sudo pip3 install python-openstackclient
sudo apt install python3-swiftclient
curl https://rclone.org/install.sh | sudo bash
git clone https://github.com/CSCfi/allas-cli-utils
```

Huomaa, että tämä asennus tarvitsee tehdä vain kerran per virtuaalikone.

## 3. Apptainer-kontin luominen {#3-creating-an-apptainer-container}

Apptainer-kontteja voi luoda monella eri tavalla. Voit luoda kontin tekemällä _sandboxin_, johon kirjaudut ja lisäät sisältöä suorittamalla asennuskomentoja. Vaihtoehtoisesti voit automatisoida asennusprosessin keräämällä kaikki komennot ja asetukset Apptainerin _määrittelytiedostoon_ (definition file), joka ohjaa asennuksen kulkua. Yksityiskohtainen katsaus konttien rakentamiseen löytyy [Apptainerin käyttäjän oppaasta](https://apptainer.org/docs/user/main/build_a_container.html).

Tässä ohjeessa käytämme näiden kahden yhdistelmää. Ensin luodaan yksinkertaisella määrittelytiedostolla uusi sandbox-kontti, jonka sisällä on ohjelmistojen asennukseen tarvittavat työkalut. Tämän jälkeen avataan shell-istunto kontin sisään ja suoritetaan tarvittavat asennukset käsin.

### 3.1 Määrittelytiedosto {#31-definition-file}

Avaa ensin tiedosto nimeltään `ubuntu_with_inst_tools.def` komennolla:

```text
nano ubuntu_with_inst_tools.def
```

Kopioi ja liitä uuteen tiedostoon alla olevan esimerkin sisältö:

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

### 3.2 Sandboxin luominen ja käyttö {#32-creating-and-using-sandbox}

Seuraavaksi käytetään tätä määrittelytiedostoa uuden Apptainer-sandboxin luomiseen:

```text
sudo apptainer build --sandbox sd_sandbox_1 ubuntu_with_inst_tools.def
```

Kun sandbox on valmis, avataan sen sisään shell-istunto. Optio `-w` mahdollistaa sandboxin muuttamisen:

```text
sudo apptainer shell -w sd_sandbox_1
```

Nyt ollaan Apptainer-sandboxin sisällä ja voidaan aloittaa tarvittavien ohjelmistojen asennus. Käytettävissä on jo Conda, jonka avulla voidaan helposti asentaa monia ohjelmistotyökaluja. Esimerkiksi seuraavilla komennoilla asennetaan _bamtools_ Conda-ympäristöön nimeltä _biotools_.

```text
conda init bash
bash
conda create -n biotools
conda activate biotools
conda install bamtools
```

Voimme käyttää myös normaaleja asennustapoja Condan sijasta. Esimerkiksi `conda install vcftools` sijaan vcf-tools voidaan asentaa näin:

```text
cd /opt/tools
git clone https://github.com/vcftools/vcftools
cd vcftools/
autoreconf -i
./configure --prefix=/opt/tools
make
make install
```

Uudempi versio samtoolsista asennetaan komennolla:

```text
apt install samtools
```

Pipillä voi asentaa Python-moduuleja:

```text
pip install pyhdfe
```

Kun kaikki tarvittavat ohjelmistot on asennettu, sandboxista poistutaan komennolla:

```text
exit
```

Huom: Jos olet käynnistänyt bash-istunnon Conda-asennuksia varten, sinun täytyy antaa exit-komento kahdesti

### 3.3 Apptainer-image tiedoston luominen {#33-creating-an-apptainer-image-file}

Nyt olemme takaisin virtuaalikoneen käyttöjärjestelmässä. Seuraavaksi muunnetaan juuri luotu sandbox Apptainer image -tiedostoksi komennolla:

```text
sudo apptainer build sd_tools_1.sif sd_sandbox_1
```

Tämän jälkeen hakemistolistauksen (`ls -lh`) perusteella hakemistossa pitäisi näkyä sekä sandbox-hakemisto että Apptainer-image tiedosto:

```text
drwxr-xr-x. 18 root   root   4.0K Sep 27 12:56 sd_sandbox_1
-rwxr-xr-x   1 ubuntu ubuntu 419M Sep 27 13:43 sd_tools_1.sif
```

Huomaa, että molempia — sekä sandboxia että Apptainer-image tiedostoa — voi käyttää asennettujen ohjelmistojen suorittamiseen. Esimerkiksi _samtools_-ohjeen voi tulostaa molemmilla komennoilla:

```text
apptainer exec sd_sandbox_1 samtools 
apptainer exec sd_tools_1.sif samtools
```

## 4. Kontin lataaminen Allakseen/SD Connectiin {#4-uploading-container-to-allas-sd-connect}

Jotta voit käyttää Apptainer-konttia SD Desktopissa, se täytyy salata CSC:n julkisella avaimella ja ladata Allakseen. Jos haluat käyttää samaa konttia myös muualla, esimerkiksi Puhtissa ja Mahtissa, täytyy Allakseen ladata lisäksi salaamaton versio.

Latausprosessissa käytetään Allas-työkaluja, jotka asennettiin vaiheessa 2, missä työkalut asennettiin hakemistoon `$HOME/allas-cli-utils`.
Ensiksi lisätään tämä hakemisto komennon PATHiin:

```text
export PATH=${HOME}/allas-cli-utils:${PATH}
```

Seuraavaksi avataan yhteys Allakseen `allas_conf`-skriptillä. Huomaa, että sinun tulee määrittää CSC-käyttäjätunnuksesi `-u your-csc-account` -valitsimella. Tässä oletetaan, että käyttäjätunnus on `kkayttaj`.

```text
source ${HOME}/allas-cli-utils/allas_conf -u kkayttaj
```

Yllä oleva komento kysyy CSC-käyttäjätunnuksen salasanan ja listaa sitten Allas-projektit, jotka käyttäjätilillä on käytettävissä.
Tässä tapauksessa valitaan projekti _project_2000123_. Tämän jälkeen Allas-yhteys valittuun projektiin pysyy voimassa seuraavat kahdeksan tuntia.

Nyt Allakseen voi yhdistää käyttäen [a-työkaluja](../Allas/using_allas/a_commands.md) tai [rclonea](../Allas/using_allas/rclone.md).
Seuraavaksi ladataan luotu kontti Allakseen komennolla:

```text
a-put --sdx sd_tools_1.sif -b 2000123_apptainer_sd -m "SD Compatible. Contains bamtools, samtools and vcftools."
```

Yllä olevassa komennossa optio `--sdx` salaa kontin CSC:n julkisella avaimella. Salattu kontti tallennetaan buckettiin `2000123_apptainer_sd`. Tässä bucketin nimi sisältää projektinumeron (2000123) yksilöllisyyden varmistamiseksi, ja _sd_ kertoo, että bucket sisältää SD Desktop -yhteensopivaa dataa. Optio `-m` lisää kuvausrivin metatietoon, jonka a-put luo.

## 5. Apptainer-konttien käyttö SD Desktopissa {#5-using-apptainer-containers-in-sd-desktop}

Jotta voit käyttää luomaasi Apptainer-konttia, sinun tulee ensin ladata siitä kopio SD Desktopiin _Data Gateway_ -työkalulla. Kirjaudu ensin [SD Desktopiin](https://sd-desktop.csc.fi) ja yhdistä haluamaasi virtuaalityöpöytään. Avaa Data Gateway, etsi oikea projekti (`project_2000123`) ja bucket (`2000123_apptainer_sd`), ja lataa Apptainer image -tiedosto (`sd_tools_1.sif`) SD Desktopiin.

Seuraavaksi avaa Linux-terminaali SD Desktopissa. Siirrä terminaalissa Apptainer-tiedosto haluamaasi hakemistoon. Tässä esimerkissä se tehdään näin:

```text
cp /home/kkayttaj/Projects/SD-connect/project_2000123/2000123_apptainer_sd/sd_tools_1.sif ./
```

Nyt voit käyttää esimerkiksi konttiin asennettua samtools-ohjelmaa näin:

```text
apptainer exec sd_tools_1.sif samtools
```

Yllä oleva komento tulostaa kontin samtools version 1.10 ohjeen. Huomaa, että SD Desktopissa on asennettuna myös toinen versio samtoolsista (1.9), joten myös seuraava komento toimii, mutta tulostaa vanhemman version ohjeen:

```text
samtools --help
```

Apptainer-konttia käytettäessä on hyvä huomioida, että sillä on oma tiedostojärjestelmänsä, joka on vain luku -tilassa. Tämän lisäksi Apptainer liittää (bind mount) tietyt hakemistot isäntäjärjestelmästä konttiympäristöön. Näiden bind mount -hakemistojen kautta dataa voidaan tuoda konttiin, ja ne ovat myös ainoat paikat, joihin pystytään kirjoittamaan uutta dataa.

Oletuksena Apptainer bind mounttaa **kotihakemiston** (`/home/$USER`), `/tmp`-hakemiston sekä **nykyisen työhakemiston** (`$PWD`) konttiin ajon aikana. Jos tarvitset muitakin hakemistoja, ne tulee määrittää erikseen singularityn `-B source-directory:target-directory` -optiolla.

Jos esimerkiksi syötetiedosto `input_bam.bam` sijaitsee nykyisessä työhakemistossa, se on automaattisesti käytettävissä kontin sisällä suoritettavassa komennossa. Jos taas tarvitset myös toisen syötetiedoston `reference.bed`, joka sijaitsee `/data`-hakemistossa, tulee kyseinen hakemisto bind-mountata käsin. Esimerkiksi näin:

```text
apptainer -B /data:/data exec sd_tools_1.sif samtools depth -a -b /data/refrence.bed input_bam.bam > result.depth
```

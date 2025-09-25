---
tags:
  - Free
catalog:
  name: Lazypipe
  description: A stand-alone pipeline for identifying viruses in host-associated or environmental samples
  description_fi: Itsenäinen putkilinja virusten tunnistamiseen isäntäperäisistä tai ympäristönäytteistä
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Puhti
---

# Lazypipe { #lazypipe }

Lazypipe on itsenäinen putkilinja virusten tunnistamiseen isäntäperäisistä tai ympäristönäytteistä. Pääpaino on bakteeri-/virussekvenssien kokoamisessa, taksonomisessa ryhmittelyssä ja taksonomisessa profiloinnissa.

[TOC]

## License { #license }

Vapaa käyttää ja avoimen lähdekoodin ohjelmisto [MIT-lisenssillä](https://raw.githubusercontent.com/OverZealous/lazypipe/master/LICENSE).

## Available { #available }

Lazypipe 3.0 on saatavilla Puhtissa.

## Usage { #usage }

Kaikki Lazypipe-putkilinjan komponentit ovat saatavilla Puhtissa. [Lazypipen kotisivu](https://www.helsinki.fi/en/projects/lazypipe) tarjoaa yksityiskohtaiset ohjeet oman Lazypipe-ympäristön luomiseksi Puhtiin, mutta tätä ei tarvita, jos käytät Lazypipe-moduulia, joka aktivoidaan seuraavilla komennoilla:

```bash
module load r-env
module load biokit
module load lazypipe
```

Tämän jälkeen Lazypipe käynnistyy komennoilla:

```bash
cp /appl/soft/bio/lazypipe/3.0/lazypipe/config.yaml config.yaml
echo tmpdir: \"$(pwd)/tmpdir\" >> config.yaml
echo res: \"$(pwd)/tmpdir\" >> config.yaml
lazypipe.pl -h
```

Tavallisesti `lazypipe.pl`-komentoa tarvitaan vain testaukseen. Varsinaisiin analyysitehtäviin Lazypipe-moduuli sisältää `sbatch-lazypipe`-komennon, jota kannattaa käyttää sen sijaan. 

`sbatch-lazypipe` on apuväline, joka luo automaattisesti asetustiedoston ja eräajotiedoston Lazypipe-ajolle ja lähettää työn Puhtin eräajojärjestelmään. Komento käyttää samoja komentorivivalitsimia kuin `lazypipe.pl`. Lisäksi `sbatch-lazypipe` pyytää käyttäjää määrittämään eräajon resurssit (laskutusprojekti, ajoaika, muisti, ytimien määrä).

Esimerkiksi suorittaaksesi [Esimerkin 1](https://www.helsinki.fi/en/projects/lazypipe/examples) Lazypipen käyttöoppaasta, sinun tulee ensin ladata lukemat ja vertailugenomi Puhtin scratch-hakemistoosi (todellisissa tapauksissa saat nämä syötetiedostot omista lähteistäsi):

```bash
mkdir /scratch/my_project/data
mkdir /scratch/my_project/hostgen
cp /appl/soft/bio/lazypipe/3.0/lazypipe/data/samples/M15small_R*.fastq /scratch/my_project/data
wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/900/108/605/GCA_900108605.1_NNQGG.v01/GCA_900108605.1_NNQGG.v01_genomic.fna.gz -P /scratch/my_project/hostgen/
```

Kun data on saatavilla, voit lähettää työn komennoilla:

```bash
cd /scratch/my_project
module load r-env
module load biokit
module load lazypipe
sbatch-lazypipe -1 data/M15/M15small_R1.fastq -S M15 -p main --anns norm\
--hostgen genomes_host/GCA_900108605.1_NNQGG.v01_genomic.fna.gz -v
```

Kun `sbatch-lazypipe` suoritetaan, se kysyy interaktiivisesti tiedot, joita tarvitaan eräajon muodostamiseen. Näihin kuuluvat seuraavat kohdat (suluissa olevia oletusarvoja käytetään, ellei uutta arvoa anneta):

*   laskutusprojekti
*   työn enimmäiskesto (oletus 24 tuntia)
*   muistivaraus (oletus 32G)
*   käytettävien laskentaydinten määrä (oletus 8)
*   sähköposti-ilmoitukset
   
Tämän jälkeen Lazypipe-työsi lähetetään eräajojärjestelmään suoritettavaksi.

## More information { #more-information }

*   [Lazypipen kotisivu](https://www.helsinki.fi/en/projects/lazypipe)
*   [Lazypipe-käyttöopas](https://bitbucket.org/plyusnin/lazypipe/wiki/UserGuide.v3.0)
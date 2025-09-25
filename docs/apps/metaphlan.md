---
tags:
  - Free
catalog:
  name: MetaPhlAn
  description: Profiling the composition of microbial communities with metagenomic data
  description_fi: Mikrobiyhteisöjen koostumuksen profilointi metagenomisen datan avulla
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Puhti
---

# MetaPhlAn { #metaphlan }



MetaPhlAn on laskennallinen työkalu, jolla profiloidaan mikrobiyhteisöjen koostumusta metagenomisista sekvensointiaineistoista. 

[TOC]

## Lisenssi { #license }

Vapaasti käytettävissä ja avoimen lähdekoodin ohjelmisto [MIT-lisenssillä](https://github.com/biobakery/MetaPhlAn2/blob/master/license.txt).

## Saatavilla { #available }

*   Puhti: 4.0.2, 4.0.3, 4.0.6, 4.1.1

## Käyttö { #usage }

Aktivoi MetaPhlAn Puhtissa suorittamalla komento:

```text
module load metaphlan
```

Peruskäytön saat näkyviin komennolla:

```text
metaphlan --help
```

MetaPhlAn osaa hakea MetaPhlAn-tietokannan ja luoda tarvitsemansa Bowtie2-indeksit automaattisesti ajon aikana, kun komento suoritetaan. Oletuksena MetaPhlAn tallentaa nämä indeksitiedostot MetaPhlAnin asennushakemistoon, mutta Puhtissa tämä ei ole mahdollista. Tästä syystä käyttäjien tulee käyttää valitsinta `--bowtie2db` määrittääkseen hakemiston, johon tietokanta- ja indeksitiedostot tallennetaan. 
 
Esimerkiksi projektissa _project_2001234_ käyttäjä voi ensin luoda hakemiston tietokantoja varten:

```text
cd /scratch/project_2001234
mkdir metaphlan_databases
```

Tietokannat voidaan myös valmistella etukäteen `--install`-valitsimella:

```text
metaphlan --install --bowtie2db metaphlan_databases
```

Tietokanta on melko suuri, ja sen lataaminen ja rakentaminen voi viedä aikaa.

Oletuksena uusin MetaPhlAn-tietokanta ladataan ja rakennetaan. Voit ladata tietyn version `--index`-parametrilla.

```text
metaphlan --install --index mpa_vJan21_CHOCOPhlAnSGB_202103 --bowtie2db metaphlan_databases
```

Ajaessasi MetaPhlAn-analyysejä sinun on lisättävä `--bowtie2db`-valitsin, ja myös `--index`, jos käytät muuta kuin oletustietokantaa. Jos tietokantaa ei löydy annetusta sijainnista, se luodaan automaattisesti.

MetaPhlAnin testisyötedatan voi ladata MetaPhlAnin GitHub-sivulta:

```text
wget https://github.com/biobakery/MetaPhlAn/releases/download/4.0.2/SRS014476-Supragingival_plaque.fasta.gz
```

Tässä esimerkissä tehtävä ajetaan interaktiivisena eräajona.

```text
sinteractive -m 16G -c 4
module load metaphlan
metaphlan --nproc 4 --bowtie2db metaphlan_databases  SRS014476-Supragingival_plaque.fasta.gz --input_type fasta > SRS014476-Supragingival_plaque_profile.txt
```

# Lisätietoja { #more-information }
*   [MetaPhlAn 4 -dokumentaatio](https://github.com/biobakery/MetaPhlAn/wiki/MetaPhlAn-4)
*   [MetaPhlAn 4 -opas](https://github.com/biobakery/biobakery/wiki/metaphlan4)
---
tags:
  - Free
catalog:
  name: Krona visualization tool
  description: Visualization tool for taxonomic classification and other hierarchical data
  description_fi: Visualisointityökalu taksonomiseen luokitteluun ja muuhun hierarkkiseen dataan
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Puhti
---

# Kronan visualisointityökalu { #krona-visualization-tool }

Krona on visualisointityökalu, jonka avulla voidaan intuitiivisesti tutkia metagenomisten luokittelujen monimutkaisten hierarkioiden suhteellisia runsaussuhteita ja luottamusarvoja. Krona yhdistää radiaalisten, tilan täyttävien esitysten muunnelman parametriseen väritykseen ja interaktiiviseen polaarikoordinaatteihin perustuvaan zoomaukseen.

Krona-kaavioita voi luoda Excel-mallipohjalla tai KronaTools-työkaluilla, jotka tukevat useita bioinformatiikan työkaluja ja raakadatan formaatteja. Interaktiiviset kaaviot ovat itsenäisiä tiedostoja ja niitä voi tarkastella millä tahansa modernilla verkkoselaimella.

[TOC]

## Lisenssi { #license }

Krona on ilmainen käyttää ja avoimen lähdekoodin ohjelmisto. Sitä jaetaan sen omalla [lisenssillä](https://raw.githubusercontent.com/marbl/Krona/master/KronaTools/LICENSE.txt).

## Saatavilla { #available }

* Puhti: 2.8.1

## Käyttö { #usage }

KronaTools-komentojen käyttöä varten lataa biokit-moduuli:

```bash
module load biokit
```

Monet bioinformatiikan työkalut tuottavat luokitteluja NCBI Taxonomy -tietokannan perusteella. Nämä luokittelut voidaan tuoda Kronaan sarkainerotelluista tiedostoista, joissa luetellaan taxonomy ID:t.

Esimerkiksi tiedosto `sample1.tsv`:

```text title="sample1.tsv"
#queryID  #taxID  #score
query1    9606    0.9
query2    9534    0.8
```

voidaan visualisoida komennolla:

```bash
ktImportTaxonomy sample1.tsv
```

Oletuksena kolme saraketta ovat _query-ID_, _taxonomy-ID_ ja _score_ (valinnainen), mutta näitä voidaan muuttaa valinnoilla `-q`,`-t` ja `-s`. Kommenttirivit (`#`) ohitetaan. Esimerkiksi [Kraken2](kraken.md)-ohjelman tulostiedosto voidaan visualisoida komennolla:

```bash
ktImportTaxonomy -q 2 -t 3 KrakenOutput -o KronaReport.html
```

Kronan visualisoinnit perustuvat HTML5:een. Niiden tarkastelua varten voit avata virtuaalityöpöydän [Puhti-selainliittymässä](../computing/webinterface/desktop.md) ja avata siellä selaimen.

Vaihtoehtoisesti voit kopioida nämä tiedostot Allaksen julkisesti saavutettavaan data-bucketiin ja tarkastella tuloksia paikallisella selaimellasi. Kopiointiin voi käyttää komentoja
[a-flip](../data/Allas/using_allas/a_commands.md#a-flip) tai [a-publish](../data/Allas/using_allas/a_commands.md#a-publish):

Esimerkiksi komento:

```bash
a-flip KronaReport.html
```

tuottaa URL-osoitteen, jonka voit kopioida selaimeen.

Lisäksi _ktImportTaxonomy_-komennon ohella on saatavilla useita sovelluskohtaisia tuontityökaluja. Esimerkiksi BLASTille (`ktImportBLAST`) ja MG-RASTille (`ktImportMGRAST`). Yleisluonteisia työkaluja on myös tekstille (`ktImportText`) ja XML-datalle (`ktImportXML`). Puhtissa voi olla hyödyllistä käyttää myös komentoa `ktImportDiskUsage` visualisoimaan, kuinka moni eri aineisto vie tilaa hakemistoissasi.

## Lisätietoja { #more-information }

* [Krona wiki](https://github.com/marbl/Krona/wiki)
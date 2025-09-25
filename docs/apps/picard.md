---
tags:
  - Free
catalog:
  name: Picard Tools
  description: Tools for working with SAM,BAM,CRAM and VCF files
  description_fi: Työkalut SAM-, BAM-, CRAM- ja VCF-tiedostojen käsittelyyn
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Puhti
---

# Picard-työkalut { #picard-tools }



Picard on komentorivityökalujen kokoelma korkean läpimenon sekvensointidatan (HTS) ja sellaisten formaattien kuin SAM/BAM/CRAM ja VCF käsittelyyn.


[TOC]

## Lisenssi { #license }

Vapaasti käytettävissä ja avoimen lähdekoodin [MIT-lisenssin](https://github.com/broadinstitute/picard/blob/master/LICENSE.txt) alaisena.

## Saatavilla { #available }


- Puhti:  2.27.4, 2.27.5, 3.0.1,  3.1.1

## Käyttö { #usage }

Picardin lataaminen: lataa moduuli:
```bash
module load picard
```

Huom: `biokit`-moduulin mukana tulee Picard-versio 2.27.5 Java-versioyhteensopivuuden vuoksi muun ohjelmiston kanssa. Uudemman Picard-version käyttöä varten lataa `picard`-moduuli.

Yhteenveto saatavilla olevista työkaluista:
```bash
picard
```

Huomaa, että Picardin ohjekirjassa komennot alkavat muodossa "java -jar
picard.jar". Puhtissa Picardia on helpointa ajaa kääreskriptin kautta,
joten korvaa tämä pelkällä `picard`.

Esimerkki:
```bash
picard SamToFASTQ I=input.bam FASTQ=output.fastq
```

Oletusarvoisesti Picard voi käyttää enintään 8 GB muistia. Jos analyysitehtäväsi
vaatii enemmän muistia, voit käynnistää Picardin komennoilla `picard16`, `picard32`
ja `picard64`, jotka varaavat vastaavasti 16, 32 tai 64 GB muistia.

Esimerkki:
```bash
picard16 SamToFASTQ I=input.bam FASTQ=output.fastq
```

Jos sinun täytyy määrittää Java-valitsimia Picardille, voit käyttää `java -jar $PICARD`.

Esimerkki:
```bash
java -Xmx128g -jar $PICARD  SamToFASTQ I=input.bam FASTQ=output.fastq
```


## Lisätietoja { #more-information }

-   [Picardin kotisivu](http://broadinstitute.github.io/picard/)
-   [Työkalujen yksityiskohtainen dokumentaatio](http://broadinstitute.github.io/picard/command-line-overview.html)
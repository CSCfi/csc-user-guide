---
tags:
  - Free
catalog:
  name: SAMtools
  description: Utilities for managing SAM/BAM formatted alignment files
  description_fi: Työkalut SAM/BAM-muotoisten kohdistustiedostojen hallintaan
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Puhti
---

# SAMtools { #samtools }



SAMtools tarjoaa työkaluja SAM- ja BAM-muotoisten kohdistusten käyttöön ja käsittelyyn. 
SAMtoolsia voi käyttää esimerkiksi indeksointiin, varianttien kutsumiseen ja kohdistusten tarkasteluun.

[TOC]

## Lisenssi { #license }

Vapaasti käytettävissä ja avoimen lähdekoodin [MIT/Expat-lisenssin](https://github.com/samtools/samtools/blob/develop/LICENSE) alaisuudessa.

## Saatavilla { #available }



Puhti: 1.9, 1.16, 1.18


## Käyttö { #usage }

SAMtoolsin käyttämiseksi Puhtissa voit käyttää alustuskomentoa:
```text
module load biokit
```

biokit-moduuli asettaa käyttöön joukon yleisesti käytettyjä bioinformatiikan työkaluja, mukaan lukien SAMtools ja Picard 
(Huomaa kuitenkin, että Puhtissa on myös bioinformatiikan työkaluja, joilla on erilliset käyttöönotto­komennot.)

Tämän jälkeen voit käynnistää samtoolsin
```
samtools
```

Voit tarkistaa saatavilla olevat samtools-versiot komennolla:

```
module spider samtools
```

Ja aktivoi haluamasi versio. Esimerkiksi:
```
module load samtools/0.1.19
```

SAMtools 1.x:n lataaminen lataa myös BCFtoolsin ja HTSlibin.

Raskaammat SAMtools-työt kannattaa suorittaa eräajoina. Alla on esimerkkieräajotiedosto 
SAMtools-työn ajamiseen Puhtissa:

```text
#!/bin/bash -l
#SBATCH --job-name=samtools
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --time=04:00:00
#SBATCH --mem=4000
#SBATCH --account=project_1234567
#SBATCH --ntasks=1

#Convert SAM file to BAM
samtools view -bS aln.sam > aln.bam

#Sort the bam file
samtools sort aln.bam aln-sorted

#Index the bam file
samtools index aln-sorted.bam
```
Yllä olevassa eräajoesimerkissä suoritetaan yksi tehtävä (-n 1). Työn enimmäiskesto on neljä tuntia 
(-t 04:00:00) ja varattu muistimäärä on noin 4 Gt (--mem=4000). Sinun on muutettava --account-asetusta 
siten, että siinä määritellään projekti, jolta laskutus tehdään.

Voit lähettää eräajotiedoston eräajojärjestelmään komennolla:
```text
sbatch batch_job_file.bash
```
Katso lisätietoja eräajojen suorittamisesta [Puhti-käyttöoppaasta](../computing/running/getting-started.md).


## Lisätietoja { #more-information }

-    [SAMtoolsin kotisivu](http://www.htslib.org/)
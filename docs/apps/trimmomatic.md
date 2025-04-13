
---
tags:
  - Free
---

# Trimmomatic

Trimmomatic suorittaa useita hyödyllisiä leikkaustehtäviä illumina paired-end- ja yksittäiselle datalle.

[TOC]

## Lisenssi {#license}

- Vapaa käyttää ja avoin lähdekoodi [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html) -lisenssin alaisuudessa.
- Lisenssi EI sovellu ohjelmistoon sisältyvien Illumina-sekvenssien sarjaan.
ILLUMINAn sekvenssit (adapterit) jne. PYSYVÄT TEKIJÄNOIKEUSSUOJATTUINA ja ovat Illumina omistuksessa, ja niitä käytetään Trimmomaticissa luvan perusteella.

## Saatavilla {#available}

- Puhti: 0.39
- [Chipster](https://chipster.csc.fi) graafinen käyttöliittymä

## Käyttö {#usage}

Trimmomatic sisältyy `biokit`-moduuliin:

```bash
module load biokit
```

Sen voi myös ladata erikseen:

```bash
module load trimmomatic
```

Trimmomatic voidaan käynnistää komennolla:

```bash
trimmomatic
```

Jos sinun tarvitsee säätää Java-asetuksia, voit käyttää muuttujaa `$TMJAR`

```bash
java <java options> -jar $TMJAR <trimmomatic options>
```

Sisällytettyjä adapterisekvenssejä ILLUMINACLIP:lle voi käyttää määrittelemällä `$ADAPTERS`, esim.:

```bash
ILLUMINACLIP:$ADAPTERS/TruSeq3-PE.fa:2:30:10
```

Trimmomaticin tehtävien tulisi olla suoritettuina joko [interaktiivisen session](../computing/running/interactive-usage.md) aikana tai erätyönä.

Esimerkki erätyön käsikirjoituksesta:

```bash
#!/bin/bash
#SBATCH --job-name=trimmomatic
#SBATCH --account=project_12345 # Korvaa projektin nimi
#SBATCH --partition=small
#SBATCH --time=00:15:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=8000

trimmomatic PE -threads $SLURM_CPUS_PER_TASK -phred64 \
forward.fq.gz reverse.fq.gz \
out_fw_paired.fq.gz out_fw_unpaired.fq.gz out_rev_paired.fq.gz out_rev_unpaired.fq.gz \
ILLUMINACLIP:$ADAPTERS/TruSeq3-PE.fa:2:30:10 \
LEADING:3 \
TRAILING:3 \
SLIDINGWINDOW:4:15 \
MINLEN:36
```

Erätyö voidaan käynnistää komennolla:

```bash
sbatch trimmomatic_script
```

## Lisätietoja {#more-information}

* [Trimmomatic kotisivu](http://www.usadellab.org/cms/?page=trimmomatic)

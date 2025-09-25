---
tags:
  - Free
catalog:
  name: Trimmomatic
  description: Trim Illumina paired-end and single-read data
  description_fi: Trimmää Illumina paired-end- ja single-end -lukudataa
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Puhti
---

# Trimmomatic { #trimmomatic }

Trimmomatic suorittaa monenlaisia hyödyllisiä trimmaustoimia Illumina paired-end- ja single-end -lukudatalle.

[TOC]

## License { #license }

- Vapaasti käytettävissä ja avoimen lähdekoodin ohjelmisto [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html) -lisenssillä.
- Lisenssi EI koske ohjelmistoon sisältyviä Illumina-sekvenssejä.
ILLUMINA-sekvenssit (adapterit) jne. OVAT YHÄ TEKIJÄNOIKEUDEN ALAISIA ja Illumina omistaa ne; niitä käytetään Trimmomaticissa luvan perusteella.

## Available { #available }

- Puhti: 0.39
- [Chipster](https://chipster.csc.fi) graafinen käyttöliittymä

## Usage { #usage }

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

Jos sinun täytyy säätää Javan asetuksia, voit käyttää muuttujaa $TMJAR

```bash
java <java options> -jar $TMJAR <trimmomatic options>
```

ILLUMINACLIP:iin sisältyviä adapterisekvenssejä voi käyttää määrittämällä $ADAPTERS, esim.:

```bash
ILLUMINACLIP:$ADAPTERS/TruSeq3-PE.fa:2:30:10
```

Trimmomatic-ajoja tulisi suorittaa joko [vuorovaikutteisessa istunnossa](../computing/running/interactive-usage.md) tai eräajona.

Esimerkki eräajon skriptistä:

```bash
#!/bin/bash
#SBATCH --job-name=trimmomatic
#SBATCH --account=project_12345 # Substitute your project name
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

Eräajo voidaan käynnistää komennolla:

```bash
sbatch trimmomatic_script
```

## More information { #more-information }

* [Trimmomaticin kotisivu](http://www.usadellab.org/cms/?page=trimmomatic)
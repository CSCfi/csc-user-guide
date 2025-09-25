---
tags:
  - Free
catalog:
  name: TopHat
  description: Splice junction mapper for RNA-Seq reads
  description_fi: RNA-Seq-lukemien liitoskohtien kartoittaja
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Puhti
---

# TopHat { #tophat }

TopHat on nopea liitoskohtien kartoittaja RNA-Seq-lukemille. Se kohdistaa RNA-Seq-lukemat nisäkäskokoisiin genomeihin käyttäen erittäin suuren läpimenon lyhytlukemakohdistinta Bowtie, ja analysoi sitten kohdistustulokset tunnistaakseen eksonien väliset liitoskohdat.

[TOC]

## Lisenssi { #license }

Vapaa käyttää ja avoimen lähdekoodin, lisensoitu [Boost Software License 1.0](https://github.com/DaehwanKimLab/tophat/blob/master/LICENSE) -lisenssillä.

## Saatavilla { #available }

-   Puhti: 2.1.1
-   [Chipster](https://chipster.csc.fi) graafinen käyttöliittymä

## Käyttö { #usage }

Puhtissa TopHat otetaan käyttöön komennolla:

```bash
module load biokit
```

Biokit-moduuli asettaa käyttöön joukon yleisesti käytettyjä bioinformatiikan työkaluja, mukaan lukien Bowtie2, TopHat2 ja Cufflinks.

TopHat-ajoja tulisi suorittaa eräajotöinä. Alla on esimerkkieräajotiedosto TopHat-ajon suorittamiseksi Puhtissa:

```bash
!/bin/bash
#SBATCH --job-name=tophat
#SBATCH --output=out_%j.txt
#SBATCH --error=err_%j.txt
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G
#SBATCH --time=24:00:00
#SBATCH --partition=small
#SBATCH --account=project_1234567

module load biokit
tophat -p $SLURM_CPUS_PER_TASK -o tophat_results Homo.sapiens_bwt2_index reads1.fq reads2.fq 
```

Yllä olevassa eräajoesimerkissä suoritetaan yksi tehtävä (`--ntasks=1`). Työ käyttää 4 ydintä (`--cpus-per-task=4`) ja 16 Gt muistia (`--mem=16G`). Työn enimmäiskesto on 24 tuntia (`--time=24:00:00`). Vaihda `--account` vastaamaan oman projektisi nimeä.

Huomaa, että TopHatille on myös kerrottava varattujen ytimien määrä. TopHatissa tämä tehdään komentoriviparametrilla `-p`. Voimme käyttää järjestelmämuuttujaa `$SLURM_CPUS_PER_TASK` vastaamaan automaattisesti `--cpus-per-task`-varauksessa annettua arvoa. Näin komentoriviä ei tarvitse muuttaa, vaikka varausta muutettaisiin.

Katso lisätietoja eräajojen ajamisesta kohdasta [Puhti user guide](../computing/running/getting-started.md).

## Tuki { #support }

[CSC Service Desk](../support/contact.md)

## Lisätietoja { #more-information }

* [TopHatin kotisivu](http://ccb.jhu.edu/software/tophat/index.shtml)
* [TopHatin käyttöohje](http://ccb.jhu.edu/software/tophat/manual.shtml)
---
tags:
  - Free
catalog:
  name: BayeScan
  description: Tool for identifying candidate loci under natural selection based on allele frequencies in populations
  description_fi: Työkalu luonnonvalinnan kohteena olevien kandidaattilokusten tunnistamiseen populaatioiden alleelifrekvenssien perusteella
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Puhti
---

# BayeScan { #bayescan }

BayeScanin tavoitteena on tunnistaa luonnonvalinnan kohteena olevat kandidaattilokukset geneettisestä datasta hyödyntämällä populaatioiden välisten alleelifrekvenssien eroja. Analyysi perustuu multinomi-Dirichlet-malliin. 

[TOC]

## Lisenssi { #license }

Vapaasti käytettävissä ja avoimen lähdekoodin [GNU GPLv3] -lisenssillä (https://www.gnu.org/licenses/gpl-3.0.html)

## Saatavuus { #available }

* Puhti: 2.1 

## Käyttö { #usage }

Käyttääksesi BayeScania, suorita ensin komento

```bash
module load biokit
```

Tämän jälkeen voit käynnistää BayeScanin esimerkiksi komennolla:

```bash
bayescan_2.1 -threads 1 test_binary_AFLP.txt 
```

bayescan_2.1-ohjelmaa käytettäessä on tärkeää määritellä säikeiden lukumäärä aina nimenomaisesti. Tämä johtuu siitä, että oletuksena BayeScan yrittää käyttää kaikkia saatavilla olevia ytimiä.

Puhti-ympäristössä BayeScan-tehtävät tulee ajaa erätöinä. Alla on esimerkkieräajotiedosto BayeScanille:

```bash
#!/bin/bash
#SBATCH --job-name=bayescan
#SBATCH --account=project_XXXXXX
#SBATCH --time=08:00:00
#SBATCH --mem=6G
#SBATCH --partition=small
#SBATCH --cpus-per-task=4
#SBATCH --nodes=1
#SBATCH --ntasks=1

module load biokit

bayescan_2.1 -threads ${SLURM_CPUS_PER_TASK} test_binary_AFLP.txt > bayescan_omp.out
```

Yllä oleva skripti varaa 8 tuntia laskenta-aikaa, 6 Gt muistia ja 4 laskentaydintä. `--account`-määrittelyn `XXXXXX` tulee korvata oman laskentaprojektisi tunnuksella. Työ voidaan lähettää eräajojärjestelmään komennolla:

```bash
sbatch script
```

Älä käytä BayeScania yli 8 ytimellä (ellei ole varmistettu, että tehtäväsi todella hyötyy suuremmasta ytimien määrästä).

Lisäohjeita erätöiden ajamiseen löytyy kohdasta [CSC:n eräajon ohjeet](../computing/running/getting-started.md)

## Lisätietoja { #more-information }

* [BayeScanin kotisivu](http://cmpg.unibe.ch/software/BayeScan/index.html)
* [BayeScanin käyttöopas](http://cmpg.unibe.ch/software/BayeScan/files/BayeScan2.1_manual.pdf)
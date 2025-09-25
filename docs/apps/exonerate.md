---
tags:
  - Free
catalog:
  name: Exonerate
  description: A generic tool for pairwise sequence comparison
  description_fi: Yleiskäyttöinen työkalu pariuttaisten sekvenssien vertailuun
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Puhti
---

# Exonerate { #exonerate }

Exonerate on yleiskäyttöinen työkalu pariuttaisten sekvenssien vertailuun. Sen avulla voit kohdistaa sekvenssejä useilla kohdistusmalleilla käyttäen joko kattavaa dynaamista ohjelmointia tai erilaisia heuristiikkoja. Voit käyttää Exoneratea esimerkiksi seuraaviin tarkoituksiin:

* cDNA:n kohdistaminen genomiseen sekvenssiin
* Proteiinin kohdistaminen genomiseen sekvenssiin
* 6-kehyksinen käännöskohdistus
* Genomien välinen kohdistus
* Kattava Smith-Waterman-Gotoh-kohdistus

[TOC]

## Lisenssi { #license }

Vapaa käyttää ja avoimen lähdekoodin [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html) -lisenssin alla.

## Saatavilla { #available }

Puhti: 2.4.0

## Käyttö { #usage }

Puhti-ympäristössä voit ottaa Exoneraten käyttöön komennolla:

```bash
module load biokit
```

biokit-moduuli ottaa käyttöön joukon yleisesti käytettyjä bioinformatiikan työkaluja, mukaan lukien Exonerate. Huomaa kuitenkin, että Puhtissa on myös muita bioinformatiikan työkaluja, joilla on erilliset käyttöönotto­komennot.

Kun `biokit`-moduuli on ladattu, `exonerate`-komennot ovat käytettävissä.

Esimerkiksi cDNA:n kohdistamiseksi genomiseen sekvenssiin voit käyttää `exonerate`-komentoa `est2genome`-mallilla:

```bash
exonerate --model est2genome query.fasta target.fasta
```

Näet `exonerate`-ohjelman komentorivivalinnat komennolla:

```bash
exonerate -h
```
 
Puhtissa suuret Exonerate-ajot tulisi suorittaa eräajona. Alla on esimerkkieräajotiedosto Exonerate-eräajon suorittamiseen Puhtissa:

```bash
#!/bin/bash
#SBATCH --job-name=exonerate_job
#SBATCH --account=<project>
#SBATCH --time=08:00:00
#SBATCH --mem=8G
#SBATCH --partition=small

module load biokit
exonerate --model est2genome query.fasta target.fasta
```

Yllä olevassa eräajoesimerkissä työn enimmäiskesto on kahdeksan tuntia (`--time=08:00:00`) ja varattu muisti 8 GB (`--mem=8G`).

Voit lähettää eräajotiedoston eräajojärjestelmään komennolla:

```bash
sbatch batch_job_file.bash
```

## Lisätietoja { #more-information }

* [Exoneraten kotisivu](https://github.com/nathanweeks/exonerate)
* [Exoneraten oppaat](https://www.animalgenome.org/bioinfo/resources/manuals/exonerate/)
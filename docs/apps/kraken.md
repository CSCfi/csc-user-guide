---
tags:
  - Free
catalog:
  name: Kraken
  description: Taxonomic sequence classification system
  description_fi: Taksonominen sekvenssiluokittelujärjestelmä
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Puhti
---

# Kraken { #kraken }

Kraken on sekvenssiluokittelija, joka liittää DNA-sekvensseihin taksonomiset tunnisteet. Kraken tarkastelee kyselysekvenssin k-merejä ja käyttää niistä saatavaa tietoa tietokantahaussa. Tietokanta mapittaa k-merit kaikkien sellaisten genomien pienimpään yhteiseen kantaisään, joiden tiedetään sisältävän kyseisen k-merin.

[TOC]

## Lisenssi { #license }

Vapaasti käytettävissä ja avoimen lähdekoodin [MIT-lisenssin](https://raw.githubusercontent.com/DerrickWood/kraken2/master/LICENSE) alainen.

## Saatavilla { #available }

- Puhti: 2.1.2 

## Käyttö { #usage }

Kraken sisältyy `biokit`-moduuliin. Ota se käyttöön komennolla:

```bash
module load biokit
```

Tämä lataa Kraken2-paketin, joka voidaan käynnistää komennolla `kraken2`. Esimerkiksi:

```bash
kraken2 --help
```

Puhtissa on saatavilla useita Kraken2-viitetietokantoja. Oletusarvoisesti Kraken2 käyttää
`standard`-tietokantaa, joka perustuu taksonomiseen informaatioon ja RefSeqin täydellisiin
genomeihin bakteeri-, arkea- ja virusdomeeneista sekä ihmisen genomiin ja kokoelmaan
tunnettuja vektoreita (UniVec_Core).

Puhtissa käytettävissä olevat tietokannat:

|Name  | Mem. request | Description    | 
|------|--------------|-----------------|
|standard| 40 GB | NCBI:n taksonominen informaatio sekä RefSeqin täydelliset genominsekvenssit bakteeri-, arkea- ja virusdomeeneista, lisäksi ihmisen genomi ja kokoelma tunnettuja vektoreita (UniVec_Core).|
|krak_microb| 44 GB | RefSeq bakteerit, arkeat, virukset, sienet ja alkueläimet |
|16S_Greengenes_k2db|  1 GB | Greengenes 16S -data |
|16S_RDP_k2db | 1 GB | RDP 16S -data |
|16S_SILVA132_k2db| 1 GB | Silva 132 16S -data |
|16S_SILVA138_k2db| 1 GB | Silva 138 16S -data |
|minikraken_8GB_20200312| 1 GB  |            |

Kraken2:n käyttäminen suuren viitetietokannan kanssa vaatii runsaasti muistia. Esimerkiksi työt standardi Kraken2-tietokannalla vaativat 40 GB muistia. Näin ollen Kraken kannattaa käytännössä aina suorittaa erätyönä. Alla on esimerkkierätyö, jossa käytetään 4 ydintä, 40 GB muistia ja 6 tunnin ajoaikaa:

```bash
#!/bin/bash -l
#SBATCH --job-name=kraken2
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --time=06:00:00
#SBATCH --partition=small
#SBATCH --ntasks=1
#SBATCH --nodes=1  
#SBATCH --cpus-per-task=4
#SBATCH --account=project_123456
#SBATCH --mem=40000

module load biokit
kraken2 -db standard --threads $SLURM_CPUS_PER_TASK input.fasta --output results.txt
```

Voit lähettää erätyötiedoston eräajojärjestelmään komennolla:

```bash
sbatch batch_job_file.bash
```

Lisätietoja erätöiden ajamisesta: katso [Puhti user guide](../computing/running/getting-started.md).

## Lisätietoja { #more-information }

* [Krakenin kotisivu](https://ccb.jhu.edu/software/kraken2/)
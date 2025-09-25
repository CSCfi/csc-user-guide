---
tags:
  - Free
catalog:
  name: HUMAnN
  description: Profiling microbial pathways with metagenomic data
  description_fi: Mikrobien aineenvaihduntareittien profilointi metagenomisella datalla
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Puhti
---

# HUMAnN { #humann }



HUMAnN on työnkulku, jolla voidaan tehokkaasti ja tarkasti profiloida mikrobien aineenvaihduntareittien läsnäolo/puuttuminen ja runsaus yhteisössä metagenomisista tai metatranskriptomisista sekvensointiaineistoista. Tämän prosessin (toiminnallinen profilointi) tavoitteena on kuvata mikrobiyhteisön ja sen jäsenten metabolinen potentiaali.

[TOC]

## Lisenssi { #license }

Vapaasti käytettävissä ja avoimen lähdekoodin, [MIT-lisenssin](https://raw.githubusercontent.com/biobakery/humann/master/LICENSE) alainen.

## Saatavilla { #available }

Puhdissa saatavilla olevat versiot: 3.0.1, 3.6, 3.8, 3.9

## Käyttö { #usage }

Puhdissa HUMAnN on asennettu konttipohjaisena sovelluksena. Aktivoi se suorittamalla komento:

```text
module load humann
humann
```

Oletusarvoisesti HUMaN yrittää tarkistaa ja päivittää MetaPhlAn-tietokannan joka suorituskerralla. Tämä epäonnistuu konttipohjaisessa asennuksessa, joten sinun tulee lisätä komentorivivalitsin:

```text
--metaphlan-options "--offline --bowtie2db /path/to/db"
```

CSC:n tarjoaman tietokannan käyttämiseksi käytä:

```text
--metaphlan-options "--offline --bowtie2db $MPA"
```

CSC tarjoaa HUMaN-tietokantojen oletusversiot. Voit käyttää niitä määrittämällä:

```text
--nucleotide-database $HUMANN_NUC
--protein-database $HUMANN_PROT
```

HUMAnN osaa hyödyntää useita suoritinytimiä. Aseta tätä varten `--cpus-per-task` haluttuun arvoon. Puhdissa voit käyttää enintään 40 ydintä. Muista myös lisätä `--threads` HUMAnN-komentoosi. Voit käyttää muuttujaa `$SLURM_CPUS_PER_TASK` vastaamaan automaattisesti pyydettyä määrää.

Esimerkkieräajon skripti (käytä oman projektisi nimeä valitsimessa `--account`)

```text
#!/bin/bash -l
#SBATCH --job-name=humann
#SBATCH --account=project_123456
#SBATCH --partition=small
#SBATCH --time=01:00:00
#SBATCH --ntasks=1  
#SBATCH --cpus-per-task=10
#SBATCH --mem=20000

# Load HUMaN module
module load humann

# Dowload a test file
wget https://github.com/biobakery/humann/raw/master/examples/demo.fastq.gz

# Run HUMaN
humann --threads=$SLURM_CPUS_PER_TASK --input demo.fastq.gz --nucleotide-database $HUMANN_NUC --protein-database $HUMANN_PROT --metaphlan-options "--offline --bowtie2db $MPA" --output demo_out
```

## Lisätietoja { #more-information }

*   [HUMAnN-kotisivu](https://huttenhower.sph.harvard.edu/humann)
*   [HUMAnN:n käyttöopas](https://github.com/biobakery/humann)
*   [HUMAnN-tutoriaali](https://github.com/biobakery/biobakery/wiki/humann3)
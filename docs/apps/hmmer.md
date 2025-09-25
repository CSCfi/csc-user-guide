---
tags:
  - Free
catalog:
  name: HMMER
  description: Toolkit to create and use sequence profile hidden Markov models
  description_fi: Työkalupakki sekvenssiprofiliin perustuvien piilotettujen Markovin mallien luomiseen ja käyttöön
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Puhti
---

# HMMER { #hmmer }

Piilotetut Markovin mallit (HMM) ovat matemaattisia työkaluja, joilla voidaan kuvata ja analysoida toisiinsa liittyviä tai samankaltaisia sekvenssialueita. 
HMM-mallit voidaan johtaa usean sekvenssin kohdistuksista siten, että ne sisältävät paikkakohtaista tietoa tiettyjen nukleotidien tai aminohappojen todennäköisyyksistä kussakin kohdistuksen kohdassa.

HMMER-paketti sisältää työkaluja sekvenssikohdistuksiin perustuviin HMM-malleihin: niiden luomiseen ja muokkaamiseen, tietokantahakujen tekemiseen sekä sekvenssikohdistusten laajentamiseen.

HMM-profiileilla tehtävät tietokantahaut voivat vaatia tavallisilla tietokoneilla hyvin pitkiä laskenta-aikoja.

[TOC]

## Lisenssi { #license }

Vapaa käyttää ja avoimen lähdekoodin [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html) -lisenssin alla.

## Saatavilla { #available }

* Puhti: 3.2.1, 3.3.2, 3.4

## Käyttö { #usage }

Käyttääksesi Puhdissa HMMERin oletusversiota, lataa biokit-moduuli:

```bash
module load biokit
```

Jos haluat käyttää jotain muuta versiota, lataa haluttu HMMER-moduulin versio. Esimerkiksi:

```bash
module load hmmer/3.2.1
```

Tämän jälkeen kunkin `hmmer`-komennon komentorivivalitsimet voi tarkistaa valitsimella `-h`. Esimerkiksi:

```bash
hmmsearch -h
```

### Pfam-tietokanta { #pfam-database }

Puhdissa voit käyttää Pfam-A-tietokantaa HMMER-komennoilla. Voit myös luoda omia HMM-tietokantoja.
Esimerkiksi proteiinisekvenssin vertailu Pfam-A HMM -tietokantaa vasten voidaan tehdä seuraavilla komennoilla.

Avaa ensin interaktiivinen eräajon istunto ja lataa biokit:

```bash
sinteractive -m 4G -c 4
module load biokit
```

Alkuperäisellä HMMER:llä voit nopeuttaa `hmmpfam`- ja `hmmserach`-komentoja käyttämällä useita
suorittimia. Käytettävien suorittimien määrä, esim. 4, annetaan valitsimella `--cpu 4`,
mutta on parempi käyttää ympäristömuuttujaa, jossa arvo on jo valmiina, *i.e.* 
`$SLURM_CPUS_PER_TASK`, jolloin se on aina linjassa eräajon skriptin pyynnön kanssa:

```bash
hmmscan --cpu $SLURM_CPUS_PER_TASK $PFAMDB/pfam_a.hmm protein.fasta > result.txt
```

Puhdissa HMMER-ajoja tulisi suorittaa interaktiivisina eräajoina tai tavallisina erätöinä. Tässä esimerkki eräajotiedostosta, joka käyttää 4 suoritinydintä:

```bash
#!/bin/bash 
#SBATCH --job-name=hmmer_job
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --time=04:00:00
#SBATCH --partition=small
#SBATCH --ntasks=1
#SBATCH --nodes=1  
#SBATCH --cpus-per-task=4
#SBATCH --account=project_123456
#SBATCH --mem=8000

module load biokit
hmmscan --cpu $SLURM_CPUS_PER_TASK $PFAMDB/pfam_a.hmm protein.fasta > result.txt
```

Työ lähetetään komennolla (missä *batch_job_file* on eräajotiedostosi nimi):

```bash
sbatch batch_job_file
```

Lisätietoja erätöiden ajamisesta: katso [Laskennan käyttöopas](../computing/running/getting-started.md).

## Lisätietoja { #more-information }

* [HMMER-käyttöopas](http://eddylab.org/software/hmmer/Userguide.pdf)
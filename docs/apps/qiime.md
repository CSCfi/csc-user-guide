---
tags:
  - Free
catalog:
  name: QIIME
  description: Package for microbial community analysis of amplicon sequencing data
  description_fi: Paketti amplicon-sekvensointidatan mikrobiyhteisöjen analysointiin
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Puhti
---

# QIIME { #qiime }

QIIME (Quantitative Insights Into Microbial Ecology) on paketti mikrobiyhteisöjen vertailuun ja analyysiin, joka perustuu ensisijaisesti monilla alustoilla tuotettuun korkean läpimenon amplicon-sekvensointidataan (esim. SSU rRNA), mutta tukee myös muuntyyppisten aineistojen (esim. shotgun-metagenomiikka) analyysia. QIIME vie käyttäjän raakadatasta alkuvaiheen analyyseihin, kuten OTU-klusterointiin, taksonomiseen luokitteluun ja OTU:iden edustajasekvensseihin perustuvien fylogeneettisten puiden rakentamiseen, ja edelleen jatkoanalyyseihin, visualisointeihin sekä julkaisulaatuisten kuvien tuottamiseen.

Vuonna 2017 julkaistiin täysin uudelleenkirjoitettu versio QIIME2. Alkuperäisen QIIME-version kehitys on päättynyt. QIIME2:n käyttöä suositellaan vahvasti useimpiin tarkoituksiin.

[TOC]

## Lisenssi { #license }

Vapaa käyttää ja avoimen lähdekoodin, [BSD 3-Clause License](https://github.com/qiime2/qiime2/blob/master/LICENSE) -lisenssillä.

## Saatavilla { #available }

- QIIME1: Puhti: 1.9.1
- QIIME2: Puhti: 2022.8, 2023.2, 2023.5, 2023.9-amplicon, 2023.9-shotgun, 2024.2-amplicon, 2024.2-shotgun, 2024.10-amplicon, 2024.10-metagenome, 2024.10-pathogenome

## Käyttö { #usage }

Lataa QIIME1-moduuli Puhtissa:

```bash
module load qiime1
```

QIIME2:n käyttöä varten tarkista saatavilla olevat versiot komennolla:

```bash
module spider qiime2
```

Lataa haluttu versio esim.:

```bash
module load qiime2/2023.9-amplicon
```

Tämän jälkeen voit käynnistää QIIME2:n komennolla:

```bash
qiime
```

## Jakelut { #distributions }

Uusimmat QIIME2-versiot ovat saatavilla eri jakeluina: amplicon/metagenome/pathogenome/tiny.
Jakelut eroavat siinä, mitkä liitännäiset niihin sisältyvät. Voit vertailla
[jakeluita](https://docs.qiime2.org/2024.10/install/#distributions) QIIME2:n
kotisivuilla.

CSC tarjoaa asennukset amplicon-, metagenome- ja pathogenome-jakeluille.

## Lisäliitännäiset { #additional-plugins }

CSC ylläpitää vain QIIME2:n perusjakeluita. Jos tarvitset liitännäisiä, joita perusjakeluihin ei sisälly, sinun on asennettava oma QIIME2 [Tykky-työkalulla](../computing/containers/tykky.md).

Valitse ensin tarpeitasi parhaiten vastaava jakelu (amplicon/metagenome/pathogenome/tiny).

Lataa vastaava [ympäristötiedosto](https://docs.qiime2.org/2024.10/install/native/).

Esimerkiksi 2024.10 amplicon -jakelulle:

```bash
wget https://data.qiime2.org/distro/amplicon/qiime2-amplicon-2024.10-py310-linux-conda.yml
```

Tarkista haluamiesi liitännäisten asennusohjeet.

Jos lisäliitännäiset voi asentaa Condalla, voit yksinkertaisesti lisätä ne ympäristötiedoston loppuun.

Jos liitännäiset vaativat lisäaskeleita, voit kopioida ne tekstitiedostoon ja käyttää
`conda-containerize update` -komentoa Tykky-dokumentaation mukaisesti.

Asennus:

```bash
module purge
module load tykky
mkdir qiime
conda-containerize new --mamba --prefix qiime qiime2-amplicon-2024.10-py310-linux-conda.yml
```

Tarvittaessa aja:

```bash
conda-containerize update qiime --post-install plugins.txt
```

## Ajo { #running }

Huomaa, että monet QIIME-tehtävät ovat laskennallisesti raskaita. Siksi nämä tehtävät tulisi suorittaa
eräajoina.

QIIME-ajot voivat olla hyvin levyintensiivisiä, erityisesti väliaikaistiedostojen käsittely, joten niille on parasta
varata nopea paikallinen levy.

Interaktiivisia eräajoja varten katso [sinteractive](../computing/running/interactive-usage.md) -dokumentaatio.

Tavallisissa eräajoissa sinun tulee varata NVMe-levytila, jota käytetään $TMPDIR-alueena.

Esimerkiksi 100 Gt paikallista levytilaa:

```text
#SBATCH --gres=nvme:100
```

Esimerkiksi alla oleva eräajon skripti suorittaa
[QIIME Moving Pictures -tutoriaalin](https://docs.qiime2.org/2019.7/tutorials/moving-pictures/#option-1-dada2)
denoising-vaiheen eräajona kahdeksaa ydintä käyttäen.

```bash
#!/bin/bash
#SBATCH --job-name=qiime_denoise
#SBATCH --account=<project>
#SBATCH --time=01:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=16G
#SBATCH --partition=small
#SBATCH --gres=nvme:100

#set up qiime
module load qiime2/2023.9-amplicon

# run task. Don't use srun in submission as it resets TMPDIR
qiime dada2 denoise-single \
  --i-demultiplexed-seqs demux.qza \
  --p-trim-left 0 \
  --p-trunc-len 120 \
  --o-representative-sequences rep-seqs-dada2.qza \
  --o-table table-dada2.qza \
  --o-denoising-stats stats-dada2.qza \
  --p-n-threads $SLURM_CPUS_PER_TASK
```

Enimmäisaika on asetettu 1 tunniksi (`--time=01:00:00`). Koska QIIME2 käyttää säikeistykseen perustuvaa rinnakkaisuutta, työ pyydetään ajamaan yhtenä tehtävänä (`--ntasks=1`), jolloin kaikkien ytimien tulee olla samalla solmulla (`--nodes=1`). Tämä yksi tehtävä käyttää kahdeksaa ydintä rinnakkaissäikeinä (`--cpus-per-task=8`), jotka voivat käyttää yhteensä enintään 16 Gt muistia (`--mem=16G`). Huomaa, että käytettävien ytimien määrä pitää määrittää myös varsinaisessa `qiime`-komennossa. Se tehdään Qiimen valinnalla `--p-n-threads`. Tässä käytämme muuttujaa `$SLURM_CPUS_PER_TASK`, joka sisältää arvon `--cpus-pre-task`. Voisimme yhtä hyvin käyttää `--p-n-threads 8`, mutta silloin on muistettava muuttaa arvoa, jos varattujen CPU:iden määrää muutetaan.

Työ lähetetään eräajojärjestelmään `sbatch`-komennolla. Jos eräajotiedoston nimi on esimerkiksi `qiime_job.sh`, lähetyskomento on:

```bash
sbatch qiime_job.sh
```
Lisätietoja eräajojen suorittamisesta löytyy [Puhti-käyttöoppaan eräajo-osiosta](../computing/running/getting-started.md).

!!! warning "Huom."
    `tab-qiime`:n käyttäminen QIIME-komentojen täydennyksen mahdollistamiseksi aiheuttaa tunnetusti ongelmia Puhtissa, joten sitä tulisi välttää.

## Lisätietoja { #more-information }

* [QIIME2-kotisivu](https://qiime2.org/)
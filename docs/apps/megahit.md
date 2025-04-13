
---
tags:
  - Free
---

# Megahit

Megahit on erittäin nopea kokoamistyökalu metagenomiikka-aineistolle.

[TOC]

## Lisenssi {#license}

Vapaa käyttää ja avoimen lähdekoodin ohjelma [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html) lisenssillä.

## Saatavilla {#available}

* Puhti: 1.2.9

## Käyttö {#usage}

Puhtissa Megahit aktivoidaan lataamalla `biokit`-ympäristö:

```bash
module load biokit
```

Käyttöohjeen saat komennolla:

```bash
megahit -h
```

Metagenomiikka-aineiston kokoaminen voi olla erittäin resurssivaatimuksista. Huomaa, ettei Meghitä tule ajaa Puhtin kirjautumissolmuilla. Suosittelemme ajamaan Megahitin erätyönä todellisia analyysitehtäviä varten.

Esimerkki Megahit-erätyöstä:

```bash
#!/bin/bash
#SBATCH --job-name=Megahit
#SBATCH --account=<project>
#SBATCH --time=12:00:00
#SBATCH --ntasks=1
#SBATCH --nodes=1
#SBATCH --output=megahit_out_8
#SBATCH --error=megahit_err_8
#SBATCH --cpus-per-task=8
#SBATCH --mem=32G
#SBATCH --partition=small

module load biokit
srun megahit -1 reads_1.fastq -2 reads_2.fastq -t $SLURM_CPUS_PER_TASK --m 32000000000 -o result_directory
```

Yllä olevassa esimerkissä `<project>` pitäisi korvata projektisi nimellä. Voit käyttää `csc-projects` tarkistaaksesi CSC-projektisi. Maksimiaika on asetettu 12 tunniksi (`--time=12:00:00`). Koska Megahit käyttää rinnakkaistusta säikeiden avulla, se käsitellään yhtenä työjoukkona, joka pitäisi suorittaa yhdellä solmulla (`--ntasks=1`, `--nodes=1`). Työ varaa kahdeksan ydintä (`--cpus-per-task=8`), jotka voivat käyttää yhteensä enintään 32 GB muistia (`--mem=32G`). Huomaa, että käytettävien ytimien määrä tulee määritellä myös varsinaisessa Megahit-komennossa. Tämä tehdään Megahit-vaihtoehdolla `-t`. Tässä tapauksessa käytämme `$SLURM_CPUS_PER_TASK`-muuttujaa, joka sisältää `--cpus-per-task` arvon (voisimme yhtä hyvin käyttää `-t 8`, mutta silloin meidän on muistettava muuttaa arvoa, jos varattujen suorittimien määrä muuttuu).

Työ lähetetään erätehtäväjärjestelmään `sbatch`-komennolla. Esimerkiksi, jos erätiedoston nimi on `megahit_job.sh`, lähetyskomento on:

```bash
sbatch megahit_job.sh 
```

Lisätietoja erätehtävien ajamisesta löytyy [Puhtin käyttäjäoppaan erätehtäväosiosta](../computing/running/getting-started.md).

## Lisätietoa {#more-information}

* [Megahit kotisivu](https://github.com/voutcn/megahit)

---
tags:
  - Free
catalog:
  name: Megahit
  description: Metagenomics assembly
  description_fi: Metagenomiikan kokoaminen
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Puhti
---

# Megahit { #megahit }

Megahit on erittäin nopea kokoamistyökalu metagenomiikka-aineistoille.

[TOC]

## Lisenssi { #license }

Vapaasti käytettävissä ja avoimen lähdekoodin ohjelmisto [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html) -lisenssillä.

## Saatavuus { #available }

* Puhti: 1.2.9

## Käyttö { #usage }

Puhtissa Megahit aktivoidaan lataamalla `biokit`-ympäristö:

```bash
module load biokit
```

Käyttöohjeen saat komennolla:

```bash
megahit -h
```

Metagenomisen datan kokoaminen voi olla hyvin resurssisyöppöä. Huomaa, että Megahitia ei tule ajaa Puhtin kirjautumissolmuilla.
Varsinaista analyysiä varten suosittelemme ajamaan Megahitin eräajona.

Esimerkki Megahit-eräajosta:

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

Yllä olevassa esimerkissä `<project>` korvataan projektisi nimellä. Voit tarkistaa CSC-projektisi komennolla `csc-projects`. Enimmäisaika on 
asetettu 12 tunniksi (`--time=12:00:00`). Koska Megahit käyttää säiepohjaista rinnakkaistusta, prosessi on yksi työ, joka suoritetaan yhdellä solmulla (`--ntasks=1`, `--nodes=1`). Työ varaa kahdeksan ydintä (`--cpus-per-task=8`), jotka voivat käyttää yhteensä enintään 32 Gt muistia (` --mem=32G`). Huomaa, että käytettävien ytimien määrä on määriteltävä myös varsinaisessa Megahit-komennossa.
Tämä tehdään Megahitin valitsimella `-t`. Tässä käytämme muuttujaa `$SLURM_CPUS_PER_TASK`, joka sisältää `--cpus-per-task`-arvon (voisimme myös käyttää `-t 8`, mutta silloin arvo pitää muistaa muuttaa, jos varattujen CPU:iden määrä muuttuu).

Työ lähetetään eräajojärjestelmään `sbatch`-komennolla. Jos eräajotiedoston nimi on `megahit_job.sh`, lähetyskomento on:

```bash
sbatch megahit_job.sh 
```

Lisätietoja erätöiden ajamisesta löytyy [Puhti-käyttöohjeen eräajoluvusta](../computing/running/getting-started.md).

## Lisätietoja { #more-information }

* [Megahitin kotisivu](https://github.com/voutcn/megahit)
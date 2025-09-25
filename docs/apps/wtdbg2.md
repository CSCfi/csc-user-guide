---
tags:
  - Free
catalog:
  name: wtdbg2
  description: Fast assembler for long-read data
  description_fi: Nopea kokoaja pitkien lukemien datalle
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Puhti
---

# wtdbg2 { #wtdbg2 }

wtdbg2 on nopea _de novo_ -kokoamistyökalu pitkien lukemien sekvenssidatalle, jonka tuottavat PacBio- tai Oxford Nanopore Technologies -sekvensointilaitteet.

[TOC]

## Lisenssi { #license }

Vapaasti käytettävissä ja avoimen lähdekoodin ohjelmisto [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html) -lisenssillä.

## Saatavilla { #available }

- Puhti: 2.5

## Käyttö { #usage }

Puhtissa wtdbg2 otetaan käyttöön lataamalla biokit-moduuli:

```bash
module load biokit
```

Tämän jälkeen käytettävissä ovat `wtdbg2`-kokoaja ja `wrpoa-cns`-konsensusohjelma. `wtdbg2` kokoaa raakalukemat ja tuottaa kontigien layoutin ja reunasekvenssit tiedostoon `prefix.ctg.lay.gz`. Suoritettava `wtpoa-cns` lukee tämän tiedoston syötteenä ja tuottaa lopullisen konsensuksen FASTA-muodossa. 

Tyypillinen työnkulku on seuraavanlainen:

```bash 
wtdbg2 -x rs -g 4.6m -t 16 -i reads.fa.gz -fo prefix
wtpoa-cns -t 16 -i prefix.ctg.lay.gz -fo prefix.ctg.fa
```

Komennossa `wtdbg2` valitsin `-g` on arvio genomin koosta ja `-x` määrittää sekvensointiteknologian; arvoja ovat mm. `rs` (PacBio RSII), `sq` (PacBio Sequel), `ccs` (PacBio CCS -lukemat) ja `ont` (Oxford Nanopore). Tämä valitsin asettaa useita parametreja ja se tulee antaa ennen muita parametreja. Jos et saa hyvää kokoamista, muita parametreja voi olla tarpeen säätää wtdbg2-manuaalin ohjeiden mukaisesti.

Suurten (yli 10 Mb) genomien kohdalla wtdbg2-kokoamisprosessi voi kestää useita tunteja tai päiviä. Puhtissa tällaiset suuret tehtävät tulee aina suorittaa eräajoina.

Alla on esimerkkieräajotiedosto _C. elegans_ -genomin kokoamiseen. 

Esimerkkiaineisto ladattiin ENA-tietokannasta seuraavilla komennoilla:

```bash
enaDataGet SRR5439404 -f fastq
mv SRR5439404/SRR5439404_subreads.fastq.gz ./
```

Varsinainen kokoamistehtävä ajettiin alla olevalla eräajolla:

```bash
#!/bin/bash
#SBATCH --job-name=wtdbg2
#SBATCH --account=<project>
#SBATCH --time=12:00:00
#SBATCH --ntasks=1
#SBATCH --nodes=1
#SBATCH --output==wtdbg2_out_32_%j
#SBATCH --error=wtdbg2_err_32_%j
#SBATCH --cpus-per-task=32
#SBATCH --mem=64G
#SBATCH --partition=small

module load biokit

wtdbg2 -x rs -g100m -t $SLURM_CPUS_PER_TASK -i SRR5439404_subreads.fastq.gz -fo c_elegas_test
wtpoa-cns -t $SLURM_CPUS_PER_TASK -i c_elegas_test.ctg.lay.gz -fo c_elegabs.ctg.fa
```

Yllä olevassa esimerkissä `<project>` tulee korvata oman projektisi nimellä. Voit tarkistaa CSC-projektisi komennolla `csc-projects`. Suurin sallittu ajoaika on asetettu 12 tuntiin (`--time=12:00:00`). Koska wtdbg2 käyttää säiepohjaista rinnakkaistusta, prosessi on yksi työ, joka tulee ajaa yhdellä solmulla (`--ntasks=1`, `--ntasks=1`). Työ varaa 32 ydintä (`--cpus-per-task=32`), jotka voivat käyttää yhteensä enintään 64 Gt muistia (`--mem=64G`). Huomaa, että käytettävien ytimien määrä pitää määritellä myös `wtdbg2`- ja `wtpoa-cns`-komennoissa. Tämä asetetaan valitsimella `-t`. Tässä käytämme muuttujaa `$SLURM_CPUS_PER_TASK`, joka sisältää `--cpus-per-task`-arvon (voisimme käyttää myös `-t 32`, mutta silloin arvon vaihtaminen pitää muistaa, jos varattujen suoritinytimien määrä muuttuu myöhemmin.

Työ lähetetään eräajojärjestelmään komennolla `sbatch`. Jos eräajotiedoston nimi on esimerkiksi `wtdbg2_job.sh`, lähetyskomento on: 

```bash
sbatch wtdbg2_job.sh 
```

Lisätietoja eräajojen ajamisesta löytyy [Puhdin käyttäjäoppaan eräajo-osiosta](../computing/running/getting-started.md).

## Lisätietoja { #more-information }

* [wtdbg2-kotisivu](https://github.com/ruanjue/wtdbg2)
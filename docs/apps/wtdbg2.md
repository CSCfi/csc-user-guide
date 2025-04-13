
---
tags:
  - Free
---

# wtdbg2

wtdbg2 on nopea _de novo_ kokoamistyökalu pitkäkestoiseen sekvenssidataan, jota tuottaa PacBio tai Oxford Nanopore Technologies -sekvensserit.

[TOC]

## Lisenssi {#license}

Vapaasti käytettävä ja avoin lähdekoodi [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html) -lisenssillä.

## Saatavuus {#available}

- Puhti: 2.5

## Käyttö {#usage}

Puhtilla wtdbg2 aktivoidaan lataamalla biokit-moduuli:

```bash
module load biokit
```

Tämän jälkeen voit käyttää `wtdbg2` assembleria ja `wrpoa-cns` konsensointikomentoja. `wtdbg2` kokoaa raakatiedot ja luo contig-mallin ja reunan sekvenssit tiedostossa `prefix.ctg.lay.gz`. Suoritettava `wtpoa-cns` käyttää tätä tiedostoa ja tuottaa lopullisen konsensuksen FASTA-muodossa.

Tyypillinen työnkulku näyttää tältä:

```bash 
wtdbg2 -x rs -g 4.6m -t 16 -i reads.fa.gz -fo prefix
wtpoa-cns -t 16 -i prefix.ctg.lay.gz -fo prefix.ctg.fa
```

`wtdbg2`-komennossa `-g` on arvioitu genomin koko ja `-x` määrää sekvensointiteknologian, joka voi olla arvoltaan `rs` PacBio RSII:lle, `sq` PacBio Sequelille, `ccs` PacBio CCS-lukemille ja `ont` Oxford Nanoporelle. Tämä optio asettaa useita parametreja ja se tulisi soveltaa ennen muita parametreja. Jos et saa hyvää kokoamista, saatat tarvita muiden parametrien hienosäätöä wtdbg2-manuaalin kuvaamalla tavalla.

Mikäli genomi on suuri (yli 10 Mb), wtdbg2:n kokoamisprosessi voi kestää useita tunteja tai päiviä. Puhtilla tällaiset suuret tehtävät tulisi aina suorittaa erätehtävinä.

Alla on esimerkki erätehtävätiedostosta _C. elegans_ genomin kokoamiseen.

Esimerkkiaineisto ladattiin ENA-tietokannasta komennoilla:

```bash
enaDataGet SRR5439404 -f fastq
mv SRR5439404/SRR5439404_subreads.fastq.gz ./
```

Varsinainen kokoamistehtävä suoritettiin alla olevalla erätehtävällä:

```bash
#!/bin/bash
#SBATCH --job-name=wtdbg2
#SBATCH --account=<project>
#SBATCH --time=12:00:00
#SBATCH --ntasks=1
#SBATCH --nodes=1
#SBATCH --output=wtdbg2_out_32_%j
#SBATCH --error=wtdbg2_err_32_%j
#SBATCH --cpus-per-task=32
#SBATCH --mem=64G
#SBATCH --partition=small

module load biokit

wtdbg2 -x rs -g100m -t $SLURM_CPUS_PER_TASK -i SRR5439404_subreads.fastq.gz -fo c_elegas_test
wtpoa-cns -t $SLURM_CPUS_PER_TASK -i c_elegas_test.ctg.lay.gz -fo c_elegabs.ctg.fa
```

Yllä olevassa esimerkissä `<project>` tulisi korvata projektisi nimellä. Voit käyttää `csc-projects` tarkistaaksesi CSC-projektisi. Maksimiaika on asetettu 12 tunniksi (`--time=12:00:00`). Koska wtdbg2 käyttää säiepohjaista rinnakkaisuutta, prosessi katsotaan yhdeksi tehtäväksi, joka tulisi suorittaa yhdellä solmulla (`--ntasks=1`). Tehtävä varaa 32 ydintä `--cpus-per-task=32`, jotka voivat käyttää yhteensä enintään 64 Gt muistia (`--mem=64G`). Huomaa, että käytettävien ytimien määrä on määriteltävä myös `wtdbg2` ja `wtpoa-cns` komennoissa. Tämä voidaan asettaa optiolla `-t`. Tässä tapauksessa käytämme `$SLURM_CPUS_PER_TASK` muuttujaa, joka sisältää `--cpus-per-task` arvon (voimme myös käyttää `-t 32`, mutta silloin meidän täytyy muistaa muuttaa arvoa, jos varattujen suorittimien määrä muuttuu myöhemmin).

Tehtävä lähetetään erätehtävien järjestelmään `sbatch` komennolla. Esimerkiksi, jos erätehtävä tiedosto on nimeltään `wtdbg2_job.sh`, niin lähetyskomento on: 

```bash
sbatch wtdbg2_job.sh 
```

Lisätietoja erätehtävien suorittamisesta löytyy [Puhtin käyttäjän oppaan erätehtäväosiosta](../computing/running/getting-started.md).

## Lisätietoa {#more-information}

* [wtdbg2 kotisivu](https://github.com/ruanjue/wtdbg2)


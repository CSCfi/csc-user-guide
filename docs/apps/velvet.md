---
tags:
  - Free
catalog:
  name: Velvet
  description: Genome assembler
  description_fi: Genomin kokoaja
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Puhti
---

# Velvet { #velvet }

Velvet on sekvenssikokoaja hyvin lyhyille lukemille.

[TOC]

## Lisenssi { #license }

Vapaasti käytettävissä ja avoimen lähdekoodin, [GNU GPLv2](https://www.gnu.org/licenses/old-licenses/gpl-2.0.html) -lisenssin alainen.

## Saatavilla { #available }

- Puhti: 1.2.10
- [Chipster](https://chipster.csc.fi) graafinen käyttöliittymä

## Käyttö { #usage }

Puhtissa Velvet-komennot alustetaan komennolla:

```bash
module load biokit
```

`velveth` (ja vastaava colorspace-versio `velveth_de`) auttaa rakentamaan aineiston `velvetg`-ohjelmaa varten. Velveth lukee joukon sekvenssitiedostoja, muodostaa hajautustaulun ja kirjoittaa ulostulohakemistoon kaksi tiedostoa, Sequences ja Roadmaps, jotka ovat tarpeen ohjelmalle Velvetg. Syntaksi on seuraava:

```bash
velveth output_directory hash_length  [[-file_format][-read_type] filename]
```

Esimerkiksi:

```bash
velveth assembly_dir 21 -shortPaired data/reads.fa
```

`velvetg` (ja vastaava colorspace-versio `velvetg_de`) on Velvetin ydin, jossa de Bruijn -graafi rakennetaan ja sitä muokataan. `velvetg`:n syntaksi on:

```bash
velvetg output_directory -options parameters
```

Esimerkki `velvetg`-komennosta:

```bash
velvetg assembly_dir -cov_cutoff 5 -read_trkg yes -amos_file yes
```
 
Kun Velvet käännettiin Puhtissa, määritettiin sallittu suurin k-mer-pituus. Mitä pidempi suurin k-mer on, sitä enemmän muistia Velvet tarvitsee (riippumatta siitä, mitä k-mer-pituutta ajossa todella käytetään). Tämän vuoksi tarjoamme useita Velvet-versioita, jotka on lueteltu alla olevassa taulukossa. Puhtissa hajautustaulussa käytettävissä oleva oletuksena suurin k-mer-pituus on 100 emästä. On kuitenkin suositeltavaa käyttää versiota, jonka sallittu maksimi k-mer on mahdollisimman lyhyt. Esimerkiksi k-mer-pituudelle 40 kannattaa käyttää `velveth_maxk50` ja `velvetg_maxk50`.

### Puhtissa saatavilla olevat Velvet-ohjelmat { #velvet-programs-available-on-puhti }

| Program 	   | max. k-mer length | type |
|------------------|-------------------|------|
| `velveth` 	   | 100 	       |normal|
| `velvetg` 	   | 100 	       |normal|
| `velveth_maxk75`   | 75 	       |normal|
| `velvetg_maxk75`   | 75 	       |normal|
| `velveth_maxk50`   | 50 	       |normal|
| `velvetg_maxk50`   | 50 	       |normal|
| `velveth_maxk35`   | 35 	       |normal|
| `velvetg_maxk35`   | 35 	       |normal|
| `velveth_de` 	   | 100 	       |colorspace|
| `velvetg_de` 	   | 100 	       |colorspace|
| `velveth_de_maxk75`| 75 	       |colorspace|
| `velvetg_de_maxk75`| 75 	       |colorspace|
| `velveth_de_maxk50`| 50 	       |colorspace|
| `velvetg_de_maxk50`| 50 	       |colorspace|
| `velveth_de_maxk35`| 35 	       |colorspace|
| `velvetg_de_maxk35`| 35 	       |colorspace|

Puhtissa Velvet-ajot tulee suorittaa eräajojärjestelmän kautta. Alla on esimerkki eräajon skriptistä Velvetille:

```bash
#!/bin/bash
#SBATCH --job-name=velvet
#SBATCH --output=put=output_velvet2.txt
#SBATCH --error=errors_velvet2.txt
#SBATCH --account=<project>
#SBATCH --time=4-00:00:00
#SBATCH --ntasks=1
#SBATCH --partition=longrun
#SBATCH --nodes=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=64G

module load biokit
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
export OMP_THREAD_LIMIT=$SLURM_CPUS_PER_TASK

velveth_maxk50 assembly_folder 45 -shortPaired -fastq temp.fastq
velvetg_maxk50 assembly_folder -ins_length 400
```

Yllä olevassa eräajon skriptissä varataan 4 laskentaydintä (`--cpus-per-task=4`) ja 64 Gt muistia neljäksi päiväksi (`--time=4-00:00:00`). Velvet voi hyödyntää säikeistettyä rinnakkaislaskentaa. Alustuskäskyn `module load biokit` jälkeen ajossa käytettävien ytimien määrä määritellään ympäristömuuttujilla `$OMP_NUM_THREADS` ja `$OMP_THREAD_LIMIT`. Tässä skriptissä nämä muuttujat asetetaan käyttäen ympäristömuuttujaa `$SLURM_CPUS_PER_TASK`, joka sisältää `--cpus-per-task`-valinnalla määritetyn arvon (tässä esimerkissä arvo on 4).

Eräajo käynnistetään komennolla:

```bash
sbatch script_file_name
```

Lisätietoja eräajojen suorittamisesta löytyy [Puhti-käyttöoppaan eräajo-osiosta](../computing/running/getting-started.md).

## Lisätietoja { #more-information }

Lisätietoja Velvetistä löytyy:

* [Velvet GitHub repository](https://github.com/dzerbino/velvet/)
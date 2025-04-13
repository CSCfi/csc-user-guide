
---
tags:
  - Free
---

# SPAdes

SPAdes on pienten genomien kokoaja lyhyille lukujonoille. SPAdes toimii Illuminan tai IonTorrentin lukujonojen kanssa ja pystyy tuottamaan hybridi-koosteita käyttäen PacBio-, Oxford Nanopore- ja Sanger-lukujonoja.

SPAdes (`spades.py`) sisältää useita erillisiä moduuleja:

* BayesHammer – lukujonovirheen korjaustyökalu Illumina-lukujonoille, joka toimii hyvin sekä yksisolu- että vakiotietoaineistoissa.
* IonHammer – lukujonovirheen korjaustyökalu IonTorrent-datalle, joka toimii myös molemmille tietotyyppien kanssa.
* SPAdes – iteratiivinen lyhyen lukun genomin kokoamisosio; K-arvot valitaan automaattisesti luku pituudesta ja tietoaineistotyypistä.
* MismatchCorrector – työkalu, joka parantaa tulosjätösten ja niin sanottujen lyhyiden inokulointien virheprosentteja; tämä moduuli käyttää BWA-työkalua [Li H. ja Durbin R., 2009]; MismatchCorrector on oletusarvoisesti pois päältä, mutta suosittelemme sen päälle kytkemistä.

Suosittelemme SPAdesin käyttöä yhdessä BayesHammerin/IonHammerin kanssa korkealaatuisten kokoamisten saavuttamiseksi. Jos kuitenkin käytät omaa lukujonovirheenkorjaustyökalua, on mahdollista kytkeä virheenkorjausmoduuli pois päältä. Myös vain lukujonovirheenkorjausvaiheen käyttö mahdollista, jos aiot käyttää muuta kokoajaa.

Yleiskäyttöisen SPAdesin lisäksi on olemassa erityisiä SPAdes-parametriasetuksia:

* Coronaspades (`coronaspades.py`)
* Metaviralspades (`metaviralspades.py`)
* Rnaviralspades (`rnaviralspades.py`)
* Metagenomiikka (`metaspades.py`)
* Plasmidien kokoaminen (`plasmidspades.py`)
* RNA-Seq -kokoaminen (`rnaspades.py`)

Lisätietoja löytyy [SPAdes-dokumentaatiosta](https://ablab.github.io/spades/installation.html).

[TOC]

## License {#license}

Ilmainen käyttää ja avoimen lähdekoodin [GNU GPLv2](https://www.gnu.org/licenses/old-licenses/gpl-2.0.html) lisenssillä.

## Available {#available}

- Puhti: 3.15.5, 4.0.0

## Usage {#usage}

Puhtissa SPAdes aktivoidaan lataamalla `spades`-moduuli.

```bash
module load spades/<version>
```

Käyttöohjeita saat käyttämällä komentoa:

```bash
spades.py -h
```

Kokoamistehtävät voivat vaatia paljon resursseja, joten SPAdes-tehtäviä ei tule koskaan ajaa Puhtin kirjautumissolmuilla. Suosittelemme ajamaan SPAdesin eräajona todellisissa analyysitehtävissä.

Esimerkki SPAdes-eräajotiedostosta:

```bash
#!/bin/bash
#SBATCH --job-name=SPAdes
#SBATCH --account=<project>
#SBATCH --time=12:00:00
#SBATCH --ntasks=1
#SBATCH --nodes=1
#SBATCH --output==spades_out
#SBATCH --error=sprdes_err
#SBATCH --cpus-per-task=8
#SBATCH --mem=32G
#SBATCH --partition=small

module load biokit
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK 
srun spades.py --pe1-1 reads_R1.fastq.gz --pe1-2 reads_R2.fastq.gz -t $SLURM_CPUS_PER_TASK -o SpadesResult
```

Yllä olevassa esimerkissä `<project>` tulee korvata projektisi nimellä. Voit käyttää `csc-projects` tarkistaaksesi CSC-projektisi. Enimmäisaika on asetettu 12 tunniksi (`--time=12:00:00`). Koska SPAdes käyttää säikeisiin perustuvaa rinnakkaisuutta, prosessi katsotaan yhdeksi työksi, joka tulisi suorittaa yhdellä solmulla (`--ntasks=1`, `--nodes=1`). Työ varaa kahdeksan ydintä `--cpus-per-task=8` ja voi käyttää yhteensä enintään 32 Gt muistia (`--mem=32G`). Huomaa, että käytettävien ytimien määrä tulee määritellä sekä `$OMP_NUM_THREADS` ympäristömuuttujalla että varsinaisessa `spades.py`-komennossa (vaihtoehto `-t`). Tässä tapauksessa käytämme `$SLURM_CPUS_PER_TASK` -muuttujaa, joka sisältää `--cpus-per-task` arvon. Voisimme myös käyttää `export OMP_NUM_THREADS=8` ja `-t 8`, mutta silloin meidän on muistettava muuttaa arvoja, jos varattujen suorittimien määrä muuttuu.

Työ ajetaan eräajojärjestelmään `sbatch`-komennolla. Esimerkiksi, jos eräajotiedoston nimi on `spades_job.sh`, silloin komento on:

```bash
sbatch spades_job.sh 
```

Lisätietoja eräajojen suorittamisesta löydät [Puhtin käyttäjäoppaan eräajojen osiosta](../computing/running/getting-started.md).

## More information {#more-information}

* [SPAdes-verkkosivusto](https://ablab.github.io/spades/)
* [SPAdes GitHub -arkisto](https://github.com/ablab/spades)


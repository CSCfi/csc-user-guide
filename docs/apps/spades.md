---
tags:
  - Free
catalog:
  name: SPAdes
  description: Genome assembly
  description_fi: Genomin kokoaminen
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Puhti
---

# SPAdes { #spades }

SPAdes on lyhyiden lukemien kokoaja pienille genomeille. SPAdes toimii Illumina- tai IonTorrent-lukemilla ja pystyy tuottamaan hybridikokoamisia käyttäen PacBio-, Oxford Nanopore- ja Sanger-lukemia.

SPAdes (`spades.py`) sisältää useita erillisiä moduuleja:

* BayesHammer – Illumina-lukemien virheenkorjaustyökalu, joka toimii hyvin sekä yksittäissolu- että vakiotietoaineistoilla.
* IonHammer – IonTorrent-datan virheenkorjaustyökalu, joka toimii myös sekä yksittäissolu- että vakiotietoaineistoilla.
* SPAdes – iteratiivinen lyhytlukukokoamisen moduuli; K-arvot valitaan automaattisesti lukeman pituuden ja aineistotyypin perusteella.
* MismatchCorrector – työkalu, joka parantaa virheellisten emäsvastaavuuksien ja lyhyiden indelien määriä tuloksena syntyvissä kontigeissa ja skaffoldeissa; tämä moduuli käyttää BWA-työkalua [Li H. and Durbin R., 2009]; MismatchCorrector on oletuksena pois päältä, mutta suosittelemme ottamaan sen käyttöön.

Suosittelemme ajamaan SPAdesin yhdessä BayesHammerin/IonHammerin kanssa korkealaatuisten kokoamisten saamiseksi. Jos kuitenkin käytät omaa virheenkorjaustyökalua, virheenkorjausmoduulin voi kytkeä pois päältä. Halutessasi voit myös käyttää pelkkää lukemien virheenkorjausvaihetta ja suorittaa kokoamisen toisella kokoajalla.

Yleiskäyttöisen SPAdesin lisäksi on saatavilla SPAdesin erityisiä parametrisarjoja:

* Coronaspades (`coronaspades.py`)
* Metaviralspades (`metaviralspades.py`)
* Rnaviralspades (`rnaviralspades.py`)
* Metagenomiikka (`metaspades.py`)
* Plasmidien kokoaminen (`plasmidspades.py`)
* RNA-Seq-kokoaminen (`rnaspades.py`)

Katso lisätietoja [SPAdesin dokumentaatiosta](https://ablab.github.io/spades/installation.html).

[TOC]

## License { #license }

Vapaa käyttää ja avoimen lähdekoodin lisenssillä [GNU GPLv2](https://www.gnu.org/licenses/old-licenses/gpl-2.0.html).

## Available { #available }

- Puhti: 3.15.5, 4.0.0

## Usage { #usage }

Puhtissa SPAdes aktivoidaan lataamalla `spades`-moduuli.

```bash
module load spades/<version>
```

Käyttöohjeen saa komennolla:

```bash
spades.py -h
```

Kokoamistehtävät voivat olla hyvin resurssia vaativia, joten älä koskaan aja oikeita SPAdes-töitä Puhtin kirjautumissolmuissa. Kaikissa varsinaisissa analyyseissä suosittelemme ajamaan SPAdesin eräajona.

Esimerkkieräajotiedosto SPAdesille:

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

Yllä olevassa esimerkissä `<project>` tulee korvata omalla projektinimelläsi. Voit käyttää `csc-projects`-komentoa CSC-projektiesti tarkistamiseen.
Enimmäisaika on asetettu 12 tunniksi (`--time=12:00:00`). Koska SPAdes käyttää säikeistykseen perustuvaa rinnakkaisuutta, prosessi on yksi työ, joka suoritetaan yhdellä solmulla (`--ntasks=1`, `--nodes=1`). Työ varaa kahdeksan ydintä (`--cpus-per-task=8`), jotka voivat käyttää yhteensä enintään 32 GB muistia (`--mem=32G`). Huomaa, että käytettävien ytimien määrä pitää määrittää sekä ympäristömuuttujalla `$OMP_NUM_THREADS` että varsinaisessa `spades.py`-komennossa (valinta `-t`). Tässä käytämme muuttujaa `$SLURM_CPUS_PER_TASK`, joka sisältää parametrin `--cpus-per-task` arvon. Voisimme yhtä hyvin käyttää asetusta `export OMP_NUM_THREADS=8` ja `-t 8`, mutta silloin arvot täytyy muistaa päivittää, jos varattujen suorittimien määrää muutetaan.

Työ lähetetään eräajojärjestelmään `sbatch`-komennolla. Jos eräajotiedoston nimi on esimerkiksi `spades_job.sh`, lähetyskomento on:

```bash
sbatch spades_job.sh 
```

Lisätietoja eräajojen suorittamisesta löytyy [Puhtin käyttäjäoppaan eräajoja käsittelevästä osiosta](../computing/running/getting-started.md).

## More information { #more-information }

*	[SPAdesin verkkosivusto](https://ablab.github.io/spades/)
*	[SPAdes GitHub -repositorio](https://github.com/ablab/spades)
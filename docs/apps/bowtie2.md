---
tags:
  - Free
catalog:
  name: Bowtie2
  description: Short read aligner
  description_fi: Lyhyiden lukujen kohdistin
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Puhti
---

# Bowtie2 { #bowtie2 }

Bowtie2 on erittäin nopea ja muistitehokas lyhyiden lukujen kohdistin. Se kohdistaa lyhyet DNA-jaksot (reads) ihmisen genomiin yli 25 miljoonan 35-bp luennan tuntinopeudella. Bowtie2 indeksoi genomin Burrows-Wheelern indeksillä pitääkseen muistinkulutuksen pienenä: tyypillisesti noin 2.2 GB ihmisen genomille (2.9 GB pareittaisille luennoille).

Bowtiesta on saatavilla kaksi versiota: Bowtie2 ja Bowtie. Uudempi Bowtie2-ohjelma poikkeaa merkittävästi edeltäjästään Bowtiesta. Esimerkiksi komentorivivalitsimet ovat näissä kahdessa työkalussa erilaiset.

[TOC]

## License { #license }

Vapaa käyttää ja avoimen lähdekoodin ohjelmisto, lisensoitu [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html) -lisenssillä.

## Available { #available }

-   Puhti: 2.3.5.1, 2.4.1, 2.4.4, 2.5.3
-   Chipsterin graafinen käyttöliittymä

## Usage { #usage }

Puhtilla Bowtie2 otetaan käyttöön osana `biokit`-modulikokoelmaa:

```bash
module load biokit
```

biokit-moduli asettaa käyttöön joukon yleisesti käytettyjä bioinformatiikan työkaluja, mukaan lukien Bowtie2. Huomaa kuitenkin, että Puhtissa on myös muita bioinformatiikan työkaluja, joiden käyttöönotto tapahtuu erillisellä komennolla.

Tyypillisessä Bowtie2-ajossa viitegenomi pitää ensin indeksoida komennolla `bowtie2-build`. Tämä kannattaa tehdä scratch-hakemistossa kotihakemiston sijaan. Esimerkiksi:

```bash
bowtie2-build genome.fa genome
```

Vaihtoehtoisesti voit käyttää `chipster_genomes` -komentoa ladataksesi valmiiksi lasketut bowtie2-indeksit CSC:n Chipster-palvelimelta Puhtiin:

```bash
chipster_genomes bowtie2
``` 

Kun viitegenomi on ladattu tai indeksoitu, varsinainen kohdistustehtävä voidaan käynnistää komennolla `bowtie2`. Esimerkiksi yksipäisille luennoille tämä voidaan tehdä komennolla:

```bash
bowtie2 -x genome -U reads.fq -S output.sam
```

Pareittaiselle aineistolle (paired-end) minimisyntaksi on:

```bash
bowtie2 -x genome -1 first_read_set.fq -2 second_read_set.fq -S output.sam
``` 

### Example batch script for Puhti { #example-batch-script-for-puhti }

Puhtissa `bowtie`- ja `bowtie2`-työt tulee ajaa eräajoina. Alla on esimerkkieräajon tiedosto Bowtie2:n pareittaisen kohdistuksen ajamiseen Puhtissa. Uudet Bowtie2-versiot skaalaavat hyvin, joten voit käyttää tehokkaasti jopa 16 ydintä eräajossa.

Huomaa, että eräajotiedostossa on määriteltävä käytettävä projekti.
Voit tarkistaa kaikki projektit, joihin kuulut, komennoilla `groups` tai
`csc-projects`. Käytä [MyCSC](https://my.csc.fi) -palvelua saadaksesi tarkempaa tietoa yksittäisestä projektista.

```bash
#!/bin/bash -l
#SBATCH --job-name=bowtie2
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --time=04:00:00
#SBATCH --partition=small
#SBATCH --ntasks=1
#SBATCH --nodes=1  
#SBATCH --cpus-per-task=16
#SBATCH --account=project_123456
#SBATCH --mem=16000

module load biokit
bowtie2-build genome.fasta genome
bowtie2 -p $SLURM_CPUS_PER_TASK -x genome -1 reads_1.fq -2 reads_2.fq > output.sam
```

Yllä olevassa eräajoesimerkissä suoritetaan yksi tehtävä (`--ntasks=1`). Bowtie2-ajo käyttää 16 ydintä (`--cpus-per-task=16`) ja yhteensä 16 GB muistia (`--mem=16000`). Työn enimmäiskesto on neljä tuntia (`--time=04:00:00`).
Kaikki ytimet varataan yhdeltä laskentasolmulta (`--nodes=1`).
Esimerkissä käytettävä projekti on `project_123456`. Tämä arvo tulee korvata oman laskentaprojektisi nimellä.

Voit lähettää eräajotiedoston eräajojärjestelmään komennolla:

```bash
sbatch batch_job_file.bash
```

Katso lisätietoja eräajojen suorittamisesta [Puhti user guide](../computing/running/getting-started.md) -oppaasta.

## References { #references }

Kun käytät Bowtie2:ta, viittaa seuraavasti:

> Langmead B, Salzberg S. Fast gapped-read alignment with Bowtie 2. Nature Methods. 2012, 9:357-359.

## Support { #support }

[CSC Service Desk](../support/contact.md)

## More information { #more-information }

Lisätietoja Bowtie2:sta löytyy [Bowtie2 home page](https://github.com/BenLangmead/bowtie2/blob/master/README.md) -sivulta.
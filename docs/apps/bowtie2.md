
---
tags:
  - Free
---

# Bowtie2

Bowtie2 on erittäin nopea ja vähän muistia käyttävä lyhyiden lukujen kohdistustyökalu. Se kohdistaa lyhyet DNA-sekvenssit (luennat) ihmisen genomiin nopeudella yli 25 miljoonaa 35-bp lukua tunnissa. Bowtie2 käyttää Burrows-Wheeler -indeksiä genomin indeksoimiseen, jotta muistijalanjälki pysyy pienenä: tyypillisesti noin 2,2 Gt ihmisen genomille (2,9 Gt paarikohtaiseen kohdistukseen).

Saatavilla on kaksi Bowtien versiota: Bowtie2 ja Bowtie. Uudempi Bowtie2 eroaa merkittävästi esisarjastaan Bowtie:stä. Esimerkiksi komentorivin vaihtoehdot ovat erilaiset näille kahdelle työkalulle.

[TOC]

## Lisenssi {#license}

Vapaa käyttää ja avoimen lähdekoodin [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html) -lisenssillä.

## Saatavilla {#available}

-  Puhti: 2.3.5.1, 2.4.1, 2.4.4, 2.5.3
-  Graafinen käyttöliittymä Chipster

## Käyttö {#usage}

Puhtissa Bowtie2 voidaan ottaa käyttöön osana `biokit`-moduulikokoelmaa:

```bash
module load biokit
```

Biokit-moduuli asentaa valikoiman yleisesti käytettyjä bioinformatiikan työkaluja, mukaan lukien Bowtie2. Huomaa kuitenkin, että Puhtissa on muita bioinformatiikan työkaluja, joita käytetään erillisellä asennuskomennolla.

Tyypillisessä Bowtie2-ajossa sinun on ensin indeksoitava referenssigenomi `bowtie2-build`-komennolla. Tämä pitäisi tehdä "scratch"-hakemistossa kodin sijaan. Esimerkiksi:

```bash
bowtie2-build genome.fa genome
```

Vaihtoehtoisesti voit käyttää `chipster_genomes`-komentoa ladataksesi valmiiksi lasketut bowtie2-indeksit CSC:n Chipster-palvelimelta Puhtiin:

```bash
chipster_genomes bowtie2
```

Kun referenssigenomi on ladattu tai indeksoitu, varsinainen kohdistustyö voidaan käynnistää `bowtie2`-komennolla. Yksikertaisten lukuparien osalta tämä voidaan tehdä seuraavasti:

```bash
bowtie2 -x genome -U reads.fq -S output.sam
```

Paariparilliselle datalle minimaalinen Bowtie2-syntaksi on:

```bash
bowtie2 -x genome -1 first_read_set.fq -2 second_read_set.fq -S output.sam
```

### Esimerkki eräajotiedosto Puhtille {#example-batch-script-for-puhti}

Puhtissa `bowtie` ja `bowtie2` -työt tulee suorittaa eräajona. Alla on esimerkki eräajotiedostosta, joka suorittaa Bowtie2-paarikohtaisen kohdistuksen Puhtilla. Uudet Bowtie2-versiot skaalautuvat hyvin, joten voit tehokkaasti käyttää jopa 16 ydintä eräajossasi.

Huomaa, että eräajotiedoston on määritettävä käytettävä projekti.
Voit tarkistaa kaikki projektit, joihin kuulut, komennolla `groups` tai
`csc-projects`. Käytä [MyCSC](https://my.csc.fi) -sivustoa saadaksesi tarkempia tietoja tietystä projektista.

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

Yllä olevassa eräajon esimerkissä suoritetaan yksi tehtävä (`--ntasks=1`). Bowtie2-työ käyttää 16 ydintä (`--cpus-per-task=16`) yhteensä 16 GB muistia (`--mem=16000`). 
Työn enimmäiskesto on neljä tuntia (`--time=04:00:00`).
Kaikki ytimet ovat yhdeltä laskentasolmultra (`--nodes=1`).
Esimerkissä käytettävä projekti on `project_123456`. Tämä arvo pitäisi korvata oman laskentaprojektisi nimellä.

Voit lähettää eräajotiedoston eräajojärjestelmään komennolla:

```bash
sbatch batch_job_file.bash
```

Katso lisätietoja eräajojen suorittamisesta [Puhtin käyttäjän oppaasta](../computing/running/getting-started.md).

## Viittaukset {#references}

Kun käytät Bowtie2:ta, viittaa:

> Langmead B, Salzberg S. Fast gapped-read alignment with Bowtie 2. Nature Methods. 2012, 9:357-359.

## Tuki {#support}

[CSC palvelupiste](../support/contact.md)

## Lisätietoja {#more-information}

Lisätietoja Bowtie2:sta löytyy [Bowtie2 kotisivulta](https://github.com/BenLangmead/bowtie2/blob/master/README.md).

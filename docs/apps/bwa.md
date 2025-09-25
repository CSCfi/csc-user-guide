---
tags:
  - Free
catalog:
  name: BWA
  description: Short read aligner
  description_fi: Lyhyiden lukemien kohdistin
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Puhti
---

# BWA { #bwa }

Burrows–Wheeler Aligner (BWA) on tehokas ohjelma, joka kohdistaa suhteellisen lyhyitä nukleotidisekvenssejä pitkää referenssisekvenssiä vasten, kuten ihmisen genomia. Se toteuttaa kolme algoritmia: BWA-MEM (`mem`), BWA-Backtrack (`aln`) ja BWA-SW (`bwasw`). BWA-Backtrack toimii alle 200 bp mittaisille kyselysekvensseille. Kahta muuta algoritmia käytetään pidemmille lukemille aina noin 100 kbp:hen asti. BWA-MEM:iä suositellaan yli 70 gb pituisille lukemille. Kaikki algoritmit tekevät aukollista kohdistusta.

BWA:ta voidaan käyttää sekä single-end- että paired-end-lukemien kohdistamiseen referenssigenomiin tai sekvenssijoukkoon.

[TOC]

## License { #license }

Vapaa käyttää ja avoimen lähdekoodin ohjelmisto [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html) -lisenssillä.

## Available { #available }

- Puhti: 0.7.17
- [Chipster](https://chipster.csc.fi) graafinen käyttöliittymä

## Usage { #usage }

Puhtissa BWA otetaan käyttöön osana `biokit`-modulikokoelmaa:

```bash
module load biokit
```

Biokit-modulit asettavat käyttöön joukon yleisesti käytettyjä bioinformatiikan työkaluja, mukaan lukien BWA. Huomaa kuitenkin, että Puhtissa on myös muita bioinformatiikan työkaluja, joilla on erilliset käyttöönotto­komennot.

BWA-komentojen perussyntaksi on:

```bash
bwa <command> [options]
```

### BWA-indeksit { #bwa-indexes }

CSC ei ylläpidä valmiiksi laskettuja BWA-indeksejä referenssigenomeille Puhtissa, mutta voit tarkistaa, tarjoavatko Chipsterissä käytettävät genomi­paketit valmiin indeksin haluamallesi genomille. Tämä onnistuu komennolla:

```
chipster_genomes bwa
``` 

Jos sopivaa genomi-indeksiä ei löydy, ensimmäinen vaihe BWA-kohdistuksen tekemisessä on referenssigenomin lataaminen ja indeksointi. Huomaa, että `$HOME`-hakemistosi on usein liian pieni kokonaisten genomien käsittelyyn. Sen sijaan analyysi kannattaa tehdä Puhti-projektisi scratch-hakemistossa.

Voit ladata referenssigenomin Puhtiin esimerkiksi `ensemblfetch`- tai `wget`-komennolla. Esimerkiksi:

```bash
ensemblfetch homo_sapiens
```

Yllä oleva komento noutaa ihmisen genomisekvenssin tiedostoon `Homo_sapiens.GRCh38.dna.toplevel.fa`. Voit laskea tälle tiedostolle BWA-indeksit komennolla:

```bash
bwa index -a bwtsw Homo_sapiens.GRCh38.dna.toplevel.fa
```

Huomaa, että pienille, alle 2 GB:n referenssigenomeille voit käyttää nopeampaa "is"-indeksointialgoritmia (`bwa index -a is`)

### Single-end-kohdistus { #single-end-alignment }

Kun indeksointi on valmis, voit suorittaa single-end-lukemien kohdistuksen komennolla:

```bash
bwa mem Homo_sapiens.GRCh38.dna.toplevel.fa reads.fastq > aln.sam
```

Jos haluat käyttää `aln`- (BWA-Backtrack) algoritmia, kohdistus tehdään kahdessa vaiheessa.

Laske ensin varsinainen kohdistus:

```bash
bwa aln Homo_sapiens.GRCh38.dna.toplevel.fa reads.fastq > aln_sa.sai
```

Tulostiedosto on BWA:n `.sai`-muodossa, jonka voit muuntaa SAM-muotoon `bwa samse` -komennolla:

```bash
bwa samse Homo_sapiens.GRCh38.dna.toplevel.fa aln_sa.sai reads.fastq > aln.sam
```

### Paired-end-kohdistus { #paired-end-alignment }

Jos käytät MEM-algoritmia, voit tehdä paired-end-kohdistuksen yhdellä komennolla:

```bash
bwa mem Homo_sapiens.GRCh38.dna.toplevel.fa read1.fq read2.fq > aln.sam
```

BWA-Backtrack-algoritmissa tulee ensin suorittaa erillinen kohdistusajo kummallekin lukutiedostolle:

```bash
bwa aln Homo_sapiens.GRCh38.dna.toplevel.fa reads1.fq > aln1.sai
bwa aln Homo_sapiens.GRCh38.dna.toplevel.fa reads2.fq > aln2.sai
```

Kaksi `.sai`-kohdistustiedostoa yhdistetään `bwa sampe` -komennolla:

```bash
bwa sampe Homo_sapiens.GRCh38.dna.toplevel.fa aln1.sai aln2.sai reads1.fq reads2.fq > aln.sam
```

### BWA-eräajojen suorittaminen Puhtissa { #running-bwa-batch-jobs-on-puhti }

Puhtissa BWA-ajot tulee suorittaa eräajoina. Alla on esimerkki eräajotiedostosta BWA-ajon suorittamiseen Puhtissa:

```bash
#!/bin/bash
#SBATCH --job-name=bwa
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --time=12:00:00
#SBATCH --ntasks=1
#SBATCH --nodes=1  
#SBATCH --cpus-per-task=8
#SBATCH --mem=32000
#SBATCH --account=your_project_name

#load the bio tools
module load biokit

# Index the reference genome
bwa index -a bwtsw Homo_sapiens.GRCh38.dna.toplevel.fa

# Run the alignnments
bwa mem -t $SLURM_CPUS_PER_TASK Homo_sapiens.GRCh38.dna.toplevel.fa reads1.fq reads2.fq > aln.sam
```

Yllä olevassa eräajoesimerkissä suoritetaan yksi BWA-tehtävä (`--ntasks=1`). BWA-ajo käyttää 8 ydintä (`--cpus-per-task=8`) ja yhteensä 32 GB muistia (`--mem=32000`). Ajolle on sallittu enintään 12 tuntia (`--time 12:00:00`). Kaikki ytimet varataan yhdeltä laskentasolmulta (`--nodes=1`). Resurssivarausten lisäksi sinun on määritettävä eräajosi laskutusprojekti korvaamalla `your_project_name` oman projektisi nimellä. Voit tarkistaa Puhtissa käytössäsi olevat projektit komennolla `csc-projects`.

Voit lähettää eräajotiedoston ajonhallintajärjestelmään komennolla:

```bash
sbatch batch_job_file.bash
```

Katso lisätietoja eräajoista [Puhti user guide](../computing/running/getting-started.md) -oppaasta.

## Lisätietoja { #more-information }

Lisätietoja BWA:sta:

* [BWA home page](http://bio-bwa.sourceforge.net/index.shtml)
* [BWA manual](http://bio-bwa.sourceforge.net/bwa.shtml)
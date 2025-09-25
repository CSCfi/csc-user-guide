---
tags:
  - Free
catalog:
  name: STAR
  description: Short read aligner
  description_fi: Lyhyiden lukujen kohdistin
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Puhti
---

# STAR { #star }


STAR (Spliced Transcripts Alignment to a Reference) on nopea NGS-lukujen kohdistin RNA-seq-dataan.

[TOC]

## License { #license }

Vapaasti käytettävissä ja avoimen lähdekoodin, [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html) -lisenssin alla.

## Available { #available }



Puhti: 2.7.10a, 2.7.11a

## Usage { #usage }

Alla luetellut `STAR`-komennot aktivoidaan lataamalla `biokit`-moduuli.

```bash
module load biokit
```

Ennen kuin voit ajaa varsinaisen kohdistusajon, sinun on indeksoitava fasta-muodossa oleva referenssigenomi. Puhti-ympäristössä referenssigenomin indeksien työkopiot sekä kaikki suuret tiedostot tulisi tallentaa hakemistoon /scatch.

Käytön helpottamiseksi aseta ympäristömuuttuja osoittamaan /scratch-hakemistoosi. (Korvaa esimerkissä käytetty polku oikealla polulla.)
```bash
export SCRATCH=/scratch/project_12345/$USER
```

Luo hakemisto referenssigenomin indeksille:
```bash
mkdir $SCRATCH/star-genome
```

Tämän jälkeen indeksointi voidaan tehdä komennolla:
```bash
STAR --runMode genomeGenerate --genomeDir $SCRATCH/star-genome --genomeFastaFiles /path/to/genome/genome.fasta --runThreadN 2
```

Kun indeksointi on valmis, varsinainen kohdistustehtävä voidaan käynnistää. STAR tuottaa tulostiedostot kiinteillä tiedostonimillä. Tämän vuoksi suositellaan, että jokainen STAR-ajo suoritetaan uudessa, tyhjässä hakemistossa. Puhtissa tämä uusi ajohakemisto kannattaa luoda projektisi /scratch-hakemistoon. Uuden, nimeltä _starjob1_, hakemiston voi luoda komennolla:
```bash
mkdir $SCRATCH/starjob1
```

Tämän jälkeen varsinainen kohdistusajo voidaan käynnistää komennoilla:
```bash
cd $SCRATCH/starjob1
STAR --genomeDir $SCRATCH/star-genomes --readFilesIn my_reads.fastq
```

STARin oletusparametrit ovat tyypillisiä, kun kohdistetaan 2x76- tai 2x101-pituisia Illumina-lukuja ihmisen genomiin.

Puhtissa kaikki laskentatehtävät tulee suorittaa eräajoina (batch). Eräajoissa voidaan hyödyntää myös säiepohjaista rinnakkaisuutta. Alla on esimerkkieräajoskripti STARille. Ajo käyttää kuutta laskentaydintä yhdeltä laskentasolmulta. Muistivaraus on 24 Gt. Huomaa, että sinun on muutettava `--account`-asetus vastaamaan projektiasi.
```bash
#!/bin/bash -l
#SBATCH --job-name=STAR
#SBATCH --output=STAR.stdout
#SBATCH --error=STAR.stderr
#SBATCH --partition=small
#SBATCH --ntasks=1
#SBATCH --nodes=1
#SBATCH --cpus-per-task=6
#SBATCH --account=project_1234567
#SBATCH --mem=24000

export SCRATCH=/scratch/project_12345/$USER

# calculate indexes. You don't need to recalculte the indexes if they already exist.
mkdir $SCRATCH/star-genome
STAR --runMode genomeGenerate --genomeDir $SCRATSCH/star-genome --genomeFastaFiles /path/to/genome/genome.fasta --runThreadN $SLURM_CPUS_PER_TASK

# Run the mapping task
STAR --genomeDir $SCRATCH/star-genome --readFilesIn my-reads.fastq --runThreadN $SLURM_CPUS_PER_TASK
```

Eräajoskripti käynnistetään komennolla sbatch. Esimerkiksi:
```bash
sbatch starjob1.sh
```

## More information { #more-information }

*   [STAR-käyttöopas](https://github.com/alexdobin/STAR/blob/master/doc/STARmanual.pdf)
*   [STAR-kotisivu](https://github.com/alexdobin/STAR/)
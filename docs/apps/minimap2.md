---
tags:
  - Free
catalog:
  name: Minimap2
  description: Short read aligner
  description_fi: Lyhyiden lukemien kohdistin
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Puhti
---

# Minimap2 { #minimap2 }

Minimap2 on nopea yleiskäyttöinen kohdistusohjelma, jolla voidaan kartoittaa DNA- tai pitkät mRNA-sekvenssit suurta viitetietokantaa vasten.
Sitä voi käyttää seuraaviin tarkoituksiin:

* tarkkojen lyhyiden lukemien kohdistukseen (mieluiten yli 100 emäksen pituiset)
* 1 kb:n genomilukemien kohdistukseen noin 15 %:n virhetasolla (esim. PacBio- tai Oxford Nanopore -genomilukemat)
* täyspitkien, kohinaisten Direct RNA- tai cDNA-lukemien kohdistukseen
* koontien contigien tai läheisesti sukua olevien, satojen megabastien pituisten kokonaiskromosomien kohdistukseen ja vertailuun

[TOC]

## Lisenssi { #license }

Vapaa käyttää ja avoimen lähdekoodin [MIT-lisenssin](https://raw.githubusercontent.com/lh3/minimap2/master/LICENSE.txt) alaisena.

## Saatavilla { #available }

* Puhti: 2.24, 2.28
* Chipsterin graafinen käyttöliittymä

## Käyttö { #usage }

Puhti-ympäristössä Minimap2 on käytettävissä osana `biokit`-modulikokoelmaa:

```bash
module load biokit
```

biokit-moduli ottaa käyttöön joukon yleisesti käytettyjä bioinformatiikan työkaluja, mukaan lukien Minimap2. Huomaa kuitenkin, että Puhtissa on myös muita bioinformatiikan työkaluja, joilla on erilliset latauskomennot.
Kun biokit-moduli on ladattu, Minimap2 käynnistyy komennolla:

```bash
minimap2
```

Ilman valitsimia `minimap2` ottaa syötteenä viitetietokannan ja kyselysekvenssitiedoston ja tuottaa karkean kohdistuksen ilman emästason kohdistusta (eli ei CIGAR-tietoja) PAF-muodossa:

```bash
minimap2 ref.fa query.fq > approx-mapping.paf
```

Jos haluat tulosteen SAM-muodossa, voit käyttää valitsinta `-a`.

Eri aineistotyypeille Minimap2 täytyy virittää optimaalisen suorituskyvyn ja tarkkuuden saavuttamiseksi.
Valitsimella `-x` voit käyttää tapauskohtaisia, Minimap2:n kehittäjien ennalta määrittelemiä ja suosittelemia parametrisarjoja.
 
### Kohdista pitkät meluisat genomilukemat (_map-pb_ ja _map-ont_) { #map-long-noisy-genomic-reads-map-pb-and-map-ont }

* PacBio-alalukemat (_map-db_):

```bash
minimap2 -ax map-pb ref.fa pacbio-reads.fq > aln.sam
```

* Oxford Nanopore -lukemat (_map-ont_):

```bash
minimap2 -ax map-ont ref.fa ont-reads.fq > aln.sam 
```

### Kohdista pitkät mRNA-/cDNA-lukemat (splice) { #map-long-mrna-cdna-reads-splice }

* PacBio Iso-Seq/perinteinen cDNA

```bash
minimap2 -ax splice -uf ref.fa iso-seq.fq > aln.sam
``` 

* Nanopore 2D cDNA-seq

```bash
minimap2 -ax splice ref.fa nanopore-cdna.fa > aln.sam
```

* Nanopore Direct RNA-seq

```bash
minimap2 -ax splice -uf -k14 ref.fa direct-rna.fq > aln.sam
```
 
* kohdistus SIRV-kontrolliin

```bash
minimap2 -ax splice --splice-flank=no SIRV.fa SIRV-seq.fa
```

### Etsi päällekkäisyyksiä pitkien lukemien välillä (_ava-pb_ ja _aca-ont_) { #find-overlaps-between-long-reads-ava-pb-and-aca-ont }

* PacBio-lukemien päällekkäisyys

```bash
minimap2 -x ava-pb reads.fq reads.fq > ovlp.paf
```

* Oxford Nanopore -lukemien päällekkäisyys

```bash
minimap2 -x ava-ont reads.fq reads.fq > ovlp.paf
```

### Kohdista lyhyet tarkat genomilukemat (sr) { #map-short-accurate-genomic-reads-sr }

Huomaa, että Minimap2 ei toimi hyvin lyhyiden splicattujen lukemien kanssa.

* single-end-kohdistus

```bash
minimap2 -ax sr ref.fa reads-se.fq > aln.sam
```

* paired-end-kohdistus

```bash
minimap2 -ax sr ref.fa read1.fq read2.fq > aln.sam
```

* paired-end-kohdistus

```bash
minimap2 -ax sr ref.fa reads-interleaved.fq > aln.sam 
```

### Koko genomin/koontien kohdistus (_asm5_) { #full-genome-assembly-alignment-asm5 }

* koonti koontia vasten

```bash
minimap2 -ax asm5 ref.fa asm.fa > aln.sam
```

## Esimerkkieräajotiedosto Puhtiin { #example-batch-script-for-puhti }

Puhtissa Minimap2-ajoja suositellaan ajettavaksi eräajoina. Alla on esimerkkieräajotiedosto
Minimap2:n paired-end-kohdistuksen ajamiseen Puhtissa.

```bash
#!/bin/bash -l
#SBATCH --job-name=minimap2
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --time=04:00:00
#SBATCH --partition=small
#SBATCH --ntasks=1
#SBATCH --nodes=1
#SBATCH --cpus-per-task=8
#SBATCH --account=<project>
#SBATCH --mem=16000

module load biokit
minimap2 -t $SLURM_CPUS_PER_TASK -ax splice -uf ref.fa iso-seq.fq > aln.sam
```

Yllä olevassa eräajoesimerkissä ajetaan yksi tehtävä (`--ntasks=1`). Minimap2-ajo
käyttää 8 ydintä (`--cpus-per-task=8`) ja yhteensä 16 Gt muistia (`--mem=16000`).
Ajon enimmäiskesto on neljä tuntia (`--time=04:00:00`). Kaikki ytimet
varataan yhdeltä laskentasolmulta (`--nodes=1`). Resurssivarausten lisäksi
sinun on määritettävä eräajon laskutettava projekti. Tämä tehdään korvaamalla
`<project>` oman projektisi nimellä. Voit tarkistaa, mitä projekteja sinulla on Puhtissa,
komennolla `csc-projects`.

Voit lähettää eräajotiedoston ajonhallintajärjestelmään komennolla:

```bash
sbatch batch_job_file.bash
```

Lisätietoja eräajojen ajamisesta: [Puhti user guide](../computing/running/getting-started.md)

## Tuki { #support }

[CSC Service Desk](../support/contact.md)

## Lisätietoja { #more-information }

* Lisätietoja Minimap2:sta löytyy [Minimap2-kotisivulta](https://lh3.github.io/minimap2/).
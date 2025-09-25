---
tags:
  - Free
catalog:
  name: Chipster_genomes
  description: Tool to download aligner indexes used by Chipster to Puhti
  description_fi: Työkalu Chipsterin käyttämien kohdistinindeksien lataamiseen Puhtiin
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Puhti
---

# Chipster_genomes { #chipster_genomes }

Chipster_genomes on apuväline Chipster-ohjelmistossa käytettyjen genomi-indeksien lataamiseen Puhtiin.
CSC ylläpitää Puhtissa useita lyhytlukujen kohdistimia (esim. BWA, Bowtie2, STAR), mutta ei valmiiksi laskettuja viitegenomien indeksejä. Oletuksena käyttäjien tulee tuoda ja indeksoida itse käyttämänsä viitegenomit.

Chipster-palvelimella on kuitenkin useiden kohdistimien indeksejä joukolle yleisesti käytettyjä viiteorganismeja.

Chipsterissä käytetty genomidata ja indeksit perustuvat Ensembl- ja Ensembl Genomes -tietokantojen aineistoihin. 
Chipsterissä kuitenkin mukana ovat vain ne sekvenssit (kromosomit), joille on määritetty karyotyyppi. 
Lisäksi GTF-tiedostoista poistetaan negatiiviset sijaintiarvot.

Näin ollen Chipster-palvelimelta ladattu data voi joissakin tapauksissa poiketa suoraan Ensemblistä saadusta datasta.

[TOC]

## Lisenssi { #license }

Vapaa käyttää ja avoimen lähdekoodin.
 
## Saatavuus { #available }

Saatavilla Puhtissa.

## Käyttö { #usage }

Työkalu `chipster_genomes` sisältyy `biokit`-moduuliin, joten ottaaksesi sen käyttöön sinun on ensin suoritettava valmistelukomento:

```bash
module load biokit
```

Tämän jälkeen voit käyttää komentoa `chipster_genomes`. Komento tarvitsee kaksi parametria:

* Tiedosto- tai indeksityyppi (bed, gtf, fasta, bowtie, bowtie2, BWA, Hisat2, TopHat2)
* Lajin nimi

Jos komento käynnistetään ilman argumentteja, se luettelee ensin käytettävissä olevat datatyypit ja pyytää valitsemaan yhden niistä.
Sen jälkeen luetellaan kyseiselle datatyypille saatavilla olevat lajit, ja työkalu pyytää käyttäjää valitsemaan niistä yhden.

```bash
chipster_genomes
```

Vaihtoehtoisesti datatyyppi voidaan antaa ensimmäisenä argumenttina ja lajin nimi toisena argumenttina.
Esimerkiksi Danio_rerio.GRCz11:n BWA-indeksit voi noutaa komennolla:

```bash
chipster_genomes bwa Danio_rerio.GRCz11
```

Huomaa, että indeksitiedostot voivat olla varsin suuria, joten data kannattaa tavallisesti ladata `/scratch`-levyalueellesi.
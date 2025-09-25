---
tags:
  - Free
catalog:
  name: Illumina BaseSpace
  description: Command line client for retrieving data from the Illumina BaseSpace environment
  description_fi: Komentorivityöline datan hakemiseen Illumina BaseSpace -ympäristöstä
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Puhti
---

# Illumina BaseSpace { #illumina-basespace }

Illumina BaseSpace -komentoriviasiakas, `bs`, mahdollistaa datan noutamisen Illumina BaseSpace -ympäristöstä Puhtiin.

[TOC]

## Lisenssi { #license }

Ohjelmistoa voi käyttää maksutta.

## Saatavilla { #available }

* Puhti: 1.0.0 

## Käyttö { #usage }

Lataa ensin biokit-moduuli:

```bash
module load biokit
```

Kun biokit on ladattu, Illumina BaseSpace -komentoriviasiakas käynnistyy komennolla:

```bash
bs
```

Palvelun käyttämiseksi sinulla on oltava tili [Illumina BaseSpace -palvelussa](https://emea.illumina.com/products/by-type/informatics-products/basespace-sequence-hub.html).

Ensimmäisenä vaiheena sinun on määritettävä todennus, jotta pääset käsiksi tietoihisi Illumina BaseSpace -palvelussa. Tämä tehdään ajamalla komento:

```bash
bs auth
```

Todennustiedot tallennetaan kotihakemistoosi Puhtissa (`$HOME/.basespace/default.cfg`). Näin todennus tarvitsee tehdä vain kerran.

Tämän jälkeen voit aloittaa työskentelyn Illumina-datasi kanssa. Esimerkiksi saatavilla olevat aineistot voidaan luetella komennolla:

```bash
bs list datasets
```

Yksittäisen aineiston voi ladata Puhtiin komennolla:

```bash
bs download dataset -i dataset_id -o local_download_dir
```

## Lisätietoja { #more-information }

Yksityiskohtaisempaa tietoa Illumina BaseSpace -asiakkaan käytöstä löytyy alla olevista linkeistä:

* [bs-esimerkit](https://developer.basespace.illumina.com/docs/content/documentation/cli/cli-examples)
* [bs-yleiskatsaus](https://developer.basespace.illumina.com/docs/content/documentation/cli/cli-overview)
---
tags:
  - Free
catalog:
  name: SALMON
  description: Program to produce transcript-level quantification estimates from RNA-seq data
  description_fi: Ohjelma RNA-seq-datan transkriptitason kvantifiointiarvioiden tuottamiseen
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Puhti
---

# SALMON { #salmon }

Salmon on nopea ohjelma, joka tuottaa erittäin tarkkoja, transkriptitason kvantifiointiarvioita RNA-seq-datasta. Tarkkuus ja nopeus perustuvat useisiin innovaatioihin, kuten kvasi-kartoituksen käyttöön (perinteisten lukukohdistusten tarkat mutta nopeasti laskettavat korvikkeet) sekä laajasti rinnakkaistettuun stokastiseen kollapsoituun variaatiopäättelyyn. Tuloksena on monipuolinen työkalu, joka sopii hyvin moniin työnkulkuihin. Voit esimerkiksi käyttää kvasi-kartoitusalgoritmia antamalla Salmonille raakatason sekvensointiluvut, tai, jos se on kätevämpää, voit syöttää Salmonille valmiit kohdistukset (esim. suosikkikohdistimesi tuottaman lajittelemattoman BAM-tiedoston); molemmissa tapauksissa se käyttää samaa nopeaa, alan huipputason päättelyalgoritmia arvioidakseen kokeesi transkriptitason runsaudet.

!!! info "Huomautus"
    Salmon toimii kartoittamalla (kvasi-kartoitus) sekvensointiluvut suoraan transkriptomiin. Tämä tarkoittaa, että Salmon-indeksi tulee rakentaa kohdetranskriptien joukolle, ei taustalla olevan eliön genomiin. Jos indeksointi vaikuttaa kestävän hyvin kauan tai kuluttavan valtavasti muistia (mikä ei pitäisi tapahtua), varmista, ettet yritä rakentaa indeksiä eliösi genomille!

[TOC]

## Lisenssi { #license }

Vapaasti käytettävissä ja avoimen lähdekoodin, lisensoitu [GNU GPLv3]:n mukaisesti (https://www.gnu.org/licenses/gpl-3.0.html).

## Saatavilla { #available }

- Puhti: 0.14.2, 0.99.0b2, 1.1.0, 1.4.0, 1.9.0

## Käyttö { #usage }

Puhtissa komento `salmon` aktivoidaan lataamalla Salmon-moduuli.

```bash
module load salmon
```

Käyttöohjeen saat komennolla:

```bash
salmon --help
```

!!! info "Huomautus"
    biokit-moduulin lataaminen tuo käyttöön vanhemman Salmon-version, joka tulee Trinityn mukana.
    Jos haluat käyttää uusinta Salmon-versiota, lataa Salmon-moduuli suoraan kuten yllä.

## Lisätietoja { #more-information }

* [Salmonin dokumentaatio](https://salmon.readthedocs.io/en/latest/)

---
tags:
  - Free
---

# BamTools

BamTools tarjoaa sekä ohjelmoijan API:n että loppukäyttäjän työkalupaketin BAM-tiedostojen käsittelyyn.

[TOC]

## Lisenssi {#license}

Vapaa käyttää ja avoimen lähdekoodin [MIT-lisenssillä](https://raw.githubusercontent.com/pezmaster31/bamtools/master/LICENSE)

## Saatavuus {#available}

-   Puhti: 2.5.2
-   Chipster graafinen käyttöliittymä

## Käyttö {#usage}

Puhtilla BamTools voidaan ottaa käyttöön osana biokit-moduulikokoelmaa:

```bash
module load biokit
```

Biokit-moduuli määrittää joukon yleisesti käytettyjä bioinformatiikan työkaluja. Huomaa kuitenkin, että Puhtilla on muita bioinformatiikan työkaluja, joilla on erillisiä asetuskomentoja.

BamToolsin syntaksi on:

```
bamtools COMMAND ARGUMENTS
```

Saatavilla olevat bamtools-komennot:

- `convert`         Muuntaa BAM:in ja useiden muiden formaattien välillä
- `count`           Tulostaa kohdistusten lukumäärän BAM-tiedostossa
- `coverage`        Tulostaa peitto-tilastot syötteenä olevasta BAM-tiedostosta
- `filter`          Suodattaa BAM-tiedostoja käyttäjän määrittelemien kriteerien mukaan
- `header`          Tulostaa BAM-otsikkotiedot
- `index`           Luo indeksi BAM-tiedostolle
- `merge`           Yhdistää useita BAM-tiedostoja yhdeksi tiedostoksi
- `random`          Valitsee satunnaisia kohdistuksia olemassa olevista BAM-tiedostoista, tarkoitettu enemmän testaustyökaluiksi.
- `resolve`         Ratkaisee parittain luetut kohdistukset (merkitsee IsProperPair-lipun tarpeen mukaan)
- `revert`          Poistaa kaksoiskappaleiden merkit ja palauttaa alkuperäiset emäslaadut
- `sort`            Lajittelee BAM-tiedoston tiettyjen kriteerien mukaan
- `split`           Jakaa BAM-tiedoston käyttäjän määrittelemän ominaisuuden perusteella, luoden uuden BAM-tulostetiedoston jokaiselle löydetylle arvolle
- `stats`           Tulostaa perustilastoja syötteenä olevista BAM-tiedostoista

Lisätietoja tietystä komennosta saa suorittamalla käskyn:

```
bamtools help COMMAND
```

## Tuki {#support}

[CSC Service Desk](../support/contact.md)

## Lisätietoja {#more-information}

Lisätietoja BamToolsista löytyy [BamToolsin kotisivulta](https://github.com/pezmaster31/bamtools).

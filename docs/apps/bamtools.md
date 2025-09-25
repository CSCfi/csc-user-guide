---
tags:
  - Free
catalog:
  name: BamTools
  description: Tools for working with BAM formatted files
  description_fi: Työkalut BAM-muotoisten tiedostojen käsittelyyn
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Puhti
---

# BamTools { #bamtools }

BamTools tarjoaa sekä ohjelmoijille API:n että loppukäyttäjille työkalupaketin BAM-tiedostojen käsittelyyn.

[TOC]

## Lisenssi { #license }

Vapaasti käytettävissä ja avoimen lähdekoodin, [MIT-lisenssin](https://raw.githubusercontent.com/pezmaster31/bamtools/master/LICENSE) alaisuudessa.

## Saatavilla { #available }

-   Puhti: 2.5.2
-   Chipsterin graafinen käyttöliittymä

## Käyttö { #usage }

Puhti-järjestelmässä BamTools voidaan ottaa käyttöön osana biokit-moduulikokoelmaa:

```bash
module load biokit
```

Biokit-moduuli asettaa käyttöön joukon yleisesti käytettyjä bioinformatiikan työkaluja. Huomaa kuitenkin, että Puhtissa on myös muita bioinformatiikan työkaluja, joilla on erilliset käyttöönottokomennot.

BamToolsin syntaksi on:

```
bamtools COMMAND ARGUMENTS
```

Käytettävissä olevat bamtools-komennot:

- `convert`         Muuntaa BAMin ja useiden muiden muotojen välillä
- `count`           Tulostaa kohdistusten lukumäärän BAM-tiedostosta/-tiedostoista
- `coverage`        Tulostaa kattavuustilastot syöte-BAM-tiedostosta
- `filter`          Suodattaa BAM-tiedostoja käyttäjän määrittelemien kriteerien perusteella
- `header`          Tulostaa BAM-otsaketiedot
- `index`           Luo indeksin BAM-tiedostolle
- `merge`           Yhdistää useita BAM-tiedostoja yhdeksi tiedostoksi
- `random`          Valitsee satunnaisia kohdistuksia olemassa olevista BAM-tiedostoista; tarkoitettu lähinnä testauskäyttöön.
- `resolve`         Käsittelee parittaiset lukemat (asettaa IsProperPair-lipun tarvittaessa)
- `revert`          Poistaa duplikaattimerkinnät ja palauttaa alkuperäiset emäslaadut
- `sort`            Lajittelee BAM-tiedoston tietyn kriteerin mukaan
- `split`           Jakaa BAM-tiedoston käyttäjän määrittelemän ominaisuuden mukaan, luoden uuden BAM-tiedoston kullekin löydetylle arvolle
- `stats`           Tulostaa perustilastoja syöte-BAM-tiedostosta/-tiedostoista

Lisätietoja tietystä komennosta saat suorittamalla komennon:

```
bamtools help COMMAND
```

## Tuki { #support }

[CSC Service Desk](../support/contact.md)

## Lisätietoja { #more-information }

Lisätietoja BamToolsista löytyy [BamToolsin kotisivulta](https://github.com/pezmaster31/bamtools).
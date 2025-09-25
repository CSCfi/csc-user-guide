---
tags:
  - Free
catalog:
  name: BioPerl
  description: Perl environment with bioperl extension
  description_fi: Perl-ympäristö BioPerl-laajennuksella
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Puhti
---

# BioPerl { #bioperl }

BioPerl on kokoelma Perl-moduuleja, jotka helpottavat bioinformatiikan sovelluksiin tarkoitettujen Perl-skriptien kehittämistä. Sellaisenaan se ei sisällä valmiita, heti käytettävissä olevia ohjelmia samaan tapaan kuin monet kaupalliset paketit ja ilmaiset verkkopohjaiset käyttöliittymät. Toisaalta BioPerl tarjoaa uudelleenkäytettäviä Perl-moduuleja, jotka helpottavat Perl-skriptien kirjoittamista sekvenssien käsittelyyn, tietokantoihin pääsyä eri tiedostomuodoissa sekä erilaisten molekyylibiologisten ohjelmien ajamista ja niiden tulosten jäsentämistä. Näin BioPerl mahdollistaa sellaisten skriptien kehittämisen, joilla voidaan analysoida suuria määriä sekvenssidataa tavoilla, jotka ovat verkkopohjaisilla järjestelmillä tyypillisesti hankalia tai mahdottomia.

[TOC]

## Lisenssi { #license }

BioPerliä saa käyttää vapaasti, ja se on avoimen lähdekoodin.

BioPerl on lisensoitu samoilla ehdoilla kuin itse Perl, joka on kaksoislisensoitu [Perl Artistic license](https://dev.perl.org/licenses/artistic.html) -lisenssillä tai [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html) -lisenssillä.

## Saatavilla { #available }

- Puhti: Perl 5.36.0 ja BioPerl 1.7.8

## Käyttö { #usage }

Puhti-ympäristössä BioPerlin saa käyttöön komennolla:

```bash
module load biokit
```

Tämän jälkeen voit käynnistää BioPerl-ohjelman komennolla:

```bash
perl my_bioperl_code.pm
```

Vaihtoehtoisesti voit muuttaa Perlin määrityksen koodisi ensimmäisellä rivillä muotoon

```bash
#!/bin/env perl
```

ja suorittaa Perl-ohjelman:

```bash
./my_bioperl_code.pm
```
 
## Tuki { #support }

[CSC Service Desk](../support/contact.md)

## Lisätietoja { #more-information }

* [BioPerlin kotisivu](https://bioperl.org/)
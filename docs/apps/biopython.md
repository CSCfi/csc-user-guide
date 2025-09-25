---
tags:
  - Free
catalog:
  name: Biopython
  description: Python environment with biopython and other bioinformatics related Python libraries
  description_fi: Python-ympäristö, jossa on Biopython ja muita bioinformatiikkaan liittyviä Python-kirjastoja
  license_type: Free
  disciplines:
    - Biosciences
  available_on:
    - Puhti
---

# Biopython { #biopython }

Biopython on kokoelma Python-moduuleja, jotka helpottavat Python-skriptien kehittämistä bioinformatiikan sovelluksiin. Tämän vuoksi se ei sisällä valmiita, heti käytettäviä ohjelmia samaan tapaan kuin monet kaupalliset paketit ja maksuttomat verkkopohjaiset käyttöliittymät. Toisaalta Biopython tarjoaa uudelleenkäytettäviä Python-moduuleja, jotka helpottavat skriptien kirjoittamista sekvenssien käsittelyyn, tietokantoihin pääsyyn useissa eri tiedostomuodoissa sekä erilaisten molekyylibiologian ohjelmien tulosten ajamiseen ja jäsentämiseen. Näin Biopython mahdollistaa skriptien kehittämisen, joilla voidaan analysoida suuria määriä sekvenssidataa tavoilla, jotka ovat tyypillisesti hankalia tai mahdottomia verkkopohjaisilla järjestelmillä.
 
[TOC]

## License { #license }

Biopython on vapaasti käytettävä ja avoimen lähdekoodin ohjelmisto. Sitä jaellaan kaksoislisenssillä: [Biopython License](https://raw.githubusercontent.com/biopython/biopython/master/LICENSE.rst) tai [BSD 3-Clause License](https://docs.conda.io/en/latest/license.html).

## Available { #available }

- Puhti: Python 3.10.6 ja Biopython 1.79
- Puhti: Python 3.12.3 ja Biopython 1.83

Puhtissa on saatavilla Biopython-kirjastot sekä monia muita bioinformatiikkaan liittyviä Python-kirjastoja.

```bash
module load biopythontools
```

Kun moduuli on ladattu, voit käynnistää Biopython-ohjelman komennolla:

```bash
python my_biopython_code.py
```

Vaihtoehtoisesti voit muuttaa koodisi ensimmäisen rivin Python-määrittelyn muotoon

```bash
#!/bin/env python
```

ja suorittaa Python-ohjelman

```bash
./my_biopython_code.pm
```

Uusia Python-kirjastoja voi asentaa komennolla `pip install`.
Esimerkiksi OBITools3-nimisen Python-kirjaston voi asentaa komennolla:

```bash
pip install --user OBITools3
```

Lisäohjeita asennuspaikan määrittämiseen jne. löytyy
[CSC:n Python-käyttöoppaasta](../support/tutorials/python-usage-guide.md).

## More information { #more-information }

Lisätietoja Biopythonista löytyy Biopythonin kotisivulta.

* [www.biopython.org](https://biopython.org/)
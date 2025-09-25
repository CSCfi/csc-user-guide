---
tags:
  - Free
catalog:
  name: PDAL
  description: for point cloud translations and processing
  description_fi: pistepilvien muunnoksiin ja käsittelyyn
  license_type: Free
  disciplines:
    - Geosciences
  available_on:
    - LUMI
    - Puhti
    - Mahti
---

# PDAL { #pdal }

[PDAL](https://www.pdal.io/) on avoimen lähdekoodin komentorivisovellus pistepilvien muunnoksiin ja käsittelyyn.

## Saatavilla { #available }

PDAL on saatavilla seuraavina versioina:

* 2.8.0 - [geoconda-3.11.10-moduuli](geoconda.md) pdal Python -kirjastolla, Puhtissa
* 2.7.2 - [QGIS-3.38-moduuli](qgis.md) ilman pdal Python -kirjastoa, mutta mukana [pdal_wrench](https://github.com/PDAL/wrench), Puhtissa
* 2.7.2 - [geoconda-3.11.9-moduuli](geoconda.md) pdal Python -kirjastolla, Puhtissa ja Mahtissa
* 2.6.2 - [QGIS-3.34-moduuli](qgis.md) ilman pdal Python -kirjastoa, mutta mukana [pdal_wrench](https://github.com/PDAL/wrench), Puhtissa
* 2.5.2 - [geoconda-3.10.9-moduuli](geoconda.md) pdal Python -kirjastolla, Puhtissa
* 2.4.1 - [geoconda-3.10.6-moduuli](geoconda.md) pdal Python -kirjastolla, Puhtissa ja Mahtissa
* 2.3.0 - [QGIS-3.31-moduuli](qgis.md) ilman pdal Python -kirjastoa, Puhtissa ja LUMIssa

## Käyttö { #usage }

### PDALin käyttö { #using-pdal }

PDALia käytettäessä jokin yllä luetelluista moduuleista on ensin aktivoitava; katso lisätiedot linkitetyiltä sivuilta.

Voit testata, latautuiko pdal onnistuneesti, seuraavalla komennolla

`pdal --help`

[Esimerkkejä PDALin käytöstä Puhtissa](https://github.com/csc-training/geocomputing/tree/master/pdal).

## Lisenssi { #license }

PDAL on lisensoitu BSD-avoimen lähdekoodin lisenssillä. [Täydellinen PDAL-lisenssi](https://pdal.io/en/latest/copyright.html)

## Viittaus { #citation }

```  PDAL contributors (2022). PDAL: The Point Data Abstraction Library, DOI: 10.5281/zenodo.2616780  ```

## Kiitokset { #acknowledgement }

Mainitsethan CSC:n ja Geoportin julkaisuissasi; tämä on tärkeää hankkeen jatkuvuuden ja rahoitusraporttien kannalta.
Esimerkiksi: "Kirjoittajat haluavat kiittää CSC:tä – Tieteen tietotekniikkakeskus, Suomi (urn:nbn:fi:research-infras-2016072531) ja tutkimuksen avointa paikkatietoinfrastruktuuria (Geoportti, urn:nbn:fi:research-infras-2016072513) laskentaresursseista ja tuesta."

## Asennus { #installation }

Katso kunkin version moduulisivu: [Geoconda](./geoconda.md) , [QGIS](./qgis.md).

## Lähteet { #references }

* [PDALin kotisivu](https://pdal.io/)
* [LAS-tiedoston esimerkki](https://pdal.io/en/latest/tutorial/las.html)
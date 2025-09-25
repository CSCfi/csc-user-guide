---
tags:
  - Free
catalog:
  name: QGIS
  description: General purpose GIS software family for viewing, editing and analysing geospatial data
  description_fi: Yleiskäyttöinen GIS-ohjelmistoperhe paikkatietoaineistojen tarkasteluun, muokkaamiseen ja analysointiin
  license_type: Free
  disciplines:
    - Geosciences
  available_on:
    - web_interfaces:
        - LUMI
        - Puhti
    - LUMI
    - Puhti
---

# QGIS { #qgis }

[QGIS](https://qgis.org/en/site/) on ilmainen ja avoimen lähdekoodin GIS-sovellus, jota voidaan käyttää paikkatietoaineistojen katseluun, muokkaukseen ja analysointiin. QGIS tukee erittäin laajaa valikoimaa vektori- ja rasterimuotoja sekä yleisiä rajapintaprotokollia kuten WMS, WMTS, WCS ja WFS. 

Supertietokoneissa QGIS:ia voidaan käyttää esimerkiksi visualisoimaan muiden työkalujen (lastools, R, Python jne.) tuottamia tulostiedostoja.


## Saatavilla { #available }

__QGIS__ on saatavilla seuraavina versioina:

* 3.38 Puhtissa, sisältää myös [GDAL](gdal.md) ja [PDAL](pdal.md). Konttiin on asennettu myös PCRaster-kirjasto, mutta [PCRaster QGIS -lisäosa](https://jvdkwast.github.io/qgis-processing-pcraster/) tulee jokaisen käyttäjän lisätä itse.
* 3.34 Puhtissa, sisältää myös [GDAL](gdal.md), [PDAL](pdal.md) ja QGISin uudet sisäiset pistepilvityökalut.
* 3.31 Puhtissa ja LUMIssa, sisältää myös [GDAL](gdal.md), [GrassGIS](grass.md), [PDAL](pdal.md) ja [SagaGIS](saga-gis.md). 
* 3.22 Puhtissa

## Käyttö { #usage }

### QGIS Puhtissa { #qgis-in-puhti }

QGIS:n käyttöä varten avaa se Puhti-verkkokäyttöliittymässä:

1. Kirjaudu sisään [Puhti-verkkokäyttöliittymään](https://puhti.csc.fi). 
2. Avaa [Desktop-sovellus](../computing/webinterface/desktop.md). 
3. Kun Desktop on käynnistynyt, kaksoisnapsauta QGIS-kuvaketta käynnistääksesi uusimman version.

Jos haluat käyttää vanhempaa versiota, avaa `Terminal` (Desktop-kuvake) ja käynnistä QGIS:

```
module load qgis/3.22
qgis
```

### QGIS LUMIssa { #qgis-in-lumi }

QGIS:n käyttöä varten avaa se LUMI-verkkokäyttöliittymässä:

1. Kirjaudu sisään [LUMI-verkkokäyttöliittymään](https://lumi.csc.fi). 
2. Avaa [Desktop-sovellus](https://docs.lumi-supercomputer.eu/runjobs/webui/desktop/). 
3. Kun Desktop on käynnistynyt, avaa uusin QGIS-versio vasemman alakulman valikosta (kohdasta Other).
    * Voit vetää ja pudottaa kuvakkeen työpöydällesi helpompaa käyttöä varten jatkossa

Jos haluat käyttää komentoriviä (CLI), avaa `Terminal Emulator` vasemman alakulman valikosta ja käynnistä QGIS:

```
module use /appl/local/csc/modulefiles
module load qgis
qgis
```

### SagaGIS-työkalupakki QGISissa { #sagagis-toolbox-in-qgis }

SagaGIS-työkalut eivät ole oletuksena saatavilla QGIS 3.31:ssä Processing Toolboxissa, mutta ne voidaan lisätä asentamalla `Saga Next Gen` -lisäosa. Tämä on uusi lisäosa, eikä kaikki työkalut välttämättä vielä toimi.  

### PyQGIS { #pyqgis }

QGIS:n toimintoihin on mahdollista päästä käsiksi myös Pythonista ilman graafista käyttöliittymää [PyQGIS-kirjaston](https://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook/) avulla. Käytä `python3`-komentoa PyQGIS-kirjastojen käyttämiseen.


### Puhti QGIS ja Allas { #puhti-qgis-and-allas }

QGIS voi lukea tiedostoja suoraan Allasista joko S3- tai SWIFT-rajapinnan kautta. Ennen QGIS:n käynnistämistä määritä yhteys ohjeen [Using geospatial files directly from cloud, inc Allas tutorial](../support/tutorials/gis/gdal_cloud.md) mukaisesti ja käynnistä sitten QGIS Terminaalista.

Suurten Allas-aineistomäärien kanssa harkitse [virtuaalirastereiden](https://research.csc.fi/virtual_rasters) käyttöä. 

## Lisenssi { #license }

QGIS on lisensoitu GNU General Public License -lisenssin alaisena.

## Viittaus { #citation }

```QGIS.org, 2024. QGIS Geographic Information System. QGIS Association. http://www.qgis.org```



## Kiitokset { #acknowledgement }

Mainitsethan CSC:n ja Geoportin julkaisuissasi; se on tärkeää projektin jatkuvuuden ja rahoitusraportoinnin kannalta.
Esimerkiksi: "Tekijät kiittävät CSC:tä – Tieteen tietotekniikan keskus, Suomi (urn:nbn:fi:research-infras-2016072531) ja Avoin paikkatietoinfrastruktuuri tutkimukselle (Geoportti, urn:nbn:fi:research-infras-2016072513) laskentaresursseista ja tuesta."


## Asennus { #installation }
* 3.38 asennettiin [Tykky-työkalun conda-containerize-toiminnolla](../computing/containers/tykky.md#conda-based-installation). .yml-tiedosto sisälsi vain `qgis`- ja `pcraster`-paketit `conda-forge`-repositorysta.
* 3.34 asennettiin [Tykky-työkalun conda-containerize-toiminnolla](../computing/containers/tykky.md#conda-based-installation). .yml-tiedosto sisälsi vain `qgis`-paketin `conda-forge`-repositorysta.
* 3.31 asennettiin [Tykky-työkalun wrap-container-toiminnolla](../computing/containers/tykky.md#container-based-installations) käyttäen [QGIS Docker -imagetä Dockerhubista, QGIS-yhteisön tarjoamana](https://hub.docker.com/r/qgis/qgis). LUMIssa `Tykky` on nimeltään `Container wrapper`.

`wrap-container -w /usr/bin docker://qgis/qgis:latest --prefix install_dir`


## Viitteet { #references }

* [QGIS-kotisivu](https://www.qgis.org/)
* [QGIS-oppaat](https://www.qgistutorials.com/en/)
* [Maksutonta QGIS-koulutusmateriaalia](https://qgis.org/en/site/forusers/trainingmaterial/index.html)
* [PyQGIS-keittokirja](https://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook/)
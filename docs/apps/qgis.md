
---
tags:
  - Free
system:
  - www-puhti
  - www-lumi
---

# QGIS

[QGIS](https://qgis.org/en/site/) on ilmainen ja avoimen lähdekoodin GIS-sovellus, jota voidaan käyttää paikkatietojen katseluun, muokkaamiseen ja analysointiin. QGIS tukee hyvin laajaa valikoimaa vektori- ja rasteriformaatteja sekä yleisiä API-protokollia, kuten WMS, WMTS, WCS ja WFS.

Supertietokoneissa QGIS:tä voidaan käyttää esimerkiksi muiden työkalujen avulla prosessoitujen tiedostojen visualisointiin: lastools, R, Python jne.

## Saatavilla {#available}

__QGIS__ on saatavilla seuraavilla versioilla:

* 3.38 Puhtissa, sisältää myös [GDAL](gdal.md) ja [PDAL](pdal.md). Myös PCRaster-kirjasto on asennettu säilöön, mutta [PCRaster QGIS -laajennus](https://jvdkwast.github.io/qgis-processing-pcraster/) tulee lisätä jokaisen käyttäjän toimesta.
* 3.34 Puhtissa, sisältää myös [GDAL](gdal.md), [PDAL](pdal.md) ja uudet natiivipistepilvityökalut QGIS:ssä.
* 3.31 Puhtissa ja LUMI:ssa, sisältää myös [GDAL](gdal.md), [GrassGIS](grass.md), [PDAL](pdal.md) ja [SagaGIS](saga-gis.md).
* 3.22 Puhtissa

## Käyttö {#usage}

### QGIS Puhtissa {#qgis-in-puhti}

QGIS:n käyttöön, avaa se Puhtin web-käyttöliittymässä:

1. Kirjaudu sisään [Puhtin web-käyttöliittymään](https://puhti.csc.fi). 
2. Avaa [Desktop-sovellus](../computing/webinterface/desktop.md). 
3. Käynnistä Desktopin jälkeen kaksoisnapsauttamalla QGIS-kuvaketta uusimmasta versiosta.

Jos haluat käyttää vanhempaa versiota, avaa `Terminal` (Desktop-kuvake) ja käynnistä QGIS:

```
module load qgis/3.22
qgis
```

### QGIS LUMI:ssa {#qgis-in-lumi}

QGIS:n käyttöön, avaa se LUMIn web-käyttöliittymässä:

1. Kirjaudu sisään [LUMIn web-käyttöliittymään](https://lumi.csc.fi). 
2. Avaa [Desktop-sovellus](https://docs.lumi-supercomputer.eu/runjobs/webui/desktop/). 
3. Käynnistä Desktopin jälkeen, avaa QGIS:n uusin versio alakulman valikosta (Other-osiossa).
   * Voit vetää ja pudottaa kuvakkeen työpöydällesi helpompaa pääsyä varten tulevaisuudessa

Jos haluat käyttää CLI:tä, avaa `Terminal Emulator` alakulman valikosta ja käynnistä QGIS:

```
module use /appl/local/csc/modulefiles
module load qgis
qgis
```

### SagaGIS työkalupakki QGIS:ssä {#sagagis-toolbox-in-qgis}

SagaGIS-työkalut eivät ole oletuksena saatavilla QGIS 3.31:ssa Processing Toolboxissa, mutta ne voidaan lisätä asentamalla `Saga Next Gen` -laajennus. Tämä on uusi laajennus, eikä kaikki työkalut välttämättä vielä toimi.

### PyQGIS {#pyqgis}

QGIS:n toimintoihin on myös mahdollista päästä käsiksi Pythonista ilman graafista käyttöliittymää [PyQGIS-kirjaston](https://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook/) avulla. Käytä `python3` PyQGIS-kirjastojen käyttöön.

### Puhti QGIS ja Allas {#puhti-qgis-and-allas}

QGIS voi __lukea__ tiedostoja suoraan Allas-palvelusta joko S3- tai SWIFT-APIn avulla. Ennen QGIS:n käynnistämistä luo yhteys kuten kuvattu [geospatiaaliset tiedostot suoraan pilvestä, mukaan lukien Allas -oppaassa](../support/tutorials/gis/gdal_cloud.md) ja käynnistä sitten QGIS Terminalista.

Suurten datamäärien käsittelyssä Allas-palvelussa harkitse [virtuaalirastereiden](https://research.csc.fi/virtual_rasters) käyttöä.

## Lisenssi {#license}

QGIS on lisensoitu GNU General Public Licensen alaisuudessa.

## Viittaus {#citation}

```QGIS.org, 2024. QGIS-kanepaikkatietojärjestelmä. QGIS Association. http://www.qgis.org```

## Kunnianosoitus {#acknowledgement}

Ole hyvä ja mainitse CSC ja Geoportti julkaisussasi, se on tärkeää projektien jatkolle ja rahoituksen raportoinnille.
Esimerkiksi voit kirjoittaa "Kirjoittajat haluavat kiittää CSC:tä - Tieteen tietotekniikan keskus, Suomi (urn:nbn:fi:research-infras-2016072531) ja Open Geospatial Information Infrastructure for Research (Geoportti, urn:nbn:fi:research-infras-2016072513) laskentaresursseista ja tuesta".

## Asennus {#installation}
* 3.38 asennettiin [Tykky'n conda-containerize funktionaalisuudella](../computing/containers/tykky.md#conda-based-installation). .yml-tiedosto sisälsi vain `qgis` ja `pcraster` paketit `conda-forge`-varastosta.
* 3.34 asennettiin [Tykky'n conda-containerize funktionaalisuudella](../computing/containers/tykky.md#conda-based-installation). .yml-tiedosto sisälsi vain `qgis` paketin `conda-forge`-varastosta.
* 3.31 asennettiin [Tykky'n wrap-container funktionaalisuudella](../computing/containers/tykky.md#container-based-installations) käyttäen [QGIS Docker -ilmettä Dockerhubista, jonka tarjoaa QGIS-yhteisö](https://hub.docker.com/r/qgis/qgis). LUMI:ssa `Tykky` on nimeltään `Container wrapper`.

`wrap-container -w /usr/bin docker://qgis/qgis:latest --prefix install_dir`

## Viitteet {#references}

* [QGIS kotisivu](https://www.qgis.org/)
* [QGIS opastuksia](https://www.qgistutorials.com/en/)
* [Ilmainen QGIS koulutusmateriaali](https://qgis.org/en/site/forusers/trainingmaterial/index.html)
* [PyQGIS ohjekirja](https://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook/)



---
tags:
  - Free
system:
  - www-puhti
  - www-lumi
---

# GRASS GIS

[GRASS](https://grass.osgeo.org/) (Geographic Resources Analysis Support System) on ilmainen paikkatietojärjestelmän (GIS) ohjelmisto, jota käytetään geospatiaaliseen tietojen hallintaan ja analysointiin, kuvankäsittelyyn, grafiikan/karttojen tuottamiseen, spatiaaliseen mallintamiseen ja visualisointiin.

## Saatavilla {#available}

__GRASS__ on saatavilla seuraavilla versioilla:

* 8.3 grassgis-moduulilla Puhtissa
* 7.8.7 [qgis/3.31 moduulilla](qgis.md) Puhtissa ja LUMIssa
* 7.8.5 [qgis/3.22 moduulilla](qgis.md) Puhtissa

## Käyttö {#usage}

### GRASS GIS komentorajapinta {#grass-gis-command-line-interface}

GRASS GIS komentorivityökaluja voidaan käyttää [interaktiivisessa istunnossa](../computing/running/interactive-usage.md) tai [erätehtävissä](../computing/running/getting-started.md). Katso [esimerkkejä GRASS GIS komentojen käytöstä Puhtissa, GRASS bash skriptauksella, Python skriptauksella tai PyGRASSilla](https://github.com/csc-training/geocomputing/tree/master/grass). Katso myös viittaukset tämän sivun lopusta.

### GRASS GIS graafinen käyttöliittymä {#grass-gis-graphical-user-interface}

#### GRASS Puhtissa {#grass-in-puhti}

Helpoin tapa käyttää GRASS GIS:ää on avata se Puhti-verkkokäyttöliittymässä.

1. Kirjaudu sisään [Puhti-verkkokäyttöliittymään](https://puhti.csc.fi).
2. Avaa [Työpöytäsovellus](../computing/webinterface/desktop.md).
3. Työpöydän käynnistämisen jälkeen kaksoisnapsauta GRASS-GIS-kuvaketta uusimmalle versiolle.

Jos haluat käyttää vanhempaa versiota, avaa `Terminal` (Työpöytäsovelluksen kuvake) ja käynnistä GRASS GIS:

```
module load qgis/3.22
grass
```

#### GRASS LUMIssa {#grass-in-lumi}

GRASS GIS:n käyttöön avaa se LUMI-verkkokäyttöliittymässä:

1. Kirjaudu sisään [LUMI-verkkokäyttöliittymään](https://lumi.csc.fi).
2. Avaa [Työpöytäsovellus](https://docs.lumi-supercomputer.eu/runjobs/webui/desktop/).
3. Työpöydän käynnistämisen jälkeen avaa uusin GRASS GIS -versio valikosta vasemmasta alakulmasta (kohdassa Muu).
   * Voit raahata ja pudottaa kuvakkeen työpöydällesi helpottamaan tulevaa käyttöä

Jos haluat käyttää CLI:tä, avaa `Terminal Emulator` valikosta vasemmassa alakulmassa ja käynnistä GRASS GIS:

```
module use /appl/local/csc/modulefiles
module load qgis
grass
```

## Lisenssi {#license}

Geographic Resources Analysis Support System (GRASS) on Copyright, 1999-2020 GRASS Development Team, ja se on lisensoitu GNU General Public License (GPL) -ehdoin. Tämä koskee kaikkea ohjelmistoa, dokumentaatiota ja siihen liittyviä materiaaleja. [GRASS GIS:n täydellinen lisenssi](https://grass.osgeo.org/about/license/)

## Viittaus {#citation}

Tätä ohjelmistoa voidaan siteerata valitsemalla sopiva viittaus [GRASS-viitevarastosta](https://grasswiki.osgeo.org/wiki/GRASS_Citation_Repository).

## Tunnustus {#acknowledgement}

Pyydämme tunnustusta CSC:lle ja Geoportille julkaisuissanne, sillä se on tärkeää projektin jatkuvuudelle ja rahoitusraporteille. Esimerkiksi voit kirjoittaa: "Tekijät haluavat kiittää CSC - IT Center for Science, Finlandia (urn:nbn:fi:research-infras-2016072531) ja Open Geospatial Information Infrastructure for Research (Geoportti, urn:nbn:fi:research-infras-2016072513) laskentaresursseista ja tuesta".

## Asennus {#installation}

* GRASS 8.3 asennettiin Puhtiin [Tykky-wrap-container-toiminnallisuudella](../computing/containers/tykky.md#container-based-installations) käyttäen [GRASS Docker -kuvaa Dockerhubista OSGEO:n tarjoamana](https://hub.docker.com/r/osgeo/grass-gis): `wrap-container -w /usr/local/bin,/usr/bin/python3 docker://osgeo/grass-gis:releasebranch_8_3-ubuntu_wxgui --prefix 8.3`
* GRASS 7.x asennettiin Puhtiin ja LUMIin osana [QGIS-asennusta](qgis.md#installation).

## Viitteet {#references}

* [GRASS GIS kotisivu](https://grass.osgeo.org/)
* [GRASS GIS manuaalit](https://grass.osgeo.org/learn/manuals/)
  * [Rinnakkaiset GRASS-tehtävät](https://grasswiki.osgeo.org/wiki/Parallel_GRASS_jobs)
* [GRASS GIS -oppaat](https://grass.osgeo.org/learn/tutorials/)
* [GRASS-tietokanta, sijainti, karttasarja ja alue](https://grass.osgeo.org/grass79/manuals/grass_database.html), peruskonseptit, jotka ovat aina tarpeen GRASS GIS:n kanssa. Jos käytetään rinnakkaislaskentaa, ole erityisen tarkka `regionin` kanssa.
* [Anna Petrasova, GRASS GIS -workshop FOSS4G:ssä, osa 5: parallelisointi](https://github.com/ncsu-geoforall-lab/grass-gis-workshop-foss4g-2022/blob/main/workshop_part_5_parallelization.ipynb)

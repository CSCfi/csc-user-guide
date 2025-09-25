---
tags:
  - Free
catalog:
  name: GRASS GIS
  description: General purpose GIS software family for viewing, editing and analysing geospatial data
  description_fi: Yleistarkoitukseen soveltuva GIS‑ohjelmistoperhe paikkatietojen tarkasteluun, muokkaukseen ja analysointiin
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

# GRASS GIS { #grass-gis }

[GRASS](https://grass.osgeo.org/) (Geographic Resources Analysis Support System) on ilmainen paikkatietojärjestelmä (GIS), jota käytetään paikkatietoaineistojen hallintaan ja analysointiin, kuvankäsittelyyn, grafiikan ja karttojen tuotantoon, spatiaaliseen mallinnukseen ja visualisointiin.

## Saatavilla { #available }

__GRASS__ on saatavilla seuraavina versioina:

* 8.3 grassgis-moduulilla Puhtissa
* 7.8.7 [qgis/3.31 -moduulilla](qgis.md) Puhtissa ja LUMIssa
* 7.8.5 [qgis/3.22 -moduulilla](qgis.md) Puhtissa


## Käyttö { #usage }

### GRASS GIS:n komentorivikäyttöliittymä { #grass-gis-command-line-interface }

GRASS GIS:n komentorivityökaluja voi käyttää [interaktiivisessa istunnossa](../computing/running/interactive-usage.md) tai [eräajoina](../computing/running/getting-started.md). Katso [esimerkkejä GRASS GIS -komentojen käytöstä Puhtissa GRASS bash -skriptauksella, Python-skriptauksella tai PyGRASSilla](https://github.com/csc-training/geocomputing/tree/master/grass). Katso myös viitteet tämän sivun lopusta.

### GRASS GIS:n graafinen käyttöliittymä { #grass-gis-graphical-user-interface }

#### GRASS Puhtissa { #grass-in-puhti }

Helpoin tapa käyttää GRASS GIS:iä on avata se Puhtin selainkäyttöliittymässä.

1. Kirjaudu sisään [Puhti-selainkäyttöliittymään](https://puhti.csc.fi).
2. Avaa [Työpöytäsovellus](../computing/webinterface/desktop.md).
3. Kun työpöytä on käynnistynyt, kaksoisnapsauta GRASS-GIS-kuvaketta uusimman version käynnistämiseksi.
 
Jos haluat käyttää vanhempaa versiota, avaa `Terminal` (työpöydän kuvake) ja käynnistä GRASS GIS:

```
module load qgis/3.22
grass
```

#### GRASS LUMIssa { #grass-in-lumi }

GRASS GIS:n käyttö LUMIn selainkäyttöliittymän kautta:

1. Kirjaudu sisään [LUMI-selainkäyttöliittymään](https://lumi.csc.fi).
2. Avaa [Työpöytäsovellus](https://docs.lumi-supercomputer.eu/runjobs/webui/desktop/).
3. Kun työpöytä on käynnistynyt, avaa uusin GRASS GIS -versio valikosta vasemmasta alakulmasta (kohdasta Other).
    * Voit vetää ja pudottaa kuvakkeen työpöydälle helpompaa käyttöä varten jatkossa

Jos haluat käyttää komentorajapintaa (CLI), avaa `Terminal Emulator` vasemman alakulman valikosta ja käynnistä GRASS GIS:

```
module use /appl/local/csc/modulefiles
module load qgis
grass
```

## Lisenssi { #license }

Geographic Resources Analysis Support System (GRASS) on tekijänoikeuksin suojattu, 1999–2020 GRASS Development Team, ja lisensoitu GNU General Public License (GPL) -lisenssin ehtojen mukaisesti. Tämä kattaa kaiken ohjelmiston, dokumentaation ja siihen liittyvät materiaalit. [GRASS GIS -lisenssi kokonaisuudessaan](https://grass.osgeo.org/about/license/)


## Viittaus { #citation }

Tähän ohjelmistoon voi viitata valitsemalla sopivan viittauksen [GRASS-viittauskokoelmasta](https://grasswiki.osgeo.org/wiki/GRASS_Citation_Repository). 


## Kiitokset { #acknowledgement }

Pyydämme mainitsemaan CSC:n ja Geoportin julkaisuissasi; tämä on tärkeää projektien jatkuvuuden ja rahoitusraportoinnin kannalta.
Esimerkiksi voit kirjoittaa: "Tekijät kiittävät CSC:tä – Tieteen tietotekniikan keskus, Suomi (urn:nbn:fi:research-infras-2016072531) ja Open Geospatial Information Infrastructure for Researchia (Geoportti, urn:nbn:fi:research-infras-2016072513) laskentaresursseista ja tuesta."


## Asennus { #installation }

* GRASS 8.3 asennettiin Puhtiin [Tykky-työkalun wrap-container-toiminnolla](../computing/containers/tykky.md#container-based-installations) käyttäen [OSGEOn tarjoamaa GRASS Docker -imagea Dockerhubista](https://hub.docker.com/r/osgeo/grass-gis): `wrap-container -w /usr/local/bin,/usr/bin/python3 docker://osgeo/grass-gis:releasebranch_8_3-ubuntu_wxgui --prefix 8.3`
* GRASS 7.x asennettiin Puhtiin ja LUMIin osana [QGIS-asennusta](qgis.md#installation).


## Viitteet { #references }

* [GRASS GIS -kotisivu](https://grass.osgeo.org/)
* [GRASS GIS -manuaalit](https://grass.osgeo.org/learn/manuals/)
  * [Rinnakkaiset GRASS-työt](https://grasswiki.osgeo.org/wiki/Parallel_GRASS_jobs)
* [GRASS GIS -oppaat](https://grass.osgeo.org/learn/tutorials/)
* [GRASS-tietokanta, sijainti, mapset ja alue (region)](https://grass.osgeo.org/grass79/manuals/grass_database.html), peruskäsitteet, joita tarvitaan aina GRASS GIS:n kanssa.
Jos käytät rinnakkaislaskentaa, ole erityisen varovainen `region`-asetuksen kanssa.
* [Anna Petrasova, GRASS GIS workshop at FOSS4G, part 5: parallelization](https://github.com/ncsu-geoforall-lab/grass-gis-workshop-foss4g-2022/blob/main/workshop_part_5_parallelization.ipynb)
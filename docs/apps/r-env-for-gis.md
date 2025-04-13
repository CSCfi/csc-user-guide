
---
tags:
  - Free
---

# R GIS:lle {#r-for-gis}

Tämä sivu on Puthin R-ympäristössä asennetuille avaruudellisille R-kirjastoille ja -työkaluille. R:n dokumentaatio löytyy yleisesti [`r-env`-sivulta](r-env.md). Avaruudelliset kirjastot sisältyvät kaikkiin R-versioihin Puthissa.

## Käyttö {#usage}

### Moduulin lataaminen {#loading-the-module}

Lataa yleinen R-moduuli komennolla

```
module load r-env
```

### Asennetut avaruudelliset R-kirjastot {#installed-spatial-r-libraries}

* [aws.s3](https://cran.r-project.org/web/packages/aws.s3/) - työskentelyyn S3-tallennuksen kanssa, esimerkiksi Allas. [Esimerkki](https://github.com/csc-training/geocomputing/blob/master/R/allas/working_with_allas_from_R_S3.R).
* [CAST](https://cran.r-project.org/web/packages/CAST/index.html) - toiminnallisuus `caret`:lle avaruudellisten tai avaruus-aikallisten datojen kanssa
* [fasterize](https://cran.r-project.org/web/packages/fasterize/index.html) - nopeampi korvike `raster`-paketin rasterize()-funktiolle
* [FORTLS](https://cran.r-project.org/web/packages/FORTLS/index.html) - maalla suoritetun laserkeilauksen (TLS) pistemassojen käsittely metsätalouden tarkoituksiin
* [gdalcubes](https://cran.r-project.org/web/packages/gdalcubes/index.html) - työskentelyyn moniaikaisten rasteridatakuutioiden kanssa
* [geodata](https://cran.r-project.org/web/packages/geodata/index.html) - pääsy ilmasto-, viljely-, korkeus-, maan käyttö-, maaperä-, lajilöydös-, saavutettavuus-, hallinnollisiin rajatietoihin ja muihin datoihin.
* [geofi](https://ropengov.github.io/geofi/) - paikkatiedon lataaminen kunnista, postinumeroista ja väestö- ja tilastoruudukosta Tilastokeskuksesta
* [geoR](https://cran.r-project.org/web/packages/geoR/index.html) - geostatistinen analyysi sisältäen perinteisiä, todennäköisyyspohjaisia ja bayeslaisia menetelmiä
* [geosphere](https://cran.r-project.org/web/packages/geosphere/index.html) - sfäärinen trigonometria maantieteellisille koordinaateille (lat, lon)
* [ggmap](https://cran.r-project.org/web/packages/ggmap/index.html) - karttavisualisoinnit `ggplot2`:n kanssa. Taustakarttana voidaan käyttää useita nettilähteitä (esim. Google Maps ja Stamen Maps). Sisältää myös työkaluja geokoodaukseen ja reititykseen
* [ggspatial](https://cran.r-project.org/web/packages/ggspatial/index.html) - karttojen piirtämiseen
* [gstat](https://cran.r-project.org/web/packages/gstat/index.html) - spatiaalinen ja spatio-aikallinen geostatistinen mallintaminen, ennustaminen ja simulointi. Variogrammin mallintaminen; yksinkertainen, tavanomainen ja universaali piste- tai lohko(ko)kriging; spatio-aikallinen kriging; sekventiaalinen Gaussin tai indikaattorin (ko)simulointi; variogrammin ja variogrammikartan piirtotyökalut
* [GWmodel](https://cran.r-project.org/web/packages/GWmodel/index.html) - paikkatietopainotetut mallit: GW-yhteenvetotilastot, GW-pääkomponenttianalyysi, GW-kuvan erottelu ja erilaiset GW-regression muodot
* [igraph]
* [lidR](https://cran.r-project.org/web/packages/lidR/index.html) - LiDAR-datan käsittely ja visualisointi (metsätalouden sovelluksille), mittareiden laskenta aluepohjaisessa lähestymistavassa, pistesuodatukset, keinotekoinen pisteiden vähentäminen, luokittelu maantieteellisestä datasta, normalisointi, yksittäisten puiden segmentointi ja muita käsittelytoimenpiteitä. [Esimerkki](https://github.com/csc-training/geocomputing/tree/master/R/R_LiDAR/R_lidar_course_exercises)
* [lidRtRee](https://cran.r-project.org/web/packages/lidaRtRee/index.html) - metsän analysointi ilmalaserkeilauksen (LiDAR) datalla
* [mapedit](https://cran.r-project.org/web/packages/mapedit/index.html) - sf-objektien interaktiivinen muokkaus
* [maptools](https://cran.r-project.org/web/packages/maptools/index.html) - työkalut maantieteellisen datan käsittelyyn ja rajapinta useiden muiden R-pakettien kanssa
* [mapview](https://cran.r-project.org/web/packages/mapview/index.html) - interaktiivisen visualisoinnin luonti spatiaalidatalle nopeasti ja helposti, taustakartalla tai ilman. Näytettyjen piirteiden attribuutit ovat täysin kyseltävissä ponnahdusikkunoiden kautta
* [ncdf4](https://cran.r-project.org/web/packages/ncdf4/index.html) - lue, kirjoita ja muuta NetCDF-tiedostoja
* [ows4R](https://cran.r-project.org/web/packages/ows4R/index.html) - datalukeminen OGC-rajapinnoista
* [raster](https://cran.r-project.org/web/packages/raster/index.html) - rasteridataa varten keskeinen paketti
* [RCSF](https://cran.r-project.org/web/packages/RCSF/index.html) - Cloth Simulation Filter (CSF) on LiDAR-maapisteiden suodatuksen algoritmi
* [rlas](https://cran.r-project.org/web/packages/rlas/index.html) - lue ja kirjoita 'las' ja 'laz'-tiedostomuotoja
* [rstac](https://cran.r-project.org/web/packages/rstac/index.html) - asiakaskirjasto Spatio-Temporal Asset Catalog (STAC) varten
* [rTLS](https://cran.r-project.org/web/packages/rTLS/index.html) - käsittele maalla suoritettua laserkeilaus (TLS) datapisteitä
* [Rsagacmd](https://cran.r-project.org/web/packages/Rsagacmd/index.html) - SAGA GIS komentojen käyttäminen R:stä
* [sen2r](https://sen2r.ranghetti.info/) - Sentinel-2 datan löytäminen, lataaminen ja käsittely
* [sf](https://cran.r-project.org/web/packages/sf/index.html) - vektoridataa varten keskeinen paketti, sidokset GDAL-, GEOS- ja PROJ-kirjastoihin. Toimii tidyverse-pakettien kanssa. Samanlaisia toiminnallisuuksia kuin `sp`:llä, mutta uudempi ja parempi
* [sp](https://cran.r-project.org/web/packages/sp/index.html) - vanhempi keskeinen paketti vektoridatalle
* [spacetime](https://cran.r-project.org/web/packages/spacetime/index.html) - spatio-aikallisen datan kanssa työskentelyyn
* [spatial](https://cran.r-project.org/web/packages/spatial/index.html) - kriging ja pistekuvioanalyysiä varten
* [spatialreg](https://cran.r-project.org/web/packages/spatialreg/index.html) - spatiaalisten poikkileikkausmallien valmistamiseen
* [spatstat](https://cran.r-project.org/web/packages/spatstat/index.html) - pistekuvioiden analysointiin
* [spdep](https://cran.r-project.org/web/packages/spdep/index.html) - spatiaalinen riippuvuus: painot, tilastot ja mallit
* [stars](https://cran.r-project.org/web/packages/stars/index.html) - spatioaikaisten matriisien (rasteri- ja vektoridatakuutiot) lukemiseen, käsittelyyn, kirjoittamiseen ja piirtämiseen
* [s2](https://cran.r-project.org/web/packages/s2/index.html) - pallon geometristen laskutoimitusten suorittamiseen
* [terra](https://cran.r-project.org/web/packages/terra/index.html) - monipuolisia menetelmiä avaruudellisen datan analyysiin, erityisesti rasteridatalle
* [tmap](https://cran.r-project.org/web/packages/tmap/index.html) - temaattisten karttojen tekemiseksi

Voit myös asentaa omia lisäkirjastoja. Seuraa vain ohjeita [pää R-sivulla](r-env.md).

### GDAL- ja SAGA GIS:n tuki {#gdal-and-saga-gis-support}

`r-env`-moduuli sisältää myös [GDAL](gdal.md) ja [SAGA GIS](saga-gis.md).

### Rinnakkaislaskenta {#parallel-computing}

Jotkut R-paketit kuten __raster__, __terra__ ja __lidR__ sisältävät funktioita, jotka tukevat rinnakkaislaskentaa. Esimerkki raster-paketin predict-funktion käyttämisestä rinnakkaisesti löytyy [esimerkeistämme](https://github.com/csc-training/geocomputing/tree/master/R).

Monille muille GIS-paketeille sinun on rinnakkaistettava koodi itse. Tämä voidaan saavuttaa useilla kirjastoilla, mukaan lukien __future__. Katso [Rinnakkaistyöt käyttäen R-opasta](../support/tutorials/parallel-r.md) lisätiedoille.

## Allaksen käyttäminen R:llä {#using-allas-from-r}

Voit käyttää Allasta R:llä käyttäen __aws.s3__-pakettia. Löydät CSC:n esimerkkejä sen käytöstä [täältä](https://github.com/csc-training/geocomputing/blob/master/R/allas/working_with_allas_from_R_S3.R).

On myös mahdollista __lukea__ ja __kirjoittaa__ tiedostoja Allasista ja Allasiin tai muihin pilviobjektitallennuksiin suoraan GDAL-pohjaisia paketteja, kuten `sf` ja `terra`, käyttäen. Ole hyvä ja tutustu [Pilvifiluista alexsuoraan, sisältäen Allas-opas](../support/tutorials/gis/gdal_cloud.md) meidän ohjeisiin ja esimerkkeihin.

Suurten datamäärien kanssa Allasissa, harkitse [virtuaalirastereiden](../support/tutorials/gis/virtual-rasters.md) käyttöä.

## Lisenssi ja tunnustaminen {#license-and-acknowledgement}

Kaikki paketit ovat lisensoitu eri avoimen lähdekoodin lisenssein (FOSS), katso tarkat tiedot linkitetyiltä sivuilta yllä.
Oikeiden viittausten löytämiseksi R:lle ja eri R-paketeille, voit kirjoittaa:

```r
citation() # R:lle viittaamiseen
citation("package") # R-paketille viittaamiseen
```

Ole hyvä ja tunnusta CSC ja Geoportti julkaisuissasi, sillä se on tärkeää projektin jatkumisen ja rahoitusraporttien kannalta.
Esimerkkinä, voit kirjoittaa "Kirjoittajat haluavat kiittää CSC - Tiede- ja tietotekniikkakeskusta, Suomi (urn:nbn:fi:research-infras-2016072531) ja Avoimen maantiedon tutkimusinfrastruktuuria (Geoportti, urn:nbn:fi:research-infras-2016072513) laskentaresursseista ja tuesta".

## Viitteet {#references}

* [Esimerkkejä R-paikkatietopakettien käyttämisestä GIS:ssä Puthissa](https://github.com/csc-training/geocomputing/tree/master/R), CSC
* [Lista spatiaalista R-paketeista CRAN:ssa](https://cran.r-project.org/web/views/Spatial.html)
* [Avaruudellinen tieteenala](https://keen-swartz-3146c4.netlify.app/), Edzer Pebesma, Roger Bivand
* [Geokomputointi R:llä](https://geocompr.robinlovelace.net/), Robin Lovelace, Jakub Nowosad, Jannes Muenchow
* [Avaruudellinen tieteenala R:llä](https://rspatial.org/index.html), Robert J. Hijmans
* [Johdatus GIS:ään ja tilalliseen analyysiin](https://mgimond.github.io/Spatial/index.html), Manuel Gimond
* [Tilallisen mallintamisen tiedettä](https://gdsl-ul.github.io/san/), Francisco Rowe, Dani Arribas-Bel
* [Opas paikkatieto-R-työkaluista](https://datacarpentry.org/r-raster-vector-geospatial/)
* [CSC:n kurssi paikkatieto-R:stä](https://e-learn.csc.fi/course/view.php?id=120), Marko Kallio
* [Maantieteellinen data-analyysi R:llä: Ympäristömuutosten visualisointi ja analyysi](https://bookdown.org/mcwimberly/gdswr-book/), Michael C. Wimberly


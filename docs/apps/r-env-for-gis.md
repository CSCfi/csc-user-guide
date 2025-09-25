---
tags:
  - Free
catalog:
  name: R for GIS
  description: R spataial analysis libraries
  description_fi: R:n spatiaalisen analyysin kirjastot
  license_type: Free
  disciplines:
    - Geosciences
  available_on:
    - Puhti
---

# R paikkatietoon { #r-for-gis }

Tämä sivu koskee Puhtin R-ympäristöön asennettuja R:n paikkatietokirjastoja ja -työkaluja. Yleinen R-dokumentaatio löytyy [`r-env`-sivulta](r-env.md). Paikkatietokirjastot sisältyvät kaikkiin Puhtin R-versioihin.

## Käyttö { #usage }

### Moduulin lataaminen { #loading-the-module }

Lataa yleinen R-moduuli komennolla

```
module load r-env
```

### Asennetut R:n paikkatietokirjastot { #installed-spatial-r-libraries }

* [aws.s3](https://cran.r-project.org/web/packages/aws.s3/) - S3-tallennuksen käsittelyyn, esim. Allas. [Esimerkki](https://github.com/csc-training/geocomputing/blob/master/R/allas/working_with_allas_from_R_S3.R).
* [CAST](https://cran.r-project.org/web/packages/CAST/index.html) - toiminnot `caret`-paketin ajamiseen spatiaalisten tai spatio-temporaalisten aineistojen kanssa
* [fasterize](https://cran.r-project.org/web/packages/fasterize/index.html) - nopeampi korvaaja rasterize()-funktiolle `raster`-paketista 
* [FORTLS](https://cran.r-project.org/web/packages/FORTLS/index.html) - maakohdistetun laserskannauksen (TLS) pistepilviaineistojen käsittely metsäkäyttöön
* [gdalcubes](https://cran.r-project.org/web/packages/gdalcubes/index.html) - moniaikaisten rasteridatakuutioiden käsittelyyn
* [geodata](https://cran.r-project.org/web/packages/geodata/index.html) - pääsy ilmasto-, viljely-, korkeus-, maankäyttö-, maaperä-, lajiesiintymä-, saavutettavuus-, hallinnollisten rajojen ja muihin aineistoihin.
* [geofi](https://ropengov.github.io/geofi/) - kuntien, postinumeroiden sekä väestö- ja tilastoruudukkojen paikkatietoaineistojen lataus Tilastokeskukselta
* [geoR](https://cran.r-project.org/web/packages/geoR/index.html) - geostatistinen analyysi, mukaan lukien perinteiset, uskottavuuteen perustuvat ja bayesilaiset menetelmät
* [geosphere](https://cran.r-project.org/web/packages/geosphere/index.html) - sfäärinen trigonometria maantieteellisille koordinaateille (lat, lon)
* [ggmap](https://cran.r-project.org/web/packages/ggmap/index.html) - karttavisualisoinnit `ggplot2`:lla. Taustakarttoina voi käyttää erilaisia verkkolähteitä (esim. Google Maps ja Stamen Maps). Sisältää työkaluja myös geokoodaukseen ja reititykseen
* [ggspatial](https://cran.r-project.org/web/packages/ggspatial/index.html) - karttojen piirtämiseen
* [gstat](https://cran.r-project.org/web/packages/gstat/index.html) - spatiaalinen ja spatio-temporaalinen geostatistinen mallinnus, ennustus ja simulointi. Variogrammimallinnus; yksinkertainen, tavallinen ja universaali piste- tai lohko-(ko)kriging; spatio-temporaalinen kriging; sekventiaalinen Gaussinen tai indikaattori-(ko)simulointi; variogrammin ja variogrammikartan piirtotyökalut
* [GWmodel](https://cran.r-project.org/web/packages/GWmodel/index.html) - paikkapainotetut mallit: GW-kuvaileva tilastotiede, GW-pääkomponenttianalyysi, GW-diskriminanttianalyysi ja erilaiset GW-regression muodot
* [igraph]
* [lidR](https://cran.r-project.org/web/packages/lidR/index.html) - LiDAR-aineiston käsittely ja visualisointi (metsäsovelluksiin), metriikoiden laskenta aluepohjaisessa lähestymistavassa, pisteiden suodatus, keinotekoinen pisteiden harvennus, luokittelu paikkatietoaineistosta, normalisointi, yksittäisten puiden segmentointi ja muut käsittelyt. [Esimerkki](https://github.com/csc-training/geocomputing/tree/master/R/R_LiDAR/R_lidar_course_exercises)
* [lidRtRee](https://cran.r-project.org/web/packages/lidaRtRee/index.html) - metsäanalyysi ilmasta tehdyn laserskannauksen (LiDAR) aineistolla
* [mapedit](https://cran.r-project.org/web/packages/mapedit/index.html) - sf-olioiden interaktiivinen muokkaus
* [maptools](https://cran.r-project.org/web/packages/maptools/index.html) - työkaluja maantieteellisen datan käsittelyyn ja käyttöliittymäkääreet spatiaalisten olioiden vaihtamiseen useiden muiden R-pakettien kanssa
* [mapview](https://cran.r-project.org/web/packages/mapview/index.html) - interaktiivisten paikkatietovisualisointien nopea ja vaivaton luonti taustakartoilla tai ilman. Näytettyjen kohteiden attribuutteja voi kysellä kokonaisuudessaan ponnahdusikkunoiden kautta
* [ncdf4](https://cran.r-project.org/web/packages/ncdf4/index.html) - NetCDF-tiedostojen luku, kirjoitus ja muokkaus
* [ows4R](https://cran.r-project.org/web/packages/ows4R/index.html) - datan luku OGC-rajapinnoista
* [raster](https://cran.r-project.org/web/packages/raster/index.html) - pääpaketti rasteriaineistoille
* [RCSF](https://cran.r-project.org/web/packages/RCSF/index.html) - Cloth Simulation Filter (CSF) on LiDARin maanpisteiden suodatusalgoritmi
* [rlas](https://cran.r-project.org/web/packages/rlas/index.html) - 'las'- ja 'laz'-tiedostomuotojen luku ja kirjoitus
* [rstac](https://cran.r-project.org/web/packages/rstac/index.html) - asiakaskirjasto Spatio-Temporal Asset Catalogille (STAC)
* [rTLS](https://cran.r-project.org/web/packages/rTLS/index.html) - maakohdistettujen laserskannausten (TLS) pistepilvien käsittely 
* [Rsagacmd](https://cran.r-project.org/web/packages/Rsagacmd/index.html) - SAGA GIS -komentojen käyttöön R:stä
* [sen2r](https://sen2r.ranghetti.info/) - Sentinel-2 -aineiston haku, lataus ja prosessointi
* [sf](https://cran.r-project.org/web/packages/sf/index.html) - pääpaketti vektoriaineistoille, sidokset GDAL-, GEOS- ja PROJ-kirjastoihin. Toimii yhdessä tidyverse-pakettien kanssa. Samankaltaista toiminnallisuutta, mutta uudempi ja parempi kuin sp
* [sp](https://cran.r-project.org/web/packages/sp/index.html) - vanhempi pääpaketti vektoriaineistoille
* [spacetime](https://cran.r-project.org/web/packages/spacetime/index.html) - spatio-temporaalisten aineistojen käsittelyyn
* [spatial](https://cran.r-project.org/web/packages/spatial/index.html) - kriging- ja pistejakauma-analyyseihin
* [spatialreg](https://cran.r-project.org/web/packages/spatialreg/index.html) - spatiaalisiin poikkileikkausmalleihin 
* [spatstat](https://cran.r-project.org/web/packages/spatstat/index.html) - pistejakaumien analysointiin
* [spdep](https://cran.r-project.org/web/packages/spdep/index.html) - spatiaalinen riippuvuus: painotuskaavat, tilastot ja mallit
* [stars](https://cran.r-project.org/web/packages/stars/index.html) - spatio-temporaalisten taulukoiden lukeminen, käsittely, kirjoitus ja piirto (rasteri- ja vektoridatakuutiot)
* [s2](https://cran.r-project.org/web/packages/s2/index.html) - geometristen laskujen tekoon pallopinnalla
* [terra](https://cran.r-project.org/web/packages/terra/index.html) - monipuoliset menetelmät spatiaalisen datan analyysiin, erityisesti rasteriaineistoille
* [tmap](https://cran.r-project.org/web/packages/tmap/index.html) - teemakarttoihin

Voit asentaa myös omia lisäkirjastoja. Seuraa ohjeita [R:n pääsivulla](r-env.md).

### GDAL- ja SAGA GIS -tuki { #gdal-and-saga-gis-support }

Moduuli `r-env` sisältää myös [GDALin](gdal.md) ja [SAGA GISin](saga-gis.md).

### Rinnakkaislaskenta { #parallel-computing }

Jotkin R-paketit, kuten __raster__, __terra__ ja __lidR__, sisältävät rinnakkaislaskentaa tukevia toimintoja. Esimerkki __raster__-paketin predict-funktion rinnakkaiskäytöstä löytyy [esimerkeistämme](https://github.com/csc-training/geocomputing/tree/master/R). 

Monien muiden GIS-pakettien kohdalla koodin rinnakkaistaminen on tehtävä itse. Se onnistuu useilla kirjastoilla, kuten __future__. Katso lisätietoja oppaasta [Parallel jobs using R tutorial](../support/tutorials/parallel-r.md).

## Allaksen käyttö R:stä { #using-allas-from-r }

Voit käyttää Allasta R:stä __aws.s3__-paketilla. CSC:n esimerkkejä käytöstä löytyy [täältä](https://github.com/csc-training/geocomputing/blob/master/R/allas/working_with_allas_from_R_S3.R). 

On myös mahdollista __lukea__ ja __kirjoittaa__ tiedostoja Allakseen ja muista pilvipohjaisista objektivarastoista suoraan GDAL-pohjaisilla paketeilla, kuten `sf` ja `terra`. Katso ohjeet ja esimerkit oppaasta [Using geospatial files directly from cloud, inc Allas tutorial](../support/tutorials/gis/gdal_cloud.md).

Suurten Allaksessa olevien tietomäärien kanssa harkitse [virtuaalirastereiden](../support/tutorials/gis/virtual-rasters.md) käyttöä. 

## Lisenssit ja kiitokset { #license-and-acknowledgement }

Kaikki paketit on lisensoitu erilaisilla vapaan ja avoimen lähdekoodin lisensseillä (FOSS); katso tarkemmat tiedot yllä linkitetyiltä sivuilta.
Löytääksesi oikeat viittaukset R:lle ja eri R-paketeille, voit kirjoittaa:

```r
citation() # for citing R
citation("package") # for citing R packages
```

Mainitsethan CSC:n ja Geoportin julkaisuissasi; se on tärkeää projektin jatkuvuuden ja rahoitusraportoinnin kannalta.
Esimerkiksi: "Kirjoittajat haluavat kiittää CSC - IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) ja Open Geospatial Information Infrastructure for Researchia (Geoportti, urn:nbn:fi:research-infras-2016072513) laskentaresursseista ja tuesta".

## Viitteet { #references }

* [Examples for using R spatial packages for GIS in Puhti](https://github.com/csc-training/geocomputing/tree/master/R), CSC
* [List of spatial R packages in CRAN](https://cran.r-project.org/web/views/Spatial.html)
* [Spatial Data Science](https://keen-swartz-3146c4.netlify.app/), Edzer Pebesma, Roger Bivand
* [Geocomputation with R](https://geocompr.robinlovelace.net/), Robin Lovelace, Jakub Nowosad, Jannes Muenchow
* [Spatial data science with R](https://rspatial.org/index.html), Robert J. Hijmans
* [Intro to GIS and Spatial analysis](https://mgimond.github.io/Spatial/index.html), Manuel Gimond
* [Spatial Modelling for Data Scientists](https://gdsl-ul.github.io/san/), Francisco Rowe, Dani Arribas-Bel
* [Tutorial for geospatial R tools](https://datacarpentry.org/r-raster-vector-geospatial/)
* [CSC course on spatial R](https://e-learn.csc.fi/course/view.php?id=120), Marko Kallio
* [Geographic Data Science with R: Visualizing and Analyzing Environmental Change](https://bookdown.org/mcwimberly/gdswr-book/), Michael C. Wimberly
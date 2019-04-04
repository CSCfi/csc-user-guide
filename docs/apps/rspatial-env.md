rspatial-env
------------

### Description

This is an convinience module for loading easily spatial analysis related R tools. It loads the following software:

*   [R](https://research.csc.fi/-/r) (3.5.0, 3.4.3, 3.4.1) with spatial packages: geoR, geoRglm, geosphere, ggmap, grid, gstat, GWmodel, lidR, mapproj, maptools, ncdf4, RandomFields, raster, rgdal, rgeos, rgrass7, rlas, RSAGA, sf, sp, spacetime, spatial, spatial.tools, spatstat, spdep, strucchange.
*   rgdal - [GDAL/OGR](https://research.csc.fi/-/gdal-o-1) (2.2.1), [Proj4](https://research.csc.fi/-/proj4) (4.9.3)
*   rgeos - GEOS (3.6.1)
*   RSAGA - [Saga GIS](https://research.csc.fi/-/saga-gis) (5.0.0 for R 3.5.0, 2.1.4 for older R versions)
*   rgrass7 - [GRASS GIS](https://research.csc.fi/-/grass-gis) (7.2.0, without GUI)

Some R packages like **raster** and **spatial.tools** packages include functions that support parallel computing. There is an example of using predict function from raster package in parallel amoung our [examples](https://github.com/csc-training/geocomputing/tree/master/R/raster_predict). If you want to use spatial.tools package, please ask for extra guidelines from CSC servicedesk.

The other option is to write R code using R packages for parallel computing (**snow**, **doMPI**, etc). Some basic guidelines are given on basic [R page](https://research.csc.fi/-/r). There is also an example of using RSAGA contour function together with snow package amoung our [examples](https://github.com/csc-training/geocomputing/tree/master/R/contours).

* * *

### Available

##### Version on CSC's Servers

Taito: 3.4.1, 3.4.3, 3.5.0

* * *

### Usage

If you want to use Saga GIS or RStudio with GUI, you should connect to taito-shell using [\-X connection or NoMachine for Windows users](https://research.csc.fi/csc-guide-connecting-the-servers-of-csc).

In Taito and Taito-shell, to load:

`module load rspatial-env`

Please note that execution of the command unloads all current modules. Thus, if your R session depends on some atypical modules, these need to be set up following the R-enviroment startup.

For more documentation is available from the general [R page](https://research.csc.fi/-/r), inc. usage of batch jobs.

Example for submitting jobs to Taito using R and spatial packages can be found from [here](https://github.com/csc-training/geocomputing/tree/master/R).

Comments:

*   Rstudio in NoMachine, you can open RStudio with spatial packeges in NoMachine from the Fluxbox menu: Applications -> Taito-shell -> GIS -> RStudio for GIS. The Rstudio under Mathematics menu does not include the spatial packages.
    *   You can achive the same also with loading rspatial-env and rstudio modules and opening Rstudio.

`module load rspatial-env rstudio  
rstudio`

*   RSAGA:
    *   RSAGA gives error messages: "Error: select a tool", but it seems to be [a bug of SAGA](https://github.com/debangs/RSAGA/blob/master/Updates%20-%20News.md). According to our tests it seems that RSAGA commands are working despite the message.
    *   RSAGA io\_gdal library does not work with rspatial-env, because of GDAL versions confict. Please try to use rgdal functions if possible. If that is not suitable solution, it is possible to use SAGA with older versions of GDAL and R, but then the list of pre-loaded R spatial packages and supported GDAL tools and formats is more limited.

`module load r-env/2.2.1 geos/3.4.2 proj4/4.9.1 gdal/1.11.1 wxwidgets saga/2.1.4`

* * *

### Discipline

Geosciences  

* * *

### References

* * *

### Support

* * *

### Manual

A lot of materials about using R for spatial analysis are available:

*   CRAN Task View of Analysis of Spatial Data: [https://cran.r-project.org/web/views/Spatial.html](https://cran.r-project.org/web/views/Spatial.html) Which packages are availeble for spatial analysis with R?
*   Robin Lovelace, Jakub Nowosad, Jannes Muenchow, under development book "[Geocomputation with R](https://geocompr.robinlovelace.net)". A lot of different topics, uses the new sf package for vector data.
*   GFC, [Spatial Data Analysis and Modeling with R](http://rspatial.org/index.html) A lot of different topics, uses the older sp package for vector data.
*   Manuel Gimond, [Intro to GIS and Spatial Analysis](https://mgimond.github.io/Spatial/index.html) A lot of different topics, uses the older sp package for vector data.
*   Marko Kallio, Juha Aalto, Kylli Ek, [Spatial data analysis with R](https://www.csc.fi/web/training/-/spatial-data-analysis-with-r). 2-day course materials, inc intro to using R in Taito.
*   Anssi Lensu (JYU), [Paikkatiedon käsittely- ja analysointiominaisuudet R-tilasto-ohjelmassa](https://research.csc.fi/documents/48467/73380/Lensu_FIUGINET_GItutkpva2013.pdf/164ba2e5-cde3-48c2-9d99-862156d797ba) Presentation at Finnish Geoinformatics research days 2013.
*   [gisfin](https://github.com/rOpenGov/gisfin) - Tools for using open Finnish spatial data.

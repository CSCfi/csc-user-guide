---
tags:
  - Free
---

# R for GIS

This page is for the spatial R libraries and tools installed in the R environment in Puhti. Documentation for R in general is located on the [`r-env` page](r-env.md). Spatial libraries are included in all R versions in Puhti.

## Usage

### Loading the module

Load the general R module with

```
module load r-env
```

### Installed spatial R libraries

* [aws.s3](https://cran.r-project.org/web/packages/aws.s3/) - for working with S3 storage, for example Allas. [Example](https://github.com/csc-training/geocomputing/blob/master/R/allas/working_with_allas_from_R_S3.R).
* [CAST](https://cran.r-project.org/web/packages/CAST/index.html) - functionality to run `caret` with spatial or spatial-temporal data
* [fasterize](https://cran.r-project.org/web/packages/fasterize/index.html) -  a faster replacement for rasterize() from the `raster` package 
* [FORTLS](https://cran.r-project.org/web/packages/FORTLS/index.html) - processing of terrestrial laser scanning (TLS) point cloud data for forestry purposes
* [gdalcubes](https://cran.r-project.org/web/packages/gdalcubes/index.html) - for working with multitemporal raster data cubes
* [geodata](https://cran.r-project.org/web/packages/geodata/index.html) - access to climate, crops, elevation, land use, soil, species occurrence, accessibility, administrative boundaries and other data.
* [geofi](https://ropengov.github.io/geofi/) - download geospatial data on municipalities, zipcodes and population and statistical grids from Statistics Finland
* [geoR](https://cran.r-project.org/web/packages/geoR/index.html) - geostatistical analysis including traditional, likelihood-based and Bayesian methods
* [geosphere](https://cran.r-project.org/web/packages/geosphere/index.html) - spherical trigonometry for geographic coordinates (lat, lon)
* [ggmap](https://cran.r-project.org/web/packages/ggmap/index.html) - map visualizations with `ggplot2`. As background map various online sources can be ued (e.g Google Maps and Stamen Maps). It includes tools also for geocoding and routing
* [ggspatial](https://cran.r-project.org/web/packages/ggspatial/index.html) - for map plotting
* [gstat](https://cran.r-project.org/web/packages/gstat/index.html) - spatial and spatio-temporal geostatistical modelling, prediction and simulation. Variogram modelling; simple, ordinary and universal point or block (co)kriging; spatio-temporal kriging; sequential Gaussian or indicator (co)simulation; variogram and variogram map plotting utility functions
* [GWmodel](https://cran.r-project.org/web/packages/GWmodel/index.html) - geographically-weighted models: GW summary statistics, GW principal components analysis, GW discriminant analysis and various forms of GW regression
* [igraph]
* [lidR](https://cran.r-project.org/web/packages/lidR/index.html) - LiDAR data manipulation and visualization (for forestry applications), computation of metrics in area based approach, point filtering, artificial point reduction, classification from geographic data, normalization, individual tree segmentation and other manipulations. [Example](https://github.com/csc-training/geocomputing/tree/master/R/R_LiDAR/R_lidar_course_exercises)
* [lidRtRee](https://cran.r-project.org/web/packages/lidaRtRee/index.html) - forest analysis with airborne laser scanning (LiDAR) data
* [mapedit](https://cran.r-project.org/web/packages/mapedit/index.html) - interactive editing of sf objects
* [maptools](https://cran.r-project.org/web/packages/maptools/index.html) - tools for manipulating geographic data and interface wrappers for exchanging spatial objects with several other R packages
* [mapview](https://cran.r-project.org/web/packages/mapview/index.html) - quickly and conveniently create interactive visualisations of spatial data with or without background maps. Attributes of displayed features are fully queryable via pop-up windows
* [ncdf4](https://cran.r-project.org/web/packages/ncdf4/index.html) - read, write and modify NetCDF-files
* [ows4R](https://cran.r-project.org/web/packages/ows4R/index.html) - reading data from OGC APIs
* [raster](https://cran.r-project.org/web/packages/raster/index.html) - main package for raster data
* [RCSF](https://cran.r-project.org/web/packages/RCSF/index.html) - Cloth Simulation Filter (CSF) is an LiDAR ground points filtering algorithm
* [rlas](https://cran.r-project.org/web/packages/rlas/index.html) - read and write 'las' and 'laz' file formats
* [rstac](https://cran.r-project.org/web/packages/rstac/index.html) - client library for Spatio-Temporal Asset Catalog (STAC)
* [rTLS](https://cran.r-project.org/web/packages/rTLS/index.html) - process terrestrial laser scanning (TLS) point clouds 
* [Rsagacmd](https://cran.r-project.org/web/packages/Rsagacmd/index.html) - for using SAGA GIS commands from R
* [sen2r](https://sen2r.ranghetti.info/) - find, download and process Sentinel-2 data
* [sf](https://cran.r-project.org/web/packages/sf/index.html) - main package for vector data, bindings to GDAL, GEOS and PROJ libraries. Works with tidyverse packages. Similar functionality, but newer and better than sp
* [sp](https://cran.r-project.org/web/packages/sp/index.html) - older main package for vector data
* [spacetime](https://cran.r-project.org/web/packages/spacetime/index.html) - for working with spatio-temporal data
* [spatial](https://cran.r-project.org/web/packages/spatial/index.html) - for kriging and point pattern analysis
* [spatialreg](https://cran.r-project.org/web/packages/spatialreg/index.html) - for spatial cross-sectional models 
* [spatstat](https://cran.r-project.org/web/packages/spatstat/index.html) - for analysing point patterns
* [spdep](https://cran.r-project.org/web/packages/spdep/index.html) - spatial dependence: weighting schemes, statistics and models
* [stars](https://cran.r-project.org/web/packages/stars/index.html) - reading, manipulating, writing and plotting spatiotemporal arrays (raster and vector data cubes)
* [s2](https://cran.r-project.org/web/packages/s2/index.html) - for geometric calculations on the sphere
* [terra](https://cran.r-project.org/web/packages/terra/index.html) - diverse methods for spatial data analysis, particularly raster data
* [tmap](https://cran.r-project.org/web/packages/tmap/index.html) - for thematic maps

You can also install your own additional libraries. Just follow the instructions in the [main R page](r-env.md).

### GDAL and SAGA GIS support

The `r-env` module includes also [GDAL](gdal.md) and [SAGA GIS](saga-gis.md).

### Parallel computing

Some R packages like __raster__, __terra__ and __lidR__ include functions that support parallel computing. There is an example of using predict function from raster package in parallel among our [examples](https://github.com/csc-training/geocomputing/tree/master/R). 

For many other GIS packages you have to parallelize the code yourself. It can be done with several libraries, including __future__. See [Parallel jobs using R tutorial](../support/tutorials/parallel-r.md) for further information.

## Using Allas from R

You can use Allas from R with the package __aws.s3__. You can find CSC examples how to use it [here](https://github.com/csc-training/geocomputing/blob/master/R/allas/working_with_allas_from_R_S3.R). 

It is also possible to __read__ and __write__ files from and to Allas or other cloud object storage directly with GDAL-based packages such as `sf` and `terra`. Please check our [Using geospatial files directly from cloud, inc Allas tutorial](../support/tutorials/gis/gdal_cloud.md) for instructions and examples.

With large quantities of data in Allas, consider using [virtual rasters](../support/tutorials/gis/virtual-rasters.md). 

## License and acknowledgement

All packages are licensed under various free and open source licenses (FOSS), see the linked pages above for exact details.
For finding out the correct citations for R and different R packages, you can type:

```r
citation() # for citing R
citation("package") # for citing R packages
```

Please acknowledge CSC and Geoportti in your publications, it is important for project continuation and funding reports.
As an example, you can write "The authors wish to thank CSC - IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (Geoportti, urn:nbn:fi:research-infras-2016072513) for computational resources and support".

## References

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

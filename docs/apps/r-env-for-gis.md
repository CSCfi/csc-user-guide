# R for GIS

This page is for the spatial R libraries and tools installed in the R environment in Puhti. The documentation for R in general is located in the [r-environment](r-env.md) page. 

## Available

Currently supported R versions for spatial libraries:

- 3.6.1

## Usage

### Loading the module

You can load the general R module with

```
module load r-env
```

### Installed spatial R libraries

* [geoR](https://cran.r-project.org/web/packages/geoR/index.html) - geostatistical analysis including traditional, likelihood-based and Bayesian methods
* [geoRglm](https://cran.r-project.org/web/packages/geoRglm/index.html) - functions for inference in generalised linear spatial models, extension to the geoR package
* [geosphere](https://cran.r-project.org/web/packages/geosphere/index.html) - spherical trigonometry for geographic coordinates (lat, lon)
* [ggmap](https://cran.r-project.org/web/packages/ggmap/index.html) - map visualizations with ggplot2. As background map various online sources can be ued (e.g Google Maps and Stamen Maps). It includes tools also for geocoding and routing
* [gstat](https://cran.r-project.org/web/packages/gstat/index.html) - spatial and spatio-temporal geostatistical modelling, prediction and simulation. Variogram modelling; simple, ordinary and universal point or block (co)kriging; spatio-temporal kriging; sequential Gaussian or indicator (co)simulation; variogram and variogram map plotting utility functions
* [GWmodel](https://cran.r-project.org/web/packages/GWmodel/index.html) - geographically-weighted models: GW summary statistics, GW principal components analysis, GW discriminant analysis and various forms of GW regression
* [lidR](https://cran.r-project.org/web/packages/lidR/index.html) - LiDAR data manipulation and visualization (for forestry applications), computation of metrics in area based approach, point filtering, artificial point reduction, classification from geographic data, normalization, individual tree segmentation and other manipulations
* [mapedit](https://cran.r-project.org/web/packages/mapedit/index.html) - interactive editing of sf objects
* [maptools](https://cran.r-project.org/web/packages/maptools/index.html)
* [mapview](https://cran.r-project.org/web/packages/mapview/index.html) - quickly and conveniently create interactive visualisations of spatial data with or without background maps. Attributes of displayed features are fully queryable via pop-up windows
* [ncdf4](https://cran.r-project.org/web/packages/ncdf4/index.html) - read, write and modify NetCDF-files
* [RandomFields](https://cran.r-project.org/web/packages/RandomFields/index.html) - simulation and analysis of random fields
* [raster](https://cran.r-project.org/web/packages/raster/index.html) - main package for raster data
* [rgdal](https://cran.r-project.org/web/packages/rgdal/index.html) - bindings to GDAL and PROJ4 libraries, for basic data reading and writing
* [rgeos](https://cran.r-project.org/web/packages/rgeos/index.html) - binding to GEOS library, for topology operations on geometries
* [rlas](https://cran.r-project.org/web/packages/rlas/index.html) - read and write 'las' and 'laz' file formats
* [RSAGA](https://cran.r-project.org/web/packages/RSAGA/index.html) - for using SAGA GIS commands from R
* [sf](https://cran.r-project.org/web/packages/sf/index.html) - main package for vector data, bindings to GDAL, GEOS and PROJ4 libraries. Works with tidyverse packages. Similar functionality, but newer and better than sp
* [sp](https://cran.r-project.org/web/packages/sp/index.html) - older main package for vector data
* [spacetime](https://cran.r-project.org/web/packages/spacetime/index.html) - for working with spatio-temporal data
* [spatial](https://cran.r-project.org/web/packages/spatial/index.html) - for kriging and point pattern analysis
* [spatial.tools](https://cran.r-project.org/web/packages/spatial.tools/index.html) - to enhance the core functionality of the package "raster", including a parallel processing engine for use with rasters
* [spdep](https://cran.r-project.org/web/packages/spdep/index.html) - spatial dependence: weighting schemes, statistics and models
* [spatstat](https://cran.r-project.org/web/packages/spatstat/index.html) - for analysing point patterns
* [viridis](https://cran.r-project.org/web/packages/viridis/index.html) - color maps for map plotting
* [fasterize](https://cran.r-project.org/web/packages/fasterize/index.html) -  a faster replacement for rasterize() from the 'raster' package 

You can also install your own additional libraries. Just follow the instructions in the [main R page](r-env.md)


### Parallel computing 

Some R packages like __raster__ and __spatial.tools__ include functions that support parallel computing. There is an example of using predict function from raster package in parallel amoung our [examples](https://github.com/csc-training/geocomputing/tree/master/R/raster_predict). 

Other than those, you have to parallelize your own R code which can be done with libraries like __Rmpi__ and __snow__.

!!! note
    Parallel computing with snow and Rmpi (like on Taito) does not work at the moment in Puhti. That capability is coming soon.

## Citation

For finding out the correct citations for R and different R packages, you can type:

```r
citation() # for citing R
citation("package") # for citing R packages
```

## References

* [Spatial analysis examples (CSC)](https://github.com/csc-training/geocomputing/tree/master/R)
* [Tutorial for geospatial R tools](https://datacarpentry.org/r-raster-vector-geospatial/)
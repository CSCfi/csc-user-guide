# R for GIS

This page is for the spatial R libraries and tools installed in the R environment in Puhti. Documentation for R in general is located on the [`r-env-singularity` page](r-env-singularity.md).

## Available

Currently supported R versions for spatial libraries:

- 4.0.3, 4.0.2 and 3.6.3 (`r-env-singularity` module)

## Usage

### Loading the module

You can load the general R module with

```
module load r-env-singularity
```

### Installed spatial R libraries

* [aws.s3](https://cran.r-project.org/web/packages/aws.s3/) - for working with S3 storage, for example Allas. [Example](https://github.com/csc-training/geocomputing/blob/master/R/allas/working_with_allas_from_R_S3.R).
* [CAST](https://cran.r-project.org/web/packages/CAST/index.html) - functionality to run `caret` with spatial or spatial-temporal data
* [fasterize](https://cran.r-project.org/web/packages/fasterize/index.html) -  a faster replacement for rasterize() from the `raster` package 
* [gdalcubes](https://cran.r-project.org/web/packages/gdalcubes/index.html) - for working with multitemporal raster data cubes
* [gdalUtils](https://cran.r-project.org/web/packages/gdalUtils/index.html) - wrappers for GDAL utilities
* [geoR](https://cran.r-project.org/web/packages/geoR/index.html) - geostatistical analysis including traditional, likelihood-based and Bayesian methods
* [geosphere](https://cran.r-project.org/web/packages/geosphere/index.html) - spherical trigonometry for geographic coordinates (lat, lon)
* [ggmap](https://cran.r-project.org/web/packages/ggmap/index.html) - map visualizations with `ggplot2`. As background map various online sources can be ued (e.g Google Maps and Stamen Maps). It includes tools also for geocoding and routing
* [gstat](https://cran.r-project.org/web/packages/gstat/index.html) - spatial and spatio-temporal geostatistical modelling, prediction and simulation. Variogram modelling; simple, ordinary and universal point or block (co)kriging; spatio-temporal kriging; sequential Gaussian or indicator (co)simulation; variogram and variogram map plotting utility functions
* [GWmodel](https://cran.r-project.org/web/packages/GWmodel/index.html) - geographically-weighted models: GW summary statistics, GW principal components analysis, GW discriminant analysis and various forms of GW regression
* [gstat](https://cran.r-project.org/web/packages/gstat/index.html) - functions for variogram modelling and kriging data 
* [lidR](https://cran.r-project.org/web/packages/lidR/index.html) - LiDAR data manipulation and visualization (for forestry applications), computation of metrics in area based approach, point filtering, artificial point reduction, classification from geographic data, normalization, individual tree segmentation and other manipulations
* [mapedit](https://cran.r-project.org/web/packages/mapedit/index.html) - interactive editing of sf objects
* [maptools](https://cran.r-project.org/web/packages/maptools/index.html) - tools for manipulating geographic data and interface wrappers for exchanging spatial objects with several other R packages
* [mapview](https://cran.r-project.org/web/packages/mapview/index.html) - quickly and conveniently create interactive visualisations of spatial data with or without background maps. Attributes of displayed features are fully queryable via pop-up windows
* [ncdf4](https://cran.r-project.org/web/packages/ncdf4/index.html) - read, write and modify NetCDF-files
* [RandomFields](https://cran.r-project.org/web/packages/RandomFields/index.html) - simulation and analysis of random fields
* [raster](https://cran.r-project.org/web/packages/raster/index.html) - main package for raster data
* [rgdal](https://cran.r-project.org/web/packages/rgdal/index.html) - bindings to GDAL and PROJ libraries, for basic data reading and writing
* [rgeos](https://cran.r-project.org/web/packages/rgeos/index.html) - binding to GEOS library, for topology operations on geometries
* [rlas](https://cran.r-project.org/web/packages/rlas/index.html) - read and write 'las' and 'laz' file formats
* [RSAGA](https://cran.r-project.org/web/packages/RSAGA/index.html) - for using SAGA GIS commands from R (no longer actively maintained)
* [Rsagacmd](https://cran.r-project.org/web/packages/Rsagacmd/index.html) - for using SAGA GIS commands from R (actively maintained, supports newer SAGA GIS versions)
* [sf](https://cran.r-project.org/web/packages/sf/index.html) - main package for vector data, bindings to GDAL, GEOS and PROJ libraries. Works with tidyverse packages. Similar functionality, but newer and better than sp
* [sp](https://cran.r-project.org/web/packages/sp/index.html) - older main package for vector data
* [spacetime](https://cran.r-project.org/web/packages/spacetime/index.html) - for working with spatio-temporal data
* [spatial](https://cran.r-project.org/web/packages/spatial/index.html) - for kriging and point pattern analysis
* [spatstat](https://cran.r-project.org/web/packages/spatstat/index.html) - for analysing point patterns
* [spdep](https://cran.r-project.org/web/packages/spdep/index.html) - spatial dependence: weighting schemes, statistics and models
* [stars](https://cran.r-project.org/web/packages/stars/index.html) - reading, manipulating, writing and plotting spatiotemporal arrays (raster and vector data cubes)
* [terra](https://cran.r-project.org/web/packages/terra/index.html) - diverse methods for spatial data analysis, particularly raster data
* [viridis](https://cran.r-project.org/web/packages/viridis/index.html) - color maps for map plotting

You can also install your own additional libraries. Just follow the instructions in the [main R page](r-env-singularity.md).

### GDAL and SAGA GIS support

The `r-env-singularity` module includes the following GDAL and SAGA GIS installations.

`r-env-singularity/3.6.3`:

* [GDAL](gdal.md) 2.4.2 and its commandline tools 
* [SAGA GIS](saga-gis.md) 7.3.0

`r-env-singularity/4.0.2` and `r-env-singularity/4.0.3`:

- GDAL 3.2.0 and its commandline tools

- SAGA GIS 7.9.0

### Parallel computing

Some R packages like __raster__ and __spatial.tools__ include functions that support parallel computing. There is an example of using predict function from raster package in parallel among our [examples](https://github.com/csc-training/geocomputing/tree/master/R/raster_predict). 

Other than those, you have to parallelize your own R code which can be done with libraries including __snow__ (see the documentation for the [r-env-singularity module](r-env-singularity.md)).

## Interactive usage

It is possible to use [RStudio with an interactive session](../support/tutorials/rstudio-or-jupyter-notebooks.md).

## Using Allas from R

You can use Allas from R with the package __aws.s3__. You can find CSC examples how to use it [here](https://github.com/csc-training/geocomputing/blob/master/R/allas/working_with_allas_from_R_S3.R). It is possible to [use files directly](gdal.md#using-files-directly-from-allas) from Allas with libraries like __sf__ and __raster__. With large quantities of data in Allas, virtual rasters should be considered. More information on how to create and use virtual rasters can be found [here.](https://research.csc.fi/virtual_rasters)

## Citation

For finding out the correct citations for R and different R packages, you can type:

```r
citation() # for citing R
citation("package") # for citing R packages
```

In your publications please acknowledge also oGIIR and CSC, for example “The authors wish to acknowledge for computational resources CSC – IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (oGIIR, urn:nbn:fi:research-infras-2016072513).”

## References

* [Geocomputation with R (book)](https://geocompr.robinlovelace.net/)
* [CSC course on spatial R](https://www.csc.fi/web/training/-/spatial-data-analysis-with-1)
* [Intro to GIS and Spatial analysis](https://mgimond.github.io/Spatial/index.html)
* [List of spatial R packages](https://cran.r-project.org/web/views/Spatial.html)
* [Spatial data science with R](https://rspatial.org/index.html)
* [Spatial analysis examples (CSC)](https://github.com/csc-training/geocomputing/tree/master/R)
* [Tutorial for geospatial R tools](https://datacarpentry.org/r-raster-vector-geospatial/)

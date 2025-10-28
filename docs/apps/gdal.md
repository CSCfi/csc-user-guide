---
tags:
  - Free
catalog:
  name: GDAL
  description: for geospatial data formats
  license_type: Free
  disciplines:
    - Geosciences
  available_on:
    - LUMI
    - Puhti
    - Mahti
---

# GDAL

[GDAL](https://gdal.org/) (Geospatial Data Abstraction Library) is a GIS translator library for accessing and transforming geospatial data. Most commonly it is used in file format or coordinate system changes. 

## Available

GDAL is available with following versions:

* 3.9.2 - in the 3.38 [QGIS](qgis.md) and 3.11.10 [geoconda](geoconda.md) in Puhti
* 3.9.1 - in the 3.11.9 [geoconda](geoconda.md) in Puhti and Mahti
* 3.8.5 stand-alone: `gdal` in Puhti
* 3.8.3 - in the 3.31 [QGIS](qgis.md) in Puhti and LUMI
* 3.6.2 - in the 3.10.x [geoconda](geoconda.md) in Puhti and Mahti
* 3.4.3 stand-alone: `gdal` in Puhti
* Also in Puhti: [r-env](r-env-for-gis.md#gdal-and-saga-gis-support) and [OrfeoToolBox](otb.md)

!!! note
    The stand-alone GDAL and R modules don't have Python bindings installed so e.g `gdal_calc` works only in the geoconda and qgis modules. Also, the supported file formats vary between the modules. `gdal/3.4.3` has the most limited driver support and no support for virtual drivers. It is possible to add more drivers to standalone and r-env GDAL installations, please ask. geoconda and qgis GDAL installations are based on conda gdal package and are impossible to change regarding drivers support. Use `gdalinfo --formats` to see supported raster formats and `ogrinfo --formats` for vector formats.

## Usage
GDAL is included in the modules listed above, so it can be used when any of these modules is loaded. 

The stand-alone `gdal` module is mainly meant for building software on top of GDAL, but can also be used for command-line usage. To load stand-alone `gdal` use:

```
# GDAL 3.8.5
module load gcc/13.2.0 openmpi/5.0.5 gdal/3.8.5
# GDAL 3.4.3
module load gcc/11.3.0 gdal/3.4.3
```

You can test if GDAL loaded successfully with following

`gdalinfo --version`

With `r-env` gdal commands can be used as:

`apptainer_wrapper exec gdalinfo --version`


#### Using files directly from object storage services or cloud, inc Allas

GDAL supports virtual [network based file systems](https://gdal.org/user/virtual_file_systems.html#network-based-file-systems) for reading and sometimes writing from several cloud storage systems, inc CSC Allas, Amazon S3, Google Cloud Storage, Microsoft Azure etc. Please check CSC's [Using geospatial files directly from cloud, inc Allas tutorial](../support/tutorials/gis/gdal_cloud.md) for instructions and examples.

#### Virtual rasters

With large quantities of raster data (also in Allas), the most convenient method of accessing them might be [GDAL virtual rasters](../support/tutorials/gis/virtual-rasters.md). 

## License 

[GDAL is licensed under an MIT/X style license](https://gdal.org/license.html)

## Citation
GDAL/OGR contributors (2024). 
GDAL/OGR Geospatial Data Abstraction software Library. 
Open Source Geospatial Foundation. 
URL https://gdal.org, 
DOI: 10.5281/zenodo.5884351


## Acknowledgement

Please acknowledge CSC and Geoportti in your publications, it is important for project continuation and funding reports.
As an example, you can write "The authors wish to thank CSC - IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (Geoportti, urn:nbn:fi:research-infras-2016072513) for computational resources and support".


## Installation 

Standalone GDAL was installed to Puhti using [Spack and its GDAL package definition](https://packages.spack.io/package.html?name=gdal). For other installations, see respective application page.

Installation settings for 3.8.5. `+` means enabled option, `~` disabled.
```
gdal@3.8.5+arrow+curl+deflate+expat+geos+gif+hdf4+hdf5+iconv+jpeg+liblzma+libxml2+lz4+netcdf+openjpeg+png+postgresql+spatialite+sqlite3+zstd
~archive~armadillo~basisu~blosc~brunsli~cfitsio~crnlib~cryptopp~csharp~ecw~filegdb~freexl~fyba~gta~hdfs~heif~idb~ipo~java~jxl~kdu~kea~lerc
~libaec~libcsf~libkml~libqb3~luratech~mongocxx~mrsid~mssql_ncli~mssql_odbc~mysql~odbc~odbccpp~ogdi~opencad~opencl~openexr~openssl~oracle
~parquet~pcidsk~pcre2~pdfium~podofo~poppler~python~qhull~rasterlite2~rdb~sfcgal~teigha~tiledb~webp~xercesc
build_system=cmake build_type=Release generator=ninja patches=52459dc
```

Installation settings for 3.4.3:
```
--with-libtiff=/appl/spack/v018/install-tree/gcc-11.3.0/libtiff-4.3.0-4xvmnn
--with-geotiff=/appl/spack/v018/install-tree/gcc-11.3.0/libgeotiff-1.6.0-m66qzg
--with-libjson-c=/appl/spack/v018/install-tree/gcc-11.3.0/json-c-0.15-cvy2yv
--with-proj=/appl/spack/v018/install-tree/gcc-11.3.0/proj-8.2.1-zj2pln
--with-libtool=yes
--with-libz=/appl/spack/v018/install-tree/gcc-11.3.0/zlib-1.2.12-tpcwxh
--with-liblzma=yes
--with-jpeg=/appl/spack/v018/install-tree/gcc-11.3.0/libjpeg-turbo-2.1.3-hnflqm"
```
## References

* [GDAL documentation, programs](https://gdal.org/programs/index.html)
* [GDAL tutorial by CSC](../support/tutorials/gis/gdal.md)
* [GDAL cheat sheet](https://github.com/dwtkns/gdal-cheat-sheet)
* [GDAL Linux examples](https://github.com/clhenrick/shell_scripts)

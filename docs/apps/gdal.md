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
    - Mahti
    - Roihu
---

# GDAL

[GDAL](https://gdal.org/) (Geospatial Data Abstraction Library) is a GIS translator library for accessing and transforming geospatial data. Most commonly it is used in file format or coordinate system changes. 

## Available

GDAL is available with following versions:

* 3.12.4 - in the 3.44.9 [QGIS](qgis.md) in Roihu.
* 3.12.2 - in the 3.14.5 [python-geo](python-geo.md) in Roihu
* 3.12.2 stand-alone: `gdal` in Roihu. Additionally is available `proj/9.7.0`.
* 3.9.1 - in the 3.11.9 [geoconda](geoconda.md) in Mahti
* 3.8.3 - in the 3.31 [QGIS](qgis.md) in LUMI
* 3.6.2 - in the 3.10.x [geoconda](geoconda.md) in Mahti
* Also in: [r-env](r-env-for-gis.md#gdal-and-saga-gis-support) and [OrfeoToolBox](otb.md)

!!! note
    The stand-alone GDAL and R modules don't have Python bindings installed so e.g `gdal_calc` works only in the geoconda and qgis modules. Also, the supported file formats vary between the modules. It is possible to add more drivers to standalone and r-env GDAL installations, please ask. geoconda and qgis GDAL installations are based on conda gdal package and are impossible to change regarding drivers support. Use `gdalinfo --formats` to see supported raster formats and `ogrinfo --formats` for vector formats.

## Usage
GDAL is included in the modules listed above, so it can be used when any of these modules is loaded. 

The stand-alone `gdal` module is mainly meant for building software on top of GDAL, but can also be used for command-line usage. To load stand-alone `gdal` use:

```
# GDAL 3.12.2 (Roihu)
gcc/15.2.0  openmpi/5.0.10 gdal/3.12.2
```

You can test if GDAL loaded successfully with following

`gdalinfo --version`

Note that, starting with GDAL 3.11, parts of the GDAL utilities are available from a [new single gdal program](https://gdal.org/en/stable/programs/index.html) that accepts commands and subcommands.


#### Using files directly from object storage services or cloud, inc Allas

GDAL supports virtual [network based file systems](https://gdal.org/user/virtual_file_systems.html#network-based-file-systems) for reading and sometimes writing from several cloud storage systems, inc CSC Allas, Amazon S3, Google Cloud Storage, Microsoft Azure etc. Please check CSC's [Using geospatial files directly from cloud, inc Allas tutorial](../support/tutorials/gis/gdal_cloud.md) for instructions and examples.

#### Virtual rasters

With large quantities of raster data (also in Allas), the most convenient method of accessing them might be [GDAL virtual rasters](../support/tutorials/gis/virtual-rasters.md). 

## License 

[GDAL is licensed under an MIT/X style license](https://gdal.org/license.html)

## Citation
GDAL/OGR contributors (2026). 
GDAL/OGR Geospatial Data Abstraction software Library. 
Open Source Geospatial Foundation. 
URL https://gdal.org, 
DOI: 10.5281/zenodo.5884351


## Acknowledgement

Please acknowledge CSC and Geoportti in your publications, it is important for project continuation and funding reports.
As an example, you can write "The authors wish to thank CSC - IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (Geoportti, urn:nbn:fi:research-infras-2016072513) for computational resources and support".


## Installation 

Standalone GDAL was installed using [Spack and its GDAL package definition](https://packages.spack.io/package.html?name=gdal). For other installations, see respective application page.

Installation settings for 3.12.2. `+` means enabled option,
```
gdal+deflate+expat+gif+hdf5+iconv+jpeg+liblzma+libxml2+lz4+netcdf+openjpeg+parquet+png+postgresql+zstd
```

## References

* [GDAL documentation, programs](https://gdal.org/programs/index.html)
* [GDAL tutorial by CSC](../support/tutorials/gis/gdal.md)
* [GDAL cheat sheet](https://github.com/dwtkns/gdal-cheat-sheet)
* [GDAL Linux examples](https://github.com/clhenrick/shell_scripts)

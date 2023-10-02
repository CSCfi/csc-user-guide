---
tags:
  - Free
---

# GDAL

[GDAL](https://gdal.org/) (Geospatial Data Abstraction Library) is a GIS translator library for accessing and transforming geospatial data. Most commonly it is used in file format or coordinate system changes. 

## Available

GDAL is available with following versions:

* 3.5.0 - [geoconda-3.10.6](geoconda.md) in Puhti
* 3.4.3 stand-alone: `gdal` in Puhti
* 3.4.1 - [QGIS-3.31 module](qgis.md) in Puhti and LUMI
* Also in Puhti: [r-env](r-env-for-gis.md#gdal-and-saga-gis-support) and [OrfeoToolBox](otb.md)

!!! note
    The stand-alone version doesn't have python bindings installed so e.g __gdal_calc__ works only in the geoconda installations. Also, the supported file formats vary slightly between the GDAL installations. For instance, the PostGIS driver is not available in stand-alone gdal but is included in the geoconda versions.

## Usage

### Using GDAL

GDAL is included in the modules listed above, so it can be used when any of these modules is loaded.

If you need to use a stand-alone version of GDAL or plan to build software on top of GDAL, you can load GDAL with

`module load gdal`

By default the latest gdal module is loaded. If you want a specific version you can specify the version number

`module load gdal/<VERSION>`

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
GDAL/OGR contributors (2022). 
GDAL/OGR Geospatial Data Abstraction software Library. 
Open Source Geospatial Foundation. 
URL https://gdal.org, 
DOI: 10.5281/zenodo.5884351



## Acknowledgement

Please acknowledge CSC and Geoportti in your publications, it is important for project continuation and funding reports.
As an example, you can write "The authors wish to thank CSC - IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (Geoportti, urn:nbn:fi:research-infras-2016072513) for computational resources and support".


## Installation 

Standalone GDAL was installed to Puhti using [Spack and its GDAL package definition](https://spack.readthedocs.io/en/latest/package_list.html#gdal) FIXME. For other installations, see respective application page.


## References

* [GDAL documentation, programs](https://gdal.org/programs/index.html)
* [GDAL tutorial by CSC](../support/tutorials/gis/gdal.md)
* [GDAL cheat sheet](https://github.com/dwtkns/gdal-cheat-sheet)
* [GDAL Linux examples](https://github.com/clhenrick/shell_scripts)

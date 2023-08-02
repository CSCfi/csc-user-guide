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


### Using files directly from Allas

It is possible to __read__ files from Allas directly with GDAL, but not to write. For results, write them first to Puhti scratch and move later to Allas. The below mentioned virtual drivers are supported also in many GDAL-based tools. The set up is the same as below, but instead of the example gdalinfo command open the file from Python or R script. In R and Python it is possible also to write to Allas directly from script. We have tested successfully: 

 * [Python](geoconda.md): gdal, geopandas, fiona and rasterio. [Example](https://github.com/csc-training/geocomputing/blob/master/python/allas/working_with_allas_from_Python_S3.py). 
 * [R](r-env-for-gis.md): sf, raster. [Example](https://github.com/csc-training/geocomputing/blob/master/R/allas/working_with_allas_from_R_S3.R). 
 * [QGIS](qgis.md)

Reading data directly from Allas is slower than reading from scratch or other supercomputer lustre disks, for example reading a ~500 Mb files from scratch takes ~1 second, but from Allas ~10 seconds. In most cases still compared to full duration of an analysis, these seconds are not important.

__Public files__ in Allas can be read with [`vsicurl`](https://gdal.org/user/virtual_file_systems.html#vsicurl):  
```
gdalinfo /vsicurl/https://a3s.fi/<name_of_your_bucket>/<name_of_your_file>
```

__Private files__ can be read by SWIFT or S3 API. SWIFT is more secure, but the credentials need to be updated after 8 hours. S3 has permanent keys, and is therefore little bit easier to use, but less secure. Both of these have a random reading and streaming API.

__SWIFT.__ Set up the connection in Puhti and then read the files with [`vsiswift`-driver](https://gdal.org/user/virtual_file_systems.html#vsiswift-openstack-swift-object-storage-random-reading):

```
module load allas
allas-conf
export SWIFT_AUTH_TOKEN=$OS_AUTH_TOKEN 
export SWIFT_STORAGE_URL=$OS_STORAGE_URL
gdalinfo /vsiswift/<name_of_your_bucket>/<name_of_your_file>
```

The export commands are needed because GDAL is looking for different environment variables than what allas-conf is writing. These commands need to be given each time you start working with Puhti, because the token is valid for 8 hours. Inside batchjobs use [allas-conf -k](../data/Allas/allas_batchjobs.md).

__S3.__ 
Set up the connection in Puhti and then read the files with [vsis3-driver](https://gdal.org/user/virtual_file_systems.html#vsis3-aws-s3-files-random-reading):
```
module load allas
allas-conf --mode s3cmd
gdalinfo /vsis3/<name_of_your_bucket>/<name_of_your_file>
```

* `module load allas` sets AWS_S3_ENDPOINT environment variable, which needs to be run each time S3 is used.
* `allas-conf` command saves your credentials in your home directory to .aws/credentials file. This needs to be run only once before first use or when you want to switch to another CSC project.


### Virtual rasters

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


## Acknowledgement

Please acknowledge CSC and Geoportti in your publications, it is important for project continuation and funding reports.
As an example, you can write "The authors wish to thank CSC - IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (Geoportti, urn:nbn:fi:research-infras-2016072513) for computational resources and support".


## Installation 

Standalone GDAL was installed to Puhti using [Spack and its GDAL package definition](https://spack.readthedocs.io/en/latest/package_list.html#gdal). For other installations, see respective application page.


## References

* [GDAL documentation, programs](https://gdal.org/programs/index.html)
* [GDAL tutorial by CSC](../support/tutorials/gis/gdal.md)
* [GDAL cheat sheet](https://github.com/dwtkns/gdal-cheat-sheet)
* [GDAL Linux examples](https://github.com/clhenrick/shell_scripts)

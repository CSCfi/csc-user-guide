# GDAL

[GDAL](https://gdal.org/) (Geospatial Data Abstraction Library) is a GIS translator library for accessing and transforming geospatial data. Most commonly it is used in file format or coordinate system changes. 

## Available

GDAL is available in Puhti with following versions:

* 3.2.1 via conda as Singularity container: [geoconda-3.8.8](geoconda.md)
* 3.2.0 as Singularity container: [r-env-singularity 4.0.2 - 4.0.5](r-env-for-gis.md)
* 3.0.4 via conda: [geoconda-3.8](geoconda.md), 
* 3.0.2 via conda: [geoconda-3.7](geoconda.md), 
* 3.0.1 stand-alone: gdal module,
* 2.4.3 via conda: [snap](snap.md)
* 2.4.2 as Singularity container: [r-env-singularity 3.6.3](r-env-for-gis.md)
* 2.4.2 via conda: [mapnik](mapnik.md)
* 2.4.1 via conda: [Orfeo ToolBox](otb.md)

!!! note
    The stand-alone versions don't have python bindings installed so e.g __gdal_calc__ works only in the conda installations. Also, the supported file formats vary slightly between the GDAL installations. For instance, the PostGIS driver is not available in gdal/3.0.1 but is included in the conda versions.

## Usage

### Using GDAL

GDAL is included in the modules listed above, so it can be used when any of these modules is loaded, or it can be loaded separately with:

`module load geoconda`

If you need to use a stand-alone version of GDAL or plan to build software on top of GDAL, you can load GDAL with

`module load gcc/9.1.0 gdal`

By default the latest gdal module is loaded. If you want a specific version you can specify the version number

`module load gcc/9.1.0 gdal/<VERSION>-omp`

You can test if GDAL loaded successfully with following

`gdalinfo --version`

With `r-env-singularity` gdal commands can be used as:

`singularity_wrapper exec gdalinfo --version`


### Using files directly from Allas

It is possible to __read__ files from Allas directly with GDAL, but not to write. For results, write them first to Puhti scratch and move later to Allas. The below mentioned virtual drivers are supported also in many GDAL-based tools. The set up is the same as below, but instead of the example gdalinfo command open the file from Python or R script. In R and Python it is possible also to write to Allas directly from script. We have tested successfully: 

 * [Python](geoconda.md): gdal, geopandas, fiona and rasterio. [Example](https://github.com/csc-training/geocomputing/blob/master/python/allas/working_with_allas_from_Python_S3.py). 
 * [R](r-env-for-gis.md): sf, raster. [Example](https://github.com/csc-training/geocomputing/blob/master/R/allas/working_with_allas_from_R_S3.R). 
 * [QGIS](qgis.md)

Reading data directly from Allas is slower than reading from scratch or other Puhti lustre disks, for example reading a ~500 Mb files from scratch takes ~1 second, but from Allas ~10 seconds. In most cases still comapered to full duration of an analysis in Puhti, these seconds are not important.

__Public files__ in Allas can be read with [`vsicurl`](https://gdal.org/user/virtual_file_systems.html#vsicurl):  
```
gdalinfo /vsicurl/https://a3s.fi/<name_of_your_bucket>/<name_of_your_file>
```

__Private files__ can be read by SWIFT or S3 API. SWIFT is more secure, but the credetials need to be updated after 8 hours. S3 has permanent keys, is therefore little bit easier to use, but less secure. Both of these have a random reading and streaming API.

__SWIFT.__ Set up the connection in Puhti and then read the files  with [`vsiswift`-driver](https://gdal.org/user/virtual_file_systems.html#vsiswift-openstack-swift-object-storage-random-reading):

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

## License and acknowledgement

GDAL is licensed under an [MIT/X style license](https://gdal.org/license.html)

Please acknowledge CSC and Geoportti in your publications, it is important for project continuation and funding reports.
As an example, you can write "The authors wish to thank CSC - IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (Geoportti, urn:nbn:fi:research-infras-2016072513) for computational resources and support".

## References

* [GDAL documentation, programs](https://gdal.org/programs/index.html)
* [GDAL tutorial by CSC](../support/tutorials/gis/gdal.md)
* [GDAL cheat sheet](https://github.com/dwtkns/gdal-cheat-sheet)
* [GDAL Linux examples](https://github.com/clhenrick/shell_scripts)

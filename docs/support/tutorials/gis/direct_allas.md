# Using files directly from Allas

[GDAL](../../../apps/gdal.md) and other GDAL-based tools can read and partly also write files directly from Allas and other external locations, which eliminates the need to download the files.

The GDAL command line tool can only __read__ files from external location, but not write. If you want to write files to Allas, you can still save them first to the supercomputer, virtual machine or own computer and move them to Allas later. In R and Python it is possible also to write to Allas directly from script. We have tested successfully:

 * [Python](../../../apps/geoconda.md): gdal, geopandas, fiona and rasterio. [Example](https://github.com/csc-training/geocomputing/blob/master/python/allas/working_with_allas_from_Python_S3.py). 
 * [R](../../../apps/r-env-for-gis.md): sf, raster. [Example](https://github.com/csc-training/geocomputing/blob/master/R/allas/working_with_allas_from_R_S3.R). 
 * [QGIS](../../../apps/qgis.md)

 
Reading data directly from Allas is slower than reading from local disks, for example reading a ~500 Mb files from your scratch directory on Puhti takes ~1 second, reading the same file from Allas takes ~10 seconds. In many cases, these seconds are negligable compared to the full duration of an analysis.

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

The export commands are needed because GDAL is looking for different environment variables than what allas-conf is writing. These commands need to be given each time you start working with Puhti, because the token is valid for 8 hours. Inside batchjobs use [allas-conf -k](../../../data/Allas/allas_batchjobs.md).

__S3.__ 
Set up the connection in Puhti and then read the files with [vsis3-driver](https://gdal.org/user/virtual_file_systems.html#vsis3-aws-s3-files-random-reading):
```
module load allas
allas-conf --mode s3cmd
gdalinfo /vsis3/<name_of_your_bucket>/<name_of_your_file>
```

* `module load allas` sets AWS_S3_ENDPOINT environment variable, which needs to be run each time S3 is used.
* `allas-conf` command saves your credentials in your home directory to .aws/credentials file. This needs to be run only once before first use or when you want to switch to another CSC project.

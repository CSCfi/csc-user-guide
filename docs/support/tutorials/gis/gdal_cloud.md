# Using geospatial files directly from cloud, inc Allas

[GDAL](../../../apps/gdal.md) is the main open-source libary for reading and writing geospatial data and many more advanced tools rely on GDAL, including QGIS, Python, R etc. GDAL on most tools depending on it can read directly from an URL or cloud storage services, which eliminates the need to download the files manually before data analysis. It can also write files to cloud storage services. Several cloud storage APIs are supported, inc CSC Allas, Amazon S3, Google Cloud Storage, Microsoft Azure etc. Reading data directly from an external service is usually slower than reading from local disks, but in many cases, these seconds are negligible compared to the full duration of an analysis.

GDAL has several virtual [network based files systems](https://gdal.org/user/virtual_file_systems.html#network-based-file-systems), that are meant for different storage services or use cases. CSC Allas supports both SWIFT or S3 API. SWIFT is more secure, but the credentials need to be updated after 8 hours. S3 has permanent keys, and is therefore little bit easier to use. Both of these have a random reading and streaming API. 

Below are described in more detail how to use GDAL with public files from URL (VSICURL), private files in S3 (VSIS3) or SWIFT (VSISWIFT) storage.

## VSICURL, reading public files from URL or cloud storage service

Without any extra settings always should work [VSICURL](https://gdal.org/user/virtual_file_systems.html#vsicurl), that can be used for reading of files available through HTTP/FTP web protocols. Public objects in object storag usually also have an URL, so this works also for public object storage files. VSICURL supports also partial reading of files, so it works well with cloud-optimized file formats. VSICURL supports also basic authentication. 

```
# A public file
gdalinfo /vsicurl/URL

# For example, from Paituli
gdalinfo /vsicurl/https://www.nic.funet.fi/index/geodata/mml/orto/normal_color_3067/mara_v_25000_50/2023/N33/02m/1/N3324F.jp2

# CSC Allas
gdalinfo /vsicurl/https://a3s.fi/bucket_name/object_name
gdalinfo /vsicurl/https://bucket_name.a3s.fi/object_name

# Amazon S3 (us-west-2)
gdalinfo /vsicurl/https://s3.us-west-2.amazonaws.com/bucket_name/object_name

#Depending on installation settings VSICURL may sometimes work also without the `/vsicurl/` before the URL.
gdalinfo URL

```

## VSIS3, reading and writing files from/to S3 services

[VSIS3](https://gdal.org/user/virtual_file_systems.html#vsis3-aws-s3-files) is suitable for working with S3 services, for example CSC Allas, LUMI-O and Amazon S3. 


### S3 settings

For accessing the data from S3 services are needed a few settings that can be given as environment variables or saved to `credentials` file. See the GDAL page for details.
  
#### Allas S3 settings with CSC supercomputers
Setting up Allas S3 connection is easiest with CSC supercomputers.

CSC supercomputers have [`allas-conf` command for setting up Allas connection](https://docs.csc.fi/data/Allas/using_allas/s3_client/#configuring-s3-connection-in-supercomputers) in the `allas` module.: 

```
module load allas
allas-conf --mode s3cmd
```

* `module load allas` sets AWS_S3_ENDPOINT environment variable, which needs to be run each time S3 is used.
* `allas-conf --mode s3cmd` must be run only when first setting up the connection or if starting to work with different CSC project.

#### Allas S3 settings in general

If you are using also CSC supercomputers, then the easiest is to set up S3 connection on a supercomputer and then:

1) Copy your `~/.aws/credentials file from supercomputer to the other machine, `C:\Users\username\.aws\credentials` on Windows or `~/.aws/credentials` on Mac or Linux. 
2) Set also AWS_S3_ENDPOINT environment variable to `a3s.fi`. Windows command shell: `set AWS_S3_ENDPOINT=a3s.fi` or Linux/Max: `export AWS_S3_ENDPOINT=a3s.fi`

If you are not using also CSC supercomputers, you can install `allas-conf` to your Linux/Max machine, follow the instructions in [CSC's Allas command line interface utilities repository](https://github.com/CSCfi/allas-cli-utils). 

### Using S3 

```
# Reading data
gdalinfo /vsis3/<name_of_your_bucket>/<name_of_your_file>

# Writing data
export CPL_VSIL_USE_TEMP_FILE_FOR_RANDOM_WRITE=YES
gdal_translate /vsis3/<name_of_your_bucket>/<name_of_your_input_file> /vsis3/<name_of_your_bucket>/<name_of_your_output_file> -of COG


## VSISWIFT, reading and writing files from/to SWIFT services

[VSISWIFT](https://gdal.org/user/virtual_file_systems.html#vsiswift-openstack-swift-object-storage) is suitable for working with SWIFT services, for example CSC Allas. For setting up the connection in Puhti or Mahti supercomputer:

```
module load allas
allas-conf
export SWIFT_AUTH_TOKEN=$OS_AUTH_TOKEN 
export SWIFT_STORAGE_URL=$OS_STORAGE_URL
gdalinfo /vsiswift/<name_of_your_bucket>/<name_of_your_file>
```

The export commands are needed because GDAL is looking for different environment variables than what allas-conf is writing. These commands need to be given each time you start working with Puhti, because the token is valid for 8 hours. Inside batchjobs use [allas-conf -k](../../../data/Allas/allas_batchjobs.md).


## Other tools
In CSC geocomputing examples Github repo are provided also example for working with Allas from R and Python.
 * [Python](../../../apps/geoconda.md): gdal, geopandas, fiona and rasterio. [Example codes on CSCs github repository](https://github.com/csc-training/geocomputing/blob/master/python/allas/working_with_allas_from_Python_S3.py). 
 * [R](../../../apps/r-env-for-gis.md): sf, raster. [Example codes on CSCs github repository](https://github.com/csc-training/geocomputing/blob/master/R/allas/working_with_allas_from_R_S3.R). 

All examples above show usage with `GDAL`, however the links to the data and configuration of the connection are the same, no matter if you use the links with `GDAL`, `Python`, `R` or `QGIS`. 
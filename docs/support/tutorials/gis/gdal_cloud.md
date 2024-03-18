# Using geospatial files directly from public repositories and S3 storage services, inc Allas

[GDAL](https://gdal.org/) is the main open-source library for reading and writing geospatial data and many more advanced tools rely on GDAL, including QGIS, ArcGIS, Python, R etc. GDAL has several virtual [network based files systems](https://gdal.org/user/virtual_file_systems.html#network-based-file-systems), that are meant for different APIs or use cases. GDAL and most tools depending on it can **read** directly from an public URL or S3 storage services. This eliminates the need to download the files manually before data analysis. GDAL can also **write** files to S3 storage services, but only some tools dependent on GDAL are supporting it. 

Reading data directly from an external service is usually slower than reading from local disks, but in many cases, these seconds are negligible compared to the full duration of an analysis, but it is important to have good Internet connection.

S3 services are very common for storing bigger amounts of data, for example:

* CSC [Allas](../../../data/Allas/index.md),
* EuroHPC [LUMI-O](https://docs.lumi-supercomputer.eu/storage/lumio/),
* ESA [Copernicus Data Space Ecosystem S3](https://documentation.dataspace.copernicus.eu/APIs/S3.html),
* Amazon [S3](https://aws.amazon.com/pm/serv-s3/),
* Google [Cloud Storage](https://cloud.google.com/storage),
* Microsoft [Azure Blob Storage](https://azure.microsoft.com/en-us/products/storage/blobs/) etc. 

More details on how to use GDAL with public files from URL (VSICURL) and private files in S3 (VSIS3) storage are given below. Special attention is on CSC Allas object storage service and supercomputers. For using GDAL on a supercomputer, a module including [GDAL](../../../apps/gdal.md), must be activated.

## Reading public files from URL

[VSICURL](https://gdal.org/user/virtual_file_systems.html#vsicurl) can be used for reading files available via URL. Public objects in S3 storage usually also have an URL, so this works also for public S3 files. VSICURL also supports partial reading of files, so it works well with cloud-optimized file formats. VSICURL also supports basic authentication. 

```
# A public file
gdalinfo /vsicurl/URL

# For example, from Paituli
gdalinfo /vsicurl/https://www.nic.funet.fi/index/geodata/mml/orto/normal_color_3067/mara_v_25000_50/2023/N33/02m/1/N3324F.jp2

# CSC Allas
gdalinfo /vsicurl/https://a3s.fi/bucket_name/object_name
# OR alternatively
gdalinfo /vsicurl/https://bucket_name.a3s.fi/object_name

# Amazon S3 (us-west-2)
gdalinfo /vsicurl/https://s3.us-west-2.amazonaws.com/bucket_name/object_name

#Depending on GDAL installation settings VSICURL may sometimes work also without the `/vsicurl/` before the URL.
gdalinfo URL
```

## Reading and writing files from/to S3 services

GDAL's [VSIS3](https://gdal.org/user/virtual_file_systems.html#vsis3-aws-s3-files) is for working with S3 services. 


### S3 connection details

For accessing the data from S3 services, first the connection details must be set correctly. Usually the following connection details are needed:

* end-point URL
* region
* access and secret key

Each service's user guide should specify the end-point and region and give instructions how to find the keys. It is recommended to save the keys and region name to `credentials` file, located in `C:\Users\username\.aws\credentials` on Windows or `~/.aws/credentials` on Mac or Linux. For example the Allas the credentials file could look like this:

```
[allas_project1]
AWS_ACCESS_KEY_ID=xxx
AWS_SECRET_ACCESS_KEY=yyy
AWS_DEFAULT_REGION=regionOne
```

The end-point URL is not needed for Amazon S3, but is needed for other services. Unfortunately it can not be given via `credentials` file, but needs to be given to GDAL as environment variable. For example to set Allas end-point: Windows command shell: `set AWS_S3_ENDPOINT=a3s.fi` or Linux/Max: `export AWS_S3_ENDPOINT=a3s.fi`

#### S3 connection set up for Allas 

On CSC supercomputers the easiest option to set up Allas connection details is to use [allas-conf command](../../../data/Allas/using_allas/s3_client.md#configuring-s3-connection-in-supercomputers):

```
module load allas
allas-conf --mode s3cmd
```

* `module load allas` sets AWS_S3_ENDPOINT environment variable, which needs to be run each time S3 is used.
* `allas-conf --mode s3cmd` writes the keys and region name to `credentials` file (also prints them to Terminal) and must be run only when using first time or when changing the CSC project.

After this, you are ready to use GDAL or GDAL-based tools on supercomputers.

If you want to use Allas on some other machine, then copy `~/.aws/credentials` file from supercomputer to the other machine and set `AWS_S3_ENDPOINT` as described above.

If you are not using CSC supercomputers, you can install `allas-conf` to your Linux/Mac machine, follow the instructions in [CSC's Allas command line interface utilities repository](https://github.com/CSCfi/allas-cli-utils). 

#### S3 connection set up for Copernicus Data Space Ecosystem (CDSE)

ESA data, inc Sentinel data, is available via [CDSE S3](https://dataspace.copernicus.eu/). Get [CDSE S3 credentials](https://documentation.dataspace.copernicus.eu/APIs/S3.html) and save to the `credentials` file as described above. With CDSE `AWS_VIRTUAL_HOSTING` should be set to False:
```
export AWS_S3_ENDPOINT=eodata.dataspace.copernicus.eu
export AWS_VIRTUAL_HOSTING=FALSE
```

#### Several connection profiles
When working with several CSC projects or different S3 storages, it is possible to have several profiles in the `credentials` file:

```
[allas_project1]
AWS_ACCESS_KEY_ID=xxx
AWS_SECRET_ACCESS_KEY=yyy
AWS_DEFAULT_REGION = regionOne

[esa_cdse]
AWS_ACCESS_KEY_ID=xxx
AWS_SECRET_ACCESS_KEY=yyy
```

Then before using GDAL, the currently used profile must be set as environment variable: `export AWS_PROFILE=allas_project1`

### Using S3 

```
# Reading data
gdalinfo /vsis3/<name_of_your_bucket>/<name_of_your_file>

# Writing data
export CPL_VSIL_USE_TEMP_FILE_FOR_RANDOM_WRITE=YES
gdal_translate /vsis3/<name_of_your_bucket>/<name_of_your_input_file> /vsis3/<name_of_your_bucket>/<name_of_your_output_file> -of COG
```


## GDAL-based tools

 * [ArcGIS Pro, connect to cloud storage](https://pro.arcgis.com/en/pro-app/latest/help/projects/connect-to-cloud-stores.htm). Only for rasters and reading.
	* ArcGIS Pro asks for all connection details while setting up Cloud storage connection, so the `credential` file or environment variables are not needed.
 * QGIS:
 	* Both raster and vector [data adding dialogs](https://docs.qgis.org/3.28/en/docs/user_manual/managing_data_source/opening_data.html#loading-a-layer-from-a-file) have options to add data from URL (HTTPS) or S3. Only reading.
	* For S3 keys add the `credentials` file as described above, or use the environment variables.
	* QGIS connects by default to Amazon S3, for connecting to some other service add to Settings -> Options -> Variables new variable with name AWS_S3_ENDPOINT, for Allas the value is `a3s.fi`.
 	* QGIS supports also point clouds from URL. 
 * [Example Python code for working with Allas, rasterio, geopandas, and boto3](https://github.com/csc-training/geocomputing/blob/master/python/allas). 
 * [Example R code for workign with Allas, terra, sf, and aws.s3](https://github.com/csc-training/geocomputing/blob/master/R/allas/working_with_allas_from_R_S3.R). 

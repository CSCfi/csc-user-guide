# Using files directly from Allas

[GDAL](../../../apps/gdal.md) and other GDAL-based tools can read and partly also write files directly from Allas and other external locations, which eliminates the need to download the files.

The GDAL command line tool can only __read__ files from external location, but not write. If you want to write files to Allas, you can still save them first to the supercomputer, virtual machine or own computer and move them to Allas later. In R and Python it is possible also to __write__ to Allas directly from script. We have tested successfully:

 * [Python](../../../apps/geoconda.md): gdal, geopandas, fiona and rasterio. [Example](https://github.com/csc-training/geocomputing/blob/master/python/allas/working_with_allas_from_Python_S3.py). 
 * [R](../../../apps/r-env-for-gis.md): sf, raster. [Example](https://github.com/csc-training/geocomputing/blob/master/R/allas/working_with_allas_from_R_S3.R). 
 * [QGIS](../../../apps/qgis.md)

 
Reading data directly from an external service, like Allas or other object storage is slower than reading from local disks, for example reading a ~500 Mb files from your scratch directory on Puhti takes ~1 second, reading the same file from Allas takes ~10 seconds. In many cases, these seconds are negligible compared to the full duration of an analysis.

## Public files

__Public files__ in Allas or other object storage can be read with [`vsicurl`](https://gdal.org/user/virtual_file_systems.html#vsicurl):  

### Allas
```
gdalinfo /vsicurl/https://a3s.fi/<name_of_your_bucket>/<name_of_your_file>
```
### Other object storage
```
gdalinfo /vsicurl/https://<baseurl_of_service>/<name_of_your_bucket>/<name_of_your_file>
```
For example, for public Google cloud, the base URL is `storage.googleapis.com`, see also [Google cloud access documentation](https://cloud.google.com/storage/docs/access-public-data#api-link).

### Private files

You may also want to access private files on Allas or other cloud storage. For this we need to not only provide the URL to the data, but also credentials for accessing the data. 

__Private files__ can be read by SWIFT or S3 API. SWIFT is more secure, but the credentials need to be updated after 8 hours. S3 has permanent keys, and is therefore little bit easier to use. Both of these have a random reading and streaming API.

You can set up the connection to Allas by using `allas-conf` tools which on the CSC supercomputers is provided in the `allas` module. For other Linux computing environments `allas-conf` can be installed by following the instruction in  [CSCs Allas command line interface utilities repository](https://github.com/CSCfi/allas-cli-utils). 
The `allas-conf` command saves your credentials in your home directory to .aws/credentials file from where it can be read by other tools.

#### Access from supercomputer to Allas private files

On the CSC supercomputers, `allas-conf` tool is provided in `allas` module.  

##### Using S3

Set up the connection by loading the allas module and configure the connection; then read the files with [`vsis3` driver](https://gdal.org/user/virtual_file_systems.html#vsis3-aws-s3-files-random-reading):
```
module load allas
allas-conf --mode s3cmd
gdalinfo /vsis3/<name_of_your_bucket>/<name_of_your_file>
```

* `module load allas` sets AWS_S3_ENDPOINT environment variable, which needs to be run each time S3 is used.

##### Using SWIFT

Set up the connection in Puhti and then read the files with [`vsiswift` driver](https://gdal.org/user/virtual_file_systems.html#vsiswift-openstack-swift-object-storage-random-reading):

```
module load allas
allas-conf
export SWIFT_AUTH_TOKEN=$OS_AUTH_TOKEN 
export SWIFT_STORAGE_URL=$OS_STORAGE_URL
gdalinfo /vsiswift/<name_of_your_bucket>/<name_of_your_file>
```

The export commands are needed because GDAL is looking for different environment variables than what allas-conf is writing. These commands need to be given each time you start working with Puhti, because the token is valid for 8 hours. Inside batchjobs use [allas-conf -k](../../../data/Allas/allas_batchjobs.md).

#### Access from any Linux computing environment to Allas private files

Follow the instructions provided in [CSCs Allas command line interface utilities repository](https://github.com/CSCfi/allas-cli-utils) to configure the connection from your computing environment to Allas and then follow the same commands as above (excluding `module load allas`, note also slightly adjusted `allas-conf` command in allas-cli-utils instructions).

#### Access from any Linux computing environment to external cloud storage private files

You will need to manually make your cloud storage credentials available to the tools you want to use, e.g. by adding them to the `.aws/credentials` file. Check your cloud storage providers manuals and [GDAL virtual file systems documentation](https://gdal.org/user/virtual_file_systems.html#).






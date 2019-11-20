# GDAL

[GDAL](https://gdal.org/) (Geospatial Data Abstraction Library) is a GIS translator library for accessing and transforming geospatial data. Most commonly it is used in file format or coordinate system changes. 

## Available

The `gdal` module is available in Puhti with following versions:

* 2.4.2 via conda
* 3.0.1 stand-alone
* 2.4.2 stand-alone

(If you think that some important GDAL version is missing from here, you can ask for installation from servicedesk@csc.fi.)

## Usage

### Using gdal

GDAL is included in the [geoconda](../apps/geoconda.md) module and can be loaded with

`module load geoconda`

If you need to use a stand-alone version of gdal or plan to build software on top of gdal, you can load gdal with

`module load gcc/9.1.0 gdal`

By default the latest gdal module is loaded. If you want a specific version you can specify the version number

`module load gcc/9.1.0 gdal/<VERSION>-omp`

You can test if gdal loaded successfully with following

`gdalinfo --version`



!!! note
    The stand-alone versions don't have python bindings installed so e.g __gdal_calc__ works only in the geoconda installation. Also, the supported file formats vary slightly between the gdal installations. For instance, the PostGIS driver is not yet available in gdal/3.0.1 but is included in the others

## Using files directly from Allas

It is possible to __read__ files from Allas directly with GDAL, but not to write.
The below mentioned virtual drivers are supported also in many GDAL-based tools. The set up is the same as below, but instead of the example gdalinfo command open the file from Python or R script. We have tested successfully: 
* Python: gdal, geopandas, fiona and rasterio 
* R: sf, raster

For results, write them first to Puhti scratch and move later to Allas. 

__Public files__ in Allas can be read with [`vsicurl`](https://gdal.org/user/virtual_file_systems.html#vsicurl):  
```
gdalinfo /vsicurl/https://a3s.fi/<name_of_your_bucket>/<name_of_your_file>
```

__Private files__ can be read by SWIFT or S3 API. SWIFT is more secure, but the credetials need to be updated after 8 hours. S3 has permanent keys, is therefore little bit easier to use, but less secure. Both of these have a random reading and streaming API.

__SWIFT.__ Set up the connection in Puhti or Taito and then read the files  with [`vsiswift`-driver](https://gdal.org/user/virtual_file_systems.html#vsiswift-openstack-swift-object-storage-random-reading):

```
module load allas
allas-conf
export SWIFT_AUTH_TOKEN=$OS_AUTH_TOKEN 
export SWIFT_STORAGE_URL=$OS_STORAGE_URL
gdalinfo /vsiswift/<name_of_your_bucket>/<name_of_your_file>
```

The export commands are needed because GDAL is looking for different environment variables than what allas-conf is writing. These commands need to be given each time you start working with Puhti, because the token is valid for 8 hours. Inside batchjobs use [allas-conf -k](../data/Allas/allas_batchjobs.md).

__S3.__ 
Create your S3 credentials with allas-conf in Puhti or Taito.
```
module load allas
allas-conf --mode s3cmd
```
Save your credentials in your home directory to .aws/credentials file like this:
```
[default]
AWS_ACCESS_KEY_ID=<access_key>
AWS_SECRET_ACCESS_KEY=<secret_key>
```
These steps you have to do only once.

Set the service endpoint for Allas and read the file using [vsis3-driver](https://gdal.org/user/virtual_file_systems.html#vsis3-aws-s3-files-random-reading):
```
export AWS_S3_ENDPOINT=a3s.fi
gdalinfo /vsis3/<name_of_your_bucket>/<name_of_your_file>
```

## License and citing

GDAL/OGR is licensed under an [MIT/X style license](https://gdal.org/license.html)

In your publications please acknowledge also oGIIR and CSC, for example “The authors wish to acknowledge for computational resources CSC – IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (oGIIR, urn:nbn:fi:research-infras-2016072513).”

### References

* [GDAL tutorials](https://gdal.org/tutorials/index.html)
* [GDAL Github](https://github.com/OSGeo/GDAL)
* [GDAL commands](https://gdal.org/programs/index.html)

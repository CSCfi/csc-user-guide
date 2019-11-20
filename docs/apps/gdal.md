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

It is possible to read files from Allas directly with GDAL, but not to write.

__Public files__ in Allas can be read with `vsicurl`:  
```
gdalinfo /vsicurl/https://a3s.fi/swift/v1/AUTH_9da5d87785e2440b95d52f31392a3973/gis-open/T34VFM_20180829T100019_clipped_scaled_1_2.tif
```

* The first part of URL you can see at least in the Allas web interface, next to the check-box where the bucket is made public.
* gis-open is the name of the bucket
* T34VFM_20180829T100019_clipped_scaled_1_2.tif is the name of the file.

For __private files__ you first have to set up the connection in Puhti or Taito and then the files is read with `vsiswift`:

```
module load allas
allas-conf
export SWIFT_AUTH_TOKEN=$OS_AUTH_TOKEN 
export SWIFT_STORAGE_URL=$OS_STORAGE_URL
gdalinfo /vsiswift/<name_of_your_bucket>/<name_of_your_file>
```

The export commands are needed because GDAL is looking for different environment variables than what allas-conf is writing.

## License and citing

GDAL/OGR is licensed under an [MIT/X style license](https://gdal.org/license.html)

In your publications please acknowledge also oGIIR and CSC, for example “The authors wish to acknowledge for computational resources CSC – IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (oGIIR, urn:nbn:fi:research-infras-2016072513).”

### References

* [GDAL tutorials](https://gdal.org/tutorials/index.html)
* [GDAL Github](https://github.com/OSGeo/GDAL)
* [GDAL commands](https://gdal.org/programs/index.html)

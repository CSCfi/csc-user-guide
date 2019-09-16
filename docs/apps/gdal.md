# GDAL

[GDAL](https://gdal.org/) (Geospatial Data Abstraction Library) is a GIS translator library for accessing and transforming geospatial data. Most commonly it is used in file format or coordinate system changes. 

## Available

The `gdal` module is available in Puhti with following versions:

* 3.0.1 
* 2.4.2
* 2.4.2 via conda

(If you think that some important GDAL version is missing from here, you can ask for installation from servicedesk@csc.fi.)

## Usage

### Using gdal

The gdal module can be loaded with 

`module load gcc/9.1.0 gdal`

By default the latest gdal module is loaded. If you want a specific version you can specify the version number

`module load gcc/9.1.0 gdal/[VERSION]-omp`

Or if you want to utilize gdal from a conda environment you can load the [geoconda](../#apps/geoconda/) module

`module load geoconda`

If you plan to work also with python or other GIS libraries, the conda environment is probably the best option

You can test if gdal loaded succesfully with following

`gdalinfo --version`

!!! note
    The supported file formats vary slightly between the gdal installations. For instance, the PostGIS driver is not yet available in gdal/3.0.1

## License and citing

All packages are licensed under various free and open source licenses (FOSS), see the linked pages above for exact details.
In your publications please acknowledge also oGIIR and CSC, for example “The authors wish to acknowledge for computational resources CSC – IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (oGIIR, urn:nbn:fi:research-infras-2016072513).”

### References

* [GDAL tutorials](https://gdal.org/tutorials/index.html)
* [GDAL Github](https://github.com/OSGeo/GDAL)
* [GDAL commands](https://gdal.org/programs/index.html)

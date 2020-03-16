# FORCE 

FORCE (Framework for Operational Radiometric Correction for Environmental monitoring) is an all-in-one solution for mass-processing medium-resolution satellite images

## Available

__FORCE__ is available in Puhti with the following versions:

* 3.0
* 2.1

## Usage

FORCE is included in the __force__ module. The __parallel__ (gnu-parallel) module needs to be loaded also. You can load these with

`module load parallel force`

By default the latest __force__ module is loaded. If you want a specific version you can specify the version number

`module load parallel force/<VERSION_NUMBER>`

## Using FORCE

FORCE is used with command line commands. All available commands can be viewed by running 

`force`

Here is an example that finds suitable satellite images from an area and time with cloud coverage of 10%. More information on Sentinel imagery download can be found from the [FORCE documentation](https://force-eo.readthedocs.io/en/latest/components/lower-level/level1/level1-sentinel2.html#level1-sentinel2).

`force-level1-sentinel2 /scratch/<PROJECT>/data/sentinel_images/ /scratch/<PROJECT>/data/sentinel_images/files.txt "60.15/24.77,60.25/24.77,60.25/25.04,60.15/25.04,60.15/24.77" 2020-03-01 2020-03-08 0 10 dry`

## Using FORCE to download sentinel images

For downloading files with FORCE you need __ESA Scihub__ or __FMI Finhub__ credentials. FMI Finhub includes only 1C level data for Baltic sea drainage area, but should be faster than ESA Scihub. The credentials should be saved in your __home directory__, the ESA Scihub credentials to __.scihub__ file and FMI Finhub credential to __.finhub__ file. Username in the first row, password second.

The download scripts have been slightly modified for the CSC environment. For ESA Scihub use __force-level1-sentinel2__ command and for FMI Finhub __force-level1-sentinel2-fh__. Both scripts follow the syntax in the user guide, see Pekka Hurskainen's presentation for examples.

## License and citing

FORCE is licensed under [the GNU GPL License](https://github.com/davidfrantz/force/blob/master/LICENSE))

In your publications please acknowledge also oGIIR and CSC, for example “The authors wish to acknowledge for computational resources CSC – IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (oGIIR, urn:nbn:fi:research-infras-2016072513).”

### References

* [FORCE github](https://github.com/davidfrantz/force)
* [FORCE documentation](https://force-eo.readthedocs.io/en/latest/)
* [FORCE tutorials](https://davidfrantz.github.io/#tutorials)
* [FORCE google grouo](https://groups.google.com/d/forum/force_eo)

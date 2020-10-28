# FORCE 

FORCE (Framework for Operational Radiometric Correction for Environmental monitoring) is an all-in-one solution for mass-processing medium-resolution satellite images

## Available

__FORCE__ is available in Puhti with the following versions:

* 3.5.1 (Singularity container)

## Usage 

FORCE is included in the __force__ module. You can load it with 

`module load force`

By default the latest __force__ module is loaded. If you want a specific version you can specify the version number

`module load force/<VERSION_NUMBER>`

## Running FORCE commands

FORCE is installed as a container. This means you need to use singularity_wrapper to run its commands

`singularity_wrapper exec <normal FORCE command>`

If working interactively, you can also start a shell inside the container with

`singularity_wrapper shell`

and after that use normal FORCE commands

We have an example of running L1 to L2 pipeline for Sentinel images in [our Github examples](https://github.com/csc-training/geocomputing/tree/master/force)

## Using FORCE to download sentinel images

For downloading files with FORCE you need __ESA Scihub__ credentials. The credentials should be saved in your __home directory__ to a __.scihub__ file and. Username in the first row, password second.

Here is an example that finds suitable satellite images from an area and time with cloud coverage of 10% and downloads them. More information on Sentinel imagery download can be found from the [FORCE documentation](https://force-eo.readthedocs.io/en/latest/components/lower-level/level1/level1-sentinel2.html#level1-sentinel2).

`singularity_wrapper exec force-level1-sentinel2 /scratch/<PROJECT>/sentinel_images/ /scratch/<PROJECT>/sentinel_images/files.txt "60.15/24.77,60.25/24.77,60.25/25.04,60.15/25.04,60.15/24.77" 2020-03-01 2020-03-08 0 10`

## License and citing

FORCE is licensed under [the GNU GPL License](https://github.com/davidfrantz/force/blob/master/LICENSE))

In your publications please acknowledge also oGIIR and CSC, for example “The authors wish to acknowledge for computational resources CSC – IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (oGIIR, urn:nbn:fi:research-infras-2016072513).”

### References

* [CSC Example](https://github.com/csc-training/geocomputing/tree/master/force)
* [FORCE github](https://github.com/davidfrantz/force)
* [FORCE documentation](https://force-eo.readthedocs.io/en/latest/)
* [FORCE tutorials](https://davidfrantz.github.io/#tutorials)
* [FORCE google group](https://groups.google.com/d/forum/force_eo)
* [FORCE v2.0 (Old) User manual](https://www.uni-trier.de/fileadmin/fb6/prof/FER/Downloads/Software/FORCE/FORCE-user-guide-v-2-0.pdf)
* [Using FORCE v2.0 (Old) in CSC environment (Taito) by Pekka Hurskainen](https://research.csc.fi/documents/48467/73370/Satellite_time_series_processing_with_FORCE_in_CSC_Hurskainen.pdf/c6960f88-ec94-4c94-aca3-734c8d283268)

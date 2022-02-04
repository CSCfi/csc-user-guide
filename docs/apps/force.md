# FORCE 

FORCE (Framework for Operational Radiometric Correction for Environmental monitoring) is an all-in-one solution for mass-processing medium-resolution satellite images

## Available

__FORCE__ is available in Puhti with the following versions:

* 3.6.5 (Singularity container)

## Usage 

FORCE is included in the __force__ module. You can load it with 

`module load force`

By default the latest __force__ module is loaded. If you want a specific version you can specify the version number

`module load force/<VERSION_NUMBER>`

## Running FORCE commands

FORCE is installed as a container, but it has wrappers for all FORCE commands, so it can be used normally. 

If working interactively, you can also start a shell inside the container with

`_debug_shell`

We have an example of running L1 to L2 pipeline for Sentinel images in [our Github examples](https://github.com/csc-training/geocomputing/tree/master/force)

## License and acknowledgement

FORCE is licensed under [the GNU GPL License](https://github.com/davidfrantz/force/blob/master/LICENSE))

Please acknowledge CSC and Geoportti in your publications, it is important for project continuation and funding reports.
As an example, you can write "The authors wish to thank CSC - IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (Geoportti, urn:nbn:fi:research-infras-2016072513) for computational resources and support".

### References

* [CSC Example](https://github.com/csc-training/geocomputing/tree/master/force)
* [FORCE github](https://github.com/davidfrantz/force)
* [FORCE documentation](https://force-eo.readthedocs.io/en/latest/)
* [FORCE tutorials](https://davidfrantz.github.io/#tutorials)
* [FORCE google group](https://groups.google.com/d/forum/force_eo)
* [FORCE v2.0 (Old) User manual](https://www.uni-trier.de/fileadmin/fb6/prof/FER/Downloads/Software/FORCE/FORCE-user-guide-v-2-0.pdf)
* [Using FORCE v2.0 (Old) in CSC environment (Taito) by Pekka Hurskainen](https://research.csc.fi/documents/48467/73370/Satellite_time_series_processing_with_FORCE_in_CSC_Hurskainen.pdf/c6960f88-ec94-4c94-aca3-734c8d283268)

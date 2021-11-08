# SAGA GIS

[Saga GIS](http://www.saga-gis.org/) (System for Automated Geoscientific Analyses) is a GIS application for spatial data editing and GIS analyses. It can be used with a graphical user interface, command line tools or through the R package `Rsagacmd` or `RSAGA`. Since the `RSAGA` package is no longer actively maintained and has not been tested on newer SAGA GIS versions, we recommend using `Rsagacmd` with SAGA GIS 7.9.0.

## Available

__SAGA GIS__ is available in Puhti with following versions:

* 7.10.0 in `r-env-singularity/4.0.4` module
* 7.9.0 in `r-env-singularity/4.0.2`, `r-env-singularity/4.0.3` and `r-env-singularity/4.0.5` modules
* 7.3.0 in `r-env-singularity/3.6.3` module
* 7.2.0 in `saga-gis` module

## Usage 

### Using SAGA GIS in Puhti web interface

This is the new recommended way.

1. Log in to [Puhti web interface](https://puhti.csc.fi). [Puhti web interface documentation](../computing/webinterface/desktop.md).
2. Start SAGA GIS with Apps -> Desktop, choose Desktop: 'None' and App: 'SAGA GIS'.

### Alternative (old) use of QGIS with NoMachine

With r-env-singularity module

SAGA GIS is installed in the general R module in Puhti. It is a Singularity container which means the commands are slightly different compared to old installations.

Before running anything, you should first start an [interactive session](../computing/running/interactive-usage.md) on a computing node and load `r-env-singularity ` module.

```
sinteractive -i
module load r-env-singularity 
```

You can test that SAGA GIS loaded successfully and print the command line tools help information with

```
singularity_wrapper exec saga_cmd -h
```

If you have connected with [NoMachine](nomachine.md) or have X11 enabled on your SSH connection, you can launch a graphical user interface with

```
singularity_wrapper exec saga_gui
```

For more information on running R jobs on Puhti, please see the [`r-env-singularity` documentation](r-env-singularity.md).

## Usage with old saga-gis module

Same commands for older SAGA GIS 7.2.0 version

```
sinteractive -i
module load gcc/9.1.0 saga-gis
saga_cmd -h
saga_gui
```

## License and citing

SAGA GIS is published under the [GPL](http://www.gnu.org/licenses/gpl.html) license. 

In your publications please acknowledge also oGIIR and CSC, for example “The authors wish to acknowledge for computational resources CSC – IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (oGIIR, urn:nbn:fi:research-infras-2016072513).”

### References

* [SAGA GIS homepage](http://saga-gis.sourceforge.net/en/)
* [SAGA GIS page on Sourceforge](https://sourceforge.net/projects/saga-gis/)
* [SAGA GIS tutorials](https://sagatutorials.wordpress.com/)
* [SAGA GIS tutorials on Sourceforge](https://sourceforge.net/p/saga-gis/wiki/Tutorials/)

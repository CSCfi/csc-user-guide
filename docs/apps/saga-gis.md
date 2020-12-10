# SAGA GIS

[Saga GIS](http://www.saga-gis.org/) (System for Automated Geoscientific Analyses) is a GIS application for spatial data editing and GIS analyses. It can be used with a graphical user interface, command line tools or through the R package RSAGA. 

## Available

__SAGA GIS__ is available in Puhti with following versions:

* 7.2.0 (`saga-gis` module)
* 7.3.0 (`r-env-singularity/3.6.3` module)
* 7.9.0 (`r-env-singularity/4.0.2` module)

## Usage with `saga-gis` module

The `saga-gis` module can be loaded with:

`module load gcc/9.1.0 saga-gis`

You can test that SAGA GIS loaded successfully and print the command line tools help information with:

`saga_cmd -h`

If you have connected with NoMachine or have X11 enabled on your SSH connection, you can launch a graphical user interface with:

`saga_gui`

!!! note
   We recommend using [NoMachine](nomachine.md) and [an interactive batch job](../computing/running/interactive-usage.md) for launching graphical user interfaces on Puhti.

## Usage with `r-env-singularity`

You can utilize SAGA GIS functions through the `Rsagacmd` and `RSAGA` R packages included in the `r-env-singularity` module.  You can load it with:

``` bash
module load r-env-singularity 
```

For more information on running R jobs on Puhti, please see the [`r-env-singularity` documentation](r-env-singularity.md).

!!! note
   Since the `RSAGA` package is no longer actively maintained and has not been tested on newer SAGA GIS versions, we recommend using `Rsagacmd` with SAGA GIS 7.9.0. 

## License and citing

SAGA GIS is published under the [GPL](http://www.gnu.org/licenses/gpl.html) license. For more information, [see here.](http://saga-gis.sourceforge.net/en/)

In your publications please acknowledge also oGIIR and CSC, for example “The authors wish to acknowledge for computational resources CSC – IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (oGIIR, urn:nbn:fi:research-infras-2016072513).”

### References

* [SAGA GIS homepage](http://saga-gis.sourceforge.net/en/)
* [SAGA GIS page on Sourceforge](https://sourceforge.net/projects/saga-gis/)
* [SAGA GIS tutorials](https://sagatutorials.wordpress.com/)
* [SAGA GIS tutorials on Sourceforge](https://sourceforge.net/p/saga-gis/wiki/Tutorials/)

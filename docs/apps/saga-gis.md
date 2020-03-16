# SAGA GIS

[Saga GIS](http://www.saga-gis.org/)(System for Automated Geoscientific Analyses) is a GIS application for spatial data editing and GIS analyses. It can be used with a graphical user interface, command line tools or through the R package RSAGA. 

## Available

__SAGA GIS__ is available in Puhti with following versions:

* 7.2.0

## Usage

SAGA GIS is included in the __saga-gis__ module and can be loaded with

`module load gcc/9.1.0 saga-gis`

You can test that the program loaded successfully and print the command line tools help information with

`saga_cmd -h`

If you have connected with a ssh connection that has __X11 forwarding__ enabled, you can launch a graphical user interface with

`saga_gui`

For __X11 forwarding__ to be enabled you need to install a suitable program
for your own computer first (unless you are using Linux or Mac). You can read
instructions how to do that
[here](../computing/connecting.md#using-graphical-applications)

!!! note
    Do not run long CPU intensive jobs on the login nodes! This means you can't run computationally intensive analysis on graphical user interfaces on Puhti until interactive Puhti-shells are made available later in 2019. Use the batch job system on Puhti or run analysis on taito-shell.

## Usage with R

You can also utilize SAGA GIS functions through the RSAGA R library that is included in the r-env module. You can load it with

`module load r-env`

## License and citing

SAGA GIS is published under the [GPL](http://www.gnu.org/licenses/gpl.html) license. More information [here](http://saga-gis.sourceforge.net/en/)

In your publications please acknowledge also oGIIR and CSC, for example “The authors wish to acknowledge for computational resources CSC – IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (oGIIR, urn:nbn:fi:research-infras-2016072513).”

### References

* [SAGA GIS homepage](http://saga-gis.sourceforge.net/en/)
* [SAGA GIS page on Sourceforge](https://sourceforge.net/projects/saga-gis/)
* [SAGA GIS tutorials](https://sagatutorials.wordpress.com/)
* [SAGA GIS tutorials on Sourceforge](https://sourceforge.net/p/saga-gis/wiki/Tutorials/)



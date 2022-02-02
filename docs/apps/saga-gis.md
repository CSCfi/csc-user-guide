# SAGA GIS

[Saga GIS](http://www.saga-gis.org/) (System for Automated Geoscientific Analyses) is a GIS application for spatial data editing and GIS analyses. It can be used with a graphical user interface, command line tools or through the R package `Rsagacmd` or `RSAGA`. Since the `RSAGA` package is no longer actively maintained and has not been tested on newer SAGA GIS versions, we recommend using `Rsagacmd` with SAGA GIS 7.9.0 and higher.

## Available

__SAGA GIS__ is available in Puhti in [r-env-singularity module  with different versions](r-env-for-gis.md).

## Usage 

### SAGA GIS command line interface

`r-env-singularity` is a Singularity container, which means the commands are slightly different compared normal installations, basically all commands need to have `singularity_wrapper exec` before the usual command.

SAGA GIS command line tools can be used in an [interactive session](../computing/running/interactive-usage.md) or [batch jobs](../computing/running/getting-started.md).

You can test that SAGA GIS loaded successfully and print the command line tools help information with

```
module load r-env-singularity 
singularity_wrapper exec saga_cmd -h
```

For more information on running R jobs on Puhti, please see the [`r-env-singularity` documentation](r-env-singularity.md).

### SAGA GIS Graphical User Interface

The easiest option for using SAGA GIS is to open it in [Puhti web interface as Desktop app](../computing/webinterface/desktop.md).

1. Log in to [Puhti web interface](https://puhti.csc.fi). 
2. Start SNAP: Apps -> Desktop, choose Desktop: 'None' and App: 'SAGA GIS'
3. The SNAP GUI is started automatically when the Desktop is launched. 


Alternatively, especially if you want to use SAGA GIS together with some other GUI tool or want to user older version, SAGA GIS can be started in Puhti web interface with remote desktop:

1. Log in to [Puhti web interface](https://puhti.csc.fi).
2. Open Remote desktop: Apps -> Desktop, choose Desktop: `mate` or `xfce`. 
3. After launcing the remote desktop open `Host Terminal` (Desktop icon) and start SAGA GIS:

```
module load r-env-singularity 
singularity_wrapper exec saga_gui
```

## License and acknowledgement

SAGA GIS is published under the [GPL](http://www.gnu.org/licenses/gpl.html) license. 

Please acknowlege CSC and Geoportti in your publications, it is important for project continuation and funding reports.
As an example, you can write "The authors wish to thank CSC - IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (Geoportti, urn:nbn:fi:research-infras-2016072513) for computational resources and support".

### References

* [SAGA GIS homepage](http://saga-gis.sourceforge.net/en/)
* [SAGA GIS page on Sourceforge](https://sourceforge.net/projects/saga-gis/)
* [SAGA GIS tutorials](https://sagatutorials.wordpress.com/)
* [SAGA GIS tutorials on Sourceforge](https://sourceforge.net/p/saga-gis/wiki/Tutorials/)

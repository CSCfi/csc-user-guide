---
tags:
  - Free
system:
  - www-puhti
---

# SAGA GIS

[Saga GIS](http://www.saga-gis.org/) (System for Automated Geoscientific Analyses) is a GIS application for spatial data editing and GIS analyses. 

## Available

__SAGA GIS__ is available:

* [r-env module with different versions](r-env-for-gis.md) with SagaGIS R packages, only in Puhti
* 7.3.0 - [qgis module](qgis.md) without SagaGIS R packages, in Puhti and LUMI

## Usage 

It can be used with a graphical user interface, command line tools or through the R package `Rsagacmd` or `RSAGA`. Since the `RSAGA` package is no longer actively maintained and has not been tested on newer SAGA GIS versions, we recommend using `Rsagacmd` with SAGA GIS 7.9.0 and higher. For more information on running R jobs on Puhti or using RStudio, please see the [`r-env` documentation](r-env.md).

For using SagaGIS, any of the modules listed about must be activated first, check the linked pages for details.


### SAGA GIS command line interface 
SAGA GIS command line tools can be used in an [interactive session](../computing/running/interactive-usage.md) or [batch jobs](../computing/running/getting-started.md).

#### SAGA GIS command line interface with r-env module

`r-env` is an Apptainer container, which means the commands are slightly different compared to normal installations, basically all commands need to have `apptainer_wrapper exec` before the usual command.

You can test that SAGA GIS loaded successfully and print the command line tools help information with

```
apptainer_wrapper exec saga_cmd -h
```

#### SAGA GIS command line interface with qgis module

With `qgis` module SagaGIS commands can be used normally, for example:

```
saga_cmd -h
```


### SAGA GIS Graphical User Interface

#### SAGA GIS Graphical User Interface in Puhti

To use SAGA GIS, open it in Puhti web interface:

1. Log in to [Puhti web interface](https://puhti.csc.fi).
2. Open [Desktop app](../computing/webinterface/desktop.md). 
3. After launching the Desktop, double-click SAGA GIS icon OR open `Terminal` (Desktop icon) and start SAGA GIS:

```
module load r-env
apptainer_wrapper exec saga_gui
```

#### SAGA GIS Graphical User Interface in LUMI

Until LUMI web interface is available, SagaGIS needs to be used with
[SSH X11 forwarding](../computing/connecting/index.md#graphical-connection).

```
module use /appl/local/csc/modulefiles
module load qgis
saga_gui
```


## License

SAGA GIS is published under the [GPL](http://www.gnu.org/licenses/gpl.html) license. 

## Citation

`Conrad, O., Bechtel, B., Bock, M., Dietrich, H., Fischer, E., Gerlitz, L., Wehberg, J., Wichmann, V., and Böhner, J. (2015): System for Automated Geoscientific Analyses (SAGA) v. 2.1.4, Geosci. Model Dev., 8, 1991-2007, doi:10.5194/gmd-8-1991-2015.  `

##  Acknowledgement

Please acknowledge CSC and Geoportti in your publications, it is important for project continuation and funding reports.
As an example, you can write "The authors wish to thank CSC - IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (Geoportti, urn:nbn:fi:research-infras-2016072513) for computational resources and support".

### References

* [SAGA GIS homepage](http://saga-gis.sourceforge.net/en/)
* [SAGA GIS page on Sourceforge](https://sourceforge.net/projects/saga-gis/)
* [SAGA GIS tutorials](https://sagatutorials.wordpress.com/)
* [SAGA GIS tutorials on Sourceforge](https://sourceforge.net/p/saga-gis/wiki/Tutorials/)

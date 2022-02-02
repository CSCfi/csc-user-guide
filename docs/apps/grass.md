# GRASS GIS

[GRASS](https://grass.osgeo.org/) (Geographic Resources Analysis Support System) is a free Geographic Information System (GIS) software used for geospatial data management and analysis, image processing, graphics/maps production, spatial modeling, and visualization.

## Available

__GRASS__ is available in Puhti with following versions:

* GRASS 7.8.5 with (default) qgis/3.22 module
* GRASS 7.4 with older qgis/3.16 module

## Usage

### GRASS GIS Command Line Interface 

In Puhti, GRASS GIS is included in [QGIS module](qgis.md). GRASS GIS command line tools can be used in an [interactive session](../computing/running/interactive-usage.md) or [batch jobs](../computing/running/getting-started.md). For using GRASS GIS, see [exmples for using GRASS GIS commands in Puhti with GRASS bash scripting, Python scripting or PyGRASS](https://github.com/csc-training/geocomputing/tree/master/grass).

### GRASS GIS Graphical User Interface

The easiest option for using GRASS GIS is to open it in [Puhti web interface as Desktop app](../computing/webinterface/desktop.md).

1. Log in to [Puhti web interface](https://puhti.csc.fi). 
2. Start SNAP: Apps -> Desktop, choose Desktop: 'None' and App: 'GRASS GIS'
3. GRASS GIS is started automatically when the Desktop is launched. 

Alternatively, especially if you want to use GRASS GIS together with some other GUI tool or want to user older version, GRASS GIS can be started in Puhti web interface with remote desktop:

1. Log in to [Puhti web interface](https://puhti.csc.fi).
2. Open Remote desktop: Apps -> Desktop, choose Desktop: `mate` or `xfce`. 
3. After launcing the remote desktop open `Host Terminal` (Desktop icon) and start GRASS GIS:

```
module load qgis
grass
```

## License and acknowledgement

Geographic Resources Analysis Support System (GRASS) is Copyright, 1999-2020 GRASS Development Team, and licensed under the terms of the GNU General Public License (GPL). This includes all software, documentation, and associated materials. [Full GRASS GIS license](https://grass.osgeo.org/about/license/)

Please acknowlege CSC and Geoportti in your publications, it is important for project continuation and funding reports.
As an example, you can write "The authors wish to thank CSC - IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (Geoportti, urn:nbn:fi:research-infras-2016072513) for computational resources and support".

### References

* [GRASS GIS homepage](https://grass.osgeo.org/)
* [GRASS GIS manuals](https://grass.osgeo.org/learn/manuals/)
* [GRASS GIS tutorials](https://grass.osgeo.org/learn/tutorials/)

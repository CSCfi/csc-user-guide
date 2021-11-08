# GRASS GIS

[GRASS](https://grass.osgeo.org/) (Geographic Resources Analysis Support System) is a free Geographic Information System (GIS) software used for geospatial data management and analysis, image processing, graphics/maps production, spatial modeling, and visualization.

## Available

__GRASS__ is available in Puhti with following versions:

* GRASS 7.4

## Usage

### Using GRASS GIS Command Line Interface 

In Puhti, GRASS GIS is installed inside the [QGIS singularity installation](qgis.md)

It can be loaded with

```
module load qgis
```

After loading the module you can use the GRASS GIS graphical user interface from an interactive session with 

```
sinteractive -i
grass
```

You can also use the command line tools that come in GRASS. See the [GRASS GIS manual](https://grass.osgeo.org/learn/manuals/) for more information. 

[Exmples for using GRASS GIS commands in Puhti with GRASS bash scripting, Python scripting or PyGRASS](https://github.com/csc-training/geocomputing/tree/master/grass).

### Using GRASS GIS Graphical User Interface

The GRASS GIS Graphical User Interface is available via the Puhti web interface:

1. Log in to [Puhti web interface](https://puhti.csc.fi). [Puhti web interface documentation](../computing/webinterface/desktop.md).
2. Start GRASS GIS with Apps -> Desktop, choose Desktop: 'None' and App: 'GRASS GIS'.

## License and citing

Geographic Resources Analysis Support System (GRASS) is Copyright, 1999-2020 GRASS Development Team, and licensed under the terms of the GNU General Public License (GPL). This includes all software, documentation, and associated materials. [Full GRASS GIS license](https://grass.osgeo.org/about/license/)

In your publications please acknowledge also oGIIR and CSC, for example “The authors wish to acknowledge for computational resources CSC – IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (oGIIR, urn:nbn:fi:research-infras-2016072513).”

### References

* [GRASS GIS homepage](https://grass.osgeo.org/)
* [GRASS GIS manuals](https://grass.osgeo.org/learn/manuals/)
* [GRASS GIS tutorials](https://grass.osgeo.org/learn/tutorials/)

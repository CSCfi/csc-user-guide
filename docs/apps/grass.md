# GRASS GIS

[GRASS](https://grass.osgeo.org/) (Geographic Resources Analysis Support System) is a free Geographic Information System (GIS) software used for geospatial data management and analysis, image processing, graphics/maps production, spatial modeling, and visualization.

## Available

__GRASS__ is available in Puhti with following versions:

* GRASS 7.4

## Usage

In Puhti GRASS GIS is installed inside the [QGIS singularity installation](qgis.md)

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

For GRASS commands to work in Puhti, you need to add `singularity_wrapper exec` before the GRASS commands. 

For example printing the instrucitons for the command grass74

```
singularity_wrapper exec grass74 -h
```

!!! note
    The recommended way of using graphical interfaces in Puhti is through [NoMachine](nomachine.md) and an [interactive batch job](../computing/running/interactive-usage.md)


## License and citing

Geographic Resources Analysis Support System (GRASS) is Copyright, 1999-2020 GRASS Development Team, and licensed under the terms of the GNU General Public License (GPL). This includes all software, documentation, and associated materials. [Full license can be found here](https://grass.osgeo.org/about/license/)

In your publications please acknowledge also oGIIR and CSC, for example “The authors wish to acknowledge for computational resources CSC – IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (oGIIR, urn:nbn:fi:research-infras-2016072513).”

### References

* [GRASS GIS homepage](https://grass.osgeo.org/)
* [GRASS GIS manuals](https://grass.osgeo.org/learn/manuals/)
* [GRASS GIS tutorials](https://grass.osgeo.org/learn/tutorials/)

---
tags:
  - Free
system:
  - www-puhti
---

# GRASS GIS

[GRASS](https://grass.osgeo.org/) (Geographic Resources Analysis Support System) is a free Geographic Information System (GIS) software used for geospatial data management and analysis, image processing, graphics/maps production, spatial modeling, and visualization.

## Available

__GRASS__ is available with following versions:

* 8.3 with grassgis module in Puhti
* 7.8.7 with [qgis/3.31 module](qgis.md) in Puhti and LUMI
* 7.8.5 with [qgis/3.22 module](qgis.md) in Puhti


## Usage

### GRASS GIS Command Line Interface 

GRASS GIS command line tools can be used in an [interactive session](../computing/running/interactive-usage.md) or [batch jobs](../computing/running/getting-started.md). See [examples for using GRASS GIS commands in Puhti with GRASS bash scripting, Python scripting or PyGRASS](https://github.com/csc-training/geocomputing/tree/master/grass). See also the references section at the end of this page.

### GRASS GIS Graphical User Interface

#### GRASS in Puhti

The easiest option for using GRASS GIS is to open it in Puhti web interface.

1. Log in to [Puhti web interface](https://puhti.csc.fi). 
2. Open [Desktop app](../computing/webinterface/desktop.md). 
3. After launching the Desktop, double-click GRASS-GIS icon for the newest version.
 
If you want to use older version, open `Terminal` (Desktop icon) and start GRASS GIS:

```
module load qgis/3.22
grass
```

#### GRASS in LUMI

Until LUMI web interface is available, GRASS needs to be used with
[SSH X11 forwarding](../computing/connecting/index.md#graphical-connection).

```
module use /appl/local/csc/modulefiles
module load qgis
grass
```

## License 

Geographic Resources Analysis Support System (GRASS) is Copyright, 1999-2020 GRASS Development Team, and licensed under the terms of the GNU General Public License (GPL). This includes all software, documentation, and associated materials. [Full GRASS GIS license](https://grass.osgeo.org/about/license/)


## Citation

This software can be cited by chosing the appropriate citation from the [GRASS citation repository](https://grasswiki.osgeo.org/wiki/GRASS_Citation_Repository). 


## Acknowledgement

Please acknowledge CSC and Geoportti in your publications, it is important for project continuation and funding reports.
As an example, you can write "The authors wish to thank CSC - IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (Geoportti, urn:nbn:fi:research-infras-2016072513) for computational resources and support".


## Installation

* GRASS 8.3 was installed to Puhti with [Tykky's wrap-container functionality](../computing/containers/tykky.md#container-based-installations) using the [GRASS Docker image from Dockerhub provided by OSGEO](https://hub.docker.com/r/osgeo/grass-gis): `wrap-container -w /usr/local/bin,/usr/bin/python3 docker://osgeo/grass-gis:releasebranch_8_3-ubuntu_wxgui --prefix 8.3`
* GRASS 7.x was installed to Puhti and LUMI as part of [QGIS installation](qgis.md#installation).


## References

* [GRASS GIS homepage](https://grass.osgeo.org/)
* [GRASS GIS manuals](https://grass.osgeo.org/learn/manuals/)
  * [Parellel GRASS jobs](https://grasswiki.osgeo.org/wiki/Parallel_GRASS_jobs)
* [GRASS GIS tutorials](https://grass.osgeo.org/learn/tutorials/)
* [GRASS database, location, mapset and region](https://grass.osgeo.org/grass79/manuals/grass_database.html), the basic concepts always needed with GRASS GIS. 
In case of using parallel computation, be extra careful with `region`.
* [Anna Petrasova, GRASS GIS workshop at FOSS4G, part 5: parallelization](https://github.com/ncsu-geoforall-lab/grass-gis-workshop-foss4g-2022/blob/main/workshop_part_5_parallelization.ipynb)

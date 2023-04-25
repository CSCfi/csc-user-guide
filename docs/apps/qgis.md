---
tags:
  - Free
---

# QGIS

[QGIS](https://qgis.org/en/site/) is a free and open source GIS application that can be used for viewing, editing and analysing geospatial data. QGIS supports a very wide range of vector and raster formats and also common API protocols like WMS, WMTS, WCS and WFS. 

In Puhti, QGIS could be used for example to visualize the resulting files from processing with other tools: lastools, R, Python etc.


## Available

__QGIS__ is available in Puhti with following versions:

* 3.31
* 3.22

## Usage

The easiest option for using  QGIS is to open it in [Puhti web interface as Desktop app](../computing/webinterface/desktop.md).

1. Log in to [Puhti web interface](https://puhti.csc.fi). 
2. Open Remote desktop: Apps -> Desktop, choose Desktop: `xfce`. 
3. After launcing the remote desktop, double-click QGIS icon for the newest version.

If you want to use older version, open `Host Terminal` (Desktop icon) and start QGIS:

```
module load qgis/3.22
qgis
```

SagaGIS tools are not available by default with QGIS 3.31 in Processing Toolbox, but can be added with installing `Saga Next Gen` plug-in. This is a new plug-in and all tools might not work yet.  

### PyQGIS

It is also possible to access QGIS functionalities from Python without an graphical user interface with the [PyQGIS library](https://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook/). Use `python3` for accessing PyQGIS libraries.


### QGIS and Allas
QGIS can __read__ files directly from Allas, either using S3 or SWIFT API. Before starting QGIS set up the connection as described in on [GDAL](gdal.md) page.

## License and acknowledgement

QGIS is licensed under the GNU General Public License. QGIS is an official project of the Open Source Geospatial Foundation (OSGeo).

Please acknowledge CSC and Geoportti in your publications, it is important for project continuation and funding reports.
As an example, you can write "The authors wish to thank CSC - IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (Geoportti, urn:nbn:fi:research-infras-2016072513) for computational resources and support".

### References

* [QGIS homepage](https://www.qgis.org/)
* [QGIS tutorials](https://www.qgistutorials.com/en/)
* [Free QGIS training material](https://qgis.org/en/site/forusers/trainingmaterial/index.html)
* [PyQGIS cookbook](https://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook/)

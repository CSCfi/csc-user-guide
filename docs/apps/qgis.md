# QGIS

[QGIS](https://qgis.org/en/site/) is a free and open source GIS application that can be used for viewing, editing and analysing geospatial data. QGIS supports a very wide range of vector and raster formats and also common API protocols like WMS, WMTS, WCS and WFS.

In Puhti, QGIS could be used for example to visualize the resulting files from other sources (lastools, R, python)

## Available

__QGIS__ is available in Puhti with following versions:

* 3.22 in a singularity container: qgis(/3.22 = default) module
* 3.16 in a singularity container: qgis/3.16 module

## Usage

The easiest option for using QGIS is to open it in [Puhti web interface as Desktop app](../computing/webinterface/desktop.md).

1. Log in to [Puhti web interface](https://puhti.csc.fi). 
2. Start QGIS: Apps -> Desktop, choose Desktop: 'single application' and App: 'QGIS'
3. QGIS is started automatically when the Desktop is launched. 


Alternatively, especially if you want to use QGIS together with some other Graphical User Interface (GUI) tool or want to use data from Allas, QGIS can be started in Puhti web interface with remote desktop:

1. Log in to [Puhti web interface](https://puhti.csc.fi).
2. Open Remote desktop: Apps -> Desktop, choose Desktop: `mate` or `xfce`. 
3. After launcing the remote desktop, double-click QGIS icon OR open `Host Terminal` (Desktop icon) and start QGIS:

```
module load qgis
qgis
```


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

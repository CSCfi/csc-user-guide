# QGIS

[QGIS](https://qgis.org/en/site/) is a free and open source GIS application that can be used for viewing, editing and analysing geospatial data. QGIS supports a very wide range of vector and raster formats and also common API protocols like WMS, WMTS, WCS and WFS.

In Puhti, QGIS could be used for example to visualize the resulting files from other sources (lastools, R, python)

## Available

__QGIS__ is available in Puhti with following versions:

* 3.22 in a singularity container: qgis(/3.22 = default) module
* 3.16 in a singularity container: qgis/3.16 module

## Usage

Using QGIS in [Puhti web interface with Desktop app](../computing/webinterface/desktop.md).

1. Log in to [Puhti web interface](https://puhti.csc.fi). 
2. Start QGIS with Apps -> Desktop, choose Desktop: 'None' and App: 'QGIS'.

Alternatively, especially if you want to use QGIS together with some other Graphical User Interface (GUI) tool or want to use data from Allas, QGIS can be started in Puhti web interface within mate or xfce Desktop App from the QGIS icon on the Desktop or from the `Host Terminal` (Desktop icon) with the commands:

```
module load qgis
qgis
```


### PyQGIS

It is also possible to access QGIS functionalities from Python without an graphical user interface with the [PyQGIS library](https://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook/). Use `python3` for accessing PyQGIS libraries.


### QGIS and Allas
QGIS can __read__ files directly from Allas, either using S3 or SWIFT API. Before starting QGIS set up the connection as described in on [GDAL](gdal.md) page.

## License and citing

QGIS is licensed under the GNU General Public License. QGIS is an official project of the Open Source Geospatial Foundation (OSGeo).

In your publications please acknowledge also oGIIR and CSC, for example “The authors wish to acknowledge for computational resources CSC – IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (oGIIR, urn:nbn:fi:research-infras-2016072513).”

### References

* [QGIS homepage](https://www.qgis.org/)
* [QGIS tutorials](https://www.qgistutorials.com/en/)
* [Free QGIS training material](https://qgis.org/en/site/forusers/trainingmaterial/index.html)
* [PyQGIS cookbook](https://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook/)

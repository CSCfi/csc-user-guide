# QGIS

[QGIS](https://qgis.org/en/site/) is a free and open source GIS application that can be used for viewing, editing and analysing geospatial data. QGIS supports a very wide range of vector and raster formats and also common API protocols like WMS, WMTS, WCS and WFS.

In Puhti, QGIS could be used for example to visualize the resulting files from other sources (lastools, R, python)

## Available

__QGIS__ has been installed in two different ways to Puhti. The Singularity installation is a container installation which makes it somewhat faster compared to the older conda installation. QGIS is available in Puhti with following versions:

* 3.16 in a singularity container
* 3.14 via conda in geoconda-3.8
* 3.10 via conda in geoconda-3.7

## Usage

### Using QGIS in Puhti web interface

This is the new recommended way.

1. Log in to [Puhti web interface](https://puhti.csc.fi). [Puhti web interface documentation](../computing/webinterface/index.md).
2. Start QGIS with Apps -> Desktop, choose Desktop: 'None' and App: 'QGIS'.

### Alternative (old) use of QGIS with NoMachine

1. Connect to Puhti with [NoMachine](nomachine.md). A SSH connection with __X11 forwarding__ should also work, but is likely slower.
2. Start an [interactive session](../computing/running/interactive-usage.md)

```
sinteractive -i
```


#### Singularity installation

Load the module and start QGIS

```
module load qgis
qgis
```

#### Conda installation

QGIS is older older versions are included in the [geoconda](../apps/geoconda.md) module and can be started with

```
module load geoconda
qgis
```    

### PyQGIS
It is also possible to access QGIS functionalities from Python without an graphical user interface with the [PyQGIS library](https://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook/). With `qgis module` use `python3` for accessing PyQGIS libraries.


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

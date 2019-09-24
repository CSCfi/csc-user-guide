# QGIS

[QGIS](https://qgis.org/en/site/) is a free and open source GIS application that can be used for viewing, editing and analysising geospatial data. QGIS supports a very wide range of vector and raster formats and also common API protocols like WMS, WMTS, WCS and WFS.

In Puhti, QGIS could be used for example to visualize the resulting files from other sources (lastools, grass, python)

## Available

__QGIS__ is available in Puhti with following versions:

* 3.8.1 Zanzibar via conda

## Usage

### Using QGIS with graphical user interface

QGIS is included in the [geoconda](../apps/geoconda.md) module and can be loaded with

`module load geoconda`

If you have connected with a ssh connection that has __X11 forwarding__ enabled, you can launch a graphical user interface with

`qgis`

For __X11 forwarding__ to be enabled you need to install a suitable program for your own computer first (unless you are using Linux or Mac). You can read instructions how to do that [here](../computing/connecting.md#Using graphics)

It is also possible to access QGIS functionalities from Python without an graphical user interface with the [PyQGIS](https://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook/) library

## License and citing

QGIS is licensed under the GNU General Public License. QGIS is an official project of the Open Source Geospatial Foundation (OSGeo).

In your publications please acknowledge also oGIIR and CSC, for example “The authors wish to acknowledge for computational resources CSC – IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (oGIIR, urn:nbn:fi:research-infras-2016072513).”

### References

* [QGIS homepage](https://www.qgis.org/)
* [QGIS tutorials](https://www.qgistutorials.com/en/)
* [Free QGIS training material](https://qgis.org/en/site/forusers/trainingmaterial/index.html)

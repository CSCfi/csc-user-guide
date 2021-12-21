# Multispectral satellite remote sensing

The purpose of this guide is to help you finding the right data and tools for satellite remote sensing tasks. The basis of this guide is a seminar about the topic held at CSC in 2018. And part of the material will also be taught in geospatial training at CSC, check the [training calendar](https://www.csc.fi/web/training) for dates and topics of upcoming courses. The guide has two parts, choose the first, if you just want to know how to get your processing done quickly (link), and the more detailed way with lots of information and considerations (link). If you encounter any problems or questions come up CSC's specialists are happy to help with all aspects of your data driven research, and can be contacted via the [CSC Service Desk](https://www.csc.fi/contact-info).

## Summary

Follow these steps if you 'just want to get the preprocessing done', rather than read the full guide, the TL;DR so to say.

1. Find data
2. Get data
3. 

## I want to know every detail of every step, where do I start?

> More information on each step of the way

### Finding the right data for your purpose

What to consider:
* resolution
    * temporal 
    * spatial
    * spectral
* costs
    * **free**
        * [Landsat](https://landsat.gsfc.nasa.gov/)
        * [MODIS](https://modis.gsfc.nasa.gov/)
        * [Copernicus Sentinel-2](https://sentinel.esa.int/web/sentinel/missions/sentinel-2)
    * others
        * [Pleiades](https://pleiades.cnes.fr/en/PLEIADES/index.htm)
        * [Spot](https://www.intelligence-airbusds.com/imagery/constellation/spot/)
        * [Planet](https://www.planet.com/products/planet-imagery/)
        * [WorldView](http://worldview3.digitalglobe.com/)
        * and many more, but focus here is on Landsat 8 and Sentinel-2, as these are most used.
* preprocessing needs
    * top of atmosphere vs bottom of atmosphere
* GUI vs API, Python/R interface

[Global satellite data providers](https://research.csc.fi/open-gis-data#intdata3)

### Data sources

=== "FinHub"

[FinHub](https://finhub.nsdc.fmi.fi/#/home)

* needs [registration](https://nsdc.fmi.fi/services/service_finhub_registration)
* only L1C 
* only Finland (and Baltics)
* same GUI and API (older version?) as SciHub

=== "SciHub"

[SciHub](https://scihub.copernicus.eu/dhus/#/home)

* needs [registration](https://scihub.copernicus.eu/dhus/#/self-registration) 

* L1C and L2A
* worldwide
* GUI and API
* Long term archive

=== "Earthexplorer"

[Earthexplorer](https://earthexplorer.usgs.gov/)

* needs [registration](https://ers.cr.usgs.gov/register)

* worldwide
* lots of different data US related
* main: Landsat
* GUI and bulk download
* LS download instructions: https://lta.cr.usgs.gov/sites/default/files/LS_C2_Help_122020.pdf

=== "other solutions, mostly commercial"

* [AWS](https://registry.opendata.aws/sentinel-2/)
* DIAS - Data and Information Access Services
    * [ONDA](https://www.onda-dias.eu/cms/)
    * [sobloo](https://sobloo.eu/)
    * [CREODIAS](https://creodias.eu/)
    * [MUNDI](https://mundiwebservices.com/)
* [Terramonitor](https://www.terramonitor.com/services/analysis-ready)
* [Sentinelhub](https://www.sentinel-hub.com/explore/)
* [Google Earth Engine](https://developers.google.com/earth-engine/datasets/catalog/sentinel-2/)


=== "CSC Puhti"

* FMI/SYKE mosaics (limited)
* - link to example script

=== "CSC Allas"

*  some data available in public buckets (limited)
* - link to example script


=== "SYKE"

* SYKE and FMI
* instructions on how to use - link to example script

### Storing data

* raw vs intermediate vs final result data
* considerations:
    * who needs that data
    * accessibility
    * 
* Puhti vs Allas vs ext harddrive vs IDA vs EuDat vs other objectstorage
* instructions on all with links

### Processing data

#### Software

What to consider:
* user skills
    * scripting
        * bash/(batch/powershell)
        * python
        * R
        * Julia 
* user needs
    * automation
    * reproducibility
* open source vs commercial
* GUI vs CLI

##### GUI

[Puhti web interface](https://puhti.csc.fi) 

###### SNAP

"All-in-one" GUI, CLI (gpt) with Python interfaces snappy and snapista
* for initial test

###### QGIS 

GIS software with limited multispectral image processing capabilities
* Visualization, mapmaking
* Band math
* semi-automatic classification plugin  (LS and others preprocessing, atmospheric correction, pansharpening; https://semiautomaticclassificationmanual.readthedocs.io/fi/latest/preprocessing_tab.html)

###### Orfeo Toolbox (+CLI, difficult to use, bugs)

##### CLI

###### SNAP GPT
###### Sen2Cor
###### FORCE
###### GDAL (OGR)


##### Python

[Geospatial Python on Puhti](https://docs.csc.fi/apps/geoconda/)

##### R

[Geospatial R on Puhti](https://docs.csc.fi/apps/r-env-for-gis/)
[Geospatial R course material]()

##### Julia

[Julia on Puhti](https://docs.csc.fi/apps/julia/)
[JuliaGeo](https://github.com/JuliaGeo)

#### Preprocessing

(can be skipped if your data is preprocessed)
How to know what preprocessing has been done? ->


#### Common usecases

##### Cloudmasking
##### Mosaicing

* mention challenges 
    * data does not match between years
    * visible borders
    * 

##### Pansharpening/Fusion
##### NDVI/Band Math
##### Subsetting
##### Aggregating

##### Addon: Georeferencing (historical images)

### Sharing processes

* github/lab
* also GUI processes can be sharable
* consider also the environment
    * container
* 

### Sharing data

* depends on above
* FAIR!
* think about long-term

# Multispectral satellite remote sensing

The purpose of this guide is to help you finding the right data and tools for satellite remote sensing tasks. The basis of this guide is a seminar about the topic held at CSC in 2018. And part of the material will also be taught in geospatial training at CSC, check the [training calendar](https://www.csc.fi/web/training) for dates and topics of upcoming courses. The guide provides a shorter summary if you just want to know how to get your processing done quickly (link), and then a more detailed way with lots of information and considerations (link). If you encounter any problems or questions come up, CSC's specialists are happy to help with all aspects of your data driven research, and can be contacted via the [CSC Service Desk](https://www.csc.fi/contact-info).



## Summary

Follow these steps if you 'just want to get the preprocessing done', rather than read the full guide, the TL;DR so to say.

1. Find data
2. Get data
3. Process
4. Store & Share

## Multispectral Satellite remote sensing data == Raster data

* raster data
    * usually one file per band
    * grid of pixel values
    * example of continuous data
    * Georeference: coordinate for the top left pixel in the image, the size of each pixel in the X direction, the size of each pixel in the Y direction, and the amount (if any) by which the image is rotated.

### What data do I need?

What to consider:
* resolution
    * temporal: when and how often a certain area is visited
    * spatial: the area on the ground that each pixel covers
    * spectral: spectral width of each band provided
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
        * and many more...
* preprocessing needs
    * top of atmosphere (data as collected by the instrument) vs bottom of atmosphere (or surface reflectance: atmospheric artifacts removed from data)
* personal preferences for software
    * Graphical User Interface (GUI)
    * Command Line Interface (CLI)
    * Application Programming interface (API)

[Global satellite data providers](https://research.csc.fi/open-gis-data#intdata3)

### Where do I find the data?

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

=== "EarthExplorer"

    [Earthexplorer](https://earthexplorer.usgs.gov/)

    * needs [registration](https://ers.cr.usgs.gov/register)

    * worldwide
    * lots of different US related datasets 
    * main: Landsat
    * GUI in web interface and bulk download
    * Landsat download instructions: https://lta.cr.usgs.gov/sites/default/files/LS_C2_Help_122020.pdf

=== "CSC environments"

    Puhti
    * [list of all available datasets in Puhti](../../data/datasets/spatial-data-in-csc-computing-env/#spatial-data-in-puhti)
        * Sentinel and Landsat mosaics of Finland provided by FMI and SYKE: ```/appl/data/geo/sentinel/s2```
        * every CSC user has read access
    Allas
    * [list of all available geospatial datasets in Allas](../../data/datasets/spatial-data-in-csc-computing-env/#spatial-data-in-allas)
        * Sentinel-2 L2A data of crop growing Finland, growing seasons 2016-present, [usage instructions](https://a3s.fi/sentinel-readme/README.txt)

=== "Paikkatietoalusta"

    * [Sentinel-2 mosaics](https://ckan.ymparisto.fi/dataset/sentinel-2-image-index-mosaics-s2ind-sentinel-2-kuvamosaiikit-s2ind) provided by [SYKE](https://www.syke.fi/en-US) and [FMI](https://en.ilmatieteenlaitos.fi/)
    * instructions on how to use - link to example script

=== "others"

    * [AWS](https://registry.opendata.aws/sentinel-2/)
    * DIAS - Data and Information Access Services
        * [ONDA](https://www.onda-dias.eu/cms/)
        * [sobloo](https://sobloo.eu/)
        * [CREODIAS](https://creodias.eu/)
        * [MUNDI](https://mundiwebservices.com/)
    * [Terramonitor](https://www.terramonitor.com/services/analysis-ready)
    * [Sentinelhub](https://www.sentinel-hub.com/explore/)
    * [Google Earth Engine](https://developers.google.com/earth-engine/datasets/catalog/sentinel-2/)

See also examples for downloading Sentinel data from FinHub/SciHub on [github](https://github.com/csc-training/geocomputing/tree/master/python/sentinel).

### Where can I store the data?

What to consider:

* raw vs intermediate vs final result data
    * what needs to be stored?
* accessibility
    * who needs to have access?
    * how needs the data to be accessed?

#### What storage solutions are available at CSC?

=== "During the process"
    
    * For direct access data can be stored on the supercomputer, check out the [different available disk areas](../../computing/disk)
    * Data can be stored on ```/scratch/project_xxx``` with xxx being your project number
    * Smaller amounts can also be stored short term on the computing nodes ```$LOCAL_SCRATCH``` during processing

=== "Short term storage"

    * [Allas overview](https://research.csc.fi/-/allas)
    * [Allas guide](../../data/Allas/index.md)

=== "Long term storage"

    * [Paituli](https://research.csc.fi/-/paituli-1)
    * [IDA overview](https://www.fairdata.fi/en/user-guide/) and [IDA guide](https://www.fairdata.fi/en/user-guide/)
    * [EUDat overview](https://research.csc.fi/-/eudat-services)

See also CSCs general [guide on working with data](../../data/datasets/index.html).


### How can I process the data?

#### Software

What to consider:
* user skills and preferences
    * Graphical User Interface (GUI)
    * Command Line Interface (CLI)
    * Application Programming Interface (API)
        * Python
        * R
        * Julia 
* user needs
    * batch processing
    * automation
    * reproducibility
* open source vs commercial
    * this guide focusses on [software available on CSC supercomputer Puhti](../../apps/#geosciences) 

##### What software is available at CSC?

* only Linux software

=== "GUI"

    Graphical User Interfaces of software available on Puhti can be accessed via the [Puhti web interface](https://puhti.csc.fi) or [NoMachine or X11 connection](../../computing/connecting/#using-graphical-applications). These graphical interfaces are mainly for visualization and testing purposes, the actual efficient processing should not happen here.

    ###### [SNAP](https://step.esa.int/main/toolboxes/snap/)

    "All-in-one" Graphical User Interface for processing of Sentinel data (+ support for other data sources) with Python interfaces [snappy](https://senbox.atlassian.net/wiki/spaces/SNAP/pages/19300362/How+to+use+the+SNAP+API+from+Python) and [snapista](https://snap-contrib.github.io/snapista/) and the [Graph Processing Tool](https://step.esa.int/docs/tutorials/SNAP_CommandLine_Tutorial.pdf) as Command Line Interface.

    * [SNAP on Puhti](https://docs.csc.fi/apps/snap/)

    ###### [QGIS](https://www.qgis.org/en/site/) 

    GIS software with limited multispectral image processing capabilities
    * Visualization
    * [Map making](https://www.qgistutorials.com/en/docs/making_a_map.html)
    * Map algebra / Band math and other [raster processing](https://docs.qgis.org/3.22/en/docs/user_manual/processing_algs/qgis/rasteranalysis.html)
    * [semi-automatic classification plugin](https://fromgistors.blogspot.com/p/semi-automatic-classification-plugin.html) 

    * [QGIS on Puhti](https://docs.csc.fi/apps/qgis/)

    ###### [Orfeo Toolbox](https://www.orfeo-toolbox.org/)

    Offers a wide variety of applications from ortho-rectification or pansharpening, all the way to classification, SAR processing, and much more!

    Orfeo Toolbox is available as [Command Line Interface](https://www.orfeo-toolbox.org/CookBook/CliInterface.html), [Graphical User Interface](https://www.orfeo-toolbox.org/CookBook/GraphicalInterface.html), Python API and as plugin to other applications.
    
    * GUI (https://www.orfeo-toolbox.org/CookBook/GraphicalInterface.html) 

=== "CLI"

    ###### SNAP GPT

    Command Line Interface for [SNAP](https://docs.csc.fi/apps/snap/).
    See examples for use of SNAP GPT on Puhti on [github](https://github.com/csc-training/geocomputing/tree/master/snap).

    ###### Sen2Cor

    [Sen2Cor](https://docs.csc.fi/apps/sen2cor/) is a stand-alone processor for Sentinel-2 Level 2A product generation and formatting.

    ###### FORCE

    [FORCE](https://docs.csc.fi/apps/sen2cor/) (Framework for Operational Radiometric Correction for Environmental monitoring) is an all-in-one solution for mass-processing medium-resolution satellite images.

    See examples for use of FORCE on Puhti on [github](https://github.com/csc-training/geocomputing/tree/master/force)

    ###### GDAL (OGR)

    [GDAL](https://docs.csc.fi/apps/gdal/) (Geospatial Data Abstraction Library) is a geospatial library for accessing and transforming geospatial data. 

    See examples for use of GDAL on Puhti on [github](https://github.com/csc-training/geocomputing/tree/master/gdal)

=== "API"

    ##### Python

    [Geospatial Python on Puhti](https://docs.csc.fi/apps/geoconda/)

    The geoconda module provides many useful Python packages for multispectral raster data processing and analysis:

    * geopandas:
    * rasterio: access to geospatial raster data.
    * rasterstats: summarizing geospatial raster datasets based on vector geometries.
    * sentinelsat: downloading Sentinel images
    * scimage: algorithms for image processing.
    * xarray: working with multidimensional raster data. 
    * dask: 

    See examples for use of geopspatial Python on Puhti on [github](https://github.com/csc-training/geocomputing/tree/master/python)

    ##### R

    [Geospatial R on Puhti](https://docs.csc.fi/apps/r-env-for-gis/)
    [Geospatial R course material]()
    [Examples geospatial R](https://github.com/csc-training/geocomputing/tree/master/R)

    ##### Julia

    [Julia on Puhti](https://docs.csc.fi/apps/julia/)
    [JuliaGeo](https://github.com/JuliaGeo)

#### Preprocessing

(can be skipped if your data is preprocessed)
How to know what preprocessing has been done? 
-> check filename and naming conventions of your platform
Look out for words like Bottom of atmosphere / Surface Reflectance that indicate that atmospheric correction has been done to the product. 

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


## Resources

https://step.esa.int/main/doc/tutorials/
https://www.earthdatascience.org/courses/use-data-open-source-python/multispectral-remote-sensing/intro-multispectral-data/ 
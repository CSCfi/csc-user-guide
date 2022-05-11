# Satellite remote sensing

The purpose of this guide is to help you finding the right data and tools for satellite remote sensing tasks. The basis of this guide is a seminar about the topic held at CSC in 2018. And part of the material will also be taught in geospatial training at CSC, check the [training calendar](https://www.csc.fi/web/training) for dates and topics of upcoming courses. The guide provides a shorter summary if you just want to know how to get your processing done quickly (link), and then a more detailed way with lots of information and considerations (link). If you encounter any problems or questions come up, CSC's specialists are happy to help with all aspects of your data driven research, and can be contacted via the [CSC Service Desk](https://www.csc.fi/contact-info).

## Summary

Follow these steps if you 'just want to get the preprocessing done', rather than read the full guide, the TL;DR so to say.

1. Find data 
    * ...
2. Get data
    * ...
3. Process
    * ...
4. Store & Share
    * ...

## Raster data

* one file per band or multiband files
* grid of pixel values
* example of continuous data
* Georeference: coordinate for the top left pixel in the image, the size of each pixel in the X direction, the size of each pixel in the Y direction, and the amount (if any) by which the image is rotated.

## Using satellite remote sensing data in your research

### What data do I need?

Consider:

* sensor
    * Optical
        * [Landsat](https://landsat.gsfc.nasa.gov/)
        * [MODIS](https://modis.gsfc.nasa.gov/)
        * [Copernicus Sentinel-2](https://sentinel.esa.int/web/sentinel/missions/sentinel-2)
        * [Pleiades](https://pleiades.cnes.fr/en/PLEIADES/index.htm)
        * [Spot](https://www.intelligence-airbusds.com/imagery/constellation/spot/)
        * [Planet](https://www.planet.com/products/planet-imagery/)
        * [WorldView](http://worldview3.digitalglobe.com/)
        * and many more...
    * RADAR (Radio Detection and Ranging) -> SAR (Synthetic Aperture Radar)
        * [Copernicus Sentinel 1](https://sentinel.esa.int/web/sentinel/missions/sentinel-1)
        * [Radarsat](https://www.asc-csa.gc.ca/eng/satellites/radarsat/default.asp)
        * [TanDEM-X](https://www.dlr.de/content/en/missions/tandem-x.html)
        * [TerraSAR-X](https://www.dlr.de/content/en/missions/terrasar-x.html)
        * [ICEYE](https://www.iceye.com/)
        * and many more...
    * LiDAR (Light Detection and Ranging)
        * [ICESat](https://icesat-2.gsfc.nasa.gov/)
        * [GEDI](https://gedi.umd.edu/)
* resolution
    * temporal: when and how often a certain area is visited
    * spatial: the area on the ground that each pixel covers
    * spectral: the area of the electromagnetic spectrum that is observed and spectral width of each band provided
* costs
    * free: e.g. Landsat, MODIS, Sentinel, ...
    * commercial: e.g. WorldView, Spot, Planet, ...
* preprocessing needs
    * raw or pre-processed
* user experience and knowledge
    * RADAR/LiDAR require solid background knowledge for processing and interpretation
    * Optical  data is more easily interpreted and processed (and more pre-processed data is available)


### Where do I find the data?

The best place to get the data from depends on your needs: Do you want to download the data into your own processing environment or do you need a processing environment close to the data? The answer depends on what you want to do with the data and where it is located.

Below is a (uncomplete) set of services, that provide download or download and processing (marked with *) capabilities:

See also a list of other places on [CSC research pages](https://research.csc.fi/open-gis-data#intdata3).

=== "CSC * "

    * Puhti
        * [list of all available datasets in Puhti](../../../data/datasets/spatial-data-in-csc-computing-env/#spatial-data-in-puhti)
        * Sentinel and Landsat mosaics of Finland provided by FMI and SYKE: ```/appl/data/geo/sentinel/s2```
        * every CSC user has **read** access to data stored on Puhti, no need to move it, unless you need to modify it
    * Allas
        * [list of all available geospatial datasets in Allas](../../../data/datasets/spatial-data-in-csc-computing-env/#spatial-data-in-allas)
        * Sentinel-2 L2A data of crop growing Finland, growing seasons 2016-present, [usage instructions](https://a3s.fi/sentinel-readme/README.txt)
        * Data can be directly read from Allas without download for some cases, see eg [GDAL docs](../../../apps/gdal/#using-files-directly-from-allas) and [Allas Python examples](https://github.com/csc-training/geocomputing/blob/master/python/allas/working_with_allas_from_Python_S3.py)

  
    
=== "Open Access Hubs"

    [SciHub](https://scihub.copernicus.eu/dhus/#/home)

    * needs [registration](https://scihub.copernicus.eu/dhus/#/self-registration) 

    * Sentinel 2 L1C and L2A products
    * Sentinel 1 SLC, GRD , RAW and OCN products
    * worldwide
    * Note: most of the data is in "Long term archive" and cannot be downloaded directly, but needs to be requested

    [FinHub](https://finhub.nsdc.fmi.fi/#/home)

    * needs [registration](https://nsdc.fmi.fi/services/service_finhub_registration)
    * Sentinel 2 L1C product
    * Sentinel 1 SLC, GRD and OCN products
    * only Finland (and Baltics)

    [ASF](https://search.asf.alaska.edu/#/)
    
    * needs [registration](https://urs.earthdata.nasa.gov/users/new?)
    * Sentinel 1 SLC, GRD , RAW and OCN products
    * Many SAR and SAR derived datasets from other sensors
    * Worldwide
    * Sentinel 1 data available for immediate download
    
    **All of the above** provide a similar Graphical User Interface (GUI) and Application Programming Interface (API) to access the data.
    Other tools for downloading the data from open access hubs: [sentinelsat](https://sentinelsat.readthedocs.io/en/stable/) with [examples for SciHub and FinHub](https://github.com/csc-training/geocomputing/blob/master/python/sentinel/sentinelsat_download_from_finhub_and_scihub.py), ...

=== "EarthExplorer"

    [Earthexplorer](https://earthexplorer.usgs.gov/)

    * needs [registration](https://ers.cr.usgs.gov/register)
    * lots of different US related datasets 
    * main: Landsat worldwide
    * GUI in web interface and bulk download
    * Landsat download instructions: https://lta.cr.usgs.gov/sites/default/files/LS_C2_Help_122020.pdf

=== "Sentinel image mosaics"

    * Available in Puhti: /appl/data/geo/sentinel?
    * Only Finland
    * [Sentinel-2 image index mosaics](https://ckan.ymparisto.fi/dataset/sentinel-2-image-index-mosaics-s2ind-sentinel-2-kuvamosaiikit-s2ind) 
    * [Sentinel-1 SAR-image mosaics](https://ckan.ymparisto.fi/dataset/sentinel-1-sar-image-mosaic-s1sar-sentinel-1-sar-kuvamosaiikki-s1sar)
    * [WMS (Geoserver)](https://data.nsdc.fmi.fi/geoserver/wms)
    * [WCS (Geoserver)](https://data.nsdc.fmi.fi/geoserver/wcs)
    * provided by [SYKE](https://www.syke.fi/en-US) and [FMI](https://en.ilmatieteenlaitos.fi/)
    * instructions on how to use - link to example script

=== "Google Cloud Storage"

    [Google Cloud Storage](https://cloud.google.com)

    * [Sentinel 2: L1C](https://cloud.google.com/storage/docs/public-datasets/sentinel-2)
    * [Landsat: Collection 1](https://cloud.google.com/storage/docs/public-datasets/landsat)
    * [FORCE](../../../apps/force/) can download directly from here

=== "Amazon Web Service (AWS) *"


    * Worldwide
    * [Sentinel-2 bucket](https://registry.opendata.aws/sentinel-2/)
    * [Sentinel-1 bucket](https://registry.opendata.aws/sentinel-1/)
    * Requester pays the download costs
    * Managed by [Sinergise](http://www.sinergise.com/) 

=== "DIAS *" 

    * Data and Information Access Services
    * multiple sites exits:
        * [ONDA](https://www.onda-dias.eu/cms/)
        * [sobloo](https://sobloo.eu/)
        * [CREODIAS](https://creodias.eu/)
        * [MUNDI](https://mundiwebservices.com/)
    * costs
    * processing platform with the data, no download needed
    * data from DIAS objectstorage can easily be transferred to Allas (link to instructions here)
    
=== "Microsoft planetary computer *"

    * [Data](https://planetarycomputer.microsoft.com/catalog) and processing platform ([Hub](https://planetarycomputer.microsoft.com/compute))
    * Currently available in preview, [request access](https://planetarycomputer.microsoft.com/account/request)
  
=== "Terramonitor"

    [Terramonitor](https://www.terramonitor.com/services/analysis-ready)

    * Pre-prosessed, analysis ready Sentinel-2 data
    * Data from Finland available between 2018-2020
    * [Pricing](https://store.terramonitor.com/category/analysis-ready?6f8e8f38_page=1) 

=== "Sentinelhub *" 

    [Sentinelhub](https://www.sentinel-hub.com/explore/)

    * Worldwide
    * Lots of different EO data sets:
        * [Sentinel-2](https://collections.sentinel-hub.com/sentinel-2-l2a/) 
        * [Sentinel-1](https://collections.sentinel-hub.com/sentinel-1-grd/)
    * Requires [subscription](https://www.sentinel-hub.com/pricing/)

=== "Google Earth Engine * "

    [Google Earh Engine](https://earthengine.google.com/) is a platform for planetary-scale Earth observation data and analysis

    * Usage:
        * [Registration](https://signup.earthengine.google.com/)
        * [From a browser](https://code.earthengine.google.com/)
        * Python: 
            * [API](https://developers.google.com/earth-engine/guides/python_install)
            * [geemap-library](https://geemap.org/)
        * [R-package](https://github.com/r-spatial/rgee)
    * Pros:
        * Great coverage of analysis ready data worldwide
            * [Sentinel-2](https://developers.google.com/earth-engine/datasets/catalog/sentinel-2/)
            * [Sentinel-1](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S1_GRD)
        * rather easy to use, nice tool to test new ideas
        * lots of case studies and tutorials:
            * https://developers.google.com/earth-engine/tutorials
            * https://www.csc.fi/fi/web/training/-/introduction-to-using-google-earth-engine
    
    * Cons:
        * Google Cloud Storage might be needed to export large datasets
        * Not always suitable for small-scale analysis
        * some errors might occur due pre-processing


### Where can I store the data?

What to consider:

* raw vs intermediate vs final result data
    * what needs to be stored?
    * storage space?
* accessibility
    * sensitive data?
    * who needs to have access?
    * how needs the data to be accessed?
    * intended usage?
* maintenance needs?
* metadata needs?

see also: (section about storage solutions in CSC documentation)[../../../data/datasets/hosting-datasets-at-CSC/#what-to-consider-when-choosing-a-suitable-storage-solution]

#### What storage solutions are available at CSC?

=== "During the process"
    
    * For direct access data can be stored on the supercomputer, check out the [different available disk areas](../../../computing/disk)
    * Data can be stored on ```/scratch/project_xxx``` with xxx being your project number
    * Smaller amounts can also be stored short term on the computing nodes ```$LOCAL_SCRATCH``` during processing

=== "Short term storage"

    * [Allas overview](https://research.csc.fi/-/allas)
    * [Allas guide](../../../data/Allas/index.md)

=== "Long term storage"

    * [Paituli](https://research.csc.fi/-/paituli-1)
    * [Fairdata overview](https://www.fairdata.fi/en/user-guide/)
    * [EUDat overview](https://research.csc.fi/-/eudat-services)

=== "Digital preservation"

    * [Fairdata PAS](https://research.csc.fi/-/digital-preservation-service)

See also CSCs general [guide on working with data](../../../data/datasets/dataset-sources.md).

### How can I process the data?

At CSC, EO data can be processed and analyzed using for example supercomputer [Puhti](../../../computing/systems-puhti.md) or a virtual machine in the CSC cloud = [cPouta](../../../cloud/pouta/pouta-what-is/).

Puhti has software ready installed (internal link to below ), you do not need to worry about it. You can also add your own installations using for example the [Tykky tool](../../../computing/containers/tykky/). In cPouta, you need to set up your own virtual machine including all security and software setup, see [instructions](../../../cloud/pouta/launch-vm-from-web-gui/).

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
    * this guide focusses on [software available on CSC supercomputer Puhti](../../../apps/#geosciences) 

##### What software is available at CSC?

* only Linux software

=== "GUI"

    Graphical User Interfaces of software available on Puhti can be accessed as an interactive job via the [Puhti web interface](https://puhti.csc.fi) or [NoMachine or X11 connection](../../../computing/connecting/#using-graphical-applications). These graphical interfaces are mainly for visualization and testing purposes, the actual efficient processing should not be done within interactive jobs.

    ###### [SNAP](https://step.esa.int/main/toolboxes/snap/)

    "All-in-one" Graphical User Interface for processing of Sentinel data (+ support for other data sources) with Python interfaces [snappy](https://senbox.atlassian.net/wiki/spaces/SNAP/pages/19300362/How+to+use+the+SNAP+API+from+Python) and [snapista](https://snap-contrib.github.io/snapista/) and the [Graph Processing Tool](https://step.esa.int/docs/tutorials/SNAP_CommandLine_Tutorial.pdf) as Command Line Interface.

    * [SNAP on Puhti](../../../apps/snap/)

    ###### [QGIS](https://www.qgis.org/en/site/) 

    GIS software with limited multispectral image processing capabilities
    * Visualization
    * [Map making](https://www.qgistutorials.com/en/docs/making_a_map.html)
    * Map algebra / Band math and other [raster processing](https://docs.qgis.org/3.22/en/docs/user_manual/processing_algs/qgis/rasteranalysis.html)
    * [semi-automatic classification plugin](https://fromgistors.blogspot.com/p/semi-automatic-classification-plugin.html) 

    * [QGIS on Puhti](../../../apps/qgis/)

    ###### [Orfeo Toolbox](https://www.orfeo-toolbox.org/)

    Offers a wide variety of applications from ortho-rectification or pansharpening, all the way to classification, SAR processing, and much more!

    Orfeo Toolbox is available as [Command Line Interface](https://www.orfeo-toolbox.org/CookBook/CliInterface.html), [Graphical User Interface](https://www.orfeo-toolbox.org/CookBook/GraphicalInterface.html), Python API and as plugin to other applications.
    
    * GUI (https://www.orfeo-toolbox.org/CookBook/GraphicalInterface.html)


=== "CLI"

    ###### SNAP GPT

    Command Line Interface for [SNAP](../../..//apps/snap/).
    See examples for use of SNAP GPT on Puhti on [github](https://github.com/csc-training/geocomputing/tree/master/snap).

    ###### Sen2Cor

    [Sen2Cor](../../..//apps/sen2cor/) is a stand-alone processor for Sentinel-2 Level 2A product generation and formatting.

    ###### FORCE

    [FORCE](../../../apps/sen2cor/) (Framework for Operational Radiometric Correction for Environmental monitoring) is an all-in-one solution for mass-processing medium-resolution satellite images.

    See examples for use of FORCE on Puhti on [github](https://github.com/csc-training/geocomputing/tree/master/force)

    ###### GDAL (OGR)

    [GDAL](../../../apps/gdal/) (Geospatial Data Abstraction Library) is a geospatial library for accessing and transforming geospatial data. 

    See examples for use of GDAL on Puhti on [github](https://github.com/csc-training/geocomputing/tree/master/gdal)

=== "API"

    ##### Python

    [Geospatial Python on Puhti](../../../apps/geoconda/)

    The geoconda module provides many useful Python packages for multispectral raster data processing and analysis:

    * rasterio: access to geospatial raster data
    * rasterstats: summarizing geospatial raster datasets based on vector geometries
    * sentinelsat: downloading Sentinel images
    * scimage: algorithms for image processing
    * xarray: working with multidimensional raster data
    * dask: scalable analytics

    See examples for use of geopspatial Python on Puhti on [github](https://github.com/csc-training/geocomputing/tree/master/python)

    ##### R

    * [Geospatial R on Puhti](../../../apps/r-env-for-gis/)
    * [Geospatial R course material](https://github.com/csc-training/r-spatial-course)
    * [Examples geospatial R](https://github.com/csc-training/geocomputing/tree/master/R)

    ##### Julia

    [Julia on Puhti](../../../apps/julia/)
    [JuliaGeo](https://github.com/JuliaGeo)    
 
## Help

Help from CSC specialists is available via servicedesk@csc.fi. We are happy to help with technical problems around our services and are open for suggestions on which Software should be installed to Puhti, or what kind of courses should be offered or materials/examples should be prepared.

## Resources

https://step.esa.int/main/doc/tutorials/
https://www.earthdatascience.org/courses/use-data-open-source-python/multispectral-remote-sensing/intro-multispectral-data/ 
https://github.com/sacridini/Awesome-Geospatial

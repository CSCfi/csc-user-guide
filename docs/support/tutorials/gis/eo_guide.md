# Earth Observation guide

This guide aims to help users who wish to work with Earth Observation (EO) data using CSC's computing resources.

The purpose of this guide is to help you find the right data and tools for EO tasks. The basis of this guide is a seminar about the topic held at CSC in 2018 and 2022. And part of the material will also be taught in geospatial training at CSC, check the [training calendar](https://www.csc.fi/training#training-calendar) for dates and topics of upcoming courses. If you encounter any problems or questions come up, CSC's specialists are happy to help with all aspects of your data-driven research, and can be contacted via the CSC Service Desk: `servicedesk@csc.fi`. 

If you are interested in the fundamentals of remote sensing, take a look at these excellent resources:

* [Fundamentals of remote sensing tutorial](https://www.nrcan.gc.ca/maps-tools-and-publications/satellite-imagery-and-air-photos/tutorial-fundamentals-remote-sensing/9309) by Canada Centre for Mapping and Earth Observation , Natural Resources Canada; an "interactive module is intended as an overview at a senior high school or early university level and touches on physics, environmental sciences, mathematics, computer sciences and geography."
* [Echoes in space - Introduction to RADAR remote sensing](https://eo-college.org/courses/echoes-in-space/) by the European Space Agency; "a detailed insight into the history of Radar technology, including all the basics that are needed to understand how electromagnetic waves work and a unique hands-on experience to work with Radar data in diverse application scenarios."
* [Newcomers guide to Earth Observation](https://business.esa.int/newcomers-earth-observation-guide) by the European Space Agency, "a  guide to help non-experts in providing a starting point in the decision process for selecting an appropriate Earth Observation (EO) solution."


## EO data benefits

* Possibility to observe wide area at same time
* Non-intrusive
* Same sensor for different parts of the world
* Time series 

## Most EO data = Raster data

* One file per band or multiband files
* Grid of pixel values
* Example of continuous data
* Georeference: coordinate for the top left pixel , the size of each pixel in the X direction, the size of each pixel in the Y direction, and the amount (if any) by which the product is rotated.

## Using EO data in your research

### What data do I need?

Consider:

* Sensor
    * Optical
        * [Landsat](https://landsat.gsfc.nasa.gov/)
        * [MODIS](https://modis.gsfc.nasa.gov/)
        * [Copernicus Sentinel-2](https://sentinel.esa.int/web/sentinel/missions/sentinel-2)
        * [Pleiades](https://pleiades.cnes.fr/en/PLEIADES/index.htm)
        * [Spot](https://www.intelligence-airbusds.com/imagery/constellation/spot/)
        * [Planet](https://www.planet.com/products/planet-imagery/)
        * [WorldView](http://worldview3.digitalglobe.com/)
        * [Proba-V](https://earth.esa.int/eogateway/catalog/proba-v-1km-333m-and-100m-products)
        * ...
    * RADAR (Radio Detection and Ranging) -> SAR (Synthetic Aperture Radar)
        * [Copernicus Sentinel 1](https://sentinel.esa.int/web/sentinel/missions/sentinel-1)
        * [Radarsat](https://www.asc-csa.gc.ca/eng/satellites/radarsat/)
        * [TanDEM-X](https://www.dlr.de/content/en/missions/tandem-x.html)
        * [TerraSAR-X](https://www.dlr.de/content/en/missions/terrasar-x.html)
        * [ICEYE](https://www.iceye.com/)
        * ...
    * LiDAR (Light Detection and Ranging)
        * [ICESat](https://icesat-2.gsfc.nasa.gov/)
        * [GEDI](https://gedi.umd.edu/)
        * ...
    * Database of all current and future EO missions can be found in the [CEOS EO handbook database](http://database.eohandbook.com/database/missiontable.aspx)
* Resolution
    * Temporal: when and how often a certain area is visited
    * Spatial: the area on the ground that each pixel covers
    * Spectral: the area of the electromagnetic spectrum that is observed and spectral width of each band provided
    * Radiometric: how many values are possible for each pixel (bit-depth)
* Costs
    * Free: e.g. Landsat, MODIS, Sentinel, ...
    * Non free (but might be possible to get for free/less for research): e.g. WorldView, Spot, Planet, ...
* Preprocessing needs
    * Raw or pre-processed 
* User experience and knowledge
    * RADAR/LiDAR require solid background knowledge for processing and interpretation
    * Optical data is more easily interpreted and processed (and more pre-processed data is available)


### Where do I find the data?

The best place to get the data depends on your needs: Do you want to download the data into your own processing environment or do you need a processing environment close to the data? The answer depends on what you want to do with the data and where it is located.

Below is a (uncomplete) set of services, that provide download or download and processing (marked with *) capabilities:

See also a list of other places on [CSC research pages](https://research.csc.fi/open-gis-data#intdata3).

=== "CSC * "

    * Puhti
        * [List of all available datasets in Puhti](../../../data/datasets/spatial-data-in-csc-computing-env.md)
        * Sentinel and Landsat mosaics of Finland provided by FMI and SYKE: ```/appl/data/geo/sentinel/s2```
        * Every CSC user has **read** access to data stored on Puhti, no need to move it, unless you need to modify it
    * Allas
        * [List of all available geospatial datasets in Allas](../../../data/datasets/spatial-data-in-csc-computing-env.md)
        * Sentinel-2 L2A data of crop growing Finland, growing seasons 2016-present, [usage instructions](https://a3s.fi/sentinel-readme/README.txt)
        * Data can be directly read from Allas without download for some cases, see eg [GDAL docs](../../../apps/gdal.md) and [Allas Python examples](https://github.com/csc-training/geocomputing/blob/master/python/allas/working_with_allas_from_Python_S3.py)
        
    
=== "Open Access Hubs"

    [SciHub](https://scihub.copernicus.eu/dhus/#/home)

    * Needs [registration](https://scihub.copernicus.eu/dhus/#/self-registration) 
    * Sentinel 2 L1C and L2A products
    * Sentinel 1 SLC, GRD , RAW and OCN products
    * Worldwide
    * Note: most of the data is in "Long term archive" and cannot be downloaded directly, but needs to be requested

    [FinHub](https://finhub.nsdc.fmi.fi/#/home)

    * Needs [registration](https://nsdc.fmi.fi/services/service_finhub_registration)
    * Sentinel 2 L1C product
    * Sentinel 1 SLC, GRD and OCN products
    * Only Finland (and Baltics)

    [ASF](https://search.asf.alaska.edu/#/)
    
    * Needs [registration](https://urs.earthdata.nasa.gov/users/new?)
    * Sentinel 1 SLC, GRD, RAW, and OCN products
    * Many SAR and SAR derived datasets from other sensors
    * Worldwide
    * Sentinel 1 data available for immediate download
    
    **All of the above** provide a similar Graphical User Interface (GUI) and Application Programming Interface (API) to access the data.
    Other tools for downloading the data from open access hubs: [sentinelsat](https://sentinelsat.readthedocs.io/en/stable/) with [examples for SciHub and FinHub](https://github.com/csc-training/geocomputing/blob/master/python/sentinel/sentinelsat_download_from_finhub_and_scihub.py), ...

=== "USGS EarthExplorer"

    [Earthexplorer](https://earthexplorer.usgs.gov/)

    * Needs [registration](https://ers.cr.usgs.gov/register)
    * Lots of different US related datasets 
    * Main: Landsat worldwide
    * GUI in web interface and bulk download
    * Landsat download instructions: https://lta.cr.usgs.gov/sites/default/files/LS_C2_Help_122020.pdf
    
=== "NASA Earthdata"

    [Earthdata](https://search.earthdata.nasa.gov)
    
    * Needs [registration](https://urs.earthdata.nasa.gov/users/new)
    * Harmonized Landsat 8 and Sentinel-2 dataset and many more
    * Graphical web interface and bulk download

=== "Sentinel image mosaics"

    * Available in Puhti: /appl/data/geo/sentinel
    * Only Finland
    * [Sentinel-2 image index mosaics](https://ckan.ymparisto.fi/dataset/sentinel-2-image-index-mosaics-s2ind-sentinel-2-kuvamosaiikit-s2ind) 
    * [Sentinel-1 SAR-image mosaics](https://ckan.ymparisto.fi/dataset/sentinel-1-sar-image-mosaic-s1sar-sentinel-1-sar-kuvamosaiikki-s1sar)
    * [WMS (Geoserver)](https://data.nsdc.fmi.fi/geoserver/wms)
    * [WCS (Geoserver)](https://data.nsdc.fmi.fi/geoserver/wcs)
    * Provided by [SYKE](https://www.syke.fi/en-US) and [FMI](https://en.ilmatieteenlaitos.fi/)

=== "Google Cloud Storage"

    [Google Cloud Storage](https://cloud.google.com)

    * [Sentinel 2: L1C](https://cloud.google.com/storage/docs/public-datasets/sentinel-2)
    * [Landsat: Collection 1](https://cloud.google.com/storage/docs/public-datasets/landsat)
    * [FORCE](../../../apps/force.md) can download directly from here

=== "Amazon Web Service (AWS) *"

    * Worldwide
    * [Sentinel-2 bucket](https://registry.opendata.aws/sentinel-2/)
    * [Sentinel-1 bucket](https://registry.opendata.aws/sentinel-1/)
    * Requester pays the download costs
    * Managed by [Sinergise](http://www.sinergise.com/) 

=== "DIAS *" 

    * Data and Information Access Services
    * Multiple sites exits:
        * [ONDA](https://www.onda-dias.eu/cms/)
        * [sobloo](https://sobloo.eu/)
        * [CREODIAS](https://creodias.eu/)
        * [MUNDI](https://mundiwebservices.com/)
    * Costs
    * Processing platform with the data, no download needed
    * Data from DIAS objectstorage can easily be transferred to Allas (link to instructions here)
    
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
        * Good coverage of analysis ready data worldwide
            * [Sentinel-2](https://developers.google.com/earth-engine/datasets/catalog/sentinel-2/)
            * [Sentinel-1](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S1_GRD)
        * (Rather easy to use, nice tool to test new ideas)
        * Lots of case studies and tutorials:
            * [GEE tutorials](https://developers.google.com/earth-engine/tutorials)
            * [CSC GEE materials](https://www.csc.fi/fi/web/training/-/introduction-to-using-google-earth-engine)
    
    * Cons:
        * Uncertain long-term availability
        * Google Cloud Storage might be needed to export large datasets
        * Not always suitable for small-scale analysis


> If you plan to work with Sentinel-2 and Landsat 8, check also the 30 m harmonized Landsat 8 and Sentinel-2 product at [NASA](https://hls.gsfc.nasa.gov/).

> Many data providers and companies also provide a Spatio Temporal Asset Catalog (STAC) of their and other datasets. These catalogues help in finding available data based on time and location with the possibility for multiple additional filters, such as cloud cover and resolution. The [STAC Index](https://www.stacindex.org/) provides a nice overview of available catalogues from all over the world. The STAC Index page also includes many resources for learning and utilizing STAC.  

### Where can I store the data?

What to consider:

* Raw vs intermediate vs final result data
    * What needs to be stored?
    * Storage space?
* Accessibility
    * Sensitive data?
    * Who needs to have access?
    * How needs the data to be accessed?
    * Intended usage?
* Maintenance needs?
* Metadata needs?

See also CSC's [guide on how to choose a suitable storage solution](../../../data/datasets/hosting-datasets-at-CSC.md).
    
* In general, data can be stored on the [supercomputer](../../../computing/disk.md) or in the object storage Allas ([Allas overview](https://research.csc.fi/-/allas), [Allas guide](../../../data/Allas/index.md)) 
* On the supercomputer, data can be stored on ```/scratch/project_xxx``` with xxx being your project number
* Smaller amounts can also be stored short term on the computing nodes ```$LOCAL_SCRATCH``` during processing
* In Allas, data is stored in so-called buckets, and can be accessed or transferred as part of the computing job, see also CSC's webinar on [Allas for spatial data](https://www.youtube.com/watch?v=mnFXe2-dJ_g).


> For longer term storage and publication, CSC offers a range of other services. See also CSC's general [guide on stroing data](../../../data/datasets/hosting-datasets-at-CSC.md).


### How can I process the data?

At CSC, EO data can be processed and analyzed using for example supercomputer [Puhti](../../../computing/systems-puhti.md) or a virtual machine in the CSC cloud = [cPouta](../../../cloud/pouta/pouta-what-is.md). You can find more information around geocomputing using CSC resources on our [Geocomputing pages](https://research.csc.fi/geocomputing).

Puhti has a lot of applications already installed (see below), you do not need to worry about it. You can also add your own installations using for example the [Tykky tool](../../../computing/containers/tykky.md). In cPouta, you need to set up your own virtual machine including all security and software setup, see [instructions](../../../cloud/pouta/launch-vm-from-web-gui.md).

#### Software

What to consider:

* User skills and preferences
    * Graphical User Interface (GUI)
    * Command Line Interface (CLI)
    * Scripting
* User needs
    * Batch processing
    * Automation
    * Reproducibility
* Open source vs commercial
    * This guide focusses on [software available on CSC supercomputer Puhti](../../../apps/index.md) 

##### What applications are available on Puhti?

* Only Linux software
* Mostly open source

GUIs of software available on Puhti can be accessed as an interactive job via the [Puhti web interface](https://puhti.csc.fi) or [X11 connection](../../../computing/connecting.md). These graphical interfaces are mainly for visualization and testing purposes, the actual efficient processing should be done within batch jobs rather than interactive jobs.

[**SNAP**](../../../apps/snap.md)

"All-in-one" Graphical User Interface for processing of Sentinel data (+ support for other data sources) with Python interfaces [snappy](https://senbox.atlassian.net/wiki/spaces/SNAP/pages/19300362/How+to+use+the+SNAP+API+from+Python) and [snapista](https://snap-contrib.github.io/snapista/) and the [Graph Processing Tool](https://step.esa.int/docs/tutorials/SNAP_CommandLine_Tutorial.pdf) as Command Line Interface. 

* See examples for use of SNAP GPT on Puhti on [github](https://github.com/csc-training/geocomputing/tree/master/snap).

[**QGIS**](../../../apps/qgis.md)

GIS software with limited multispectral image processing capabilities

* Visualization
* [Map making](https://www.qgistutorials.com/en/docs/making_a_map.html)
* Map algebra / Band math and other [raster processing](https://docs.qgis.org/3.22/en/docs/user_manual/processing_algs/qgis/rasteranalysis.html)
* [Semi-automatic classification plugin](https://fromgistors.blogspot.com/p/semi-automatic-classification-plugin.html) 


[**Orfeo Toolbox (OTB)**](../../../apps/otb.md)

Offers a wide variety of applications from ortho-rectification or pansharpening, all the way to classification, SAR processing, and much more!

Orfeo Toolbox is available as [Command Line Interface](https://www.orfeo-toolbox.org/CookBook/CliInterface.html), [Graphical User Interface](https://www.orfeo-toolbox.org/CookBook/GraphicalInterface.html), Python API and as plugin to other applications.

* GUI (https://www.orfeo-toolbox.org/CookBook/GraphicalInterface.html)

[**Sen2Cor**](../../../apps/sen2cor.md) 

A stand-alone processor for Sentinel-2 Level 2A product generation and formatting with CLI.

[**FORCE**](../../../apps/force.md) 

The Framework for Operational Radiometric Correction for Environmental monitoring is an all-in-one solution for mass-processing medium-resolution satellite images with CLI and GUI.

See examples for use of FORCE on Puhti on [github](https://github.com/csc-training/geocomputing/tree/master/force)

[**GDAL (OGR)**](../../../apps/gdal.md)

The Geospatial Data Abstraction Library is a geospatial library for accessing and transforming geospatial data with CLI and Python package. 

See examples for use of GDAL on Puhti on [github](https://github.com/csc-training/geocomputing/tree/master/gdal)

[**Python**](../../../apps/python.md)

The [geoconda module](../../../apps/geoconda.md) provides - among others - many useful Python packages for raster data processing and analysis:

* *py6s*: Python interface to the Second Simulation of the Satellite Signal in the Solar Spectrum (6S) atmospheric Radiative Transfer Model.
* *rasterio*: access to geospatial raster data.
* *rasterstats*: summarizing geospatial raster datasets based on vector geometries.
* *sentinelsat*: downloading Sentinel images
* *scimage*: algorithms for image processing.
* *stackstac*: STAC data to xarray
* *xarray*: working with multidimensional raster data.

You can find examples of geospatial Python on Puhti on [github](https://github.com/csc-training/geocomputing/tree/master/python). See also raster lesson of CSC version of GeoPython [course material](https://github.com/csc-training/notebooks) for further examples.

[**R**](../../../apps/r-env.md)

All available R packages on Puhti are included in the [r-env module](../../../apps/r-env.md).

* [Geospatial R on Puhti](../../../apps/r-env-for-gis.md)
* [Geospatial R course material](https://github.com/csc-training/r-spatial-course)
* [Examples geospatial R](https://github.com/csc-training/geocomputing/tree/master/R)

[**Julia**](../../../apps/julia.md)

Julia packages can be installed by the user. [JuliaGeo](https://github.com/JuliaGeo) provides an overview of available packages for geospatial data handling.

**Matlab**

[Matlab on Puhti](../../../apps/matlab.md)

### Machine Learning with EO data

One example of the advanced usage of EO data is for machine learning. If you are interested in the topic, you can find a lot of examples using EO and other geospatial data for machine learning in our [Machine learning with spatial data course exercises]( https://github.com/csc-training/GeoML) on Github. 
 
## Where can I get help?

You can find all the ways that you can get help from CSC specialists via our [contact page](../../contact.md).
We are happy to help with technical problems around our services and are open for suggestions on which Software should be installed to Puhti, or what kind of courses should be offered or materials/examples should be prepared. 

## Acknowledgement

This guide was developed in cooperation with the Finnish Environment Institute [SYKE](https://www.syke.fi/), as part of the [Geoportti](https://www.geoportti.fi/) project.

## Resources and further reading

* [ESA tutorials](https://step.esa.int/main/doc/tutorials/)
* [Earthdatascience intro to multispectral data](https://www.earthdatascience.org/courses/use-data-open-source-python/multispectral-remote-sensing/intro-multispectral-data/)
* [Awesome Geospatial](https://github.com/sacridini/Awesome-Geospatial)
* [Awesome EO code](https://github.com/acgeospatial/awesome-earthobservation-code)
* [EO handbook database](http://database.eohandbook.com/)

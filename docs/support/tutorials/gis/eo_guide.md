# Earth Observation guide

This guide aims to help users to work with Earth Observation (EO) data using CSC's computing resources. The purpose of this guide is to help you find the right data and tools for your raster data based EO tasks. If you are interested in the fundamentals of EO, please check the resources at the bottom of the page.

**What are the benefits of using EO data**

* Possibility to observe wide area at same time
* Non-intrusive
* Same sensor for different parts of the world
* Time series 

!!! default "Raster data format"

Most EO data is available in [raster format]( 
https://towardsdatascience.com/the-ultimate-beginners-guide-to-geospatial-raster-data-feb7673f6db0). The most common file formats are [GeoTiff](https://en.wikipedia.org/wiki/GeoTIFF) and [GeoJPEG2000](http://giswiki.org/wiki/GeoJPEG2000).


## What data do I need?

What to consider when chosing data:

* Sensor
    * Optical, Multispectal: [Landsat](https://landsat.gsfc.nasa.gov/), [MODIS](https://modis.gsfc.nasa.gov/), [Copernicus Sentinel-2](https://sentinel.esa.int/web/sentinel/missions/sentinel-2),[Pleiades](https://pleiades.cnes.fr/en/PLEIADES/index.htm), [Spot](https://www.intelligence-airbusds.com/imagery/constellation/spot/), [Planet](https://www.planet.com/products/planet-imagery/), [WorldView](http://worldview3.digitalglobe.com/), [Proba-V](https://earth.esa.int/eogateway/catalog/proba-v-1km-333m-and-100m-products), ...
    * RADAR (Radio Detection and Ranging) -> SAR (Synthetic Aperture Radar): [Copernicus Sentinel 1](https://sentinel.esa.int/web/sentinel/missions/sentinel-1), [Radarsat](https://www.asc-csa.gc.ca/eng/satellites/radarsat/), [TanDEM-X](https://www.dlr.de/content/en/missions/tandem-x.html), [TerraSAR-X](https://www.dlr.de/content/en/missions/terrasar-x.html), [ICEYE](https://www.iceye.com/),...
    * LiDAR (Light Detection and Ranging): [ICESat](https://icesat-2.gsfc.nasa.gov/), [GEDI](https://gedi.umd.edu/), ...
* Resolution
    * Temporal: when and how often a certain area is visited
    * Spatial: the area on the ground that each pixel covers
    * Spectral: the area of the electromagnetic spectrum that is observed and spectral width of each band provided
        * Depending on the wavelengths observed,  clouds and atmospheric artifacts may result in data gaps
    * Radiometric: how many values are possible for each pixel (bit-depth)
* Costs
    * Free: e.g. Landsat, MODIS, Sentinel, ...
    * Non free (but might be possible to get for free/less for research): e.g. WorldView, Spot, Planet, ...
* Preprocessing level
    * Raw data
    * Analysis ready data 
    * Mosaics
* User experience and knowledge
    * RADAR/LiDAR require solid background knowledge for processing and interpretation
    * Optical data is more easily interpreted and processed (and more pre-processed data is available)

!!! default "EO database"

    Database of all current and future EO missions and instrument information can be found in the [CEOS EO handbook database](http://database.eohandbook.com/database/instrumenttable.aspx)

## Where can I find the data?

For working with EO data there are two main options:
* Use a service which has EO data readily available and offers data processing and analysis capabilities. Usually these give better user experience and efficiency, but the services might be limited in computing power, available tools or options for adding own data. The commercial systems also might have costs.
* Use your own processing environment (PC, cloud or HPC) and download the data to this system. This requires extra effort for downloading and managing the data, but in other ways might give more freedom.

!!! default "Other geospatial datasets"

    To find other geospatial datasets, check out [CSC open spatial dataset list](https://research.csc.fi/open-gis-data).

### Services providing EO data and processing capabilities

**CSC services**

* Puhti
    * [List of all available datasets in Puhti](../../../data/datasets/spatial-data-in-csc-computing-env.md)
    * Sentinel and Landsat mosaics of Finland provided by FMI and SYKE: ```/appl/data/geo/sentinel/s2```
    * Accessing data in Puhti requires CSC user account with a project where Puhti service is enabled. All Puhti users have **read** access to data stored on Puhti, no need to move it, unless you need to modify it.
* Allas
    * [List of all available geospatial datasets in Allas](../../../data/datasets/spatial-data-in-csc-computing-env.md#spatial-data-in-allas)
    * Sentinel-2 L2A data of Finland, where crops are grown, during growing seasons of 2016-present, [usage instructions](https://a3s.fi/sentinel-readme/README.txt)
    * [Data from Allas can be read directly with different tools](../../../apps/gdal.md#using-files-directly-from-allas).
        
    
**[Amazon Web Service (AWS) open EO data](https://registry.opendata.aws/?search=tags:gis,earth%20observation,events,mapping,meteorological,environmental,transportation)** provides many different worldwide datasets, including Landsat and Sentinel. Some of the data can be downloaded on "requestor pays" basis. The situation is changing all the time, currently [Sentinel-2 L2A Cloud-optimized Geotiffs](https://registry.opendata.aws/sentinel-2-l2a-cogs/) are available for free. AWS also offers the possibility for virtual machines, with both CPU and GPU.

**[Data and Information Access Services (DIAS)](https://www.copernicus.eu/en/access-data/dias)** are paid processing platforms with direct data access. The services provide primarily Copernicus data.
    
**[Microsoft planetary computer](https://planetarycomputer.microsoft.com)** provides [worldwide EO data](https://planetarycomputer.microsoft.com/catalog). For [computing](https://planetarycomputer.microsoft.com/docs/concepts/computing/) it offers JupyterHub together with Dask Gateway, both CPUs and GPUs are avaialable. It is currently available in preview: [request access to the planetary computer](https://planetarycomputer.microsoft.com/account/request).

**[Google Earth Engine](https://earthengine.google.com/)** is a processing platform, which requires [registration](https://signup.earthengine.google.com/). It can be accessed via browser and has worldwide analysis ready data available of, among others [Sentinel-2](https://developers.google.com/earth-engine/datasets/catalog/sentinel-2/) and [Sentinel-1](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S1_GRD). In general JavaScript is used to use the platform, but also [Python](https://developers.google.com/earth-engine/guides/python_install) and [R](https://github.com/r-spatial/rgee) support exists. Check out [GEE's tutorials](https://developers.google.com/earth-engine/tutorials). Note that Google Cloud Storage might be needed to export large datasets.

### EO data download services 

[**European Space Agency's SciHub**](https://scihub.copernicus.eu/dhus/#/home) provides worldwide Sentinel 2 L1C and L2A and Sentinel 1 SLC, GRD , RAW and OCN products. It requires free [registration](https://scihub.copernicus.eu/dhus/#/self-registration) and many of the data is in "Long term archive" and cannot be downloaded directly, but needs to be requested. Download is limited to 2 concurrent processes per user.

[**FinHub**](https://finhub.nsdc.fmi.fi/#/home) is the Finnish national mirror of SciHub; others national mirrors also exist. It covers Finland and the Baltics and offers Sentinel 2 L1C (but not L2A) and Sentinel 1 SLC, GRD and OCN products and requires own registration. Finhub does not have concurrent download limitations.

!!! default  ""  
    **Both of the above** provide a similar Graphical User Interface (GUI) and Application Programming Interface (API) to access the data. Other tools for downloading the data from open access hubs: [sentinelsat](https://sentinelsat.readthedocs.io/en/stable/) with [examples for SciHub and FinHub](https://github.com/csc-training/geocomputing/blob/master/python/sentinel/sentinelsat_download_from_finhub_and_scihub.py), ...


[**USGS EarthExplorer**](https://earthexplorer.usgs.gov/) provides lots of different US related datasets, also worldwide Landsat mission datasets. It requires free [registration](https://ers.cr.usgs.gov/register). Data can be browsed and downloaded via GUI in web interface and bulk download.
    
[**NASA Earthdata**](https://search.earthdata.nasa.gov) provides among many others harmonized Landsat 8 and Sentinel-2 dataset. It requires [registration](https://urs.earthdata.nasa.gov/users/new) and download is possible via Graphical web interface and bulk download.

**Finnish Sentinel image mosaics** are provided by  [SYKE](https://www.syke.fi/en-US) and [FMI](https://en.ilmatieteenlaitos.fi/) and partly available in Puhti: `/appl/data/geo/sentinel`. Among others, [Sentinel-2 image index mosaics](https://ckan.ymparisto.fi/dataset/sentinel-2-image-index-mosaics-s2ind-sentinel-2-kuvamosaiikit-s2ind)  and [Sentinel-1 SAR-image mosaics](https://ckan.ymparisto.fi/dataset/sentinel-1-sar-image-mosaic-s1sar-sentinel-1-sar-kuvamosaiikki-s1sar) are available.

[**Google Cloud Storage**](https://cloud.google.com) provides [Sentinel 2: L1C](https://cloud.google.com/storage/docs/public-datasets/sentinel-2)
 and [Landsat: Collection 1](https://cloud.google.com/storage/docs/public-datasets/landsat). Data can be downloaded from here for example with [FORCE](../../../apps/force.md).

[**Terramonitor**](https://www.terramonitor.com/services/analysis-ready) provides pre-prosessed, analysis ready Sentinel-2 data from Finland available between 2018-2020.[Contact Terramonitor about pricing](https://www.terramonitor.com/services/analysis-ready#contact)

[**Sentinelhub**](https://www.sentinel-hub.com/explore/) provides among others worldwide [Sentinel-2](https://collections.sentinel-hub.com/sentinel-2-l2a/) and [Sentinel-1](https://collections.sentinel-hub.com/sentinel-1-grd/) data. Requires [subscription](https://www.sentinel-hub.com/pricing/).

!!! default "STAC"

    Many data providers and companies also provide a Spatio Temporal Asset Catalog (STAC) of their and other datasets. These catalogues help in finding available data based on time and location with the possibility for multiple additional filters, such as cloud cover and resolution. The [STAC Index](https://www.stacindex.org/) provides a nice overview of available catalogues from all over the world. The STAC Index page also includes many resources for learning and utilizing STAC. Check out also CSC's [examples for utilizing STAC from Python](https://github.com/csc-training/geocomputing/blob/master/python/STAC).

## Where can I store the data?

What to consider when chosing a storage location:

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

In general, data can be stored on the [supercomputer disk](../../../computing/disk.md) or in the object storage Allas ([Allas overview](https://research.csc.fi/-/allas), [Allas guide](../../../data/Allas/index.md)). On the supercomputer, data can be stored on ```/scratch/project_xxx``` with xxx being your project number. Smaller amounts can also be stored short term on the computing nodes ```$LOCAL_SCRATCH``` during processing. In Allas, data is stored in so-called buckets, and can be accessed or transferred as part of the computing job, see also CSC's webinar on [Allas for spatial data](https://www.youtube.com/watch?v=mnFXe2-dJ_g).

!!! default "Longer term storage solutions at CSC"

    For longer term storage and publication, CSC offers a range of other services. See also CSC's general [guide on stroing data](../../../data/datasets/hosting-datasets-at-CSC.md) and CSC's [guide on how to choose a suitable storage solution](../../../data/datasets/hosting-datasets-at-CSC.md).


## How can I process the data?

At CSC, EO data can be processed and analyzed using for example [supercomputer Puhti](../../../computing/systems-puhti.md) or a virtual machine in the CSC cloud, [cPouta](../../../cloud/pouta/pouta-what-is.md). You can find more information around geocomputing using CSC resources on our [Geocomputing pages](https://research.csc.fi/geocomputing).

Puhti has a lot of applications already installed (see below), you do not need to worry about it. If you need further applications, you can ask us to install them for you. You can also add your own installations using for example the [Tykky tool](../../../computing/containers/tykky.md).   In cPouta, you need to set up your own virtual machine including all security and software setup, see [our cPouta instructions](../../../cloud/pouta/launch-vm-from-web-gui.md).

!!! default "Please note"

    Puhti (and also CSC's other supercomputers Mahti and LUMI), work differently from your own computer. Before starting to use them, please familiarize yourself with the environment by for example visit the respective chapters in our [CSC computing environment self-learning course](https://ssl.eventilla.com/csccompenvselflearn).

What to consider when chosing software:

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

### What applications are available on Puhti?

To Puhti, only Linux based software can be installed. Most of the installed geospatial tools are open source.

GUIs of software available on Puhti can be accessed as an interactive job via the [Puhti web interface](https://puhti.csc.fi) or [X11 connection](../../../computing/connecting.md). These graphical interfaces are mainly for visualization and testing purposes, the actual efficient processing should be done within batch jobs.


[**FORCE**](../../../apps/force.md) - Framework for Operational Radiometric Correction for Environmental monitoring

* All-in-one processing engine with CLI for EO image archives 
* [FORCE example for Puhti](https://github.com/csc-training/geocomputing/tree/master/force)

[**GDAL (OGR)**](../../../apps/gdal.md) - Geospatial Data Abstraction Library

* Collection of command-line tools for accessing and transforming geospatial data 
* [GDAL example for Puhti](https://github.com/csc-training/geocomputing/tree/master/gdal)

[**Julia**](../../../apps/julia.md)

* Julia is provided via the `Julia` module, it does not include any packages, but they can be installed by the user. 
* [JuliaGeo](https://github.com/JuliaGeo) provides an overview of packages for geospatial data.

[**Matlab**](../../../apps/matlab.md)

* You can run Matlab jobs on Puhti conveniently from your own computers Matlab installation.

[**Orfeo Toolbox (OTB)**](../../../apps/otb.md)

* Offers a wide variety of applications from ortho-rectification or pansharpening, all the way to classification, SAR processing, and much more.
* Orfeo Toolbox is available as CLI, GUI and via Python interface.


[**Python**](../../../apps/python.md)

* The [geoconda module](../../../apps/geoconda.md) provides many useful Python packages for raster data processing and analysis:

    * py6s: Python interface to the Second Simulation of the Satellite Signal in the Solar Spectrum (6S) atmospheric Radiative Transfer Model.
    * rasterio: access to geospatial raster data.
    * rasterstats: summarizing geospatial raster datasets based on vector geometries.
    * sentinelsat: downloading Sentinel images
    * scimage: algorithms for image processing.
    * stackstac: STAC data to xarray
    * xarray: working with multidimensional raster data.

* [Geospatial Python examples for Puhti](https://github.com/csc-training/geocomputing/tree/master/python). See also raster lesson of CSC version of GeoPython [course material](https://github.com/csc-training/notebooks) for further examples.


[**QGIS**](../../../apps/qgis.md)

* General Geographic Information System (GIS) with limited multispectral image processing capabilities
* GUI with batch processing possibility and Python interface
* Used for example for [visualization](https://www.qgistutorials.com/en/docs/making_a_map.html) and [map algebra and other raster processing](https://docs.qgis.org/3.22/en/docs/user_manual/processing_algs/qgis/rasteranalysis.html)
* Many plug-ins available, for EO data processing, check out the [Semi-automatic classification plugin](https://fromgistors.blogspot.com/p/semi-automatic-classification-plugin.html).

[**R**](../../../apps/r-env-for-gis.md)

* All R packages are provided in `r-env` module, including many that can be used for EO data processing, such as terra, CAST, raster, spacetime.

[**Sen2Cor**](../../../apps/sen2cor.md)

* A command-line tool for Sentinel-2 Level 2A product generation and formatting.

[**Sen2mosaic**](../../../apps/sen2cor.md)

* A command-line tool to download, preprocess and mosaic Sentinel-2 data.

[**SNAP**](../../../apps/snap.md) - ESA Sentinel Application Platform

* Tool for processing of Sentinel data (+ support for other data sources) 
* GUI, CLI (Graph Processing Tool, GPT) and Python interfaces (snappy and snapista (snapista currently not available on Puhti))
* [SNAP GPT example for Puhti](https://github.com/csc-training/geocomputing/tree/master/snap).

### Machine Learning with EO data

One example of the advanced usage of EO data is for machine learning. If you are interested in the topic, you can find a lot of examples using EO and other geospatial data for machine learning in our [Machine learning with spatial data course exercises]( https://github.com/csc-training/GeoML) on Github. 
 
## Where can I get help?

If you are interested in using CSC services for your EO research, please make yourself familiar with the services:

* Visit a course, seminar or workshop; you can find all upcoming and past events in [the CSC training calendar](https://www.csc.fi/en/training#training-calendar)
    * For getting familiar and started with CSCs environment, check out the [self learning CSC computing environment material](https://ssl.eventilla.com/csccompenvselflearn)
* Find information about services and how to use them in [CSC's documentation pages](../../../index.md)
* For information on geocomputing in CSC environment, checkout the collection of CSC's [geocomputing learning materials](https://research.csc.fi/gis-learning-materials) and [geocomputing examples on github](https://github.com/csc-training/geocomputing)

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
* [CSC geocomputing seminar materials](https://research.csc.fi/geocomputing-seminars), especially materials of the 2022 EO-workshop


If you are interested in the fundamentals of EO, take a look at these excellent resources:

* [Fundamentals of remote sensing tutorial](https://www.nrcan.gc.ca/maps-tools-and-publications/satellite-imagery-and-air-photos/tutorial-fundamentals-remote-sensing/9309) by Canada Centre for Mapping and Earth Observation , Natural Resources Canada; an "interactive module is intended as an overview at a senior high school or early university level and touches on physics, environmental sciences, mathematics, computer sciences and geography."
* [Echoes in space - Introduction to RADAR remote sensing](https://eo-college.org/courses/echoes-in-space/) by the European Space Agency; "a detailed insight into the history of Radar technology, including all the basics that are needed to understand how electromagnetic waves work and a unique hands-on experience to work with Radar data in diverse application scenarios."
* [Newcomers guide to Earth Observation](https://business.esa.int/newcomers-earth-observation-guide) by the European Space Agency, "a  guide to help non-experts in providing a starting point in the decision process for selecting an appropriate Earth Observation (EO) solution."
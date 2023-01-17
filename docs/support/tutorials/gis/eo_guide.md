# Earth Observation guide

This guide aims to help researchers to work with Earth Observation (EO) data using CSC's computing resources. The purpose of this guide is to give an overview of available options, so it would be easier to decide if CSC has suitable services for your your EO reseach. It also helps you find the right data and tools for raster data based EO tasks. If you are interested in the fundamentals of EO, please check the [resources and further reading section](#resources-and-further-reading).

**What are the benefits of using EO data?**

* Possibility to observe wide areas at same time
* Non-intrusive, cost-efficient
* Same sensor for different parts of the world, easy to compare different areas
* Time series to see changes during different seasons and years

## Why should I use CSC computing resources for EO?

For working with EO data there are in general three main options:

1) **Special EO services**, which provide both data and advanced ready-to-use processing environments. Usually these give better user experience and efficiency, but the services might be limited in computing power, available tools or options for adding own data. Often these have fees for using.
2) **Commercial clouds** with local copy of open EO data. The data is practically always saved to object-storage and usually can be downloaded from anywhere as independent service. They provide also general computing services where EO data analysis tools need to be installed by the end-user. The most common option for processing in the cloud are virtual machines. These options usually have some fees, mainly for processing. The data download may be free of charge or then have some small costs depending on the amount of data needed. Data download costs might be smaller if using virtual machines of the same cloud provider in the same region.
3) **Own processing environment** - PC, local cluster. All data needs to be downloaded to this system and all tools must be installed, which requires extra effort. On the other hand it gives more freedom to select the tools and set-up. Usually this does not cause any extra costs, but the computing power is usually rather limited.

CSC options do not fit well in this categorization, rather they have some features from all of these. **CSC computing services provide a lot of computing power and storage space, and they are free of charge** for Finnish researchers for academic or educational use. 

At CSC, EO data can be processed and analyzed using [supercomputer Puhti](../../../computing/systems-puhti.md) or a virtual machine in the [cPouta cloud service](../../../cloud/pouta/pouta-what-is.md). Puhti's computing capacity can hardly be compared to any other EO service, in both available cores and amount of memory. Both Puhti and cPouta have also GPU resources, which are especially useful for deep learning use cases. 

Puhti has also a lot of [pre-installed applications](#what-applications-are-available-on-puhti), so it is an environment ready to use. cPouta virtual machines are similar to commercial cloud offerings, there all set-up is done by the end-user.  In both services, it is only possible to install tools that support Linux.

At CSC, are available only [some Finnish datasets](#eo-data-at-csc), so often working with CSC comptuing services requires to download EO data from other services, see [list of EO data download services](#eo-data-download-services). The available local storage in Puhti and cPouta is ~1-20 Tb, more space is available from [Allas object storage](../../../data/Allas/index.md).

Using CSC computing services is technically a little bit demanding, requiring basic Linux skills and ability to use some scripting language or command-line tools. Supercomputers and virtual machines have several specific consepts, so it takes a few hours to get started. The new Puhti web interface makes the start considerably easier, providing several graphical tools. It has also Studio and JupyterLab for easy start with R or Python.

## What data do I need?

What to consider when chosing data:

* Sensor
    * Optical
    * Multispectal
    * Hyperspectral
    * RADAR (Radio Detection and Ranging) -> SAR (Synthetic Aperture Radar)
    * LiDAR (Light Detection and Ranging)
* Resolution
    * Temporal: when and how often a certain area is visited
    * Spatial: the area on the ground that each pixel covers
    * Spectral: the area of the electromagnetic spectrum that is observed and spectral width of each band provided
        * Depending on the wavelengths observed,  clouds and atmospheric artifacts may result in data gaps
    * Radiometric: how many values are possible for each pixel (bit-depth)
* Costs:
    * Some EO data is available as open data
    * Some commercial datasets might be possible to get for free/less for research
* Preprocessing level
    * Raw data
    * Analysis ready data 
    * Mosaics
* User experience and knowledge
    * RADAR/LiDAR require solid background knowledge for processing and interpretation
    * Optical data is more easily interpreted and processed (and more pre-processed data is available)

### Some widely used EO datasets

|Name|Max resolution, m|Revisit time, days|Years of operation|Open data|
|--------------|------------|-----|---------|---------|
|**Optical, multispectral**|
|**[ESA, Sentinel-2](https://sentinel.esa.int/web/sentinel/missions/sentinel-2)**|10-60|5|2015->|Yes|
|**[NASA, Landsat](https://landsat.gsfc.nasa.gov/)**|15-120|8|1972->|Yes|
|[ESA, Proba-V](https://earth.esa.int/eogateway/catalog/proba-v-1km-333m-and-100m-products)|100-1000|1-2|2013->|Yes|
|[Airbus, Spot](https://www.intelligence-airbusds.com/imagery/constellation/spot/)|1.5|-|1986->|No|
|[Planet, several satellites ](https://www.planet.com/products/planet-imagery/)|0.5-5|-|2009-> |No|
|[DigitalGlobe, WorldView](http://worldview3.digitalglobe.com/)|0.3-30|-|1997->|No|
|[Airbus, Pleiades](https://pleiades.cnes.fr/en/PLEIADES/index.htm)|0.3-0.5|-|2012->|No|
||||||
|**Hyperspectral**|||||
|**[NASA, MODIS](https://modis.gsfc.nasa.gov/)**|250-100|1-2|1999->|Yes|
|[NASA, EO-1](https://www.usgs.gov/centers/eros/science/earth-observing-1-eo-1)|10-30|-|2000-2017|Yes|
||||||
|**Radar, SAR**|||||
|**[ESA, Sentinel 1](https://sentinel.esa.int/web/sentinel/missions/sentinel-1)**|5|6|2014->|Yes|
|[ESA, Radarsat](https://www.asc-csa.gc.ca/eng/satellites/radarsat/)|1-100|24|1995->|Yes|
|[TanDEM-X](https://www.dlr.de/content/en/missions/tandem-x.html)/[TerraSAR-X](https://www.dlr.de/content/en/missions/terrasar-x.html)|0.25-40|-|2010->|No|
|[ICEYE](https://www.iceye.com/)|0.5-2.5|1|2018->|No|
||||||
|**LiDAR**|Footprint size||||
|[NASA, ICESat2](https://icesat-2.gsfc.nasa.gov/)|13|91|2019->|Yes|
|[NADA, GEDI](https://gedi.umd.edu/)|25|-|2018->|Yes|

!!! default "EO database"

    Database of all EO missions and instrument information can be found in the [CEOS EO handbook database](http://database.eohandbook.com/database/instrumenttable.aspx)
    
  

## Where can I find the data?

The commercial data is usually available from data provider, the open datasets have several copies in different services. Usually it is good to use data close to the processing, for speeding up the download. For bigger downloads it is important that services have a download API.

!!! default "STAC"

    Many data providers provide a Spatio Temporal Asset Catalog (STAC) of their datasets. These catalogues help in finding available data based on time and location with the possibility for multiple additional filters, such as cloud cover and resolution. The [STAC Index](https://www.stacindex.org/) provides a nice overview of available catalogues from all over the world. The STAC Index page also includes many resources for learning and utilizing STAC. Check out also CSC's [examples for utilizing STAC from Python](https://github.com/csc-training/geocomputing/blob/master/python/STAC).

### EO data at CSC

Some Finnish EO datasets are available locally at CSC. STAC for data at CSC is coming in 2023.

* **Sentinel and Landsat mosaics** of Finland in Puhti. Accessing data in Puhti requires CSC user account with a project where Puhti service is enabled. All Puhti users have **read** access to public data stored on Puhti. For using these files, you do not need to copy them, unless you need to modify them.
* **Sentinel-2 L2A data** of Finland in Allas. Allas files are public, so anybody can download them, also from local laptop or from other services.
* [More information and list of all spatial datasets in CSC computing environment](../../../data/datasets/spatial-data-in-csc-computing-env.md)

### EO data download services  

**[SYKE/FMI, Finnish image mosaics](https://www.syke.fi/fi-FI/Tutkimus__kehittaminen/Tutkimus_ja_kehittamishankkeet/Hankkeet/Paikkatietoalusta_PTA)** Mosaics are available both for Sentinel 1 and 2, and Landsat, for several time periods per year. Some of them are available in Puhti, but not all. [FMI has also STAC catalog for these mosaics](https://pta.data.lit.fmi.fi/stac/root.json)

[**European Space Agency's SciHub**](https://scihub.copernicus.eu/dhus/#/home) provides worldwide all main products for Sentinel 1, 2 and 3. It requires free registration. Big part of the data is in the "Long term archive" and cannot be downloaded directly, but needs to be requested. Download is limited to 2 concurrent processes per user.

[**FinHub**](https://finhub.nsdc.fmi.fi/#/home) is the Finnish national mirror of SciHub; others national mirrors also exist. It covers Finland and the Baltics and offers Sentinel 2 L1C (but not L2A) and Sentinel 1 SLC, GRD and OCN products and requires own registration. Finhub does not have concurrent download limitations nor "Long term archive".

!!! default  ""  
    **Both of the above** provide a similar Graphical User Interface (GUI) and Application Programming Interface (API) to access the data. You can also use for example the [sentinelsat](https://sentinelsat.readthedocs.io/en/stable/) tool for downloading data from ESA open access hubs. See also [CSC examples for SciHub and FinHub data download](https://github.com/csc-training/geocomputing/blob/master/python/sentinel/sentinelsat_download_from_finhub_and_scihub.py). STAC catalog will be available for Scihub data during 2023.
    
[**USGS EarthExplorer**](https://earthexplorer.usgs.gov/) provides lots of different US related datasets, also worldwide Landsat mission datasets. It requires free registration. Data can be browsed and downloaded via web interface and bulk download. USGS is the prime provider of the new [Landsat Collection 2 data](https://www.usgs.gov/landsat-missions/landsat-data-access).
    
[**NASA Earthdata**](https://search.earthdata.nasa.gov) provides among many others [harmonized Landsat 8 and Sentinel-2 dataset](https://hls.gsfc.nasa.gov/). It requires free registration and download is possible via web interface and bulk download.

**[Amazon Web Service (AWS) open EO data](https://registry.opendata.aws/?search=tags:gis,earth%20observation,events,mapping,meteorological,environmental,transportation)** is a collection of worldwide EO datasets provided by different organizations, including Landsat and Sentinel. Some of the data can be downloaded only on "requestor pays" basis. The situation is changing all the time, currently [Sentinel-2 L2A Cloud-optimized Geotiffs](https://registry.opendata.aws/sentinel-2-l2a-cogs/) are available for free, also via STAC. 

**[Microsoft planetary computer](https://planetarycomputer.microsoft.com)**: Sentinel, Landsat, MODIS etc. STAC available. It is currently available in preview.

[**Google Cloud Storage open EO data**](https://cloud.google.com/storage/docs/public-datasets), including Sentinel-2 L1C and Landsat: Collection 1 data. Data can be downloaded from here for example with [FORCE](../../../apps/force.md).
    
[**Terramonitor**](https://www.terramonitor.com/services/analysis-ready) provides pre-prosessed, analysis ready Sentinel-2 data from Finland available between 2018-2020. Commercial service.

!!! default "Other geospatial datasets"

    To find other geospatial datasets, check out [CSC open spatial dataset list](https://research.csc.fi/open-gis-data).  


## How can I process EO data at CSC?

You can find more information about geocomputing using CSC resources and how to get started on [CSC geocomputing pages](https://research.csc.fi/geocomputing), including links to creating user accounts and all other practical information. 

### What applications are available on Puhti?

[**FORCE**](../../../apps/force.md) - Framework for Operational Radiometric Correction for Environmental monitoring. All-in-one processing engine with CLI for EO image archives. [FORCE example for Puhti](https://github.com/csc-training/geocomputing/tree/master/force)

[**GDAL (OGR)**](../../../apps/gdal.md) - Geospatial Data Abstraction Library.  Collection of command-line tools for accessing and transforming geospatial data, relatively fast and require little computational resources. GDAL support reading data directly from Internet or object storage. GDAL is included in many other tools for data reading and writing. [GDAL example for Puhti](https://github.com/csc-training/geocomputing/tree/master/gdal)

[**Julia**](../../../apps/julia.md) - Puhtis Julia installation does not include any geospatial packages, but they can be installed by the user. [JuliaGeo](https://github.com/JuliaGeo) provides an overview of packages for geospatial data.

[**Matlab**](../../../apps/matlab.md) - you can run Matlab jobs on Puhti conveniently from your own computers Matlab installation.

[**Orfeo Toolbox (OTB)**](../../../apps/otb.md) - offers a wide variety of applications from ortho-rectification or pansharpening, all the way to classification, SAR processing, and much more. Orfeo Toolbox is available as CLI, GUI and via Python interface.


[**Python**](../../../apps/python.md)

* The [geoconda module](../../../apps/geoconda.md) provides many useful Python packages for raster data processing and analysis, inc best tools for working with STAC catalogues.
* [Machine learning modules](../../../apps/index.md#data-analytics-and-machine-learning) provide all common machine learning frameworks, also for deep learning.


[**QGIS**](../../../apps/qgis.md) - is a very widely used GUI for working with spatial data, it has also limited multispectral image processing capabilities.  GUI with batch processing possibility and Python interface. Used for example for visualization, map algebra and other raster processing. Many plug-ins available, for EO data processing, check out the [QGIS Semi-automatic classification plugin](https://fromgistors.blogspot.com/p/semi-automatic-classification-plugin.html).

[**R**](../../../apps/r-env-for-gis.md) - Puhti R installation includes a lot of geospatial packages, includeing serveral useful for EO data processing.

[**Sen2Cor**](../../../apps/sen2cor.md) - a command-line tool for Sentinel-2 Level 2A product generation and formatting.

[**Sen2mosaic**](../../../apps/sen2cor.md) - a command-line tool to download, preprocess and mosaic Sentinel-2 data.

[**SNAP**](../../../apps/snap.md) - ESA Sentinel Application Platform. Tool for processing of Sentinel data (+ support for other data sources). GUI, CLI (Graph Processing Tool, GPT) and Python interfaces. [SNAP GPT example for Puhti](https://github.com/csc-training/geocomputing/tree/master/snap).

If you need further applications, you can ask CSC to install them for you. 
 
### Machine Learning with EO data

One example of the advanced usage of EO data is for machine learning. If you are interested in the topic, you can find a lot of examples from [CSC machine learning with spatial data course materials]( https://github.com/csc-training/GeoML). For practical guidelines, see also [CSC machine learning guide](../ml-guide.md)


## Alternative processing services
Below is a list of alternative EO processing services that might be useful, when a lot of data is required and downloading it all to CSC might not be feasible. All of them include the main open datasets: Sentinel, Landsat, MODIS etc.

**[Google Earth Engine](https://earthengine.google.com/)** is a processing platform, which requires registration, but is free of charge for research users. It can be accessed via browser and has worldwide analysis ready data available (<a href="https://developers.google.com/earth-engine/datasets/catalog/" aria-label="GEE data catalogue">browse the catalogue</a>). In general, JavaScript is used on the platform, but also  <a href="https://developers.google.com/earth-engine/guides/python_install" aria-label="Python on GEE">Python</a>  and  <a href="https://github.com/r-spatial/rgee" aria-label="R on GEE">R</a> support exists. Check out [GEE's tutorials](https://developers.google.com/earth-engine/tutorials). Note that Google Cloud Storage might be needed to export large datasets.

**[Microsoft planetary computer](https://planetarycomputer.microsoft.com)**. For computing it offers JupyterHub together with Dask Gateway, both CPUs and GPUs are available. It is currently available in preview.

 **[Data and Information Access Services (DIAS)](https://www.copernicus.eu/en/access-data/dias)** cloud based Virtual Machines (VMs), dedicated baremetal servers, containers, operating system and software images. Specialized in EO, user support available. Commercial services. 
 
[**Sentinelhub**](https://www.sentinel-hub.com/explore/). Several different APIs. Commercial service.

**Commercial clouds**: Amazon, Google Cloud and Microsoft Azure, all provide virtual machines and other processing services, all of them have some local data, see links above. No EO support.
 
## Where can I get help?

If you are interested in using CSC services for your EO research, please make yourself familiar with the services:

* Visit a course, seminar or workshop; you can find all upcoming and past events in [the CSC training calendar](https://www.csc.fi/en/training#training-calendar)
    * For getting started, go through [CSC Computing Environment - Self Learning course](https://ssl.eventilla.com/csccompenvselflearn)
* Find information about services and how to use them in [CSC's documentation pages](../../../index.md)
* For information on geocomputing in CSC environment, checkout the collection of  [CSC's geocomputing learning materials](https://research.csc.fi/gis-learning-materials) and [CSC geocomputing examples on Github](https://github.com/csc-training/geocomputing)

You can find all the ways that you can get help from CSC specialists via [CSC contact page](../../contact.md). We are happy to help with technical problems around our services and are open for suggestions on which software should be installed to Puhti, or what kind of courses should be offered or materials/examples should be prepared. 

## Acknowledgement

This guide was developed in cooperation with the [Finnish Environment Institute, SYKE](https://www.syke.fi/), as part of the [Geoportti project](https://www.geoportti.fi/).

## Resources and further reading

If you are interested in the fundamentals of EO, take a look at these excellent resources:

* [Fundamentals of remote sensing tutorial](https://www.nrcan.gc.ca/maps-tools-and-publications/satellite-imagery-and-air-photos/tutorial-fundamentals-remote-sensing/9309) by Canada Centre for Mapping and Earth Observation , Natural Resources Canada; an "interactive module is intended as an overview at a senior high school or early university level and touches on physics, environmental sciences, mathematics, computer sciences and geography."
* [Echoes in space - Introduction to RADAR remote sensing](https://eo-college.org/courses/echoes-in-space/) by the European Space Agency; "a detailed insight into the history of Radar technology, including all the basics that are needed to understand how electromagnetic waves work and a unique hands-on experience to work with Radar data in diverse application scenarios."
* [Newcomers guide to Earth Observation](https://business.esa.int/newcomers-earth-observation-guide) by the European Space Agency, "a  guide to help non-experts in providing a starting point in the decision process for selecting an appropriate Earth Observation (EO) solution."
* [Earthdatascience intro to multispectral data](https://www.earthdatascience.org/courses/use-data-open-source-python/multispectral-remote-sensing/intro-multispectral-data/)

Further reading:
* [CSC geocomputing seminar materials](https://research.csc.fi/geocomputing-seminars), especially materials of the 2022 EO-workshop
* [ESA tutorials](https://step.esa.int/main/doc/tutorials/)
* [Awesome EO code](https://github.com/acgeospatial/awesome-earthobservation-code), long list of EO tools


!!! default "Raster data format"

    Most EO data is available in <a href="https://towardsdatascience.com/the-ultimate-beginners-guide-to-geospatial-raster-data-feb7673f6db0" aria-label="Towards data science guide to raster data">raster format</a>. The most common file formats are <a href="https://en.wikipedia.org/wiki/GeoTIFF" aria-label="GeoTiff data format description">GeoTiff</a> and <a href="http://giswiki.org/wiki/GeoJPEG2000" aria-label="GeoJPEG2000 data format description">GeoJPEG2000</a>.

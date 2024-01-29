# Earth Observation guide

This guide aims to help researchers to work with Earth Observation (EO) data using CSC's computing resources. The purpose of this guide is to give an overview of available options, so it would be easier to decide if CSC has suitable services for your EO research. It also helps you find the right data and tools for raster data based EO tasks. This guide focuses on spaceborne platforms. However, many tools and concepts also apply to airborne platforms. If you are interested in the fundamentals of EO, please check the [resources and further reading section](#resources-and-further-reading).

**What are the benefits of using EO data?**

* Possibility to observe wide areas at same time
* Non-intrusive
* Same sensor for different parts of the world, easy to compare different areas
* Time series to see changes during different seasons and years
* Cost-efficient

!!! default "Raster data format"

    Most EO data is available in <a href="https://towardsdatascience.com/the-ultimate-beginners-guide-to-geospatial-raster-data-feb7673f6db0" aria-label="Towards data science guide to raster data">raster format</a>. The most common file formats are <a href="https://en.wikipedia.org/wiki/GeoTIFF" aria-label="GeoTiff data format description">GeoTiff</a> and <a href="http://giswiki.org/wiki/GeoJPEG2000" aria-label="GeoJPEG2000 data format description">GeoJPEG2000</a>.

## Why should I use CSC computing resources for EO?

For working with EO data in general, there are three main options:

1) **EO specific services**, which provide both data and advanced ready-to-use processing environments. Usually these give better user experience and efficiency, but the services might be limited in computing power, available tools and options for adding own data. Often these have fees for using. Examples are [Google Earth Engine](https://earthengine.google.com/), [SentinelHub](https://www.sentinel-hub.com/) and  [Microsoft Planetary Computer](https://planetarycomputer.microsoft.com).

2) **Cloud services** with access to EO data. Practically, the data is often stored in object-storage and can be accessed as independent service. They  also provide general computing services, such as virtual machines, to which EO  tools need to be installed by the end-user. These options usually have some fees, mainly for processing. The data download may be free of charge or have a small cost, depending on the amount of data needed. One example is [Amazon Web Services](https://registry.opendata.aws/); also the [Microsoft Planetary Computer](https://planetarycomputer.microsoft.com) and [Copernicus Data Space Ecosystem](https://dataspace.copernicus.eu/) somewhat fit this category.

3) **Own computing environment** - PC, local cluster, virtual machines. Data needs to be downloaded and all tools must be installed to this system. On the other hand, it gives more freedom to select the tools and set-up. Usually this does not cause any extra costs, but the computing power is usually rather limited.

CSC services do not fit well in this categorization, as they provide some features from all of these. **CSC computing services provide a lot of computing power and storage space, and they are free of charge** for Finnish researchers for academic or educational use. 

At CSC, EO data can be processed and analyzed using a supercomputer, for example [supercomputer Puhti](../../../computing/systems-puhti.md), or a virtual machine in the [cPouta cloud service](../../../cloud/pouta/pouta-what-is.md). Puhti's computing capacity can hardly be compared to any other EO service, in both available processing power and amount of memory. Both Puhti and cPouta have also GPU resources, which are especially useful for large simulations and deep learning use cases. 

Puhti has also a lot of [pre-installed applications](#what-applications-are-available-on-puhti), so it is an environment ready to use. cPouta virtual machines are similar to commercial cloud services, where all set-up and installations are done by the end-user. In general, both services only support Linux software.

At CSC, [some Finnish EO datasets](#eo-data-at-csc) are available for direct use. In many cases, however, downloading EO data from other services (see [list of EO data download services](#eo-data-download-services)) is a required step of the process. Puhti and cPouta provide local storage of ~1-20 Tb. For more storage space,  [Allas object storage](../../../data/Allas/index.md) can be used.

Using CSC computing services requires basic Linux skills and ability to use some scripting language (for example Python, R, Julia) or command-line tools. In addition, supercomputers and virtual machines require you to understand some specific concepts, so it takes a few hours to get started. The [Puhti web interface](https://www.puhti.csc.fi/) makes the start considerably easier, providing a desktop environment in the web browser, which enables the use of tools with Graphical User Interfaces (GUI) and also tools like R Studio and JupyterLab for an easy start with R, Python and Julia.

## What data do I need?

When starting a task that requires EO data, there are multiple factors to consider. The decision on what are the most important factors depends heavily on the task and the resources available. The following list summarizes what one needs to consider when defining the data needs:

* Sensor: Different sensors cover different intervals of the electromagnetic (EM) spectrum and with that show different properties of the observed areas, they can be active or passive:
    * Multispectral: multiple intervals around the visible spectrum of the EM are observed at the same time
    * Hyperspectral: more but usually shorter intervals of the EM are observed at the same time
    * RADAR (Radio Detection and Ranging), SAR (Synthetic Aperture Radar), active sensing in the microwave/radio frequencies of the EM spectrum
    * LiDAR (Light Detection and Ranging), using a laser as energy source in the optical part of the EM spectrum 
    * Note that depending on the wavelengths observed, clouds, ground conditions and atmospheric artifacts may result in data gaps
* Resolution
    * Temporal: when and how often a certain area is revisited
    * Spatial: the area on the ground that each pixel covers, determining the size of the smallest possible feature that can be detected
    * Spectral: the area of the electromagnetic spectrum that is observed and spectral width of each band provided
    * Radiometric: number of bits used to represent the energy recorded (bit-depth)
* Costs:
    * Some EO data is freely available as open data
    * Some commercial datasets might be possible to get for free/less for research
* Preprocessing level
    * Raw data - can have different levels and often need to be processed before it can be used for reliable analysis
    * Different levels of preprocessed data - make sure you are aware of what kind of preprocessing has been performed on your data
    * Analysis ready data (ARD)
    * Mosaics
* User experience and knowledge
    * Appropriate background knowledge required for many tasks
    * ARD is "ready to go", but be aware of what preprocessing has been performed on your data
  

### Some widely used EO datasets

|Name|Max resolution, m|Revisit time, days|Years of operation|Open data|
|--------------|------------|-----|---------|---------|
|**Multispectral**|
|**[ESA, Sentinel-2](https://sentinel.esa.int/web/sentinel/missions/sentinel-2)**|10-60|5|2015->|Yes|
|**[NASA, Landsat](https://landsat.gsfc.nasa.gov/)**|15-120|8|1972->|Yes|
|[ESA, Proba-V](https://earth.esa.int/eogateway/catalog/proba-v-1km-333m-and-100m-products)|100-1000|1-2|2013->|Yes|
|[Airbus, Spot](https://www.intelligence-airbusds.com/imagery/constellation/spot/)|1.5|-|1986->|No|
|[Planet, several satellites ](https://www.planet.com/products/planet-imagery/)|0.5-5|-|2009-> |No*|
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
|[TanDEM-X](https://www.dlr.de/en/research-and-transfer/projects-and-missions/tandem-x)/[TERRASAR-X](https://www.dlr.de/en/research-and-transfer/projects-and-missions/terrasar-x)|0.25-40|-|2010->|No|
|[ICEYE](https://www.iceye.com/)|0.5-2.5|1|2018->|No|
||||||
|**LiDAR**|Footprint size||||
|[NASA, ICESat2](https://icesat-2.gsfc.nasa.gov/)|13|91|2019->|Yes|
|[NADA, GEDI](https://gedi.umd.edu/)|25|-|2018->|Yes|

\* See [Planets page for education and research](https://www.planet.com/markets/education-and-research/) for limited, non-commercial access to PlanetScope and RapidEye imagery.

!!! default "EO database"

    Database of all EO missions and instrument information can be found in the [CEOS EO handbook database](http://database.eohandbook.com/database/instrumenttable.aspx). See also [EOReader band mapping graphics](https://eoreader.readthedocs.io/en/latest/optical_band_mapping.html) for an overview of observed wavelength intervals for different optical sensors.
    
    
## Where can I find the data?

Commercial datasets are usually available from data provider, while open datasets may be available in different processing stages from different services. Where possible, it might be a good idea to check processing options close to the data, for direct access or faster download. While graphical browse and download services can provide a good overview of the data and are easy to use, the download of huge amounts of data gets considerably easier using a bulk downloader or download API (Application Programming Interface).

!!! default "STAC"

    Many data providers provide a Spatio Temporal Asset Catalog (STAC) of their datasets. These catalogs help in finding available data based on time and location with the possibility for multiple additional filters, such as cloud cover and resolution. The [STAC Index](https://www.stacindex.org/) provides a nice overview of available catalogs from all over the world, including [Paituli STAC](https://stacindex.org/catalogs/paituli-stac-finland#/). The STAC Index page also includes many resources for learning and utilizing STAC. Check out also CSC's [examples for utilizing STAC from Python](https://github.com/csc-training/geocomputing/blob/master/python/STAC) and [examples for utilizing STAC from R](https://github.com/csc-training/geocomputing/tree/master/R/STAC).

### EO data at CSC

Some Finnish EO datasets are available locally at CSC. A STAC catalog for all spatial data available at CSC is currently in progress. You can find more information about it and its current content from the [Paituli STAC page](https://paituli.csc.fi/stac.html).

* **Landsat mosaics** of Finland in Puhti. Accessing data in Puhti requires CSC user account with a project where Puhti service is enabled. All Puhti users have **read** access to these datasets. You do not need to move the files: they can be used directly, unless you need to modify them, which requires you to make your own copy.
* **Sentinel-2 L2A data** of Finland in Allas. These files are public, so anybody can download them, also from own computer or other services.
* [More information and list of all spatial datasets in CSC computing environment](../../../data/datasets/spatial-data-in-csc-computing-env.md)

### EO data download services  

**[SYKE/FMI, Finnish image mosaics](https://www.syke.fi/fi-FI/Tutkimus__kehittaminen/Tutkimus_ja_kehittamishankkeet/Hankkeet/Paikkatietoalusta_PTA)** : Sentinel-1, Sentinel-2 and Landsat mosaics, for several time periods per year. Some of them are available in Puhti, but not all. [FMI provides also a STAC catalog for these mosaics](https://pta.data.lit.fmi.fi/stac/root.json)

[**Copernicus Data Space Ecosystem**](https://dataspace.copernicus.eu/) provides worldwide main products for Sentinel-1, -2 and -3. It requires free registration. Includes possibility for visualisation and data processing. This was introduced in late 2023 and replaced the European Space Agency's SciHub. This service provides much more than a data download service, see below for more information.

[**FinHub**](https://finhub.nsdc.fmi.fi/#/home) is the Finnish national mirror of SciHub; other national mirrors also exist. It covers Finland and the Baltics and offers Sentinel-2 L1C (but not L2A) and Sentinel 1 SLC, GRD and OCN products and requires own registration. FinHub provides a similar Graphical User Interface (GUI) and Application Programming Interface (API) to access the data as the old SciHub. You can also use for example the [sentinelsat](https://sentinelsat.readthedocs.io/en/stable/) tool for downloading data from FinHub. 
    
[**USGS EarthExplorer**](https://earthexplorer.usgs.gov/) provides among others US related datasets, also worldwide Landsat mission datasets. It requires free registration. Data can be browsed and downloaded via web interface and bulk download. USGS is the main provider of the new [Landsat Collection 2 data](https://www.usgs.gov/landsat-missions/landsat-data-access).
    
[**NASA Earthdata**](https://search.earthdata.nasa.gov) provides among many others [harmonized Landsat 8 and Sentinel-2 dataset](https://hls.gsfc.nasa.gov/). It requires free registration and download is possible via web interface and bulk download.

**[Amazon Web Service (AWS) open EO data](https://registry.opendata.aws/?search=tags:gis,earth%20observation,events,mapping,meteorological,environmental,transportation)** is a collection of worldwide EO datasets provided by different organizations, including Landsat and Sentinel. Some of the data can be downloaded only on "requestor pays" basis. Currently, [Sentinel-2 L2A Cloud-optimized Geotiffs](https://registry.opendata.aws/sentinel-2-l2a-cogs/) are available for free, also via STAC.

**[Microsoft planetary computer](https://planetarycomputer.microsoft.com)** provides a STAC of all available data, which includes Sentinel, Landsat, MODIS. It is currently available in preview.

[**Google Cloud Storage open EO data**](https://cloud.google.com/storage/docs/public-datasets), including Sentinel-2 L1C and Landsat Collection 1 data. Data can be downloaded for example with [FORCE](../../../apps/force.md).
    
[**Terramonitor**](https://www.terramonitor.com) provides pre-prosessed, analysis ready Sentinel-2 data from Finland available between 2018-2020. It is a commercial service.

!!! default "Other geospatial datasets"

    To find other geospatial datasets, check out [CSC open spatial dataset list](https://research.csc.fi/open-gis-data).  

### Copernicus Data Space Ecosystem

The Copernicus Data Space Ecosystem does not only provide the possibility to browse, visualize and download Copernicus and other programs earth observation data, it also provides several options for further processing the data in the cloud. Almost all of the services require self registration, which everyone can do for free. Check out their website for all [available dataset descriptions](https://documentation.dataspace.copernicus.eu/Data.html) (note that duplicates may be available due to reprocessing by newest baselines).

The [Copernicus Data Space Ecosystem Browser](https://dataspace.copernicus.eu/browser/) serves as a central hub for accessing and exploring  Earth observation and environmental data provided by the Copernicus Sentinel constellations, contributing missions, auxiliary engineering data, on-demand data and more (Check out the [documentation on Data](https://documentation.dataspace.copernicus.eu/Data.html) for more details) . Users can visualize, compare and analyze and download all this data.

The [Copernicus Data Workspace](https://dataspace.copernicus.eu/workspace/) is a tool for managing and reviewing Earth observation-related products. This platform enables you to aggregate and review products, which can then be further processed or downloaded for various purposes. When products are selected for processing, you are provided with a list of processors that are capable of processing relevant data types. The processors can be further parameterized to fine-tune the results.

The [openEO Algorithm Plaza](https://marketplace-portal.dataspace.copernicus.eu) is a marketplace to discover and share various EO algorithms expressed as openEO process graphs.

The [openEO Web Editor](https://openeo.dataspace.copernicus.eu/) is a web-based graphical user interface (GUI) that allows users (who are not familiar with a programming language) to interact with the openEO API and perform various tasks related to Earth observation data processing, such as querying available data, defining processing workflows, executing processes, and visualizing the results. It allows users to build complex processing chains by connecting different processing steps as building blocks and provides options to specify parameters and input data for each step.

[Copernicus own Jupyter Lab instances](https://jupyterhub.dataspace.copernicus.eu/) provide example notebooks, and the possibility to add own packages via pip. 10Gb of persistent space per user (deleted after 15 days without login). The example notebooks are also available on [Copernicus Data Space Ecosystem github](https://github.com/eu-cdse/notebook-samples). JupyterHub provides several server options with 2 - 4 CPUs and  4 - 16 Gb of RAM. Note that in addition to personal limits, also the total number of active users seems to be limited.

The Copernicus Data Space Ecosystem provides several different APIs to access the data. A [Copernicus access token](https://documentation.dataspace.copernicus.eu/APIs/Token.html) is needed to make use of these interfaces.

Catalog APIs, all connected to the same database:

    - Odata
    - OpenSearch
    - STAC (Spatio Temporal Asset Catalog)

Streamlined Data Access APIs (SDA) enables users to access and retrieve Earth observation (EO) data from the Copernicus Data Space Ecosystem catalogue. These APIs also provide you with a set of tools and services to support data processing and analysis:

    - SentinelHub
    - OpenEO

In addition, also direct EO data access to the CDSE object storage with S3 is provided, as well as an on-demand production API and traceability service.

The [Copernicus Request builder](https://shapps.dataspace.copernicus.eu/requests-builder/) lets you build requests for the different APIs via Graphical User Interface (GUI). It can also provide complete Python scripts using 'requests' or 'sentinelhub' Python packages. Requests can be sent immediately from the GUI or copied into own script/terminal.

The [Sentinel Hub QGIS Plugin](https://documentation.dataspace.copernicus.eu/Applications/QGIS.html) allows you to view satellite image data from the Copernicus Data Space Ecosystem or from Sentinel Hub directly within a QGIS workspace. All datasets are available that are part of collections associated with your user. The current functionality of the QGIS Plugin is for visualization; it does not allow you to perform operations or access properties of the dataset.

The [Copernicus dashboard](https://dashboard.dataspace.copernicus.eu/) shows the state of services and products.

Different services have different limitations, which are described here in the [CDSE quota documentation](https://documentation.dataspace.copernicus.eu/Quotas.html). Compared to the previous system (SciHub), the number of concurrent downloads per user has increased from two to four for most APIs.

For downloading data from the CDSE to CSC computing environment, we recommend using the **S3** access to the CDSE object storage, via command line tools like `s3cmd` and `rclone` or Pythons `boto3`. Also other ways of accessing the data via Python are supported and work in CSC computing environment as shown in the example Notebooks, using [SentinelHub](https://github.com/eu-cdse/notebook-samples/blob/main/sentinelhub/data_download_process_request.ipynb) or [basic OData API and requests](https://github.com/eu-cdse/notebook-samples/blob/main/geo/odata_basics.ipynb).

You can copy data from CDSE object storage also directly to CSCs object storage Allas, following the instructions on [Allas docs page](../../../data/Allas/accessing_allas.md#copying-files-directly-between-object-storages) with endpoint `eodata.dataspace.copernicus.eu` and access and secret keys from following the [instructions about generating CDSE access keys](https://documentation.dataspace.copernicus.eu/APIs/S3.html#generate-secrets). 


## How can I process EO data at CSC?

You can find information about geocomputing using CSC resources and how to get started on [CSC geocomputing pages](https://research.csc.fi/geocomputing), including links to creating user accounts and all other practical information. 

### What to consider when choosing a software?

There is no single software perfect for every task and taste. The right software depends as much on the task to be worked on, as on the taste and skillset of the user. The following list sunmmarizes things that need to be considered when choosing a software. 

* Functionality: Does the software provide the tools you need to reach your goal?
* Interaction type: How do you want to interact with the software?
    * Graphical User Interface (GUI)
    * Command Line Interface (CLI)
    * Scripting 
* Technical aspects:
    * Reproducibility: Does the tool provide the possibility to record work steps?
    * Supported operating systems: Can the tool be installed to the operating system available to you?
    * Automation possibility: Can the tool execution be automatized for big data processing, if needed?
    * Combination possibility: Can you combine the tool with other tools?
    * Computational efficiency: Does the tool make good use of the available computational resources (especially GPUs)?
    * Support for parallel computing or batch processing
* Open source vs proprietary
    * Proprietary tools need licenses which may be expensive and/or limiting the use of the tool
    * FOSS (free and open source software) allows the user to inspect the source code and provide high level insights in its functionality

### What applications are available on Puhti?

[**FORCE**](../../../apps/force.md) - Framework for Operational Radiometric Correction for Environmental monitoring. All-in-one processing engine with CLI for EO image archives. [FORCE example for Puhti](https://github.com/csc-training/geocomputing/tree/master/force)

[**GDAL (OGR)**](../../../apps/gdal.md) - Geospatial Data Abstraction Library. Collection of command-line tools for accessing and transforming geospatial data. It is relatively fast and requires little computational resources. GDAL supports reading data directly from the Internet or object storage. GDAL is included in many other tools for data reading and writing. [GDAL example for Puhti](https://github.com/csc-training/geocomputing/tree/master/gdal)

[**Julia**](../../../apps/julia.md) - Puhtis Julia installation does not include any geospatial packages, but they can be installed by the user. [JuliaGeo](https://github.com/JuliaGeo) provides an overview of packages for geospatial data.

[**Matlab**](../../../apps/matlab.md) - you can run Matlab jobs on Puhti conveniently from your own computers Matlab installation.

[**Orfeo Toolbox (OTB)**](../../../apps/otb.md) - offers a wide variety of applications from ortho-rectification or pansharpening, all the way to classification, SAR processing, and much more. Orfeo Toolbox is available as CLI, GUI and via Python interface.

[**Python**](../../../apps/python.md)

* The [geoconda module](../../../apps/geoconda.md) provides many useful Python packages for raster data processing and analysis, such as `rasterio`, `rasterstats`, `scimage`, `sentinelhub`, `xarray` and tools for working with STAC.
* [Machine learning modules](../../../apps/by_discipline.md#data-analytics-and-machine-learning) provide some common machine learning frameworks, also for deep learning..

[**QGIS**](../../../apps/qgis.md) - open source tool with GUI for working with spatial data including limited multispectral image processing capabilities.  GUI with batch processing possibility and Python interface. Used for example for visualization, map algebra and other raster processing. Many plug-ins available, for EO data processing, check out the [QGIS Semi-automatic classification plugin](https://fromgistors.blogspot.com/p/semi-automatic-classification-plugin.html).

[**R**](../../../apps/r-env-for-gis.md) - Puhti R installation includes a lot of geospatial packages, including several useful for EO data processing, such as `terra`, `CAST`, `raster` and `spacetime`, also `rstac` for working with STAC catalogs.

[**Sen2Cor**](../../../apps/sen2cor.md) - a command-line tool for Sentinel-2 Level 2A product generation and formatting.

[**Sen2mosaic**](../../../apps/sen2cor.md) - a command-line tool to download, preprocess and mosaic Sentinel-2 data.

[**SNAP**](../../../apps/snap.md) - ESA Sentinel Application Platform. Tool for processing of Sentinel data (+ support for other data sources). GUI, CLI (Graph Processing Tool, GPT) and Python interfaces. [SNAP GPT example for Puhti](https://github.com/csc-training/geocomputing/tree/master/snap).

If you need further applications, you can ask CSC to install them for you. 
 
### Machine Learning with EO data

One example of the advanced usage of EO data is for machine learning. If you are interested in the topic, you can find a lot of examples from [CSC machine learning with spatial data course materials]( https://github.com/csc-training/GeoML). For practical guidelines, see also [CSC machine learning guide](../ml-guide.md)

## Alternative processing services

Below is a list of alternative EO processing services that might be useful, when a lot of data is required and downloading it all to CSC might not be feasible. 

**[Google Earth Engine](https://earthengine.google.com/)** is a processing platform, which requires registration, but is currently free of charge for research users. It can be accessed via browser and has worldwide analysis ready data available (<a href="https://developers.google.com/earth-engine/datasets/catalog/" aria-label="GEE data catalog">browse the catalog</a>). In general, JavaScript is used on the platform, but also  <a href="https://developers.google.com/earth-engine/guides/python_install" aria-label="Python on GEE">Python</a>  and  <a href="https://github.com/r-spatial/rgee" aria-label="R on GEE">R</a> support exists. Check out [GEE's tutorials](https://developers.google.com/earth-engine/tutorials). Note that Google Cloud Storage might be needed to export large datasets.

**[Microsoft planetary computer](https://planetarycomputer.microsoft.com)** offers JupyterHub together with Dask Gateway, both CPUs and GPUs are available. It is currently available in preview.

 **[Data and Information Access Services (DIAS)](https://www.copernicus.eu/en/access-data/dias)** offer cloud based Virtual Machines (VMs), dedicated baremetal servers, containers, operating system and software images. These services are specialized in EO and have user support available. All of them are commercial services. The new [**Copernicus Data Space Ecosystem**](https://dataspace.copernicus.eu/) combines some of the DIASes into one, including also free trials of the service. See the [Copernicus Data Space Ecosystem - Analyse page](https://dataspace.copernicus.eu/analyse) for more information on the services.
 
[**Sentinelhub**](https://www.sentinel-hub.com/explore/) is a commercial service that offers several different APIs.

**Commercial clouds**: Amazon, Google Cloud and Microsoft Azure, all provide virtual machines and other processing services, all of them have some local data, see links above. 
 
## Where can I get help?

If you are interested in using CSC services for your EO research, please make yourself familiar with the services:

* Visit a course, seminar or workshop; you can find all upcoming and past events in [the CSC training calendar](https://www.csc.fi/en/training#training-calendar)
    * For getting started, go through [CSC Computing Environment - Self Learning course](https://ssl.eventilla.com/csccompenvselflearn)
* Find information about services and how to use them in [CSC's documentation pages](../../../index.md)
* For information on geocomputing in CSC environment, checkout the collection of  [CSC's geocomputing learning materials](https://research.csc.fi/gis-learning-materials) and [CSC geocomputing examples on Github](https://github.com/csc-training/geocomputing)

You can find all the ways that you can get help from CSC specialists via [CSC contact page](../../contact.md). We are happy to help with technical problems around our services and are open for suggestions on which software should be installed to Puhti, or what kind of courses should be offered or materials/examples should be prepared. Please also let us know, if you would like to add a service to this page or find anything unclear.

## Acknowledgement

This guide was developed in cooperation with the [Finnish Environment Institute, SYKE](https://www.syke.fi/), as part of the [Geoportti project](https://www.geoportti.fi/).

## Contributions welcome

If you find any mistakes or outdated links, have improvement suggestions or want to add more information about a certain topic, please add them to our [Github issue for improving the EO guide](https://github.com/CSCfi/csc-user-guide/issues/1549), send a pull request to our [CSC documentation on github](https://github.com/CSCfi/csc-user-guide/) or contact us via any of the ways mentioned in [CSC contact page](../../contact.md). Thank you!

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
* [Overview of big EO data management and analysis platforms (from 2020)](https://www.mdpi.com/2072-4292/12/8/1253)

---
tags:
  - Free
---

# Geoconda

Geoconda is a collection of python packages that facilitate the
development of python scripts for geoinformatics applications. It
includes following python packages:

-   [boto3](https://boto3.readthedocs.io) - for working files in S3 storage, for example Allas. [Allas S3 example in CSC geocomputing Github](https://github.com/csc-training/geocomputing/blob/master/python/allas/working_with_allas_from_Python_S3.py).
-   [cartopy] - for map plotting.
-   [cfgrib](https://pypi.org/project/cfgrib/) - map GRIB files to the NetCDF Common Data Model
-   [copc-lib](https://github.com/RockRobotic/copc-lib) - reader and writer interface for [Cloud Optimized Point Clouds (COPC)](https://copc.io/) Only in geoconda 3.10.9.
-   [dask](https://dask.org/) - provides advanced parallelism for analytics, enabling performance at scale, including [dask-geopandas](https://dask-geopandas.readthedocs.io/), [Dask-ML](https://ml.dask.org/) and [Dask JupyterLab extension](https://github.com/dask/dask-labextension). 
    -   [Dask parallization example in CSC geocomputing Github](https://github.com/csc-training/geocomputing/tree/master/python/puhti/05_parallel_dask).
    -   [STAC example in CSC geocomputing Github](https://github.com/csc-training/geocomputing/tree/master/python/STAC).
-   [descartes] - use Shapely or GeoJSON-like geometric objects as matplotlib paths and patches.
-   [Google Earth Engine API](https://developers.google.com/earth-engine/guides/python_install) - see how to [set up GEE authentication in Puhti](#google-earth-engine-authentication-set-up). 
-   [fiona] - reads and writes spatial data files.
-   [geoalchemy2]  - provides extensions to [SQLAlchemy] for working with spatial databases, primarily PostGIS.
-   **[geopandas]** - GeoPandas extends the datatypes used by [pandas].
-   [igraph](https://igraph.org/python/) - for fast routing. [Routing examples in CSC geocomputing Github](https://github.com/csc-training/geocomputing/tree/master/python/routing)
-   [geopy](https://geopy.readthedocs.io/) - client for several popular geocoding web services.
-   [geo2ml](https://github.com/mayrajeo/geo2ml) - for preparing spatial data for machine learning NEW 2024
-   [h3pandas](https://h3-pandas.readthedocs.io/en/latest/) - for hexagonal geospatial indexing system, with Pandas and GeoPandas. NEW 2024
-   **[jupyter]** - Jupyter Notebooks and JupyterLab, best to use with [Puhti web interface](../computing/webinterface/index.md) and [Jupyter](../computing/webinterface/jupyter.md)
-   [laspy](https://pythonhosted.org/laspy/) - for reading, modifying, and creating .LAS LIDAR files. 
-   [leafmap](https://leafmap.org/) - for geospatial analysis and interactive mapping in a Jupyter environment.
-   [lidar](https://lidar.gishub.org/) - for delineating the nested hierarchy of surface depressions in digital elevation models (DEMs).
-   [metpy](https://unidata.github.io/MetPy/latest/index.html) - reading, visualizing, and performing calculations with weather data.
-   [movingpandas](http://movingpandas.org) - for trajectory data
-   [networkx] - for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks. [Routing examples in CSC geocomputing Github](https://github.com/csc-training/geocomputing/tree/master/python/routing)
-   [pyproj] - performs cartographic transformations and geodetic computations.
-   [pyogrio](https://pyogrio.readthedocs.io/en/latest/index.html) - vectorized spatial vector file format I/O using GDAL/OGR.
-   [openeo](https://openeo.org/) - for connecting to Earth observation cloud back-ends in a simple and unified way. NEW 2024
-   [open3d](http://www.open3d.org/docs/release/index.html) - for 3D data processing
-   [osmnx] - download spatial geometries and construct, project, visualize, and analyze street networks from
    OpenStreetMap's APIs. [Routing examples in CSC geocomputing Github](https://github.com/csc-training/geocomputing/tree/master/python/routing) Only in geoconda-3.10.x.
-   [owslib](https://geopython.github.io/OWSLib/index.html) -  for retrieving data from Open Geospatial Consortium (OGC) web services
-   [pcraster](https://pcraster.geo.uu.nl/) - for spatio-temporal environmental modelling. NEW 2024
-   [python-pdal](https://github.com/PDAL/python) - PDAL Python extension for lidar data
-   [Py6S](https://py6s.readthedocs.io/en/latest/index.html) - Python interface to the Second Simulation of the Satellite Signal in the Solar Spectrum (6S) atmospheric Radiative Transfer Model
-   [pysal] - spatial analysis functions.    
-   [pdal](https://pdal.io/) - for lidar data
-   [pyntcloud](https://pyntcloud.readthedocs.io/) - for working with 3D point clouds.
-   [pystac-client](https://pystac-client.readthedocs.io/) -  for working with STAC Catalogs and APIs.  [STAC example in CSC geocomputing Github](https://github.com/csc-training/geocomputing/tree/master/python/STAC).
-   [python-cdo](https://pypi.org/project/cdo/) - scripting interface to CDO (Climate Data Operators).
-   **[rasterio]** - access to geospatial raster data.
-   [rasterstats] - for summarizing geospatial raster datasets based on
    vector geometries. It includes functions for zonal statistics and
    interpolated point queries. [rasterstats example in CSC geocomputing Github](https://github.com/csc-training/geocomputing/tree/master/python/zonal_stats)
-   [rtree] - spatial indexing and search.
-   [r5py](https://r5py.readthedocs.io/en/stable) - for rapid realistic routing on multimodal transport networks, see [below how to set memory correctly](#r5py-memory-settings) for r5py. NEW 2024
-   [sentinelhub](https://sentinelhub-py.readthedocs.io/en/latest/index.html) - for working with new Sentinel Hub services.
-   [sentinelsat] - downloading Sentinel images, [sentinelsat example in CSC geocomputing Github] (https://github.com/csc-training/geocomputing/tree/master/python/sentinel)
-   [shapely] - manipulation and analysis of geometric objects in the Cartesian plane.
-   [scipy](https://www.scipy.org/) - inc pandas, numpy, matplotlib etc
-   **[scikit-learn]** - machine learning for Python. [Spatial machine learning scikit-learn (shallow learning) exercises](https://github.com/csc-training/geocomputing/tree/master/machineLearning)
-   [skimage] -  algorithms for image processing.
-   [stackstac](https://stackstac.readthedocs.io/) - STAC data to xarray, [STAC example in CSC geocomputing Github](https://github.com/csc-training/geocomputing/tree/master/python/STAC).
-   [swiftclient, keystoneclient](https://docs.openstack.org/python-swiftclient/latest/) - for working with SWIFT storage, for example Allas. [Allas Swift example in CSC geocomputing Github](https://github.com/csc-training/geocomputing/blob/master/python/allas/working_with_allas_from_Python_Swift.py).
-   [whiteboxtools](https://www.whiteboxgeo.com/) -  wide-scope processing of geospatial data, many tools operate in parallel, see [CSC whiteboxtools page](whiteboxtools.md) for details.
-   **[xarray](http://xarray.pydata.org)** - for multidimensional raster data, inc. [rioxarray](https://corteva.github.io/rioxarray). [STAC example in CSC geocomputing Github](https://github.com/csc-training/geocomputing/tree/master/python/STAC).
    -   [xarray-spatial](https://xarray-spatial.org/) - efficient common raster analysis functions for xarray.
    -   [xarray_leaflet](https://github.com/xarray-contrib/xarray_leaflet) - xarray extension for tiled map plotting.
-   And many more, for retrieving the full list in Puhti use:
    `list-packages`
    
Additionally geoconda includes:

-   [spyder] - Scientific Python Development Environment with graphical interface (similar to RStudio for R). 
-   **[GDAL/OGR](../apps/gdal.md)** commandline tools 
-   [GMT] The Generic Mapping Tools 
-   [landsatlinks](https://github.com/ernstste/landsatlinks) - for creating download URLs for Landsat Collection 2 Level 1 product bundles using the USGS/EROS Machine-to-Machine API. Use `python3.10 -m landsatlinks`.
-   [PDAL](https://pdal.io/) - Point Data Abstraction Library
-   [ncview](http://cirrus.ucsd.edu/~pierce/software/ncview/quick_intro.html) for visualizing netcdf files
   
Python has multiple packages for parallel computing, for example
**multiprocessing**, **joblib** and **dask**. In our [Puhti Python examples](https://github.com/csc-training/geocomputing/tree/master/python/puhti) there are examples how to utilize these different parallelisation libraries.

If you think that some important GIS package for Python is missing from here, you can ask for installation from [CSC Service Desk](../support/contact.md).


## Available

The `geoconda` module is available:

* 3.11.9 (Python 3.11.9, PDAL 2.7.2, GDAL 3.9.1, created August 2024), in Puhti and Mahti.
* 3.10.9 (Python 3.10.9, PDAL 2.5.2, GDAL 3.6.2, created March 2023), in Puhti.
* 3.10.6 (Python 3.10.6, PDAL 2.4.1, GDAL 3.5.0, created September 2022), in Puhti and Mahti.

Version number is the same as the Python version.

## Usage

For using Python packages and other tools listed above, you can initialize them with:

```bash
module load geoconda
```

By default the latest geoconda module is loaded. If you want a specific version you can specify the version number of geoconda:

```bash
module load geoconda/[VERSION]
```

To check the exact packages and versions included in the loaded module:

```bash
list-packages
```
 
You can add more Python packages to `geoconda` by following the instructions in
our
[Python usage guide](../support/tutorials/python-usage-guide.md#installing-python-packages-to-existing-modules).

You can edit your Python code in Puhti with:

* [Visual Studio Code in Puhti web interface](../computing/webinterface/vscode.md), 
* [Visual Studio Code on your local laptop](../support/tutorials/remote-dev.md),
* [Jupyter Notebook or Lab in Puhti web interface](../computing/webinterface/jupyter.md) or 
* Spyder in [Puhti web interface with remote desktop](../computing/webinterface/desktop.md).

To open Spyder in Puhti web interface with remote desktop:

1. Log in to [Puhti web interface](https://puhti.csc.fi).
2. Open Remote desktop: Apps -> Desktop. 
3. After launching the remote desktop open `Terminal` (Desktop icon) and start Spyder:

```bash
module load geoconda
spyder
```

### r5py memory settings
`r5py` by default does not correctly understand how much memory it has available in a supercomputer so, it has to be defined manually. It is using Java in the background, so add environmental variable to set maximum memory available for Java: 

* `export _JAVA_OPTIONS="-Xmx4g"` from command-line before starting Python OR
* `os.environ["_JAVA_OPTIONS"] = "-Xmx4g"` in the beginning of your Python code.

### Google Earth Engine authentication set up
For using Google Earth Engine (GEE) API with `earthengine-api` package, one needs to have an account in GEE. Before first usage, also set up GEE authentication in Puhti:

1. Open Puhti web interface
2. Start Desktop app
3. In the Desktop, open:
    * Web Browser under Applications menu and
    * Terminal from shortcuts
4. In the Terminal:

```
module load geoconda
python

import os
os.environ['PATH'] = '/appl/opt/csc-cli-utils/google-cloud-sdk/bin:' + os.environ['PATH']

import ee
ee.Authenticate()
```

This prints out a long link and asks for a code. Copy the link to the Web Browser and open the Google log-in page. Log-in and copy the created code back to Python.


## Using Allas from Python

There are two Python libraries installed in Geoconda that can interact with Allas. __Swiftclient__ uses the swift protocol and __boto3__ uses S3 protocol. You can find CSC examples how to use both [here](https://github.com/csc-training/geocomputing/tree/master/python/allas). 

It is also possible to __read__ and __write__ files from and to Allas or other cloud object storage directly with GDAL-based packages such as `geopandas` and `rasterio`. Please check our [Using geospatial files directly from cloud, inc Allas tutorial](../support/tutorials/gis/gdal_cloud.md) for instructions and examples.

With large quantities of data in Allas, consider using [virtual rasters](https://research.csc.fi/virtual_rasters). 



## License

All packages are licensed under various free and open source licenses (FOSS), see the linked pages above for exact details.

## Citation

Please see the above linked package pages for citation information per package.

##  Acknowledgement

Please acknowledge CSC and Geoportti in your publications, it is important for project continuation and funding reports.
As an example, you can write "The authors wish to thank CSC - IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (Geoportti, urn:nbn:fi:research-infras-2016072513) for computational resources and support".

## Installation

Geoconda was installed to Puhti and Mahti using [Tykkys conda-containerize functionality](../computing/containers/tykky.md). The WhiteboxTools conda package installs only WhiteboxTools installer, therefore for proper installation of Whiteboxtools required additional post installation command and folder to wrap commandline tools.

```bash
conda-containerize new --mamba --prefix install_dir --post download_wbt -w miniconda/envs/env1/lib/python3.10/site-packages/whitebox/WBT/whitebox_tools geoconda_3.10.9.yml
```

Geoconda conda environment files and `download_wbt` and `start_wbt.py` needed for WhiteboxTools are available in [CSCs geocomputing repository](https://github.com/csc-training/geocomputing/tree/master/supercomputer_installations/geoconda). Note that for reproducibility, you'll need to define the package versions in the environment file, which can be checked on Puhti and Mahti using `list-packages` command after loading the `geoconda` module.


## References

-   [CSC Python parallelisation examples]
-   [Python spatial] libraries
-   [Geoprocessing with Python using Open Source GIS]
-   [GeoExamples], a lot of examples of using Python for spatial analysis
-   [Automating GIS processes course materials], where most of the exercises are done using Python (University of Helsinki)
-   [Geohack Week materials]
-   [Multiprocessing Basics]
-   [Geographic Data Science with Python]
-   [Aalto Spatial Analytics course material]

------------------------------------------------------------------------


  [Conda]: https://conda.io/docs/
  [cartopy]: http://scitools.org.uk/cartopy/
  [descartes]: https://pypi.python.org/pypi/descartes
  [fiona]: https://pypi.python.org/pypi/Fiona
  [gdal]: https://pypi.python.org/pypi/GDAL
  [geoalchemy2]: https://geoalchemy-2.readthedocs.io/en/latest/
  [GMT]: https://www.generic-mapping-tools.org/
  [SQLAlchemy]: http://sqlalchemy.org 
  [geopandas]: http://geopandas.org/
  [jupyter]: https://jupyter.org/
  [pandas]: http://pandas.pydata.org 
  [networkx]: https://networkx.github.io/
  [pyproj]: https://pypi.python.org/pypi/pyproj?
  [pysal]: https://pysal.org/
  [osmnx]: https://osmnx.readthedocs.io/en/stable/index.html
  [rasterio]: https://rasterio.readthedocs.io/en/latest/
  [rasterstats]: http://pythonhosted.org/rasterstats/
  [rtree]: http://toblerity.org/rtree/
  [shapely]: https://pypi.python.org/pypi/Shapely
  [skimage]: http://scikit-image.org/
  [scikit-learn]: https://scikit-learn.org/stable/
  [snappy]: https://senbox.atlassian.net/wiki/spaces/SNAP/pages/19300362/How+to+use+the+SNAP+API+from+Python
  [SNAP]: snap.md
  [spyder]: https://docs.spyder-ide.org/
  [Conda environments]: https://conda.io/docs/user-guide/tasks/manage-environments.html#
  [Bioconda]: bioconda.md
  [Python spatial]: https://github.com/SpatialPython/spatial_python/blob/master/packages.md
  [Geoprocessing with Python using Open Source GIS]: http://www.gis.usu.edu/%7Echrisg/python/2009/
  [GeoExamples]: https://geoexamples.com/
  [Automating GIS processes course materials]: https://automating-gis-processes.github.io
  [Geohack Week materials]: https://geohackweek.github.io/schedule.html
  [Multiprocessing Basics]: https://pymotw.com/2/multiprocessing/basics.html
  [sentinelsat]: https://sentinelsat.readthedocs.io/en/stable/index.html
  [CSC Python parallelisation examples]: https://github.com/csc-training/geocomputing/tree/master/python/puhti
  [Geographic Data Science with Python]: https://geographicdata.science/book/intro.html
  [Aalto Spatial Analytics course material]: https://spatial-analytics.readthedocs.io/en/latest/course-info/course-info.html


---
tags:
  - Free
catalog:
  name: Python-geo
  description: Python libraries for spatial analysis 
  license_type: Free
  disciplines:
    - Geosciences
  available_on:
    - Roihu
---

# Python-geo

Python-geo is a collection of python packages that facilitate the
development of python scripts for geoinformatics applications. It
includes following python packages:



-   [access](https://access.readthedocs.io/) - for calculating the spatial accessibility of resources. 
-   [async-tiff](https://github.com/developmentseed/async-tiff) - fast reader for TIFF-files. NEW 2026
-   [boto3](https://boto3.readthedocs.io) - for working files in S3 storage, for example Allas. [Allas S3 example in CSC geocomputing Github](https://github.com/csc-training/geocomputing/blob/master/python/allas/working_with_allas_from_Python_S3.py).
-   [cartopy] - for map plotting.
-   [cdsapi](https://cds.climate.copernicus.eu/how-to-api) - access to Copernicus Climate Data Store. NEW 2026
-   [cfgrib](https://pypi.org/project/cfgrib/) - map GRIB files to the NetCDF Common Data Model
-   [contextily](https://contextily.readthedocs.io/en/latest/) -  to retrieve tile maps from the internet. 
-   [copc-lib](https://github.com/RockRobotic/copc-lib) - reader and writer interface for [Cloud Optimized Point Clouds (COPC)](https://copc.io/) 
-   [dask](https://dask.org/) - provides advanced parallelism for analytics, enabling performance at scale, including [dask-geopandas](https://dask-geopandas.readthedocs.io/), [Dask-ML](https://ml.dask.org/) and [Dask JupyterLab extension](https://github.com/dask/dask-labextension). 
    -   [Dask parallization example in CSC geocomputing Github](https://github.com/csc-training/geocomputing/tree/master/python/puhti/05_parallel_dask).
    -   [STAC example in CSC geocomputing Github](https://github.com/csc-training/geocomputing/tree/master/python/STAC).
    -   [dask-image](https://dask-image.readthedocs.io/) - image processing with Dask Arrays. 
-   [datashader](https://datashader.org/) - for big data rendering. NEW 2026
-   [duckdb](https://duckdb.org/docs/index.html) - to execute analytical SQL queries fast. 
-   [esda](https://github.com/pysal/esda) - Exploratory Spatial Data Analysis. 
-   [fiona] - reads and writes spatial data files.   
-   [geoalchemy2]  - provides extensions to [SQLAlchemy] for working with spatial databases, primarily PostGIS.
-   [geocube](https://corteva.github.io/geocube/stable/readme.html) - convert geopandas vector data into rasterized xarray data. 
-   [geodatasets](https://geodatasets.readthedocs.io/) download and cache spatial data example files. 
-   **[geopandas]** - GeoPandas extends the datatypes used by [pandas].
-   [geoparquet-io](https://geoparquet.io/) - fast reader for GeoParquet files. NEW 2026
-   [geopy](https://geopy.readthedocs.io/) - client for several popular geocoding web services.
-   [geoviews](https://geoviews.org/) - geographic visualizations for HoloViews. NEW 2026
-   [Google Earth Engine API](https://developers.google.com/earth-engine/guides/python_install) - see how to [set up GEE authentication](#google-earth-engine-authentication-set-up). 
-   [holoviews](https://holoviews.org/) - plot big datasets. NEW 2026
-   [h3pandas](https://h3-pandas.readthedocs.io/en/latest/) - for hexagonal geospatial indexing system, with Pandas and GeoPandas. 
-   [h3-py](https://uber.github.io/h3-py/intro.html) - Python bindings for H3, a hierarchical hexagonal geospatial indexing system. 
-   [h5py](https://www.h5py.org/) - for HDF5 files. NEW 2026
-   [icechunk](https://icechunk.io/en/stable/) - cloud-native transactional tensor storage engine. NEW 2026
-   [igraph](https://igraph.org/python/) - for fast routing. [Routing examples in CSC geocomputing Github](https://github.com/csc-training/geocomputing/tree/master/python/routing)
-   [laspy](https://pythonhosted.org/laspy/) - for reading, modifying, and creating .LAS LIDAR files. 
-   [leafmap](https://leafmap.org/) - for geospatial analysis and interactive mapping in a Jupyter environment.
-   [lidar](https://lidar.gishub.org/) - for delineating the nested hierarchy of surface depressions in digital elevation models (DEMs).
-   [lonboard](https://developmentseed.org/lonboard/latest/) - fast, interactive geospatial data visualization in Jupyter. NEW 2026
-   [metpy](https://unidata.github.io/MetPy/latest/index.html) - reading, visualizing, and performing calculations with weather data.
-   [movingpandas](http://movingpandas.org) - for trajectory data
-   [networkx] - for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks. [Routing examples in CSC geocomputing Github](https://github.com/csc-training/geocomputing/tree/master/python/routing)
-   [papermill](https://papermill.readthedocs.io/en/latest/) - for parameterizing and executing Jupyter Notebooks. NEW 2026
-   [pot](https://pythonot.github.io/) - solvers for optimization problems related to Optimal Transport for signal, image processing and machine learning. NEW 2026
-   [pyproj] - performs cartographic transformations and geodetic computations.
-   [pyogrio](https://pyogrio.readthedocs.io/en/latest/index.html) - vectorized spatial vector file format I/O using GDAL/OGR.
-   [obstore](https://developmentseed.org/obstore/latest/) - fast access to S3, Google Cloud Storage and Azure Storage. NEW 2026
-   [odc-stac](https://odc-stac.readthedocs.io/en/latest/) -  STAC data to xarray, [STAC example in CSC geocomputing Github](https://github.com/csc-training/geocomputing/tree/master/python/STAC). NEW 2026
-   [openeo](https://openeo.org/) - for connecting to Earth observation cloud back-ends in a simple and unified way.
-   [open3d](http://www.open3d.org/docs/release/index.html) - for 3D data processing
-   [osmnx] - download spatial geometries and construct, project, visualize, and analyze street networks from
    OpenStreetMap's APIs. [Routing examples in CSC geocomputing Github](https://github.com/csc-training/geocomputing/tree/master/python/routing) 
-   [owslib](https://geopython.github.io/OWSLib/index.html) -  for retrieving data from Open Geospatial Consortium (OGC) web services
-   [pcraster](https://pcraster.geo.uu.nl/) - for spatio-temporal environmental modelling.
-   [psycopg2](https://www.psycopg.org/docs/) - PostgreSQL database adapter for Python.
-   [python-pdal](https://github.com/PDAL/python) - PDAL Python extension for lidar data
-   [pysal] - spatial analysis functions.    
-   [pdal](https://pdal.io/) - for lidar data
-   [pysheds](https://github.com/pysheds/pysheds) - for watershed delineation. 
-   [pystac-client](https://pystac-client.readthedocs.io/) -  for working with STAC Catalogs and APIs.  [STAC example in CSC geocomputing Github](https://github.com/csc-training/geocomputing/tree/master/python/STAC).
-   [python-cdo](https://pypi.org/project/cdo/) - scripting interface to CDO (Climate Data Operators).
-   **[rasterio]** - access to geospatial raster data.
-   [rasterstats] - for summarizing geospatial raster datasets based on
    vector geometries. It includes functions for zonal statistics and
    interpolated point queries. [rasterstats example in CSC geocomputing Github](https://github.com/csc-training/geocomputing/tree/master/python/zonal_stats)
-   [rio-cogeo](https://cogeotiff.github.io/rio-cogeo/) - for Cloud Optimized GeoTIFF (COG) creation. 
-   [rtree] - spatial indexing and search.
-   [r5py](https://r5py.readthedocs.io) - for rapid realistic routing on multimodal transport networks, see [below how to set memory correctly](#r5py-memory-settings) for r5py.
-   [shap](https://shap.readthedocs.io/en/latest/) - for explaining the output of any machine learning model. NEW 2026
-   [sentinelhub](https://sentinelhub-py.readthedocs.io/en/latest/index.html) - for working with new Sentinel Hub services.
-   [shapely] - manipulation and analysis of geometric objects in the Cartesian plane.
-   [scikit-gstat](https://scikit-gstat.readthedocs.io/en/latest/) - for variogram analysis. NEW 2026
-   **[scikit-learn]** - machine learning for Python. [Spatial machine learning scikit-learn (shallow learning) exercises](https://github.com/csc-training/geocomputing/tree/master/machineLearning)
-   [skimage] -  algorithms for image processing.
-   [scipy](https://www.scipy.org/) - inc pandas, numpy, matplotlib etc
-   [sparse](https://sparse.pydata.org/en/stable/) - for sparse arrays. NEW 2026
-   [spectral](https://www.spectralpython.net/) - for processing hyperspectral image data. NEW 2026
-   [stackstac](https://stackstac.readthedocs.io/) - STAC data to xarray, [STAC example in CSC geocomputing Github](https://github.com/csc-training/geocomputing/tree/master/python/STAC/stacstac(old)). Has not been updated lately, use rather `odc-stac`.
-   [swiftclient, keystoneclient](https://docs.openstack.org/python-swiftclient/latest/) - for working with SWIFT storage, for example Allas. [Allas Swift example in CSC geocomputing Github](https://github.com/csc-training/geocomputing/blob/master/python/allas/working_with_allas_from_Python_Swift.py).
-   [whiteboxtools](https://www.whiteboxgeo.com/) -  wide-scope processing of geospatial data, many tools operate in parallel, see [CSC whiteboxtools page](whiteboxtools.md) for details. Also Whitebox Workflows for Python.
-   **[xarray](http://xarray.pydata.org)** - for multidimensional raster data, inc. [rioxarray](https://corteva.github.io/rioxarray). [STAC example in CSC geocomputing Github](https://github.com/csc-training/geocomputing/tree/master/python/STAC).
    -   [cf_xarray](https://cf-xarray.readthedocs.io/en/latest/) - interpret Climate and Forecast metadata convention attributes present on xarray objects. NEW 2026
    -   [flox](https://flox.readthedocs.io/en/latest/) - fast GroupBy reductions for Xarray. NEW 2026
    -   [xarray-spatial](https://xarray-spatial.readthedocs.io/) - efficient common raster analysis functions for xarray. [xarray-spatial example in CSC geocomputing Github](https://github.com/csc-training/geocomputing/tree/master/python/zonal_stats)
    -   [xclim](https://xclim.readthedocs.io/en/stable/) - for climate analysis. NEW 2026
-   [xgboost](https://xgboost.readthedocs.io/) - Gradient Boosting machine learning algorithms. NEW 2026
-   [zarr](https://zarr.readthedocs.io/en/stable/) - for reading and writing data to Zarr format. NEW 2026

-   And many more, for retrieving the full list use:
    `list-packages`
    
Additionally python-geo includes:

-   **[jupyter]** - Jupyter Notebooks and JupyterLab. Use from [web interface](../computing/webinterface/index.md) with [Jupyter app](../computing/webinterface/jupyter.md). Includes [Dask Extension](https://github.com/dask/dask-labextension) and [Resource usage Extension](https://github.com/jupyter-server/jupyter-resource-usage).
-   **[GDAL/OGR](../apps/gdal.md)** commandline tools 
-   [GMT] The Generic Mapping Tools 
-   [PDAL](https://pdal.io/) - Point Data Abstraction Library
   
Python has multiple packages for parallel computing, for example
**multiprocessing**, **joblib** and **dask**. In our [Puhti Python examples](https://github.com/csc-training/geocomputing/tree/master/python/puhti) there are examples how to utilize these different parallelisation libraries.

If you think that some important GIS package for Python is missing from here, you can ask for installation from [CSC Service Desk](../support/contact.md).


## Available

The `python-geo` module is available:

* 3.14.3 (Python 3.14.3, PDAL 2.10.0, GDAL 3.12.2, created April 2026), in Roihu-CPU

The version number is the same as the Python version.

In Puhti, Mahti and LUMI python-geo is named [geoconda](geoconda.md)

## Usage



For using Python packages and other tools listed above, you can initialize them with:

```bash
module load python-geo
```

By default the latest python-geo module is loaded. If you want a specific version you can specify the version number of python-geo:

```bash
module load python-geo/[VERSION]
```

To check the exact packages and versions included in the loaded module:

```bash
list-packages
```
 
You can add more Python packages to `python-geo` by following the instructions in our
[Python usage guide](../support/tutorials/python-usage-guide.md#installing-python-packages-to-existing-modules).

You can edit your Python code with [web interface](../computing/webinterface/index.md) or [LUMI](https://docs.lumi-supercomputer.eu/runjobs/webui/jupyter/) web interface :

* [Visual Studio Code](../computing/webinterface/vscode.md)
* [JupyterLab](../computing/webinterface/jupyter.md) 

### r5py memory settings
`r5py` by default does not correctly understand how much memory it has available in a supercomputer so, it has to be defined manually. It is using Java in the background, so add environmental variable to set maximum memory available for Java: 

* `export _JAVA_OPTIONS="-Xmx4g"` from command-line before starting Python OR
* `os.environ["_JAVA_OPTIONS"] = "-Xmx4g"` in the beginning of your Python code.

### Google Earth Engine authentication set up
For using Google Earth Engine (GEE) API with `earthengine-api` package, GEE account and project are needed. Before first usage, also set up GEE authentication:

```
module load python-geo allas
earthengine authenticate --quiet
```

This prints out a long link and asks for a code. Copy the link to the web browser of your local laptop. Follow the instructions on the web page and finally copy the created code back to Terminal.

## Using Allas or LUMI-O from Python

There are two Python libraries installed in Python-geo that can interact with Allas or LUMI-O. __Swiftclient__ uses the swift protocol and __boto3__ uses S3 protocol. You can find CSC examples how to use both [here](https://github.com/csc-training/geocomputing/tree/master/python/allas). 

It is also possible to __read__ and __write__ files from and to Allas or other cloud object storage directly with GDAL-based packages such as `geopandas` and `rasterio`. Please check our [Using geospatial files directly from cloud, inc Allas tutorial](../support/tutorials/gis/gdal_cloud.md) for instructions and examples.

With large quantities of raster data, consider using [virtual rasters](https://research.csc.fi/virtual_rasters).

## License

All packages are licensed under various free and open source licenses (FOSS), see the linked pages above for exact details.

## Citation

Please see the above linked package pages for citation information per package.

##  Acknowledgement

Please acknowledge CSC and Geoportti in your publications, it is important for project continuation and funding reports.
As an example, you can write "The authors wish to thank CSC - IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (Geoportti, urn:nbn:fi:research-infras-2016072513) for computational resources and support".

## Installation

Python-geo was installed to Roihu using [Tykkys conda-containerize functionality](../computing/containers/tykky.md). In LUMI, geoconda was installed using [LUMI container wrapper](https://docs.lumi-supercomputer.eu/software/installing/container-wrapper/). The functionality of the tools is almost identical with `--post` option being `--post-install` on LUMI container wrapper. The WhiteboxTools conda package installs only WhiteboxTools installer, therefore for proper installation of Whiteboxtools required additional post installation command and folder to wrap commandline tools.

```bash
conda-containerize new --mamba --prefix install_dir --post download_wbt -w miniconda/envs/env1/lib/python3.11/site-packages/whitebox/WBT/whitebox_tools python-geo_3.11.10.yml
```

Python-geo conda environment files and `download_wbt` and `start_wbt.py` needed for WhiteboxTools are available in [CSCs geocomputing repository](https://github.com/csc-training/geocomputing/tree/master/supercomputer_installations/python-geo). Note that for reproducibility, you'll need to define the package versions in the environment file, which can be checked using `list-packages` command after loading the `python-geo` module.


## References

-   [CSC Python parallelisation examples](https://github.com/csc-training/geocomputing/tree/master/python/puhti)
-   [Multiprocessing Basics](https://pymotw.com/2/multiprocessing/basics.html)
-   [Automating GIS processes course materials](https://automating-gis-processes.github.io) by University of Helsinki
-   [Aalto Spatial Analytics course material](https://spatial-analytics.readthedocs.io/en/latest/course-info/course-info.html) by Henrikki Tenkanen / Aalto University
-   [Introduction to GIS Programming](https://geog-312.gishub.org/index.html) by Dr. Qiusheng Wu / University of Tennessee
-   [Geographic Data Science with Python](https://geographicdata.science/book/intro.html) by Sergio Rey, Dani Arribas-Bel, Levi Wolf
-   [Python Foundation for Spatial Analysis](https://courses.spatialthoughts.com/python-foundation.html) by Ujaval Gandhi

------------------------------------------------------------------------


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

# Geoconda

Geoconda is a collection of python packages that facilitate the
development of python scripts for geoinformatics applications. It
includes following python packages:

-   [ArcGIS Python API](https://developers.arcgis.com/python/) - provides simple and efficient tools for sophisticated vector and raster analysis, geocoding, map making, routing and directions. 
-   [boto3](https://boto3.readthedocs.io) - for working files in S3 storage, for example Allas. [Example](https://github.com/csc-training/geocomputing/blob/master/python/allas/working_with_allas_from_Python_S3.py).
-   [cartopy] - for map plotting.
-   [cfgrib](https://pypi.org/project/cfgrib/) - map GRIB files to the NetCDF Common Data Model
-   [dask](https://dask.org/) - provides advanced parallelism for analytics, enabling performance at scale, including [dask-geopandas](https://dask-geopandas.readthedocs.io/), [Dask-ML](https://ml.dask.org/) and [Dask JupyterLab extension](https://github.com/dask/dask-labextension)
-   [descartes] - use Shapely or GeoJSON-like geometric objects as matplotlib paths and patches.
-   [fiona] - reads and writes spatial data files.
-   [gdal] - reads and writes spatial data files, and GDAL/OGR data manipulation tools.
-   [geoalchemy2]  - provides extensions to [SQLAlchemy] for working with spatial databases, primarily PostGIS.
-   **[geopandas]** - GeoPandas extends the datatypes used by [pandas].
-   [igraph](https://igraph.org/python/) - for fast routing.
-   **[jupyter]**(https://jupyter.org/) - Jupyter Notebooks and JupyterLab, [CSC RStudio and Jupyter Notebooks tutorial](../support/tutorials/rstudio-or-jupyter-notebooks.md) describes how to use these with Puhti
-   [laspy](https://pythonhosted.org/laspy/) - for reading, modifying, and creating .LAS LIDAR files. 
-   [lidar](https://lidar.gishub.org/) - for delineating the nested hierarchy of surface depressions in digital elevation models (DEMs).
-   [movingpandas](http://movingpandas.org) - for trajectory data
-   [networkx] - for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks.
-   [pyproj] - performs cartographic transformations and geodetic computations.
-   [open3d](http://www.open3d.org/) - for 3D Data Processing
-   [osmnx] - download spatial geometries and construct, project, visualize, and analyze street networks from
    OpenStreetMap's APIs.
-   [owslib](https://geopython.github.io/OWSLib/index.html) -  for retrieving data from Open Geospatial Consortium (OGC) web services
-   [pysal] - spatial analysis functions.    
-   [pdal](https://pdal.io/) - for lidar data
-   [pyntcloud](https://pyntcloud.readthedocs.io/) - for working with 3D point clouds.
-   [pystac-client](https://pystac-client.readthedocs.io/) -  for working with STAC Catalogs and APIs.
-   [python-cdo](https://pypi.org/project/cdo/) - scripting interface to CDO (Climate Data Operators).
-   **[rasterio]** - access to geospatial raster data.
-   [rasterstats] - for summarizing geospatial raster datasets based on
    vector geometries. It includes functions for zonal statistics and
    interpolated point queries.
-   [rtree] - spatial indexing and search.
-   [sentinelsat] - downloading Sentinel images
-   [shapely] - manipulation and analysis of geometric objects in the Cartesian plane.
-   [scipy](https://www.scipy.org/) - inc pandas, numpy, matplotlib etc
-   **[scikit-learn]** - machine learning for Python.
-   [skimage] -  algorithms for image processing.
-   [swiftclient, keystoneclient](https://docs.openstack.org/python-swiftclient/latest/) - for working with SWIFT storage, for example Allas.
-   **[xarray]**(http://xarray.pydata.org) - for multidimensional raster data, inc. [rioxarray](https://corteva.github.io/rioxarray). 
-   And many more, for retrieving the full list in Puhti use:
    `list-packages`
    
Additionally geoconda includes:

-   [spyder] - Scientific Python Development Environment with graphical interface (similar to RStudio for R). 
-   [GDAL/OGR](../apps/gdal.md) commandline tools 
-   [GMT] The Generic Mapping Tools 
-   [PDAL] Point Data Abstraction Library
-   [ncview](http://cirrus.ucsd.edu/~pierce/software/ncview/quick_intro.html) for visualizing netcdf files
-   proj4, geos and many more, see `/appl/soft/geo/geoconda/miniconda3/envs/geoconda-3.x/bin` or `/appl/soft/geo/conda/singularity/geoconda/2021/bin` for full
    list.
   
Python has multiple packages for parallel computing, for example
**multiprocessing**, **joblib** and **dask**. In our [Puhti Python examples](https://github.com/csc-training/geocomputing/tree/master/python/puhti) there are examples how to utilize these different parallelisation libraries.

(If you think that some important GIS package for Python is missing from here, you can ask for installation from servicedesk@csc.fi.)


## Available

The `geoconda` module is available in Puhti:

* 3.9.12
* 3.8.8 

Version number is the same as Python version.

## Usage

For using Python packages and other tools listed above, you can initialize them with:

`module load geoconda`

By default the latest geoconda module is loaded. If you want a specific version you can specify the version number of geoconda:

`module load geoconda/[VERSION]`

To check the exact packages and versions included in the loaded module:

`list-packages`
 
You can add more Python packages to `geoconda`, see instructions from [CSC Python page](python.md#installing-python-packages-to-existing-modules).

You can edit your Python code in Puhti with:
* [Visual Studio Code in Puhti web interface](../computing/webinterface/vscode.md), 
* [Visual Studio Code on your local laptop](../support/tutorials/remote-dev.md),
* [Jupyter Notebook or Lab in Puhti web interface](../computing/webinterface/jupyter.md) or 
* Spyder in [Puhti web interface with remote desktop](../computing/webinterface/desktop.md).

To open Spyder in Puhti web interface with remote desktop:

1. Log in to [Puhti web interface](https://puhti.csc.fi).
2. Open Remote desktop: Apps -> Desktop, choose Desktop: `mate` or `xfce`. 
3. After launcing the remote desktop open `Host Terminal` (Desktop icon) and start Spyder:

```
module geoconda
spyder
```

## Using Allas from Python

There are two Python libraries installed in Geoconda that can interact with Allas. __Swiftclient__ uses the swift protocol and __boto3__ uses S3 protocol. You can find CSC examples how to use both [here](https://github.com/csc-training/geocomputing/tree/master/python/allas). With large quantities of data in Allas, virtual rasters should be considered. More information on how to create and use virtual rasters can be found [here](https://research.csc.fi/virtual_rasters).

## License and acknowledgement

All packages are licensed under various free and open source licenses (FOSS), see the linked pages above for exact details.

Please acknowledge CSC and Geoportti in your publications, it is important for project continuation and funding reports.
As an example, you can write "The authors wish to thank CSC - IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (Geoportti, urn:nbn:fi:research-infras-2016072513) for computational resources and support".

### References

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
  [pdal]: https://github.com/PDAL/python
  [snappy]: https://senbox.atlassian.net/wiki/spaces/SNAP/pages/19300362/How+to+use+the+SNAP+API+from+Python
  [SNAP]: snap.md
  [spyder]: https://docs.spyder-ide.org/
  [-X connection or NoMachine for Windows users]: ../tutorials/nomachine-usage.md
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


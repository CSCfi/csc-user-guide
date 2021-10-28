# Geoconda

Geoconda is a collection of python packages that facilitate the
development of python scripts for geoinformatics applications. It
includes following python packages:

-   [ArcGIS Python API](https://developers.arcgis.com/python/) - provides simple and efficient tools for sophisticated vector and raster analysis, geocoding, map making, routing and directions. 
-   [boto3](https://boto3.readthedocs.io) - for working files in S3 storage, for example Allas. [Example](https://github.com/csc-training/geocomputing/blob/master/python/allas/working_with_allas_from_Python_S3.py).
-   [cartopy] - for map plotting.
-   [dask](https://dask.org/) - provides advanced parallelism for analytics, enabling performance at scale, including [Dask-ML](https://ml.dask.org/) and [Dask JupyterLab extension](https://github.com/dask/dask-labextension)
-   [descartes] - use Shapely or GeoJSON-like geometric objects as matplotlib paths and patches.
-   [fiona] - reads and writes spatial data files.
-   [gdal] - reads and writes spatial data files, and GDAL/OGR data manipulation tools.
-   [geoalchemy2]  - provides extensions to [SQLAlchemy] for working with spatial databases, primarily PostGIS.
-   **[geopandas]** - GeoPandas extends the datatypes used by [pandas].
-   [igraph](https://igraph.org/python/) - for fast routing.
-   [jupyter](https://jupyter.org/) - Jupyter Notebooks and JupyterLab, [CSC RStudio and Jupyter Notebooks tutorial](../support/tutorials/rstudio-or-jupyter-notebooks.md) describes how to use these with Puhti
-   [laspy](https://pythonhosted.org/laspy/tut_part_1.html)
-   [laxpy](https://github.com/brycefrank/laxpy)
-   [networkx] - for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks.
-   [pyproj] - performs cartographic transformations and geodetic computations.
-   [osmnx] - download spatial geometries and construct, project, visualize, and analyze street networks from
    OpenStreetMap's APIs.
-   [pysal] - spatial analysis functions.    
-   [pdal](https://pdal.io/) - for lidar data
-   **[rasterio]** - access to geospatial raster data.
-   [rasterstats] - for summarizing geospatial raster datasets based on
    vector geometries. It includes functions for zonal statistics and
    interpolated point queries.
-   [rtree] - spatial indexing and search.
-   [sentinelsat] - downloading Sentinel images
-   [shapely] - manipulation and analysis of geometric objects in the Cartesian plane.
-   [scipy](https://www.scipy.org/) - inc pandas, numpy, matplotlib etc
-   [scikit-learn] - machine learning for Python.
-   [skimage] -  algorithms for image processing.
-   [swiftclient, keystoneclient](https://docs.openstack.org/python-swiftclient/latest/) - for working with SWIFT storage, for example Allas.
-   [xarray](http://xarray.pydata.org) - for multidimensional raster data. 
-   And many more, for retrieving the full list in Puhti use:
    `list-packages`
    
Additionally geoconda includes:

-   [spyder] - Scientific Python Development Environment with graphical interface (similar to RStudio for R). 
-   [GDAL/OGR](../apps/gdal.md) commandline tools 3.2.1 in geoconda-3.8.8, 3.0.4 in geoconda-3.8 and 3.0.2 in geoconda-3.7
-   [GMT] The Generic Mapping Tools in geoconda 3.8 and 3.8.8.
-   [PDAL] 2.2.0 in geoconda-3.8.8, 2.1.0 in geoconda-3.8 and 2.0.1 in geoconda-3.7
-   [QGIS](../apps/qgis.md) only in geoconda 3.8 and 3.7, latest version in own qgis module.
-   [LasTools](../apps/lastools.md) only in geoconda 3.8 and 3.7, latest version in own lastools module.
-   [ncview](http://cirrus.ucsd.edu/~pierce/software/ncview/quick_intro.html) for visualizing netcdf files
-   proj4, geos and many more, see `/appl/soft/geo/geoconda/miniconda3/envs/geoconda-3.x/bin` or `/appl/soft/geo/conda/singularity/geoconda/2021/bin` for full
    list.
    
!!! note
    If you want to use Spyder, ncview or other tools with graphical user interfaces,connect to Puhti web interface and start a [remote desktop](../computing/webinterface/desktop.md) or [Visual Studio Code](../computing/webinterface/vscode.md). You can also [edit and run Python code remotely](../support/tutorials/remote-dev.md) with some code editors like Visual Studio Code

Python has multiple packages for parallel computing, for example
**multiprocessing**, **joblib** and **dask**. In our [Puhti Python examples](https://github.com/csc-training/geocomputing/tree/master/python/puhti) there are examples how to utilize these different parallelisation libraries.

(If you think that some important GIS package for Python is missing from here, you can ask for installation from servicedesk@csc.fi.)


## Available

The `geoconda` module is available in Puhti:

* 3.8.8 (Singularity installation with wrappers, the usage of singularity container should not be visible in normal use-cases.)
* 3.8-deprecated 
* 3.7-deprecated 

3.8 and 3.7 are depricated, because these are normal conda installations, which causes heavy load to Puhti disk system.

Version number is the same as Python version.

## Usage

For using Python packages and other tools listed above, you can initialize them with:

`module load geoconda`

By default the latest geoconda module is loaded. If you want a specific version you can specify the version number of geoconda:

`module load geoconda/[VERSION]`

For using the Spyder IDE give:

`spyder`

To check the exact packages and versions included in the loaded module:

`list-packages`
 
You can add more Python packages to `geoconda`, see instructions from [CSC Python page](python.md#installing-python-packages-to-existing-modules).


## Using Allas from Python

There are two Python libraries installed in Geoconda that can interact with Allas. __Swiftclient__ uses the swift protocol and __boto3__ uses S3 protocol. You can find CSC examples how to use both [here](https://github.com/csc-training/geocomputing/tree/master/python/allas). With large quantities of data in Allas, virtual rasters should be considered. More information on how to create and use virtual rasters can be found [here](https://research.csc.fi/virtual_rasters).

## License and citing

All packages are licensed under various free and open source licenses (FOSS), see the linked pages above for exact details.
In your publications please acknowledge also oGIIR and CSC, for example “The authors wish to acknowledge for computational resources CSC – IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (oGIIR, urn:nbn:fi:research-infras-2016072513).”

### References

-   [CSC Python parallelisation examples]
-   [Python spatial] libraries
-   [Geoprocessing with Python using Open Source GIS]
-   [GeoExamples], a lot of examples of using Python for spatial analysis
-   [Automating GIS processes course materials], where most of the exercises are done using Python (University of Helsinki)
-   [Geohack Week materials]
-   [Multiprocessing Basics]

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

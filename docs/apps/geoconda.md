# Geoconda

Geoconda is a collection of python packages that facilitate the
development of python scripts for geoinformatics applications. It
includes following python packages:

-   [ArcGIS Python API](https://developers.arcgis.com/python/) - provides simple and efficient tools for sophisticated vector and raster analysis, geocoding, map making, routing and directions. 
-   [cartopy] - for map plotting.
-   [descartes] - use Shapely or GeoJSON-like geometric objects as matplotlib paths and patches.
-   [fiona] - reads and writes spatial data files.
-   [gdal] - reads and writes spatial data files, and GDAL/OGR data manipulation tools.
-   [geoalchemy2]  - provides extensions to [SQLAlchemy] for working with spatial databases, primarily PostGIS.
-   [igraph](https://igraph.org/python/) - for fast routing.
-   **[geopandas]** - GeoPandas extends the datatypes used by [pandas].
-   [laspy](https://pythonhosted.org/laspy/tut_part_1.html)
-   [laxpy](https://github.com/brycefrank/laxpy)
-   [networkx] - for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks.
-   [pyproj] - performs cartographic transformations and geodetic computations.
-   [osmnx] - download spatial geometries and construct, project, visualize, and analyze street networks from
    OpenStreetMap's APIs.
-   **[pysal]** - spatial analysis functions.    
-   [pdal](https://pdal.io/) - for lidar data
-   **[rasterio]** - access to geospatial raster data.
-   [rasterstats] - for summarizing geospatial raster datasets based on
    vector geometries. It includes functions for zonal statistics and
    interpolated point queries.
-   [rtree] - spatial indexing and search.
-   [shapely] - manipulation and analysis of geometric objects in the Cartesian plane.
-   [scikit-learn] - machine learning for Python.
-   [skimage] -  algorithms for image processing.
-   [xarray](http://xarray.pydata.org) - for multidimensional raster data. 
-   And many more, for retrieving the full list in Puhti use:
    `list-packages`
    
Additionally geoconda includes:

-   [spyder] - Scientific Python Development Environment with graphical interface (similar to RStudio for R). 
-   [GDAL/OGR](../apps/gdal.md) commandline tools 3.0.2
-   [PDAL] 2.0.1
-   [QGIS](../apps/qgis.md) 3.10.0
-   [LasTools](../apps/lastools.md) 20171231
-   [ncview](http://cirrus.ucsd.edu/~pierce/software/ncview/quick_intro.html) for visualizing netcdf files
-   proj4, geos and many more, see `/appl/soft/geo/geoconda/miniconda3/envs/geoconda-3.7/bin`for full
    list.
    
!!! note
    If you want to use Spyder, QGIS, ncview or other tools with graphical user interfaces, you should connect to Puhti using -X connection.

Python has also packages for parallel computing, for example
**multiprocessing**. In our examples there is two cases using Python
multiprocessing: [zonal statistics] and [focal mean].

(If you think that some important GIS package for Python is missing from
here, you can ask for installation from servicedesk@csc.fi.)

## Available

The `geoconda` module is available in Puhti:

* 3.7 (version number is the same as Python version)



## Usage

### Using geoconda

For using Python packages and other tools listed above, you can initialize them with:

`module load geoconda`

By default the latest geoconda module is loaded. If you want a specific version you can specify the version number of geoconda:

`module load geoconda/[VERSION]`

For using the Spyder IDE give:

`spyder`

To check the exact packages and versions included in the loaded module:

`list-packages`
 

### Adding more Python packages to GeoConda

You can add more Python packages to Geoconda for your own use with `pip`, for example:

`pip install [newPythonPackageName] --user --target=/projappl/[yourProject]/python3.7/site-packages/`.

If you do not give the installation folder as target, the packages are by default installed to your home directory under
`.local/lib/python3.7/site-packages`

If you would like to make a own conda environment, it is recommended to make also own [Miniconda installation](../support/tutorials/conda.md). Or then you can use [bioconda].


## License and citing

All packages are licensed under various free and open source licenses (FOSS), see the linked pages above for exact details.
In your publications please acknowledge also oGIIR and CSC, for example “The authors wish to acknowledge for computational resources CSC – IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (oGIIR, urn:nbn:fi:research-infras-2016072513).”

### References


-   [Python spatial] libraries
-   [Essential Python Geospatial Libraries]
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
  [SQLAlchemy]: http://sqlalchemy.org 
  [geopandas]: http://geopandas.org/
  [pandas]: http://pandas.pydata.org 
  [networkx]: https://networkx.github.io/
  [pyproj]: https://pypi.python.org/pypi/pyproj?
  [pysal]: http://pysal.readthedocs.io/en/latest/
  [osmnx]: https://osmnx.readthedocs.io/en/stable/index.html
  [rasterio]: https://mapbox.github.io/rasterio/
  [rasterstats]: http://pythonhosted.org/rasterstats/
  [rtree]: http://toblerity.org/rtree/
  [shapely]: https://pypi.python.org/pypi/Shapely
  [skimage]: http://scikit-image.org/
  [scikit-learn]: https://scikit-learn.org/stable/
  [pdal]: https://github.com/PDAL/python
  [snappy]: https://senbox.atlassian.net/wiki/spaces/SNAP/pages/19300362/How+to+use+the+SNAP+API+from+Python
  [SNAP]: snap.md
  [spyder]: https://pythonhosted.org/spyder/
  [-X connection or NoMachine for Windows users]: ../tutorials/nomachine-usage.md
  [zonal statistics]: https://github.com/csc-training/geocomputing/tree/master/python/zonal_stats
  [focal mean]: https://github.com/csc-training/geocomputing/tree/master/python/focal_mean
  [geo-env]: https://research.csc.fi/-/geo-env
  [Python]: https://research.csc.fi/-/python
  [Conda environments]: https://conda.io/docs/user-guide/tasks/manage-environments.html#
  [Bioconda]: bioconda.md
  [Python spatial]: https://github.com/SpatialPython/spatial_python/blob/master/packages.md
  [Essential Python Geospatial Libraries]: http://spatialdemography.org/essential-python-geospatial-libraries/
  [Geoprocessing with Python using Open Source GIS]: http://www.gis.usu.edu/%7Echrisg/python/2009/
  [GeoExamples]: http://geoexamples.blogspot.fi/
  [Automating GIS processes course materials]: https://automating-gis-processes.github.io
  [Geohack Week materials]: https://geohackweek.github.io/schedule.html
  [Multiprocessing Basics]: https://pymotw.com/2/multiprocessing/basics.html

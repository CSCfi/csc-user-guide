# Virtual rasters

[Virtual rasters](https://gdal.org/drivers/raster/vrt.html) is useful GDAL concept for managing large raster datasets that are split into not overlapping map sheets. Virtual rasters are not useful for managing time-series or overlapping rasters, for example remote sensing tiles. 

Technically a virtual raster is just a small xml file that tells GDAL where the actual data files are, but from user's point of view virtual rasters can be treated much like any other raster format. Virtual rasters can include raster data in any file format GDAL supports. Virtual rasters are useful because they allow handling of large datasets as if they were a single file eliminating need for locating correct files.

For example the [NLS 2m and 10m DEM are available in Puhti](../../../data/datasets/spatial-data-in-csc-computing-env.md). These datasets are split into a number of tif files (map sheets) and if we wanted for example to calculate zonal statistics for some areas scattered around whole Finland we would have to somehow find out which file covers which area and compute statistics from correct file. Further complications would arise if an area we want to calculate statistics for happens to lie at a border between two or more map sheets. Similar issues with edge effects would arise for example when using focal functions where information from surrounding files is also needed. These issues can be easily avoided by creating a virtual raster for the whole study area and above mentioned problems will be automatically taken care of by GDAL.

It is possible to use virtual rasters so, that only the small xml-file is stored locally and the big raster files are in Allas, Amazon S3, publicly on server or any other place supported by GDAL virtual drivers. The data is moved to local only for the area and zoom level requested when the virtual raster is opened. The best performing format to save your raster data in remote service is [Cloud optimized GeoTIFF](https://www.cogeo.org/), but other formats are also possible.

## Using virtual rasters
Virtual rasters are supported by any GDAL based tool, including Python and R spatial packages, ArcGIS, FME, GrassGIS, MapInfo, QGIS, and SagaGIS. Additionally ArcGIS and MapInfo have respectively also their own virtual raster format similar to GDAL virtual raster.

### Reading only a part of a big virtual raster with  bbox

The key for efficient usage of virtual rasters is often the support for reading only a part of the big virtual raster. This can be done both with R and Python, for many other tools the crop has to be done as extra step with saving the cropped data to a file.

With **GDAL** it is easy to crop a small part out of the big virtual raster:

`gdal_translate -projwin 614500 6668500 644500 6640500 test.vrt test_clip.tif`

**R**:

Terra:
```
library(terra)  
vrt <- rast("test.vrt")  
data = crop(vrt , ext(614500, 644500, 6640500, 6668500))
```

Raster:
```
library(raster)  
vrt <- raster("test.vrt")  
data = crop(vrt , extent(614500, 644500, 6640500, 6668500))
```

**Python**:

```
import rasterio
from rasterio.windows import from_bounds
vrt_path = "test.vrt"
with rasterio.open(vrt_path) as src:
    rst = src.read(window=from_bounds(614500, 6640500, 644500, 6668500, src.transform))
```


### Running analysis that reads only some parts of the virtual raster

It's possible to work with very large virtual rasters when the analysis doesn't actually need to output a raster of similar size. A good example would be calculating zonal statistics for polygons spread out across large area, see [CSC training github](https://github.com/csc-training/geocomputing/tree/master/python/zonal_stats) for example. In this case raster data is read only from areas overlapping with the polygons.

### Working with large virtual rasters visually

It is worth noting that while running some analysis on a 2m DEM covering whole Finland is entirely feasible in Puhti with the basic .vrt, viewing the data with for example QGIS is not practical for such a large dataset without further optimization. If you wanted to easily view a big virtual raster, you have to do a few things:

*   Create overviews for your virtual raster using gdaladdo command. You should take care to not create overviews that are so large that the overviews become a huge file themselves.
*   If your virtual raster is really big it makes sense to create a hierarchial structure of virtual rasters where topmost virtual raster points to smaller virtual rasters which point to smaller virtual rasters and so on until you have the last virtual raster pointing to actual files. The reason for using this approach is that if you don't do this also the overviews used get really big. Note that using this kind of hierachial structure may produce some artifacts when running analysis on the data so it should be reserved for viewing purposes.
*   Pre calculate statistics for your virtual rasters and source files. This is to make opening files faster in for example QGIS. QGIS needs to sample for min and max value in the data to be able to set the colorscale right and this takes time with large virtual rasters. To avoid having to do this you can precompute statistics to separate XML file with `gdalinfo --stats` command.
*   A good trick in QGIS when working with large rasters is to enable raster toolbar (View->Toolbars->Raster Toolbar) This allows you to easily adjust colorscale to area shown in screen which lets you have good contrast regardless of zoom level.
*   QGIS seems to be pretty good at handling large datasets when above mentioned steps have been taken. Even with 2m DEM from whole finland zooming and moving the map is quite smooth.

## Creating virtual rasters

Following tools support creating virtual rasters:

*   [GDAL gdalbuildvrt](https://gdal.org/programs/gdalbuildvrt.html) commandline tool.
*   GDAL gdal_translate with STAC search
*   [Python](https://gdal.org/api/python/osgeo.gdal.html#osgeo.gdal.BuildVRT) and [R](https://rdrr.io/cran/terra/man/vrt.html) have wrappers for GDAL gdalbuildvrt, for [longer example for R see StackOverflow's answer](https://stackoverflow.com/questions/68332846/improving-computational-speed-of-zonal-statistics-on-150gb-of-raster-tiles-in-r).
*   [QGIS,](https://docs.qgis.org/3.10/en/docs/user_manual/processing_algs/gdal/rastermiscellaneous.html?highlight=virtual#build-virtual-raster) [GrassGIS](https://grass.osgeo.org/grass79/manuals/r.buildvrt.html) and [SagaGIS](http://www.saga-gis.org/saga_tool_doc/7.5.0/io_gdal_12.html) provide graphical interface for gdalbuildvrt
*   [lidR](https://cran.r-project.org/web/packages/lidR/index.html) supports writing lidar data analysis results directly as virtual raster
* [vrt_creator.py](../../../data/datasets/spatial-data-in-csc-computing-env.md) in Puhti for custom areas with 2m or 10m DEM

In Puhti glalbuildvrt is included in all [modules including GDAL](../../../apps/gdal.md), Python BuildVRT in [geoconda](../../../apps/geoconda.md), QGIS in [QGIS](../../../apps/qgis.md), R terra and lidR in [r-env](../../../apps/r-env.md) module.

### Creating virtual raster with GDAL gdalbuildvrt

If your data is divided to subfolders the easiest option is to create the virtual raster with a help of input file list:

`gdalbuildvrt -input_file_list file_list.txt virtual_raster.vrt`

Check gdalbuildvrt documentation for additional options, for example for setting no-data value.


#### Creating the file list for gdalbuildvrt

File list should include preferably full paths, but for local files also relative paths can be used.

**Linux** 

`find /appl/data/geo/mml/dem2m/ -name "*.**tif**" > file_list.txt`

**Windows**

`dir \data\dem2m\*.**tif** /S /B > file_list.txt`

**Raster files in Allas / some other S3**

If doing this from Puhti, load allas module. 

List the file names as they are in the bucket with rclone or some other tool:

`rclone lsf --include '*.**tif**' allas:<your_bucket_name > file_list.txt`

Next add to the file list the full paths as they are required by GDAL, using vsicurl, vsis3 or vsiswift drivers. See longer explanations of GDAL drivers and Allas from [Puhti GDAL page](../../../apps/gdal.md).

`sed -i -e 's-^-/**vsicurl**/https://a3s.fi/<your_bucket_name>/-' file_list.txt`

`sed -i -e 's-^-/**vsis3**/<your_bucket_name>/-' file_list.txt`

`sed -i -e 's-^-/**vsiswift**/<your_bucket_name>/-' file_list.txt`

Set up your credentials for [GDAL](../../../apps/gdal.md) before running `gdalbuildvrt`.

### Creating virtual raster from STAC search results

STAC (Spatio-Temporal Asset Catalog) is a way to describe (raster) datasets with support to search data by time and location. For example [Paituli STAC](https://paituli.csc.fi/stac.html) includes several Finnish datasets and explains the STAC concepts in more detail. 

[GDAL supports searching STAC](https://gdal.org/drivers/raster/stacit.html) and creating virtual rasters based on the results.

For example following creates virtual raster based on search results from Paituli STAC, the query asks for files in `corine_land_cover_at_geocubes` Collection in specified time interval and location (bbox), based on Assets (=files) with name `COG`. 

`gdal_translate "STACIT:\"https://paituli.csc.fi/geoserver/ogc/stac/v1/search?collections=corine_land_cover_at_geocubes&datetime=2017-01-05/2019-02-14&bbox=19.5,61.5,28.7,63.0\":asset=COG" -of VRT corine.vrt`

Note, that GDAL removes from virtual raster Assets that are fully covered with newer Assets. For example, Paituli STAC has CORINE data available for 2012 and 2018. If the above search is changed to cover also 2012 then STAC search would find also CORINE 2012 Items, but these would still not be in the created VRT. If 2012 data is needed to the virtual raster, then the time interval has to be adjusted, so that 2018 would not be included.

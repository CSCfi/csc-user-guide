# GDAL

[GDAL](http://www.gdal.org) is a very versatile open source library for raster and vector data, supporting tens of different formats and any coordinate system. GDAL is used in the background by many GIS-softwares for data reading and writing. GDAL is usually very fast, but in most cases it does not support parallel computing. GDAL also has Java and Python API. Additionally the library includes [command-line tools](https://gdal.org/programs/index.html) for many different purposes. Below we take a look at a few of them.

## Getting started

* [Install GDAL](https://gdal.org/download.html#binaries). If you have installed already QGIS or R/Python GIS packages, then you should have GDAL already. Just find where it is, look for example for OSGeo shell, Anaconda Prompt or gdalinfo file from your disk.
* Open terminal, OSGeo shell, Anaconda Prompt or Windows Command Prompt.
* (See the basic command-line help at the end of this page.)
* [GDAL is available in Puhti](../../../apps/gdal.md).

## Main tools

*  [gdalinfo](http://www.gdal.org/gdalinfo.html) and [ogrinfo](http://www.gdal.org/ogrinfo.html) - for printing metadata about a file (coordinate system, tiling, bands, attribute fields etc). Tools with gdal* in name are for raster files and with ogr* for vector files.
*   [gdal_translate](http://www.gdal.org/gdal_translate.html) and [ogr2ogr](http://www.gdal.org/ogr2ogr.html) - for changing format and modifying files.
*   [gdalwarp](http://www.gdal.org/gdalwarp.html) and [ogr2ogr](http://www.gdal.org/ogr2ogr.html) - for chaning coordinate system
*   [gdal_merge ](http://www.gdal.org/gdal_merge.html)and [ogr2ogr](http://www.gdal.org/ogr2ogr.html) - for joinig files
*   [gdal_edit](https://gdal.org/programs/gdal_edit.html#gdal-edit) - chaning raster files in place
*   [gdalbuildvrt](https://gdal.org/programs/gdalbuildvrt.html) - creating virtual rasters, see our [Virtual rasters tutorial](virtual-rasters.md) for details.
*   GDAL has additionally many other tools, for full reference see [GDAL programs page](https://gdal.org/programs/index.html) where all tools and options of the tools are described in detail.


It is important to notice that most tools create a new file and then some settings might changes, because GDAL-defaults are used, for example raster inner tiling or compression. If you want to preserve these check with gdalinfo what has been used and add additional options to the commands.

## EPSG codes

The easiest way for defining a coordinate system with GDAL is to use EPSG codes. The most common codes for Finland are:

```
3067 ETRS-TM35FIN  
4326 WGS-84
```

*   More Finnish EPSG codes can be found from [JHS-recommendatation](https://www.suomidigi.fi/sites/default/files/2020-07/JHS197_liite10.doc).
*   [Database of all EPSG codes](https://epsg.org/home.html).

## Examples

**Print file metadata**

```
gdalinfo file.tif  
ogrinfo -al -so file.shp
```

**Change coordinate system**

Use `-t_srs` for defining the new coordinate system.

```
ogr2ogr -t_srs EPSG:3067 output.shp input.shp  
gdalwarp -t_srs EPSG:4326 input.tif output.tif
```

If the original coordinate system is not written to file or GDAL does not understand it correctly, it can be given with `-s_srs`:

`gdalwarp -s_srs EPSG:3386 -t_srs EPSG:2393 input_kkj0.tif output_kkj3.tif`

**Add coordinate system**

For manually adding coordinate system to a file use **-a_srs** (this does not change the data, just adds information about coordinate system).

`ogr2ogr -a_srs EPSG:2394 output_no_srs.shp input_kkj4.shp`  
`gdal_edit -a_srs EPSG:3067 input.tif`  
`gdal_translate -a_srs EPSG:2394 input_no_srs.tif output_kkj4.tif`

**Change format**

```
gdal_translate input.ecw output.tif  
ogr2ogr output.shp input.mif
```

Set compression and tiling to raster file.  
`gdal_translate -co COMPRESS=JPEG -co "TILED=YES input.ecw output.tif`

Create Cloud Optimized GeoTiff, includes tiling and internal overviews by default
`gdal_translate world.tif world__cog.tif -of COG -co COMPRESS=LZW`

Use specific encoding for vector data attribute data.

`ogr2ogr output.shp input.gml -lco ENCODING=UTF-8`

Read data from a WFS web service.

`ogr2ogr output.shp WFS:"http://geohub.jrc.ec.europa.eu/effis/ows" layername`

Read OpenStreetMap data downloaded for example from [Geofabrik](http://download.geofabrik.de/europe/finland.html).

`ogr2ogr OSM_aineisto finland-latest.osm.pbf`

Select only lakes or municipalities. Check data with ogrinfo and read OpenStreetMap [Map Features](http://wiki.openstreetmap.org/wiki/Map_Features) page for selecting other features.

`ogr2ogr -where "natural like 'water'" fin_lakes.shp finland-latest.osm.pbf multipolygons  
ogr2ogr -where "admin_level='8'" fin_municipalities.shp finland-latest.osm.pbf multipolygons`

**Optimize Shape file's dbf-file**

Shape datasets have ofter too big .dbf-files, because field lengths are based to defaults, not data. For optimizing field lengths for string and integer fields:

`ogr2ogr output.shp input.shp –lco RESIZE=YES`

For existing file the same can be done with ogrinfo.

`ogrinfo file1.dbf -sql "RESIZE file1"`

One option for fixing the double type field lengths is to to it manually with OpenCalc. When the .dbf is opened in OpenCalc, the field types and lengths are displayed on first row, for example: N,19,11\. These can be manually changed to more suitable, for example N,9,2.

**CSV to Shape**

A CSV file with coordinates in CoordX ja CoordY columns and in EPSG:3067 coordinates system can be changed to a Shape-format:  

`ogr2ogr output.shp input.csv -oo X_POSSIBLE_NAMES=CoordX -oo Y_POSSIBLE_NAMES=CoordY -a_srs EPSG:3067`

GDAL tries to guess the field types and lengths, but sometimes might go wrong. For fixing create first a .csvt and check / edit it if needed.

`ogr2ogr out.csv in.csv -oo AUTODETECT_WIDTH=YES -oo AUTODETECT_TYPE=YES -lco CREATE_CSVT=YES`

**Merge files**

`gdal_merge -o merged.tif input1.tif input2.tif`

For vector data there is no merge command, but an append option in ogr2ogr. So first create a copy of one of the input files (1.), and then append the second file (2). -nln defines the layer name

`(1) ogr2ogr file_merged.shp file1.shp  
(2) ogr2ogr -update -append file_merged.shp file2.shp -nln file_merged`

**Clip files**

With bbox:

```
gdal_translate -projwin xmin ymax xmax ymin input.tif output.tif  
ogr2ogr -spat xmin ymin xmax ymax output.shp input.shp
```

With Shape-file:

```
ogr2ogr -clipsrc clippingLayer.shp output.shp input.shp  
gdalwarp -cutline clippingLayer.shp -crop_to_cutline -dstalpha input.tif output.tif
```

## Batch files

The biggest advantage of GDAL commands is that it is very easy to run the same command on many files with a for loop ([DOS](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/for), [Linux](http://stackoverflow.com/questions/9612090/how-to-loop-list-of-file-names-returned-by-find)) with wildcards ([DOS](https://docs.microsoft.com/en-us/previous-versions/windows/desktop/indexsrv/ms-dos-and-windows-wildcard-characters), [Linux](http://www.linfo.org/wildcard.html)) or batch file.

**DOS**

`FOR %i IN (input_folder/*.tif) DO gdal_translate -of ECW %i output_folder/%~ni.ecw`

* %i - file name, i could be changed to anything else
* IN (*.tif) - which files are selected, usually wildcards are useful here
* Modifications of the file name:
    *   %i = file path, name and extension: input_folder/map.tif
    *   %~ni = file name: map
    *   %~pni = file path and name: input_folder/map



### Linux

From command line:

`for i in *.shp; do echo ogrinfo $i -sql "CREATE SPATIAL INDEX ON ${i/.shp/}"; done`

From batch file:

```
    #!/bin/bash
    for i in $(find -name '*.tif')
    do
        echo $i
        gdal_translate $i ../infrared_lossless/${i/tif/jp2} -of JP2ECW -co target=0
    done
```

## Windos and Linux basic commands

*   Change working directory and list contents of it. DOS: [cd](http://www.computerhope.com/cdhlp.htm) and [dir](http://www.computerhope.com/dirhlp.htm). Linux: [cd](http://www.computerhope.com/unix/ucd.htm) and [ls](http://www.computerhope.com/unix/uls.htm).
*   Copy the folder hierarchy (without the files)
    *   Windows: [xcopy](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/xcopy) source destination /t /e (give the command in the folder, where source is)
    *   Linux: find -type d -exec [mkdir](http://www.computerhope.com/unix/umkdir.htm) ../compress95/{} \; (give the command in the folder from where you want to make the copy of)
*   Copy and delete files: DOS: [copy](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/copy) and [del](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/del). Linux: [cp](http://www.computerhope.com/unix/ucp.htm) and [rm](http://www.computerhope.com/unix/urm.htm).


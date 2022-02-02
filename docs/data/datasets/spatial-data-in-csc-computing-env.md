# Spatial data in CSC computing environment
## Spatial data in Puhti

Puhti has following datasets:

*   **Paituli data**. Paituli includes datasets from Finnish Digital and Population Data Services Agency, Finnish Food Agency, Finnish Meteorological Institute, Finnish Transport Infrastructure Agency, Institute for the languages of Finland, Karelia UAS, National Land Survey of Finland, Natural resource institute Finland, Statistics Finland and University of Helsinki..
    -   [Full list of Paituli datasets](https://paituli.csc.fi/metadata.html)
    -   All Paituli datasets have a readme-file with a link to Etsin dataset descriptions and terms of use.
    -   If in trouble finding some file, you can also use Paituli download page as help. You can see the dataset path under links (crop the beginning) or you can download the file list with "Download list of files" if the dataset has a lot of mapsheets.
    -   NLS normal color ortho images are not available in Puhti, but the infrared ones are.
    - Additions to NLS data:
        +   2m and 10m DEM and infrared orthophotos have virtual rasters, see Puhti virtual rasters below.
        +   Stereoclassified lidar data has been slightly modified. The original NLS data had mistakes in headers, these have been fixed. Additionally lax-index files have been added.
        + Automatically classified lidar data, only data of year 2019
*   **LUKE, multi-source national forest inventory**, 2013, 2015, 2017 and 2019. LUKE license changed in Aug 2019 to CC BY 4.0.
*   **SYKE, All open spatial datasets** available from [SYKE open data service](https://www.syke.fi/fi-FI/Avoin_tieto/Paikkatietoaineistot/Ladattavat_paikkatietoaineistot).
*   **Satellite mosaics produced by SYKE and FMI** in Paikkatietoalusta project, **added in 2020**
    -   [Sentinel1 SAR mosaics](https://ckan.ymparisto.fi/dataset/sentinel-1-sar-image-mosaic-s1sar-sentinel-1-sar-kuvamosaiikki-s1sar): 10/2019 ->, 3 mosaics per month
    -   [Sentinel2 index mosaics](https://ckan.ymparisto.fi/dataset/sentinel-2-image-index-mosaics-s2ind-sentinel-2-kuvamosaiikit-s2ind): 2018 ->, 2 mosaics per month, only during vegetation period, NDVI, NDBI, NDMI, NDTI, META.
    -   [Historical Landsat satellite image mosaics](https://ckan.ymparisto.fi/dataset/historical-landsat-satellite-image-mosaics-href-historialliset-landsat-kuvamosaiikit-href): 1985, 1990, 1995
    -   [Historical Landsat NDVI mosaics: 1984-2011](https://ckan.ymparisto.fi/dataset/historical-landsat-image-index-mosaics-hind-historialliset-landsat-kuvaindeksimosaiikit-hind)

NLS 2m DEM, lidar, infrared ortophotos, all SYKE datasets and satellite mosaics are updated in Puhti automatically every Monday.

The open spatial data is stored in Puhti: **/appl/data/geo**

Open spatial data in Puhti is maintained by CSC personnel. If you notice any problems with data or wish some new dataset, contact CSC Servicedesk.

### Puhti virtual rasters

CSC has added [virtual rasters](../../support/tutorials/gis/virtual-rasters.md) to NLS 2m and 10m elevation models and infrared ortophotos in Puhti. There are two variants of virtual rasters for the elevation models: 

1.  The **direct** virtual rasters contain directly the source tif images without any hierarchical structure, overviews or pre-calculated statistics. The direct virtual raster is meant for using **only in scripts**. It should **not** be opened in QGIS, unless zoomed in and need to open only a few files etc:
    *   2m DEM: `/appl/data/geo/mml/dem2m/dem2m_direct.vrt`
    *   10m DEM: `/appl/data/geo/mml/dem10m/dem10m_direct.vrt`
    *   infrared orthophotos: `/appl/data/geo/mml/orto/infrared_3067/infrared_euref_direct.vrt`

2.  The **hierarchical** virtual raster is mainly for **viewing** purposes for example with QGIS. It has a hierarchical structure where a virtual raster for each folder contains all the data stored in that folder and it's subfolders. The hierarchical file structure also contains statistics (min, max, mean, stddev) and overviews for each vrt file, which enables a fairly responsive viewing of the entire DEM dataset for example in QGIS. This way the whole dataset can be easily viewed at different zoom levels. You may use the lowest level virtual raster (for example M41 in the 2m DEM) also in scripts, higher level virtual rasters may cause computational errors.

    *   2m DEM: `/appl/data/geo/mml/dem2m/dem2m_hierarchical.vrt`
    *   10m DEM: `/appl/data/geo/mml/dem10m/dem10m_hierarchical.vrt`

#### Puhti: create virtual rasters of DEM for custom area

In some cases it might be useful to create virtual rasters that cover only your study area or some part of it. CSC has made a Python script for creating virtual rasters for custom area from NLS 2m and 10m DEM datasets in Puhti. It's used in the following way:

```
module load geoconda
python /appl/soft/geo/vrt/vrt_creator.py dataset polygon_file output_directory
```

Supported _dataset_ values are: dem2m, dem10m and demCombined. The last option prefers 2m DEM whenever it's available and interpolating rest of the areas to 2m resolution from 10m DEM using bicubic interpolation.

Optional arguments:

*   -i: create individual vrt for each polygon, default behavior is to create one vrt covering all polygons.
*   -o: create overviews
*   -p: output name prefix

## Spatial data in Allas

CSC computing services users are welcome to share spatial data in Allas with other users, if the data license terms allow this. This is a community service, meaning that any CSC user is welcome to contribute and add data to Allas. The data buckets in Allas are owned by data collaborators. If you would like some share some data you have in Allas, and would like the dataset be added to this page, contact CSC Servicedesk

Currently available:

1.  **[Sentinel2 2A level images](https://a3s.fi/sentinel-readme/README.txt)**. Maria Yli-Heikkilä (LUKE) has downloaded data of Finland from vegetation period (ca 10.5.-1.9.) in 2016-2020. 



## License and acknowledgement

In general all datasets have an open license, but the exact terms vary a bit, mostly CC-BY-4.0 licenses are in use. Check the readme-files for further info.

Please acknowlege the data producer according to license terms as well as CSC and Geoportti in your publications, it is important for project continuation and funding reports. If you use data provided in Allas, please also acknowledge the person sharing the data.
As an example, you can write "The authors wish to thank CSC - IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (Geoportti, urn:nbn:fi:research-infras-2016072513) for data provision".

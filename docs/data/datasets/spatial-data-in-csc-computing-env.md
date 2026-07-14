# Spatial data in CSC computing environment
## Spatial data in Roihu

The datasets listed below are provided through CSC-managed Roihu dataset
projects. They are mounted under `/dataset/<dataset-project-id>` and are
readable by all Roihu users. You do not need to create or join these dataset
projects.

Use the files directly from `/dataset`. If you need to modify a dataset,
copy the required files to your computational project's
`/scratch/<project-id>` directory first.

Roihu has the following datasets:

| Path | Dataset collection | Access and updates |
|------|--------------------|--------------------|
| `/dataset/project_2019680` | Paituli datasets | Read-only for Roihu users; selected NLS datasets updated weekly |
| `/dataset/project_2019679` | NLS automatically classified lidar | Read-only; updated weekly |
| `/dataset/project_2019681` | Finnish Forest Centre datasets | Read-only; update schedule varies by dataset |

More detail on each dataset:

*  In `/dataset/project_2019680` are **Paituli datasets**. Paituli includes datasets from Finnish Digital and Population Data Services Agency, Finnish Food Agency, Finnish Meteorological Institute, Finnish Transport Infrastructure Agency, Institute for the languages of Finland, Karelia UAS, National Land Survey of Finland, Natural resource institute Finland, Statistics Finland, Swedish University of Agricultural Sciences and University of Helsinki.
    -   [Full list of Paituli datasets](https://etsin.fairdata.fi/datasets?facet_keyword=Paituli)
    -   If in trouble finding some file, you can also use Paituli download page as help. You can see the dataset path under links (crop the beginning) or you can download the file list with "Download list of files" if the dataset has a lot of mapsheets.
    - NLS 2m DEM is updated in Roihu automatically every Monday.
    - Additions to NLS data:
        + 2m, 10m and 25m DEMs have virtual rasters, see Roihu virtual rasters below.
        + Stereoclassified lidar data has been slightly modified. The original NLS data had mistakes in headers, these have been fixed. Additionally lax-index files have been added.
    - The easiest way to find Paituli raster data is with [Paituli STAC](https://paituli.csc.fi/stac.html), it has also links to Roihu local files.
 
*  In `/dataset/project_2019679` is **[NLS, automatically classified lidar](https://www.maanmittauslaitos.fi/kartat-ja-paikkatieto/aineistot-ja-rajapinnat/tuotekuvaukset/laserkeilausaineisto-05-p)**, 2008->.
    * Includes index map in root folder.
    * Updated in Roihu automatically every Monday.

*  In `/dataset/project_2019681` are **Finnish Forest Centre** datasets:
    * [Canopy height model](https://www.paikkatietohakemisto.fi/geonetwork/srv/fin/catalog.search#/metadata/0e7ad446-2999-4c94-ad0d-095991d8f80a) Updated in Roihu automatically every Monday.
    * [Gridcells](http://www.paikkatietohakemisto.fi/geonetwork/srv/fin/catalog.search#/metadata/3fa1beeb-ea6b-42b1-8e76-eb2bc8ac6d24) For now in Roihu unfortunately only some of the files. All files will be added during autumn 2026.
    * [Forest mask](https://www.paikkatietohakemisto.fi/geonetwork/srv/fin/catalog.search#/metadata/df99fbd3-44b3-4ffc-b84a-9459f318d545) Updated 7/2026. Compared to Puhti, the files are unzipped in Roihu.
    * [Forest resource plots](http://www.paikkatietohakemisto.fi/geonetwork/srv/fin/catalog.search#/metadata/332e5abf-63c2-4723-9c2d-4a926bbe587a) 2022 version. Will be updated during autumn 2026.

All datasets have a readme-file with dataset name in Finnish and English and links to full dataset description and license.

Puhti had also:
* SYKE, All open spatial datasets available from [SYKE open data service](https://www.syke.fi/fi-FI/Avoin_tieto/Paikkatietoaineistot/Ladattavat_paikkatietoaineistot). Future undecied, inform CSC servicedesk if you need.
* NLS ortho images are not copied to Roihu. Access these via [Paituli STAC](https://paituli.csc.fi/stac).   
* [Historical Landsat satellite image mosaics](https://ckan.ymparisto.fi/dataset/historical-landsat-satellite-image-mosaics-href-historialliset-landsat-kuvamosaiikit-href): 1985, 1990, 1995. These will not be added to Roihu. [Paituli STAC](https://paituli.csc.fi/stac) includes SYKE's yearly Landsat mosaics, get data via STAC.
 
Accessing data in Roihu requires CSC user account with a project with Roihu service enabled. All Roihu users have **read** access to these datasets. You do not need to move the files: they can be used directly, unless you need to modify them, which requires you to make your own copy. Open spatial data in Roihu is maintained by CSC personnel. If you notice any problems with data or wish some new dataset, contact CSC Servicedesk.

### Roihu virtual rasters

Virtual rasters is a very practical concept for working with bigger raster datasets, see CSC [Virtual rasters](../../support/tutorials/gis/virtual-rasters.md) page for longer explanation and how to create own virtual rasters, inc from STAC search results.

### NLS DEM ready-made virtual rasters
CSC has added to some datasets virtual rasters to Roihu. There are two variants of virtual rasters for the elevation models:  

1.  The **direct** virtual rasters contain directly the source tif images without any hierarchical structure, overviews or pre-calculated statistics. The direct virtual raster is meant for using **only in scripts**. It should **not** be opened in QGIS, unless zoomed in and need to open only a few files etc:
    *   NLS 2m DEM: `/dataset/project_2019680/mml/dem2m/dem2m_direct.vrt`
    *   NLS 10m DEM: `/dataset/project_2019680/mml/dem10m/dem10m_direct.vrt`
    *   NLS 25m DEM: `/dataset/project_2019680/mml/dem25m/tif_cog/2000/dem25m.vrt`
    *   Several LUKE datasets also have .vrt files added.

2.  The **hierarchical** virtual raster is mainly for **viewing** purposes for example with QGIS. It has a hierarchical structure where a virtual raster for each folder contains all the data stored in that folder and it's subfolders. The hierarchical file structure also contains statistics (min, max, mean, stddev) and overviews for each vrt file, which enables a fairly responsive viewing of the entire DEM dataset for example in QGIS. This way the whole dataset can be easily viewed at different zoom levels. You may use the lowest level virtual raster (for example M41 in the 2m DEM) also in scripts, higher level virtual rasters may cause computational errors.

    *   NLS 2m DEM: `/appl/data/geo/mml/dem2m/dem2m_hierarchical.vrt`

## Paituli STAC
STAC is a great option to search and download raster data. [Paituli STAC](https://paituli.csc.fi/stac) currently includes around 175 Finnish raster datasets:

* ~125 datasets from Paituli. All Paituli datasets have 2 assets - one with public URL-link to data and one Puhti specific path. Puhti specific paths can and should be used ONLY when working on CSC supercomputer Puhti.
* [ESA, Sentinel-2 products](http://urn.fi/urn:nbn:fi:fd-e1007ae5-1529-3e5c-8bf2-b218c77e25a5), processed to Level-2A (Surface Reflectance), a selection of mostly cloud-free products from Finland. Downloaded to CSC Allas by Maria Yli-Heikkilä (LUKE), Arttu Kivimäki (NLS/FGI) and Matias Heino (Aalto).
* ~40 [Geoportti geocube datasets](https://vm0160.kaj.pouta.csc.fi/geocubes/datasets/), all recalculated to common grid at several different resolutions.
* 12 [datasets from FMI Tuulituhohaukka STAC catalog](https://pta.data.lit.fmi.fi/stac/root.json), including Sentinel-1, Sentinel-2 and Landsat mosaics and indices.

For usage tips and more information, see [Paituli STAC](https://paituli.csc.fi/stac) page.

These datasets are public, so anybody can download them, also from own computer or other services, Roihu access is not needed.

## License and acknowledgement

In general all datasets have an open license, but the exact terms vary a bit, mostly CC-BY-4.0 licenses are in use. Check the readme-files for further info.

Please acknowledge the data producer according to license terms as well as CSC and Geoportti in your publications, it is important for project continuation and funding reports. If you use data provided in Allas, please also acknowledge the person sharing the data.
As an example, you can write "The authors wish to thank CSC - IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (Geoportti, urn:nbn:fi:research-infras-2016072513) for data provision".

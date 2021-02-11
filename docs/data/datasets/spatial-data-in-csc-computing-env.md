# Spatial data in Puhti

Currently (Feb 2021) there are following datasets:

*   **Paituli data**. Paituli includes datasets from Finnish Digital and Population Data Services Agency, Finnish Food Agency, Finnish Meteorological Institute, Finnish Transport Infrastructure Agency, Institute for the languages of Finland, Karelia UAS, National Land Survey of Finland, Natural resource institute Finland, Statistics Finland and University of Helsinki..
    -   [Full list of Paituli datasets](https://paituli.csc.fi/metadata.html)
    -   All Paituli datasets have a readme-file with a link to Etsin dataset descriptions and terms of use.
    -   If in trouble finding some file, you can also use Paituli download page as help. You can see the dataset path under links (crop the beginning) or you can download the file list with "Download list of files" if the dataset has a lot of mapsheets.
    -   NLS normal color ortho images are not available in Puhti, but the infrared ones are.
    - Additions to NLS data:
        +   Dem 2m and 10m have virtual rasters, see [Puhti virtual rasters](/puhti-virtual-rasters).
        +   Stereoclassified lidar data has been slightly modified. The original NLS data had mistakes in headers, these have been fixed. Additionally lax-index files have been added.
        + Automatically classified lidar data, only data of year 2019
*   **LUKE, multi-source national forest inventory**, 2013, 2015 and 2017. LUKE license changed in Aug 2019 to CC BY 4.0.
*   **SYKE, All open spatial datasets** available from [SYKE open data service](https://www.syke.fi/fi-FI/Avoin_tieto/Paikkatietoaineistot/Ladattavat_paikkatietoaineistot).
*   **Satellite mosaics produced by SYKE and FMI** in Paikkatietoalusta project, **added in 2020**
    -   [Sentinel1 SAR mosaics](https://ckan.ymparisto.fi/dataset/sentinel-1-sar-image-mosaic-s1sar-sentinel-1-sar-kuvamosaiikki-s1sar): 10/2019 ->, 3 mosaics per month
    -   [Sentinel2 index mosaics](https://ckan.ymparisto.fi/dataset/sentinel-2-image-index-mosaics-s2ind-sentinel-2-kuvamosaiikit-s2ind): 2018 ->, 2 mosaics per month, only during vegetation period, NDVI, NDBI, NDMI, NDTI, META.
    -   [Historical Landsat satellite image mosaics](https://ckan.ymparisto.fi/dataset/historical-landsat-satellite-image-mosaics-href-historialliset-landsat-kuvamosaiikit-href): 1985, 1990, 1995
    -   [Historical Landsat NDVI mosaics: 1984-2011](https://ckan.ymparisto.fi/dataset/historical-landsat-image-index-mosaics-hind-historialliset-landsat-kuvaindeksimosaiikit-hind)

NLS 2m DEM, lidar, infrared ortophotos, all SYKE datasets and satellite mosaics are updated in Puhti automatically every Monday.

The open spatial data is stored in Puhti: **/appl/data/geo**

Open spatial data in Puhti is maintained by CSC personnel. If you notice any problems with data or wish some new dataset, contact CSC Servicedesk.


# Spatial data in Allas

CSC computing services users are welcome to share spatial data in Allas with other users, if the data license terms allow this. This is a community service, meaning that any CSC user is welcome to contribute and add data to Allas. The data buckets in Allas are owned by data collaborators. If you would like some share some data you have in Allas, and would like the dataset be added to this page, contact CSC Servicedesk

Currently available:

1.  **[Sentinel2 2A level images](https://a3s.fi/sentinel-readme/README.txt)**. Maria Yli-Heikkilä (LUKE) has downloaded data of Finland from vegetation period (ca 10.5.-1.9.) in 2016-2020. 

## License and citing

In general all datasets have an open license, but the exact terms vary a bit, mostly CC-BY-4.0 licenses are in use. Check the readme-files for further info.

In your publications please acknowledge the data producer according to the license terms, for Allas data the person who has shared data in Allas and also oGIIR and CSC, for example “The authors wish to acknowledge for provided data CSC – IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (oGIIR, urn:nbn:fi:research-infras-2016072513).”

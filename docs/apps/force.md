# FORCE 

FORCE (Framework for Operational Radiometric Correction for Environmental monitoring) is an all-in-one solution for mass-processing medium-resolution satellite images

## Available

__FORCE__ is available in Puhti with the following versions:

* 2.1

## Usage

FORCE is included in the __force__ module and can be loaded with

`module load force`

## Using FORCE

The following tools are available in FORCE. Notice __some of the commands have .sh in the end__

| Command                             | Description                                                                   |
|-------------------------------------|-------------------------------------------------------------------------------|
| force-level1-landsat.sh             | Maintenance of Level-1 data pool, Landsat                                     |
| force-level1-sentinel2_nv.sh        | Download of data and maintenance of Level-1 data pool, Sentinel-2 from Scihub |
| force-level1-sentinel2_nv_finhub.sh | Download of data and maintenance of Level-1 data pool, Sentinel-2 from Finhub |
| force-parameter-level2              | Generation ofparameter file skeleton for Level 2 processing                   |
| force-level2.sh                     | Level 2 processing of image archives                                          |
| force-l2ps                          | Level 2 processing of single image                                            |
| force-quicklook-level2.sh           | Generation of quicklooks of Level 2 products                                  |
| force-parameter-level3              | Generation of parameter file skeleton for Level 3 processing                  |
| force-level3                        | Level 3 processing                                                            |
| force-quicklook-level3.sh           | Generation of quicklooks of Level 3 products                                  |
| force-parameter-tsa                 | Generation of parameter file skeleton for time series processing              |
| force-tsa                           | Time series generation / analysis                                             |
| force-parameter-cso                 | Generation of parameter file skeleton for CSO processing                      |
| force-cso                           | Clear Sky Observations mining                                                 |
| force-parameter-improphe            | Generation of parameter file skeleton for ImproPhe processing                 |
| force-improphe                      | Improve spatial resolution of coarse continuous fields                        |
| force-parameter-l2imp               | Generation,of,parameter,file,skeleton for Level,2,ImroPhe processing          |
| force-l2imp                         | Improve spatial resolution of lower resolution Level2 ARD                     |
| force-lut-modis                     | Generation,and,maintenance,of,water,vapor,database,using MODIS products       |
| force                               | Print version and short disclaimer                                            |
| force-mosaic.sh                     | Virtual mosaicking of data products                                           |
| force-qai-inflate                   | Inflate QAI bit layers                                                        |
| force-tile-finder                   | Convert geographic coordinates to tile and pixel coordinates                  |
| force-tabulate-grid                 | Extract the processing grid as ESRI shapefile                                 |

## Using FORCE to download sentinel images

For downloading files with FORCE you need __ESA Scihub__ or __FMI Finhub__ credentials. FMI Finhub includes only 1C level data for Baltic sea drainage area, but should be faster than ESA Scihub. The credentials should be saved in your __home directory__, the ESA Scihub credentials to .scihub file and FMI Finhub credential to .finhub file. Username in the first row, password second.

The download scripts have been slightly modified for the CSC environment. For ESA Scihub use __force-level1-sentinel2_nv.sh__ script and for FMI Finhub __force-level1-sentinel2_nv_finhub.sh__. Both scripts follow the syntax in the user guide, see Pekka Hurskainen's presentation for examples.

## License and citing

FORCE is licensed under [the GNU GPL License](http://www.gnu.org/licenses/)

In your publications please acknowledge also oGIIR and CSC, for example “The authors wish to acknowledge for computational resources CSC – IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (oGIIR, urn:nbn:fi:research-infras-2016072513).”

### References

* [FORCE homepage](https://www.uni-trier.de/?id=63673)
* [FORCE user guide](https://www.uni-trier.de/fileadmin/fb6/prof/FER/Downloads/Software/FORCE/FORCE-user-guide-v-2-0.pdf)
* [Using FORCE in CSC environment (Taito) by Pekka Hurskainen](https://research.csc.fi/documents/48467/73370/Satellite_time_series_processing_with_FORCE_in_CSC_Hurskainen.pdf/c6960f88-ec94-4c94-aca3-734c8d283268)

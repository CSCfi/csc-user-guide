---
tags:
  - Free
catalog:
  name: PDAL
  description: for point cloud translations and processing
  license_type: Free
  disciplines:
    - Geosciences
  available_on:
    - LUMI
    - Mahti
    - Roihu
---

# PDAL

[PDAL](https://www.pdal.io/) is an open source command line application for point cloud translations and processing.

## Available

PDAL is available in the following versions:

* 2.10.1 - [QGIS-3.44.9 module](qgis.md) without pdal Python library, but with [pdal_wrench](https://github.com/PDAL/wrench), in Roihu
* 2.10.0 - [geoconda-3.14.5 module](geoconda.md) with pdal Python library, in Roihu
* 2.7.2 - [geoconda-3.11.9 module](geoconda.md) with pdal Python library, in Mahti
* 2.4.1 - [geoconda-3.10.6 module](geoconda.md) with pdal Python library, in Mahti
* 2.3.0 - [QGIS-3.31 module](qgis.md) without pdal Python library, in LUMI

## Usage

### Using pdal

For using PDAL, any of the modules listed about must be activated first, check the linked pages for details.

You can test if pdal loaded successfully with following

`pdal --help`

[Examples for using PDAL in Roihu](https://github.com/csc-training/geocomputing/tree/master/pdal).

### Finnish National Land Survey's lidar data in Roihu

The Finnish national [lidar data](https://www.maanmittauslaitos.fi/en/maps-and-spatial-data/expert-users/product-descriptions/laser-scanning-data) is already stored in Roihu, both the older stereo-classified version (`/dataset/project_2019680/mml/laserkeilaus/`) and the new automatically classified data (`/dataset/project_2019679/`). More info about [locally stored spatial datasets](https://research.csc.fi/gis_data_in_csc_computing_env).

## License 

PDAL is licensed with the BSD open source license. [The full PDAL licence](https://pdal.io/en/latest/copyright.html)

## Citation

```  PDAL contributors (2026). PDAL: The Point Data Abstraction Library, DOI: 10.5281/zenodo.2616780  ```



## Acknowledgement

Please acknowledge CSC and Geoportti in your publications, it is important for project continuation and funding reports.
As an example, you can write "The authors wish to thank CSC - IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (Geoportti, urn:nbn:fi:research-infras-2016072513) for computational resources and support".

## Installation

Please see the respectives versions module page: [Geoconda](./geoconda.md) , [QGIS](./qgis.md).


## References

* [PDAL homepage](https://pdal.io/)
* [LAS file example](https://pdal.io/en/latest/tutorial/las.html)


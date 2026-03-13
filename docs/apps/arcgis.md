---
tags:
  - Other
catalog:
  name: ArcGIS Python API
  description: Spatial analysis and data science
  license_type: Other
  disciplines:
    - Geosciences
  available_on:
    - Puhti
---
# ArcGIS Python API

!!! info "Note"
    CSC had an ArcGIS consortium until 31.12.2025. From 2026 onwards CSC does not provide ArcGIS licenses for Finnish universities.

The [ArcGIS API for Python](https://developers.arcgis.com/python/) is a powerful, modern Pythonic library that supports the latest releases of ArcGIS Enterprise and ArcGIS Online and provides a consistent programmatic experience for scripting and automating across the ArcGIS product suite. It is used for three key workflows:

* GIS organization administration: management of users, groups, items, and servers, customizing the look and feel of your ArcGIS Enterprise or ArcGIS Online organization
* Content management: authoring and publishing content (layers, web maps, services), cloning and moving content within and between organizations, editing and updating layers and services
* **Spatial analysis and data science**: data wrangling and engineering, working with spatial data as pandas dataframes, spatial analysis, mapping and visualization, machine learning and deep learning

For more details on what you can do with the API and a deep dive into the modules, please see the [Overview of the ArcGIS API for Python](https://developers.arcgis.com/python/latest/guide/overview-of-the-arcgis-api-for-python/).

Puhti ArcGIS Python API installation is based on [ESRI's arcgis_learn metapackage](https://developers.arcgis.com/python/latest/guide/install-and-set-up/deep-learning/) and includes also packages for deep learning.

Some parts of ArcGIS Python API require logging in to your home organization's ArcGIS Online. 

## Available

ArcGIS Python API is available in Puhti:

* 2.4.0.1 in `geoconda/3.12.10` module, see [geoconda page](geoconda.md)
* 2.1.0.3 in `arcgis-python-api` module

## Usage

Load the module

```bash
module load arcgis-python-api
```

To check the exact packages and versions included in the loaded module:

```bash
list-packages
```

## License

ArcGIS Python API is available under [Apache license 2.0](https://github.com/Esri/arcgis-python-api/blob/master/LICENSE). The module includes also several other libraries, which have their own licences. 

## Citation

Esri. (Year). ArcGIS API for Python (Version). https://developers.arcgis.com/python/

## Acknowledgement

Please acknowledge CSC and Geoportti in your publications, it is important for project continuation and funding reports.
As an example, you can write "The authors wish to thank CSC - IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (Geoportti, urn:nbn:fi:research-infras-2016072513) for computational resources and support".

## Installation

`arcgis-python-api` module was installed on Puhti using [Tykky's conda-containerize functionality](../computing/containers/tykky.md), using this [ArcGIS Python API conda environment file](https://github.com/csc-training/geocomputing/blob/master/supercomputer_installations/arcgis-python-api-2.1.0.yml).

## Other ArcGIS tools in CSC's computing environment

* ArcGIS Pro is available only for Windows operating system, which is unfortunately not supported in CSC's computing environment.
* ESRI provides [a wide range of server products](https://enterprise.arcgis.com/en/server/latest/get-started/windows/about-arcgis-server-licensing-roles.htm) for large scale spatial data analysis. These ArcGIS server products usually support Linux operating system and can be installed to [cPouta](../cloud/pouta/index.md).

---
tags:
  - Other
catalog:
  name: LAStools
  description: for LiDAR datasets
  license_type: Other
  disciplines:
    - Geosciences
  available_on:
    - Roihu
---

# LAStools

[LAStools](https://lastools.github.io/) is a collection of tools for LiDAR data processing.

## Usage

### Using LAStools

LAStools is included in following modules:

* lastools: 2026 (more exactly 260326) in Roihu

Load the newest version (default):

`module load lastools` 

The 2026 versions of LAStools are based on the new [native Linux version of LAStools](https://rapidlasso.de/lastools-linux/) and requires `64` at the end of all tools. You can test that the LAStools module is loaded successfully with

`lasinfo64 -h`

For using licensed tools for testing, use `-demo` in the command, see [Lastools documentation](https://rapidlasso.de/lastools-test-and-validate-in-demo-mode/) for more information.  

### LAStools commands

All lastool installations include the open source tools of LAStools.

* las2las - extracts last returns, clips, subsamples, translates, etc ...
* las2txt - turns LAS into human-readable and easy-to-parse ASCII
* lasdiff - compares the data of two LAS/LAZ/ASCII files 
* lasindex - creates a spatial index LAX file for fast spatial queries
* lasinfo - prints out a quick overview of the contents of a LAS file
* lasmerge - merges several LAS or LAZ files into a single LAS or LAZ file
* lasprecision - analyses the actual precision of the LIDAR points
* laszip - compresses the LAS files in a completely lossless manner
* txt2las - converts LIDAR data from ASCII text to binary LAS format

The 2026 version include also: `lasoptimize64, las2dem64, las2iso64, las2shp64, las2tin64, las3dpoly64, lasboundary64, lascanopy64, lasclassify64, lasclip64, lascolor64, lascontrol64, lascopy64, lasdatum64, lasdistance64, lasduplicate64, lasgrid64, lasground64, lasground_new64, lasheight64, lasintensity64, laslayers64, lasnoise64, lasoverage64, lasoverlap64, lasreturn64, lassort64, lassplit64, lasthin64, lastile64, lastrack64, lasvdatum64, lasvoxel64`. 2025 version has additionally: `blast2dem64, demdiff64, demzip64, e572las64, lascopcindex64, laslicman64, lasplanes64, lasprobe64 and shp2las64`. See the License for terms of use for these tools. 

2026 version supports multi-core processing.

In Roihu, only the command line tools are available, without the graphical user interface.

### Using a licensed version

CSC provides only the "free" version of LAStools. If you have your own license for LAStools, it can be also used. 

For using the native Linux version, copy the license file to your projects `projapp` directory and provide the license file location as environment variable before using the tools:

```
export LAStoolsLicenseFile=/projappl/project_200xxxx/yyy/lastoolslicense.txt
```

### Finnish National Land Survey's lidar data in Roihu

The Finnish national [lidar data](https://www.maanmittauslaitos.fi/en/maps-and-spatial-data/expert-users/product-descriptions/laser-scanning-data) is already stored in Roihu, both the older stereo-classified version (`/dataset/project_2019680/mml/laserkeilaus/`) and the new automatically classified data (`/dataset/project_2019679/`). More info about [locally stored spatial datasets](https://research.csc.fi/gis_data_in_csc_computing_env).

### LAStools with many files

If you are processing large number of lidar files with LAStools, it is possible in Roihu to process the files in parallel. 

* For using up to 386 cores (=1 node in Roihu), the best option would be using xargs - see [CSC GDAL parallel example](https://github.com/csc-training/geocomputing/tree/master/gdal) for details.
* For multi-node usage, see [Tutorial: xargs workflow for many small, independent runs](../support/tutorials/many.md).

## License 

For information on the legal use and licensing of LAStools, please read the [LAStools LICENSE](https://lastools.github.io/LICENSE.txt).

## Acknowledgement

If you use this software on Roihu, please acknowledge CSC and Geoportti in your publications, it is important for project continuation and funding reports.
As an example, you can write "The authors wish to thank CSC - IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (Geoportti, urn:nbn:fi:research-infras-2016072513) for computational resources and support".


## Citation

Citation of the software depends on which license was used:

* LAStools, "Efficient LiDAR Processing Software" (version 220613, academic), obtained from http://rapidlasso.com/LAStools
* M. Isenburg, "LAStools - efficient LiDAR processing software" (version 220613, unlicensed), obtained from http://rapidlasso.com/LAStools
* rapidlasso GmbH, "LAStools - efficient LiDAR processing software" (version 220613, commercial), obtained from http://rapidlasso.com/LAStools

## Installation
**2026 version** was installed using Singularity container based on [CSC's LasTools Apptrainer recipes](https://github.com/CSCfi/singularity-recipes/blob/main/lastools) and [Tykky's wrap-container functionality](../computing/containers/tykky.md#container-based-installations).

```
#2025 and 2026
wrap-container -w /opt/LAStools/bin lastools_2025.sif --prefix 2025
```


## References

* [LAStools homepage](https://lastools.github.io/)
* [LAStools Github](https://github.com/LAStools/LAStools)
* [LAStools examples and tutorials](https://rapidlasso.de/knowledge/)

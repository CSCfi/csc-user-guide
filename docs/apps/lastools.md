---
tags:
  - Other
---

# LAStools

[LAStools](https://lastools.github.io/) is a collection of tools for LiDAR data processing.

## Usage

### Using LAStools

LAStools is included in following modules:

* lastools: 2023 (more exactly 230914) and 2022 (220613)
* geoconda: 3.11.9, 3.10.9 and 3.10.6 (all with older 20171231)

Load one of these modules, for example the newest version (default):

`module load lastools` 

The 2023 version of LAStools is based on the new native Linux version of LAStools and requires `64` at the end of all tools. You can test that the LAStools module is loaded successfully with

`lasinfo64 -h`

For all older versions, for example in the **geoconda** module, you will need to omit the 64 at the end of the tool name, for example:

`lasinfo -h`

### LAStools commands

All lastool installations in Puhti include the open source tools of LAStools.

* las2las - extracts last returns, clips, subsamples, translates, etc ...
* las2txt - turns LAS into human-readable and easy-to-parse ASCII
* lasdiff - compares the data of two LAS/LAZ/ASCII files 
* lasindex - creates a spatial index LAX file for fast spatial queries
* lasinfo - prints out a quick overview of the contents of a LAS file
* lasmerge - merges several LAS or LAZ files into a single LAS or LAZ file
* lasprecision - analyses the actual precision of the LIDAR points
* laszip - compresses the LAS files in a completely lossless manner
* txt2las - converts LIDAR data from ASCII text to binary LAS format

The 2023 version includes also: `lasoptimize64, las2dem64, las2iso64, las2shp64, las2tin64, las3dpoly64, lasboundary64, lascanopy64, lasclassify64, lasclip64, lascolor64, lascontrol64, lascopy64, lasdatum64, lasdistance64, lasduplicate64, lasgrid64, lasground64, lasground_new64, lasheight64, lasintensity64, laslayers64, lasnoise64, lasoverage64, lasoverlap64, lasreturn64, lassort64, lassplit64, lasthin64, lastile64, lastrack64, lasvdatum64, lasvoxel64`. See the License for terms of use for these tools. [The native Linux version of LAStools](https://rapidlasso.de/release-of-lastoolslinux/) does not currently support multi-core processing.

In Puhti, only the command line tools are available, without the graphical user interface.

### Using a licensed version

CSC provides only the "free" version of LAStools. If you have your own license for LAStools, it can be used also in Puhti. 

For using the 2023 native Linux version, copy the license file to your projects projappl directory in Puhti and provide the license file location as environment variable before using the tools:

```
export LAStoolsLicenseFile=/projappl/project_200xxxx/yyy/lastoolslicense.txt
```

**Alternative:** Also using the licensed Windows version is possible with wine (Windows emulator). You can install the .exe files yourself for your project. Download and unzip __LAStools__ to your [projappl disk area](../computing/disk.md).

```
cd /projappl/<your_project>
wget https://lastools.github.io/download/LAStools.zip
unzip LAStools.zip
```

Then add your license file to the /bin folder and you can start running the __.exe__ files with __wine64__

Notice you can only use the 64-bit versions of the tools with wine64

Here is an example of running __lasinfo64.exe__ with __wine64__

```
module load wine
wine64 lasinfo64.exe -i <LAS file>
```


### Finnish National Land Survey's lidar data in Puhti

The Finnish national [lidar data](https://www.maanmittauslaitos.fi/en/maps-and-spatial-data/expert-users/product-descriptions/laser-scanning-data) is already stored in Puhti. You can find it from filepath: __/appl/data/geo/mml/laserkeilaus__. [More info](https://research.csc.fi/gis_data_in_csc_computing_env).

### LAStools with many files

If you are processing large number of lidar files with LAStools, it is possible in Puhti to process the files in parallel. 

* For using up to 40 cores (=1 node in Puhti), the best option would be using GNU parallel - see [CSC GDAL parallel example](https://github.com/csc-training/geocomputing/tree/master/gdal) for details.
* For multi-node usage, see [Tutorial: GNU Parallel workflow for many small, independent runs](../support/tutorials/many.md).

## License 

For information on the legal use and licensing of LAStools, please read the [LAStools LICENSE](https://lastools.github.io/LICENSE.txt).

## Acknowledgement

If you use this software on Puhti, please acknowledge CSC and Geoportti in your publications, it is important for project continuation and funding reports.
As an example, you can write "The authors wish to thank CSC - IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (Geoportti, urn:nbn:fi:research-infras-2016072513) for computational resources and support".


## Citation

Citation of the software depends on which license was used:

* LAStools, "Efficient LiDAR Processing Software" (version 220613, academic), obtained from http://rapidlasso.com/LAStools
* M. Isenburg, "LAStools - efficient LiDAR processing software" (version 220613, unlicensed), obtained from http://rapidlasso.com/LAStools
* rapidlasso GmbH, "LAStools - efficient LiDAR processing software" (version 220613, commercial), obtained from http://rapidlasso.com/LAStools

## Installation
**2023 version** was installed to Puhti using Singularity container based on [CSC's LasTools Apptrainer recipy](https://github.com/CSCfi/singularity-recipes/blob/main/lastools/lastools_2023.def) and [Tykky's wrap-container functionality](../computing/containers/tykky.md#container-based-installations).

`wrap-container -w /opt/LAStools lastools.sif --prefix 2023`

**2022 version** was installed to Puhti with [Tykky's wrap-container functionality](../computing/containers/tykky.md#container-based-installations) using the [LAStools Docker image from Dockerhub](https://hub.docker.com/r/pydo/lastools). 

`wrap-container -w /opt/LAStools docker//:pydo/lastools:latest --prefix 2022`


## References

* [LAStools homepage](https://lastools.github.io/)
* [LAStools Github](https://github.com/LAStools/LAStools)
* [LAStools examples and tutorials](https://rapidlasso.de/knowledge/)

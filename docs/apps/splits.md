# SPLITS

SPLITS (Spline Analysis of Time Series) is a software package to analyze time series of remotely sensed parameters such as vegetation indices.

## Available

__SPLITS__ is available in Puhti with the following versions:

* 1.11
* 1.10

## Usage

SPLITS is included in the __splits__ module. The __gcc__ module needs to be loaded also. You can load these with

`module load gcc splits`

By default the latest __splits__ module is loaded. If you want a specific version you can specify the version number

`module load gcc splits/<VERSION_NUMBER>`

## Using SPLITS

SPLITS is a command line tool. The following commands are available  

* peakcal - analyze the structure of bottoms and peaks in a phenological time series
* phencal - calculate phenological parameters from a fitted spline model
* prepro - preprocess MODIS data to be used with SPLITS
* splcal - use a fitted spline model to interpolate data
* splfit - fit a spline model to a time series image
* splview - graphical user interface for spline model exploration

More detailed manual can be found from the following path

`/appl/spack/install-tree/gcc-9.1.0/splits-1.11-tx4u6g/share/man/man1`

## License and acknowledgement

SPLITS is licensed under [the GNU GPL License](https://www.gnu.org/licenses/gpl-3.0.de.html))

Please acknowledge CSC and Geoportti in your publications, it is important for project continuation and funding reports.
As an example, you can write "The authors wish to thank CSC - IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (Geoportti, urn:nbn:fi:research-infras-2016072513) for computational resources and support".

### References

* [SPLITS homepage](http://sebastian-mader.net/splits/)


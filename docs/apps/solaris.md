# Solaris

[Solaris](https://step.esa.int/main/toolboxes/snap/) is a python toolbox for running tensorflow and pytorch machine learning pipelines for geospatial data.

## Available

__Solaris__ is available in Puhti with following versions:

* 0.1.3 (with tensorflow 1.13.1 and pytorch 1.1.0)

## Usage

Solaris is included in the __solaris__ module and can be loaded with

`module load solaris`

Solaris module includes a conda environment that has the Solaris library and many additional geospatial and machine learning libraries

!!! note
    For this version of Solaris, you should choose to use pytorch on your scripts as the included tensorflow can't use Puhti GPU at the moment due to incompatibility issues

## Additional Python libraries in the solaris module

* pandas (0.24.2)
* geopandas (0.5.0)
* rasterio (1.0.24)
* scikit-image (0.15.0)
* gdal (2.4.1)
* networkx (2.3)
* tensorflow (1.13.1)
* pytorch (1.1.0)

## License and citing

Solaris toolset is licensed with Apache Licence 2.0. Read the full license [here](https://github.com/CosmiQ/solaris/blob/master/LICENSE.txt).

In your publications please acknowledge also oGIIR and CSC, for example “The authors wish to acknowledge for computational resources CSC – IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (oGIIR, urn:nbn:fi:research-infras-2016072513).”

### References

* [Solaris homepage](https://solaris.readthedocs.io/en/latest/)
* [Solaris github](https://github.com/CosmiQ/solaris)
* [CSC example pipeline](https://github.com/csc-training/geocomputing/tree/master/machineLearning/cnn)

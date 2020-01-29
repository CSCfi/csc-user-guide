# Solaris

[Solaris](https://step.esa.int/main/toolboxes/snap/) is a python toolbox for running tensorflow and pytorch machine learning pipelines for geospatial data.

## Available

__Solaris__ is available in Puhti with following versions:

* 0.2.1 (with tensorflow 1.13.1 and pytorch 1.3.1)

## Usage

Solaris is included in the __solaris__ module and can be loaded with

`module load solaris`

Solaris module includes a conda environment that has the Solaris library and many additional geospatial and machine learning libraries

## Additional Python libraries in the solaris module

* pandas (0.25.3)
* geopandas (0.6.2)
* rasterio (1.1.0)
* scikit-image (0.16.2)
* gdal (3.0.2)
* networkx (2.4)
* tensorflow (1.13.1)
* pytorch (1.3.1)
* And many more, for retrieving the full list in Puhti use:
    `list-packages`

## License and citing

Solaris toolset is licensed with Apache Licence 2.0. Read the full license [here](https://github.com/CosmiQ/solaris/blob/master/LICENSE.txt).

In your publications please acknowledge also oGIIR and CSC, for example “The authors wish to acknowledge for computational resources CSC – IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (oGIIR, urn:nbn:fi:research-infras-2016072513).”

### References

* [Solaris homepage](https://solaris.readthedocs.io/en/latest/)
* [Solaris github](https://github.com/CosmiQ/solaris)
* [CSC example pipeline](https://github.com/csc-training/geocomputing/tree/master/machineLearning/cnn)

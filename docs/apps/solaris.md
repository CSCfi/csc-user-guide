# Solaris

[Solaris](https://solaris.readthedocs.io) is a python toolbox for running tensorflow and pytorch machine learning pipelines for geospatial data.

## Available

__Solaris__ is available in Puhti with following versions:

* 0.1.3 (with pytorch 1.1.0)
* 0.3.0 (with pytorch 1.6.0)

## Usage

Solaris is included in the __solaris__ module and can be loaded with

`module load solaris`

Solaris module includes a conda environment that has the Solaris library and many additional geospatial and machine learning libraries

!!! note
    In Puhti use Solaris only with pytorch, the included tensorflow can't use Puhti GPU at the moment due to incompatibility issues

## Additional Python libraries in the solaris module

* gdal 
* pandas 
* geopandas 
* networkx 
* rasterio 
* scikit-image 
* And many more, for retrieving the full list in Puhti use:
    `list-packages`

## License and citing

Solaris toolset is licensed with Apache Licence 2.0. Read the full license [here](https://github.com/CosmiQ/solaris/blob/master/LICENSE.txt).

In your publications please acknowledge also oGIIR and CSC, for example “The authors wish to acknowledge for computational resources CSC – IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (oGIIR, urn:nbn:fi:research-infras-2016072513).”

### References

* [Solaris homepage](https://solaris.readthedocs.io)
* [Solaris github](https://github.com/CosmiQ/solaris)
* [CSC example pipeline](https://github.com/csc-training/geocomputing/tree/master/machineLearning/cnn)

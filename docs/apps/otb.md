---
tags:
  - Free
---

# Orfeo ToolBox (Open Source processing of remote sensing images) 

[Orfeo ToolBox](https://www.orfeo-toolbox.org/) or OTB is an open source application for processing high resolution optical, multispectral and radar images at the terabyte scale.

## Available

Orfeo ToolBox is available in the following versions:

* Puhti: 8.0.1

## Usage

### Loading Orfeo ToolBox

Orfeo ToolBox can be loaded with

`module load orfeotoolbox`

### Using the command line tools

You can find the numerous **OTB applications** and examples of them from the [OTB CookBook](https://www.orfeo-toolbox.org/CookBook/Applications.html)

For example, you can calculate NDVI from a Sentinel virtual raster by using the **otbcli_RadiometricIndices** application. This requires NIR band to be in the first channel and RED band in the second

`otbcli_RadiometricIndices -in <virtual raster> -channels.nir 1 -channels.red 2 -list Vegetation:NDVI -out <output_file>`

### Using the OTB Python tools

The applications included in OTB can also be run by using the Python bindings included in the module.

Here's an example how to run mean raster calculation on a test virtual raster with Python.

```
import otbApplication as otb

fp = <INPUT RASTER FILEPATH>

out = <OUTPUT RASTER FILEPATH>

app = otb.Registry.CreateApplication("Smoothing")
app.SetParameterString("in", fp)
app.SetParameterString("type", "mean")
app.SetParameterString("out", out)
app.ExecuteAndWriteOutput()
```

### Using the graphical tools

Start [Monteverdi](https://www.orfeo-toolbox.org/CookBook-8.0/Monteverdi.html):
```
monteverdi
```
Also other graphical tools available, see 'ls /appl/soft/geo/orfeotoolbox/8.0.1/bin/otbgui*' for full list. 

### Running OTB applications in parallel 

OTB applications seem to scale the number of processing threads automatically which means that the applications generally run faster when given more CPU cores. 

Here is an example batch job script with 4 CPU cores

```
#!/bin/bash
#SBATCH --job-name=<name_of_your_job>
#SBATCH --account=<your_project>
#SBATCH --time=00:03:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem-per-cpu=2000
#SBATCH --partition=small

module load otb

otbcli_RadiometricIndices -in test_vrt.vrt -channels.nir 1 -channels.red 2 -list Vegetation:NDVI -out NDVI.tif
```

!!! note
    It is also possible to run OTB in parallel in several computing nodes [using MPI](https://www.orfeo-toolbox.org/CookBook/CliInterface.html#parallel-execution-with-mpi) but it has not been tested yet on Puhti

## License 

Orfeo ToolBox is licensed under the Apache License, Version 2.0. [The full Orfeo ToolBox licence](https://github.com/orfeotoolbox/OTB/tree/develop/Copyright)

## Citation

`Grizonnet, M., Michel, J., Poughon, V. et al. Orfeo ToolBox: open source processing of remote sensing images. Open geospatial data, softw. stand. 2, 15 (2017). https://doi.org/10.1186/s40965-017-0031-6`



## Acknowledgement

Please acknowledge CSC and Geoportti in your publications, it is important for project continuation and funding reports.
As an example, you can write "The authors wish to thank CSC - IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (Geoportti, urn:nbn:fi:research-infras-2016072513) for computational resources and support".


## Installation

Orfeo Toolbox was installed to Puhti with [Tykky's wrap-container functionality](../computing/containers/tykky.md#container-based-installations) using the [Orfeo Toolbox Docker image from Dockerhub provided by OTB community](https://hub.docker.com/r/orfeotoolbox/otb). 

`wrap-container -w /opt/otb/bin,/usr/bin/python3 docker://orfeotoolbox/otb:8.0.1 --prefix install_dir`


## References

* [Orfeo ToolBox homepage](https://www.orfeo-toolbox.org/)
* [Orfeo ToolBox general documentation](https://www.orfeo-toolbox.org/CookBook/)
* [Orfeo ToolBox Python API documentation](https://www.orfeo-toolbox.org/PythonDoc/)


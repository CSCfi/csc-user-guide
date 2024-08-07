---
tags:
  - Free
---

# WhiteboxTools

[WhiteboxTools](https://www.whiteboxgeo.com/manual/wbt_book/intro.html) is an advanced geospatial data analysis platform which includes more than 450 tools. Many tools operate in parallel, taking full advantage of your multi-core processor.

## Available

Only WhiteboxTools Open Core tools are available on Puhti. WhiteboxTools is available with following versions:

* 2.3.5 in 3.11.9 **geoconda** module
* 2.2.0 in 3.10.x **geoconda** modules
* 2.1.0 in the **WhiteboxTools** module 

## Usage

Load a module, select module based on version:

```
module load geoconda
```

Or `module load whiteboxtools` if you want to use the older version.

To check whiteboxtools version
```
whitebox_tools --version
```

Here is an example of calculating Hillshade for a 10m DEM. 

```
whitebox_tools -r=Hillshade -v -i=/appl/data/geo/mml/dem10m/2019/M3/M34/M3444.tif -o=test_hillshade.tif --azimuth=315.0 --altitude=30.0
```

!!! note
    Whiteboxtools seem to have problems with Finnish NLS lidar files.

## Example batch job script

```
#!/bin/bash
#SBATCH --account=<YOUR-PROJECT>
#SBATCH --cpus-per-task=1
#SBATCH --partition=small
#SBATCH --time=00:10:00
#SBATCH --mem=2G

module load whiteboxtools
whitebox_tools -r=Hillshade -v -i=/appl/data/geo/mml/dem10m/2019/M3/M34/M3444.tif -o=test_hillshade.tif --azimuth=315.0 --altitude=30.0
```

## License 

The WhiteboxTools open-core platform is distributed under the MIT license. [The full WhiteboxTools license](https://www.whiteboxgeo.com/manual/wbt_book/license.html)

## Citation

`Lindsay, J.B. (2014) The Whitebox Geospatial Analysis Tools project and open-access GIS, Proceedings of the GIS Research UK 22nd Annual Conference, The University of Glasgow, 16-18 April, DOI: 10.13140/RG.2.1.1010.8962.`



## Acknowledgement

Please acknowledge CSC and Geoportti in your publications, it is important for project continuation and funding reports.
As an example, you can write "The authors wish to thank CSC - IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (Geoportti, urn:nbn:fi:research-infras-2016072513) for computational resources and support".


## Installation

Whiteboxtools are part of [Geoconda installation](./geoconda.md#installation).


## References

* [WhiteboxTools User Manual](https://www.whiteboxgeo.com/manual/wbt_book/intro.html)
* [Whitebox Geospatial Inc](https://www.whiteboxgeo.com/)
* [WhiteboxTools Github](https://github.com/jblindsay/whitebox-tools)




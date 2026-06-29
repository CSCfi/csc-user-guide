---
tags:
  - Free
catalog:
  name: WhiteboxTools
  description: an advanced geospatial data analysis platform
  license_type: Free
  disciplines:
    - Geosciences
  available_on:
    - Puhti
    - LUMI
    - Roihu
---

# WhiteboxTools

[Whitebox Next Gen](https://www.whiteboxgeo.com/products-wbw.html) is an advanced geospatial data analysis platform which includes more than 700 tools. Many tools operate in parallel, taking full advantage of your multi-core processor.

## Available

Only WhiteboxTools Open Core tools are available. WhiteboxTools is available with following versions:

* 2.4.0 in 3.14.5 **python-geo** module, includes also Whitebox Workflows for Python, in Roihu
* 2.4.0 in 3.14.3 **geoconda** module, includes also Whitebox Workflows for Python, in Puhti and LUMI.
* 2.4.0 in 3.11.10 **geoconda** module, in Puhti and LUMI.
* 2.3.5 in 3.11.9 **geoconda** module, in Puhti.
* 2.2.0 in 3.10.x **geoconda** modules, in Puhti.
* 2.1.0 in the **WhiteboxTools** module, in Puhti.

## Usage

Load a module, select module based on version:

```
# Roihu
module load python-geo

# Puhti/LUMI
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

module load python-geo
whitebox_tools -r=Hillshade -v -i=/appl/data/geo/mml/dem10m/2019/M3/M34/M3444.tif -o=test_hillshade.tif --azimuth=315.0 --altitude=30.0
```

## License 

The WhiteboxTools open-core platform is distributed under the MIT OR Apache-2.0 license. [The full WhiteboxTools license](https://github.com/jblindsay/whitebox_next_gen/blob/main/docs/legal/PRO_LICENSING_NOTICE.md)

## Citation

Lindsay, J.B. (2026). Whitebox Next Generation [Software]. Whitebox Geospatial Inc.


## Acknowledgement

Please acknowledge CSC and Geoportti in your publications, it is important for project continuation and funding reports.
As an example, you can write "The authors wish to thank CSC - IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (Geoportti, urn:nbn:fi:research-infras-2016072513) for computational resources and support".


## Installation

Whiteboxtools are part of [Geoconda](./geoconda.md#installation) or  [Python-geo](./python-geo.md#installation) installation.


## References

* [Whitebox Next Gen Github](https://github.com/jblindsay/whitebox_next_gen/)
* [User documentation](https://github.com/jblindsay/whitebox_next_gen/tree/main/crates/wbw_python)



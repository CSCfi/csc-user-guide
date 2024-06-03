---
tags:
  - Free
---

# Sen2Cor

[Sen2Cor](https://step.esa.int/main/snap-supported-plugins/sen2cor/) is a stand-alone processor for Sentinel-2 Level 2A product generation and formatting.

## Available

__Sen2Cor__ is available in Puhti with following versions:

* 2.10 (pre-release)
* 2.9

## Usage

Sen2Cor is included in the __sen2cor__ module and can be loaded with

`module load sen2cor`

You run the program with the command

`L2A_Process <arguments>`

More information on the available arguments can be displayed with

`L2A_Process --help`

or from [the Sen2Cor user manual](https://step.esa.int/thirdparties/sen2cor/2.10.0/docs/S2-PDGS-MPC-L2A-SRN-V2.10.0.pdf).

## Advanced usage

Further configuration of `L2A_Process` can be done via the `L2A_GIPP.xml` file. 
After running `L2A_Process` for the first time, you can find the default GIPP file in your `$HOME/sen2cor/2.10/cfg` directory. 
Here you can adjust it to your needs using any editor and add it to the call: `L2A_Process --GIP_L2A $HOME/sen2cor/2.10/cfg/L2A_GIPP.xml <other arguments>` .

## License 

Sen2Cor is published under the [GPL-3](https://www.gnu.org/licenses/gpl.html) license.


## Citation

` M. Main-Knorn, B. Pflug, J. Louis, V. Debaecker, U. Müller-Wilm, F. Gascon, "Sen2Cor for Sentinel-2", Proc. SPIE 10427, Image and Signal Processing for Remote Sensing XXIII, 1042704 (2017)`


## Acknowledgement

Please acknowledge CSC and Geoportti in your publications, it is important for project continuation and funding reports.
As an example, you can write "The authors wish to thank CSC - IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (Geoportti, urn:nbn:fi:research-infras-2016072513) for computational resources and support".


## Installation

Sen2cor was installed on Puhti using [ESAs standalone Sen2cor installer for Linux](https://step.esa.int/main/snap-supported-plugins/sen2cor/).


## References

* [Sen2Cor user manual](https://step.esa.int/thirdparties/sen2cor/2.10.0/docs/S2-PDGS-MPC-L2A-SRN-V2.10.0.pdf)
* [Sen2Cor v2.10 release notes ](http://step.esa.int/thirdparties/sen2cor/2.10.0/docs/S2-PDGS-MPC-L2A-SRN-V2.10.0.pdf)
* [Sen2Cor user forum](https://forum.step.esa.int/c/optical-toolbox/sen2cor)


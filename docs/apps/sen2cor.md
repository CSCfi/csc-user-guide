# Sen2Cor

[Sen2Cor](http://step.esa.int/main/third-party-plugins-2/sen2cor/sen2cor_v2-8/) is a stand-alone processor for Sentinel-2 Level 2A product generation and formatting.

## Available

__Sen2Cor__ is available in Puhti with following versions:

* 2.8

## Usage

Sen2Cor is included in the __sen2cor__ module and can be loaded with

`module load sen2cor`

You run the program with the command

`L2A_Process <arguments>`

More information on the available arguments can be displayed with

`L2A_Process --help`

or from [the Sen2Cor user manual](http://step.esa.int/thirdparties/sen2cor/2.8.0/docs/S2-PDGS-MPC-L2A-SUM-V2.8.pdf).

## Parallel processing

Sen2Cor supports parallel processing for products with more than one tile. By default the number of cores used is set to AUTO which equals as many as there are available. You can configure that in the file __L2A-GIPP.xml__ which can be found in __$HOME/.sen2cor/cfg__ after running the program the first time. As Sen2Cor supports parallelisation only with shared memory, you can only use one CSC computing node (40 CPU cores) at a time for a parallel batch job. If you need more cpu cores, you can run the jobs with [Puhti array jobs](../computing/running/array-jobs)

Note that if you have only one tile, extra cores won't speed up processing.

## License and citing

Sen2Cor is published under the [GPL-3](https://www.gnu.org/licenses/gpl.html) license.

In your publications please acknowledge also oGIIR and CSC, for example “The authors wish to acknowledge for computational resources CSC – IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (oGIIR, urn:nbn:fi:research-infras-2016072513).”

### References

* [Sen2Cor user manual](http://step.esa.int/thirdparties/sen2cor/2.8.0/docs/S2-PDGS-MPC-L2A-SUM-V2.8.pdf)
* [Sen2Cor v2.8 release notes ](http://step.esa.int/thirdparties/sen2cor/2.8.0/docs/S2-PDGS-MPC-L2A-SRN-V2.8.pdf)
* [Sen2Cor user forum](https://forum.step.esa.int/c/s2tbx/sen2cor)


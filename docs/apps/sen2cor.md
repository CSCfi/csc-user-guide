# Sen2Cor

[Sen2Cor](http://step.esa.int/main/snap-supported-plugins/sen2cor/sen2cor-v2-9/) is a stand-alone processor for Sentinel-2 Level 2A product generation and formatting.

## Available

__Sen2Cor__ is available in Puhti with following versions:

* 2.9
* 2.8

## Usage

Sen2Cor is included in the __sen2cor__ module and can be loaded with

`module load sen2cor`

You run the program with the command

`L2A_Process <arguments>`

More information on the available arguments can be displayed with

`L2A_Process --help`

or from [the Sen2Cor user manual](http://step.esa.int/thirdparties/sen2cor/2.9.0/docs/S2-PDGS-MPC-L2A-SUM-V2.9.0.pdf).

## Advanced usage

Further configuration of `L2A_Process` can be done via the `L2A_GIPP.xml` file. 
After running `L2A_Process` for the first time, you can find the default GIPP file your $HOME/sen2cor/2.9/cfg directory. Here you can adjust it to your needs using any editor and add it to the call: L2A_Process --GIP_L2A $HOME/sen2cor/2.9/cfg/L2A_GIPP.xml <other arguments>

## License and citing

Sen2Cor is published under the [GPL-3](https://www.gnu.org/licenses/gpl.html) license.

In your publications please acknowledge also oGIIR and CSC, for example “The authors wish to acknowledge for computational resources CSC – IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (oGIIR, urn:nbn:fi:research-infras-2016072513).”

### References

* [Sen2Cor user manual](http://step.esa.int/thirdparties/sen2cor/2.9.0/docs/S2-PDGS-MPC-L2A-SUM-V2.9.0.pdf)
* [Sen2Cor v2.9 release notes ](http://step.esa.int/thirdparties/sen2cor/2.9.0/docs/S2-PDGS-MPC-L2A-SRN-V2.9.0.pdf)
* [Sen2Cor user forum](https://forum.step.esa.int/c/s2tbx/sen2cor)


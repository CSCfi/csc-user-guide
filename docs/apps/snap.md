# SNAP

[SNAP](https://step.esa.int/main/toolboxes/snap/) (Sentinel Application Platform) is a remote sensing toolbox architecture developed by the European Space Agency. It includes tools for all relevant remote sensing satellites.

## Available

__SNAP__ is available in Puhti with following versions:

* 7.0.0 (with snappy 6.0 and python 2.7.5)

### Installed plug-ins

* Sentinel toolboxes (1,2,3)
* All Idepix processors
* SMOS toolbox
* SNAPHU
* Radarsat toolbox
* PROBA-V toolbox
* Sen2Cor (external tool)

## Usage

### Using SNAP with graphical user interface

SNAP is included in the __snap__ module and can be loaded with

`module load snap`

If you have connected with a ssh connection that has __X11 forwarding__ enabled, you can launch a graphical user interface of SNAP with

`snap`

For __X11 forwarding__ to be enabled you need to install a suitable program for your own computer first (unless you are using Linux or Mac). You can read instructions how to do that [here](../computing/connecting.md#Using graphics)

### Graph Processing Tool (gpt) command

The Graph Processing Tool __gpt__ is a command line tool used for bulk processing. 

There is a also a custom __gpt_array__ command that allows the usage of gpt with [Puhti array jobs](../computing/running/array-jobs). It solves the problem of multiple jobs using and creating a cache folder to the same location. It can be used for example in the following way.

`gpt_array /scratch/<project>/snap_cache/tmp_snap_userdir_"$SLURM_ARRAY_TASK_ID" <normal gpt arguments>`

### Python library snappy

It is also possible to access SNAP functionalities from Python with the __snappy__ Python library. When loading the snap module like above, a conda environment is also loaded that has python 2.7 and snappy installed so you can just start python and import snappy. This conda environment also includes pandas, numpy, geopandas, rasterio, rasterstats and spyder. If you need additional libraries, contact __servicedesk@csc.fi__.

## License and citing

All SNAP software is published under the [GPL-3](https://www.gnu.org/licenses/gpl.html) license and its sources are available on [GitHub](https://github.com/senbox-org/).

In your publications please acknowledge also oGIIR and CSC, for example “The authors wish to acknowledge for computational resources CSC – IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (oGIIR, urn:nbn:fi:research-infras-2016072513).”

### References

* [SNAP homepage](http://step.esa.int/main/toolboxes/snap/)
* [SNAP wiki](https://senbox.atlassian.net/wiki/spaces/SNAP/overview)
* [SNAP tutorials](http://step.esa.int/main/doc/tutorials/)
* [snappy Python examples](https://senbox.atlassian.net/wiki/spaces/SNAP/pages/19300362/How+to+use+the+SNAP+API+from+Python)

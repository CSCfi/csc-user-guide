# SNAP

[SNAP](https://step.esa.int/main/toolboxes/snap/) (Sentinel Application Platform) is a remote sensing toolbox architecture developed by the European Space Agency. It includes tools for all common remote sensing satellites.

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

SNAP is included in the __snap__ module and can be loaded with

`module load snap`

### Using SNAP with graphical user interface

If you have connected with a ssh connection that has __X11 forwarding__ enabled, you can launch a graphical user interface of SNAP with

`snap`

For __X11 forwarding__ to be enabled you need to install a suitable program for your own computer first (unless you are using Linux or Mac). You can read instructions how to do that [here](../computing/connecting.md)

!!! note
    Do not run long CPU intensive jobs on the login nodes! This means you can't run computationally intensive analysis on graphical user interfaces on Puhti until interactive Puhti-shells are made available later in 2019. Use the batch job system on Puhti or run analysis on taito-shell.

### Using SNAP with Graph Processing Tool (gpt) command

The Graph Processing Tool __gpt__ is a command line tool used for bulk processing. It can be run with

`gpt <full_path_to_graph_xml_file> -Pfile=<inputfile> -t <outputfile>`

Some relevant __gpt__ options include

* __-q__    Number of threads the gpt instance will use. Set it to the number of CPU cores requested or more
* __-c__    Cache size in bytes. Change this if storage space becomes an issue
* __-x__    Clear internal tile cache after writing a complete row of tiles to output file. Add this if memory becomes an issue

More information on the [SNAP command line tutorial](http://step.esa.int/docs/tutorials/SNAP_CommandLine_Tutorial.pdf)

There is a also a custom made __gpt_array__ command that allows the usage of gpt with [Puhti array jobs](../computing/running/array-jobs.md). It solves the problem of multiple jobs using the same cache folder. The command is otherwise the same as __gpt__ but you include the cache-folder's path as first argument. In an array job you can define that cache folder dynamically with the iterating environment variable __$SLURM_ARRAY_TASK_ID__ and make sure each job has an individual cache folder.

`gpt_array /scratch/<project>/snap_cache/tmp_snap_userdir_"$SLURM_ARRAY_TASK_ID" <normal gpt arguments>`

### Using SNAP with the Python library snappy

It is also possible to access SNAP functionalities from Python with the __snappy__ Python library. When loading the snap module with `module load snap`, a conda environment is also loaded that has __python 2.7__ and __snappy__ installed so you can just start python and import snappy. This conda environment also includes pandas, numpy, geopandas, rasterio, rasterstats and spyder. If you need additional libraries, contact __servicedesk@csc.fi__.

## License and citing

All SNAP software is published under the [GPL-3](https://www.gnu.org/licenses/gpl.html) license and its sources are available on [GitHub](https://github.com/senbox-org/).

In your publications please acknowledge also oGIIR and CSC, for example “The authors wish to acknowledge for computational resources CSC – IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (oGIIR, urn:nbn:fi:research-infras-2016072513).”

### References

* [SNAP homepage](http://step.esa.int/main/toolboxes/snap/)
* [SNAP command line tutorial](http://step.esa.int/docs/tutorials/SNAP_CommandLine_Tutorial.pdf)
* [SNAP wiki](https://senbox.atlassian.net/wiki/spaces/SNAP/overview)
* [SNAP tutorials](http://step.esa.int/main/doc/tutorials/)
* [snappy Python examples](https://senbox.atlassian.net/wiki/spaces/SNAP/pages/19300362/How+to+use+the+SNAP+API+from+Python)

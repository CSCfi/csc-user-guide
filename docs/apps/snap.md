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

### SNAP userdir configuration (Do this the first time!) 

SNAP uses significant amount of storage space for cache and temporary files. These files easily fill your HOME directory so a script was written for configuring the snap user directories easily. You should always run this the first time you start using SNAP in Puhti or if you switch projects.

After loading the module run

`source snap_add_userdir <YOUR-PROJECTS-SCRATCH-FOLDER>`

If you run the command with another folder again, it overwrites the previous settings. 

You could also request a fast [nvme](../computing/running/creating-job-scripts-puhti.md#local-storage) disk in a batch job and run the command first in the batch job so that all the temp/cache files are written to a fast disk rather than the scratch. It might provide speed improvement in demanding calculations.

### Using SNAP with graphical user interface

If you have connected with [NoMachine](nomachine.md) or have X11 enabled on your SSH connection, you can launch a graphical user interface of SNAP with

`snap`

!!! note
   We recommend using [NoMachine](nomachine.md) and [an interactive batch job](../computing/running/interactive-usage.md) for launching graphical user interfaces on Puhti

### Using SNAP with Graph Processing Tool (gpt) command

The Graph Processing Tool __gpt__ is a command line tool used for bulk processing. It can be run with

`gpt <full_path_to_graph_xml_file> -Pfile=<inputfile> -t <outputfile>`

Some relevant __gpt__ options include

* __-q__    Number of threads the gpt instance will use. Set it to the number of CPU cores requested or more
* __-c__    Cache size in bytes. Change this if storage space becomes an issue
* __-x__    Clear internal tile cache after writing a complete row of tiles to output file. Add this if memory becomes an issue

More information on the [SNAP command line tutorial](http://step.esa.int/docs/tutorials/SNAP_CommandLine_Tutorial.pdf)

There is a also a custom made __gpt_array__ command that allows the usage of gpt with [Puhti array jobs](../computing/running/array-jobs.md). It solves the problem of multiple jobs using the same cache folder. The command is otherwise the same as __gpt__ but you include the cache-folder's path as first argument. In an array job you can define that cache folder dynamically with the iterating environment variable __$SLURM_ARRAY_TASK_ID__ and make sure each job has an individual cache folder.

`gpt_array /scratch/<project>/snap/tmp_snap_userdir_"$SLURM_ARRAY_TASK_ID" <normal gpt arguments>`

### Using SNAP with the Python library snappy

It is also possible to access SNAP functionalities from Python with the __snappy__ Python library. When loading the snap module with `module load snap`, a conda environment is also loaded that has __python 2.7__ and __snappy__ installed so you can just start python and import snappy. 

This conda environment also includes:

* pandas
* numpy 
* geopandas 
* rasterio
* rasterstats
* sentinelsat
* spyder

And many more, for retrieving the full list in Puhti use: `list-packages` If you need additional libraries, contact __servicedesk@csc.fi__.

## License and citing

All SNAP software is published under the [GPL-3](https://www.gnu.org/licenses/gpl.html) license and its sources are available on [GitHub](https://github.com/senbox-org/).

In your publications please acknowledge also oGIIR and CSC, for example “The authors wish to acknowledge for computational resources CSC – IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (oGIIR, urn:nbn:fi:research-infras-2016072513).”

### References

* [SNAP homepage](http://step.esa.int/main/toolboxes/snap/)
* [SNAP command line tutorial](http://step.esa.int/docs/tutorials/SNAP_CommandLine_Tutorial.pdf)
* [SNAP wiki](https://senbox.atlassian.net/wiki/spaces/SNAP/overview)
* [SNAP tutorials](http://step.esa.int/main/doc/tutorials/)
* [snappy Python examples](https://senbox.atlassian.net/wiki/spaces/SNAP/pages/19300362/How+to+use+the+SNAP+API+from+Python)


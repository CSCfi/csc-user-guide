# SNAP

[SNAP](https://step.esa.int/main/toolboxes/snap/) (Sentinel Application Platform) is a remote sensing toolbox architecture developed by the European Space Agency. It includes tools for all common remote sensing satellites.

## Available

__SNAP__ is available in Puhti with following versions:

* 8.0 (Singularity container with snappy 8.0.3 and Python 3.6.9)
* 7.0 (with snappy 6.0 and python 2.7.5)

The 8.0 version has been installed as a singularity container. There are small differences in the commands between 7.0 and 8.0, see below
### Installed plugins 

* Sentinel toolboxes (1,2,3) 
* All Idepix processors __(only in 7.0)__
* SMOS toolbox 
* SNAPHU __(only in 7.0)__
* Radarsat toolbox 
* PROBA-V toolbox
* Sen2Cor (external tool) __(only in 7.0)__

You can install more plugins to your user directory from the SNAP Graphical user interface

## Usage

SNAP is included in the __snap__ module and can be loaded with

`module load snap`

This loads the newest available version. You can load an older version with 

`module load snap/<VERSION>`

### SNAP userdir and Java temp dir configuration 

SNAP uses significant amount of storage space for cache and temporary files. By default these are written to your HOME directory and may easily fill your HOME. For avoiding that configure your [snap user directory](https://senbox.atlassian.net/wiki/spaces/SNAP/pages/15269950/SNAP+Configuration) and Java temporary folder. You should run this script every time you start using SNAP in Puhti or want to change the used folders. 

After loading the module run

`source snap_add_userdir <YOUR-PROJECTS-SCRATCH-FOLDER>`

You could also request a fast [nvme](../computing/running/creating-job-scripts-puhti.md#local-storage) disk in a batch job and run the command first in the batch job so that all the temp/cache files are written to a fast disk rather than the scratch. It might provide speed improvement in demanding calculations.

`source snap_add_userdir $LOCAL_SCRATCH` with batch jobs

`source snap_add_userdir $TMPDIR` with interactive jobs

This scripts sets also Java temporary folder, it is set to be snap/temp subfolder in the folder you defined. If you want to set Java temporary folder to be somewhere else use:
`export _JAVA_OPTIONS=-Djava.io.tmpdir=<SOME-FOLDER>`

!!! note
        The graphical user interface does not follow snap.userdir setting, but it notices the Java setting. Using SNAP GUI will create a __.snap__ folder inside your HOME directory and fill it. Empty it if you run out of space in your HOME directory.

### Using SNAP with graphical user interface

If you have connected with [NoMachine](nomachine.md) or have X11 enabled on your SSH connection, you can launch a graphical user interface on an interactive batch job session

__SNAP 8.0__
```
sinteractive -i
<set up snap.userdir>
singularity_wrapper exec snap
```

__SNAP 7.0__
```
sinteractive -i
<set up snap.userdir>
snap
```

!!! note
         We recommend using [NoMachine](nomachine.md) for launching graphical user interfaces on Puhti

### Using SNAP with Graph Processing Tool (gpt) command

The Graph Processing Tool __gpt__ is a command line tool used for bulk processing. It can be run for example with the following commands

__SNAP 8.0__
```
singularity_wrapper exec gpt <full_path_to_graph_xml_file> -Pfile=<inputfile> -t <outputfile>
```
__SNAP 7.0__
```
gpt <full_path_to_graph_xml_file> -Pfile=<inputfile> -t <outputfile>
```

Some relevant __gpt__ options include

* __-q__    Number of threads the gpt instance will use. Set it to the number of CPU cores requested or more
* __-c__    Cache size in bytes. Change this if storage space becomes an issue
* __-x__    Clear internal tile cache after writing a complete row of tiles to output file. Add this if memory becomes an issue

More information on the [SNAP command line tutorial](http://step.esa.int/docs/tutorials/SNAP_CommandLine_Tutorial.pdf)

There is a also a custom made __gpt_array__ command that allows the usage of gpt with [Puhti array jobs](../computing/running/array-jobs.md). It solves the problem of multiple jobs using the same cache folder. The command is otherwise the same as __gpt__ but you include the cache-folder's path as first argument. In an array job you can define that cache folder dynamically with the iterating environment variable __$SLURM_ARRAY_TASK_ID__ and make sure each job has an individual cache folder.
__SNAP 8.0__
```
singularity_wrapper exec gpt_array /scratch/<project>/snap/tmp_snap_userdir_"$SLURM_ARRAY_TASK_ID" <normal gpt arguments>
```

__SNAP 7.0__
```
gpt_array /scratch/<project>/snap/tmp_snap_userdir_"$SLURM_ARRAY_TASK_ID" <normal gpt arguments>
```

[Here is a full example of using gpt_array with Puhti array jobs](https://github.com/csc-training/geocomputing/tree/master/snap)
### Using SNAP with the Python library snappy

It is also possible to access SNAP functionalities from Python with the __snappy__ library.

__SNAP 8.0__

Running snappy scripts with batch jobs:
```
singularity_wrapper exec python3 <YOUR-PYTHON-SCRIPT>
```

See available packages:
```
singularity_wrapper exec pip list
```

Installing new packages to your HOME directory, see [Python](python.md#installing-python-packages-to-existing-modules) instructions how to change installation directory.

```
singularity_wrapper exec pip <NEW-PACKAGE-NAME> --user
```



__SNAP 7.0__

The SNAP 7.0 has a conda environment that includes pandas, geopandas, rasterio, rasterstats, sentinelsat, spyder

for retrieving the full list in Puhti use: `list-packages`

## License and citing

All SNAP software is published under the [GPL-3](https://www.gnu.org/licenses/gpl.html) license and its sources are available on [GitHub](https://github.com/senbox-org/).

In your publications please acknowledge also oGIIR and CSC, for example “The authors wish to acknowledge for computational resources CSC – IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (oGIIR, urn:nbn:fi:research-infras-2016072513).”

### References

* [SNAP homepage](http://step.esa.int/main/toolboxes/snap/)
* [SNAP CSC example](https://github.com/csc-training/geocomputing/tree/master/snap)
* [SNAP command line tutorial](http://step.esa.int/docs/tutorials/SNAP_CommandLine_Tutorial.pdf)
* [SNAP wiki](https://senbox.atlassian.net/wiki/spaces/SNAP/overview)
* [SNAP tutorials](http://step.esa.int/main/doc/tutorials/)
* [snappy Python examples](https://senbox.atlassian.net/wiki/spaces/SNAP/pages/19300362/How+to+use+the+SNAP+API+from+Python)


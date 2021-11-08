# SNAP

[SNAP](https://step.esa.int/main/toolboxes/snap/) (Sentinel Application Platform) is a remote sensing toolbox architecture developed by the European Space Agency. It includes tools for all common remote sensing satellites.

## Available

__SNAP__ is available in Puhti with following versions:

* 8.0 (Singularity container with snappy 8.0.3 and Python 3.6.9)
* 7.0 (with snappy 6.0 and python 2.7.5)

### Installed plugins 

* Sentinel toolboxes (1,2,3) 
* All Idepix processors (only in 7.0)
* SMOS toolbox 
* SNAPHU (only in 7.0)
* Radarsat toolbox 
* PROBA-V toolbox
* [Sen2Cor](sen2cor.md) (external tool) (only in 7.0)

You can install more plugins to your user directory from the SNAP Graphical user interface

## Usage

SNAP is included in the __snap__ module and can be loaded with:

`module load snap`

This loads the newest available version. You can load an older version with:

`module load snap/<VERSION>`

### SNAP userdir and Java temp dir configuration 

SNAP uses significant amount of storage space for cache and temporary files. By default these are written to your HOME directory and may easily fill your HOME. For avoiding that configure your [snap user directory](https://senbox.atlassian.net/wiki/spaces/SNAP/pages/15269950/SNAP+Configuration) and Java temporary folder. You should run this script every time you start using SNAP in Puhti or want to change the used folders. 

After loading the snap module run

`source snap_add_userdir <YOUR-PROJECTS-SCRATCH-FOLDER>`

You could also request a fast [nvme](../computing/running/creating-job-scripts-puhti.md#local-storage) disk in a batch job and run the command first in the batch job so that all the temp/cache files are written to a fast disk rather than the scratch. It might provide speed improvement in demanding calculations.

`source snap_add_userdir $LOCAL_SCRATCH` with batch jobs

`source snap_add_userdir $TMPDIR` with interactive jobs

This scripts sets also Java temporary folder, it is set to be snap/temp subfolder in the folder you defined. If you want to set Java temporary folder to be somewhere else use:
`export _JAVA_OPTIONS="$_JAVA_OPTIONS -Djava.io.tmpdir=<SOME-FOLDER>"` after setting the user directory.

!!! note
        The graphical user interface does not follow snap.userdir setting, but it notices the Java setting. Using SNAP GUI will create a __.snap__ folder inside your HOME directory and fill it. Empty it if you run out of space in your HOME directory.

### Java memory settings
__By default SNAP/8.0 in Puhti uses only up to 2 Gb memory for Java.__ To increase this, add `-J-xmx10G` or similar setting to `snap` or `gpt` command. `-J-xmx10G` extends the Java maximum memory to 10Gb. Adjust this according to your needs and job memory reservation. Compared to your job memory reservation use for Java a few Gb less.

### Using SNAP with Graphical User Interface (GUI) via Puhti web interface

This is the new recommended way.

1. Log in to [Puhti web interface](https://puhti.csc.fi). [Puhti web interface documentation](../computing/webinterface/desktop.md).
2. Start SNAP with Apps -> Desktop, choose Desktop: 'None' and App: 'SNAP'
3. The SNAP GUI is started automatically when the Desktop is launched. To launch SNAP alternatively from the command line, use:
```
source snap_add_userdir $TMPDIR
snap -J-xmx10G
```

### Using SNAP with Graph Processing Tool (gpt) command

The Graph Processing Tool `gpt` is a command line tool used for bulk processing. Using GPT more computing power can be used than with SNAP graphical interface, because it can be used in scripts and therefore included in jobs that can be submitted to any [Puhti partition](../computing/running/batch-job-partitions.md).

GPT command looks often something like this:

```
gpt -J-xmx10G <full_path_to_graph_xml_file> -Pfile=<inputfile> -t <outputfile>
```

Some relevant __gpt__ options include:

* __-J-xmx10G__    maximum memory used by Java.
* __-q__    Number of threads the gpt instance will use. Set it to the number of CPU cores requested or more
* __-c__    Cache size in bytes. Change this if storage space becomes an issue
* __-x__    Clear internal tile cache after writing a complete row of tiles to output file. Add this if memory becomes an issue


See the links under references at the end of this page for additional info about GPT.

Also the following command is very useful in creating the graphs for different operators. It can be executed in an interactive session
```
sinteractive -i
module load snap
gpt <snap-operator> -h
```

`gpt --diag -J-Xmx60G -c 40G` can be used to see which memory and cache settings are used by `gpt`.

#### GPT examples for Puhti

* [Full examples how to run GPT in Puhti in GitHub](https://github.com/csc-training/geocomputing/tree/master/snap). The examples include both a simple job with one GPT graph and an [array job](../computing/running/array-jobs.md) where the same graph is computed for several input images.


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
* [SNAP command line tutorial (GPT)](http://step.esa.int/docs/tutorials/SNAP_CommandLine_Tutorial.pdf)
* [SNAP wiki](https://senbox.atlassian.net/wiki/spaces/SNAP/overview)
* [SNAP tutorials](http://step.esa.int/main/doc/tutorials/)
* [snappy Python examples](https://senbox.atlassian.net/wiki/spaces/SNAP/pages/19300362/How+to+use+the+SNAP+API+from+Python)
* [Creating a GPF Graph](https://senbox.atlassian.net/wiki/spaces/SNAP/pages/70503590/Creating+a+GPF+Graph)
* [Bulk Processing with GPT command](https://senbox.atlassian.net/wiki/spaces/SNAP/pages/70503475/Bulk+Processing+with+GPT)


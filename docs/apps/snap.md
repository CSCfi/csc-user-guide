---
tags:
  - Free
catalog:
  name: SNAP
  description: for remote sensing applications
  license_type: Free
  disciplines:
    - Geosciences
  available_on:
    - web_interfaces:
        - Puhti
        - Roihu
    - Puhti
    - Roihu
---

# SNAP

[SNAP](https://step.esa.int/main/) (Sentinel Application Platform) is a remote sensing toolbox architecture developed by the European Space Agency. It includes tools for ESA satellite data.

## Available

__SNAP__ is available with following versions:

* SNAP `13.0` + Python 3.12.3 including esa_snappy and pyroSAR + JupyterLab in Roihu
* SNAP `13.0` + Python 3.12.3 including esa_snappy and pyroSAR + JupyterLab in Puhti
* SNAP `jupyter` (9.0) + Python 3.6.9 including snappy and snapista + JupyterLab in Puhti
* SNAP `9.0` + Python 3.6.9 including snappy and snapista in Puhti
* SNAP `8.0` + Python 3.6.9 including snappy in Puhti

The versions including JupyterLab can be used in the Jupyter application in the Puhti webinterface via the **custom module** option.

## Usage

SNAP is included in the __snap__ module and can be loaded with:

`module load snap`

This loads the newest available version. You can load an older version with:

`module load snap/<VERSION>`

### Using SNAP with Graphical User Interface (GUI) in the Puhti/Roihu web interface

The easiest option for using SNAP is to open it in the Puhti/Roihu web interface.

1. Log in to web interface: [Puhti](https://puhti.csc.fi) or [Roihu](https://roihu.csc.fi)
2. Open [Desktop app](../computing/webinterface/desktop.md). 
3. After launching the remote desktop, start SNAP from `Applications` (upper left corner) -> `Geosciences`.

Alternatively, open terminal from `Applications` -> `Terminal emulator`:

```
module load snap
source snap_add_userdir $TMPDIR
snap -J-Xmx10G
```

#### SNAP userdir and Java temp dir configuration 

SNAP uses a significant amount of storage space for cache and temporary files. By default, these are written to your HOME directory and may easily fill your HOME. For avoiding that configure your [snap user directory](https://senbox.atlassian.net/wiki/spaces/SNAP/pages/15269950/SNAP+Configuration) and Java temporary folder. You should run this script every time you start using SNAP in Roihu or want to change the used folders. The SNAP launcher under Applications sets the userdir to `$TMPDIR` automatically.

Roihu has by default 20 Gb space in `$TMPDIR`. If that is not enough, set userdir to your project's scratch. This can be done only if launching SNAP from terminal.

```
mkdir /scratch/project_200XXXX/snap-tmp
source snap_add_userdir /scratch/project_200XXXX/snap-tmp
```

This scripts sets also Java temporary folder, it is set to be snap/temp subfolder in the folder you defined. If you want to set Java temporary folder to be somewhere else use:
`export _JAVA_OPTIONS="$_JAVA_OPTIONS -Djava.io.tmpdir=<SOME-FOLDER>"` after setting the user directory.

!!! note
     The graphical user interface does not follow snap.userdir setting, but it notices the Java setting. Using SNAP GUI will create a __.snap__ folder inside your HOME directory and fill it. Empty it if you run out of space in your HOME directory.

#### Java memory settings

__By default SNAP uses only up to 2 Gb memory for Java.__ To increase this, add `-J-xmx10G` or similar setting to `snap` or `gpt` command. `-J-Xmx10G` extends the Java maximum memory to 10Gb. Adjust this according to your needs and job memory reservation. Compared to your job memory reservation use for Java a few Gb less.

### Using SNAP with Graph Processing Tool (gpt) command

The Graph Processing Tool `gpt` is a command line tool used for bulk processing. Using GPT more computing power can be used than with SNAP graphical interface, because it can be used in scripts and therefore included in jobs that can be submitted to any [partition](../computing/running/batch-job-partitions.md).

GPT command looks often something like this:

```
gpt -J-Xmx10G <full_path_to_graph_xml_file> -Pfile=<inputfile> -t <outputfile>
```

Some relevant __gpt__ options include:

* __-J-Xmx10G__    maximum memory used by Java.
* __-q__    Number of threads the gpt instance will use.
* __-c__    Data cache size in bytes. Change this if storage space becomes an issue
* __-x__    Clear internal tile cache after writing a complete row of tiles to output file. Add this if memory becomes an issue


See the links under references at the end of this page for additional info about GPT.

Also the following command is very useful in creating the graphs for different operators. It can be executed in an interactive session
```
sinteractive -i
module load snap
gpt <snap-operator> -h
```

`gpt --diag -J-Xmx60G -c 40G` can be used to see which memory and cache settings are used by `gpt`.

#### GPT examples for Roihu

* [Full examples how to run GPT in Roihu](https://github.com/csc-training/geocomputing/tree/master/snap). The examples include both a simple job with one GPT graph and parallel batch job where the same graph is computed for several input images.


### Using SNAP with the Python interfaces

It is also possible to access SNAP functionalities from Python.

__SNAP 9.0 and 13.0__

Running Python scripts with batch jobs:
```
python3 <YOUR-PYTHON-SCRIPT>
```

See available packages:
```
pip list
```

Installing new packages to your `$HOME` directory:

```
pip <NEW-PACKAGE-NAME> --user
```

It is also possible to install packages to directories other than `$HOME`.
Please see our
[Python usage guide](../support/tutorials/python-usage-guide.md#installing-python-packages-to-existing-modules)
for instructions.

__SNAP 8.0__

Running snappy scripts with batch jobs:
```
apptainer_wrapper exec python3 <YOUR-PYTHON-SCRIPT>
```

See available packages:
```
apptainer_wrapper exec pip list
```

Installing new packages to your `$HOME` directory:

```
apptainer_wrapper exec pip <NEW-PACKAGE-NAME> --user
```

It is also possible to install packages to directories other than `$HOME`.
Please see our
[Python usage guide](../support/tutorials/python-usage-guide.md#installing-python-packages-to-existing-modules)
for instructions.

### Using the Python package with JupyterLab

1. Log in to web interface: [Puhti](https://puhti.csc.fi) or [Roihu](https://roihu.csc.fi)
2. Open [Jupyter app](../computing/webinterface/jupyter.md). 
3. Select **custom module** and write `snap` as module.

In Jupyter remember to set the temporary directories. Follow the [SNAP set up Notebook](https://github.com/csc-training/geocomputing/blob/master/snap/SNAP_set_up.ipynb) to get started.

## Updating SNAP

SNAP minor and module updates are stored in the `$HOME/.snap` directory. This means that all minor updates need to be installed by the user. You can do this in SNAP Desktop by following the instructions in the pop-up at start up.

## License

All SNAP software is published under the [GPL-3](https://www.gnu.org/licenses/gpl.html) license.

## Citation

```SNAP - ESA Sentinel Application Platform v{VERSION}, http://step.esa.int```



##  Acknowledgement

Please acknowledge CSC and Geoportti in your publications, it is important for project continuation and funding reports.
As an example, you can write "The authors wish to thank CSC - IT Center for Science, Finland (urn:nbn:fi:research-infras-2016072531) and the Open Geospatial Information Infrastructure for Research (Geoportti, urn:nbn:fi:research-infras-2016072513) for computational resources and support".


## Installation

SNAP 13.0 was installed with Singularity using installer provided by ESA, with pip was added Jupyter, `esa_snappy` and `pyroSAR`. The container was finally wrapped with [Tykky's wrap-container functionality](../computing/containers/tykky.md#container-based-installations).

SNAP 9.0 was installed to Puhti with Singularity using the [SNAP Docker image provided by mundialis on Dockerhub](https://hub.docker.com/r/mundialis/esa-snap) with some small additions to provide snappy and snapista Python interfaces. The container was finally wrapped with [Tykky's wrap-container functionality](../computing/containers/tykky.md#container-based-installations).

`wrap-container -w /usr/local/snap/bin,/usr/bin snap9_py.sif --prefix install_dir`

[CSC SNAP Singularity definition files](https://raw.githubusercontent.com/CSCfi/singularity-recipes/main/snap).


## References

* [SNAP homepage](http://step.esa.int/main/toolboxes/snap/)
* [SNAP CSC example](https://github.com/csc-training/geocomputing/tree/master/snap)
* [SNAP command line tutorial (GPT)](http://step.esa.int/docs/tutorials/SNAP_CommandLine_Tutorial.pdf)
* [SNAP wiki](https://senbox.atlassian.net/wiki/spaces/SNAP/overview)
* [SNAP tutorials](http://step.esa.int/main/doc/tutorials/)
* [snappy Python examples](https://senbox.atlassian.net/wiki/spaces/SNAP/pages/19300362/How+to+use+the+SNAP+API+from+Python)
* [Creating a GPF Graph](https://senbox.atlassian.net/wiki/spaces/SNAP/pages/70503590/Creating+a+GPF+Graph)
* [Bulk Processing with GPT command](https://senbox.atlassian.net/wiki/spaces/SNAP/pages/70503475/Bulk+Processing+with+GPT)


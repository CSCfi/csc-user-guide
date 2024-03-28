# Utilizing Apptainer containers in SD Desktop

!!! warning-label
    Skill level - Advanced 

As the SD Desktop is not directly connected internet, you can't use tools like Git, Conda or Pip to install new software there.
Instead, you can use  [Apptainer](https://apptainer.org/docs/user/latest/introduction.html) software container tool to add new software to your SD Desktop environment. However, you have to first build or download an Apptainer container elsewhere, and then use _Allas/SD Connect_ to import the container to SD Desktop.

Note: Apptainer is a fork on Singularity container system, so in many occasions instructions may refer to Singularity. In most cases you can just replace "Singularity" with "Apptainer".

If you have root access to a machine with Apptainer, you can build your own container that contains exactly the software and datasets you need. Many software are also available as ready-made Apptainer containers or as Docker containers that can be converted into
Appainer containers. In this document we show how to import a ready-made Apptaner container from a public repository to SD Desktop.


## Step by step tutorial

*Before you start, please activate services **Puhti, SD Desktop** and **Allas/SD Connect** for your project. This happens in [MyCSC](https://my.csc.fi/login){ target="_blank" }.*

<iframe width="562" height="316" srcdoc="https://www.youtube.com/embed/6-_pSrRu4-c" title="Utilizing Apptainer containers in SD Desktop" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

How to import a ready-made Apptainer container from a public repository to SD Desktop:

1. [Find a suitable container](#find-a-suitable-container)
2. [Download the container](#download-the-container)
3. [Upload the container to SD Connect](#upload-the-container-to-allas-sd-connect)
4. [Download the container to SD Desktop](#using-a-container-in-sd-desktop)

### Importing ready-made container through Puhti

#### Find a suitable container
In the example below we import [BETA Binding and Expression Target Analysis](https://cistrome.org/BETA/index.html) software to SD Desktop.
This tool is available as a ready-made Apptainer container in [Biocontainers](https://biocontainers.pro/registry) repository. You can find the tool by searching for _Binding and Expression Target Analysis_ in the repository. When you open the detailed information of the resulting _cistrome_beta_ container, 
you can see that the Singularity module can be downloaded from URL: <https://depot.galaxyproject.org/singularity/cistrome_beta:1.0.7--py27heb79e2c_4>

#### Download the container
As we don't need to build the container from scratch, we can use [puhti.csc.fi](../../computing/index.md) server to download the container image and push it to Allas.

First [login to puhti.csc.fi](https://www.puhti.csc.fi/public/){ target="_blank" }. Then, start an interactive batch job session with command:

```text
sinteractive
```

In the interactive session move to `LOCAL_SCRATCH` directory and set some Singularity related environment variables:

```text
export SINGULARITY_TMPDIR=$LOCAL_SCRATCH
export SINGULARITY_CACHEDIR=$LOCAL_SCRATCH
unset XDG_RUNTIME_DIR
```

Then download a local copy of the Beta container with command

```text
apptainer pull beta.sif https://depot.galaxyproject.org/singularity/cistrome_beta:1.0.7--py27heb79e2c_4
```

This creates a new singularity container file, `beta.sif`. From the home page of BETA software 
we download also a test data set for confirming that the container works.

```text
wget http://cistrome.org/BETA/src/BETA_test_data.zip
```

#### Upload the container to Allas / SD Connect

Then we upload these two files to Allas/SD Connect. In this example we use project _2012345_.

```text
module load allas
allas-conf project_2012345
a-put --sdx beta.sif -b 2012345_beta
a-put --sdx BETA_test_data.zip -b 2012345_beta
```

The commands above store the files into bucket `2012345_beta` in Allas. `a-put` is used with option `--sdx` in order to encrypt the uploaded data with SD Desktop compatible encryption. 

### Using a container in SD Desktop

First [login to sd-desktop.csc.fi](https://sd-desktop.csc.fi/){ target="_blank" } and open your virtual desktop session.

Once the `.sif` formatted Apptainer container file and the sample data has been uploaded to Allas, we can copy 
them to SD Desktop. To do this open _DataGateway_, in your session SD Desktop. After that copy the data to local disk in SD Desktop.

You can do that using the **graphical DataGateway tool** on the Desktop (see the [video](https://youtu.be/6-_pSrRu4-c?t=397){ target="_blank" }).

Or you can use **Linux command line**: Open a Linux terminal in the SD-Desktop. In the terminal, move the Apptainer file and test data to your current locations:

```text
cp Projects/SD-connect/project_201234/2012345_beta/beta.sif ./
cp Projects/SD-connect/project_201234/2012345_beta/BETA_test_data.zip ./
```

Unzip the test dataset:

```text 
unzip BETA_test_data.zip
```

Now you can run BETA through _apptainser_ command. 
For example the _help_ of command _BETA minus_ is shown with command:

```text
apptainer exec beta.sif BETA minus -h
```

And the analysis with sample data in directory `BETA_test_data` can
be executed with commands like:

```text
apptainer exec beta.sif BETA minus -p BETA_test_data/3656_peaks.bed --bl -g hg19
```

In this example the results will be written to directory `BETA_OUTPUT`. 








# Utilizing singularity containers in SD-Desktop

As the SD Desktop is not directly connected internet, you can't use tools like Git, Gonda or Pip to install new software there.
In stead, you can use Singularity [Singularity](https://sylabs.io/guides/3.8/user-guide/) software container tool to add new software to your SD Desktop environment. However, you have to first build  or download a singularity container elsewhere, and then use _Allas/SD Connect_ to import the container to SD Desktop.

If you have a root access to a machine with singularity, you can build your own container, that contains exactly the software and
datasets you need. Many software are also available as ready made Singularity containers or as Docker containers that can be converted into
Singularity containers. In this document we show, how to import a ready-made Singularity container from a public repository to SD Desktop.


## Importing ready made container through Puhti


In the example below we import [BETA Binding and Expression Target Analysis](https://cistrome.org/BETA/index.html) software to SD Desktop.
This tool is available as a ready made Singularity container in [Biocontainers](https://biocontainers.pro/registry) repository. You can find the tool
by searching for _Binding and Expression Target Analysis_ in the repository. When you open the detailed information of the resulting _cistrome_beta_ cintainer, 
you can see that the sigularity module can be downloaded from url: "https://depot.galaxyproject.org/singularity/cistrome_beta:1.0.7--py27heb79e2c_4" 

As we don't need to build the container from scratch, we can use [puhti.csc.fi](../../computing/overview.md) server to download the container 
image and push it to Allas.

First login to _puhti.csc.fi_. Then, start an interactive batch job session with command:

```text
sinteractive
```
In the interactive session move to LOCAL_SCRATCH directory an set some Singularity related environment variables:
 
 ```text
 export SINGULARITY_TMPDIR=$LOCAL_SCRATCH
 export SINGULARITY_CACHEDIR=$LOCAL_SCRATCH
 unset XDG_RUNTIME_DIR
```

Then download a local copy of the Beta container with command

```text
singularity pull beta.sif https://depot.galaxyproject.org/singularity/cistrome_beta:1.0.7--py27heb79e2c_4
```
This creates a new singularity container file, _beta.sif_, is then uploaded allas that. From the home page of BETA software 
we download also a test data set for confirming that the container works.

```text
wget http://cistrome.org/BETA/src/BETA_test_data.zip
```

Then we upload these two files to Allas. In this examople we use project _2012345_.

```text
module load allas
allas-conf project_2012345
a-put --nc beta.sif -b 2012345_beta
a-put --nc BETA_test_data.zip -b 2012345_beta
```

The commands above store the files into bucket _2012345_beta_ in Allas. _a-put_ is used with option _--nc_ 
as we don't want to compress the data. 

## Using a container in SD desktop

Once the sif formatted singularity container file and the sample data has been uploaded to Allas, we can copy 
them to SD Desktop. Open _SD Connect downloader_, navigate the to the right project (_project_2012345_) and bucket (_2012345_beta_), 
and download the sif file (_beta.sif_) and the test data set (_BETA_test_data.zip_).

After that open a Linux terminal in the SD-Desktop. In the terminal, move the singularity file and test data to 
your current locations:

```text
mv SDCONNECTDATA/project_201234/2012345_beta/beta.sif ./
mv SDCONNECTDATA/project_201234/2012345_beta/BETA_test_data.zip ./
```
Unzip the test dataset:
```text 
unzip BETA_test_data.zip
```
Now you can run BETA through singularity command. 
For example the _help_ of command _BETA minus_ is shown with command:

```text
singularity exec beta.sif BETA minus -h
```
And the analysis with sample data in directory _BETA_test_data_ can
be executed with commands like:

```text
singularity exec beta.sif BETA minus -p BETA_test_data/3656_peaks.bed --bl -g hg19
```
In this example the results will be written to directory _BETA_OUTPUT_. 








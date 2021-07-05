# Utilizing singularity containers in SD-Desktop

The Linux environment used in the SD Desktop includes [Singularity](https://sylabs.io/guides/3.8/user-guide/) 
software container tool that allows running containerized software and workflows. Singularity
provides the easiest way to add software to your SD Desktop enviroment. As the SD Desktop is not directly connected internet, 
you can't use tools like git, conda or pip to install new software. Also in the case of Singularity, you have to first build 
or download a singularity container somewere else, and then use _Allas/SD Connect_ to import the container to SD Desktop.

## Importing ready made containwer through Puhti


In the example below we import [BETA Binding and Expression Target Analysis](https://cistrome.org/BETA/index.html) sofware to SD Desktop.
This tool is available as a ready made Singularity container in [Biocontainers](https://biocontainers.pro/registry) repository. You can find the tool
by searching for _Binding and Expression Target Analysis_ in the repostory. When you open the detailed information of the resulting _cistrome_beta_ cintainer, 
you can see that the sigularity module can be downloaded from url: "https://depot.galaxyproject.org/singularity/cistrome_beta:1.0.7--py27heb79e2c_4" 

As we don't need to build the containwer from scratch, we can use Puhti.csc.fi server to download the image and push it to Allas.

First login to puhti.csc.fi. The start an interactive batch job session with command:

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
we download also a test dataset for confirming that the container works.

```text
wget http://cistrome.org/BETA/src/BETA_test_data.zip
```

Then we upload these two files to Allas for project _2012345_

```text
module load allas
allas-conf project-2012345
a-put --nc beta.sif -b 2012345_beta
a-put --nc BETA_test_data.zip -b 2012345_beta
```

The commands above store the files into bucket _2012345_beta_ in Allas. 






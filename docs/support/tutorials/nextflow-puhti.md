
# Running Nextflow pipelines on Puhti
Nextflow (http://nextflow.io](http://nextflow.io/) is a scalable and reproducible scientific workflow management system that interacts with containerised applications to perform compute-intensive tasks. This workflow provide built-in support for containers like Singularity, which is a containerisation technology that is compliant with HPC environment. Although, nextflow pipelines allow us to choose Docker engine as an executor for running pipelines, please note that Puhti users can't use Docker containers as users lack administrative privileges for running the applications. 

## How Singularity works with Nextflow
The integration of Singularity containers with Nextflow follows the same execution model as with Docker containers. So it does not require additional modifications in nextflow script as such to be compatible with Singularity. One has to just enable the use of Singularity engine (instead of Docker) in the Nextflow configuration file. Nextflow is able to pull remote container images stored in Singularity or Docker-Hub registry. The remote container images are usually specified in your nextflow script or configuration file by simply prefixing the image name with the `shub://` or `docker://` as required by the Singularity tool. It is also possible to specify a different Singularity image for each process definition in nextflow pipeline script. 

Here is a general recipe for running your nextflow pipeline on Puhti :

1. Prepare your singularity images on your local environment
2. Login to Puhti supercomputer
3. Install Nextflow in your workspace
4. Set-up your Nextflow pipeline environment
5. Run your Nextflow pipeline as a batch job
6. Optional Tutorial - Demonstration of WtP Nextflow pipeline on Puhti

## 1. Prepare your Singularity images on your local environment

Singularity containers can't be built directly on Puhti. So one has to build and copy singularity container(s) of nextflow pipeline from your local environment to Puhti. 

Here are some options for preparing your singularity image:

- Build a Singularity image on your local system  and then copy it to Puhti
- Convert a Docker image to Singularity on your local system  and then copy it to Puhti.
- Copy a Singularity image from a container registry to Puhti.

You can also use cPouta environment at CSC to build singularity images.

!!!  Note: Singularity is installed only on compute nodes in Puhti  and cannot be executed/tested on login nodes.

## 2. Login to Puhti supercomputer

SSH into the login node of Puhti cluster (More instructions [here](../../computing/overview.md))

```
ssh <csc_username>@puhti.csc.fi
```

## 3. Install Nextflow in your workspace

Please follow the instructions [here](../../apps/bioconda.md#2-installing-software-for-your-own-use-with-bioconda) in order to make custom installations of software. In future CSC may provide nextflow as a module.

For the installation of nextflow, you could be doing as below: 

```
export PROJAPPL=/projappl/project_xxx
module load bioconda
conda create -n next_flow -c bioconda nextflow  # next_flow is a env name
source activate next_flow  
```

## 4. Set-up your Nextflow pipeline environment

Running nextflow pipelines can some times be quite compute-intensive and may require lot of downloading data such as databases and singularity images. This can take a long time and even may not work successfully for downloading singularity images. So please prepare early depending on your tool

You can do the following basic preparation before running nextflow pipeline:

- Copy singularity images from your local workspace to your project folder on Puhti. Pay attention to the singularity cache directory (i.e., SINGULARITY_CACHEDIR or some other name given by you tool) which is usually $HOME/.singularity/cache.  Disk space of your home directory is quite limited (10 GB) on Puhti.
- Move all your raw data to your scratch directory on Puhti
- Clone Git repository of your tool to your scratch folder and then run your pipeline from a GitHub repository. Alternatively, use nextflow pipeline directly from DockerHub if the pipeline available

## 5. Run your Nextflow pipeline as a batch job

Please follow our instructions for writing a batch job on Puhti at [CSC documentation pages](../../computing/running/example-job-scripts-puhti.md).

Here is a minimal script to start with your Nextflow pipeline on Puhti:

```
#!/bin/bash
#BATCH --time=00:15:00 # change your time settings
#SBATCH --partition=test #  change partition as needed
#SBATCH --account=project_XXX # add your project number here
#SBATCH --cpus-per-task=xx # change as you need

export PROJAPPL=/projappl/project_XXX
module load bioconda
source activate nextflow

# Actual Nextflow command here
nextflow run  <workflow.nf> [options]
```

## 6. Potional Tutorial - Demonstration of WtP Nextflow pipeline

WtP is a scalable and easy-to-use workflow for phage identification and analysis. More details about the pipeline can be found [here](https://github.com/replikation/What_the_Phage).

Login to puhti and  install nextflow using conda environment as instructed above.

## Set-up WtP pipeline on Puhti

You can either clone WtP GitHub  repository to your  project directory under scratch drive on Puhti as below:

```
cd  /Path_on_scratch
git clone  https://github.com/replikation/What_the_Phage.git
nextflow run /Path_on_scratch/What_the_Phage/phage.nf --help
```

or pull the Nextflow pipeline from DockerHub:

```
nextflow run replikation/What_the_Phage  -r v0.8.0 --help
```

In either case, pay attention to the versions of different singularity containers as mentioned in containers.config file. 

### Bring your WtP singularity images to Puhti

WtP is a scalable and easy-to-use workflow for phage identification and analysis. More details about the pipeline can be found [here](https://github.com/replikation/What_the_Phage).

Login to puhti and install nextflow using `conda` environment as instructed above.

## Set-up WtP pipeline on Puhti

You can either clone WtP GitHub repository to your project directory under `scratch` drive on Puhti as below:

```
cd  /Path_on_scratch/
git clone  https://github.com/replikation/What_the_Phage.git
nextflow run /Path_on_scratch/What_the_Phage/phage.nf --help
```

or pull yoour Nextflow pipeline from DockerHub:

```
nextflow run replikation/What_the_Phage --help
```

In either case, pay attention to the versions of different singularity containers used for running Nextflow pipeline as mentioned in configs/containers.config file. 

### Run WtP pipelines as a batch job on Puhti:

Submit the following batch script to run nextflow pipeline:

```
#!/bin/bash
#SBATCH --time=01:00:00
#SBATCH --partition=small
#SBATCH --account=project_XXX
#SBATCH --cpus-per-task=4

# Set-up Nextflow on Puhti
export TMPDIR=$PWD
export PROJAPPL=/projappl/project_XXX
module load bioconda
source activate nextflow

# actual Nextflow command 
nextflow run /Path_on_scratch/What_the_Phage/phage.nf --fasta /Path_on_scratch/What_the_Phage/test-data/OX2_draft.fa --cores 4 --output results -profile local,singularity --cachedir /Path_on_scratch//What_the_Phage/singularity --databases /Path_on_scratch/What_the_Phage/databases/WtP_databases --workdir
/Path_on_scratch/What_the_Phage/workflow-phages-username 
```

Please note that your singularity images in this example should be in the folder:"/Path_on_scratch//What_the_Phage/singularity". Otherwise, nextflow tries to download singularity images again and eventually may prone to failures.

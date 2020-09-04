
# Running Nextflow pipelines on Puhti
[Nextflow](https://www.nextflow.io/) is a scalable and reproducible scientific workflow management system that interacts with containerised applications to perform compute-intensive tasks. This workflow provides built-in support for containers like Singularity, which is a containerisation technology that is compliant with HPC environment. Although nextflow pipelines allow us choosing Docker engine as an executor for running pipelines, please note that Docker containers can't be used due to the lack of administrative privileges to Puhti users. 

## How Singularity works with Nextflow
The integration of Singularity containers with Nextflow follows the same execution model as with Docker containers. So it does not require additional modifications in Nextflow script as such to be compatible with Singularity. One has to just enable the use of Singularity engine (instead of Docker) in the Nextflow configuration file. Nextflow is able to pull remote container images stored in Singularity or Docker-Hub registry. The remote container images are usually specified in your Nextflow script or configuration file by simply prefixing the image name with the `shub://` or `docker://`. It is also possible to specify a different Singularity image for each process definition in Nextflow pipeline script. 

Here is a generic recipe for running your Nextflow pipeline on Puhti :
1. Prepare your singularity images on your local environment
2. Login to Puhti supercomputer
3. Activate conda environment for Nextflow on Puhti
4. Set-up your Nextflow pipeline environment
5. Run your Nextflow pipeline as a batch job
6. (Optional) tutorial - Demonstration of WtP Nextflow pipeline on Puhti

## 1. Prepare your Singularity images on your local environment

Singularity containers can't be built directly on Puhti. So one has to build and copy singularity container(s) of nextflow pipeline from your local environment to Puhti supercomputer. 

Here are some options for preparing your singularity image:

- Build a Singularity image on your local system  and then copy it to Puhti
- Convert a Docker image to Singularity on your local system and then copy it to Puhti.
- Copy a Singularity image from a container registry to Puhti.

You can also use [cPouta](../../cloud/pouta/launch-vm-from-web-gui.md) environment at CSC to build singularity images.

!!!  Note: Singularity is installed only on compute nodes in Puhti and is not available for execution or testing on login nodes.

## 2. Login to Puhti supercomputer

SSH into the login node of Puhti cluster (See instructions [here](../../computing/overview.md))

```
ssh <csc_username>@puhti.csc.fi
```

## 3. Activate conda environment for Nextflow on Puhti

Nextflow on Puhti is available *via* conda environment and is activate as below:

```
module load bioconda
source activate nextflow

```

In case you need any custom installations with specific version of Nextflow in your workspace, please follow instructions [here](../../apps/bioconda.md#2-installing-software-for-your-own-use-with-bioconda). 

For the installation of Nextflow, you can use the following conda approach: 

```
export PROJAPPL=/projappl/project_xxx
module load bioconda
conda create -n next_flow -c bioconda nextflow=0.30.1  # next_flow is a env name and you can install with specific version of nextflow
source activate next_flow  
```

## 4. Set-up your Nextflow pipeline environment

Running Nextflow pipelines can sometimes be quite compute-intensive and may require downloading large volumes of data such as databases and singularity images. This can take a while and may not even work successfully in case of downloading singularity images on Puhti. 

You can do the following basic preparation before running Nextflow pipeline:

- Copy singularity images from your local workspace to your project folder on Puhti. Pay attention to the singularity cache directory (i.e., SINGULARITY_CACHEDIR or some other name given by you tool) which is usually $HOME/.singularity/cache. The disk space of your home directory is quite limited (10 GB) on Puhti.
- Move all your raw data to your project directory on Puhti
- Clone GitHub repository of your pipeline to your scratch directory and then run your pipeline from a GitHub repository. Alternatively, use Nextflow pipeline directly from DockerHub if the pipeline is available

## 5. Run your Nextflow pipeline as a batch job

Please follow our instructions for writing a batch job on Puhti as described in [CSC documentation pages](../../computing/running/example-job-scripts-puhti.md).

Here is a minimal script to get started with your Nextflow pipeline on Puhti:

```
#!/bin/bash
#SBATCH --time=00:15:00 # change your time settings
#SBATCH --partition=test #  change partition as needed
#SBATCH --account=project_XXX # add your project number here
#SBATCH --cpus-per-task=xx # change as you need

module load bioconda
source activate nextflow

# Actual Nextflow command here
nextflow run  <workflow.nf> [options]
```

## 6. (Optional) tutorial - Demonstration of WtP Nextflow pipeline

WtP is a scalable and easy-to-use workflow for phage identification and analysis. More details about the pipeline can be found [here](https://github.com/replikation/What_the_Phage).

Login to Puhti and install Nextflow using conda environment as instructed above.

## Set-up WtP pipeline on Puhti

You can either clone WtP GitHub repository to your project directory in scratch drive  as below:

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

WtP is a multi-container pipeline requiring as many as 21 singularity images (see [here](https://github.com/replikation/What_the_Phage/blob/master/configs/container.config) for further details) at the time of writing this tutorial. All these containers are downloaded in cPouta environment to avoid any build failures of singularity images on Puhti due to the lack of privileged access for users. For the sake of this tutorial, the downloaded singularity images are uploaded to ``Allas`` which is an object storage environment at CSC.

The images on `Allas` object storage can be downloaded to your project directory on scratch as below:
```
mkdir /Path_on_scratch/What_the_Phage/singularity
cd /Path_on_scratch/What_the_Phage/singularity
wget https://a3s.fi/puhti_singularity/WtP_singularity.tar.gz
tar -xavf WtP_singularity.tar.gz
```

### Run WtP pipelines as a batch job on Puhti:

Submit the following batch script to run nextflow pipeline:
```
#!/bin/bash
#SBATCH --time=01:00:00
#SBATCH --partition=small
#SBATCH --account=project_XXX
#SBATCH --cpus-per-task=4

export TMPDIR=$PWD
# Activate  Nextflow on Puhti
module load bioconda
source activate nextflow

# Nextflow command here
nextflow run /Path_on_scratch/What_the_Phage/phage.nf --fasta /Path_on_scratch/What_the_Phage/test-data/OX2_draft.fa --cores 4 --output results -profile local,singularity --cachedir /Path_on_scratch//What_the_Phage/singularity --databases /Path_on_scratch/What_the_Phage/databases/WtP_databases --workdir
/Path_on_scratch/What_the_Phage/workflow-phages-username 
```

Please note that Singularity images in this example should be in the folder:"/Path_on_scratch//What_the_Phage/singularity". Otherwise, Nextflow tries to download Singularity images again and eventually may be prone to failures.


# Running Nextflow pipelines on Puhti
[Nextflow](https://www.nextflow.io/) is a scalable and reproducible scientific workflow 
management system that interacts with containerised applications to perform 
compute-intensive tasks. Nextflow provides built-in support for containers 
like Singularity, which is a containerisation technology that is compliant 
with HPC environment. Although Nextflow pipelines allow us to choose Docker 
engine as an executor for running pipelines, please note that Docker 
containers can't be used in Puhti due to the lack of administrative privileges for researchers.

## Strengths of Nextflow

* Easy installation
* No database needed
* Implicit parallelism supported
* Can handle complex dependencies and conditional execution
* Supports error recovery

## Disadvantages of Nextflow

* Limited MPI support
* May create a lot of job steps and excess IO
* Does not integrate well with Slurm

## How Singularity works with Nextflow
The integration of Singularity containers with Nextflow follows the same 
execution model as with Docker containers. So it does not require additional 
modifications in a Nextflow script as such to be compatible with Singularity. 
One has to just enable the use of Singularity engine (instead of Docker) 
in the Nextflow configuration file. Nextflow is able to pull remote container 
images stored in Singularity or Docker-Hub registry. The remote container 
images are usually specified in your Nextflow script or configuration 
file by simply prefixing the image name with the `shub://` or `docker://`. 
It is also possible to specify a different Singularity image for each 
process definition in the Nextflow pipeline script. 

Here is a generic recipe for running your Nextflow pipeline on Puhti :

1. Prepare your singularity images on your local environment
2. Login to Puhti supercomputer
3. Load Nextflow as a module on Puhti
4. Set-up your Nextflow pipeline environment
5. Run your Nextflow pipeline as a batch job
6. (Optional) tutorial - Demonstration of WtP Nextflow pipeline on Puhti

## 1. Prepare your Singularity images on your local environment

Singularity containers can't be built directly on Puhti. So one has to 
build and copy singularity container(s) of a nextflow pipeline from your 
local environment to Puhti supercomputer. 

Here are some options for preparing your singularity image:

- Build a Singularity image on your local system  and then copy it to Puhti
- Convert a Docker image to Singularity on your local system and then copy it to Puhti.
- Copy a Singularity image from a container registry to Puhti.

You can also use [cPouta](../../cloud/pouta/launch-vm-from-web-gui.md) environment at CSC to build singularity images.

!!! note 
    Singularity is installed only on the compute nodes in Puhti and 
    it is not available for execution or testing on login nodes.

## 2. Login to Puhti supercomputer

SSH into the login node of Puhti cluster (See instructions [here](../../computing/index.md#connecting-to-the-supercomputers))

```
ssh yourcscusername@puhti.csc.fi
```
Where **yourcscusername** is the username you get from CSC.

## 3. Load  Nextflow module on Puhti

Nextflow on Puhti is available as a module and can be load as below:

```
module load nextflow/21.10.6
```

In case you need any custom installations with specific version of Nextflow in your 
workspace, please follow instructions [here](../../computing/containers/tykky.md). 

## 4. Set-up your Nextflow pipeline environment

Running Nextflow pipelines can sometimes be quite compute-intensive and 
may require downloading large volumes of data such as databases and 
singularity images. This can take a while and may not even work successfully 
in case of downloading singularity images on Puhti. 

You can do the following basic preparation before running your Nextflow pipeline:

- Copy singularity images from your local workspace to your project folder on Puhti. 
  Pay attention to the singularity cache directory (i.e., `SINGULARITY_CACHEDIR` or some 
  other name given by your software tool) which is usually `$HOME/.singularity/cache`. 
  The disk space of your home directory is quite limited (10 GB) on Puhti.
- Move all your raw data to your project directory (`/scratch/<project name>`) on Puhti
- Clone the GitHub repository of your pipeline to your scratch directory and then run your 
  pipeline. Alternatively, use the Nextflow pipeline directly 
  from DockerHub if the pipeline is available

## 5. Run your Nextflow pipeline as a batch job

Please follow our instructions for writing a batch job on Puhti as described in 
[CSC documentation pages](../../computing/running/example-job-scripts-puhti.md).

Here is a minimal script to get started with your Nextflow pipeline on Puhti:

```
#!/bin/bash
#SBATCH --time=00:15:00 # change your time settings
#SBATCH --partition=test #  change partition as needed
#SBATCH --account=project_XXX # add your project number here
#SBATCH --cpus-per-task=xx # change as you need
#SBATCH --mem-per-cpu=1G   # increase as needed

module load nextflow/21.10.6 

# Actual Nextflow command here
nextflow run  <workflow.nf> [options]
```

## 6. (Optional) tutorial - Demonstration of WtP Nextflow pipeline

WtP is a scalable and easy-to-use workflow for phage identification 
and analysis. More details about the pipeline can be found 
[here](https://github.com/replikation/What_the_Phage).

Login to Puhti and load  Nextflow module as instructed above.

## Set-up WtP pipeline on Puhti

You can either clone the WtP GitHub repository to your project scratch directory as below
(remember to edit the project name):

```
cd  /scratch/project_xxx
git clone  https://github.com/replikation/What_the_Phage.git
nextflow run /scratch/project_xxx/What_the_Phage/phage.nf --help
```

or pull the Nextflow pipeline from DockerHub:

```
nextflow run replikation/What_the_Phage  -r v0.8.0 --help
```

In either case, pay attention to the versions of different singularity 
containers as mentioned in `containers.config` file. 

### Bring your WtP singularity images to Puhti

WtP is a multi-container pipeline requiring as many as 21 singularity images 
(see [here for further details)](https://github.com/replikation/What_the_Phage/blob/master/configs/container.config) 
at the time of writing this tutorial. All these containers were downloaded 
in cPouta environment to avoid any build failures of singularity images on Puhti due to the lack 
of privileged access for users. For the sake of this tutorial, the downloaded singularity 
images were then uploaded to ``Allas`` which is an object storage environment at CSC.

The images on `Allas` object storage can be downloaded to your project directory on scratch as below:
```bash
mkdir -p /scratch/project_xxx/What_the_Phage/singularity
cd /scratch/project_xxx/What_the_Phage/singularity
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

module load nextflow/21.10.6 

# Nextflow command here
nextflow run /scratch/project_xxx/What_the_Phage/phage.nf --fasta /scratch/project_xxx/What_the_Phage/test-data/OX2_draft.fa --cores 4 --output results -profile local,singularity --cachedir /scratch/project_xxx/What_the_Phage/singularity --databases /scratch/project_xxx/What_the_Phage/databases/WtP_databases --workdir /scratch/project_xxx/What_the_Phage/workflow-phages-username 
```

Please note that the Singularity images in this example should be in the folder:
`"/scratch/project_xxx/What_the_Phage/singularity"`. Otherwise, Nextflow tries to download 
the images again which increases the likelihood of failures. Remember to edit `project_xxx`
to match your computing project.

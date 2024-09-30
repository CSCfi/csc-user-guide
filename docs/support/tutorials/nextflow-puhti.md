
# Running Nextflow pipelines on Puhti
[Nextflow](https://www.nextflow.io/) is a scalable and reproducible scientific workflow 
management system that interacts with containerised applications to perform 
compute-intensive tasks. Nextflow provides built-in support for  HPC-friendly containers 
such as Apptainer and Singularity. Although Nextflow pipelines allow us to choose Docker 
engine as an executor for running pipelines, please note that Docker 
containers can't be used in Puhti due to the lack of administrative privileges for researchers.

## Strengths of Nextflow

* Easy installation
* Supports implicit parallelism 
* Can handle complex dependencies and conditional execution
* Handles error recovery

## Disadvantages of Nextflow

* Has limited MPI support
* Creates a lot of job steps and excessive I/O load
* Does not efficiently integrate with Slurm

## Use Apptainer/Singularity containers with Nextflow
Containers can be smoothly integrated with Nextflow pipelines. No additional 
modifications in Nextflow script is needed except enabling the Singularity engine (instead of Docker) 
in the Nextflow configuration file in HPC environment. Nextflow is able to pull remote container 
images stored in Singularity or Docker-Hub registry. The remote container 
images are usually specified in Nextflow script or configuration 
file by simply prefixing the image name with the `shub://` or `docker://`. It is also possible to specify a different Singularity image for each 
process definition in the Nextflow pipeline script. 

Here is a generic recipe for running your Nextflow pipeline on Puhti:

1. Login to Puhti supercomputer 
2. Prepare your container images
3. Load Nextflow as a module on Puhti
4. Set-up your Nextflow pipeline environment
5. Run your Nextflow pipeline as a batch job
6. (Optional) tutorial - Demonstration of WtP Nextflow pipeline on Puhti
7. (Optional) tutorial - Demonstration of nf-core Nextflow pipeline using HyperQueue executor


## 1. Login to Puhti supercomputer

SSH into the login node of Puhti cluster (See instructions [here](../../computing/index.md#connecting-to-the-supercomputers))

```
ssh yourcscusername@puhti.csc.fi
```
Where **yourcscusername** is the username you get from CSC.

## 2. Prepare your Apptainer/Singularity images

Most nextflow pipelines would pull the needed container images on the fly. However, when there are multiple images are involved, it is a good idea to prepare the images locally first before launching your nextflow pipeline.

Here are some options for preparing your Apptainer/Singularity image:

- Build a Singularity/Apptainer image on Puhti without sudo access (with *--fakeroot* flag) 
- Convert a Docker image to Singularity on your local system and then copy it to Puhti.
- Convert a Docker image from a container registry on Puhti.

More information on these different options can be found on [CSC documentation](../../computing/containers/creating.md)

!!! note 
    Singularity/Apptainer is installed on the login and compute nodes and does not require loading a separate module in Puhti/Mahti/LUMI 


## 3. Load  Nextflow module on Puhti

Nextflow is available as a module on Puhti and can be load as below:

```
module load nextflow/21.10.6
```

!!! note 
     Please make sure to load the right version of the nextlfow module as some pipelines require a specific version of nextflow.  

## 4. Set-up your Nextflow pipeline environment

Running Nextflow pipelines can sometimes be quite compute-intensive and 
may require downloading large volumes of data such as databases and 
singularity images. This can take a while and may not even work successfully 
in case of downloading singularity images on Puhti. 

You can do the following basic preparation steps before running your Nextflow pipeline:

- Copy singularity images from your local workspace to your project folder on Puhti. Pay attention to the singularity cache directory (i.e., `SINGULARITY_CACHEDIR` or some other name given by your software tool) which is usually `$HOME/.singularity/cache`. 
- Move all your raw data to your project directory (`/scratch/<project name>`) on Puhti.
- Clone the GitHub repository of your pipeline to your scratch directory and then run your pipeline. 

## 5. Run your Nextflow pipeline as a batch job

Please follow our instructions for writing a batch job on Puhti as described in 
[CSC documentation pages](../../computing/running/example-job-scripts-puhti.md).

Although Nextflow comes with native slurm support, one has to be cautious on launching multiple jobs that do not take longer computing time. Instead one can launch the nextflow job as normal batch for the coexecution of all job stasks in the same job allocation. Here is a minimal script to get started with your Nextflow pipeline on Puhti:

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

!!! note 
     If you are directly pulling multiple images on the fly, please set `$TMPDIR` and `$CACHEDIR` to either local scratch (i.e., ```$LOCAL_SCRATCH```) or  /scratch folder (/scratch/project_xxx) in the batch script. Otherwise `$HOME`, directory, which is 10 GB  will be used. To avoid any diskspace errors while pulling images, set `$TMPDIR` and `$CACHEDIR`  as below:

     ```bash 
     export APPTAINER_TMPDIR=$LOCAL_SCRATCH
     export APPTAINER_CACHEDIR=$LOCAL_SCRATCH
     ```

## 6. (Optional) tutorial - Demonstration of WtP Nextflow pipeline

WtP is a scalable and easy-to-use workflow for phage identification 
and analysis. More details about the pipeline can be found 
[here](https://github.com/replikation/What_the_Phage).

Login to Puhti and load  Nextflow module as instructed above.

### Set-up WtP pipeline on Puhti

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
images were then uploaded to `Allas` which is an object storage environment at CSC.

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


## 7. (Optional) tutorial2 - Demonstration of nf-core Nextflow pipeline using HyperQueue executor

In this example, let's use HyperQueue meta executor (../../apps/hyperqueue.md) for running nextflow pipeline. This executor can be used to scale up analysis across the multiple nodes. 

Here is a batch script for running a nf-core pipeline:

```bash
#!/bin/bash
#SBATCH --job-name=nextflowjob
#SBATCH --account=project_2001659
#SBATCH --partition=small
#SBATCH --time=00:10:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=40
#SBATCH --mem-per-cpu=2G
  
module load hyperqueue/0.16.0
module load nextflow/22.10.1

# create a directory on scratch folder for running nextflow pipeline
mkdir -p /scratch/project_xxx/$USER/nextflow && cd /scratch/project_xxx/$USER/nextflow

export SINGULARITY_TMPDIR="/scratch/project_xxx/$USER/nextflow"
export SINGULARITY_CACHEDIR="/scratch/project_xxx/$USER/nextflow"
unset XDG_RUNTIME_DIR

# Specify a location for the HyperQueue server
export HQ_SERVER_DIR=${PWD}/hq-server-${SLURM_JOB_ID}
mkdir -p "${HQ_SERVER_DIR}"

# Start the server in the background (&) and wait until it has started
hq server start &
until hq job list &>/dev/null ; do sleep 1 ; done

# Start the workers in the background and wait for them to start
srun --exact --cpu-bind=none --mpi=none hq worker start --cpus=${SLURM_CPUS_PER_TASK} &
hq worker wait "${SLURM_NTASKS}"

# As an example, let's clone a nf-core pipeline (`git clone 
# https://github.com/nf-core/rnaseq.git -b 3.10``) ad run test sample
# navigate to rnaseq folder

cd rnaseq
nextflow run main.nf -profile test,singularity --outdir . -resume

# Wait for all jobs to finish, then shut down the workers and server
hq job wait all
hq worker stop all
hq server stop
```

!!! note 
     In case you are using multiple nodes, make sure to use right executor and the executor knows how many jobs it can submit. Below is an example snippet for nextflow config file:
     
     ```bash 
    echo "executor {
     queueSize = $(( 40*SLURM_NNODES ))
     name = 'hq'
    cpus = $(( 40*SLURM_NNODES )) 
    }" >> nextflow.config

    ```






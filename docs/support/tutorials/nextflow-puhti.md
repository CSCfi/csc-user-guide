# Running Nextflow pipelines on Puhti

[Nextflow](https://www.nextflow.io/) is a scalable and reproducible scientific
workflow management system that interacts with containerized applications to
perform compute-intensive tasks. Nextflow provides built-in support for
HPC-friendly containers such as Apptainer and Singularity. Although Nextflow
pipelines allow us to choose Docker engine as an executor for running
pipelines, please note that Docker containers can't be used on Puhti due to the
lack of administrative privileges for regular users.

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
modifications to Nextflow scripts are needed except enabling the Singularity
engine (instead of Docker) in the Nextflow configuration file in the HPC
environment. Nextflow is able to pull remote container images stored in
Singularity or Docker Hub registry. The remote container images are usually
specified in the Nextflow script or configuration file by simply prefixing the
image name with `shub://` or `docker://`. It is also possible to specify a
different Singularity image for each process definition in the Nextflow
pipeline script.

Here is a generic recipe for running a Nextflow pipeline on Puhti:

* [1. Login to Puhti supercomputer](#1-login-to-puhti-supercomputer)
* [2. Prepare your Apptainer/Singularity images](#2-prepare-your-apptainersingularity-images)
* [3. Load Nextflow module on Puhti](#3-load-nextflow-module-on-puhti)
* [4. Set-up your Nextflow pipeline environment](#4-set-up-your-nextflow-pipeline-environment)
* [5. Run your Nextflow pipeline as a batch job](#5-run-your-nextflow-pipeline-as-a-batch-job)
* [6. Demonstration of WtP Nextflow pipeline (optional)](#6-demonstration-of-wtp-nextflow-pipeline-optional)
* [7. Demonstration of nf-core Nextflow pipeline using HyperQueue executor (optional)](#7-demonstration-of-nf-core-nextflow-pipeline-using-hyperqueue-executor-optional)

## 1. Login to Puhti supercomputer

SSH to the login node of Puhti supercomputer
([more instructions here](../../computing/index.md#connecting-to-the-supercomputers)).

```bash
ssh <username>@puhti.csc.fi   # replace <username> with your CSC username
```

## 2. Prepare your Apptainer/Singularity images

Most Nextflow pipelines pull the needed container images on the fly. However,
when there are multiple images involved, it is a good idea to prepare the
images locally first before launching your Nextflow pipeline.

Here are some options for preparing your Apptainer/Singularity image:

* Build a Singularity/Apptainer image on Puhti without `sudo` access using
  `--fakeroot` flag.
* Convert a Docker image to Apptainer on your local system and then copy it
  to Puhti.
* Convert a Docker image from a container registry on Puhti.

More information on these different options can be found in our
[documentation on creating containers](../../computing/containers/creating.md).

!!! note
    Singularity/Apptainer is installed on the login and compute nodes and does
    not require loading a separate module on neither Puhti, Mahti or LUMI.

## 3. Load Nextflow module on Puhti

Nextflow is available as a module on Puhti and can be loaded, for example, as
below:

```bash
module load nextflow/21.10.6
```

!!! note
     Please make sure to specify the right version of the Nextflow module as
     some pipelines require a specific version of Nextflow.  

## 4. Set-up your Nextflow pipeline environment

Running Nextflow pipelines can sometimes be quite compute-intensive and may
require downloading large volumes of data, such as databases and container
images. This can take a while and may not even work successfully for the first
time when downloading multiple Apptainer/Singularity images or databases on
Puhti.

You can do the following basic preparation steps before running your Nextflow
pipeline:

* Copy Apptainer images from your local workstation to your project folder on
  Puhti. Pay attention to the Apptainer cache directory (i.e.
  `$APPTAINER_CACHEDIR`) which is usually `$HOME/.apptainer/cache`. Note that
  `$HOME` directory quota is only 10 GB on Puhti, so it may fill up quickly.
* Move all your raw data to your project directory (`/scratch/<project>`)
  on Puhti.
* Clone the GitHub repository of your pipeline to your scratch directory and
  then [run your pipeline](#5-run-your-nextflow-pipeline-as-a-batch-job).

## 5. Run your Nextflow pipeline as a batch job

Please follow our
[instructions for writing a batch job script for Puhti](../../computing/running/example-job-scripts-puhti.md).

Although Nextflow comes with native Slurm support, one has to avoid launching
large amounts of very short jobs using it. Instead, one can launch a Nextflow
job as a regular batch job that co-executes all job tasks in the same job
allocation. Below is a minimal example to get started with your Nextflow
pipeline on Puhti:

```bash
#!/bin/bash
#SBATCH --time=00:15:00            # Change your runtime settings
#SBATCH --partition=test           # Change partition as needed
#SBATCH --account=<project>        # Add your project name here
#SBATCH --cpus-per-task=<value>    # Change as needed
#SBATCH --mem-per-cpu=1G           # Increase as needed

# Load Nextflow module
module load nextflow/21.10.6 

# Actual Nextflow command here
nextflow run workflow.nf <options>
```

!!! note
     If you are directly pulling multiple images on the fly, please set
     `$APPTAINER_TMPDIR` and `$APPTAINER_CACHEDIR` to either local scratch
     (i.e. `$LOCAL_SCRATCH`) or to your scratch folder (`/scratch/<project>`)
     in the batch script. Otherwise `$HOME` directory, the size of which is
     only 10 GB, will be used. To avoid any disk quota errors while pulling
     images, set `$APPTAINER_TMPDIR` and `$APPTAINER_CACHEDIR` in your batch
     script as below:

     ```bash
     export APPTAINER_TMPDIR=$LOCAL_SCRATCH
     export APPTAINER_CACHEDIR=$LOCAL_SCRATCH
     ```

     Note that this also requires requesting NVMe disk in the batch script by
     adding `#SBATCH --gres=nvme:<value in GB>`. For example, add
     `#SBATCH --gres=nvme:100` to request 100 GB of space on `$LOCAL_SCRATCH`.

## 6. Demonstration of WtP Nextflow pipeline (optional)

WtP is a scalable and easy-to-use workflow for phage identification and
analysis.
[See here for more details about the pipeline](https://github.com/replikation/What_the_Phage).

[Login to Puhti](#1-login-to-puhti-supercomputer) and
[load a Nextflow module as instructed above](#3-load-nextflow-module-on-puhti).

### 6.1 Set-up WtP pipeline on Puhti

You can either clone the WtP GitHub repository to your project scratch
directory as below (remember to replace `<project>` with your project name):

```bash
cd /scratch/<project>
git clone https://github.com/replikation/What_the_Phage.git
nextflow run /scratch/<project>/What_the_Phage/phage.nf --help
```

or pull the Nextflow pipeline from Docker Hub:

```bash
nextflow run replikation/What_the_Phage -r v0.8.0 --help
```

In either case, pay attention to the versions of different
Singularity/Apptainer containers as mentioned in `containers.config` file.

### 6.2 Bring your WtP Apptainer images to Puhti

WtP is a multi-container pipeline requiring as many as 21 container images
([more details here](https://github.com/replikation/What_the_Phage/blob/master/configs/container.config))
at the time of writing this tutorial. All these containers were downloaded
to a cPouta environment to avoid any build failures of container images on
Puhti due to the lack of root privileges for users. For the sake of this
tutorial, the downloaded container images were then uploaded to
[Allas](../../data/Allas/introduction.md) which is an object storage
environment at CSC.

The images in Allas object storage can be downloaded to your project scratch as
below:

```bash
mkdir -p /scratch/<project>/What_the_Phage/singularity
cd /scratch/<project>/What_the_Phage/singularity
wget https://a3s.fi/puhti_singularity/WtP_singularity.tar.gz
tar -xavf WtP_singularity.tar.gz
```

### 6.3 Run WtP pipelines as a batch job on Puhti

Submit the following batch script to run the Nextflow pipeline:

```bash
#!/bin/bash
#SBATCH --time=01:00:00
#SBATCH --partition=small
#SBATCH --account=<project>
#SBATCH --cpus-per-task=4

export TMPDIR=${PWD}
export SCRATCH=/scratch/<project>/What_the_Phage

# Activate Nextflow on Puhti
module load nextflow/21.10.6 

# Nextflow command here
nextflow run ${SCRATCH}/phage.nf \
         --fasta ${SCRATCH}/test-data/OX2_draft.fa \
         --cores 4 \
         --output results \
         --profile local,singularity \
         --cachedir ${SCRATCH}/singularity \
         --databases ${SCRATCH}/databases/WtP_databases \
         --workdir ${SCRATCH}/workflow-phages-username
```

Please note that the container images in this example should be in the folder
`/scratch/<project>/What_the_Phage/singularity`. Otherwise, Nextflow tries to
download the images again which increases the likelihood of failures. Remember
to edit `<project>` to match your actual CSC computing project name.

## 7. Demonstration of nf-core Nextflow pipeline using HyperQueue executor (optional)

In this example, let's use [HyperQueue meta executor](../../apps/hyperqueue.md)
for running Nextflow pipeline. This executor can be used to scale up analysis
across the multiple nodes when needed.

Here is a batch script for running a nf-core pipeline on Puhti:

```bash
#!/bin/bash
#SBATCH --job-name=nextflowjob
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=00:10:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=40
#SBATCH --mem-per-cpu=2G
  
module load hyperqueue/0.16.0
module load nextflow/22.10.1

# create a directory on scratch folder for running nextflow pipeline
export SCRATCH=/scratch/<project>/$USER/nextflow
mkdir -p ${SCRATCH}
cd ${SCRATCH}

export APPTAINER_TMPDIR="${SCRATCH}"
export APPTAINER_CACHEDIR="${SCRATCH}"
unset XDG_RUNTIME_DIR

# Specify a location for the HyperQueue server
export HQ_SERVER_DIR=${PWD}/hq-server-${SLURM_JOB_ID}
mkdir -p "${HQ_SERVER_DIR}"

# Start the server in the background (&) and wait until it has started
hq server start &
until hq job list &>/dev/null ; do sleep 1 ; done

# Start the workers in the background and wait for them to start
srun --overlap --cpu-bind=none --mpi=none hq worker start --cpus=${SLURM_CPUS_PER_TASK} &
hq worker wait "${SLURM_NTASKS}"

# As an example, let's clone a nf-core pipeline and run a test sample
git clone https://github.com/nf-core/rnaseq.git -b 3.10
cd rnaseq
nextflow run main.nf -profile test,singularity --outdir . -resume

# Wait for all jobs to finish, then shut down the workers and server
hq job wait all
hq worker stop all
hq server stop
```

!!! note
     In case you are using multiple nodes, ensure that you use the right
     executor and that the executor knows how many jobs it can submit. For
     this, below is an example snippet that one should add to the
     `nextflow.config` file:

     ```text
     executor {
     queueSize = 40*SLURM_NNODES
     name = 'hq'
     cpus = 40*SLURM_NNODES
     }
     ```

## More information

* [Official Nextflow documentation](https://www.nextflow.io/docs/latest/index.html)
* [CSC's Nextflow documentation](../../apps/nextflow.md)
* [High-throughput Nextflow workflow using HyperQueue](nextflow-hq.md)

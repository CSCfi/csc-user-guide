# Running Nextflow pipelines on Puhti and Mahti

[Nextflow](https://www.nextflow.io/) is one of the scientific wokrflow managers and provides built-in support for
HPC-friendly containers such as Apptainer (= Singularity). One of the advantages of Nextflow is that the actual pipeline functional logic is separated from the execution environment. The same script can therefore be executed in different environments by changing the execution environment without touching actual pipeline code. Nextflow uses `executor` information to decide where the job should be run. Once executor is configured, Nextflow submits each process to the specified job scheduler on your behalf (=you don't need to write sbatch script, Nextflow writes on the fly for you, instead ).

Default executor is `local` where process is run in your computer/localhost where Nextflow is launched.  Other executors include:

- SLURM
- PBS/Torque
- Amazon (AWS Batch)
- SGE (Sun Grid Engine)

There are many other high-throughput tools and workflow managers exist for scientific computing and selecting the right tool can sometimes be challenging. Please refer to our [high-throughput computing and workflows page](../../computing/running/throughput.md) to get an overview from the selected list of relevant tools.

## Installation
 
### Nextflow

Nextflow itself is available as a module on Puhti and Mahti. One can choose the version of the nextflow depending on the requirement of your own pipeline. Please note that the Nextflow version starting from 23.04.3 can only be
used for pipelines built with DSL2 syntax. You can select a lower version for DSL1-compliant pipelines.

Nextflow can be loaded as below:

```bash
module load nextflow/<version>     # e.g., module load nextflow/22.10.1
```

Please note that one has to load Nextflow module with a version. Otherwise, the latest version of stable module installed at that point is used. For the reproducibility point of view, make sure to load versions of all tools including the Nextflow module.

!!! info "Note"
     Please make sure to specify the correct version of the Nextflow module as
     some pipelines require a specific version of Nextflow.


### Installation of tools used in Nextflow

1. Local installations: By default, Nextflow expects that the analysis tools are available locally. Tools can be activated from existing [modules](../../apps/by_discipline.md) or [own custom module installations](../../computing/modules.md#using-your-own-module-files).
    
2. Container instalaltions:
Containers can be smoothly integrated with Nextflow pipelines. No additional
modifications to Nextflow scripts are needed except enabling the
Apptainer engine in the Nextflow configuration
file in the HPC environment. Nextflow can pull remote container images as Apptainer
from container registries on the fly. The remote container images are
usually specified in the Nextflow script or configuration file by simply
prefixing the image name with `shub://` or `docker://`. It is also possible to
specify a different Apptainer image for each process definition in the
Nextflow pipeline script.

Although Nextflow
allows choosing Docker engine for running
pipelines, please note that Docker containers can't be used on supercomputers due to the
lack of administrative privileges for normal users.

Most Nextflow pipelines pull the needed container images on the fly. However,
when multiple images are needed in a pipeline, it is a good idea to prepare the
images locally first before launching your Nextflow pipeline. More information about [creating containers](../../computing/containers/creating.md).


!!! info "Note"
    Apptainer is installed on login and compute nodes and does
    not require loading a separate module on either Puhti, Mahti or LUMI.

    * For binding folders or using other Apptainer flags, use [--apptainer-args option] or delcare in the nextflow.config files.

!!! info "Note"
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

Running Nextflow pipelines can sometimes be quite compute-intensive and may
require downloading large volumes of data such as databases and container
images. This can take a while and may not even work successfully for the first
time when downloading multiple Apptainer images or databases.



## Usage

Nextflow pipelines can be run in different ways in supercomputering environment:

1. [In interactive mode](../../computing/running/interactive-usage.md) with local executor, with limited resources. Useful mainly for debugging or testing very small workflows.
2. With batch job and local executor. Useful for small and medium size workflows
3. With batch job and SLURM executor. This can use multiple nodes and different SLURM partitions (CPU and GPU), but may create significant overhead, with many small jobs. Could be used, if each job step for each file takes at least 30 min.
4. With batch job and HyperQueue as a sub-job scheduler. Can use multiple nodes in the same batch job allocation, most complex set up. Suits well for cases, when workflow includes a lot of small job steps with many input files (high-troughput computing).

!!! info "Note"
    Please do not launch heavy Nextflow workflows on login nodes.

Please follow our
[instructions for writing a batch job script for Puhti](../../computing/running/example-job-scripts-puhti.md).

### Nextflow script

The following minimalist example demonstrates the basic syntax of Nextflow.

```nextflow title="workflow.nf"
#!/usr/bin/env nextflow
  
greets = Channel.fromList(["Moi", "Ciao", "Hello", "Hola","Bonjour"])

/*
 * Use echo to print 'Hello !' in different languages to a file
 */

process sayHello {

  input:
    val greet

  output:
    path "${greet}.txt"

  script:
    """
    echo ${greet} > ${greet}.txt
    """
}

workflow {

    // Print  a greeting
    sayHello(greets)
}

```
This script defines one process named `sayHello`. This process takes a set of greetings from different languages and then writes each one to a separate file in a random order.

The resulting terminal output would look similar to the text shown below:

```bash
N E X T F L O W  ~  version 23.04.3
Launching `hello-world.nf` [intergalactic_panini] DSL2 - revision: 880a4a2dfd
executor >  local (5)
[a0/bdf83f] process > sayHello (5) [100%] 5 of 5 ✔
```

### Running Nextflow pipeline with local executor interactively
To run Nextflow in [interactive session](https://docs.csc.fi/computing/running/interactive-usage/):
```
sinteractive -c 2 -m 4G -d 250 -A project_2xxxx  # replace actual project number here
module load nextflow/23.04.3                     # Load nextflow module
nextflow run workflow.nf
```

### Running Nextflow with local executor in a batch job

To launch a Nextflow job as a regular batch job that executes all job tasks in the same job
allocation, create the batch job file:

```bash title="nextflow_local_batch_job.sh"
#!/bin/bash
#SBATCH --time=00:15:00            # Change your runtime settings
#SBATCH --partition=test           # Change partition as needed
#SBATCH --account=<project>        # Add your project name here
#SBATCH --cpus-per-task=<value>    # Change as needed
#SBATCH --mem-per-cpu=1G           # Increase as needed

# Load Nextflow module
module load nextflow/23.04.3

# Actual Nextflow command here
nextflow run workflow.nf <options>
# nf-core pipeline example:
# nextflow run nf-core/scrnaseq  -profile test,singularity -resume --outdir .
```

Finally, submit the job to the supercomputer:

```
sbatch nextflow_local_batch_job.sh
```

### Running Nextflow with SLURM executor 

The first batch job file reserves resources only for Nextflow itself. Nextflow then creates further SLURM jobs for workflow's processes. The SLURM jobs created by Nextflow may be distributed to several nodes of a supercomputer and also to use different partitions for different workflow rules, for example CPU and GPU. SLURM executor should be used only, if the job steps are at least 20-30 minutes long, otherwise the it could overload SLURM.

!!! warning
    Please do not use SLURM executor, if your workflow includes a lot of short processes. It would overload SLURM.

To enable the SLURM executor, set the `process.xx` settings in [nextflow.config file](https://www.nextflow.io/docs/latest/config.html). The settings are similar to [batch job files](../../computing/running/example-job-scripts-puhti.md).

```bash title="nextflow.config"
profiles {


 standard {
     process.executor = 'local'
   }

 puhti {
     process.clusterOptions = '--account=project_xxxx --ntasks-per-node=1 --cpus-per-task=4 --ntasks=1 --time=00:00:05'
     process.executor = 'slurm'
     process.queue = 'small'
     process.memory = '10GB'
    }
    
}
```

Create the batch job file, note the usage of a profile.

```bash title="nextflow_slurm_batch_job.sh"
#!/bin/bash
#SBATCH --time=00:15:00            # Change your runtime settings
#SBATCH --partition=test           # Change partition as needed
#SBATCH --account=<project>        # Add your project name here
#SBATCH --cpus-per-task=1    # Change as needed
#SBATCH --mem-per-cpu=1G           # Increase as needed

# Load Nextflow module
module load nextflow/23.04.3

# Actual Nextflow command here
nextflow run workflow.nf -profile puhti
```

Finally, submit the job to the supercomputer:

```
sbatch nextflow_slurm_batch_job.sh
```

This will submit each process of your workflow as a separate batch job to Puhti supercomputer.


### Running Nextflow with HyperQueue executor

[HyperQueue meta-scheduler](../../apps/hyperqueue.md) executer is suitable, if your workflow includes a lot of short processes and you need several nodes for the computation. However, the executor settings can be complex depending on the pipeline.

Here is a batch script for running a
[nf-core pipeline](https://nf-co.re/pipelines):

```bash title="nextflow_hyperqueue_batch_job.sh"
#!/bin/bash
#SBATCH --job-name=nextflowjob
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=01:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=40
#SBATCH --mem-per-cpu=2G
  
module load hyperqueue/0.16.0
module load nextflow/22.10.1
module load git

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

# Ensure Nextflow uses the right executor and knows how many jobs it can submit
# The `queueSize` can be limited as needed. 
echo "executor {
  queueSize = $(( 40*SLURM_NNODES ))
  name = 'hq'
  cpus = $(( 40*SLURM_NNODES ))
}" >> nextflow.config

nextflow run main.nf -profile test,singularity --outdir . -resume

# Wait for all jobs to finish, then shut down the workers and server
hq job wait all
hq worker stop all
hq server stop
```

Finally, submit the job to the supercomputer:

```
sbatch nextflow_hyperqueue_batch_job.sh
```

## More information

* [Official Nextflow documentation](https://www.nextflow.io/docs/latest/index.html)
* [CSC's Nextflow documentation](../../apps/nextflow.md)
* [Master thesis by Antoni Gołoś comparing automated workflow approaches on supercomputers](https://urn.fi/URN:NBN:fi:aalto-202406164397)
  * [Full code Nextflow example from Antoni Gołoś with 3 different executors for Puhti](https://github.com/antonigoo/LIPHE-processing/tree/nextflow/workflow)

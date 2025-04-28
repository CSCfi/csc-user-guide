# Running Nextflow pipelines on supercomputers

[Nextflow](https://www.nextflow.io/) is a scientific workflow manager and provides built-in support for
HPC-friendly containers such as Apptainer (= Singularity). One of the advantages of Nextflow is that the actual pipeline functional logic is separated from the execution environment. The same script can therefore be executed in different environments by changing the execution environment without touching actual pipeline code. Nextflow uses `executor` information to decide where the job should be run. Once executor is configured, Nextflow submits each process to the specified job scheduler on your behalf.

Default executor is `local` where processes are run in the computer where Nextflow is launched. Several other [executors](https://www.nextflow.io/docs/latest/executor.html) are supported, the CSC computing environments best suit SLURM and HyperQueue executors.

There are many other high-throughput tools and workflow managers for scientific computing and selecting the right tool can sometimes be challenging. Please refer to our [high-throughput computing and workflows page](../../computing/running/throughput.md) to get an overview of relevant tools.

## Installation
 
### Nextflow

Nextflow itself is available as a module on Puhti, Mahti and LUMI. Specific versions available are described on the [Nextflow main page](../../apps/nextflow.md).

### Installation of tools used in Nextflow

#### Local installations

By default, Nextflow expects that the analysis tools are available locally. Tools can be activated from existing [modules](../../apps/by_discipline.md) or [own custom module installations](../../computing/modules.md#using-your-own-module-files). See also how to [create containers](../../computing/containers/creating.md).
    
#### On-the-fly Apptainer installations

Containers can be smoothly integrated with Nextflow pipelines. No additional
modifications to Nextflow scripts are needed except for enabling the
Apptainer engine in the Nextflow configuration
file. Nextflow can pull remote container images as Apptainer
from container registries on the fly. The remote container images are
usually specified in the Nextflow script or configuration file by simply
prefixing the image name with `shub://` or `docker://`. It is also possible to
specify a different Apptainer image for each process definition in the
Nextflow pipeline script.

Most Nextflow pipelines pull the needed container images on the fly. However,
when multiple images are needed in a pipeline, it is a good idea to prepare the
containers locally before launching the Nextflow pipeline. 

Practical considerations:

* Apptainer is installed on login and compute nodes and does not require loading a separate module on CSC supercomputers.
* For binding folders or using other [Apptainer settings](https://www.nextflow.io/docs/latest/reference/config.html#apptainer) use `nextflow.config` file.
* If you are directly pulling multiple Apptainer images on the fly, please use the NVMe disk of a compute node for storing the Apptainer images. For that in your batch job file, first request NVMe disk space and then set Apptainer temporary folders as environmental variables.

```bash title="batch_job.sh"
#SBATCH --gres=nvme:100   # Request 100 GB of space to local disk

export APPTAINER_TMPDIR=$LOCAL_SCRATCH
export APPTAINER_CACHEDIR=$LOCAL_SCRATCH
```

!!! warning
    Although Nextflow supports also Docker containers, these can't be used as such on supercomputers due to the lack of administrative privileges for normal users.

## Usage

Nextflow pipelines can be run in different ways in the supercomputer environment:

1. [In interactive mode](../../computing/running/interactive-usage.md) with local executor, with limited resources. Useful mainly for debugging or testing very small workflows.
2. With batch job and local executor. Useful for small and medium size workflows.
3. With batch job and SLURM executor. This can use multiple nodes and different SLURM partitions (CPU and GPU), but may create significant overhead, with many small jobs. Could be used, if each job step for each file takes at least 30 min.
4. With batch job and HyperQueue as a sub-job scheduler. Can use multiple nodes in the same batch job allocation, most complex set up. Well-suited for cases, when the workflow includes a lot of small job steps with many input files (high-troughput computing).

For general introduction to batch jobs, see [example job scripts for Puhti](../../computing/running/example-job-scripts-puhti.md).

!!! Note
    Whenever you're unsure how to run your workflow efficiently, don't hesitate
    to [contact CSC Service Desk](../contact.md).

### Nextflow script

The following minimalist example demonstrates the basic syntax of a Nextflow script.

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

    // Print a greeting
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

To run Nextflow in [interactive session](../../computing/running/interactive-usage.md):
```
sinteractive -c 2 -m 4G -d 250 -A project_2xxxx  # replace actual project number here
module load nextflow/23.04.3                     # Load nextflow module
nextflow run workflow.nf
```

!!! info "Note"
    Please do not launch heavy Nextflow workflows on login nodes.

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

If the workflow includes only limited number of individual jobs/job steps [SLURM executor of Nextflow](https://www.nextflow.io/docs/latest/executor.html#slurm) could be considered.

The first batch job file reserves resources only for Nextflow itself. Nextflow then creates further SLURM jobs for workflow's processes. The SLURM jobs created by Nextflow may be distributed to several nodes of a supercomputer and also to use different partitions for different workflow rules, for example CPU and GPU. SLURM executor should be used only, if the job steps are at least 20-30 minutes long, otherwise it may overload SLURM.

!!! warning
    Please do not use SLURM executor, if your workflow includes a lot of short processes. It would overload SLURM. Use HyperQueue executor instead.

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
#SBATCH --cpus-per-task=1          # Change as needed
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
#SBATCH --partition=small
#SBATCH --account=<project>
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=40
#SBATCH --mem-per-cpu=2G
#SBATCH --time=01:00:00

# Load the required modules
module load hyperqueue
module load nextflow

# Create a per job directory
wrkdir=${PWD}/WRKDIR-${SLURM_JOB_ID}

# Set the directory which hyperqueue will use 
export HQ_SERVER_DIR=${wrkdir}/.hq-server
mkdir -p ${HQ_SERVER_DIR}

# Start the server in the background (&) and wait until it has started
hq server start &
until hq job list &>/dev/null ; do sleep 1 ; done

# Start the workers in the background and wait for them to start
srun --overlap --cpu-bind=none --mpi=none hq worker start --cpus=${SLURM_CPUS_PER_TASK} &
hq worker wait "${SLURM_NTASKS}"

# change to the work directory if needed 

cd ${wrkdir}
# Ensure Nextflow uses the right executor and knows how many jobs it can submit
# The `queueSize` can be limited as needed. 
											
echo "executor {
  queueSize = $(( 40*SLURM_NNODES ))
  name = 'hq'
  cpus = $(( 40*SLURM_NNODES ))
}" >> ${wrkdir}/nextflow.config

# run the Nextflow pipeline here 
nextflow run main.nf <options>

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
* [General guidelines for high-throughput computing in CSC's HPC environment](../../computing/running/throughput.md)
* [Official HyperQueue documentation](https://it4innovations.github.io/hyperqueue/stable/)
* [CSC's HyperQueue documentation](../../apps/hyperqueue.md) 


# Running Nextflow pipelines on Puhti

[Nextflow](https://www.nextflow.io/) is one of the scientific wokrflow managers and provides built-in support for
HPC-friendly containers such as Apptainer and Singularity. Although Nextflow
allows choosing Docker engine for running
pipelines, please note that Docker containers can't be used on Puhti due to the
lack of administrative privileges for normal users.

There are many other high-throughput tools and workflow managers exist for scientific computing and selecting the right tool can sometimes be challenging. Please refer to our [high-throughput computing and workflows page](../../computing/running/throughput.md) to get an overview from the selected list of relevant tools.

## Installation
 
### Custom installations
The installation of Nextflow is easy as it is java-based tool. You can for example download the latest version of Nextflow binary to your /home directory  on Puhti as below: 

```bash

module load biojava/21
curl -s https://get.nextflow.io | bash && mv nextflow ~/bin
chmod +x ~/bin/nextflow

```

### Nextflow module
Nextflow is also available as a module on Puhti. One can choose the version of the nextflow depending on the requirement of your own pipeline. Please note that the Nextflow version starting from 23.04.3 can only be
used for pipelines built with DSL2 syntax. You can downgrade to lower versions for DSL1-compliant pipelines.


Nextflow can be loaded as
below:

```bash
module load nextflow/<version>     # e.g., module load nextflow/22.10.1
```

!!! info "Note"
     Please make sure to specify the correct version of the Nextflow module as
     some pipelines require a specific version of Nextflow.


### Installation of tools used in Nextflow

1. Local installations: By default, Nextflow expects that the analysis tools are available locally. Tools can be activated from existing [Puhti modules](../../apps/by_discipline.md) or [own custom module installations](../../computing/modules.md#using-your-own-module-files).
    
2. Container instalaltions:
Containers can be smoothly integrated with Nextflow pipelines. No additional
modifications to Nextflow scripts are needed except enabling the
Singularity/Apptainer engine in the Nextflow configuration
file in the HPC environment. Nextflow can pull remote container images as Singularity/Apptainer
from container registries on the fly. The remote container images are
usually specified in the Nextflow script or configuration file by simply
prefixing the image name with `shub://` or `docker://`. It is also possible to
specify a different Singularity image for each process definition in the
Nextflow pipeline script.

Most Nextflow pipelines pull the needed container images on the fly. However,
when multiple images are needed in a pipeline, it is a good idea to prepare the
images locally first before launching your Nextflow pipeline.

Here are some options for preparing your Apptainer/Singularity image:

* Build a Singularity/Apptainer image on Puhti without `sudo` access using
  `--fakeroot` flag.
* Convert a Docker image to Apptainer on your local system and then copy it
  to Puhti.
* Convert a Docker image from a container registry on Puhti.

More information on these different options can be found in our
[documentation on creating containers](../../computing/containers/creating.md).

!!! info "Note"
    Singularity/Apptainer is installed on login and compute nodes and does
    not require loading a separate module on either Puhti, Mahti or LUMI.
    * Apptainer container can be downloaded from some repository or built locally. For building custom Apptainer containers, see [Creating containers page](../../computing/containers/creating.md).

    * For binding folders or using other Apptainer flags, use [--apptainer-args option] or delcare in the nextflow.config files.

Running Nextflow pipelines can sometimes be quite compute-intensive and may
require downloading large volumes of data such as databases and container
images. This can take a while and may not even work successfully for the first
time when downloading multiple Apptainer/Singularity images or databases.


## Usage
Nextflow pipelines can be run in different ways in supercomputering environment:

1. [In interactive mode](../../computing/running/interactive-usage.md) with local executor, with limited resources. Useful mainly for debugging or testing very small workflows.
2. With batch job and local executor. Useful for small and medium size workflows
3. With batch job and SLURM executor. This can use multiple nodes and different SLURM partitions (CPU and GPU), but may create significant overhead, if many small jobs. Could be used, if each job step for each file takes at least 30 min.
4. With batch job and HyperQueue as a sub-job scheduler. Can use multiple nodes in the same batch job allocation, most complex set up. Suits well for cases, when workflow includes a lot of small job steps with many input files (high-troughput computing).

!!! info "Note"
    Please do not launch heavy Nextflow workflows on login nodes.

### Running Nextflow pipeline with local executor interactively
Lanuch an [interactive session](https://docs.csc.fi/computing/running/interactive-usage/) on Puhti as below:
```
sinteractive -c 2 -m 4G -d 250 -A project_2xxxx  # replace actual project number here
module load nextflow/23.04.3                     # Load nextflow module
```

Please note that one has to load Nextflow module with a version. Otherwise, the latest version of stable module installed at that point is used. For the reproducibility point of view, make sure to load versions of all tools including the Nextflow module.


The following "Hello-world" minimalist example demonstrates the basic syntax of Nextflow. Copy the below script to a file named, hello-world.nf.

```nextflow
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

 Execute the script by entering the following command on Puhti interactive terminal: 

```nextflow
module load nextflow/23.04.3
nextflow run hello-world.nf
```
This script defines one process named `sayHello`. This process takes a set of greetings from different languages and then writes each one to a separate file in a random order.

The resulting terminal output would look similar to the text shown below:

```nextflow
N E X T F L O W  ~  version 23.04.3
Launching `hello-world.nf` [intergalactic_panini] DSL2 - revision: 880a4a2dfd
executor >  local (5)
[a0/bdf83f] process > sayHello (5) [100%] 5 of 5 ✔
```

### Running Nextflow  with local executor in a batch job

Please follow our
[instructions for writing a batch job script for Puhti](../../computing/running/example-job-scripts-puhti.md).

Although Nextflow supports SLURM natively, avoid launching
large amounts of very short jobs using SLURM. Instead, one can launch a Nextflow
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
module load nextflow/23.04.3

# Actual Nextflow command here
nextflow run workflow.nf <options>
# nf-core pipeline example: nextflow run nf-core/scrnaseq  -profile test,singularity -resume --outdir .
```

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


Finally, copy above script to a fle (e.g., nextflow_script.sh) and  submit the job to cluster as below:

```
sbatch nextflow_script.sh
```

Monitor the status of submitted Slurm job

```
   squeue -j <slurmjobid>
   # or
   squeue --me
   # or
   squeue -u $USER
```

### Running Nextflow  with SLURM executor (Currently NOT recommended on Puhti when you have several small jobs)

One of the advantages of Nextflow is that the actual pipeline functional logic is separated from the execution environment. The same script can therefore be executed in different environments by changing the execution environment without touching actual pipeline code. Nextflow uses `executor` information to decide where the job should be run. Once executor is configured, Nextflow submits each process to the specified job scheduler on your behalf (=you don't need to write sbatch script, Nextflow writes on the fly for you, instead ).

Default executor is `local` where process is run in your computer/localhost where Nextflow is launched.  Other executors include:

- PBS/Torque
- SLURM
- Amazon (AWS Batch)
- SGE (Sun Grid Engine)

To enable the SLURM executor on Puhti, simply set  `process.executor` property to slurm value in the `nextflow.config` file as shown below:

```
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

In this case, you can run a Nextflow script as below: 

```
nextflow run <nextflow_script> -profile puhti
```
This will submit each process of your job as a separate batch job to Puhti cluster.


### Running Nextflow with HyperQueue executor

In this example, let's use the
[HyperQueue meta-scheduler](../../apps/hyperqueue.md) for executing a Nextflow
pipeline. This executor can be used to scale up analysis across multiple nodes
when needed. However, the executor settings can be complex depending on the pipeline.

Here is a batch script for running a
[nf-core pipeline](https://nf-co.re/pipelines) on Puhti:

```bash
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

# Ensure Nextflow uses the right executor and knows how much it can submit
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

!!! info "Note"
     Please make sure that your Nextflow configuration file (`nextflow.config`)
     has the correct executor name when using the HypeQueue executor. Also,
     when multiple nodes are used, ensure that the executor knows how many jobs
     it can submit using the parameter `queueSize` under the `executor` block.
     The `queueSize` can be limited as needed. Here is an example snippet that
     you can use and modify as needed in your `nextflow.config` file:

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

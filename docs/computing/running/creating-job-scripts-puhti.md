# Creating a batch job script for Puhti

A batch job script contains the definitions for the resources to be reserved for
the job and the commands the user wants to run.

[TOC]


## A basic batch job script

An example of a simple batch job script:
```
#!/bin/bash
#SBATCH --job-name=myTest
#SBATCH --account=<project>
#SBATCH --time=02:00:00
#SBATCH --mem-per-cpu=2G
#SBATCH --partition=small

module load myprog/1.2.3

srun myprog -i input -o output
```
The first line `#!/bin/bash` tells that the file should be interpreted
as a bash script.

The lines starting with `#SBATCH` are arguments for the batch system.
These examples only use a small subset of the options. For a list of all possible
options, see the [Slurm documentation](https://slurm.schedmd.com/sbatch.html).

The general syntax of a `#SBATCH` option:
```
#SBATCH option_name argument
```

In our example,
```
#SBATCH --job-name=myTest
```
sets the name of the job. It can be used to identify a job in the queue and
other listings.

```
#SBATCH --account=<project>
```
sets the billing project for the job. **This argument is mandatory. Failing to
set it will cause the job to be held with the reason _AssocMaxJobsLimit_**
Please replace `<project>` with the Unix group of the project. You 
can find it in [My CSC](https://my.csc.fi) under the _My projects_ tab. More 
information about [billing](../../accounts/billing.md).

The time reservation is set with option `--time`

```
#SBATCH --time=10:00:00
```

Time is provided using the format __hh:mm:ss__ (optionally __d-hh:mm:ss__, where
__d__ is _days_). The maximum time depends on the selected queue. When the time
reservation ends, the job is terminated regardless of whether it is finished or not, so the time
reservations should be sufficiently long. A job consumes billing units according to
its actual runtime.

```
#SBATCH --mem-per-cpu=2G
```
sets the required memory per requested CPU core. If the requested
memory is exceeded, the job is terminated.

The partition needs to be set according to the job requirements.
```
#SBATCH --partition=small
```

!!! Note "Available partitions"
    [The available batch job partitions](batch-job-partitions.md).


After defining all required resources in the batch job script, set up the 
environment. Note that for modules to be available for batch jobs, they need to be loaded in
the batch job script.

```
module load myprog/1.2.3
```

Finally, we launch our program using the `srun` command:
```
srun myprog -i input -o output
```


## Serial and shared memory batch jobs

Serial and shared memory jobs need to be run within one computing node. Thus, the jobs are limited by the hardware specifications available in the nodes. In Puhti, each node has two processors with 20 cores each, i.e. 40 cores in total.

The Sbatch option `--cpus-per-task` is used the define the number of computing cores that the batch job task uses. The option `--nodes=1` ensures that all the reserved cores are located in the same node, and `--ntasks=1` assigns all reserved computing cores for the same task.

In thread-based jobs, the `--mem` option is recommended for memory reservation. This option defines the amount of memory required per node. Note that if you use `--mem-per-cpu` option instead, the total memory request of the job will be the memory request multiplied by the number of reserved cores (`--cpus-per-task`). Thus, if you modify the number of cores, also check the memory reservation.

In most cases, it is the most efficient to match the number of reserved cores to the number of threads or processes the application uses. Check the documentation for application-specific details.

If the application has a command line option to set the number of threads/processes/cores, it should always be used to make sure the software behaves as expected. Some applications use only one core by default, even if more are reserved.

Some other applications may try to use all cores in the node even if only some are reserved. The environment variable `$SLURM_CPUS_PER_TASK` can be used instead of a number. This way, the command does not need to be edited if the `--cpus-per-task` is changed. Use the environment variable `OMP_NUM_THREADS` to set the number of threads the program uses.


## MPI-based batch jobs

In MPI jobs, each task has its own memory allocation. Thus, the tasks can be distributed between nodes.
 
Set the number of MPI tasks:
``` 
 --ntasks=<number_of_mpi_tasks>
```
 
If more fine-tuned control is required, the exact number of nodes and number of tasks per node can be specified with
`--nodes` and `--ntasks-per-node`, respectively.

It is recommended to request memory using the `--mem-per-cpu` option.


!!! Note
    - MPI should **not** be started with _mpirun_ or _mpiexec_, use `srun` instead.
    - A MPI module has to be loaded in the batch job script for the submission to work properly.

## Hybrid batch jobs 

In hybrid jobs, each tasks is allocated several cores. Each tasks then uses some other parallelization than MPI to do work.
The most common strategy is for every MPI-task to launch multiple threads using OpenMP. 
To request more cores per MPI task, use the argument `--cpus-per-task`. The default value is one core per task. 
 
The optimal ratio between the number of tasks and cores per tasks varies for each program, testing is required to find
the right combination for your application. 

!!! Note
    By default, running a single task per node with multiple threads using **hpcx-mpi** will bind all threads to a single
    core and no speedup will be gained. This can be fixed by setting `export OMP_PROC_BIND=true` in your job script. This
    will bind the threads to different cores. Another possibility is to turn off slurms core binding with the `srun` flag `--cpu-bind=none`. 


## Additional resources in batch jobs

### Local storage 

Some nodes in Puhti have a local fast storage available for jobs. The local storage is good for I/O-intensive programs.

The local storage is available on:

* GPU nodes in the `gpu` and `gputest` partitions
* I/O nodes shared by the `small`, `large` and `longrun` partitions

Request local storage using the `--gres` flag in the job submission:
```
--gres=nvme:<local_storage_space_per_node>
```
The amount of space is given in GB (with a maximum of 3600 GB per node).  For example, to request 100 GB of storage, use option `--gres=nvme:100`. The local storage reservation is on a per node basis.

Use the environment variable `$LOCAL_SCRATCH` in your batch job scripts to access the local storage on each node.

!!! Note
    The local storage is emptied after the job has finished, so please move any data you want to keep to
    the shared disk area.


### GPUs

Puhti has 320 NVIDIA Tesla V100 GPUs. The GPUs are available on the `gpu` and `gputest` partitions using the option:
```
--gres=gpu:v100:<number_of_gpus_per_node>
```
The `--gres` reservation is on a per node basis. There are 4 GPUs per GPU node. 

Multiple resources can be requested with a comma-separated list.

Request both GPU and local storage:
```
--gres=gpu:v100:<number_of_gpus_per_node>,nvme:<local_storage_space_per_node>
```

For example, to request 1 GPU and 10 GB of NVME storage the option would be `--gres=gpu:v100:1,nvme:10`.

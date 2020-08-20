# Creating a batch job script for Mahti

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
#SBATCH --partition=medium

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

## MPI-based batch jobs

<-- FIXME add hyperthreading, maybe as a subheader level topic? -->

The recommended way to is to specify the exact number of nodes and number of tasks per node  with
`--nodes` and `--ntasks-per-node`, respectively. For MPI-only job, use all cores in the node, either
128 for all physical nodes, or 256 including also the virtual cores (or hyperthreading or SMT).

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

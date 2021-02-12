# Creating a batch job script for Mahti

Please have a look at the [Puhti documentation](creating-job-scripts-puhti.md)
for the general introduction to batch scripts in the CSC supercomputing
environment. On this page we focus on Mahti specific topics.

!!! Note
    Mahti does not have GPUs, NVMe disk on compute nodes, or the need
    to reserve memory. Instead, full nodes are allocated for jobs,
    with the exception of [interactive jobs](../interactive-usage/#sinteractive-in-mahti), also
    [see below](#using-interactive-partition-for-non-parallel-pre-or-post-processing). Many options also work
    differently in Puhti and Mahti, so it is not advisable to copy scripts from Puhti
    to Mahti.

[TOC]


## Basic MPI batch jobs

An example of a simple MPI batch job script:
```
#!/bin/bash
#SBATCH --job-name=myTest
#SBATCH --account=<project>
#SBATCH --time=02:00:00
#SBATCH --partition=medium
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=128

module load myprog/1.2.3

srun myprog -i input -o output
```

Specify the exact number of nodes and number of tasks per node  with
`--nodes` and `--ntasks-per-node`, respectively. Use all 128 cores in
the node.

!!! Note
    - MPI processes should **not** be started with _mpirun_ or _mpiexec_. Use `srun` instead.
    - appropriate software module has to be loaded in the batch job script for the submission to
      work properly.

## Hybrid batch jobs

As explained for [Puhti](../creating-job-scripts-puhti/#hybrid-batch-jobs), hybrid
parallelization can run multiple OpenMP threads per MPI task. In addition to the
`--ntasks-per-node=X` one needs to set `--cpus-per-task=Y`. The default is one cpu
(thread) per task. To use all physical cores in a Mahti node choose `X * Y = 128`,
like in [this example](../example-job-scripts-mahti#mpi-openmp).
If you are using simultaneous multithreading (see section below) your should use `X * Y = 256`

The optimal ratio between the number of tasks and cores per tasks varies for each
program and job input. Testing is required to find the right combination for your
application. You can find some examples for
[cp2k](../../../apps/cp2k/#performance-notes) and
[NAMD](../../../apps/namd/#performance-considerations).

## Hybrid batch jobs with simultaneous multithreading (SMT)

Mahti is configured so that it doesn't place any theads to the logical cores
by default. SMT support can be enabled with `--hint=multithread` option.
When this option is used, it is important to use the `--ntasks-per-node=X` and
`--cpus-per-task=Y` so that `X * Y = 256`. Failing to do so will leave some of the
actual physical cores unallocated and performance will be suboptimal.
[Example batch job script for SMT](../example-job-scripts-mahti#mpi-openmp-with-simultaneous-multithreading).

## Undersubscribing nodes

If an application requires more memory per core than there is available
with full node (2 GB / core) it is possible to use also a subset of
cores within a node. Also, if the application is memory bound, memory
bandwidth and the application performance can be improved by using
only a single core per NUMA domain or L3 cache (look
[Mahti technical description](../systems-mahti.md) for details.
Note that billing is, however, always based
on full nodes.

When undersubscribing nodes, one should always set
`--ntasks-per-node=X` and `--cpus-per-task=Y` so that `X * Y = 128`,
even with pure MPI jobs. By default, Slurm scatters MPI tasks
`--cpus-per-task` apart, i.e. with `--cpus-per-task=8` the MPI task
**0** is bound to CPU core **0**, the MPI task **1** is bound to CPU
core **7** *etc.*. Memory bandwidth (and application performance) is
the best when the tasks are executing on maximally scattered cores. As
an example, in order to use 32 GB / core, one can run only with 8
tasks per node as
```
#SBATCH --ntasks-per-node=8
#SBATCH --cpus-per-task=16

module load myprog/1.2.3
export OMP_NUM_THREADS=1

srun myprog -i input -o output
```

For hybrid applications, one should use 
`OMP_PROC_BIND` OpenMP runtime environment variable for 
placing the OpenMP threads. As an example, in order to run
one MPI task per NUMA domain and one OpenMP thread per L3cache one
can set

```bash
#SBATCH --ntasks-per-node=8
#SBATCH --cpus-per-task=16

export OMP_NUM_THREADS=4
export OMP_PROC_BIND=spread

module load myprog/1.2.3

srun myprog -i input -o output
```

Please check also our [Mahti batch script examples](example-job-scripts-mahti.md) page.

## Using interactive partition for non-parallel pre- or post-processing

In many cases the computing tasks include pre- or post-processing steps that are not able to utilize parallel computing.
In these cases it is recommended that, if possible, the task is split into several, chained, batch jobs and that the non-parallel 
processing is executed in the `interactive` partition of Mahti. 

In the interactive partition the jobs can reserve just few cores so that the non-parallel tasks can be executed without wasting resources.  
Note that you can use interactive partition also for non-interactive jobs and that you can link two batch jobs so that the second job starts 
only when the first one has finished. 

For example, say that we would like to post-process the _output_ file, produced with the very first MPI example job in this page. The post processing command:
`python post-proc.py output` uses only serial computing and requires about 40 minutes and 3 GB of memory. Instead of including the post-processing 
to the main job it is reasonable to execute it as separate job in the interactive partition.

Jobs in interactive partition can reserve 1-8 cores and each core reserves 1,875 GB of memory. Thus in this case we will reserve 2 cores `--cpus-per-task=2` to have enough memory (3,75 GB) available.  Further, `--dependency=afterok:<slurm-jobid>`  defines that the job can start only when the previously sent job has successfully finished. Here the `<slurm-jobid>` is replaced with ID number of the batch job that produces the _output_ file (you'll get the ID number when you submit the job).

```bash
#!/bin/bash
#SBATCH --job-name=post-process-myTest
#SBATCH --account=<project>
#SBATCH --time=00:50:00
#SBATCH --partition=interactive
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=2
#SBATCH --dependency=afterok:<slurm-jobid>

python post-proc.py output
```

## Executing large amounts of small non-MPI jobs

In Mahti, GREASY meta sheduler can be used to process large amounts of small non-MPI jobs.
Please check the GREASY instructon page for more details.
*   [GREASY in Mahti](greasy.md)







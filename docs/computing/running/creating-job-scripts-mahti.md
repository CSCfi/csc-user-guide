# Creating a batch job script for Mahti

Please have a look at the [Puhti documentation](creating-job-scripts-puhti.md)
for the general introduction to batch scripts in the CSC supercomputing
environment. On this page we focus on Mahti-specific topics.

!!! Note
    Full nodes are allocated for jobs, with the exception of
    [interactive jobs](interactive-usage.md#sinteractive-on-mahti),
    [see also below](#using-interactive-partition-for-non-parallel-pre-or-post-processing).
    Many options also work differently on Mahti compared to Puhti, so it is not
    advisable to copy scripts from Puhti to Mahti without appropriate
    modifications.

    Note also that only Mahti GPU nodes have NVMe disk on compute nodes.

[TOC]

## Basic MPI batch jobs

An example of a simple MPI batch job script:

```bash
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

As explained for [Puhti](creating-job-scripts-puhti.md#hybrid-batch-jobs), hybrid
parallelization can run multiple OpenMP threads per MPI task. In addition to the
`--ntasks-per-node=X` one needs to set `--cpus-per-task=Y`. The default is one cpu
(thread) per task. To use all physical cores in a Mahti node choose `X * Y = 128`,
like in [this example](example-job-scripts-mahti.md#mpi-openmp).
If you are using simultaneous multithreading (see section below) your should use `X * Y = 256`

The optimal ratio between the number of tasks and cores per tasks varies for each
program and job input. Testing is required to find the right combination for your
application. You can find some examples for
[CP2K](../../apps/cp2k.md#performance-notes) and
[NAMD](../../apps/namd.md#performance-considerations).

## Hybrid batch jobs with simultaneous multithreading (SMT)

Mahti is configured so that it doesn't place any theads to the logical cores
by default. SMT support can be enabled with `--hint=multithread` option.
When this option is used, it is important to use the `--ntasks-per-node=X` and
`--cpus-per-task=Y` so that `X * Y = 256`. Failing to do so will leave some of the
actual physical cores unallocated and performance will be suboptimal.
[Example batch job script for SMT](example-job-scripts-mahti.md#mpi-openmp-with-simultaneous-multithreading).

## GPU batch jobs

Mahti has 24 GPU nodes and each of them has four Nvidia Ampere A100 GPUs and a local 3.8 TB Nvme drive.
The GPUs are available on the `gputest` ,`gpusmall` and `gpumedium` partitions using the option:

```bash
#SBATCH --gres=gpu:a100:<number_of_gpus_per_node>
```

Mahti's `gpusmall` partition supports only one or two GPU jobs. So the maximum is `--gres=gpu:a100:2`

```bash
#SBATCH --partition=gpusmall
#SBATCH --gres=gpu:a100:1
```

In Mahti's `gpusmall` partition there are also A100 GPUs that have been sliced into smaller a100_1g.5gb GPUs
with one seventh of the compute and memory capacity of a full A100 GPU. For each GPU slice you can reserve
at most 4 CPU cores and for each GPU slice the job is allocated 17.5 GiB of memory. Also note that you can reserve
at most one GPU slice per job. The GPU slices are available on `gpusmall` using the options:

```bash
#SBATCH --partition=gpusmall
#SBATCH --gres=gpu:a100_1g.5gb:1
```

Mahti's `gpumedium` partition supports multi-GPU jobs with four GPUs per compute node.
The example below will allocate four GPUs per compute node, so eight GPUs altogether:

```bash
#SBATCH --nodes=2
#SBATCH --partition=gpumedium
#SBATCH --gres=gpu:a100:4
```

The `gpumedium` is the only gpu partition where more than one compute node is available (maximum number for the `--nodes` flag is six).

The `gputest` partition is for short test runs. Maximum for the `--time` flag is 15 minutes and one job per account can be run in a RUNNING state.
Maximum for the  `--nodes` flag is one but all four GPUs on a node can be allocated for a test job.

In Mahti fast local storage is only available on GPU nodes and it is good for IO intensive applications.
Request local storage using the `--gres` flag in the job submission:

```bash
#SBATCH --gres=nvme:<local_storage_space_per_node>
```

The amount of space is given in GB (with a maximum of 3800 GB per node). For example, to request 100 GB of storage, use option `--gres=nvme:100`. The local storage reservation is on a per node basis. Use the environment variable `$LOCAL_SCRATCH` in your batch job scripts to access the local storage on each node.

Multiple resources can be requested with a comma-separated list.
Request both GPU and local storage:

```bash
#SBATCH --gres=gpu:a100:<number_of_gpus_per_node>,nvme:<local_storage_space_per_node>
```

Many GPU applications also support cpu multithreading but not all. If cpu threading is supported cpu cores for the application threading operations can be enabled using `--cpus-per-task` flag. The example below will use one GPU and 32 cores are available for cpu threading (32 is 1/4 of the CPU cores of a single node) also 950 GB local fast disk storage (1/4 of the total amount of local disk on a node). Ampere A100 GPU also has its own 40GB memory (and that memory will not need any reservation flag). Default amount of main memory allocated per GPU is 122.5GB

```bash
#SBATCH --partition=gpusmall
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=32
#SBATCH --gres=gpu:a100:1,nvme:950

# If multithreading is OpenMP implementation then define also OMP_NUM_THREADS environment variable
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
```

So above example will use 1/4 of all resources on a GPU node and therefore four similar batch jobs could run on a GPU node.

## Undersubscribing nodes

If an application requires more memory per core than there is available
with full node (2 GB / core) it is possible to use also a subset of
cores within a node. Also, if the application is memory bound, memory
bandwidth and the application performance can be improved by using
only a single core per NUMA domain or L3 cache (look at
[Mahti technical description](../systems-mahti.md) for details.
Note that billing is, however, always based on full nodes.

When undersubscribing nodes, one should always set
`--ntasks-per-node=X` and `--cpus-per-task=Y` so that `X * Y = 128`,
even with pure MPI jobs. By default, Slurm scatters MPI tasks
`--cpus-per-task` apart, i.e. with `--cpus-per-task=8` the MPI task
**0** is bound to CPU core **0**, the MPI task **1** is bound to CPU
core **7** _etc._. Memory bandwidth (and application performance) is
the best when the tasks are executing on maximally scattered cores. As
an example, in order to use 32 GB / core, one can run only with 8
tasks per node as

```bash
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

Jobs in interactive partition can reserve 1-8 cores and each core reserves 1.875 GB of memory. Thus in this case we will reserve 2 cores `--cpus-per-task=2` to have enough memory (3,75 GB) available.  Further, `--dependency=afterok:<slurm-jobid>`  defines that the job can start only when the previously sent job has successfully finished. Here the `<slurm-jobid>` is replaced with ID number of the batch job that produces the _output_ file (you'll get the ID number when you submit the job).

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

In Mahti, [HyperQueue](../../apps/hyperqueue.md) meta-scheduler
can be used to process large amounts of small non-MPI jobs.

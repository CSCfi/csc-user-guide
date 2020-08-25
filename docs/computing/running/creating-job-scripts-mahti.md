# Creating a batch job script for Mahti

Please have a look at the [Puhti documentation](creating-job-scripts-puhti.md)
for the general introduction to batch scripts in the CSC supercomputing
environment. The rest of this page focuses on Mahti specific topics.

!!! Note
    Mahti does not have GPUs, NVMe disk on compute nodes or the need
    to reserve memory. Instead, full nodes are allocated for jobs,
    with the exception of interactive jobs (to be added). Many options also work
    differently in Puhti and Mahti, so it is not advisable to copy scripts from Puhti
    to Mahti.
<!-- FIXME interactive jobs -->

!!! Note
    This page is under construction

[TOC]


## Basic MPI batch jobs

An example of a simple MPI-batch job script:
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
    - MPI should **not** be started with _mpirun_ or _mpiexec_, use `srun` instead.
    - An MPI module has to be loaded in the batch job script for the submission to
      work properly.

## Hybrid batch jobs

As explained for [Puhti](../creating-job-scripts-puhti#hybrid-batch-jobs), hybrid
parallelization can run multiple OpenMP threads per MPI task. In addition to the
`--ntasks-per-node=X` one needs to set `--cpus-per-task=Y`. The default is one cpu
(thread) per task. To use all physical cores in a Mahti node choose `X * Y = 128`,
like in [this example](../example-job-scripts-mahti#mpi-openmp).
If you are using hyperthreading (see section below) your should use `X * Y = 256`

The optimal ratio between the number of tasks and cores per tasks varies for each
program and job input. Testing is required to find the right combination for your
application. You can find some examples for
[cp2k](../../../apps/cp2k#performance-notes) and
[NAMD](../../../apps/namd#performance-considerations).

## Hybrid batch jobs with hyperthreading

Mahti is configured so that it doesn't place any theads to the logical cores
by default. Hyperthreading support can be enabled with `--hint=multithread` option.
When this option is used, it is important to use the `--ntasks-per-node=X` and
`--cpus-per-task=Y` so that `X * Y = 256`. Failing to do so will leave some of the
actual physical cores unallocated and performance will be suboptimal.
 Example batch job script can be found
[here](../example-job-scripts-mahti#mpi-openmp-with-hyperthreading).

## Undersubscribing nodes

<!-- FIXME: to be checked with new Slurm config -->
If application requires more memory per core than there is available
with full node (2 GB / core) it is possible to use also a subset of
cores within a node. Also, if application is memory bound, memory
bandwidth and the application performance can be improved by using
only a single core per NUMA domain or L3 cache (see FIXME for details
about Mahti architecture). Note that billing is, however, always based
on full nodes.

When undersubscribing nodes, one should always set
`--ntasks-per-node=X` and `--cpus-per-task=Y` so that `X * Y = 128`,
even with pure MPI jobs. By default, Slurm scatters MPI tasks
`--cpus-per-task` apart, i.e. with `--cpus-per-task=8` the MPI task
**0** is bind to CPU core **0**, the MPI task **1** is bind to CPU
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

For hybrid applications, one should use `OMP_PLACES` and
`OMP_PROC_BIND` OpenMP runtime environment variables for obtaining
optimum placemenet of OpenMP threads. As an example, in order to run
one MPI tasks per NUMA domain and one OpenMP thread per L3cache one
can set

```bash
#SBATCH --ntasks-per-node=8
#SBATCH --cpus-per-task=16

export OMP_NUM_THREADS=4
export OMP_PLACES=cores
export OMP_PROC_BIND=spread

module load myprog/1.2.3

srun myprog -i input -o output
```

Please check also our [Mahti batch script examples](example-job-scripts-mahti.md) page.
---
tags:
  - Free
---

# HyperQueue

!!! warning "Autoallocation"
    The autoallocation feature available in HQ is still under development and buggy, don't use it
    as it's very likely that the job queue will be filled with idling workers which just waste
    resources.

!!! info "sbatch-hq"
    For simple task farming workflows, where the intention is to run many similar (non-MPI parallel,
    independent) commands/programs, you can use the CSC utility tool `sbatch-hq` to avoid writing
    a batch script for HyperQueue from scratch. [See below for details and an example](#sbatch-hq).

HyperQueue (HQ) is an efficient sub-node task scheduler. Instead of submitting each one of
your computational tasks using `sbatch` or `srun` you can just allocate a large resource block
and then use HyperQueue to submit your tasks. This will be much less stressful for the batch queue
system and is therefore the recommended way to run your high-throughput computing use cases.

## License

Free to use and open source under [MIT License](https://github.com/It4innovations/hyperqueue/blob/main/LICENSE)

## Available

* Puhti: 0.11.0, 0.13.0
* Mahti: 0.11-dev, 0.13.0

## Usage

```bash
module load hyperqueue
```

HyperQueue works on a worker-server-client basis. Here, the server manages connections, workers are
started on compute nodes and execute commands which the client submitted to the server. This
resembles a Slurm within a Slurm, but you have to start the server and workers yourself.

### Starting the server

!!! info "Note"
    The following instructions apply for Slurm job scripts where only full nodes
    are allocated. [A full example](#full-example) (for Puhti) can be found at the bottom.

Specify where on the file system the HyperQueue server should be placed. All `hq` commands
respect this variable so make sure it's set before you call any `hq` commands. The server
location can also be placed using the command line flag `--server-dir /server/location/on/lustre`.

```bash
export HQ_SERVER_DIR=/server/location/on/lustre
```

If the server directory is not specified it will default to the user home directory. In this case
one has to be careful not to mix up separate computations. For simple cases that fit inside one
Slurm job, we recommend starting one server per job in some job-specific directory.

Start the server:

```bash
hq server start &
until hq job list &>/dev/null ; do sleep 1 ; done
```

Here, the server is placed in the background (`&`) so that we can continue.

### Starting the workers

Start the workers (again in the background so our script can continue):

```bash
srun --exact --cpu-bind=none --mpi=none hq worker start --cpus=${SLURM_CPUS_PER_TASK} &
```

Here, we launch one worker per node with each worker getting the full node. If you need HQ
to be aware of other resources, e.g memory, local disk or GPUS, see the [Generic resource
section](https://it4innovations.github.io/hyperqueue/v0.11.0/jobs/gresources/) in the
official documentation.

Next, we can start submitting jobs or alternatively wait for all the workers to connect
to the server before submission. This is generally good practice as we can notice issues with
the workers early.

Wait until all workers are online (note no timeout):

```bash
hq worker wait "${SLURM_NTASKS}"
```

### Submitting jobs

!!!info "Output"
    By default HQ creates one folder for each job where output is redirected.
    You can use the `--log`, `--stdout` and `--stderr` flags to change this behavior.
    Note that it's not possible to direct output from multiple jobs into the same file
    as each submission will clear the file.

See `hq submit --help` for the full list of options.

```bash
hq submit <hq submit args> --cpus <n> <COMMAND/executable> <args to program>
```

This is a non-blocking command similar to `sbatch`.

HyperQueue is not limited to running a single execution per submission. Using the
`--array 1-N` flag we can start a program *N* times similar to how Slurm array jobs work.

```bash
hq submit --array 1-10 --cpus <n> <COMMAND>
```

`<COMMAND>` then has access to the environment variable `HQ_TASK_ID` which is used
to enumerate all the tasks.

When we have submitted everything we want, we need to wait for the jobs to finish.
This can be done e.g. with:

```bash
hq job wait all
```

Once we are done running all of our jobs, we shutdown the workers and server to avoid a false
error from Slurm when the job ends:

```bash
hq worker stop all
hq server stop
```

#### sbatch-hq

For simple task farming workflows, where you only want to run many similar (non-MPI parallel,
independent) commands/programs, you can use the CSC utility tool `sbatch-hq`. Just specify the
list of commands to run in a file, one command per line. The tool `sbatch-hq` will create and
launch a batch job that starts running commands from the file using HyperQueue. You can specify
how many nodes you want to run the commands on and `sbatch-hq` will keep executing the commands
until all are done, or the batch job time limit is reached.

!!! info "Note"
    Do not include `srun` in the commands you want to run. HyperQueue will take care of
    launching the tasks using the allocated resources as requested.

Let's assume we are working on Mahti and we have a file named `commandlist` with a list of commands
that we want to run using 16 threads each. As an example, let's reserve 2 nodes so that we can run
16 tasks simultaneously:

```bash
module load sbatch-hq
sbatch-hq --cores=16 --nodes=2 --account=<project> --partition=medium --time=02:00:00 commandlist
```

The number of commands in the file can (usually should) be much larger than the number of commands
that can fit running simultaneously in the reserved nodes. See `sbatch-hq --help` for more details
on usage and input options.

### Full example

```bash
#!/bin/bash
#SBATCH --partition=small
#SBATCH --account=<project>
#SBATCH --nodes=1
#SBATCH --cpus-per-task=40
#SBATCH --ntasks-per-node=1
#SBATCH --time=00:30:00

module load hyperqueue

# Specify a location for the HyperQueue server
export HQ_SERVER_DIR=${PWD}/hq-server-${SLURM_JOB_ID}
mkdir -p "${HQ_SERVER_DIR}"

# Start the server in the background (&) and wait until it has started
hq server start &
until hq job list &>/dev/null ; do sleep 1 ; done

# Start the workers (one per node, in the background) and wait until they have started
srun --exact --cpu-bind=none --mpi=none hq worker start --cpus=${SLURM_CPUS_PER_TASK} &
hq worker wait "${SLURM_NTASKS}"

# Simple example workflow. Compute the checksums of all files in the current
# directory. For small files you would do this very simply in a single
# interactive compute node, right ;)
#
#     sha256sum $(find . -maxdepth 1 -type f) > checksums.txt
#
# Parallelized with HyperQueue (not restricted to a single node):

for f in $(find . -maxdepth 1 -type f) ; do
    hq submit --stdout $f.sha256 sha256sum $f
done

# Wait until all jobs have finished, shut down the HyperQueue workers and server
hq job wait all
hq worker stop all
hq server stop
```

### With other workflow managers

If your workflow manager is using `sbatch` for each process execution and you have many short
processes it's advisable to switch to HyperQueue to improve throughput and decrease load on
the system batch scheduler.

#### Snakemake

Using Snakemake's `--cluster` flag we can use `hq submit` instead of `sbatch`:

```bash
snakemake --cluster "hq submit --cpus <threads> ..."
```

If you are porting a more complicated workflow from Slurm, you can do
argument parsing and transformations programmatically using Snakemake's [job
properties](https://snakemake.readthedocs.io/en/stable/executing/cluster.html#job-properties)

#### Nextflow

See a [separate tutorial](../support/tutorials/nextflow-hq.md) for instructions on
how to use HyperQueue as an executor for Nextflow workflows.

## More information

!!!info "MPI"
    Although HyperQueue does not do MPI execution out of the box, it's possible
    using a combination of the HQ feature [Multinode
    Tasks](https://it4innovations.github.io/hyperqueue/stable/jobs/multinode/)
    and `orterun`, `hydra` or `prrte`. This way one can schedule MPI tasks at a
    node-level granularity.

* [Full documentation for HQ](https://it4innovations.github.io/hyperqueue/v0.11.0/)
* [Using HyperQueue and local disk to process many files](https://csc-training.github.io/csc-env-eff/hands-on/throughput/hyperqueue.html)
* [Farming Gaussian jobs with sbatch-hq](https://csc-training.github.io/csc-env-eff/hands-on/throughput/gaussian_hq.html)

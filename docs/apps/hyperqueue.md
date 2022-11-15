---
tags:
  - Free
---

# HyperQueue

!!!warning "Autoallocation"
    The autoallocation feature available in HQ is still under development and buggy, don't use it
    as it's very likely that the job queue will be filled with idling workers which just waste
    resources.

HyperQueue (HQ) is a tool for efficient sub-node task scheduling. Instead of submitting each one of
your computational tasks using `sbatch` or `srun` you can instead allocate a large resource block
and then use HyperQueue to submit your tasks. This will be much less stressful for the batch queue
system and is therefore the recommended way to run your high-throughput computing use cases.

## License

Free to use and open source under [MIT License](https://github.com/It4innovations/hyperqueue/blob/main/LICENSE)

## Available

* Puhti: 0.11.0
* Mahti: 0.11-dev

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
    are allocated. [A full example](#full-example) (for Mahti) can be found at the bottom.

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
until hq jobs ; do sleep 1 ; done
```

Here, the server is placed in the background (`&`) so that we can continue.

### Starting the workers

Start the workers (again in the background so our script can continue):

```bash
srun --cpu-bind=none --hint=nomultithread --mpi=none --ntasks-per-node=$SLURM_NNODES -c $SLURM_CPUS_PER_TASK hq worker start --cpus=$SLURM_CPUS_PER_TASK &
```

Here, we launch one worker per node with each worker getting the full node. If you need HQ
to be aware of other resources, e.g memory, local disk or GPUS, see the [Generic resource
section](https://it4innovations.github.io/hyperqueue/v0.11.0/jobs/gresources/) in the
official documentation.

Next, we can start submitting jobs or alternatively wait for all the workers to connect
to the server before submission. This is generally good practice as we can notice issues with
the workers early.

Loop until all workers are online (note no timeout):

```bash
echo "Checking if workers have started"
until [[ $num_up -eq $SLURM_NNODES ]]; do
    num_up=$(hq worker list | grep -c RUNNING)
    echo "$num_up/$SLURM_NNODES workers have started"
    sleep 1
done
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

!!! info "sbatch-hq"
    For very simple submissions where you only want to run each line within a file with
    identical resources (task farming) you can just use the CSC utility tool `sbatch-hq`.
    This way you do not have to care about HyperQueue. Run `module load sbatch-hq` to load
    the wrapper (only available on Mahti).

When we have submitted everything we want, we need to wait for the jobs to finish.
This can be done e.g. with:

```bash
while hq job list --all | grep -q "RUNNING\|PENDING"; do
    echo "WAITING FOR JOBS TO FINISH"
    sleep 30
done
```

Once we are done running all of our jobs, we shutdown the workers and server to avoid a false
error from Slurm when the job ends:

```bash
hq worker stop all
hq server stop
```

### Full example

```bash
#!/bin/bash
#SBATCH --partition=medium
#SBATCH --account=<project>
#SBATCH --nodes=4
#SBATCH --cpus-per-task=128
#SBATCH --ntasks-per-node=1
#SBATCH --time=01:00:00

export SLURM_EXACT=1

# Load the required modules
module load hyperqueue

# Set the directory which hyperqueue will use
export HQ_SERVER_DIR=$PWD/hq-server-$SLURM_JOB_ID
mkdir -p "$HQ_SERVER_DIR"

echo "STARTING HQ SERVER, log in $HQ_SERVER_DIR/HQ.log"
echo "===================="
hq server start &>> "$HQ_SERVER_DIR/HQ.log" &
until hq job list &>/dev/null ; do sleep 1 ; done

echo "STARTING HQ WORKERS ON $SLURM_NNODES nodes"
echo "===================="
srun --cpu-bind=none --mpi=none hq worker start --cpus=$SLURM_CPUS_PER_TASK &>> "$HQ_SERVER_DIR/HQ.log" &

until [[ $num_up -eq $SLURM_NNODES ]]; do
    num_up=$(hq worker list 2>/dev/null | grep -c RUNNING )
    echo "WAITING FOR WORKERS TO START ( $num_up / $SLURM_NNODES )"
    sleep 1
done

## Here you run your submit commands, workflow managers etc...
## hq submit <hq submit args> --cpus <n> <COMMAND/executable> <args to program>
## ...

while hq job list --all | grep -q "RUNNING\|PENDING"; do
    echo "WAITING FOR JOBS TO FINISH"
    # Adjust the timing here if you get to much output in the Slurm log file
    # Now set to 30 seconds
    sleep 30
done

echo "===================="
echo "DONE"
echo "===================="
echo "SHUTTING DOWN HYPERQUEUE"
echo "===================="
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
* [Farming Gaussian jobs with HyperQueue](https://csc-training.github.io/csc-env-eff/hands-on/throughput/gaussian_hq.html)

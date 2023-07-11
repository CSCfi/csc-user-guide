---
tags:
  - Free
---

# HyperQueue
[HyperQueue (HQ)](https://it4innovations.github.io/hyperqueue/stable/) is an efficient sub-node task scheduler. Instead of submitting each one of
your computational tasks using `sbatch` or `srun` you can just allocate a large resource block
and then use HyperQueue to submit your tasks. This will be much less stressful for the batch queue
system and is therefore the recommended way to run your high-throughput computing use cases.

!!! warning "Autoallocation"
    The autoallocation feature available in HQ is still under development and buggy, don't use it
    as it's very likely that the job queue will be filled with idling workers which just waste
    resources.

!!! info "sbatch-hq"
    For simple task farming workflows, where the intention is to run many similar (non-MPI parallel,
    independent) commands/programs, you can use the CSC utility tool `sbatch-hq` to avoid writing
    a batch script for HyperQueue from scratch. [See below for details and an example](#sbatch-hq).

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
Specify where on the file system the HyperQueue server should be placed. All `hq` commands
respect this variable so make sure it's set before you call any `hq` commands. The server
location can also be placed using the command line flag `--server-dir "$PWD/.hq-server"`.

```bash
export HQ_SERVER_DIR="$PWD/.hq-server"
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

Let's assume we have a file named `commandlist` with a list of commands that we want to
run using 8 threads each. As an example, let's reserve 1 compute node for the whole job.
This means that we could run either 5 or 16 tasks simultaneously depending on whether we
are using Puhti or Mahti.

```bash
module load sbatch-hq
sbatch-hq --cores=8 --nodes=1 --account=<project> --partition=test --time=00:15:00 commandlist
```

The number of commands in the file can (usually should) be much larger than the number of commands
that can fit running simultaneously in the reserved nodes. See `sbatch-hq --help` for more details
on usage and input options.


### Creating a batch job
You can copy the following example and run it as given and then modify it to suit your needs.

Directory structure

```text
.             # Current working directory
├── batch.sh  # Batch script for HyperQueue server and workers
└── task      # Executable task script for HyperQueue
```

We assume that HyperQueue tasks are independent and run on a single node.
Example of a simple, executable `task` script.

```bash
#!/bin/bash
echo "$HQ_TASK_ID"
sleep 1
```

In a Slurm batch job each Slurm task correspond to one HyperQueue worker.
We can increase the amount of workers by increasing the number of Slurm tasks.
In a partial node allocation we reserve a fraction of the CPUs and memory on a node per worker.
In a full node allocation we reserve all the CPUs and memory on a node per worker.
Example of a `batch.sh` script that starts the server and workers, and then submits tasks.

=== "Puhti partial single node"
    ```bash
    #!/bin/bash
    #SBATCH --partition=small    # single node partition
    #SBATCH --ntasks=1           # one HyperQueue worker
    #SBATCH --cpus-per-task=10   # one or more cpus per worker
    #SBATCH --mem-per-cpu=1000   # desired amount of memory
    #SBATCH --time=00:15:00
    ```

=== "Puhti partial multinode"
    ```bash
    #!/bin/bash
    #SBATCH --partition=large    # multi node partition
    #SBATCH --ntasks=2           # two or more HyperQueue workers
    #SBATCH --cpus-per-task=10   # one or more cpus per worker
    #SBATCH --mem-per-cpu=1000   # desired amount of memory
    #SBATCH --time=00:15:00
    ```

=== "Puhti full single node"
    ```bash
    #!/bin/bash
    #SBATCH --partition=small
    #SBATCH --ntasks=1           # one worker node
    #SBATCH --cpus-per-task=40   # all cpus on a node
    #SBATCH --mem-per-cpu=0      # reserve all memory on a node
    #SBATCH --time=00:15:00
    ```

=== "Puhti full multinode"
    ```bash
    #!/bin/bash
    #SBATCH --partition=large
    #SBATCH --ntasks=2           # two or more worker nodes
    #SBATCH --cpus-per-task=40   # reserve all cpus on a node
    #SBATCH --mem-per-cpu=0      # reserve all memory on a node
    #SBATCH --time=00:15:00
    ```

=== "Mahti full node"
    ```bash
    #!/bin/bash
    #SBATCH --partition=medium
    #SBATCH --ntasks=1           # one or more worker nodes
    #SBATCH --cpus-per-task=128  # all cpus on a node
    #SBATCH --mem-per-cpu=0      # reserve all memory on a node
    #SBATCH --time=00:15:00
    ```

```bash
# Load dependencies
module load hyperqueue

# Specify a location for the server
export HQ_SERVER_DIR="$PWD/.hq-server/$SLURM_JOB_ID"

# Create a directory for the server
mkdir -p "$HQ_SERVER_DIR"

# Start the server in the background
hq server start &

# Wait until the server has started
until hq job list &> /dev/null ; do sleep 1 ; done

# Set memory for workers in bytes according to SLURM_MEM_PER_CPU if greater than zero.
# Otherwise, leave unset which uses all the memory of the node.
if [[ "${SLURM_MEM_PER_CPU:-0}" -gt 0 ]]; then
    # Calculate the total memory reservation and convert from megabytes to bytes.
    TOTAL_MEM_BYTES=$((SLURM_CPUS_PER_TASK * SLURM_MEM_PER_CPU * 1000000))
    TOTAL_MEM_OPT="--resource mem=sum($TOTAL_MEM_BYTES)"
else
    TOTAL_MEM_OPT=""
fi

# Start the workers in the background
srun --overlap --cpu-bind=none --mpi=none hq worker start \
    --manager slurm \
    --idle-timeout 5m \
    --on-server-lost finish-running \
    --cpus="$SLURM_CPUS_PER_TASK" \
    $TOTAL_MEM_OPT &

# Wait until all workers have started
hq worker wait "$SLURM_NTASKS"

# Submit tasks to workers
NUM_TASKS=1000
for ((i=1; i<=NUM_TASKS; i++)); do
    hq submit --stdout=none --stderr=none --cpus=1 ./task
done

# Wait for all the tasks to finish
hq job wait all

# Shut down the workers and server
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

---
tags:
  - Free
---

# HyperQueue

[HyperQueue (HQ)](https://github.com/It4innovations/hyperqueue) is an efficient sub-node
task scheduler. Instead of submitting each of your computational tasks as separate Slurm
jobs or job steps, you can allocate a large resource block and then use HyperQueue to
submit your tasks to this allocation. A single resource allocation will be much less
stressful for the batch queue system and is the recommended way to run your high-throughput
computing use cases. Furthermore, we can use HyperQueue instead of Slurm as the task
executor for other workflow managers, such as Snakemake and Nextflow.

## License

Free to use and open source under [MIT License](https://github.com/It4innovations/hyperqueue/blob/main/LICENSE)

## Available

* Puhti: 0.13.0, 0.15.0, 0.16.0
* Mahti: 0.13.0, 0.15.0, 0.16.0
* LUMI: 0.18.0

## Usage

Initialize the recommended version of HyperQueue on Puhti and Mahti like this:

```bash
module load hyperqueue
```

Use `module spider` to locate other versions. 
To access CSC's HyperQueue modules on LUMI,
remember to first run `module use /appl/local/csc/modulefiles`.

```bash
module use /appl/local/csc/modulefiles
module load hyperqueue
```

### Task-farming with sbatch-hq tool

For simple task-farming workflows, where you only want to run many similar, independent,
and non-MPI parallel programs, you can use the CSC utility tool `sbatch-hq`.
Just specify the list of commands to run in a file, one command per line.
The tool `sbatch-hq` will create and launch a batch job that starts running
commands from the file using HyperQueue. You can specify how many nodes you
want to run the commands on, and `sbatch-hq` will keep executing the commands
until all are done or the batch job time limit is reached.

Let's assume we have a `tasks` file with a list of commands we want to run using
eight threads each. **Do not use `srun` in the commands!** HyperQueue will launch
the tasks using the allocated resources as requested. For example, 

```text
command1 arguments1
command2 arguments2
# and so on
```

For example, let's reserve one compute node for the whole job, which means we could
run either five tasks simultaneously using Puhti or 16 tasks simultaneously using Mahti.

```bash
module load sbatch-hq
sbatch-hq --cores=8 --nodes=1 --account=<project> --partition=test --time=00:15:00 tasks
```

The number of commands in the file can (usually should) be much larger than the number of
tasks that can fit running simultaneously in the reserved nodes. See `sbatch-hq --help`
for more details on usage and input options.

### Using HyperQueue in a Slurm batch job

HyperQueue works on a worker-server-client basis. The server manages connections
between workers and the client. The client submits tasks to the server, which sends
them to the available workers. The client and server may run on login or compute nodes,
and the workers run on compute nodes. HyperQueue resembles a Slurm within a Slurm,
but you must start the server and workers yourself. We recommend reading the official
[HyperQueue documentation](https://it4innovations.github.io/hyperqueue/stable/).

This example consists of a batch script and an executable task script. The batch
script starts the HyperQueue server and workers and submits tasks to the workers.
The task script is an executable script that we submit to the workers. You can copy
the following example, run it as given, and modify it to suit your needs. The
directory structure looks as follows:

```text
.             # Current working directory
├── batch.sh  # Batch script for HyperQueue server and workers
└── task      # Executable task script for HyperQueue
```

**Task**

We assume that HyperQueue tasks are independent and run on a single node.
Here is an example of a simple, executable `task` script written in Bash.

```bash
#!/bin/bash
sleep 1
```

The overhead per task is around 0.1 milliseconds.
Therefore, we can efficiently execute even very small tasks.

**Batch job**

In a Slurm batch job, each Slurm task corresponds to one HyperQueue worker.
We can increase the number of workers by increasing the number of Slurm tasks.
We reserve a fraction of the CPUs and memory on a node per worker in a partial
node allocation and all the CPUs and memory on a node per worker in a full node
allocation.

=== "Puhti partial single node"
    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=small    # single node partition
    #SBATCH --nodes=1            # one compute node
    #SBATCH --ntasks-per-node=1  # one HyperQueue worker
    #SBATCH --cpus-per-task=10   # one or more cpus per worker
    #SBATCH --mem-per-cpu=1000   # desired amount of memory per cpu
    #SBATCH --time=00:15:00
    ```

=== "Puhti partial multinode"
    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=large    # multi node partition
    #SBATCH --nodes=2            # two or more nodes
    #SBATCH --ntasks-per-node=1  # one HyperQueue worker per node
    #SBATCH --cpus-per-task=10   # one or more cpus per worker
    #SBATCH --mem-per-cpu=1000   # desired amount of memory per cpu
    #SBATCH --time=00:15:00
    ```

=== "Puhti full single node"
    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=small    # single node partition
    #SBATCH --nodes=1            # one compute node
    #SBATCH --ntasks-per-node=1  # one HyperQueue worker
    #SBATCH --cpus-per-task=40   # all cpus on a node
    #SBATCH --mem=0              # reserve all memory on a node
    #SBATCH --time=00:15:00
    ```

=== "Puhti full multinode"
    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=large    # multi node partition
    #SBATCH --nodes=2            # two or more nodes
    #SBATCH --ntasks-per-node=1  # one HyperQueue worker per node
    #SBATCH --cpus-per-task=40   # reserve all cpus on a node
    #SBATCH --mem=0              # reserve all memory on a node
    #SBATCH --time=00:15:00
    ```

=== "Mahti full node"
    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=medium   # multi node partition
    #SBATCH --nodes=1            # one or more nodes
    #SBATCH --ntasks-per-node=1  # one HyperQueue worker per node
    #SBATCH --cpus-per-task=128  # all cpus on a node
    #SBATCH --mem=0              # reserve all memory on a node
    #SBATCH --time=00:15:00
    ```

**Module**

We load the HyperQueue module to make the `hq` command available.

```bash
module load hyperqueue
```

**Server**

Next, we specify where HyperQueue places the server files.
All `hq` commands respect this variable, so we set it before using any `hq` commands.
If a server directory is not specified, it will default to the user's home directory.
In this case, one has to be careful not to mix up separate computations as well as
mind the limited storage space available under `$HOME`. We recommend starting one
server per job in a job-specific directory for simple cases that fit inside one
Slurm job.

```bash
# Specify a location for the server
export HQ_SERVER_DIR="$PWD/hq-server/$SLURM_JOB_ID"

# Create a directory for the server
mkdir -p "$HQ_SERVER_DIR"
```

Now, we start the server in the background and wait for it to start. The server
keeps running until we stop it; therefore, we place it in the background so it
does not block the execution of the rest of the script.

```bash
# Start the server in the background
hq server start &

# Wait until the server has started
until hq job list &> /dev/null ; do sleep 1 ; done
```

**Workers**

</--
Next, we start HyperQueue workers in the background with the number of CPUs and the amount
of memory defined in the batch script. We access those values using the `SLURM_CPU_PER_TASK`
and `SLURM_MEM_PER_CPU` environment variables. By starting the workers using the `srun`
command, we create one worker per Slurm task. We also wait for all workers to connect,
which is generally good practice as we can notice issues with the workers early.

```bash
# Set memory for workers in bytes according to SLURM_MEM_PER_CPU if greater than zero.
# Otherwise, leave unset to use all the memory of the node.
if [[ "${SLURM_MEM_PER_CPU:-0}" -gt 0 ]]; then
    # Calculate the total memory reservation and convert it from megabytes to bytes.
    TOTAL_MEM_BYTES=$((SLURM_CPUS_PER_TASK * SLURM_MEM_PER_CPU * 1000000))
    TOTAL_MEM_OPT="--resource mem=sum($TOTAL_MEM_BYTES)"
else
    TOTAL_MEM_OPT=""
fi

# Start the workers in the background.
srun --overlap --cpu-bind=none --mpi=none hq worker start \
    --manager slurm \
    --on-server-lost finish-running \
    --cpus="$SLURM_CPUS_PER_TASK" \
    $TOTAL_MEM_OPT &

# Wait until all workers have started
hq worker wait "$SLURM_NTASKS"
```
-->

Next, we start HyperQueue workers in the background with the number of CPUs defined
in the batch script using the `$SLURM_CPUS_PER_TASK` environment variable. By starting
the workers using the `srun` command, we create one worker per Slurm task. We also
wait for all workers to connect, which is generally good practice as we can notice
issues with the workers early.

```bash
# Start the workers in the background.
srun --overlap --cpu-bind=none --mpi=none hq worker start \
    --manager slurm \
    --on-server-lost finish-running \
    --cpus="$SLURM_CPUS_PER_TASK" &

# Wait until all workers have started
hq worker wait "$SLURM_NTASKS"
```

**Computing tasks**

Now we can submit tasks with `hq submit` to the server, which executes them on the
available workers. It is a non-blocking command; thus, we do not need to run it in
the background. Regarding file I/O, we turn off output by setting `--stdout=none`
and `--stderr=none`. Otherwise, HyperQueue will create output files for each task,
which can create excess I/O on the parallel filesystem when there are many tasks.
After submitting all the tasks, we wait for them to complete to synchronize the script.

```bash
# Submit tasks to workers
hq submit --stdout=none --stderr=none --cpus=1 --array=1-1000 ./task

# Wait for all the tasks to finish
hq job wait all
```

It is worth reading the sections about
[Jobs and Tasks](https://it4innovations.github.io/hyperqueue/stable/jobs/jobs/)
and [Task Arrays](https://it4innovations.github.io/hyperqueue/stable/jobs/arrays/)
to understand the different ways to run computations with HyperQueue. For more
complex task dependencies, we can use HyperQueue as the executor for other workflow
managers, such as [Snakemake](#using-snakemake-with-hyperqueue) or
[Nextflow](#using-nextflow-with-hyperqueue).

**Stopping the workers and the server**

Once we are done running all of our tasks, we shut down the workers and server to
avoid a false error from Slurm when the job ends.

```bash
# Shut down the workers and server
hq worker stop all
hq server stop
```

### Using local disks with HyperQueue

We can use [temporary local disk areas](../computing/disk.md#temporary-local-disk-areas)
with HyperQueue to perform I/O intensive tasks. Since a HyperQueue task can run on any
allocated node, the local disk of each node must have a copy of all the files that the
task may use. A typical workflow consists of

1. Copying and extracting archived input files from the parallel file system to
   the local disk.
2. Computing the HyperQueue tasks (`hq submit`) that use the local disk.
3. Archiving and copying the output files from the local disk to the parallel file
   system.

For steps 1 and 3, we can run an `<executable>` on each allocated node as a Slurm
job step as follows:

```bash
srun -m arbitrary -w "$SLURM_JOB_NODELIST" <executable>
```

Without the options, `srun` would run the executable on every Slurm task, which
could be on the same node. The `srun` command can be omitted if only a single node
is requested.

### Complete example scripts for Puhti

=== "Single node"

    File: `task`

    ```bash
    #!/bin/bash
    echo "Hello from task $HQ_TASK_ID!" > "output/$HQ_TASK_ID.out"
    sleep 1
    ```

    File: `batch.sh`

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=small
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=10
    #SBATCH --mem-per-cpu=1000
    #SBATCH --time=00:15:00

    module load hyperqueue

    # Specify a location and create a directory for the server
    export HQ_SERVER_DIR="$PWD/hq-server/$SLURM_JOB_ID"
    mkdir -p "$HQ_SERVER_DIR"

    # Start the server in the background and wait until it has started
    hq server start &
    until hq job list &> /dev/null ; do sleep 1 ; done

    # Start the workers in the background
    srun --overlap --cpu-bind=none --mpi=none hq worker start \
        --manager slurm \
        --on-server-lost finish-running \
        --cpus="$SLURM_CPUS_PER_TASK" &

    # Wait until all workers have started
    hq worker wait "$SLURM_NTASKS"

    # Create a directory for output files
    mkdir -p output

    # Submit tasks to workers
    hq submit --stdout=none --stderr=none --cpus=1 --array=1-1000 ./task

    # Wait for all tasks to finish
    hq job wait all

    # Shut down the workers and server
    hq worker stop all
    hq server stop
    ```

=== "Multinode + local disk"

    The archive `input.tar.gz` used in this example extracts into `input` directory.

    File: `extract`

    ```bash
    #!/bin/bash
    tar xf input.tar.gz -C "$LOCAL_SCRATCH"
    mkdir -p "$LOCAL_SCRATCH/output"
    ```

    File: `task`

    ```bash
    #!/bin/bash
    cd "$LOCAL_SCRATCH"
    cat "input/$HQ_TASK_ID.inp" > "output/$HQ_TASK_ID.out"
    sleep 1
    ```

    File: `archive`

    ```bash
    #!/bin/bash
    cd "$LOCAL_SCRATCH"
    tar czf "output-$SLURMD_NODENAME.tar.gz" output
    cp "output-$SLURMD_NODENAME.tar.gz" "$SLURM_SUBMIT_DIR"
    ```

    File: `batch.sh`

    ```bash
    #!/bin/bash
    #SBATCH --account=<project>
    #SBATCH --partition=large
    #SBATCH --nodes=2
    #SBATCH --ntasks-per-node=1
    #SBATCH --cpus-per-task=40
    #SBATCH --mem=0
    #SBATCH --time=00:15:00
    #SBATCH --gres=nvme:1

    module load hyperqueue

    # Specify a location and create a directory for the server
    export HQ_SERVER_DIR="$PWD/hq-server/$SLURM_JOB_ID"
    mkdir -p "$HQ_SERVER_DIR"

    # Start the server in the background and wait until it has started
    hq server start &
    until hq job list &> /dev/null ; do sleep 1 ; done

    # Start the workers in the background
    srun --overlap --cpu-bind=none --mpi=none hq worker start \
        --manager slurm \
        --on-server-lost finish-running \
        --cpus="$SLURM_CPUS_PER_TASK" &

    # Wait until all workers have started
    hq worker wait "$SLURM_NTASKS"

    # Download some example input files
    wget https://a3s.fi/CSC_training/input.tar.gz

    # Extract input files to the local disk and create a directory for outputs
    srun -m arbitrary -w "$SLURM_JOB_NODELIST" ./extract

    # Submit tasks to workers
    hq submit --stdout=none --stderr=none --cpus=1 --array=1-1000 ./task

    # Wait for all tasks to finish
    hq job wait all

    # Archive and copy output from each local disk to working directory on Lustre
    srun -m arbitrary -w "$SLURM_JOB_NODELIST" ./archive

    # Shut down the workers and server
    hq worker stop all
    hq server stop
    ```

### Using Snakemake with HyperQueue

Using Snakemake's `--cluster` flag, we can use `hq submit` instead of `sbatch`:

```bash
snakemake --cluster "hq submit --cpus <threads> ..."
```

If you are porting a more complicated workflow from Slurm, you can do argument
parsing and transformations programmatically using Snakemake's
[job properties](https://snakemake.readthedocs.io/en/stable/snakefiles/rules.html#job-properties).

### Using Nextflow with HyperQueue

See a [separate tutorial](../support/tutorials/nextflow-hq.md) for instructions on
using HyperQueue as an executor for Nextflow workflows.

### Multinode tasks

Although HyperQueue does not do MPI execution out of the box, it's possible
using a combination of the HQ feature
[Multinode Tasks](https://it4innovations.github.io/hyperqueue/stable/jobs/multinode/)
and `orterun`, `hydra` or `prrte`. This way, one can schedule MPI tasks at a node-level
granularity.

### Automatic worker allocation

We recommend avoiding using the automatic allocator. It automatically generates
and submits batch scripts to start workers, which adds unnecessary complexity.
Also, the automatically generated batch scripts have some issues and could be more
flexible.

## More information

* [Using HyperQueue and local disk to process many files](https://csc-training.github.io/csc-env-eff/hands-on/throughput/hyperqueue.html)
* [Farming Gaussian jobs with sbatch-hq](https://csc-training.github.io/csc-env-eff/hands-on/throughput/gaussian_hq.html)

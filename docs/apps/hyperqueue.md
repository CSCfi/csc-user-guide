---
tags:
  - Free
catalog:
  name: HyperQueue
  description: Scheduler for sub-node tasks
  license_type: Free
  disciplines:
    - Miscellaneous
  available_on:
    - LUMI
    - Roihu
---

# HyperQueue

[HyperQueue (HQ)](https://github.com/It4innovations/hyperqueue) is an efficient sub-node
task scheduler. Instead of submitting each of your computational tasks as separate Slurm
jobs or job steps, you can allocate a large resource block and then use HyperQueue to
submit your tasks to this allocation. A single resource allocation will be much less
stressful for the batch queue system and is the recommended way to run your high-throughput
computing use cases. HyperQueue can also act as the task executor for workflow managers
such as [Snakemake or Nextflow](#using-snakemake-or-nextflow-with-hyperqueue).

## Available

* Roihu-CPU: 0.25.1
* Roihu-GPU: 0.25.1
* LUMI: 0.18.0

## License

Free to use and open source under [MIT License](https://github.com/It4innovations/hyperqueue/blob/main/LICENSE)

## Usage

### Loading the module

Load the default version of HyperQueue on **Roihu-CPU** or **Roihu-GPU** like this:

```bash
module load hyperqueue
```

To access CSC's HyperQueue modules on **LUMI**, you first need to make the CSC modules available:

```bash
module use /appl/local/csc/modulefiles
module load hyperqueue
```

### Task farming with sbatch-hq

For simple task-farming workflows, where you only want to run many similar, independent,
and non-MPI parallel programs, you can use the CSC utility tool `sbatch-hq`. It creates
and launches a batch job that runs your commands using HyperQueue, executing them until
all are done or the batch job time limit is reached.

Specify the list of commands to run in a file, one command per line. **Do not use `srun`
in the commands!** HyperQueue launches the tasks using the allocated resources as
requested. For example, a `tasks` file might contain:

```text
command1 arguments1
command2 arguments2
# and so on
```

Then submit the tasks, reserving for example eight cores on a single node:

```bash
module load sbatch-hq
sbatch-hq --cores=8 --nodes=1 --account=<project> --partition=test --time=00:15:00 tasks
```

The number of commands in the file can (usually should) be much larger than the number of
tasks that can fit running simultaneously in the reserved nodes. See `sbatch-hq --help`
for more details on usage and input options.

### Running HyperQueue in a Slurm batch job

For more control than `sbatch-hq` offers, you can drive HyperQueue yourself from a Slurm
batch job.

HyperQueue works on a worker-server-client basis. The server manages connections
between workers and the client. The client submits tasks to the server, which sends
them to the available workers. The client and server may run on login or compute nodes,
and the workers run on compute nodes. HyperQueue resembles a Slurm within a Slurm,
but you must start the server and workers yourself. We recommend reading the official
[HyperQueue documentation](https://it4innovations.github.io/hyperqueue/stable/).

In a Slurm batch job, each Slurm task corresponds to one HyperQueue worker. The example
below uses a job-specific directory containing an executable `task.sh` script and a `batch.sh`
script that starts the server and workers, submits the tasks, and shuts everything down:

```text
.             # Current working directory
├── batch.sh  # Batch script for HyperQueue server and workers
└── task.sh   # Executable task script for HyperQueue
```

#### Example: Single-node job on Roihu-CPU

The `task.sh` script is an executable script submitted to the workers. We assume tasks are
independent and run on a single node. Here is a trivial example written in Bash:

```bash title="task.sh"
#!/bin/bash
sleep 1   # ~0.1 ms HyperQueue overhead per task, so even tiny tasks run efficiently
```

The `batch.sh` script orchestrates the run. The inline comments explain each step:

```bash title="batch.sh"
#!/bin/bash
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1   # one HyperQueue worker
#SBATCH --cpus-per-task=10    # cpus per worker
#SBATCH --mem-per-cpu=1000    # memory per cpu
#SBATCH --time=00:15:00

module load hyperqueue

# Server files go in a job-specific directory: start one server per job to avoid
# mixing up separate computations and the limited storage under $HOME (the default
# location if HQ_SERVER_DIR is unset). All hq commands respect this variable.
export HQ_SERVER_DIR="$PWD/hq-server/$SLURM_JOB_ID"
mkdir -p "$HQ_SERVER_DIR"

# Start the server in the background and wait until it is up. We background it because
# the server keeps running until we stop it and must not block the rest of the script.
hq server start &
until hq job list &> /dev/null ; do sleep 1 ; done

# Start one worker per Slurm task with srun, reserving the requested cpus. We wait for
# all workers to connect so that any worker problems surface early.
srun --overlap --cpu-bind=none --mpi=none hq worker start \
    --manager slurm \
    --on-server-lost finish-running \
    --cpus="$SLURM_CPUS_PER_TASK" &
hq worker wait "$SLURM_NTASKS"

# Submit the tasks (non-blocking). We disable per-task stdout/stderr files to avoid
# excess I/O on the parallel filesystem when there are many tasks. Then wait for them.
hq submit --stdout=none --stderr=none --cpus=1 --array=1-1000 ./task.sh
hq job wait all

# Shut down the workers and server to avoid a false error from Slurm when the job ends.
hq worker stop all
hq server stop
```

Notes on the resource request: each Slurm task becomes one HyperQueue worker. Use
`--cpus-per-task` and `--mem-per-cpu` to reserve a fraction of a node per worker (a
*partial* node allocation, as above), or `--cpus-per-task=<all cpus on a node>` together
with `--mem=0` to reserve a whole node per worker (a *full* node allocation). Increase
`--nodes` to run workers on more nodes; the [multinode example](#example-multinode-job-on-roihu-cpu-with-local-disks)
below uses a full multinode allocation.

It is worth reading the sections about
[Jobs and Tasks](https://it4innovations.github.io/hyperqueue/stable/jobs/jobs/)
and [Task Arrays](https://it4innovations.github.io/hyperqueue/stable/jobs/arrays/)
to understand the different ways to run computations with HyperQueue. For more
complex task dependencies, you can use HyperQueue as the executor for other workflow
managers, such as [Snakemake or Nextflow](#using-snakemake-or-nextflow-with-hyperqueue).

#### Example: Multinode job on Roihu-CPU with local disks

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

The following complete multinode example stages input to and output from the local disk.
The archive `input.tar.gz` used here extracts into an `input` directory.

```bash title="extract.sh"
#!/bin/bash
tar xf input.tar.gz -C "$TMPDIR"
mkdir -p "$TMPDIR/output"
```

```bash title="task.sh"
#!/bin/bash
cd "$TMPDIR"
cat "input/$HQ_TASK_ID.inp" > "output/$HQ_TASK_ID.out"
sleep 1
```

```bash title="archive.sh"
#!/bin/bash
cd "$TMPDIR"
tar czf "output-$SLURMD_NODENAME.tar.gz" output
cp "output-$SLURMD_NODENAME.tar.gz" "$SLURM_SUBMIT_DIR"
```

```bash title="batch.sh"
#!/bin/bash
#SBATCH --account=<project>
#SBATCH --partition=medium
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=384
#SBATCH --mem=0
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

# Download some example input files
wget https://a3s.fi/CSC_training/input.tar.gz

# Extract input files to the local disk and create a directory for outputs
srun -m arbitrary -w "$SLURM_JOB_NODELIST" ./extract.sh

# Submit tasks to workers
hq submit --stdout=none --stderr=none --cpus=1 --array=1-1000 ./task.sh

# Wait for all tasks to finish
hq job wait all

# Archive and copy output from each local disk to working directory on Lustre
srun -m arbitrary -w "$SLURM_JOB_NODELIST" ./archive.sh

# Shut down the workers and server
hq worker stop all
hq server stop
```

### Using Snakemake or Nextflow with HyperQueue

See a [Nextflow](../support/tutorials/nextflow-tutorial.md#running-nextflow-with-hyperqueue-executor) or [Snakemake](../apps/snakemake.md#running-snakemake-with-hyperqueue-executor) page for instructions on
using HyperQueue as an executor for Nextflow or Snakemake workflows.

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

## References

If you use HyperQueue in your work, the developers ask that you cite:

> Jakub Beránek, Ada Böhm, Gianluca Palermo, Jan Martinovič, Branislav Jansík.
> HyperQueue: Efficient and ergonomic task graphs on HPC clusters. *SoftwareX*,
> 27:101814, 2024. <https://doi.org/10.1016/j.softx.2024.101814>

## More information

* [Using HyperQueue and local disk to process many files](https://csc-training.github.io/csc-env-eff/hands-on/throughput/hyperqueue.html)
* [Farming Gaussian jobs with sbatch-hq](https://csc-training.github.io/csc-env-eff/hands-on/throughput/gaussian_hq.html)

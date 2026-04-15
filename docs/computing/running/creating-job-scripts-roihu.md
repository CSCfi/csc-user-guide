# Creating a batch job script for Roihu

A batch job script contains the definitions of the resources to be reserved for
a job and the commands the user wants to run.

[TOC]

## The structure of a batch job script

An example of a batch job script using a share of resources on a single node:

```bash
#!/bin/bash
#SBATCH --job-name=my-test          # Job name
#SBATCH --account=<project>         # Billing project, has to be defined!
#SBATCH --partition=small           # Job partition (queue)
#SBATCH --time=00:30:00             # Max. duration of the job
#SBATCH --nodes=1                   # Number of nodes used for the job
#SBATCH --ntasks=1                  # Number of tasks allocated
#SBATCH --cpus-per-task=1           # Number of CPU cores allocated per task
#SBATCH --mem-per-cpu=2000M         # Memory to reserve per CPU core
#SBATCH --output=slurm-%j.out       # Standard output of the job script
#SBATCH --hint=nomultithread        # Allocate full CPU cores
##SBATCH --mail-type=BEGIN          # Uncomment to enable mail

module load myprog/1.2.3            # Load required modules

srun myprog -i input -o output      # Run program using requested resources
```

The first line `#!/bin/bash` tells that the file should be interpreted as a
Bash script.

The lines starting with `#SBATCH` are arguments (directives) for the batch job
system. These examples only use a small subset of the options. For a list of
all possible options, see the
[Slurm documentation](https://slurm.schedmd.com/sbatch.html).

The general syntax of an `#SBATCH` option is:

```bash
#SBATCH --option_name=argument
```

The first line in our example, sets the name of the job:

```bash
#SBATCH --job-name=my-test
```

The name of the job will be *my-test*. It can be used to identify a job in the
queue and other listings.


The billing project for the job is set with option `--account`:

```bash
#SBATCH --account=<project>
```

Please replace `<project>` with the Unix
group of your project. You can find it in [MyCSC](https://my.csc.fi) under the
*Projects* tab. [More information about billing](../../accounts/billing.md).

!!! warning "Remember to specify the billing project"
    The billing project argument is mandatory. Failing to
    set it will cause an error:

    ```text
    sbatch: error: AssocMaxSubmitJobLimit
    sbatch: error: Batch job submission failed: Job violates accounting/QOS policy (job submit limit, user's size and/or time limits)
    ```

The partition (queue) needs to be set according to the job requirements. For
example:

```bash
#SBATCH --partition=small
```

!!! info "Available partitions"
    [See the available batch job partitions](batch-job-partitions.md).

The runtime reservation is set with option `--time`:

```bash
#SBATCH --time=00:30:00
```

Time is provided using the format `hours:minutes:seconds` (optionally `days-hours:minutes:seconds`)
The maximum runtime depends on the selected queue. **When the
time reservation ends, the job is terminated regardless of whether it has
finished or not**, so the time reservations should be sufficiently long. Note
that a job consumes Billing Units according to its actual runtime.

The number of nodes used for the job can be set with option `--nodes`:

```bash
#SBATCH --nodes=1
```

This does **not** mean that the all the resources of the node(s) would be reserved, but that
all the tasks and CPU cores will be allocated from a single node in this case. In general,
here one could give a range `--nodes=<minnodes>-<maxnodes>` to define the spread of nodes
across which the resources would be allocated.

The number of tasks allocated for the job can be set with option `--ntasks`:

```bash
#SBATCH --ntasks=1
```

The allocated tasks can be used in different ways in the job script, most typically as
MPI processes.

The number of CPU cores per task allocated for the job can be set with option `--cpus-per-task`:

```bash
#SBATCH --cpus-per-task=1
```

The product of `--ntasks` and `--cpus-per-task` defines the total amount of CPU cores
allocated for the job.

The amount of memory reserved for each CPU core is set with option `--mem-per-cpu`:

```bash
#SBATCH --mem-per-cpu=2000M
```

If the program exceeds the reserved amount of memory, the job is terminated.

The standard output file of the job script is set with option `--output`:

```bash
#SBATCH --output=slurm-%j.out
```

The standard output means all the prints that would be visible in the shell if
the commands listed in the script were executed in an interactive shell.
Here `%j` is a replacement symbol for jobid, so the output will go to the file `slurm-<slurm-jobid>.out`.
By default, this file collects also the standard error, but it is possible
to specify a different file for standard error with `--error=<filename_pattern>`.

The allocation of CPU cores vs hardware threads is controlled with the option:

```bash
#SBATCH --hint=nomultithread
```

Use this option always by default and change it only if you are absolutely sure that it is beneficial.

!!! info "About `--hint=nomultithread`"
    The default behavior regarding this setting is likely to change.

The user can be notified by email when the job *starts* by using the
`--mail-type` option

```bash
##SBATCH --mail-type=BEGIN          # Uncomment to enable mail
```

Other useful arguments (multiple arguments are separated by a comma) are `END`
and `FAIL`. By default, the email will be sent to the email address linked to
your CSC account. This can be overridden with the `--mail-user=` option.

After defining all required resources in the batch job script, set up the
required environment by loading suitable modules. Note that for modules to be
available for batch jobs, they need to be loaded in the batch job script.
[More information about environment modules](../modules.md).

```bash
module load myprog/1.2.3
```

Finally, we launch our application using the requested resources with the
`srun` command:

```bash
srun myprog -i input -o output
```

## Serial and shared memory batch jobs

Serial and shared memory jobs need to be run within one compute node. Thus, the
jobs are limited by the hardware specifications available in the nodes.
On Roihu, each node has two processors with 192 cores each, i.e. 384 cores in total.
[See more technical details about Roihu](../systems-roihu.md).

The `#SBATCH` option `--cpus-per-task` is used to define the number of
computing cores that the batch job task uses. The option `--nodes=1` ensures
that all the reserved cores are located in the same node, and `--ntasks=1`
assigns all reserved computing cores for the same task.

In thread-based jobs, the `--mem` option is recommended for memory reservation.
This option defines the amount of memory required *per node*. Note that if you
use `--mem-per-cpu` option instead, the total memory request of the job will be
the memory requested per CPU core (`--mem-per-cpu`) multiplied by the number of
reserved cores (`--cpus-per-task`). **Thus, if you modify the number of cores,
also check that the memory reservation is appropriate.**

Typically, the most efficient practice is to match the number of reserved cores
(`--cpus-per-task`) to the number of threads or processes the application uses.
However, always [check the application-specific details](../../apps/index.md).

If the application has a command-line option to set the number of
threads/processes/cores, it should always be used to ensure that the software
behaves as expected. Some applications use only one core by default, even if
more are reserved.

Other applications may try to use all cores in the node, even if only some
are reserved. The environment variable `$SLURM_CPUS_PER_TASK`, which stores the
value of `--cpus-per-task`, can be used instead of a number when specifying the
amount of cores to use. This is useful as the command does not need to be
modified if the `--cpus-per-task` is changed later.

Finally, use the environment variable `OMP_NUM_THREADS` to set the number of
threads the application uses. For example,

```bash
export OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK:-1}
```

(note the `:-1` syntax, which sets the number of threads to 1
if `--cpus-per-task` was not set).

## MPI-based batch jobs

In MPI jobs, each task has its own memory allocation. Thus, the tasks can be
distributed over multiple nodes.

When running jobs on a partial node (`small` partition), set the number of MPI tasks with:

``` bash
#SBATCH --ntasks=<number_of_mpi_tasks>
```

When running on full nodes (`medium` and `large` partitions),
it is recommended to **not** use `--ntasks` option,
but instead set `--nodes` and `--ntasks-per-node` instead:

``` bash
#SBATCH --nodes=<number_of_full_nodes>
#SBATCH --ntasks-per-node=384  # Number of MPI tasks per node = number of CPU cores per node
```

This ensures predictable distribution and CPU binding of processes within the node,
[see Performance checklist](./performance-checklist.md).

!!! info "Running MPI programs"
    - MPI programs **should not** be started with `mpirun` or `mpiexec`. Use
      `srun` instead.
    - An MPI module has to be loaded in the batch job script for the program
      to work properly.

## Hybrid batch jobs (e.g. MPI+OpenMP)

In hybrid jobs, each task is allocated several cores. Each task then uses some
parallelization, other than MPI, to do the work. The most common strategy is
for every MPI task to launch multiple threads using OpenMP. To request more
cores per MPI task, use the argument `--cpus-per-task`. The default value is
one core per task.

When running on full nodes, it is recommended to write
`--ntasks-per-node` and `--cpus-per-task` options on
the same `#SBATCH` line for clarity:

``` bash
#SBATCH --nodes=<number_of_full_nodes>
#SBATCH --ntasks-per-node=192 --cpus-per-task=2  # The product should be 384
#SBATCH --ntasks-per-node=96  --cpus-per-task=4  # The product should be 384
```

The reason is that these options go hand-in-hand in a sense that their product should
always be 384 in order to use all CPU cores available on the Roihu node.
You can comment out one of the lines to test the optimal run configuration for
your application,
[see Performance checklist](./performance-checklist.md).

The optimal ratio between the number of tasks and cores per tasks varies for each
program and job input. Testing is required to find the right combination for your
application. You can find some examples for
[CP2K](../../apps/cp2k.md#performance-notes) and
[NAMD](../../apps/namd.md#performance-considerations).

!!! info "Threads per task in hybrid MPI+OpenMP jobs"
    Set the number of OpenMP threads per MPI task in your batch script using
    the `OMP_NUM_THREADS` and `SLURM_CPUS_PER_TASK` environment variables:

    ```bash
    export OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK:-1}
    ```

## GPU jobs

Each Roihu-GPU node has four Nvidia GH200 superchips. The GPUs are available in the `gpu*` partitions.

The resource allocation is based on full GH200 GPUs in `gputest`, `gpumedium`, and `gpularge` partitions
and the GPUs can be requested with:

```bash
#SBATCH --partition=gpumedium
#SBATCH --gres=gpu:gh200:<number_of_gpus_per_node>
```

Note that the `--gres` reservation is on a per-node basis. There are 4 GPUs per GPU node.

!!! info "About `gpuinteractive` partition"
    The MIGs are not configured yet.

In `gpuinteractive` partition, the GH200 GPUs are sliced into smaller Multi-Instance GPUs (MIG).
Each MIG here has one XXXth of the compute and memory capacity of a full GH200 GPU.
For each GPU slice you can reserve at most XXX CPU cores and for each GPU slice the job is allocated XXX GiB of CPU memory.
Also note that you can reserve at most one GPU slice per job. The GPU slices are available using the options:

```bash
#SBATCH --partition=gpuinteractive
#SBATCH --gres=gpu:gh200_xxx:1
```

## Visualization jobs

Roihu has visualization nodes with Nvidia L40 GPUs. These nodes are available in the `vizinteractive` partition.

These nodes can be requested with:

```bash
#SBATCH --partition=vizinteractive
#SBATCH --gres=gpu:l40:<number_of_gpus_per_node>
```

Note that the `--gres` reservation is on a per-node basis. There are 2 GPUs per GPU node.


## Additional resources in batch jobs

### Local temporary storage

All nodes on Roihu have fast local storage space (NVMe) available for jobs.
Using local storage is recommended for I/O-intensive applications, i.e. jobs
that, for example, read and write a lot of small files.
[See more details](../disk.md#temporary-local-disk-areas).

Local temporary storage is available for every job without extra billing.
Quota is set per user, so available space on a node is independent of
job count or reserved resources:

- Roihu-CPU shared nodes (`small`, `interactive`, and `test` partitions) have 20 GiB quota
- Roihu-CPU full nodes (`medium` and `large` partitions) have 600 GiB quota
- Roihu-GPU nodes have 150 GiB quota

Use the environment variable `$TMPDIR` in your batch job scripts to
access the local temporary storage space on each node. For example, to extract a large
dataset package to the local storage:

```bash
tar xf my-large-dataset.tar.gz -C $TMPDIR
```

!!! warning "Remember to recover your data"
    The local storage space reserved for your job is emptied after the job has
    finished. Thus, if you write data to the local disk during your job, please
    remember to move anything you want to preserve to the shared disk area at
    the end of your job. Particularly, the commands to move the data must be
    given in the batch job script as you cannot access the local storage space
    anymore after the batch job has completed. For example, to copy some output
    data back to the directory from where the batch job was submitted:

    ```bash
    mv $TMPDIR/my-important-output.log $SLURM_SUBMIT_DIR
    ```

### Fast local scratch storage

As a new feature on Roihu, it is possible to request local disk mounts from a centralized pool of fast storage resources.
This fast storage capacity is provided over the network and
appears as local scratch from within a Slurm job.

!!! info "About fast local scratch storage"
    This section is work in progress.

Request this local storage using the following flag in the batch script:

```bash
#SBATCH xxx
```

For example, requesting 100 GiB storage:

```bash
#SBATCH xxx
```

Then, this storage is available in path `...` during the job script.


### Simultaneous multithreading (SMT) on Roihu-CPU

SMT support can be enabled with `--hint=multithread` option.
When this option is used, it is important to use the `--ntasks-per-node=X` and
`--cpus-per-task=Y` so that `X * Y = 768`. Failing to do so will leave some of the
actual physical cores unallocated and performance will be suboptimal.

### Undersubscribing full nodes on Roihu-CPU

If an application requires more memory per core than there is available
with full node (2 GB / core) it is possible to use also a subset of
cores within a node. Also, if the application is memory bound, memory
bandwidth and the application performance can be improved by using
only a single core per NUMA domain or L3 cache (look at
[Roihu technical description](../systems-roihu.md) for details.
Note that billing is, however, always based on full nodes.

When undersubscribing nodes, one should always set
`--ntasks-per-node=X` and `--cpus-per-task=Y` so that `X * Y = 384`,
even with pure MPI jobs. By default, Slurm scatters MPI tasks
`--cpus-per-task` apart, i.e. with `--cpus-per-task=16` the MPI task
**0** is bound to CPU core **0**, the MPI task **1** is bound to CPU
core **15** _etc._. Memory bandwidth (and application performance) is
the best when the tasks are executing on maximally scattered cores. As
an example, in order to use 32 GB / core, one can run only with 24
tasks per node as

```bash
...
#SBATCH --ntasks-per-node=24 --cpus-per-task=16

module load myprog/1.2.3
export OMP_NUM_THREADS=1

srun myprog -i input -o output
```

For hybrid applications, one should use
`OMP_PROC_BIND` OpenMP runtime environment variable for
placing the OpenMP threads. As an example, in order to run
one MPI task per NUMA domain and one OpenMP thread per L3 cache one
can set

```bash
...
#SBATCH --ntasks-per-node=8 --cpus-per-task=48

export OMP_NUM_THREADS=3
export OMP_PROC_BIND=spread

module load myprog/1.2.3

srun myprog -i input -o output
```

### Using small partition for non-parallel pre- or post-processing

In many cases, large computing tasks include pre- or post-processing steps that are not able to utilize parallel computing.
In these cases it is recommended that, if possible, the task is split into several, chained, batch jobs and that the non-parallel
processing is executed in the small partition of Roihu.
In the small partition the jobs can reserve just few cores so that the non-parallel tasks can be executed without wasting resources.

For example, say that we would like to post-process an _output_ file of a previous job. The post processing command:
`python post-proc.py output` uses only serial computing and requires about 40 minutes and 3 GB of memory. Instead of including the post-processing
to the main job it is reasonable to execute it as separate job in the small partition as in the example below.
Further, by defining `--dependency=afterok:<slurm-jobid>`, the job is allowed to start only when the previously sent job has successfully finished.
Here the `<slurm-jobid>` is replaced with ID number of the batch job that produces the _output_ file (you'll get the ID number when you submit the job).

```bash
#!/bin/bash
#SBATCH --job-name=post-process-my-test
#SBATCH --account=<project>
#SBATCH --time=00:50:00
#SBATCH --partition=small
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=4G
#SBATCH --dependency=afterok:<slurm-jobid>

python post-proc.py output
```

### Executing large amounts of small non-MPI jobs

In Roihu, [HyperQueue](../../apps/hyperqueue.md) meta-scheduler
can be used to process large amounts of small non-MPI jobs.

## More information

* [Roihu example batch scripts](example-job-scripts-roihu.md)
* [Available batch job partitions](batch-job-partitions.md)
* [Batch job training materials](https://csc-training.github.io/csc-env-eff/part-1/batch-jobs/)
* [Slurm documentation](https://slurm.schedmd.com/documentation.html)

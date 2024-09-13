# Creating a batch job script for Puhti

A batch job script contains the definitions of the resources to be reserved for
a job and the commands the user wants to run.

[TOC]

## A basic batch job script

An example of a simple batch job script:

```bash
#!/bin/bash
#SBATCH --job-name=myTest           # Job name
#SBATCH --account=<project>         # Billing project, has to be defined!
#SBATCH --time=02:00:00             # Max. duration of the job
#SBATCH --mem-per-cpu=2G            # Memory to reserve per core
#SBATCH --partition=small           # Job queue (partition)
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

The general syntax of an `#SBATCH` option:

```bash
#SBATCH option_name argument
```

In our example,

```bash
#SBATCH --job-name=myTest
```

sets the name of the job to *myTest*. It can be used to identify a job in the
queue and other listings.

```bash
#SBATCH --account=<project>
```

sets the billing project for the job. Please replace `<project>` with the Unix
group of your project. You can find it in [My CSC](https://my.csc.fi) under the
*Projects* tab. [More information about billing](../../accounts/billing.md).

!!! warning "Remember to specify the billing project"
    The billing project argument is mandatory. Failing to
    set it will cause an error:

    ```text
    sbatch: error: AssocMaxSubmitJobLimit
    sbatch: error: Batch job submission failed: Job violates accounting/QOS policy (job submit limit, user's size and/or time limits)
    ```

The runtime reservation is set with option `--time`:

```bash
#SBATCH --time=02:00:00
```

Time is provided using the format `hh:mm:ss` (optionally `d-hh:mm:ss`, where
`d` is _days_). The maximum runtime depends on the selected queue. **When the
time reservation ends, the job is terminated regardless of whether it has
finished or not**, so the time reservations should be sufficiently long. Note
that a job consumes billing units according to its actual runtime.

```bash
#SBATCH --mem-per-cpu=2G
```

sets the required memory per requested CPU core. If the requested memory is
exceeded, the job is terminated.

The partition (queue) needs to be set according to the job requirements. For
example:

```bash
#SBATCH --partition=small
```

!!! info "Available partitions"
    [See the available batch job partitions](batch-job-partitions.md).

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
jobs are limited by the hardware specifications available in the nodes. On
Puhti, each node has two processors with 20 cores each, i.e. 40 cores in total.
[See more technical details about Puhti](../systems-puhti.md).

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
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
```

## MPI-based batch jobs

In MPI jobs, each task has its own memory allocation. Thus, the tasks can be
distributed over multiple nodes.
 
Set the number of MPI tasks with:

``` bash
#SBATCH --ntasks=<number_of_mpi_tasks>
```
 
If more fine-tuned control is required, the exact number of nodes and number of
tasks per node can be specified with `--nodes` and `--ntasks-per-node`,
respectively. This is typically recommended in order to avoid tasks spreading
over unnecessary many nodes,
[see Performance checklist](./performance-checklist.md#limit-unnecessary-spreading-of-parallel-tasks-in-puhti).

It is recommended to request memory using the `--mem-per-cpu` option.

!!! info "Running MPI programs"
    - MPI programs **should not** be started with `mpirun` or `mpiexec`. Use
      `srun` instead.
    - An MPI module has to be loaded in the batch job script for the program
      to work properly.

## Hybrid batch jobs 

In hybrid jobs, each task is allocated several cores. Each task then uses some
parallelization, other than MPI, to do the work. The most common strategy is
for every MPI task to launch multiple threads using OpenMP. To request more
cores per MPI task, use the argument `--cpus-per-task`. The default value is
one core per task.

The optimal ratio between the number of tasks and cores per tasks varies for
each application. Testing is required to find the right combination for your
application.

!!! info "Threads per task in hybrid MPI/OpenMP jobs"
    Set the number of OpenMP threads per MPI task in your batch script using
    the `OMP_NUM_THREADS` and `SLURM_CPUS_PER_TASK` environment variables:

    ```bash
    export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
    ```

## Additional resources in batch jobs

### Local storage

Some nodes on Puhti have fast local storage space (NVMe) available for jobs.
Using local storage is recommended for I/O-intensive applications, i.e. jobs
that, for example, read and write a lot of small files.
[See more details](../disk.md#temporary-local-disk-areas).

Local storage is available on:

* GPU nodes in the `gpu` and `gputest` partitions (max. 3600 GB per node)
* I/O nodes shared by the `small`, `large`, `longrun` and `interactive`
  partitions (max. 1490/3600 GB per node)
* BigMem nodes in the `hugemem` and `hugemem_longrun` partitions (max. 5960 GB
  per node)

Request local storage using the `--gres` flag in the batch script:

```bash
#SBATCH --gres=nvme:<local_storage_space_per_node_in_GB>
```

The amount of space is given in GB (check maximum sizes from the list above).
For example, to request 100 GB of storage, use option `--gres=nvme:100`. The
local storage reservation is on a per-node basis.

Use the environment variable `$LOCAL_SCRATCH` in your batch job scripts to
access the local storage space on each node. For example, to extract a large
dataset package to the local storage:

```bash
tar xf my-large-dataset.tar.gz -C $LOCAL_SCRATCH
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
    mv $LOCAL_SCRATCH/my-important-output.log $SLURM_SUBMIT_DIR
    ```

### GPUs

Puhti has 320 Nvidia Tesla V100 GPUs. The GPUs are available in the `gpu` and
`gputest` partitions and can be requested with:

```bash
#SBATCH --gres=gpu:v100:<number_of_gpus_per_node>
```

The `--gres` reservation is on a per-node basis. There are 4 GPUs per GPU node.

Multiple resources can be requested with a comma-separated list. To request
both GPU and local storage:

```bash
#SBATCH --gres=gpu:v100:<number_of_gpus_per_node>,nvme:<local_storage_space_per_node>
```

For example, to request 1 GPU and 10 GB of NVMe storage the option would be
`--gres=gpu:v100:1,nvme:10`.

## More information

* [Puhti example batch scripts](example-job-scripts-puhti.md)
* [Available batch job partitions](batch-job-partitions.md)
* [Batch job training materials](https://csc-training.github.io/csc-env-eff/part-1/batch-jobs/)
* [Slurm documentation](https://slurm.schedmd.com/documentation.html)

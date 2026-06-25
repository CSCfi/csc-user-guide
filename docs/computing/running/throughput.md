# High-throughput computing and workflows

High-throughput computing (HTC) refers to running a large number of computational
tasks, frequently enabled by automatization, scripts and workflow managers. This
page introduces the key concepts you should consider when designing high-throughput
workflows and helps you narrow down the right set of tools for your use case. By
carefully selecting the most appropriate technology stack, your jobs will idle
less in the queue, IO-operations will be more efficient and the performance of the
whole HPC system will remain stable and fast for all users.

## Concepts

### High-throughput computing and workflows on HPC

A characteristic feature of high-throughput computing is running a large amount of
similar, often short, computational tasks. When these tasks are independent of each
other this is frequently called *task farming* or an *embarrassingly parallel*
problem, since the tasks can in principle be distributed to as many processors as
there are tasks to run. Typical examples are analyzing many datasets the same way,
or running the same simulation with many different parameters.

A *workflow* is a series of tasks where some tasks depend on the output of others
and therefore must run in a defined order. Workflow managers automate the execution
of such task graphs.
Workflows are frequently very specific, and one seldom finds a method that works out
of the box for a given application.

### Why a single large Slurm job instead of many small ones

Running a large number of separate batch jobs (launched with `sbatch`) and job
steps (launched with `srun`) poses problems for batch job schedulers such as Slurm.
Many jobs and job steps generate excess log data and slow down Slurm. Short jobs
also have a large scheduling overhead, meaning that an increasing fraction of the
time is spent waiting in the queue instead of computing.

To enable high-throughput computing while avoiding these issues, **pack your tasks
so that they run with as few `sbatch` and `srun` invocations as possible** —
typically by reserving one large resource allocation and running many tasks inside
it with a suitable tool (see below).

### Tasks: count, size, and dependencies

A *task* (or *subtask*) is a single unit of work in your workflow, for example one
simulation, one dataset to analyze, or one parameter value to evaluate. Use the following properties of your tasks drive the choice of tool:

- **Large number of small tasks.** Running large number (over 100) of very short tasks (under ~30 minutes) is inefficient as individual Slurm jobs and should be packed.

- **Dependencies between tasks.** Are the tasks independent of each other, or must
  some tasks finish before others can start? Independent tasks can be handled by
  simple [HTC tools](#high-throughput-computing-on-hpc). Tasks with dependencies
  generally call for a [workflow manager](#workflows-on-hpc).

Don't hesitate to [contact CSC Service Desk](../../support/contact.md) if you have any concerns about how to
implement your workflow.
Workflows contains hundreds or thousands of *multi-node* tasks may require a special solution.


## High-throughput computing on HPC

This section covers tools for running a large number of *independent* tasks. They
cover HTC use cases from tens to hundreds of thousands of tasks.
The options are ordered roughly from "try this first" downwards.

### Built-in HTC options in your software

Many simulation packages can run multiple independent simulations within a single
Slurm job step. **If your software offers such a built-in option, use it as your
first choice.** Examples available at CSC:

- [GROMACS `multidir` option](../../support/tutorials/gromacs-throughput.md)
- [FARMING mode of CP2K](../../apps/cp2k.md#high-throughput-computing-with-cp2k) (also supports dependencies between subjobs)
- [LAMMPS multi-partition switch](../../apps/lammps.md#high-throughput-computing-with-lammps)
- [Amber multi-pmemd](../../apps/amber.md#high-throughput-computing-with-amber)

### Individual Slurm jobs, job steps, and array jobs

Plain Slurm tools are a good fit when each task is long enough that the scheduling
overhead is negligible (individual runtimes longer than ~30 minutes).
Slurm should also be your first option for MPI jobs.

You can check the limits on the number of running and queued jobs for a project as follows:

```bash
sacctmgr show assoc user=$USER account=<project> format=Account,Partition,MaxJobs,MaxSubmit -p
```

Here `MaxJobs` is the maximum number of jobs that can run simultaneously and
`MaxSubmit` is the maximum number of jobs that can be queued and running at the
same time.

[Array jobs](array-jobs.md) are the native Slurm way to submit many similar independent tasks with
a single command. They integrate seamlessly with Slurm and support MPI/OpenMP tasks,
but do not pack job steps or handle dependencies. On Puhti you can also use
`sbatch_commandlist` to run a list of commands as an array job, though `sbatch-hq`
(see [HyperQueue](../../apps/hyperqueue.md)) is a more efficient alternative.

### GNU Parallel and xargs

[GNU Parallel](../../support/tutorials/many.md) lets you efficiently run a very large number of short, *serial*,
independent tasks without bloating the Slurm log. It does not require a database or
a persistent manager and does not support dependencies between tasks.
You can also use the Linux `xargs` utility for the same purpose, see [xargsjob.sh](https://a3s.fi/pub/xargsjob.sh) for an example.


### HyperQueue

[HyperQueue](../../apps/hyperqueue.md) is the recommended general-purpose tool for high-throughput computing.
Instead of submitting each task as a separate Slurm job or job step, you allocate a
large resource block and let HyperQueue schedule your tasks into it with minimal
load on Slurm and little extra I/O. It can schedule tasks at sub-node granularity,
supports MPI tasks, and scales to large numbers of tasks across many nodes.

For simple command-list task farming, the CSC utility `sbatch-hq` wraps HyperQueue
so you can submit an ensemble of similar independent tasks directly from a file of
commands. HyperQueue can also act as the [task executor for workflow
managers](#workflows-on-hpc).

### Distributed computing in your programming language

If your work is already written in a high-level language, the language's own
parallel and distributed computing facilities are often the simplest option:

- Python:
    * [Python parallel jobs](../../support/tutorials/python-usage-guide.md#python-parallel-jobs)
    * [CSC Dask tutorial](../../support/tutorials/dask-python.md)
    * [CSC machine learning guide](../../support/tutorials/ml-guide.md)
- R:
    * [Parallel jobs using R](../../support/tutorials/parallel-r.md)
    * [R targets library](https://docs.ropensci.org/targets/)
- Julia:
    * [Julia batch jobs](../../support/tutorials/julia.md)

## Workflows on HPC

When your tasks have dependencies and form a pipeline, use a workflow manager. These
tools track which tasks depend on which, run tasks in the correct order, recover from
errors by restarting failed tasks, and typically integrate containers automatically.

### HyperQueue

[HyperQueue](../../apps/hyperqueue.md) schedules task graphs efficiently and can run dependent tasks within a
single resource allocation. It can also serve as the task executor underneath
Snakemake or Nextflow. To define dependencies between tasks, use the
[HyperQueue Python API](https://it4innovations.github.io/hyperqueue/stable/python/),
which lets you build a task graph where each task can declare the tasks it depends on.

### Snakemake

[Snakemake](../../apps/snakemake.md) is a popular Python-based workflow manager with dependency support and
automatic container integration. See the [Snakemake on Puhti
tutorial](../../support/tutorials/snakemake-puhti.md) for how to run it at CSC,
including with the HyperQueue executor.

### Nextflow

[Nextflow](../../apps/nextflow.md) is a popular workflow manager based on Groovy, with dependency support
and container integration. See the [Nextflow
tutorial](../../support/tutorials/nextflow-tutorial.md) for how to run it at CSC,
including with the HyperQueue executor.

### FireWorks

[FireWorks](fireworks.md) is a workflow tool for complex dependencies and multi-node subtasks. Be
aware that it can create a lot of job steps and extra files, which is less ideal for
HTC; prefer the options above when they fit your use case.

### Other options

This is not a complete list, and other tools may also work for your use case.

## Other considerations

### I/O and the parallel file system

When running many parallel tasks, input/output (IO) efficiency often becomes a
problem. CSC supercomputers use [Lustre](../lustre.md) as the parallel distributed file system.
It is designed for efficient parallel IO of large files, but when dealing with many
small files IO quickly becomes a bottleneck. Intensive IO-operations risk degrading
the file system performance for all users and should be moved away from Lustre.

If you need to read and write thousands of files, choose a faster location for the
IO-heavy part of your workflow:

- If your application is containerized, [mount your datasets with SquashFS](../containers/overview.md#reading-datasets-from-squashfs-file). This
  reduces a dataset of thousands of files to a single file from Lustre's point of
  view, while appearing as an ordinary directory inside the [Singularity container](../containers/overview.md).
- If you run a Conda/pip environment, [containerize it with Tykky](../containers/tykky.md). CSC has
  [deprecated direct usage of Conda environments](../../support/tutorials/conda.md) because they bring about a huge
  number of files that are read on every run, causing system-wide slowdowns.
- Otherwise, use [fast local NVMe disk](../disk.md#compute-nodes-with-local-ssd-nvme-disks) (available on the CPU nodes of Puhti and on
  Mahti), or [ramdisk](../disk.md#compute-nodes-without-local-ssd-nvme-disks) (`/dev/shm`) on Mahti CPU partitions with node-based
  allocation (only if you know what you are doing).
- If you must use Lustre for IO-heavy tasks, leverage [file striping](../lustre.md#file-striping-and-alignment).

Further details on [how to work efficiently with Lustre are documented here](../lustre.md#best-practices).

!!! warning "Note"
    Please do not reserve GPU nodes just to use the node's NVMe disk. To run on
    GPUs, your code must be GPU-enabled and benefit from the resources, [see usage
    policy](../usage-policy.md#gpu-nodes). Remember that the CPU nodes of Puhti also have NVMe disks.

### Further reading

- [Data storage guide for machine learning](../../support/tutorials/ml-data.md) — where to work with ML data and how
  to use the shared file system efficiently
- [Farming Gaussian jobs with HyperQueue](https://csc-training.github.io/csc-env-eff/hands-on/throughput/gaussian_hq.html)
- [Fast disk areas in CSC computing environment](https://csc-training.github.io/csc-env-eff/hands-on/data-io/tutorial-fastdisks.html)

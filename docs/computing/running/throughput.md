# High-throughput computing and workflows

High-throughput computing (HTC) refers to running a large number of computational tasks, frequently enabled by automatization, scripts and workflow managers.
This page introduces the key concepts you should consider when designing high-throughput workflows and helps you narrow down the right set of tools for your use case.
By carefully selecting the most appropriate technology stack, your jobs will idle less in the queue, IO-operations will be more efficient and the performance of the whole HPC system will remain stable and fast for all users.

## Concepts

### High-throughput computing and workflows on HPC

A characteristic feature of high-throughput computing is running a large amount of similar, often short, computational tasks.
When these tasks are independent of each other this is frequently called *task farming* or an *embarrassingly parallel* problem, since the tasks can in principle be distributed to as many processors as there are tasks to run.
Typical examples are analyzing many datasets the same way, or running the same simulation with many different parameters.

A *workflow* is a series of tasks where some tasks depend on the output of others and therefore must run in a defined order.
Workflow managers automate the execution of such task graphs.
Workflows are frequently very specific, and one seldom finds a method that works out of the box for a given application.

### Why a single large Slurm job instead of many small ones

Running a large number of separate batch jobs (launched with `sbatch`) and job steps (launched with `srun`) poses problems for batch job schedulers such as Slurm.
Many jobs and job steps generate excess log data and slow down Slurm.
Short jobs also have a large scheduling overhead, meaning that an increasing fraction of the time is spent waiting in the queue instead of computing.

To enable high-throughput computing while avoiding these issues, **pack your tasks so that they run with as few `sbatch` and `srun` invocations as possible**, by reserving one large resource allocation and running many tasks inside it with a suitable tool.
As a heuristic, if you are running more than 20 short tasks (under ~30 minutes) that run on a single node, you should consider packing them into a single slurm job.

### Other considerations

High-throughput workflows are often limited by I/O rather than by compute, so pay close attention to how your tasks use the parallel file system.
The Lustre file systems at CSC are optimized for reading and writing a moderate number of large files, and they perform poorly when a workload reads or writes large numbers of small files.
A common bottleneck occurs at task startup, when many tasks simultaneously open the same set of files, which can overload the file system and slow down not only your own jobs but the whole system for other users.
Some workflow tools also generate a large number of small intermediate and log files, which compounds the problem.
Whenever possible, reduce the number of files by keeping intermediate data in memory, bundling small files into archives, or directing heavy I/O to [local disk ares](../disk.md#temporary-local-disk-areas) instead of the shared parallel file system.

Containers are an effective way to reduce the file-count problem described above.
Software stacks that consist of a large number of small files, such as Python with its external packages or R with its libraries, are particularly problematic on the parallel file system, both when installed there and when imported at task startup.
Packaging such software into a single container image collapses these many small files into one file, which the parallel file system handles much more efficiently and which speeds up task startup considerably.
When running a high-throughput workload, run the task-farming or workflow tool inside a single long-running container rather than launching a separate container for each individual task, as starting many containers adds significant overhead.
See the [containers documentation](../containers/overview.md) for how to build and run containers at CSC.

## Task farming on HPC

This section covers tools for running a large number of *independent* tasks.
They cover HTC use cases from tens to hundreds of thousands of tasks.
The options are ordered roughly from "try this first" downwards.

### Individual Slurm jobs, job steps, and array jobs

Plain Slurm tools are a good fit when each task is long enough that the scheduling overhead is negligible (individual runtimes longer than ~30 minutes).
Slurm should also be your first option for MPI jobs because MPI jobs must be started using `srun`.
[Array jobs](array-jobs.md) are the native Slurm way to submit many similar independent tasks with a single command.
They integrate seamlessly with Slurm and support MPI tasks, but do not pack job steps or handle dependencies.

You can check the limits on the number of running and queued jobs as follows:

```bash
sacctmgr show assoc user=$USER format=Account,Partition,MaxJobs,MaxSubmit -p
```

Here `MaxJobs` is the maximum number of jobs that can run simultaneously and `MaxSubmit` is the maximum number of jobs that can be queued and running at the same time.

### Task farming with Python multiprocess on single node

```python title="farming.py"
#!/usr/bin/env python3
import os
import subprocess
from concurrent.futures import ProcessPoolExecutor, as_completed

def task(arg: str) -> str:
    # Run one task. Use subprocess to call an external command,
    # or replace this with your own Python code.
    ret = subprocess.run(["echo", "-n", arg], capture_output=True, text=True)
    return ret.stdout

if __name__ == "__main__":
    # Use one worker per reserved core (SLURM_CPUS_PER_TASK).
    max_workers = int(os.getenv("SLURM_CPUS_PER_TASK", "1"))

    # The arguments to run the task with, one task per argument.
    args = [str(i) for i in range(100)]

    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        # Submit all tasks to the pool; they run as workers become free.
        futures = [executor.submit(task, arg) for arg in args]

        # Collect the results as the tasks finish.
        results = []
        for future in as_completed(futures):
            results.append(future.result())

        print(results)
```

```bash title="farming.sh"
#!/bin/bash
#SBATCH --account=<project>
#SBATCH --partition=small
#SBATCH --time=00:15:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=10
#SBATCH --mem-per-cpu=1000
# You can load modules and set environment here if needed.
python3 farming.py
```

Submit to slurm

```bash
sbatch farming.sh
```

This approach is a good fit when your tasks run on a single node and you want fine-grained control over how they are executed.
The example above relies only on the Python standard library available from the system Python, so it requires no additional installation or environment setup.
Compared to shell scripting, Python scripting is more robust and easier to maintain, especially as the logic for launching and coordinating tasks grows more complex.
It also lets you integrate pre- and post-processing of your data directly into the same script, keeping intermediate results in memory and avoiding writing unnecessary files to the parallel file system.
The `ProcessPoolExecutor` distributes the tasks across the cores reserved for the job, and the number of workers is taken from `SLURM_CPUS_PER_TASK` so it automatically matches the resources requested in the batch script.

### Distributed computing in your programming language

If your work is already written in a high-level language, the language's own parallel and distributed computing facilities are often the simplest option:

Bash:

* [GNU xargs and parallel](../../support/tutorials/many.md) commands let you efficiently run a very large number of short, *serial*, independent tasks without bloating the Slurm log.
It does not require a database or a persistent manager and does not support dependencies between tasks.

Python:

* [Python parallel jobs](../../support/tutorials/python-usage-guide.md#python-parallel-jobs)
* [CSC Dask tutorial](../../support/tutorials/dask-python.md)
* [CSC machine learning guide](../../support/tutorials/ml-guide.md)

R:

* [Parallel jobs using R](../../support/tutorials/parallel-r.md)
* [R targets library](https://docs.ropensci.org/targets/)

Julia:

* [Julia multiprocessing on single node](../../apps/julia.md#multi-processing-on-single-node)
* [Julia multiprocessing on multiple nodes](../../apps/julia.md#multi-processing-on-multiple-nodes)

### Built-in HTC options in your software

Many simulation packages can run multiple independent simulations within a single Slurm job step.
Examples available at CSC:

- [GROMACS `multidir` option](../../support/tutorials/gromacs-throughput.md)
- [FARMING mode of CP2K](../../apps/cp2k.md#high-throughput-computing-with-cp2k) (also supports dependencies between subjobs)
- [LAMMPS multi-partition switch](../../apps/lammps.md#high-throughput-computing-with-lammps)
- [Amber multi-pmemd](../../apps/amber.md#high-throughput-computing-with-amber)

### Further reading

- [Farming Gaussian jobs with HyperQueue](https://csc-training.github.io/csc-env-eff/hands-on/throughput/gaussian_hq.html)

## Workflows on HPC

When your tasks have dependencies and form a pipeline, use a workflow manager.
These tools track which tasks depend on which, run tasks in the correct order and recover from errors by restarting failed tasks.
The following is not a complete list, and other tools may also work for your use case.

### HyperQueue

[HyperQueue](../../apps/hyperqueue.md) is a general-purpose tool for high-throughput computing.
Instead of submitting each task as a separate Slurm job or job step, you allocate a large resource block and let HyperQueue schedule your tasks into it with minimal load on Slurm and little extra I/O.
It can schedule tasks at sub-node granularity and scales to large numbers of tasks across many nodes.
To handle dependencies between tasks, [HyperQueue's Python API](https://it4innovations.github.io/hyperqueue/stable/python/), lets you build a task graph where each task can declare the tasks it depends on.
HyperQueue can also act as the task executor for workflow managers such as Snakemake and Nextflow.

For simple command-list task farming, the CSC utility `sbatch-hq` wraps HyperQueue so you can submit an ensemble of similar independent tasks directly from a file of commands.

### Snakemake

Snakemake is a popular Python-based workflow manager with dependency support and automatic container integration.
See the [Snakemake page](../../apps/snakemake.md) for how to run it at CSC, including with the HyperQueue executor.

### Nextflow

Nextflow is a popular workflow manager based on Groovy, with dependency support and container integration.
See the [Nextflow page](../../apps/nextflow.md) for how to run it at CSC, including with the HyperQueue executor.

### FireWorks

[FireWorks](../../apps/fireworks.md) is a workflow tool for complex dependencies and multi-node subtasks.
Be aware that it can create a lot of job steps and extra files, which is less ideal for HTC; prefer the options above when they fit your use case.

## Support

!!! Info "Support"
    Workflows containing a large number of *multi-node* tasks may require a special solution.
    Don't hesitate to [contact CSC Service Desk](../../support/contact.md) if you have any concerns about how to implement your workflow.

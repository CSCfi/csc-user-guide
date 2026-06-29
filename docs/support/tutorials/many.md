# GNU xargs and parallel workflows for many small, independent runs

## Overview

This tutorial is one approach to
high-throughput computing, where a large
number of similar, independent tasks are packed into a small number of Slurm
jobs instead of being submitted as individual jobs.

Both [xargs](https://www.gnu.org/software/findutils/) and
[GNU Parallel](https://www.gnu.org/software/parallel/) are command-line tools
for running a large number of tasks in parallel, and they work about the same
for this purpose. In this tutorial we use `xargs`, as it is simple, lightweight,
and usually provided by the base operating system, but the same workflow can be
done with GNU Parallel's `parallel` command. Here we use the tool inside a single
Slurm allocation to keep all the reserved cores busy: the names of the input
files are fed to `xargs`, which keeps running tasks until they are all
done, starting a new task as soon as a core becomes free.

`xargs` is a good fit for this purpose because it does not require a
database or a persistent manager process, it makes efficient use of scheduler
resources, and it scales easily to a large number of tasks and nodes. On the
other hand, it only runs serial subtasks and has no support for dependencies
between tasks or for error recovery. It also expects you to organize the input
and output files carefully, and scaling up requires you to consider the I/O
performance of the system. A modest familiarity with bash scripting is
recommended.

If your tasks have dependencies, you need error recovery or you want to explore tools, see
the [high-throughput computing and workflows](../../computing/running/throughput.md) page.

## Example: Running 80000 independent single-core tasks

In general, there are three pieces of input that are needed for designing the
workflow:

1. How many runs there will be in total?
2. How long does a single run take?
4. How many files will be created?

The first two determine how the runs are grouped into batch jobs, and the last
one determines the directory hierarchy.

Let's consider an example where we have 80000 independent, non-parallel
single-core runs, each taking from 0 to 30 minutes, with a 15-minute average. In
the worst case, all the runs in a batch job take the maximum amount of time, 30
minutes. We can see that a single 40-hour batch job should be enough for at
least 80 runs with a single core, and 3200 runs with all 40 cores in a full
compute node. Thus, all 80000 runs should fit in 25 40-hour batch jobs, each
reserving one full compute node.

Let's say our application is a real disk-hog, and in addition to one input file
and one output file that we wish to keep, it also creates 100 temporary files in
the current directory. We can have at maximum about 400 input and output files
in a single directory, and use the fast local disk in the I/O nodes for the
temporary files. For 80000 runs we thus get 200 directories, each with 400 runs.

```
many
    dir-001
        input-001
        input-002
        ...
        input-400
    dir-002
    ...
    dir-200
```

Additional consideration needs to be taken if the single runs are parallel, or
there are dependencies between them, but that's another story.

Let's look at the job script for our example case:

```bash
#!/bin/bash
#SBATCH --partition=small
#SBATCH --account=<project>
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=40
#SBATCH --time=40:00:00
#SBATCH --mem=160G
#SBATCH --gres=nvme:3600
#SBATCH --array=0-24

cd /scratch/${SLURM_JOB_ACCOUNT}/many

(( from_dir_index = SLURM_ARRAY_TASK_ID * 8 + 1 ))
(( to_dir_index = SLURM_ARRAY_TASK_ID * 8 + 8 ))

job_dirs=$(printf "%dir-%03d " $(seq $from_dir_index $to_dir_index))

find $job_dirs -name 'input-*' | \
    xargs -n 1 -P $SLURM_CPUS_PER_TASK bash wrapper.sh {}
```

The batch job reserves a whole node for 40 hours. One task starts in the node,
which has access to all 40 CPU cores in the node. Since we reserve all the
cores, we can reserve all the memory and all the local disk all the same, no
need to be stringy here. The last line, `#SBATCH --array=0,24`, tells the batch
system to execute 25 copies of this job, each job identified by a unique number
in environment variable `SLURM_ARRAY_TASK_ID`. Depending on the queue situation,
many of these jobs can run in parallel.

The `xargs` command is usually provided by the base operating system. In HPC systems
one often needs to load a module to make similar GNU Parallel `parallel` command
available. We use xargs command (or GNU Parallel)
within the node to "schedule" all 3200 runs in a job, so that at any point
in time all 40 cores are busy, but not overloaded.

Next lines calculate which directories belong to the current array job, using
the `SLURM_ARRAY_TASK_ID` environment variable.

The main "loop" of the script is implemented with `xargs` command (or GNU Parallel `parallel` command).
With the option `-P $SLURM_CPUS_PER_TASK` we tell xargs to
keep running 40 commands (applications) in parallel. Since we need to copy
files into and out from the local SSD for each run, we wrap our application in a
small shell script, `wrapper.sh`, which takes the input file name as an
argument. The names of the input files are fed to xargs through a pipe,
and xargs keeps on running the `bash wrapper.sh <input file>` command as
long as there are arguments in the pipe.

Separating the wrapper script from the batch job script makes it possible to
develop and test each other separately. In general, use small test sets when
developing the workflow, and do not expect to get it perfect on the first try.
You can study and test a small version of the example case with

```
export SBATCH_ACCOUNT=<your project>
wget -c https://a3s.fi/docs-files/support/tutorials/many.tar.gz -O - | tar xz
cd many
bash create_inputs.sh
tree /scratch/${SBATCH_ACCOUNT}/many
sbatch job.sh
```

!!! Note
    Running multiple separate jobs inside a larger allocation may result in
    idle resources. Please make sure that such a job has a lot of quick jobs
    to run, so that the last running job is not keeping the complete allocation
    alive for long. Thus, the length of a subjob should be much less than
    the duration of the allocation, and the number of subjobs much larger
    than the cores requested in one task.

You can use [seff](../faq/how-much-memory-my-job-needs.md) to learn how long 
past jobs have been.

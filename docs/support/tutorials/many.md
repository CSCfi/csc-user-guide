# GNU Parallel workflow for many small, independent runs

The goal is to have a workflow that is

1. *simple* to understand,
2. fits well into the *batch queue system*, and
3. does not stress the *parallel file system*.

There is a plethora of workflow tools. Whatever tool one chooses, it will
unlikely match the particular workflow and underlying computing platform out of
the box. Some amount of programming is needed in most cases. A very much related
discussion is in [Array jobs](../../computing/running/array-jobs.md)
chapter of <https://docs.csc.fi>.

## Strengths of GNU Parallel

* Does not require a database or persistent manager process
* Easily scales to a large number of tasks/nodes
* Efficient use of scheduler resources

## Disadvantages of GNU Parallel

* User is required to do careful organization of input and output files
* Scaling up requires consideration of system I/O performance
* Modest familiarity with bash scripting recommended
* Only serial subtasks
* No support for dependencies or error recovery

## System limits outline

The maximum number of jobs that each user can submit per month should be kept
below one thousand. Too many batch jobs will generate excess log data and slows
down the job scheduler.
[Array jobs](../../computing/running/array-jobs.md) are basically
just a shorthand, so a single array job of 100 members counts the same as 100
individual jobs from the batch queue system's perspective.

The job maximum runtime is limited by the queue parameters. The minimum time is
not limited, but if the job is too short, it is just generating proportionally
large scheduling overhead in the batch system.

!!! Tip
      A good target is to write batch
      jobs that finish somewhere between two hours and two days.

Parallel file systems work poorly when a single client (application program)
tries to perform too many file operations. Such cases can be e.g. applications
installed with the Conda package manager directly on the shared file system. 
One miniconda environment is easily over 20000 files and Anaconda distribution
is much worse. Many of these files need to be opened every time a Conda application
is launched. When running many, relatively short jobs, avoid running applications installed with Conda. However, if your application requires a complex environment,
use applications packed into Singularity containers, which are single files from
the perspective of the file system. To easily containerize a Conda environment,
see the [Tykky container wrapper tool](../../computing/containers/tykky.md)

"Too many files" issues are also often encountered with workflows consisting of
thousands of small runs. As a general guide, keep the number of files in a
single directory well below one thousand, and organize your data into multiple
directories. Also, use command `csc-workspaces` to monitor that the total number
of files in your projects stays well below the limits. If most of the files are
temporary, or there simply is too many of them, using the fast local SSD disks
in the
[I/O nodes](../../computing/running/creating-job-scripts-puhti.md#local-storage)
can solve the problem. You can pack small files into a bigger archive file with
the `tar` command. Most importantly, if there are output files that you do not need,
find out how to turn off writing those in the first place.

Please contact <servicedesk@csc.fi> if your workflow needs help to fit into the
limits given above.


## An example case, 80000 independent runs

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

module load parallel

cd /scratch/${SLURM_JOB_ACCOUNT}/many

(( from_dir_index = SLURM_ARRAY_TASK_ID * 8 + 1 ))
(( to_dir_index = SLURM_ARRAY_TASK_ID * 8 + 8 ))

job_dirs=$(printf "%dir-%03d " $(seq $from_dir_index $to_dir_index))

find $job_dirs -name 'input-*' | \
    parallel -j $SLURM_CPUS_PER_TASK bash wrapper.sh {}
```

The batch job reserves a whole node for 40 hours. One task starts in the node,
which has access to all 40 CPU cores in the node. Since we reserve all the
cores, we can reserve all the memory and all the local disk all the same, no
need to be stringy here. The last line, `#SBATCH --array=0,24`, tells the batch
system to execute 25 copies of this job, each job identified by a unique number
in environment variable `SLURM_ARRAY_TASK_ID`. Depending on the queue situation,
many of these jobs can run in parallel.

Next we load a module providing
[GNU parallel](https://www.gnu.org/software/parallel/). We use this tool
within the node to "schedule" all 3200 runs in a job, so that at any point
in time all 40 cores are busy, but not overloaded.

Next lines calculate which directories belong to the current array job, using
the `SLURM_ARRAY_TASK_ID` environment varible.

The main "loop" of the script is implemented with GNU parallel command
`parallel`. With the option `-j $SLURM_CPUS_PER_TASK` we tell GNU parallel to
keep running 40 commands (applications) in parallel. Since we need to copy
files into and out from the local SSD for each run, we wrap our application in a
small shell script, `wrapper.sh`, which takes the input file name as an
argument. The names of the input files are fed to GNU parallel through a pipe,
and GNU parallel keeps on running the `bash wrapper.sh <input file>` command as
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

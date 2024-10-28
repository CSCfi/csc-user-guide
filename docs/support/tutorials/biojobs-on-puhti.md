# Running your first job on Puhti

## Logging in

To prepare and run your jobs, you first need to log in to Puhti. You
can use either command line application or a special terminal
program. Command line applications come standard on most operating
systems. Terminal programs may need to be installed separately, but they
typically offer more options on things like font size, copy-paste etc.

On Linux or macOS open a terminal. In Windows 10 open Powershell. Give command:

```text
ssh yourcscusername@puhti.csc.fi
```
Where **yourcscusername** is the username you get from CSC.

You can find more detailed instructions in our User Guide: [Connecting
to CSC supercomputers](../../computing/connecting/index.md).


## What is Puhti?

Puhti, like most modern HPC (High Performance Computing) systems, is
a cluster computer. It means that is has a small number of login nodes
and a large number of compute nodes.

When you log in, you end up in one of the two login nodes. Login nodes
are meant for things like moving data and setting up and managing your
batch jobs. You should not run actual jobs on the login nodes. There
are only two login nodes and they are shared by everybody. Running big
jobs on them can make the system slow and unresponsive for all
(More details in our [usage policy](../../../computing/usage-policy)).

Jobs should be run in the compute nodes. This is done using the *batch
job system* also called a *scheduler* or a *workload manager*. The
system in use in Puhti is called [Slurm](https://slurm.schedmd.com/overview.html).

To run your job through the batch job system you use command **srun**
or write a batch jobs script and use command **sbatch**. We will
discuss this in more detail later.

To check what kind of compute nodes are available in Puhti, see the
User Guide: [Technical details about
Puhti](../../computing/systems-puhti.md).


## Software environment

Puhti has a selection of commonly used bioscience software
available. You can check the listing in
[Applications](../../apps/by_discipline.md#biosciences).

The application listing may not be quite up to date, so it is a good
idea to use **module spider** command to see if a software (and which
version) is available, *e.g*:

```text
module spider bowtie2
```

To avoid conflicts between different applications and versions, most
software on Puhti is installed as *modules*. To use an application you
will need to load the module, *e.g*:

```text
module load bowtie2
```
You can also specify a specific version, *e.g*:
```text
module load bowtie2/2.3.5.1
```
If you do not specify a version, the default version (typically latest
stable release) is loaded.

We also provide a module that loads many commonly used bioscience 
applications at once:
```text
module load biokit
```
The easiest way to see the content of the biokit module is to load it, and check the listing.
```text
module list
```

To see which modules to load, see the instruction page for each software

For more information on the module system, please see the user guide:
[The module system](../../computing/modules.md).


## Planning your job

To run a job through a batch job system, you will need to reserve
resources, *i.e.* cores, memory and time, suitable for the job. To
decide on the needed resources, you will have to answer some
questions:

### How many cores can my application use?

First a short note on terminology: When speaking about home computers
people usually use terms "processor" and "core". For example, most
modern home computers have one processor with two or more cores. When
speaking about HPC machines the corresponding terms are "socket" and
"CPU". For example, Puhti compute nodes have two sockets with 20 CPUs
each. This tutorial uses terms "processors/cores", as they are
probably more familiar for people without HPC background.

Applications can be divided into categories according to the amount 
of cores they can use:

- **Serial applications**
    - Can only use one core
    - Many bioscience applications belong to this category
    - If the application manual makes no mention of number of cores or 
      threads to use, the application is probably serial
    - Reserving more cores will not make these applications any faster, 
      as they can only use one
- **Shared memory/threaded/OpenMP applications**
    - Can use more than one core, but all cores must be in the same node 
      (so in Puhti max 40 cores)
    - Most bioscience applications that can use more than one core are 
      in this category
    - Also remember to tell the application the number of cores to use
    - Check the application documentation for correct command line options
    - Usually it is best to match the number of cores to the number of threads, 
      but check the application documentation 
- **MPI parallel applications**
    - Can use more than one core, cores need not be in the same node
    - Only very few bioscience applications in this category
- **Hybrid parallel applications**
    - A job where each MPI task is allocated several cores. Each task then 
      uses some other parallelization than MPI to do work. The most common strategy 
      is for every MPI task to launch multiple threads using OpenMP.
    - Quite rare in bioscience applications

To find out what category your application belongs to, read the documentation.

It should also be noted that more cores does not automatically mean
faster run time. Reserving too many cores can actually make the
software run slower. The optimal number of cores depends on the
application, data and the analysis performed. You should check the
application documentation to see if the developers give any
guidelines. It is also a good idea to run some tests with different
core numbers to see how well the application scales.


### How much memory does my application need?

Estimating the required memory can be quite difficult. In many cases
it is affected by the data and the application options chosen. Also
number of threads used can often effect the memory requirements.

You should read the application documentation to see if the developers
give any estimate. Often it is also helpful to check the user forums,
if the software has one.

Often, especially when running an application for the first time, you
just have to make a guess. If you get an error message about memory
running out, increase memory reservation and try again. If the job
finishes, you can check the actual memory usage and use that to make
the reservations in the future.

More information can be found in this FAQ entry: [How to estimate how
much memory my batch job
needs?](../faq/how-much-memory-my-job-needs.md)


### How much time should I reserve?

Knowing the run tme in advance can also be difficult if you are not
familiar with the application.

You should make sure to reserve enough, as the job will be stopped
when the time reservation runs out, whether it is finished or not.

On the other hand reserving too much time is not that big of a
problem. The job will finish when the last task of the job
finishes. Your job will only consume billing units according to the
actual elapsed time, not according to reservation.

It is OK to reserve the maximum time allowed in the partition you are
using when running an application first time. After the job finishes,
you can check the elapsed time, and make a more informed reservation
next time.


## Running your job

### Interactive jobs

Interactive jobs are good for things like testing, running small tasks
and for software that has a graphical user interface.

As mentioned, you should not run jobs in the login node. Instead you
can use **sinteractive** command to open an interactive shell:

```text
sinteractive -i
```
For more detailed instructions, see the User Guide: [Interactive usage](../../computing/running/interactive-usage.md)

Longer jobs that take more resources are best run as batch jobs.

### Batch jobs

Running a batch job typically has three steps:
1. Make sure you have all the necessary input files
    1. For instructions on how to move data from your own computer to Puhti, see section [Data/Moving data](../../data/moving/index.md) in the User Guide
2. Write a batch job script
    1. Use a text editor like nano, vim or emacs to write the script
    2. If you write the script on your own computer, and move it to 
       Puhti, some care should be taken. Make sure it is saved as text, 
       not as a Word doc or something like that. Also be aware that Windows 
       treats line endings differently than Linux, and this can cause problems.
3. Submit the job

Here is an example batch job script. It is saved as *myjobscript*
```text
#!/bin/bash
#SBATCH --job-name=bowtie2
#SBATCH --account=project_123456
#SBATCH --ntasks=1
#SBATCH --nodes=1  
#SBATCH --cpus-per-task=16
#SBATCH --mem=16g
#SBATCH --time=04:00:00
#SBATCH --partition=small

module load biokit
bowtie2 -p $SLURM_CPUS_PER_TASK -x genome -1 reads_1.fq -2 reads_2.fq > output.sam
```

All the lines staring with **#SBATCH** are passed on to the batch job
system. We use them to request the necessary resources.

Job name (--job-name) is mainly used to identify your job *e.g.* when
listing jobs with **squeue** or checking past jobs with **sacct**.

It is necessary to to inform the system which project should be
billed. This is done with **--account**. You can check the projects that
you belong to in [MyCSC](https://my.csc.fi/myProjects) or with `csc-projects`
in the command line.

Bowtie2 is a shared memory application. As discussed earlier that
means it can use more than one core, but all cores must be in the same
node. We specify that we want to run one task (--ntask=1) in one node
(--nodes=1) using 16 cores (--cpus-per-task):

```text
#SBATCH --ntasks=1
#SBATCH --nodes=1  
#SBATCH --cpus-per-task=16
```

Because it is a shared memory application we can use `--mem` to specify
the total memory requested for the task. For an MPI job we would have
to request memory per core with `--mem-per-cpu`.

```text
#SBATCH --mem=16G
```

The time reservation is given as hours:minutes:seconds *i.e.* `hh:mm:ss`. in
this case we reserve four hours:

```text
#SBATCH --time=04:00:00
```

We also need to specify which partition (also called a queue) we want 
the job to run in. This is specified with the `--partition` option. For 
most bioscience jobs "small" is the correct choice. It is for jobs that
run inside one node.

```text
#SBATCH --partition=small
```

You can check the available partitions in the User Guide: [Available
batch job partitions](../../computing/running/batch-job-partitions.md)

By default various outputs and error messages that would be printed to
the screen if the application was run interactively, are saved in a
file called *slurm-&lt;jobid&gt;.out*. Sometimes it is clearer to separate
the outputs and errors. This can be done adding options `--output` and
`--error`. The `%j` will be replaced by jobid of the job in the file name.

```text
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
```

There are also other available options. For a more detailed
explanation, please see the User Guide: [Creating a batch job script
for Puhti](../../computing/running/creating-job-scripts-puhti.md)

When you have written the batch job script, you can submit the job to the queue:
```text
sbatch myjobscript
```
If the job was submitted successfully, you should see a message:
```text
Submitted batch job <jobid>
```

It is possible to launch a job directly with command **srun** by
giving the options given as `#SBATCH` lines directly as command line
options, but writing a batch job script is generally preferable for
clarity and ease of re-use if you *e.g.* want submit a similar job with
different data or modified parameters.

### Array jobs

If you wish to run several instances of the same command with different 
input files or different set of parameters, you should consider running 
them as an array job. Array jobs offer an easy way to launch and manage 
a group of similar jobs.

Running array jobs is described in detail in the User Guide: 
[Array jobs](../../computing/running/array-jobs.md)

## Managing jobs

You can check your current jobs, both running and queueing:
```text
squeue -u <username>
```
Or  get a bit more detailed listing using:
```text
squeue -l -u <username>
```
You can check the status of your job in the column named ST or STATUS (depending
whether option -l is used or not). R or RUNNING means the job is currently running.
P or PENDING means it is still waiting in the queue.

If the job is pending, you can see the reason in the NODELIST(REASON) column. 

Reason:
```text
(Resources)
```
or
```text
 (Nodes required for job are DOWN, DRAINED or reserved for jobs in higher priority partitions)
```
mean that there are currently no available resources to run your job. The
job will run as soon as resources are free.

Reason:
```text
(Priority)
```
means your job is being held back by the fair share functionality of the 
batch job system: When a user runs many jobs in a short amount of time, their 
jobs will have lower priority. These jobs will spend a bit longer in the queue, 
but will be run eventually.

Queueing time will depend on the overall load on the system (*i.e.* how many jobs are in the 
queue before yours) and on the resource requirements of your jobs.

If it feels your jobs queue a long time, you might want to check this FAQ entry:
[Why is my batch job queueing so long?](../faq/why-is-my-job-queueing-so-long.md)

There are also other reasons, but they are less common. Consult **servicedesk@csc.fi** if necessary.

You can cancel a submitted batch job with:
```text
scancel <jobid>
```

## Monitoring resource usage

After the job has finished you can use commands **seff** and **sacct** to check the 
resources the job actually used.
```text
seff <jobid>
```

Most important things to check are the CPU efficiency and memory utilization.

There are many things that can cause poor CPU efficiency. It could, for example,
indicate that the program is waiting for disk access to catch up. In these cases
you should consider using a node with fast local disk.  For details, please see the User Guide: 
[Creating a batch job script for Puhti](../../computing/running/creating-job-scripts-puhti.md)

Low efficiency could also be due to reserving more than one core and the application
scaling poorly. Check especially if the percentage matches the number of cores reserved,
*e.g.* 25% with four cores or 12,5% with eight cores *etc*. This is typically due to the
application only using one core. Check if the application can really use more than one core, 
or if you have set the corresponding application parameter correctly. 

```text
CPU Efficiency: 12.48% of 06:56:08 core-walltime
```

Also check the actual utilized memory and set the memory reservation for the next run
accordingly, but leave some safety buffer, e.g. few GB. Fore example, in the following
job, the memory request has been way too large (92GB requested vs. 6GB used).

```text
Memory Utilized: 5.98 GB
Memory Efficiency: 6.25% of 92.59 GB
```

The other command to check the status and resource usage of past jobs is **sacct**. It is handy
when you want to see the status of many jobs (*e.g* all the subjobs of an array job).
Command **seff** will only show one job at a time.

```text
sacct
```
The information shown by default includes the state of the jobs (PENDING/RUNNING/COMPLETED/FAILED) 
and the jobid. 

You can also specify which fields to show with the -o option:
```text
sacct -o jobid,jobname,ntasks,ReqNodes,allocnodes,reqcpus,alloccpus,reqmem,maxrss,timelimit,elapsed,state -j <jobid>
```
By default **sacct** only shows jobs run on current date. You can select the start date
with option -S.
```text
sacct -S <YYYY-MM-DD>
```
Please note, that the `sacct` command is heavy on the queuing system, so don't build scripts that
run it repeatedly.

## Troubleshooting

### Getting familiar with a new program

Here are some useful steps when familiarizing yourself with a new program.

- Read the manual
- It may be helpful to first try run the program interactively to find the correct command line options
    - This allows to use `top` to get rough a estimate on memory use etc.
- If developers provide some test or example data, run it first
    - Make sure the results are as expected
- You can use the test partition to check your batch job script
    - Limits : 15 min, 2 nodes
    - Job turnaround usually very fast
    - Can be useful to spot typos, missing files *etc.* before submitting a job that will spend long in the queue
- Before very large runs, it’s a good idea do a smaller trial run
    - Check that results are as expected
    - Check resource usage after test run and adjust accordingly 
    - Try different core numbers and see how the software scales

### Troubleshooting checklist

Start with these if your job fails:

1. Did the job run out of time?
2. Did the job run out of memory?
3. Did the job actually use resources you specified?
    - Problems in the batch job script can cause parameters to be ignored and default values getting used instead
4. Did it fail immediately or did it run for some time?
    - Jobs failing immediately are often due to something simple like 
      typos in command line, missing inputs, bad parameters *etc.*
5. Check the error file captured by the batch job script
6. Check any other error files and logs the program may have produced
7. Error messages can sometimes be long, cryptic and a bit intimidating, 
   but try skimming through them and see if you can spot something 
   ”human readable” instead of ”nerd readable”
    - Often you can spot the actual problem easily if you go through the 
      whole message. Something like ”required input file so-and-so missing” 
      or ”parameter X out of range” *etc.*

If you can't figure it out, please don't hesitate to contact us at
**servicedesk@csc.fi**. Remember to include relevant information like what
program you were trying to run on which server etc.


#Batch job Basics 

[TOC]


CSC uses a batch job systems to execute computing tasks on our supercomputers. 

This chapter goes through the basics of creating and submitting batch jobs using the SLURM (Simple Linux Utility for Resource Management) batch job system. 

**The key concepts of the CSC batch job system:**

- Jobs do not run instantly, but are put in a queue
    - Jobs are executed when there are availabe resources and depending on a priority score 
    - The priority score for a job exists to ensure fair sharing of computational resources between all the users of the cluster

- The start time for a job can't be predicted
    - Depends heavily on acctual runtimes for all user jobs and submission of new jobs

- Computational resources (runtime, memory, number of cores, etc. ) are requested explicitly.

- If you go over the time or memory limit, your job will terminated.



## Creating a batch job file

A batch job file will contain definitions for resources to be reserved for the job and the commands the user wants to run. 

An example of a simple batch job file.

```
/bin/bash -l
#SBATCH --job-name=myTest
#SBATCH --account=project_<project_id>
#SBATCH --partition=serial
#SBATCH --time=02:00:00
#SBATCH --mem-per-cpu=2G

module load myprog/1.2.3

myprog -i input -o output
```
The first line with `/bin/bash -l` tells that the file should be interpreted as a bash script (the `-l` flag invokes a login shell, which is
needed for the module system to work properly) . 

Lines starting with `#SBATCH` are arguments to the batch system.  
We will present some of the options, for a list of all possible options,
see the [slurm documentation](https://slurm.schedmd.com/srun.html).

The general syntax  is:
```
#SBATCH option_name argument
```

```
#SBATCH --jobname=myTest
```
sets the name of the job.
It can be used to identify a job in the queue and other listings. 
```
#SBATCH --account=project_<project_id>
```
sets the billing project for the job. **This argument is mandatory, failing to set it will cause your job to be held with 
the reason "_AssocMaxJobsLimit_"** 
You can check you projects in [My CSC](https://my.csc.fi) in the "My Projects" tab. 

The partition i.e. queue needs to be set according to the job requirements.
```
#SBATCH --partition=serial
```
Different queues have different limits and available resources. 


_Information about the different queues:_

| Queue		     |  Time Limit   |Job node limit | Number of nodes | Memory | Cores/GPUs node   |
|----------------|---------------|---------------|-----------------|--------|-------------------|
|Serial\*\*      |  3 days       | 1 node        |     532         | 190G   | 40 cores          |
|	             |               |               |     132          | 382G   |                   |
|                |               |               |     12          | 764G   |                   |
|parallel\*\*    |  3 days       | 100 nodes     |     532         | 190G   | 40 cores          |
|                |               |               |     132          | 382G   |                   |
|                |               |               |     12          | 764G   |                   |
|hugemem         |  3 days       |  1 node       |     6           | 1532G  | 40 cores          |
|gputest         |  30 minutes   |  2 nodes      |     2           | 382G   | 40 cores + 4 GPUs |
|gpu             |  3 days       |  160 GPUs     |     78          | 382G   | 40 cores + 4 GPUs |


Time reservation is set with option `--time`

```
#SBATCH --time=10:00:00
```
Time is given in format __hh:mm:ss__ (optionally __d-hh:mm:ss__, where __d__ is days). Maximum time depends on the queue selected. When time reservation ends, the job is terminated whether it is finished or not, so time reservations should be sufficient. Job will consume billing units according to it's actual runtime. 

```
#SBATCH --mem-per-cpu=2G
```
sets the required memory per requested cpu-core. If you go over the requested memory, your job will be terminated. 

```
module load myprog/1.2.3 
```
Is needed to make the right modules available for the jobs. For more information about
modules see [modules](/this/link/is/broken).


The example batch script file above runs the command  

```
myprog -i input -o output 
```
on one node using a single core. Multiple commands can be run in one batch script.




To run programs using multiple cores and nodes see the following sections:

- [Serial and Thread Based Batch Jobs](serial-and-thread-based-batch-jobs.md)
- [MPI Based Bath Jobs](mpi-batch-jobs.md)
- [Array jobs](array-jobs.md)


##Running Batch Jobs
A batch job is submitted to the queue with command
```
sbatch <batch_job_file>
```
When the job is successfully launched, the command prints out a line, telling the ID number of the submitted job.

To check that the job was submitted correctly use command
```
squeue -u <username>
```
A submitted batch job can be cancelled with:
```
cancel <jobid>
```

You can also submit jobs directly from the commandline using 
```
srun [OPTIONS] [EXECUTABLE] [EXECUTABLE ARGUMENTS] 
```
The same options define with `#SBATCH` are usable with `srun`.

!!! Note
    When using `srun` directly the command only returns once the job has been completed. 
    If you interrupt the command or lose your connection, the job will be canceled. Due to this 
    we do not recomend using srun directly for any larger jobs. 



More information on running and managing batch jobs in [Managing Batch Jobs](managing-batch-jobs.md).


# Batch Job Basics
##Batch jobs
CSC uses batch job systems to execute computing tasks in clusters and supercomputers. In this chapter we provide introduction to the SLURM (Simple Linux Utility for Resource Management) batch job system that is used in CSC supercomputers.

Batch job systems are essential for effective usage of large computing servers. First of all, the batch job system takes care that the server does not get overloaded: Users can submit large amounts of jobs to be executed and the batch job system takes automatically care that optimal number of jobs are running, while rest of the jobs are queueing until sufficient resources are available. Further, most of the batch job systems have a "fair share" functionalities that take care that, on the long run, all the users get equal possibilities to use resources. For example in a case where user A has submitted 500 jobs before user B submits his job, the user B don't have to wait that all the jobs of user A have been processed. Instead, the batch job system gives higher priority to the job of user B compared to user A, as user A is already using much more computing resources that user B.

When a batch job system is used, the commands to be executed are not started immediately like in normal interactive usage. Instead the user creates a file that contains the Linux commands to be executed. In addition to the commands, this so called batch job file normally contains information about the resources that the job needs (for example: required computing time, memory and number of cores). The batch job file is submitted to the batch job system with a job submission command. After that the batch job system checks the resource requirements of the job, sends the job to a suitable queue and starts the job when sufficient resources are available. If the job exceeds the requested values (e.g. requires more computing time than what was requested) the batch job system kills the job. After job submission, user can follow the progress of the job or cancel the job if needed.

##Batch job file

A typical batch job file will contain definitions for resources to be reserved for the job and the actual commands user wants to run. 

An example of a simple batch job file.

```
/bin/bash -l
#SBATCH --job-name=myTest
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
#SBATCH --account=project_<project_id>
#SBATCH --partition=serial
#SBATCH --time=02:00:00
#SBATCH --tasks=1
#SBATCH --mem=6000

module load myprog/1.2.3
myprog -i input -o output
```

The batch job file starts with a shebang line:

```
#!/bin/bash -l
```
I tells the computer the file should be executed as bash script. Option `-l` makes bash act as if it was invoked as a login shell. It is needed to make sure things like the module system work as expected.

The shebang line is followed by a number of lines starting with #SBATCH. These lines are passed on to the batch job system. They should have all the resource reservations and any other instructions necessary. 

Instead of adding them to the batch job file, it is also possible to to give them as command line option for the job submit command. In most cases it is preferable to include them in the batch job file: It makes it easier to check what parameters were used and it also makes it easier to re-use the file.

The general syntax for these lines is:
```
#SBATCH option_name argument
```
Most options have a short one letter name, and a longer, more descriptive, name. The actual syntax depens on whether using the short or long names. For example these two lines mean the same:
```
-J jobname
--job-name=jobname
```
This guide will use the long names for consistency's sake, but they are identical in function and choice is up to user preferences.

Option <var>--jobname</var> sets the name of the job.
```
#SBATCH --jobname=myTest
```
It can be used e.g. to identify a job in the queue. It should be noted that the name can be truncated in the listings, so it is a good idea to keep the name short, or include the identifying part in the beginning of the name.

The next two lines capture the stdout and stderr to a file:
```
#SBATCH --output=output_%j.txt
#SBATCH --error=errors_%j.txt
```
Stdout and stderr comprise the text that would be printed to screen if the program was run in interactive mode. Typically normal output goes to stdout and error messages go to stderr, but it depends on the program. It is a good idea to always capture at least stderr (option `--error`) as it is helpful in trobleshooting failed jobs. It also a good idea to include `%j` to the file name. It will be replaced with the job ID number in the actual file name. This way the files will not get accidentally overwritten by other jobs. It will also preserve the job ID, which is useful in troubleshooting, checking the resource usage after the job is finished, etc.

The next options set the billing project for the job. 
```
#SBATCH --account=project_<project_id>
```
You can check you projects in [My CSC](https://my.csc.fi) in the "My Projects" tab. Current project can be checked with command:
```
id -gn
```

The partition i.e. queue needs to be set according to the job requirements.
```
#SBATCH --partition=<partition>
```

Time resevation is set with option `--time`
```
#SBATCH --time=10:00:00
```
Time is given in format __hh:mm:ss__. Maximum time depends on the queue selected. When time reservation ends, the job is terminated whether it is finished or not, so time reservations should be sufficient. Job will consume billing units according to it's actual runtime. On the other hand too long time reservations can cause the job to spend longer in the queue.


The next set of options set the number of cores and nodes to use. They depend on the type of job and are discussed in more detail in the job type specific articles:

- [Serial and Thread Based Batch Jobs](serial-and-thread-based-batch-jobs.md)
- [MPI Based Bath Jobs](MPI-batch-jobs.md)
- [Array jobs](array-jobs.md)


##Running batch jobs
A batch job is submitted to the queue with command
```
sbatch <batch_job_file>
```

To check that the job was submitted correctly use command
```
squeue -u <username>
```
A submitted batch job can be cancelled with:
```
scancel <jobid>
```
More information on running and managing batch jobs in [Managing Batch Jobs](managing-batch-jobs.md).
# Managing Batch Jobs

The basic SLURM commands for submitting batch jobs are `sbatch` that submits jobs to batch job system and `scancel` that can be used to stop and remove a queueing or a running job. The basic syntax of the sbatch command is:
```
sbatch -options batch_job_file
```
Normally the sbatch options are included in the batch job file, but you can use the options in command line too. For example:
```
sbatch --jobname test2 --time 00:05:00 batch_job_file.sh
```
If the same option is used both in command line and in the batch job file, the value defined in the command line overrides the value in the batch job file. 

When the job is successfully launched, the command prints out a line, telling the ID number of the submitted job. For example:
```
Submitted batch job 6594 
```
The job ID number can be used to follow the progress of the job or to remove it. For example, a job with ID 6594 can be removed from the batch job system with command:
```
scancel 6594
```
Progress of the submitted batch jobs can be followed with commands `squeue`, `sjstat` and `sacct`. These commands can also be used to check the status and parameters of the batch job environment.

By default `squeue` command lists all the jobs which are submitted to the SLURM scheduler. If you want to see status of your own jobs only, you can use command:
```
squeue -l -u username
```
or
```
squeue -l -u $USER
```
You can also check the status of a specific job by defining the jobid with `-j` switch. Using option `-p <partition>` will display only jobs on that SLURM partition.

Command `scontrol` allows to view SLURM configuration and state. To check when the job waiting in the queue will be executed, the command: 
```
scontrol show job <jobid> 
```
can be used. A row "StartTime=..." gives an estimate on the job start-up time. It may happen that the job execution time can not be approximated, in which case "StartTime= Unknown". Note, that the "StartTime" may change, e.g., be shortened, as the time goes.

The `sacct` command can be used to study the log file of the batch job system. Thus it can show information about both active jobs and jobs that have already finished. By default the sacct command shows information about users' own jobs. The sacct command has a wide selection of options and parameters that can be used to select the data to be displayed. 

By default sacct displays information from the time period that starts from the midnight of current day. You can change the starting date with option `-S YYYY-MM-DD`. For example, to list the information since first of August 2019 you can use command:
```
sacct -S 2019-08-01
```
Information about specific jobs can be checked with option `-j <jobid>`. For example detailed information about job number 6594 could be shown with command:
```
sacct -S 2013-02-01 -j 6594 -l 
```
Quite often the full listing (`-l`) of the job information is not desirable. To choose only specific information, you can use option `-o` combined with the list of fields to display. For example:
```
[kkayttaj@taito-login4~]$ sacct -j 6594 -o MaxRSS,AveRSS,ReqMem,Elapsed,AllocCPUS
    MaxRSS     AveRSS     ReqMem    Elapsed AllocCPUS
---------- ---------- ---------- ---------- ---------
                          2347Mc   02:01:49         4
  3480116K   3480116K     2347Mc   02:01:49         1
```
In the example above, the listing shows that job 6594 used 3.5 GB (3480116 KB) of memory and lasted 2 hours, 1 minute and 49 seconds. This information could then be used to optimize batch job parameters for other similar jobs.

When a batch job has finished it is good to run `seff` command to check the efficiency of your job. The syntax of the seff command is:
```
seff jobid
```
A sample session below shows a case where a job (job_id: 54321) took 49 min and 19 s and used the reserved CPU-resources rather efficiently (98.68% efficiency). In the cases of memory, nearly 40 GB was reserved but  only bit over 4 GB was used in maximum. Thus for a second similar job, the user should consider decreasing the memory reservation.
```
[kkayttaj@taito-login4~] seff 54321
Job ID: 54321
Cluster: csc
User/Group: kayttaj/somegroup
State: COMPLETED (exit code 0)
Cores: 1
CPU Utilized: 00:48:40
CPU Efficiency: 98.68% of 00:49:19 core-walltime
Memory Utilized: 4.06 GB
Memory Efficiency: 10.39% of 39.06 GB
```

## Most frequently used SLURM commands.

| Command   | Description   |
| ---   | ---  |
| sacct   | Displays accounting data for all jobs.   |
| salloc   | Allocate resources for interactive use.   |
| sbatch   | Submit a job script to a queue.   |
| scancel   | Signal jobs or job steps that are under the control of SLURM (cancel jobs or job steps).   |
| scontrol   | View SLURM configuration and state.   |
| seff   | View the CPU and memory efficiency (real usage compared to the reserved resources)   |
| sinfo   | View information about SLURM nodes and partitions.   |
| sjstat   | Display statistics of jobs under control of SLURM (combines data from sinfo, squeue and scontrol).   |
| smap   | Graphically view information about SLURM jobs, partitions, and set configurations parameters.   |
| squeue   | View information about jobs located in the SLURM scheduling queue.   |
| srun   | Run a parallel job.   |


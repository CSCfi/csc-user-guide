# Submitting a batch job

A batch job is submitted to the queue with the command
```
sbatch <batch_job_file>
```
When the job is successfully launched, the command prints out a line, telling
the ID number of the submitted job.

To check that the job was submitted correctly use command
```
squeue -u <username>
```
A submitted batch job can be cancelled with:
```
scancel <jobid>
```

To view information about your jobs use:

```
sacct
```
The information includes the state of the jobs (PENDING/RUNNING/COMPLETED/FAILED) and JobID. 


By default the `sacct` command shows information about users' own jobs. 
The `sacct` command has a wide selection of options and parameters that can be used to select the data to be displayed.
The full set of options and parameters are described [here](https://slurm.schedmd.com/sacct.html).

# Submitting a batch job

Submit to the queue:
```
sbatch <batch_job_file>
```
When the job is successfully launched, the command prints out the ID number of the submitted job.

Check that the job was submitted correctly:
```
squeue -u <username>
```
Cancel a submitted batch job with:
```
scancel <jobid>
```
Information about your jobs:
```
sacct
```
The information includes the state of the jobs (PENDING/RUNNING/COMPLETED/FAILED) and the JobID. 

By default, the `sacct` command displays information about the users' own jobs. It also has a wide selection of options and parameters that can be used to select which data is displayed.

[All options and parameters](https://slurm.schedmd.com/sacct.html).

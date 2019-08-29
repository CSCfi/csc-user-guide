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




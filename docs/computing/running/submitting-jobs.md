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
cancel <jobid>
```

You can also submit jobs directly from the commandline using
```
srun [OPTIONS] [EXECUTABLE] [EXECUTABLE ARGUMENTS]
```
The same options defined with `#SBATCH` are usable with `srun`.

!!! Note
    When using `srun` directly the command only returns once the job has been
    completed. If you interrupt the command or lose your connection, the job
    will be canceled. Due to this we do not recommend using srun directly for
    any larger jobs.

More information on managing batch jobs can be found in
[Managing Batch Jobs](managing-batch-jobs.md).

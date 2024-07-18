# Submitting a batch job

Submit a job to the queue with command `sbatch`:

```bash
sbatch <batch_job_file>
```

For example:

```bash
sbatch job.sh
```

When the job is successfully submitted, the command prints out the ID number of
the submitted job. For example, `Submitted batch job 3609650`.

To check if your job is running correctly:

```bash
squeue -u $USER
```

or

```bash
squeue --me
```

You should see your job ID and other details displayed in the terminal.

To cancel a submitted batch job:

```bash
scancel <jobid>
```

For example,

```bash
scancel 3609650
```

To find out more about your jobs:

```bash
sacct
```

The information includes the state of the jobs (`PENDING`, `RUNNING`,
`COMPLETED`, `FAILED`, etc.) and the job ID. By default, the `sacct` command
displays information about a user's own jobs that have been submitted to the
queue on the current date. It also has a wide selection of options and
parameters that can be used to select which data is displayed. 
[See all `sacct` options and parameters](https://slurm.schedmd.com/sacct.html).

!!! warning "Avoid querying too much data with `sacct`"
    Do not query job data from a long time period with `sacct`. `sacct` fetches
    its data from the Slurm accounting database, and with large queries the
    operation can be heavy on the system. In particular, avoid running the
    command many times in a row. Instead, you can redirect the output data to a
    file and then search that for whatever information you want to analyze.
    For example, to save the data from the past 7 days in a file
    `sacct-output.txt`:

    ```bash
    sacct --starttime now-7days > sacct-output.txt
    ```

## More information

- [Creating Puhti batch jobs](creating-job-scripts-puhti.md)
- [Creating Mahti batch jobs](creating-job-scripts-mahti.md)
- [Available batch job partitions](batch-job-partitions.md)

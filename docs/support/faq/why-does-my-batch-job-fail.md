# Why does my batch job fail?

Below are common error messages you may get when the job fails, and advice how
to fix them.

## Invalid account or account/partition combination specified

The complete error message is as shown below:

```text
sbatch: error: Batch job submission failed: Invalid account or account/partition combination specified
```

This error message refers to Slurm options `--account=<project>` and
`--partition`. The most common causes are:

* Project does not exist.
* Project exists, but you are not a member of it. See how to
  [add a member to project](../../accounts/how-to-add-members-to-project.md)
* You are a project member, but the project has not been enabled on Puhti. See
  how to
  [add service access for project](../../accounts/how-to-add-service-access-for-project.md).
* Partition does not exist.
* Partition exists, but your project is not enabled in it.

## Job violates accounting/QOS policy

The complete error message is as shown below:

```text
sbatch: error: AssocMaxSubmitJobLimit
sbatch: error: Batch job submission failed: Job violates accounting/QOS policy (job submit limit, user's size and/or time limits)
```

The most common causes are:

* Job script is missing the `--account` parameter.
* Your project has too many jobs in the system, either running or queuing.
  Note that internally, Slurm counts each job within an array job as a separate
  job.
* The job was executed directly `./script_name.sh` or `bash script_name.sh`,
  while it should be submitted with `sbatch script_name.sh`.


## Requested node configuration is not available

The complete error message is as shown below:

```text
sbatch: error: Batch job submission failed: Requested node configuration is not available
```

The most common causes are:

* Requesting e.g. a GPU or NVMe in a partition that does not have them.
* Requesting e.g. more memory or time than the chosen partition has to offer. Especially if
  using the `--mem-per-cpu` flag to specify memory, note that this will be multiplied by the
  number or requested CPUs (1 per task by default) and the result must be within the limits
  of the chosen partition.

See [batch job partitions](../../computing/running/batch-job-partitions.md) for more details
on the resources available in each queue.

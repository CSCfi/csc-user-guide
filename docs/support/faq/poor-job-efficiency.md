# The login banner says my job efficiency is poor. What should I do?

The [efficiency banner](../../computing/performance.md#efficiency-banner-at-login)
shown when you log in to Roihu rates your job efficiency as _poor_ when your
jobs used on average less than 50% of the resources they reserved over the last
month. The efficiency of a job is the highest of its CPU, memory and GPU
efficiency, so a job only gets a low value when it left all of its reserved
resources mostly unused. Every job counts equally, whatever its size or length.

The rating is a monthly average, so it improves gradually as your new, more
efficient jobs replace the old ones. The banner is updated at most once an
hour.

## Find the inefficient jobs

Open the [Job monitoring app](../../computing/performance.md#job-monitoring-app)
from _Jobs_ > _Job monitoring_ in the Roihu web interface. It lists your jobs
from the last 60 days, with efficiency values below 50% shown in red. Select a
job ID to see how the job used its resources over time.

You can also check a single job with
[`seff`](../../computing/performance.md#quick-start-efficiency-report-with-seff):

```bash
seff <JOBID>
```

## Common causes and fixes

* **The program uses fewer cores than you reserved.** Reserving more cores
  does not speed up a program that is not parallelized. If the program is
  parallel, tell it how many cores to use, for example by setting its threads
  option to `$SLURM_CPUS_PER_TASK`, as some programs use only one core by
  default. See
  [Serial and shared memory batch jobs](../../computing/running/creating-job-scripts-roihu.md#serial-and-shared-memory-batch-jobs).
* **The program does not scale to the number of cores you reserved.** Run a
  [scaling test](../../computing/running/performance-checklist.md#perform-a-scaling-test)
  to find a core count the program can use efficiently.
* **You reserved much more memory than the job needs.** See
  [How to estimate how much memory my batch job needs?](how-much-memory-my-job-needs.md)
* **You reserved whole nodes for a job that uses only part of them.** Use the
  `small` partition, where you can reserve only the cores and memory you need.
  See [Available batch job partitions](../../computing/running/batch-job-partitions.md).
* **The GPUs are idle much of the time, or the job uses only one of several
  GPUs.** A common reason is that the CPUs cannot load the data fast enough.
  See [GPU utilization](../tutorials/ml-guide/gpu.md#gpu-utilization) in the
  machine learning guide. If your program cannot use GPUs, run it on the CPU
  partitions.
* **The job spends its time waiting for the file system.** High I/O wait in the
  Job monitoring app is a sign of this, often caused by reading or writing many
  small files. Use [fast local storage](local_scratch_for_data_processing.md)
  instead, and see
  [Mind your I/O](../../computing/running/performance-checklist.md#mind-your-io-it-can-make-a-big-difference).
* **You run many short jobs.** Short jobs spend a large part of their run time
  starting up, for example loading modules and data. Run many small tasks
  within one job instead, see
  [High-throughput computing and workflows](../../computing/running/throughput.md).

If you cannot find the cause, [contact CSC Service Desk](../contact.md). For
larger efforts, see the
[CSC optimization service](../../computing/performance.md#csc-optimization-service).

## More information

* [Performance analysis](../../computing/performance.md)
* [Performance checklist](../../computing/running/performance-checklist.md)

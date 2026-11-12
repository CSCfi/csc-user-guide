# Performance Analysis

Roihu has three ways to check how efficiently your jobs use the resources they
reserved:

* The [`seff` command](#quick-start-efficiency-report-with-seff) summarizes the
  CPU, memory and GPU use of a single job and the billing units it consumed.
* The [Job monitoring app](#job-monitoring-app) in the Roihu web interface shows
  how your finished jobs used their resources over time.
* The [efficiency banner](#efficiency-banner-at-login) shown when you log in
  summarizes the efficiency of all your recent jobs.

## Quick Start: Efficiency Report with seff

Slurm job efficiency report (command: `seff`) gives a quick summary of
requested and used resources for both running and finished batch jobs. 

```bash
seff <JOBID>
```

It is an easy way to get an overall picture of how efficiently the CPUs were
used (CPU Efficiency) and how much of the allocated memory was actually used
(Memory Efficiency).

!!! note inline end "Hint"
    You may add the `seff` command to the end of your batch job script to
    always get an efficiency report for your jobs:

    ```bash
    seff $SLURM_JOBID
    ```

    The job is still running at that point, so the report only includes the
    job steps that have already finished (those started with `srun`). Run
    `seff` again after the job has ended to get the complete figures.

```console title="Example output for a single node job"
[kkayttaj@roihu-cpu-login2 perf]$ seff 307386
Job ID: 307386
Cluster: roihu
Partition: medium
User/Group: kkayttaj/kkayttaj
State: COMPLETED (exit code 0)
Nodes: 1
Cores per node: 384
CPU Utilized: 2-09:05:29
CPU Efficiency: 92.44% of 2-13:45:36 core-walltime
Job Wall-clock time: 00:09:39
Memory Utilized: 76.45 GB (estimated maximum)
Memory Efficiency: 10.27% of 744.72 GB (744.72 GB/node)
Job consumed 46.32 CSC billing units, billed on CPU usage
Billed project: project_2001234
CPU usage: 46.32 CPU BU
Mem usage: 0.00 CPU BU
```

## Understanding the seff output

- **Job ID, Cluster, Partition, User/Group and State** are identifying metadata.
  `State: COMPLETED (exit code 0)` confirms the job ran to completion without
  error. A nonzero exit code would be the first thing to check before looking
  at efficiency values at all.

- **Nodes / Cores per node** shows how many nodes and cores per node were
  allocated. In this example, `1 node x 384` cores means the job got a full
  Roihu CPU node.

- **CPU Utilized** is the *total* CPU time consumed, summed across every core,
  expressed as `d-hh:mm:ss`. This is not to be mistaken with wall-clock time,
  which does not account for individual cores.

- **CPU Efficiency** is `CPU Utilized` divided by core-walltime, where
  core-walltime is cores allocated multiplied by wall-clock time. This metric
  answers the question: of all the CPU-seconds allocated, how many were
  actually doing work?

- **Job Wall-clock time** is the actual elapsed time the job ran, independent
  of core count. Compare this against your `--time` request and for applications
  like GROMACS, against `-maxh`.

- **Memory Utilized / Memory Efficiency** shows peak memory used versus what was
  reserved. High memory efficiency values are especially important on core-based
  partitions like `small`, where jobs share a node and unused reserved memory
  can't be used by other jobs, increasing queue times. If the job ran several
  tasks, `seff` estimates the peak as the peak of the largest task multiplied
  by the number of tasks, and marks it `(estimated maximum)`. Note that `seff`
  reports memory in GiB, although it labels the values GB.

- **Billing Units** shows how the job was charged, and which resource determined
  the price. Up to date information about billing units can be found on the
  [Billing page](./hpc-billing.md). Local scratch reserved with `--gres=nvme`
  is shown on its own `NVME usage` line. Reserved
  [disaggregated storage](disk.md#disaggregated-storage) is not yet included
  in the `seff` figures, although it is billed.

### GPU jobs

Jobs on the GPU partitions are billed for the reserved GPUs only, so `seff`
shows a `GPU usage` line instead of the CPU and memory lines. It also adds a GPU
efficiency report with the mean, standard deviation and maximum of the load and
memory use of each GPU, and the energy each GPU used. The GPU figures come from
the job monitoring system, so they are also available for running jobs. If
there is no monitoring data for the job, for example because it was very
short, the report says `GPU Efficiency: not available`.

See the machine learning guide for examples of the
[GPU load and memory](../support/tutorials/ml-guide/gpu.md#tools-for-monitoring-gpu-utilization)
and [GPU energy](../support/tutorials/ml-guide/gpu.md#tools-for-monitoring-gpu-energy-usage)
output.

## Job monitoring app

Roihu records the resource use of each job at 10-second intervals. The
[Job monitoring app](webinterface/index.md#job-monitoring) in the
[Roihu web interface](https://www.roihu.csc.fi) shows this data for your
finished jobs, so you can see not only how much of its resources a job used,
but also how the use changed over the job's lifetime. Open the app from _Jobs_ >
_Job monitoring_ in the top navbar.

The app lists your completed jobs from the last 60 days with their efficiency:

* **CPU %** is the average share of time the reserved CPU cores were busy.
* **Mem %** is the peak memory use as a share of the reserved memory.
* **GPU %** is the average load of the reserved GPUs.

Values below 50% are shown in red, values from 50% to 75% in yellow and values
of 75% or more in green.

Select a job ID to open the report for that job. The report starts with a table
of the resources the job had on each node, how much of them it used and the
resulting efficiency. Above the table, the report tells you whether your
resource requests need attention:

* GPU jobs are assessed on their GPU load only, as the GPUs are what the job is
  billed for.
* Jobs that reserve part of a node should use at least 75% of both their CPU
  cores and their memory, as the reserved resources are not available to other
  jobs.
* Jobs that reserve whole nodes are flagged only if both their CPU and memory
  efficiency are below 75%, as no other job can use the rest of the node anyway.

Below the table, charts show the use of each resource during the job: GPU load,
memory and power, CPU load per node and per core, IO wait, and memory use. They
help you find problems that a single efficiency value hides, for example a job
that only uses one of its GPUs, or a job that spends long periods waiting for
the file system (high IO wait) instead of computing.

Reports become available a few minutes after a job has finished. Jobs that ran
for less than a minute are not recorded, and you can only see your own jobs.

Compared with `seff`, the app shows how the resource use changed over time,
while `seff` reports the totals Slurm records for the job, including the billing
units. As they measure the use in different ways, their efficiency values can
differ slightly.

## Efficiency banner at login

When you log in to Roihu with SSH, a banner summarizes the efficiency of your
jobs over the last week, the last month and all time:

```text
┏━━━ Efficiency ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                             ┃
┃ Your job efficiency: ● good                                                 ┃
┃                                                                             ┃
┃     All time:   412 jobs,   301 efficient jobs,  71.3% average efficiency   ┃
┃   Last month:    58 jobs,    47 efficient jobs,  76.8% average efficiency   ┃
┃    Last week:    12 jobs,    10 efficient jobs,  81.2% average efficiency   ┃
┃                                                                             ┃
┃ Job reports at: https://roihu.csc.fi/pun/sys/dashboard/custom/job_table     ┃
┃ For help:       https://docs.csc.fi/support/contact/                        ┃
┃                                                                             ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```

The banner uses the same data as the [Job monitoring app](#job-monitoring-app):

* The efficiency of a job is the highest of its CPU, memory and GPU efficiency.
  The banner currently is generous in its assessment, counting a job towards the efficient totals when this is at least 50%. This will likely be raised in the future.
* The rating at the top is based on your average efficiency over the last
  month: good for 75% or more, average for 50% or more, and poor below that. If
  you had no jobs last month, the rating uses your all-time average.
* Jobs on the `interactive` and `gpuinteractive` partitions are not counted,
  as interactive sessions mostly wait for user input.

To keep logins fast, the banner is shown from a saved copy that is updated in
the background at most once an hour. It therefore shows the figures from an
earlier login, and it is not shown at your first login.

Open the Job monitoring app to see which jobs used their resources poorly.

To get more detailed information about the performance of your program, you
should use one of the profiling tools available (see below).

## Profiling tools

Good profiling tools may help one to get a full picture of the computational
and communication patterns of a program and to identify potential performance
bottlenecks. At CSC, several profiling tools are available:

* [Scalasca](../apps/scalasca.md) is trace-based parallel performance analysis tool for MPI,
  OpenMP and hybrid MPI+OpenMP programs
* [cProfile](../apps/cProfile.md) is the recommended, in-built profiling tool
  for Python programs
* [nsys](../apps/nsys.md) is the command-line interface of Nsight Systems a system-wide performance analysis tool designed to visualize an application’s algorithms
* [ncu](../apps/ncu.md) is the command-line interface of Nsight Compute, a tool to debug and optimize CUDA kernels

## CSC optimization service

CSC application specialists can support you in improving the performance of your scientific computations, from small scripts to large software package. Smaller optimization requests are typically handled through the regular user support, while more extensive efforts may require establishing a funded development project. Read more about the service at [research.csc.fi](https://research.csc.fi/sciences/code-optimization/)

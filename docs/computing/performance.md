# Performance Analysis

## Quick Start: Efficiency Report with seff

Slurm job efficiency report (command: `seff`) gives a quick summary of
requested and used resources for both running and finished batch jobs. 

```bash
seff <JOBID>
```

It is an easy way to get an overall picture of how efficiently the CPUs were
used (CPU Efficiency) and how much of the allocated memory was actually used
(Memory Efficiency).

!!! note "Hint"
    you may add the `seff` command to the end of your batch job script to
    always get an efficiency report for your jobs: `seff $SLURM_JOBID`

Example output for a single node job:

```bash
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
Billed project: project_2001659
CPU usage: 46.32 CPU BU
Mem usage: 0.00 CPU BU
```

## Understanding the seff output

**Job ID, Cluster, Partition, User/Group and State** are identifying metadata.
`State: COMPLETED (exit code 0)` confirms the job ran to completion without
error. A nonzero exit code would be the first thing to check before looking
at efficiency values at all.

**Nodes / Cores per node** shows how many nodes and cores per node were
allocated. In this example, `1 node x 384` cores means the job got a full
Roihu CPU node.

**CPU Utilized** is the *total* CPU time consumed, summed across every core,
expressed as `d-hh:mm:ss`. This is not to be mistaken with wall-clock time,
which does not account for individual cores.

**CPU Efficiency** is `CPU Utilized` divided by core-walltime, where
core-walltime is cores allocated multiplied by wall-clock time. This metric
answers the question: of all the CPU-seconds allocated, how many were
actually doing work?

**Job Wall-clock time** is the actual elapsed time the job ran, independent
of core count. Compare this against your `--time` request and for applications
like GROMACS, against `-maxh`.

**Memory Utilized / Memory Efficiency** shows peak memory used versus what was
reserved. High memory efficiency values are especially important on core-based
partitions like `small`, where jobs share a node and unused reserved memory
can't be used by other jobs, increasing queue times.

**Billing Units** shows how the job was charged, and which resource determined
the price. Up to date information about billing units can be found on the
[Billing page](./hpc-billing.md).

To get more detailed information about the performance of your program, you
should use one of the profiling tools available (see below).

## Profiling tools

Good profiling tools may help one to get a full picture of the computational
and communication patterns of a program and to identify potential performance
bottlenecks. At CSC, several profiling tools are available:

* [Intel VTune Profiler](../apps/vtune.md) is a powerful profiler that can be
  used to collect performance data of your application and is suited for both
  serial and multithreaded codes
* [Scalasca](../apps/scalasca.md) is trace-based parallel performance analysis tool for MPI,
  OpenMP and hybrid MPI+OpenMP programs
* [Intel Trace Analyzer and Collector](../apps/itac.md) is a MPI profiling and
  tracing tool for parallel programs
* [cProfile](../apps/cProfile.md) is the recommended, in-built profiling tool
  for Python programs
* [nvprof](../apps/nvprof.md) is a command-line CUDA profiler and tracing tool
  for CUDA programs
* [nsys](../apps/nsys.md) is the command-line interface of Nsight Systems a system-wide performance analysis tool designed to visualize an application’s algorithms
* [ncu](../apps/ncu.md) is the command-line interface of Nsight Compute, a tool to debug and optimize CUDA kernels

## CSC optimization service

CSC application specialists can support you in improving the performance of your scientific computations, from small scripts to large software package. Smaller optimization requests are typically handled through the regular user support, while more extensive efforts may require establishing a funded development project. Read more about the service at [research.csc.fi](https://research.csc.fi/sciences/code-optimization/)

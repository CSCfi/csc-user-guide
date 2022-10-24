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
puhti-login12:~$ seff 366910
Job ID: 366910
Cluster: puhti
User/Group: louhivuo/louhivuo
State: COMPLETED (exit code 0)
Nodes: 1
Cores per node: 40
CPU Utilized: 01:13:41
CPU Efficiency: 94.47% of 01:18:00 core-walltime
Job Wall-clock time: 00:01:57
Memory Utilized: 22.13 GB (estimated maximum)
Memory Efficiency: 14.16% of 156.25 GB (3.91 GB/core)
Job consumed 1.81 CSC billing units based on following used resources
CPU BU: 1.30
Mem BU: 0.51
```

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
* [cProfile](cProfile.md) is the recommended, in-built profiling tool
  for Python programs
* [nvprof](nvprof.md) is a command-line CUDA profiler and tracing tool
  for CUDA programs
* [nsys](nsys.md) is the command-line interface of Nsight Systems a system-wide performance analysis tool designed to visualize an application’s algorithms
* [ncu](ncu.md) is the command-line interface of Nsight Compute, a tool to debug and optimize CUDA kernels

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
[kkayttaj@puhti-login11 logs]$ seff 29221065
Job ID: 29221065
Cluster: puhti
User/Group: kkayttaj/kkayttaj
State: COMPLETED (exit code 0)
Nodes: 2
Cores per node: 40
CPU Utilized: 16:01:21
CPU Efficiency: 97.17% of 16:29:20 core-walltime
Job Wall-clock time: 00:12:22
Memory Utilized: 23.68 GB (estimated maximum)
Memory Efficiency: 6.38% of 371.09 GB (185.55 GB/node)
Job consumed 24.14 CSC billing units based on following used resources
Billed project: project_2001659
CPU usage: 16.49 CPU BU
Mem usage: 7.65 CPU BU
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
* [cProfile](../apps/cProfile.md) is the recommended, in-built profiling tool
  for Python programs
* [nvprof](../apps/nvprof.md) is a command-line CUDA profiler and tracing tool
  for CUDA programs
* [nsys](../apps/nsys.md) is the command-line interface of Nsight Systems a system-wide performance analysis tool designed to visualize an application’s algorithms
* [ncu](../apps/ncu.md) is the command-line interface of Nsight Compute, a tool to debug and optimize CUDA kernels

---
tags:
  - Free
---

# Scalasca

[Scalasca](https://www.scalasca.org/) is an open-source software tool
that supports the performance optimization of parallel programs by
measuring and analyzing their runtime behavior via event traces. The analysis
identifies potential performance bottlenecks - in particular those
concerning communication and synchronization - and offers guidance in
exploring their causes. Scalasca supports applications using MPI,
OpenMP, POSIX threads, or MPI+OpenMP/Pthreads parallelization.

## Available

* Puhti: 2.6
* Mahti: 2.6

## License

Usage is possible for both academic and commercial purposes.

## Usage

Using Scalasca involves three steps:

1. Instrumentation
2. Execution measurement collection & analysis
3. Analysis report examination

### Instrumentation

Scalasca uses
[the Score-P measurement infrastructure](https://perftools.pages.jsc.fz-juelich.de/cicd/scorep/tags/scorep-7.1/html/)
for instrumentation of the target application. Score-P can be used
also as a stand-alone tool without Scalasca.

In order to instrument an application, you need to recompile the
application using the Score-P instrumentation command `scorep`, which is added
as a prefix to the original compile and link commands:

```bash
module load scorep
scorep mpicc -o my_prog my_prog.c
```

or setting in a Makefile for C/C++ codes:

```
CC=scorep mpicc
```

or, similarly, for Fortran codes:

```
F90=scorep mpif90
```

### Measurement collection and analysis

While applications instrumented by Score-P can be executed directly
with a measurement configuration defined via environment variables,
the `scan` convenience command provided by
Scalasca can be used to control certain aspects of the Score-P
measurement environment during the execution of the target
application. To produce a performance measurement using an
instrumented executable, prefix `srun`
with the `scan` command in the batch job script:

```bash
...
#SBATCH --ntasks=40

module load scalasca
scan srun ./my_app
```

By default, a flat profile is collected. Upon completion, measurement
results are stored in the experiment directory, which by default is
composed of the prefix `scorep_`, the target application executable
name, the run configuration (e.g., number of MPI ranks and/or OpenMP
threads), and a few other parameters of the measurement
configuration. For example, in the above example
`scorep_my_app_40_sum`.

One can also collect event trace data. As tracing can produce huge
amounts of data, it is recommended to first estimate the size of
trace, and possibly filter out some functions from the measurement.
Estimate can be obtained with `scorep-score` command:

```text
$ scorep-score -r scorep_my_app_40_sum/profile.cubex

Estimated aggregate size of event trace:                   1022kB
Estimated requirements for largest trace buffer (max_buf): 129kB
Estimated memory requirements (SCOREP_TOTAL_MEMORY):       4097kB
(hint: When tracing set SCOREP_TOTAL_MEMORY=4097kB to avoid intermediate flushes
 or reduce requirements using USR regions filters.)

flt     type max_buf[B] visits time[s] time[%] time/visit[us]  region
         ALL    131,431 20,196   12.81   100.0         634.28  ALL
         MPI     95,054  8,076    8.65    67.5        1071.04  MPI
         USR     24,168  8,056    3.38    26.3         418.96  USR
         COM     12,168  4,056    0.78     6.1         193.47  COM
      SCOREP         41      8    0.00     0.0          48.00  SCOREP

         MPI     94,000  8,000    0.17     1.3          20.97  MPI_Sendrecv
         USR     12,000  4,000    0.00     0.0           0.25  swap_fields
         COM     12,000  4,000    0.00     0.0           0.53  exchange
         USR     12,000  4,000    3.33    26.0         832.89  evolve
         MPI        826     14    0.01     0.1         823.21  MPI_Recv
...
```

In order to filter out the measurement of `swap_fields` and `evolve`,
one can create a file `scorep.filter` with the contents:

```text
SCOREP_REGION_NAMES_BEGIN
 EXCLUDE
   swap_fields
   evolve
SCOREP_REGION_NAMES_END
```

and check the effect of filtering with `-f` option:

```bash
$ scorep-score -f scorep.filter -r scorep_my_app_40_sum/profile.cubex

Estimated aggregate size of event trace:                   835kB
Estimated requirements for largest trace buffer (max_buf): 105kB
...
```

One could now proceed with the trace collection by setting
`SCOREP_FILTERING_FILE` environment variable and by passing options
`-q` and `-t` to `scan` command:

```bash
...
#SBATCH --ntasks=40

module load scalasca

export SCOREP_FILTERING_FILE=scorep.filter

scan -q -t srun ./my_app
```

After the trace collection is finished, Scalasca will carry out
trace-analysis for identifying various performance bottlenecks.
With tracing enabled, the experiment directory would be
`scorep_my_app_40_trace`.

## Analysis report examination

The Scalasca analysis report explorer `square` cannot currently be run on CSC
supercomputers. However, user may install Scalasca on their local
workstation, and copy the experiment directory there for analysis,
e.g.:

```bash
rsync -r puhti.csc.fi:/scratch/.../rundir/scorep_my_app_40_trace .
square scorep_my_app_40_trace
```

For large traces, one may copy only the post-processed trace analysis
result file `scorep_my_app_40_trace/scout.cubex`.

The OTF2 formatted event trace `scorep_my_app_40_trace/trace.otf2` can
be analyzed also with [Intel Trace Analyzer](itac.md).

## More information

- [Scalasca user guide](https://apps.fz-juelich.de/scalasca/releases/scalasca/2.6/docs/manual/index.html)
- [POP Online training](https://pop-coe.eu/further-information/online-training)

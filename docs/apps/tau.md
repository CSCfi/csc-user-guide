---
tags:
  - Free
catalog:
  name: TAU
  description: Performance analysis toolkit for parallel programs
  disciplines:
    - Miscellaneous
  license_type: Free
  unchecked: true
  available_on:
    - Roihu
---

# TAU

[TAU](https://www.cs.uoregon.edu/research/tau/home.php) (Tuning and Analysis
Utilities) is an open-source toolkit for performance analysis of parallel
programs. It measures where an application spends its time, broken down by
function, MPI process and thread, and can also record hardware counters.
TAU supports applications written in C, C++ and Fortran that use MPI,
OpenMP, or MPI+OpenMP parallelization.

## Available

* Roihu-CPU: 2.36

On Roihu, TAU is built with support for MPI, OpenMP, PAPI hardware counters
and PDT source instrumentation.

## License

Usage is possible for both academic and commercial purposes.

## Usage

Using TAU involves three steps:

1. Instrumentation
2. Execution and measurement
3. Analysis of the results

TAU is built with GCC and Open MPI, which are loaded by default. Load TAU with:

```bash
module load tau
```

If you have changed the default modules, load GCC and Open MPI first:
`module load gcc/15.2.0 openmpi/5.0.10 tau`.

### Instrumentation

To instrument an application, recompile it with the TAU compiler wrappers
instead of the usual compilers. The wrappers call the MPI compilers
themselves, so they replace `mpicc`, `mpicxx` and `mpif90`:

| Language | Instead of | Use        |
|----------|------------|------------|
| C        | `mpicc`    | `tau_cc.sh`  |
| C++      | `mpicxx`   | `tau_cxx.sh` |
| Fortran  | `mpif90`   | `tau_f90.sh` |

For example:

```bash
tau_cc.sh -O2 -fopenmp -o my_app my_app.c
```

or in a Makefile for C/C++ codes:

```
CC=tau_cc.sh
CXX=tau_cxx.sh
```

or, similarly, for Fortran codes:

```
F90=tau_f90.sh
```

By default, TAU instruments the source code using its PDT parser, which adds
timers to every function. MPI calls and OpenMP threads are measured
automatically.

The PDT parser supports C up to the C99 standard. For C code that uses
newer language features, or if source instrumentation otherwise fails, use
compiler-based instrumentation instead:

```bash
export TAU_OPTIONS="$TAU_OPTIONS -optCompInst"
```

### Execution and measurement

Run the instrumented application normally with `srun`. TAU writes one profile
file per MPI process and thread (`profile.<rank>.0.<thread>`) to the working
directory, or to the directory given in `PROFILEDIR`:

```bash
...
#SBATCH --ntasks=8
#SBATCH --cpus-per-task=4

module load tau

export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
export PROFILEDIR=$PWD/tau_profiles
mkdir -p $PROFILEDIR

srun ./my_app
```

With 8 MPI tasks and 4 OpenMP threads each, this produces 32 profile files.

## Analysis of the results

A text summary of the profiles can be printed on Roihu with `pprof`. Run it
in the directory that contains the profile files:

```bash
cd tau_profiles
pprof -s          # summary over all processes and threads
pprof             # full profile for each process and thread
```

The summary lists, for each function, the exclusive and inclusive time, the
number of calls and the time per call, for example:

```text
FUNCTION SUMMARY (total):
---------------------------------------------------------------------------------------
%Time    Exclusive    Inclusive       #Call      #Subrs  Inclusive Name
              msec   total msec                          usec/call
---------------------------------------------------------------------------------------
  1.8           31           31          24           0       1332 double thread_part(long, long) C
...
```

For graphical analysis with ParaProf, pack the profiles into a single file and
copy it to your workstation:

```bash
cd tau_profiles
paraprof --pack my_app.ppk
```

```bash
rsync roihu-cpu.csc.fi:/scratch/.../rundir/tau_profiles/my_app.ppk .
paraprof my_app.ppk
```

ParaProf is part of TAU, so you need a local TAU installation to open the file.

## More information

- [TAU home page](https://www.cs.uoregon.edu/research/tau/home.php)
- [TAU user guide](https://www.cs.uoregon.edu/research/tau/docs/newguide/)
- [POP Online training](https://pop-coe.eu/further-information/online-training)
# Compiling applications

## Building CPU applications

C/C++ and Fortran applications can be build with Intel or GNU
compiler suites. The Intel module is loaded by default, and it can changed to
GNU with the command:  FIXME: what is default?
```
module swap intel gcc
```

Different applications function better with different suites, so selection
needs to be done on case by case basis.

The actual compiler commands for building serial application with the two
suites are:

| Compiler suite | C  | C++ | Fortran |
| :------------- | :- | :-- | :------ |
| [Intel](https://software.intel.com/en-us/parallel-studio-xe/documentation/get-started) | icc | icpc | ifort |
| [GNU](https://gcc.gnu.org) | gcc | g++ | gfortran |

Intel and GNU compilers use different compiler options, table below lists
recommended basic optimization flags. It is best to start from the safe level
and then move up to intermediate or even aggressive, while making sure that
the results are correct and that the program has better performance.

| Optimisation level | Intel       | GNU               |
| :----------------- | :---------- | :---------------- |
| **Safe**           | -O2 -xCASCADELAKE -fp-model strict | -O2 -march=cascadelake |
| **Intermediate**   | -O2 -xCASCADELAKE | -O3 -march=cascadelake |
| **Aggressive**     | -O3 -xCASCADELAKE -fp-model fast=2 -no-prec-div | -O3 -march=cascadelake -ffast-math -funroll-loops |

Please note that not all applications benefit from the AVX-512 vector set
(`-xCASCADELAKE` or `-march=cascadelake`). It may be a good idea to test also
with AVX2 (`-xCORE-AVX2` or `-mavx2`) and compare the performance.

Detailed list of options for Intel and GNU compiler can be found from man
pages (`man icc/ifort`, `man gcc/gfortran` when corresponding programming
environment is loaded, or in the compiler manuals on the Web (see links
above).

All available versions of the compiler suites can be found with
```bash
module spider intel
module spider gcc
```

## Building GPU applications

Both CUDA and OpenACC programming models are supported on Puhti. To use them,
one needs to load specific modules (`module load cuda` for CUDA or
`module load pgi` for OpenACC).


### CUDA

The CUDA compiler (`nvcc`) takes care of compiling CUDA code for the target
GPU device and passing on the rest to a non-CUDA compiler (`gcc`).

To generate code for a given target device, one needs to tell the CUDA
compiler what compute capability the target device supports. On Puhti, the
GPUs (Volta V100) support compute capability 7.0, so one needs specify it with
`-gencode arch=compute_70,code=sm_70`.

For example, to compile a CUDA kernel (`example.cu`) on Puhti, the command
would be:
```bash
nvcc -gencode arch=compute_70,code=sm_70 example.cu
```

In principle, one can also target multiple GPU architectures by repeating the
`-gencode` multiple times for different compute capabilities. On Puhti this is
not necessary, since there is only one type of GPUs.


### OpenACC

OpenACC is supported with the PGI compilers (`pgcc`, `pgfortran`). 
To enable OpenACC support, one needs to give `-acc` flag to the compiler.

To generate code for a given target device, one needs to tell the compiler
what compute capability the target device supports. On Puhti, the GPUs (Volta
V100) support compute capability 7.0, so one needs to specify it with
`-ta=tesla:cc70`.

For example, to compile C code that uses OpenACC directives (`example.c`) on
Puhti, the command would be:

```bash
pgcc -acc -ta=tesla:cc70 example.c
```

To get information about what the compiler actually did with the OpenACC
directives, one can e.g. use `-Minfo=all`.


## Building MPI applications

There are currently three MPI environments available: **hpcx-mpi**,
**mpich**, and **intel-mpi**. We recommend to start with **hpcx-mpi**, and
try then others if your applications does not work or performs badly. All MPI
implementations can be used with both Intel and GNU compiler suites. PGI 
compiler cannot at the moment be used with MPI. The MPI environments are used
via `module load` i.e.
```bash
module load hpcx-mpi
```

When building MPI applications, one should use *mpixxx* compiler wrappers,
which differ depending on the compiler suite and MPI environment (FIXME: table
is not correct yet):

| Compiler suite | hpcx-mpi or mpich      | intel-mpi                 |
| :------------- | :--------------------- | :------------------------ |
| Intel          | mpifort, mpicc, mpicpc | mpiifort, mpiicc, mpiicpc |
| GNU            | mpigcc, mpig++, mpif90 | mpigcc, ...               |

## Building OpenMP and hybrid applications

Additional compiler and linker flags are needed when building OpenMP or
MPI/OpenMP hybrid applications:

| Compiler suite | OpenMP flag |
| :------------- | :---------- |
| Intel          | -qopenmp    |
| GNU            | -fopenmp    |

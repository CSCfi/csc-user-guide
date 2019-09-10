# Compiling applications

## General instructions

- Whenever possible, use the [local disk](disk.md#login-nodes) on the login-node to compile your software.
    - Compiling on the local disk is much faster and shifts load from the shared filesystem. 
    - The local disk is cleaned frequently, so move your files after compiling has finished. 



## Building CPU applications

C/C++ and Fortran applications can be build with Intel or GNU
compiler suites. The compiler suite is selected via the [Modules](modules.md)
system, i.e.
```
module load intel
```
or
```
module load gcc
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

| Optimisation level | Intel                        | GNU               |
| :----------------- | :--------------------------- | :---------------- |
| **Safe**           | -O2 -xHost -fp-model precise | -O2 -march=native |
| **Intermediate**   | -O2 -xHost                   | -O3 -march=native |
| **Aggressive**     | -O3 -xHost -fp-model fast=2 -no-prec-div -fimf-use-svml=true | -O3 -march=native -ffast-math -funroll-loops |

Please note that not all applications benefit from the AVX-512 vector set
(`-xHost` or `-march=native`). It may be a good idea to test also
with AVX2 (`-xCORE-AVX2` or `-mavx2`) and compare the performance.

Detailed list of options for Intel and GNU compiler can be found from man
pages (`man icc/ifort`, `man gcc/gfortran` when corresponding programming
environment is loaded, or in the compiler manuals on the Web (see links
above).

All available versions of the compiler suites can be found with
```
module spider intel
module spider gcc
```

## Building GPU applications

Both CUDA and OpenACC programming models are supported on Puhti. To use them,
one needs to load specific modules.

For example, to load CUDA 10.1 environment, the command is:
```bash
module load gcc/8.3.0 cuda/10.1.168
```

and to load the PGI compiler for OpenACC, the command is:
```bash
module load pgi
```

For more detailed information about the available modules, please see `module
spider cuda` or `module spider pgi`.

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
**mpich**, and **intel-mpi**. The default is **hpcx-mpi**, which we also
recommend as the first one to try.

If **hpcx-mpi** doesn't work for your application, or it performs badly, you
can then also try the other ones to see if they work better. All MPI
implementations can be used with both Intel and GNU compiler suites. PGI
compiler cannot at the moment be used with MPI. The MPI environments are used
via `module load` i.e.
```bash
module load hpcx-mpi
```

When building MPI applications, one should use *mpixxx* compiler wrappers,
that differ depending on the compiler suite and the MPI environment:

| Compiler suite | hpcx-mpi or mpich      | intel-mpi                 |
| :------------- | :--------------------- | :------------------------ |
| Intel          | mpifort, mpicc, mpicxx | mpiifort, mpiicc, mpiicpc |
| GNU            | mpif90, mpicc, mpicxx  | mpif90, mpicc, mpicxx     |


## Building OpenMP and hybrid applications

Additional compiler and linker flags are needed when building OpenMP or
MPI/OpenMP hybrid applications:

| Compiler suite | OpenMP flag |
| :------------- | :---------- |
| Intel          | -qopenmp    |
| GNU            | -fopenmp    |

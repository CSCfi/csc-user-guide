# Compiling applications in Mahti

## General instructions

CHECKME: is there local disk in Mahti

- Whenever possible, use the [local disk](disk.md#login-nodes) on the login node for compiling software.
    - Compiling on the local disk is much faster and shifts load from the shared file system. 
    - The local disk is cleaned frequently, so please move your files elsewhere after compiling. 


## Building applications

CHECKME: is Intel available as module

C/C++ and Fortran applications can be built with Intel or GNU
compiler suites. The compiler suite is selected via the [Modules](modules.md)
system, i.e.
```
module load intel
```
or
```
module load gcc
```
Different applications function better with different suites, so the selection
needs to be done on a case-by-case basis.

The actual compiler commands for building a serial application with the two
suites:

| Compiler suite | C  | C++ | Fortran |
| :------------- | :- | :-- | :------ |
| [Intel](https://software.intel.com/en-us/parallel-studio-xe/documentation/get-started) | icc | icpc | ifort |
| [GNU](https://gcc.gnu.org) | gcc | g++ | gfortran |

Intel and GNU compilers use different compiler options. The recommended basic optimization 
flags are listed in the table below. It is recommended to start from the safe level
and then move up to intermediate or even aggressive, while making sure the results are 
correct and the program's performance has improved.

| Optimisation level | Intel                        | GNU               |
| :----------------- | :--------------------------- | :---------------- |
| **Safe**           | -O2 -xHost -fp-model precise | -O2 -march=native |
| **Intermediate**   | -O2 -xHost                   | -O3 -march=native |
| **Aggressive**     | -O3 -xHost -fp-model fast=2 -no-prec-div -fimf-use-svml=true | -O3 -march=native -ffast-math -funroll-loops |


A detailed list of options for the Intel and GNU compilers can be found on the _man_
pages (`man icc/ifort`, `man gcc/gfortran` when the corresponding programming
environment is loaded, or in the compiler manuals (see the links above).

List all available versions of the compiler suites:
```
module spider intel
module spider gcc
```


## Building MPI applications

CHECKME: supported MPIs in Mahti

There are currently three MPI environments available: **hpcx-mpi**,
**mpich**, and **intel-mpi**. The default is **hpcx-mpi**, which is 
also recommended to begin with.

If **hpcx-mpi** is incompatible with your application or delivers insufficient performance, 
please try another environment. All MPI
implementations can be used with both Intel and GNU compiler suites. The PGI
compiler cannot presently be used with MPI. The MPI environments can be used
via `module load`, i.e.
```bash
module load hpcx-mpi
```

When building MPI applications, use _mpixxx_ compiler wrappers
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

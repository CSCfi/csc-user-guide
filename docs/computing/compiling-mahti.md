# Compiling applications in Mahti

## General instructions


- Whenever possible, use the [local disk](disk.md#login-nodes) on the login node for compiling software.
    - Compiling on the local disk is much faster and shifts load from the shared file system. 
    - The local disk is cleaned frequently, so please move your files elsewhere after compiling. 


## Building MPI applications

C/C++ and Fortran applications can be built with
[GNU](https://gcc.gnu.org), [AMD](https://developer.amd.com/amd-aocc/), 
or [Intel](https://software.intel.com/en-us/parallel-studio-xe/documentation/get-started)
compiler suites. The GNU compilers are loaded by default. AMD compilers can be
loaded using the [Modules](modules.md) system with the command:
```
module load clang
```
and Intel compilers with the command:
```
module load intel
```

Different applications function better with different suites, so the selection
needs to be done on a case-by-case basis.

The MPI environment in Mahti is OpenMPI, and when building MPI
applications all compiler suites can be used with
the `mpicc` (C), `mpicxx` (C++), or `mpif90` (Fortran) wrappers.

The compiler options for different suites are different. The
recommended basic optimization flags are listed in the table below. It
is recommended to start from 
the safe level and then move up to intermediate or even aggressive,
while making sure the results are  correct and the program's
performance has improved. 


| Optimisation level | GNU               | Intel                        | AMD (clang) |
| :----------------- | :---------------- | :--------------------------- | :----------- |
| **Safe**           | -O2 -march=native | -O2 -fp-model precise | -O2 -march=native  |
| **Intermediate**   | -O3 -march=native | -O2                    | -O3 -march=native |
| **Aggressive**     | -O3 -march=native -ffast-math -funroll-loops | -O3 -fp-model fast=2 -no-prec-div -fimf-use-svml=true | -O3 -march=native -ffast-math -funroll-loops |


A detailed list of options for the Intel and GNU compilers can be found on the _man_
pages (`man gcc/gfortran`, `man icc/ifort`)  when the corresponding programming
environment is loaded, or in the compiler manuals (see the links above).

List all available versions of the compiler suites:
```
module spider gcc
module spider clang
module spider intel
```

## Building OpenMP and hybrid applications

Additional compiler and linker flags are needed when building OpenMP or
MPI/OpenMP hybrid applications:

| Compiler suite | OpenMP flag |
| :------------- | :---------- |
| GNU and AMD    | -fopenmp    |
| Intel          | -qopenmp    |

## Building GPU applications

TBA ...

## Building serial applications

For building serial applications, one needs to use compiler suite
specific compiler command:

| Compiler suite | C  | C++ | Fortran |
| :------------- | :- | :-- | :------ |
| GNU            | gcc | g++ | gfortran |
| AMD            | clang | clang++ | flang |
| Intel          | icc | icpc | ifort |

## Building GPU applications

The CUDA, OpenACC and OpenMP Offloading (for C++ codes) programming 
models are supported on Mahti. Specific modules have to be loaded 
in order to use them.

For example, to load the NVIDIA HPC SDK 21.2 environment:
```bash
module load nvhpc/21.2
```

For more detailed information about the available modules, please see `module
spider nvhpc`.

### CUDA

The compiler (`nvc++`) is a C++17 compiler which supports CUDA, OpenACC, and OpenMP
Offloading on NVIDIA GPUs.
The (`nvcc`) is the CUDA C and CUDA C++ compiler driver for NVIDIA GPUs.
The (`nvfortran`) is the CUDA Fortran compiler driver for NVIDIA GPUs.


To generate code for a given target device, tell the CUDA
compiler what compute capability the target device supports. On Mahti, the
GPUs (Ampere V100) support compute capability 8.0. Specify this using
`-gencode arch=compute_80,code=sm_80`.

For example, compiling a CUDA kernel (`example.cu`) on Puhti:
```bash
nvcc -gencode arch=compute_80,code=sm_80 example.cu
```



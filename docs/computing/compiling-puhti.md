# Compiling applications in Puhti

## General instructions

- Whenever possible, use the [local disk](disk.md#login-nodes) on the login node for compiling software.
    - Compiling on the local disk is much faster and shifts load from the shared file system.
    - The local disk is cleaned frequently, so please move your files elsewhere after compiling.

## Building CPU applications

!!! info
    Intel reorganized their compiler suites and names of Intel compilers have changed following the Red Hat Enterprise Linux 8 (RHEL8) update on Puhti. In addition, Intel changed the underlying technology of their compilers and renamed the old compilers as Intel Compilers Classic.

C/C++ and Fortran applications can be built with Intel or GNU
compiler suites. The compiler suite is selected via the [Modules](modules.md)
system, i.e.

```bash
# New Intel compilers 
module load intel-oneapi-compilers
```

or

```bash
# Old Intel compilers
module load intel-oneapi-compilers-classic
```

or

```bash
module load gcc
```

Different applications function better with different suites, so the selection
needs to be done on a case-by-case basis.

The actual compiler commands for building a serial application with these
suites:

| Compiler suite | C  | C++ | Fortran |
| :------------- | :- | :-- | :------ |
| [Intel, new](https://software.intel.com/en-us/parallel-studio-xe/documentation/get-started) | icx | icpx | ifx |
| [Intel, classic](https://software.intel.com/en-us/parallel-studio-xe/documentation/get-started) | icc | icpc | ifort |
| [GNU](https://gcc.gnu.org) | gcc | g++ | gfortran |

Intel and GNU compilers use different compiler options. The recommended basic optimization
flags are listed in the table below. It is recommended to start from the safe level
and then move up to intermediate or even aggressive, while making sure the results are
correct and the program's performance has improved.

| Optimisation level | Intel                        | GNU               |
| :----------------- | :--------------------------- | :---------------- |
| **Safe**           | -O2 -xHost -fp-model precise | -O2 -march=native |
| **Intermediate**   | -O2 -xHost                   | -O3 -march=native |
| **Aggressive**     | -O3 -xHost -fp-model fast=2 -no-prec-div -fimf-use-svml=true -qopt-zmm-usage=high| -O3 -march=native -ffast-math -funroll-loops -mprefer-vector-width=512|

A detailed list of options for the Intel and GNU compilers can be found on the _man_
pages (`man icc/ifort`, `man gcc/gfortran` when the corresponding programming
environment is loaded, or in the compiler manuals (see the links above).

Please note that some flags, for example `-no-prec-div` and `-qopt-zmm-usage`, are currently supported only by the intel classic compilers (`icc`/`icpx`/`ifort`). More information about the current and planned flags support for the intel compilers can be checked with `icx -qnextgen-diag` or in the manuals.

Also, not all applications benefit from the AVX-512 vector set
(`-xHost` or `-march=native`). It may be a good idea to also test AVX2
(`-xCORE-AVX2` or `-mavx2`) and compare the performance.


List all available versions of the compiler suites:

```bash
module spider intel-oneapi-compilers
module spider gcc
```

## Building GPU Applications

GPU support in Puhti is provided through NVIDIA compilers:

- The `nvc` compiler is a C11 compiler that supports OpenACC for NVIDIA GPUs, and OpenACC and OpenMP for multicore CPUs.

- The `nvc++` compiler is a C++17 compiler that supports GPU programming with C++17 parallel algorithms, OpenACC, and OpenMP offloading on NVIDIA GPUs. However, it does not currently support C++ CUDA codes.

- The `nvcc` compiler is the CUDA C and CUDA C++ compiler driver for NVIDIA GPUs.

- The `nvfortran` compiler is the CUDA Fortran compiler driver for NVIDIA GPUs, supporting both OpenACC and multicore processing for OpenACC and OpenMP.

Specific instructions on how to load and use these compilers are provided in the following sections.

### CUDA

The CUDA compiler (`nvcc`) takes care of compiling the CUDA code for the target
GPU device and passing on the rest to a non-CUDA compiler (i.e. `gcc`). For example, to load the CUDA 11.7 environment together with the GNU compiler:

```bash
module load gcc/11.3.0 cuda/11.7.0
```

To generate code for a given target device, tell the CUDA
compiler what compute capability the target device supports. On Puhti, the
GPUs (Volta V100) support compute capability 7.0. Specify this using
`-gencode arch=compute_70,code=sm_70`.

For example, compiling a CUDA kernel (`example.cu`) on Puhti:

```bash
nvcc -gencode arch=compute_70,code=sm_70 example.cu
```

In principle, it is also possible to target multiple GPU architectures by repeating
`-gencode` multiple times for different compute capabilities. However, this is
not necessary on Puhti, since there is only one type of GPU.

### OpenACC

!!! warning
    OpenACC support is provided through the NVIDIA `nvc` and `nvc++` compilers.
    However, it is important to note that the support can be somewhat 
    limited and may lack certain functionalities, such as MPI 
    parallelization. For additional information about OpenACC support, 
    the CSC service desk should be contacted.
    
The compilers can be accessed through the NVIDIA HPC SDK module:

```
module load .unsupported
module load nvhpc/22.7
```

Enabling OpenACC support requires providing the `-acc` flag to the compiler. For Fortran codes, this can be achieved as follows:

```
nvfortran -acc example.F90 -gpu=cc70
```

For information about what the compiler actually does with the OpenACC directives, use `-Minfo=all`.

## Building MPI applications

There are currently two MPI environments available: `openmpi` and `intel-oneapi-mpi`. The default is `openmpi`, which is
also recommended to begin with.

If `openmpi` is incompatible with your application or delivers insufficient performance,
please try another environment. The MPI environments can be used
via `module load`, i.e.

```bash
module load openmpi
```

When building MPI applications, use _mpixxx_ compiler wrappers
that differ depending on the compiler suite and the MPI environment:

| Compiler suite | openmpi               | intel-oneapi-mpi                 |
| :------------- | :--------------------- | :------------------------ |
| Intel          | mpifort, mpicc, mpicxx | mpiifort, mpiicc, mpiicpc |
| GNU            | mpif90, mpicc, mpicxx  | incompatible    |

## Building OpenMP and hybrid applications

Additional compiler and linker flags are needed when building OpenMP or
MPI/OpenMP hybrid applications:

| Compiler suite | OpenMP flag |
| :------------- | :---------- |
| Intel          | -qopenmp    |
| GNU            | -fopenmp    |

## Building software using Spack

[Spack](https://spack.io) is a flexible package manager that can be used to
install software on supercomputers and Linux and macOS systems. The basic
module tree including compilers, MPI libraries and many of the available
software on CSC supercomputers have been installed using Spack.

CSC provides a module `spack/v0.18-user` on Puhti that can be used by users to
build software on top of the available compilers and libraries using Spack. It
is also possible to install different customized versions of packages available
in the module tree for special use cases. [See here for a short tutorial on how
to install software on CSC supercomputers using Spack](../support/tutorials/user-spack.md).
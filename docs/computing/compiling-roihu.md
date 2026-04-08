# Compiling applications in Roihu

!!! info
    Roihu has separate CPU and GPU partitions with different CPU architectures:

    - Roihu-CPU nodes use AMD x86 processors
    - Roihu-GPU nodes use NVIDIA Grace (ARM) processors

    Binaries compiled for one architecture are generally not usable on the other.
    Accordingly, software should be compiled on the same side where it will be run:

    - Compile for CPU nodes on the Roihu-CPU login node
    - Compile for GPU nodes on the Roihu-GPU login node


## General instructions

- Whenever possible, use the [local disk](disk.md#login-nodes) on the login node for compiling software.
    - Compiling on the local disk is much faster and shifts load from the shared file system.
    - The local disk is cleaned frequently, so please move your files elsewhere after compiling.


## Compiling on Roihu-CPU

C/C++ and Fortran applications can be built with
the [GNU](https://gcc.gnu.org) or the [AMD](https://developer.amd.com/amd-aocc/)
compiler suites. GNU compilers are loaded by default. AMD compilers can be
loaded using the [Modules](modules.md) system with the command:
```
module load aocc
```

The compiler executables are as follows:

| Compiler suite | C  | C++ | Fortran |
| :------------- | :- | :-- | :------ |
| GNU            | gcc | g++ | gfortran |
| AMD            | clang | clang++ | flang |

For applications that depend on MPI, it is recommended to instead use the compiler
wrappers described in the [MPI section](#building-mpi-applications) below.

The compiler options for different suites are different. The
recommended basic optimization flags are listed in the table below. It
is recommended to start from the safe level and then move up to intermediate
or even aggressive, while ensuring the results are correct and the program's
performance has improved.

| Optimization level | GNU               | AMD (clang) |
| :----------------- | :---------------- | :----------- |
| **Safe**           | -O2 -march=native | -O2 -march=native |
| **Intermediate**   | -O3 -march=native | -O3 -march=native |
| **Aggressive**     | -O3 -march=native -ffast-math -funroll-loops |

!!! info
    Because the Roihu-CPU login and compute nodes share the same CPU architecture,
    compiling for the native architecture (`-march=native`) is optimal even if
    the compilation is done on login nodes.

Example of compiling a non-MPI C program in GNU environment:
```bash
gcc -O3 -march=native example.c -o example
```

A detailed list of options for the GNU and AMD compilers can be found in the _man_
pages (`man gcc/gfortran`)  when the corresponding programming
environment is loaded, or in the compiler manuals (see the links above).

We recommend testing and profiling your application with both compiler suites
to see which compiler works the best for your use case.

List all available versions of the compiler suites:
```
module spider gcc
module spider aocc
```


## Building MPI applications

The MPI environment in Roihu is OpenMPI. You may use one of the MPI compiler wrappers
`mpicc` (C), `mpicxx` (C++), or `mpif90` (Fortran) when compiling MPI applications.
These wrappers end up calling the compiler from your currently loaded compiler suite
(GNU or AMD) and work in both compiler suites.

Example:
```bash
mpicc -O3 -march=native example.c -o example
```

List all available versions of OpenMPI (one is always loaded by default):
```
module spider openmpi
```

TODO:

- `aocc` does currently not have a corresponding MPI module. Revisit this and test once that is available
- Better links/instructions for finding compiler docs


## Building OpenMP and hybrid applications

An additional compiler and linker flag is needed when building an OpenMP or a hybrid
MPI/OpenMP application:

| Compiler suite | OpenMP flag |
| :------------- | :---------- |
| GNU and AMD    | -fopenmp    |

Example compilation of a hybrid MPI/OpenMP application:
```bash
mpicc -O3 -march=native -fopenmp example.c -o example
```


## Compiling on Roihu-GPU

!!! info
    When compiling for the GPU nodes on Roihu, make sure you use Roihu's GPU login nodes.
    Binaries compiled on Roihu-CPU are not compatible with Roihu-GPU nodes.

CUDA is the recommended programming model for Nvidia GPUs and CSC provides it as
an environment module.

### CUDA

The CUDA compiler (`nvcc`) takes care of compiling the CUDA code for the target
GPU device and passing on the rest to a non-CUDA compiler (i.e. `gcc`).
For example, to load the CUDA 13.1 environment together with the GNU compiler:

```bash
module load gcc/15.2.0 cuda/13.1.1
```

To generate code for a given target device, tell the CUDA
compiler what compute capability the target device supports. On Roihu, the
GPUs (Hopper 200) support compute capability 9.0. Specify this using
`-gencode arch=compute_90,code=sm_90`. Alternatively, you may use `compute_90a`
or `sm_90a` to enable Hopper-specific extension features that may produce more
performant code.

For example, compiling a CUDA kernel (`example.cu`) on Roihu:

```bash
nvcc -gencode arch=compute_90a,code=sm_90a example.cu
```

!!! info
    Code generated with `arch=compute_90a` or `code=sm_90a` is not backwards or forwards
    compatible with other GPU architectures. If this is a concern for you, use the
    more generic `arch=compute_90,code=sm_90` options.


## Building software using Spack

[Spack](https://spack.io) is a flexible package manager that can be
used to install software on supercomputers and Linux and macOS
systems. The basic module tree including compilers, MPI libraries and
many of the available software on CSC supercomputers have been
installed using Spack.

[See here for a short tutorial on how
to install software on CSC supercomputers using Spack](../support/tutorials/user-spack.md).

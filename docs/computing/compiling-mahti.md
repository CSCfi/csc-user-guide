# Compiling applications in Mahti

## General instructions


- Whenever possible, use the [local disk](disk.md#login-nodes) on the login node for compiling software.
    - Compiling on the local disk is much faster and shifts load from the shared file system. 
    - The local disk is cleaned frequently, so please move your files elsewhere after compiling. 


## Building MPI applications

C/C++ and Fortran applications can be built with
[GNU](https://gcc.gnu.org) or [AMD](https://developer.amd.com/amd-aocc/)
compiler suites. The GNU compilers are loaded by default. AMD compilers can be
loaded using the [Modules](modules.md) system with the command:
```
module load aocc
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


| Optimisation level | GNU               | AMD (clang) |
| :----------------- | :---------------- | :----------- |
| **Safe**           | -O2 -march=native | -O2 -march=native  |
| **Intermediate**   | -O3 -march=native | -O3 -march=native |
| **Aggressive**     | -O3 -march=native -ffast-math -funroll-loops | -O3 -march=native -ffast-math -funroll-loops |


A detailed list of options for the GNU and AMD compilers can be found on the _man_
pages (`man gcc/gfortran`)  when the corresponding programming
environment is loaded, or in the compiler manuals (see the links above).

List all available versions of the compiler suites:
```
module spider gcc
module spider aocc
```

<!-- ### Intel compilers

!!! warning
    Support for Intel compilers may be somewhat limited and may lack certain functionalities. For more detailed information, it is recommended to contact the CSC service desk.

Access to the Intel compilers can be obtained by loading the .unsupported modules:

```
module load .unsupported
module load intel-oneapi-compilers/2021.4.0
```

Comprehensive information about flags and optimization options that can be used with the compiler can be found in the manual pages, accessible with `man icc/ifort`. -->

## Building OpenMP and hybrid applications

Additional compiler and linker flags are needed when building OpenMP or
MPI/OpenMP hybrid applications:

| Compiler suite | OpenMP flag |
| :------------- | :---------- |
| GNU and AMD    | -fopenmp    |


## Building serial applications

For building serial applications, one needs to use compiler suite
specific compiler command:

| Compiler suite | C  | C++ | Fortran |
| :------------- | :- | :-- | :------ |
| GNU            | gcc | g++ | gfortran |
| AMD            | clang | clang++ | flang |

## Building GPU applications

The CUDA, OpenACC and OpenMP Offloading (for C++ codes) programming 
models are provided on Mahti by the NVIDIA HPC compilers:

Compilers:

- The (`nvc`) is a C11 compiler that supports OpenACC for NVIDIA  GPUs while  OpenACC and OpenMP for multicore CPUs.

- The compiler (`nvc++`) is a C++17 compiler which supports GPU programming with C++17 parallel algorithms, OpenACC, and OpenMP
Offloading on NVIDIA GPUs. It does not support yet C++ CUDA codes.

- The (`nvcc`) is the CUDA C and CUDA C++ compiler driver for NVIDIA GPUs.

- The (`nvfortran`) is the CUDA Fortran compiler driver for NVIDIA GPUs, it supports OpenACC as also multicore for OpenACC and OpenMP.

### CUDA

To generate code for a given target device, tell the CUDA
compiler what compute capability the target device supports. On Mahti, the
GPUs (Ampere V100) support compute capability 8.0. Specify this using
`-gencode arch=compute_80,code=sm_80`.

For example, compiling a CUDA kernel (`example.cu`) on Puhti (for C or C++ codes):
```bash
nvcc -gencode arch=compute_80,code=sm_80 example.cu
```

Compile a CUDA Fortran code named example.cuf
```bash
nvfortran -gpu=cc80 example.cuf
```

### OpenACC

!!! warning
    OpenACC support is provided through the NVIDIA `nvc` and `nvc++` compilers.
    However, it is important to note that the support can be somewhat 
    limited and may lack certain functionalities, such as MPI 
    parallelization. For additional information about OpenACC support, 
    the CSC service desk should be contacted.

The compilers can be accessed through the NVIDIA HPC SDK module:
```bash
module load .unsupported
module load nvhpc/22.3
```

For more detailed information about the available modules, please see `module
spider nvhpc`.

To enable OpenACC support, one needs to give `-acc` flag to the compiler.

To generate code for a given target device, tell the compiler
what compute capability the target device supports. On Puhti, the GPUs (Ampere A100) 
support compute capability 8.0. 

For example, to compiling C code that uses OpenACC directives (`example.c`):

```bash
nvc -acc example.c .gpu=cc80
```

For information about what the compiler actually does with the OpenACC
directives, use `-Minfo=all`.

For Fortran code:
```bash
nvfortran -acc example.F90 -gpu=cc80
```

For C++ code:
```bash
nvc++ -acc example.cpp -gpu=cc80
```

### OpenMP Offloading

To enable OpenMP Offloading, the options `-mp=gpu` is required

For example, compile a C code with OpenMP offloading:
```bash
nvc -mp=gpu example.c -gpu=cc80
```

For Fortran code:
```bash
nvfortran -mp=gpu example.F90 -gpu=cc80
```

For C++ code:
```bash
nvc++ -mp=gpu example.cpp -gpu=cc80
```

The `nvc++` compiler supports codes that contain OpenACC, OpenMP Offloading and C++ parallel algorithms in the same code, 
for such case you can compile with:
```bash
nvc++ -stdpar -acc -mp=gpu example.cpp -gpu=cc80
```

<!-- For MPI, load the module
```bash
module load openmpi/4.1.2
```

The use of the wrappers `mpicc`, `mpic++`, `mpif90`, executes the corresponding `nvc`,`nvc++`,`nvfortran` respectively. -->

## Building software using Spack

[Spack](https://spack.io) is a flexible package manager that can be used to
install software on supercomputers and Linux and macOS systems. The basic
module tree including compilers, MPI libraries and many of the available
software on CSC supercomputers have been installed using Spack.

CSC provides a module `spack/v0.17-user` on Mahti that can be used by users to
build software on top of the available compilers and libraries using Spack. It
is also possible to install different customized versions of packages available
in the module tree for special use cases. [See here for a short tutorial on how
to install software on CSC supercomputers using Spack](../support/tutorials/user-spack.md).
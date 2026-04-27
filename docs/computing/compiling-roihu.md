# Compiling applications in Roihu

!!! info
    Roihu has separate CPU and GPU partitions with different CPU architectures:

    - Roihu-CPU nodes use AMD (x86) processors
    - Roihu-GPU nodes use NVIDIA Grace (ARM) processors

    Binaries compiled for one architecture are not usable on the other.
    Accordingly, software should be compiled on the same side where it will be run:

    - Compile for CPU nodes on the Roihu-CPU login node
    - Compile for GPU nodes on the Roihu-GPU login node


## General instructions

- Whenever possible, use the [local disk](roihu-disk.md#login-nodes) on the login node for compiling software.
    - Compiling on the local disk is much faster and shifts load from the shared file system.
    - The local disk is cleaned frequently, so please move your files elsewhere after compiling.


- Please see [the page on available HPC libraries](hpc-libraries.md) for using common libraries (BLAS, FFTW, ...)
and linking them to your applications.

## Compiling on Roihu-CPU

!!! info
    When compiling for the CPU nodes on Roihu, make sure you use Roihu's CPU login nodes.
    Binaries compiled on Roihu-GPU are not compatible with Roihu-CPU nodes.

Roihu-CPU provides [GNU](https://gcc.gnu.org) and [AMD AOCC](https://developer.amd.com/amd-aocc/)
compiler environments for building C/C++ and Fortran applications.
These environments are available under the following [modules](modules.md):

| Compiler suite               | Modules                                                  |
| :--------------------------- | :------------------------------------------------------- |
| GNU 15.2.0                   | `gcc/15.2.0 openmpi/5.0.10`                              |
| AMD AOCC 5.0.0               | `aocc/5.0.0 openmpi/5.0.10`                              |

The first compiler suite is loaded by default.
You can change the environment by loading the listed modules, for example,

```bash
module load aocc/5.0.0 openmpi/5.0.10
```

List all available versions of the compiler suites:
```bash
module spider gcc
module spider aocc
```

The compiler executables are as follows:

| Compiler suite | C     | C++     | Fortran  |
| :------------- | :---- | :------ | :------- |
| GNU            | gcc   | g++     | gfortran |
| AMD            | clang | clang++ | flang    |

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
environment is loaded, or in the compiler manuals:
- [GNU](https://gcc.gnu.org)
- [AMD AOCC](https://developer.amd.com/amd-aocc/)

We recommend testing and profiling your application with both compiler suites
to see which compiler works the best for your use case.


### Building MPI applications

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


### Building OpenMP and hybrid applications

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


Roihu-GPU provides [GNU](https://gcc.gnu.org) and [NVIDIA-HPC](https://developer.nvidia.com/hpc-compilers)
compiler environments for building C/C++ and Fortran applications under the following [modules](modules.md):

| Compiler suite               | Modules                                                  |
| :--------------------------- | :------------------------------------------------------- |
| GNU 14.3.0 + CUDA 12.9.1     | `gcc/14.3.0 cuda/12.9.1 openmpi/5.0.8 openblas/0.3.30`   |
| GNU 15.2.0 + CUDA 13.1.1     | `gcc/15.2.0 cuda/13.1.1 openmpi/5.0.8 openblas/0.3.30`   |
| NVIDIA HPC 26.3              | `nvhpc/26.3`                                             |

The first compiler suite is loaded by default.
You can change the environment by loading the listed modules, for example,

```bash
module load nvhpc/26.3
```

!!! info "About the `nvhpc` module"
    Note that the `nvhpc` module includes CUDA, MPI, and BLAS implementations,
    so you don't need to load these modules separately when using the `nvhpc` module.
    For this reason, the `module load` might note you about inactive modules.

    To avoid leaving inactive modules, you can purge modules before loading the environment:

    ```bash
    module purge
    module load nvhpc/26.3
    ```

List all available versions of the compiler suites:
```bash
module spider gcc
module spider cuda
module spider nvhpc
```

The compiler executables are as follows:

| Compiler suite | C   | C++   | Fortran   |
| :------------- | :-- | :---- | :-------- |
| GNU            | gcc | g++   | gfortran  |
| NVIDIA HPC     | nvc | nvc++ | nvfortran |


In addition, the CUDA [`nvcc`](https://docs.nvidia.com/cuda/cuda-compiler-driver-nvcc/index.html) compiler is available for building GPU kernel code. See the [CUDA section below](#compiling-cuda-applications).


### Compiling CUDA applications

CUDA is the recommended programming model for Nvidia GPUs and it is
provided in `cuda` and `nvhpc` modules.

The CUDA compiler (`nvcc`) takes care of compiling CUDA kernels code for the target
GPU device and passes the rest to the currently loaded host compiler like `gcc` or `nvhpc`.

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


### Compiling MPI+CUDA applications

All the provided GNU and NVIDIA compiler environments provide a CUDA-aware MPI library.

If the structure of the MPI+CUDA application allows, you can build it in parts:

1. Compile CUDA kernels to object files with `nvcc -c`
2. Compile host code to object files with the MPI compiler wrappers that will call the loaded host compiler (`mpicc -c`, `mpicxx -c`, or `mpif90 -c`)
3. Link all the object files with the MPI compiler wrapper (`mpicc`, `mpicxx`, or `mpif90`)

It is also possible to compile the whole codebase with `nvcc`, but then
we need to provide the necessary MPI compile and link options
to the underlying host compiler called by `nvcc`.
This can be achieved as follows via `-Xcompiler` and `-Xlinker` flags:

```bash
# Parse MPI options for compiler
Xcompiler="-Xcompiler $(mpicxx --showme | tr ' ' '\n' | sed '/^-Wl,/d;1d' | paste -sd, -)"

# Parse MPI options for linker
Xlinker="-Xlinker $(mpicxx --showme | tr ' ' '\n' | sed -n 's/^-Wl,//p' | paste -sd, -)"

# Compile MPI code using nvcc
nvcc -gencode arch=compute_90a,code=sm_90a $Xcompiler $Xlinker mpi_cuda_code.cu
```

!!! warning
    Remember to load the modules used for compiling also when running the application
    to ensure that the correct MPI library is used during the runtime.


### Compiling application using OpenMP offload, OpenACC, and C++ standard parallelism

!!! warning
    It is recommended to use the NVIDIA HPC compilers for
    compiling codes using OpenMP offload, OpenACC, and C++ standard parallelism.

Start by loading NVIDIA HPC compilers:

```bash
module purge
module load nvhpc/26.3
```

The compiler options for enabling different GPU programming models are as follows:

| Programming model | Compiler option              |
| :---------------- | :--------------------------- |
| OpenMP offload    | `-mp=gpu`                    |
| OpenACC           | `-acc=gpu`                   |
| C++ stdpar        | `-stdpar=gpu` (`nvc++` only) |


To generate efficient code for the GH200 superchips on Roihu,
specify the target with the following option:
```raw
-gpu=cc90
```

Example compilation commands:

| Programming model | C                                      | C++                                            | Fortran                                        |
| :---------------- | :------------------------------------- | :--------------------------------------------- | :--------------------------------------------- |
| OpenMP offload    | `nvc -O3 -mp=gpu  -gpu=cc90 example.c` | `nvc++ -O3 -mp=gpu  -gpu=cc90 example.cpp`     | `nvfortran -O3 -mp=gpu  -gpu=cc90 example.F90` |
| OpenACC           | `nvc -O3 -acc=gpu -gpu=cc90 example.c` | `nvc++ -O3 -acc=gpu -gpu=cc90 example.cpp`     | `nvfortran -O3 -acc=gpu -gpu=cc90 example.F90` |
| C++ stdpar        |  N/A                                   | `nvc++ -O3 -stdpar=gpu  -gpu=cc90 example.cpp` |  N/A                                           |


The compilers support also codes that contain multiple programming models.
As an example, compile a C++ code that contains OpenMP offload, OpenACC, and C++ parallel algorithms with:
```bash
nvc++ -O3 -mp=gpu -acc=gpu -stdpar=gpu -gpu=cc90 example.cpp
```

### Compiling MPI application using OpenMP offload, OpenACC, and C++ standard parallelism

The `nvhpc` module is bundled with GPU-aware MPI implementation with
the usual compiler wrappers, and MPI applications can be compiled
like above but replacing `nvc`, `nvc++`, and `nvfortran` with
`mpicc`, `mpicxx`, and `mpif90`, respectively:

| Programming model | C                                        | C++                                             | Fortran                                     |
| :---------------- | :--------------------------------------- | :---------------------------------------------- | :------------------------------------------ |
| OpenMP offload    | `mpicc -O3 -mp=gpu  -gpu=cc90 example.c` | `mpicxx -O3 -mp=gpu  -gpu=cc90 example.cpp`     | `mpif90 -O3 -mp=gpu  -gpu=cc90 example.F90` |
| OpenACC           | `mpicc -O3 -acc=gpu -gpu=cc90 example.c` | `mpicxx -O3 -acc=gpu -gpu=cc90 example.cpp`     | `mpif90 -O3 -acc=gpu -gpu=cc90 example.F90` |
| C++ stdpar        |  N/A                                     | `mpicxx -O3 -stdpar=gpu  -gpu=cc90 example.cpp` |  N/A                                        |



<!--
## Building software using Spack

[Spack](https://spack.io) is a flexible package manager that can be
used to install software on supercomputers and Linux and macOS
systems. The basic module tree including compilers, MPI libraries and
many of the available software on CSC supercomputers have been
installed using Spack.

[See here for a short tutorial on how
to install software on CSC supercomputers using Spack](../support/tutorials/user-spack.md).
-->

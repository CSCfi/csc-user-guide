# Compiling & linking GPU-programs

In order to make application runnable on GPUs one has to use CUDA programming language, the OpenCL programming language or the OpenACC directive based approach.
For more information on these approaches look at:

CUDA

[https://github.com/csc-training/CUDA/blob/master/course-material/intro-to-cuda-csc.pdf](https://github.com/csc-training/CUDA/blob/master/course-material/intro-to-cuda-csc.pdf)
[https://devblogs.nvidia.com/parallelforall/even-easier-introduction-cuda/](https://devblogs.nvidia.com/parallelforall/even-easier-introduction-cuda/)

OpenACC

[https://devblogs.nvidia.com/parallelforall/getting-started-openacc/](https://devblogs.nvidia.com/parallelforall/getting-started-openacc/)


## Building CUDA applications

The CUDA compiler is called using the

```
nvcc
```
command. The CUDA compiler will take care of the device code compilation and pass the rest on to the C/C++/Fortran compiler loaded which can be changed by loading different versions of the gcc module.

When compiling CUDA code one should pass the compiler what compute capability the target device supports. Current GPU type is Volta V100. These GPUs support compute capability 7.0. To tell the compiler what compute capability to target for compute capability 7.0 (Volta V100) use:

```
-gencode arch=compute_70,code=sm_70
```
The gencode argument can be repeated multiple times so to compile for all architectures that might be in the system use:

```
-gencode arch=compute_60,code=sm_60 -gencode arch=compute_70,code=sm_70
```

## Building CUDA and MPI supported applications

Building CUDA programs with MPI can be done in two ways, one can either point the nvcc compiler to use the mpic++ compiler wrappers instead of gcc directly as a backend compiler or manually include and link MPI using the nvcc compiler.

To change what backend compiler nvcc uses pass the 
```
-ccbin
```
flag to nvcc:
```
nvcc -ccbin=mpic++ cuda-mpi.cu
```
Alternatively the linking can be done by the 
```
mpic++
```
wrapper by hand and not need to change the backend compiler:
```
nvcc -I$MPI_ROOT/include -L$MPI_ROOT/lib -lmpi cuda-mpi.cu
```
Please note that the actual include paths and libraries depend on the MPI library.

## Building OpenACC applications

To compile and link the application, the PGI environment must be used. Unless you have strict requirement for using C++ compiler

```
pgc++
```
it is often more convenient to deploy PGI's C-compiler with c99 standard extensions:

```
module purge
module load pgi/19.1 openmpi/3.1.4 cuda/10.0

pgcc -c99 -O3 -Minfo=all -acc -ta=tesla:cc60,cc70 acc_example.c -o acc_example
mpicc -c99 -O3 -Minfo=all -acc -ta=tesla:cc60,cc70 -o mpi-helloacc mpi-helloacc.c

```

Here we target compute capability 6.0 and 7.0.  Since we asked for compiler info via 

```
-Minfo=all
```
we will be rewarded by a rather exhaustive listing of messages.

Fortran OpenACC compilation goes as follows:

```
module purge
module load pgi/19.1 openmpi/3.1.4 cuda/10.0

pgfortran -O3 -Minfo=all -acc -ta=tesla:cc60,cc70 acc_example.F90 -o acc_example
mpifort -O3 -Minfo=all -acc -ta=tesla:cc60,70 -o mpi-helloacc mpi-helloacc.F90

```

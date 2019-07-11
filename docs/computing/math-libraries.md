# Mathematical libraries
## MKL (Intel Math Kernel Library)
Intel MKL is a mathematical library collection that is optimized for Intel processors. MKL can be used with both Intel and GNU compilers for Fortran and C/C++ programming. However cluster libraries (BLACS, ScaLAPACK and Cluster FFT functions) will work only with IntelMPI.

MKL includes the following groups of routines:

* BLAS (Basic Linear Algebra Subprograms)
* Sparse BLAS
* LAPACK (Linear Algebra PACKage)
* PBLAS (Parallel Basic Linear Algebra Subprograms)
* BLACS (Basic Linear Algebra Communication Subprograms)
* ScaLAPACK (Scalable LAPACK)
* Sparse Solver routines (direct sparse solver PARDISO, direct sparse solver DSS, iterative sparse solvers RCI, preconditioners for iterative solution process)
* Vector Mathematical Functions (VML, arithmetic, power, trigonometric, exponential, hyperbolic, special, and rounding)
* Vector Statistical Functions (VSL, random numbers, convolution and correlation, statistical estimates)
* General Fast Fourier Transform (FFT) Functions and Cluster FFT function
* Partial Differential Equations (PDE) support tools (Trigonometric Transform routines, Poisson routines)
* Nonlinear least squares problem solver routines
* Data Fitting functions (spline-based)
* Support Functions (timing, thread control, memory management, error handling, numerical reproducibility)

MKL library has two integer interfaces 32-bit (they call it: LP64) and 64-bit integer (ILP64) interfaces. So if someone is working with data arrays that have more than 231-1 elements the ILP64 interface is for it.

MKL has sequential and threaded programming modes. OpenMP and Intel® Threading Building Blocks threading technologies are supported.
See: [Improving performance with threading](https://software.intel.com/en-us/mkl-linux-developer-guide-improving-performance-with-threading) for more information.

Documentation links

* [Get Started guide](https://software.intel.com/en-us/get-started-with-mkl-for-linux) 
* [Developer Guide](https://software.intel.com/en-us/mkl-linux-developer-guide)
* [Developer reference C](https://software.intel.com/en-us/mkl-developer-reference-c)
* [Developer reference Fortran](https://software.intel.com/en-us/mkl-developer-reference-fortran)

## Usage of MKL
Load one of the supported compiler environments and make sure that mkl module has been loaded. If not give command:
```
module load mkl 
```
Because MKL includes many libraries and programming interfaces a link line can be a long list. To find a correct line for a case, specify your choices using [Intel Math Kernel Library (MKL) Link Line Advisor](https://software.intel.com/en-us/articles/intel-mkl-link-line-advisor) tool.

Some Link Line Advisor tips.

| Select Intel® product:  | choose the release which has been "module load mkl" |  
| :------------- |:-------------|
| Select OS | Linux |
| Select compiler  | choose the one that is in use |
| Select architecture | Intel 64 |
| Select dynamic or static linking | static/dynamic/single dynamic are all ok |
| Select interface layer | what is the integer range in your code (see also "help me" option)|
| Select threading layer | sequential and threaded programming modes are supported |
| Select OpenMP librarary | Select library if OpenMP was selected in above step  |
| Select cluster library | Select these If a code is using ScaLAPACK, BLACS or Cluster FFT |
| Select MPI library | IntelMPI |
| Select the Fortran 95 interfaces | Select this only if an application has a Intel MKL Fortran module interface. (if a code has a standard BLAS/LAPACK interface you do not select these) |
| Link with Intel® MKL libraries explicitly |Intel compiler supports variants of the *-mkl* compiler option, If link explicitly then all necessary MKL libraries will be in a link line (and not any *-mkl* variant).  See more info below. |


Copy the results (link line and compiler option results) into a Makefile. In command line compiling and linking case remove all brackets that the advisor gives (for example if there is a variable (MKLROOT) in brackets then remove the brackets.

When running OpenMP (threaded) application there are environment variables for threading control. Before running an application set the OMP_NUM_THREADS variable. For example 16 threads:

```
            export OMP_NUM_THREADS=16
```

**For quick linking Intel compiler** supports variants of the *-mkl* compiler option. The compiler links an application using the LP64 interface and it does not use Intel MKL Fortran module 95 interfaces.

* *-mkl* or *mkl=parallel* to link with threaded MKL (OpenMP (use *-qopenmp* option also) or TBB (use *-tbb* option also) ) 
* *-mkl=sequential* to link with sequential MKL
* *-mkl=cluster* to link with cluster libraries that use IntelMPI

for example
```
ifort -o my_fortran_binary my_fortran_code.f90 -mkl=sequential
```
Add option *-static-intel* if static linking is needed, dynamic linking is the default. If also option *-qopenmp-link=static* is in use
then OpenMP library will be linked statically otherwise not.

## MKL include files

This [link](https://software.intel.com/en-us/node/528477) has a include file table (for Fortran and C/C++).


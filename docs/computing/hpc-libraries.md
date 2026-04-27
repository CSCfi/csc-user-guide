# High-performance libraries

Various high-performance libraries for dense linear algebra, fast
Fourier transforms, *etc.* are available via the module system. Many
libraries are provided both as single-threaded and multithreaded
versions, multithreaded modules are designated with `omp` in the
module version. For pure MPI applications and applications calling
libraries from multiple threads it is recommended to use a single-
threaded library.

Availability of libraries may depend on the loaded compiler suite and
MPI environment, use `module avail` for finding out available
libraries. See the documentation of the library for
instructions on how to build against it. Note
that most modules set `LIBRARY_PATH` and `LD_LIBRARY_PATH` environment
variables so that the `-llibrary` linker flag is often enough. Most
modules set also `<library>_INSTALL_ROOT` environment variables that
can be utilized in custom build scripts. As an example, the `fftw`
library can be used as follows:

```bash
module load fftw
<compiler_command> -o myprog myprog.o -lfftw3
```

and the directory containing `include`, `lib`, *etc.* is found under the
`FFTW_INSTALL_ROOT` environment variable.


## Libraries on Roihu-CPU

Selected libraries available on Roihu-CPU:

- Dense linear algebra: `openblas`, `amdblis`
- Dense distributed linear algebra: `netlib-scalapack`
- Fast Fourier transforms: `fftw`

## Libraries on Roihu-GPU

Selected libraries available on Roihu-GPU:

- For Grace CPU:
  - Dense linear algebra: `nvhpc` (includes NVPL), `openblas`, `netlib-lapack`
  - Dense distributed linear algebra: `nvhpc` (includes NVPL), `netlib-scalapack`
  - Fast fourier transforms: `nvhpc` (includes NVPL), `fftw`
- For Hopper GPU:
  - CUDA (module `cuda`/`nvhpc`) includes libraries such as
    cublas, cufft, cusolver, ...


## Libraries on Puhti

Selected libraries available on Puhti:

- Dense linear algebra: `intel-oneapi-mkl`
- Dense distributed linear algebra: `intel-oneapi-mkl`, `netlib-scalapack`
- Fast fourier transforms: `fftw`

## Libraries on Mahti

Selected libraries available on Mahti:

- Dense linear algebra: `openblas`, `amdblis`, `amdlibflame`
- Dense distributed linear algebra: `netlib-scalapack`, `amdscalapack`
- Fast fourier transforms: `fftw`

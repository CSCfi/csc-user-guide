# High performance libraries

Various high performance libraries for dense linear algebra, fast
fourier transforms *etc.* are available via the module system. Many
libraries are provided both as single threaded and multithreaded
versions, multithreaded modules are designated with `omp` in the
module version. For pure MPI applications and applications calling
libraries from multiple threads it is recommended to use a single
threaded library.

Availibility of libraries may depend on the loaded compiler suite and
MPI environment, use `module avail` for finding out available
libraries. See the documentation of library for
instructions on how to build against that particular library. Note
that most modules set `LIBRARY_PATH` and `LD_LIBRARY_PATH` environment
variables so that `-llibrary` linker flag is often enough. Most
modules set also `<library>_INSTALL_ROOT` environment variables that
can be utilized in custom build scripts. As an example, `fftw`
library can be used as follows:

```bash
module load fftw
<compiler_command> -o myprog myprog.o -lfftw3
```

and the directory containing `include`, `lib`, *etc.* are found under
`FFTW_INSTALL_ROOT` environment variable.

## Libraries in Puhti

Selected libraries available in Puhti:

- Dense linear algebra: `intel-oneapi-mkl`
- Dense distributed linear algebra: `intel-oneapi-mkl`, `netlib-scalapack`
- Fast fourier transforms: `fftw`

## Libraries in Mahti

Selected libraries available in Mahti:

- Dense linear algebra: `openblas`, `amdblis`, `amdlibflame`
- Dense distributed linear algebra: `netlib-scalapack`, `amdscalapack`
- Fast fourier transforms: `fftw`

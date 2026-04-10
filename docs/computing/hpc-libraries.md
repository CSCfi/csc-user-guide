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


## Libraries on Roihu

!!! warning
    On Roihu-CPU and Roihu-GPU, many of the installed modules do not currently
    set the `CPATH`, `LIBRARY_PATH` or `LD_LIBRARY_PATH` environment variables.
    We expect to change this in the near future; until then, you may have to
    set them manually eg. when compiling an application that depends on a module.
    You can use `module show <modulename>` to see where the module files are located.
    Many modules define variable like `modulename_INSTROOT` that points to the
    installation directory once the module has been loaded. For example, `fftw`
    headers are in `$FFTW_INSTROOT\include` and the compiled library files are
    in `$FFTW_INSTROOT\lib`.


### Roihu-CPU

Selected libraries available on Roihu-CPU:

- Dense linear algebra: `openblas`
- Dense distributed linear algebra: `netlib-scalapack`
- Fast fourier transforms: `fftw`

### Roihu-GPU

Selected libraries available on Roihu-GPU:

- Dense linear algebra: `openblas`, `netlib-lapack`, `cublas`
- Dense distributed linear algebra: `netlib-scalapack`
- Fast fourier transforms: `fftw`


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

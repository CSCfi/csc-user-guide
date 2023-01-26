# Overview

If you cannot find a software suitable for your needs from the [list of pre-installed
applications](../../apps/index.md) or using `module spider`, it is possible to install
own software on CSC supercomputers. The installation procedure will vary based on your
specific application. There are, however, some universal rules you should be mindful of:

- You cannot use `sudo`, i.e. typical `sudo apt` or `sudo yum` commands you might find
  online will not work on CSC supercomputers.
- You cannot install into "standard" system locations, e.g. `/usr/bin`, `/usr/lib` etc.
  Instead, the best location for your own installations is the `/projappl` directory of
  your project.
- Use the fast local disk `$TMPDIR` when compiling to avoid stressing the parallel file
  system. Compiling applications typically cause quite a bit of I/O load.
- Many software might require some dependencies, e.g. [HPC libraries](hpc-libraries.md)
  such as FFTW or ScaLAPACK. Note that many of these are available as pre-installed
  modules, so you may not need to install *everything* from scratch.
- New software are not automatically added to your `$PATH`. To access the software,
  either provide the full path or add with `export PATH=/path/to/my/app/bin:$PATH`.

!!! info "Note"
    Don't hesitate to contact [CSC Service Desk](../../support/contact.md) if you
    encounter issues with installing your own software.

## Native installations

Native installations refer to applications that are installed directly to the system.
Typically, one downloads the source code of the software, compiles the code, and installs
to a location where the user has write-access, e.g. the project's `/projappl` directory.
Native installation from source code might sometimes be the only way to install an
application, and is recommended especially for software with few or no dependencies.

### Compiling

HPC software written using languages such as C, C++ or Fortran need to be compiled before
installing. Guidelines on compiling software on CSC supercomputer can be find from the
links below. A list of available HPC libraries that may need to be linked upon compiling
is also provided.

- [Compiling on Puhti](compiling-puhti.md)
- [Compiling on Mahti](compiling-mahti.md)
- [Compiling on LUMI](compiling-lumi.md)
- [HPC libraries](hpc-libraries.md)

### Spack

### Ready-made binaries

Ready-made binaries typically exhibit optimal performance only on the system on which
they have been compiled on. This applies especially for MPI codes, which should always
be re-compiled for best performance. However, if the binary you want to run is a simple
serial or threaded application, you can try running it directly.

## Containers

## Python/R environments

## More information

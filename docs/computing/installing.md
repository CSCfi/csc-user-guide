# Overview

It is possible to install own software on CSC supercomputers if you cannot find a software
suitable for your needs from the [list of pre-installed applications](../apps/index.md)
or using `module spider`. The installation procedure will vary based on your specific
application. There are, however, some general rules you should be mindful of:

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

!!! info "Help is available!"
    Don't hesitate to contact [CSC Service Desk](../support/contact.md) if you
    encounter issues with installing your own software.

## Native installations

Native installations refer to applications that are installed directly to the system.
Typically, one downloads the source code of the software, compiles the code, and installs
to a location where the user has write-access, e.g. the project's `/projappl` directory.
Native installation from source code might sometimes be the only way to install an
application, and is recommended especially for software with few or no dependencies.

### Compiling

HPC software written using programming languages such as C, C++ or Fortran need to be
compiled before installing. Guidelines on compiling software on CSC supercomputers can
be found from the links below. A list of available HPC libraries that may need to be
linked upon compiling is also provided.

- [Compiling on Puhti](compiling-puhti.md)
- [Compiling on Mahti](compiling-mahti.md)
- [Compiling on LUMI](compiling-lumi.md)
- [HPC libraries](hpc-libraries.md)

### Spack

[Spack](https://spack.io) is a flexible package manager that can be used to install
software on supercomputers and Linux and macOS systems. The basic module tree including
compilers, MPI libraries and many of the available software on CSC supercomputers have
been installed using Spack. Spack is similar to the [EasyBuild package manager extensively
used on LUMI](https://docs.lumi-supercomputer.eu/software/installing/easybuild/).

CSC provides user Spack modules on Puhti and Mahti that can be used to build software on top of the
available compilers and libraries. It is also possible to install different customized versions of
packages available in the module tree for special use cases. [See here for a short tutorial on how to
install software on CSC supercomputers using Spack](../support/tutorials/user-spack.md). Spack is
also available on [LUMI](https://docs.lumi-supercomputer.eu/software/installing/spack/).

### Ready-made binaries

Ready-made binaries typically exhibit optimal performance only on the system on which
they have been compiled on. This applies especially for MPI codes, which should always
be re-compiled for best performance. However, if the binary you want to use is a simple
serial or threaded application, you can try running it directly.

## Containers

Containerizing applications can be a very efficient way to install software and libraries,
especially if the application has complex dependencies such as most Python environments
([see below](#pythonr-environments)). CSC supercomputers support Apptainer/Singularity
containers, which are similar to Docker, but better suited for multi-user HPC systems. In
most cases, ready-made Docker containers can be easily converted into an Apptainer image.
Another option is to build your own container from scratch. More details on working with
containers in CSC's computing environment can be found from the links below:

- [Overview of containers](containers/overview.md)
- [Running containers](containers/run-existing.md)
- [Creating containers](containers/creating.md)
- [Tykky container wrapper](containers/tykky.md)

## Python/R environments

Best practice guidelines on installing own Python and R packages can be found in
the Python, R and Tykky container wrapper pages below.

- [Installing Python packages and environments](../apps/python.md)
- [Containerizing Conda and pip environments with Tykky](containers/tykky.md)
- [R package installations](../apps/r-env.md#r-package-installations)

Briefly, individual Python packages with no/few dependencies can be installed
alongside CSC's pre-installed Python modules with `pip install --user <package>`.
More complicated environments should always be containerized. This is accomplished
easily with [Tykky](containers/tykky.md).

Similarly, the pre-installed R module provided by CSC is a containerized environment
containing more than 1300 packages. If these do not suit your needs, you can install your
own packages into a project-specific location under `/projappl` and add this to your library
trees in R. [See here for specific details](../apps/r-env.md#r-package-installations).

## More information

- [Installing your own software](https://csc-training.github.io/csc-env-eff/part-2/installing/)
  (CSC Computing Environment slides and tutorials)

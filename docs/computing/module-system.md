# The module system

The module system enables managing several incompatible environments
within one computer. Use the module command to query available applications,
libraries or compiler suites and dynamically initialize them for use. 
The module system should be used both in interactive and batch jobs.

*Environment modules* provide a convenient way to set up everything
required by a particular application. Module system modifies the
environment variables of the user's shell so that the correct versions
of executables are in the path and linker can find the correct version
of needed libraries. For example, the command `mpicc` points to
different compilers depending of the loaded module.

CSC uses a recently developed version of environment modules called
**Lmod**. It is developed at Texas Advanced Computing Center (TACC) and
it is implemented using *Lua* programming language. More technical
details can be found from the [Lmod homepage].

[TOC]

## Basic usage

The syntax of the module commands is:

    module command module-name

The currently loaded modules, i.e. what your current environment is,
are listed with:

    module list

For general module information one uses command `module help`. For
example, to get more information about loaded module `intel`,
use:

    module help intel

Load new modules to your environment with `load` command, for
example load the `trilinos` module using:

    module load trilinos

Note that you can only load modules that are compatible with other
modules that you have loaded. That is, you can not load modules that are
conflicting with previously loaded modules, or modules that depend on
modules that have not been loaded.

Modules that are not needed or that are conflicting with other modules
can be unloaded using `unload`:

    module unload mkl

Most commonly used module commands.

|  Module command               |  Description                                  |
|-------------------------------|-----------------------------------------------|
| module help *modulename*      | Show information about a module.              |
| module load *modulename*      | Loads the given environment module.           |
| module unload *modulename*    | Unloads the given environment module.         |
| module list                   | List the loaded modules.                      |
| module avail                  | List modules that are available to be loaded. |
| module spider *name*          | Searches the entire list of possible modules. |
| module swap *module1 module2* | Replaces a module with a second module.       |

### Finding modules

You can list the modules that are compatible with your current module
set by using:

    module avail

Because of the hierarchical structure of the Lmod system you can not
load all installed modules using just one `module load` command. The
`avail` command does not show modules that can not be loaded due to
conflicts or unmet dependencies. Reason for these protective
restrictions is to prevent you from loading module combinations that do
not work.

You can get the list of all installed software packages using:

    module spider

You can also give the name or part of the name of the module as an
argument, for example:

    module spider int

will list all modules with string "int" in the name. More detailed
description of a module can be printed using the full module name with
version number, for example:

    module spider fftw/3.3.2

### Solving conflicts

As mentioned above, the module system does not let the user to load
conflicting modules. In these cases you have to solve these conflicts
before loading the module. In the easiest case the module system gives
you explicit guidance. For example, if you try to load a compiler module
on top of another one, you will get an error message:

      -bash-4.1$ module load gcc

    Lmod has detected the following error: You can only have one compiler module loaded at a time.
    You already have intel loaded.
    To correct the situation, please enter the following command:

      module swap intel gcc/4.8.2

Some modules depend on other modules. Also in these cases the
information from the module system is obvious, for example:

    -bash-4.1$ module load netcdf4

    Lmod has detected the following error: Cannot load module "netcdf4/4.3.0" without these modules loaded:
      hdf5-par/1.8.10

More complicated procedures are needed when the module is not compatible
with currently loaded compiler and/or MPI-library. In these cases the
`module avail` command does not even list the module and `module load`
command can not find it. Easiest way to check what environment is
required for the desired module is to use `module spider` command with
version information. For example:

    -bash-4.1$ module spider hypre/2.9.0b
    ------------------------------------------------------------------
     hypre: hypre/2.9.0b
    ------------------------------------------------------------------
      This module can only be loaded through the following modules:
           intel/12.1.5, intelmpi/4.0.3
           intel/13.0.1, intelmpi/4.1.0
           intel/13.1.0, intelmpi/4.1.0
    ...

  
So in this case you will have to load one the listed environments before
you can proceed with `module load` command.

## Advanced topics

In general, libraries built with one compiler need to be linked with
applications using the same compiler. For example, you can not use the
MPI Fortran90 module compiled with Intel compilers with *gfortran*, but
you have to use a version compiled with *gfortran*. Environment modules
have several mechanisms that prevent the user from setting up a
non-working environment.

The module hierarchy helps us to keep the compiler and MPI library
settings compatible with each other. In practice, for each supported
compiler there is a module for a supported MPI library. When user
switches the compiler module, the module system tries to find the
correct versions of loaded modules:

    -bash-4.1$ module list
    Currently Loaded Modules:
      1) intel/12.1.5 2) mkl/10.3.11 3) intelmpi/4.0.3

    -bash-4.1$ module switch intel gcc
    Due to MODULEPATH changes the following modules have been reloaded:
     1) mkl/10.3.11 2) intelmpi/4.0.3

If a correct version is not found, the module system *deactivates* these
modules. In practice, the module is unloaded, but it is marked so that
when the compiler/MPI configuration is changed, the system tries to find
a correct version automatically.

This hierarchy is implemented by changing the **$MODULEPATH** variable.
Every compiler module adds its own path to the module path so that
software modules compatible with that specific compiler can be listed.
When the compiler module is unloaded, this path is removed from the
module path. Same applies also to the MPI modules.

### Using your own module files

If you want to use modules to control the software packages that you
install by yourself, you can add your own modules files to your home
directory. For example, if you add the module files to
**$HOME/modulefiles**, you can access them after you add the path to the
modules search path using command:

    module use $HOME/modulefiles

  [Lmod homepage]: http://www.tacc.utexas.edu/tacc-projects/mclay/lmod

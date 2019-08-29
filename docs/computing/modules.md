# Module system

The module system enables managing several incompatible software environments
within one computer. Use the module command to query available applications,
libraries or compiler suites and dynamically initialize them for use.
The module system should be used both in interactive and batch jobs.

*Environment modules* provide a convenient way to set up everything
required by a particular application. Module system modifies the
environment variables of the user's shell so that the correct versions
of executables are in the path and linker can find the correct version
of needed libraries. For example, the command `mpicc` points to
different compilers depending on the loaded module.

CSC uses environment modules called
**Lmod**. It is developed at Texas Advanced Computing Center (TACC) and
is implemented using the *Lua* programming language. More technical
details can be found from the [Lmod homepage].

[TOC]

## Basic usage

The syntax of the module commands is:

```text
module command module-name
```

The currently loaded modules, i.e. what your current environment is,
are listed with:

```text
module list
```

For general information about a module, one uses command `module help`. For
example, to get more information about loaded module `intel`, use:

```text
module help intel
```

Load new modules to your environment with `load` command, for
example to load the `intel-mpi` module use:

```text
module load intel-mpi
```

Note that you can only load modules that are compatible with other
modules that you have loaded. That is, you can not load modules that are
conflicting with previously loaded modules, or modules that depend on
modules that have not been loaded.

Modules that are not needed or that are conflicting with other modules
can be unloaded using `unload`:

```text
module unload intel-mkl
```

Here is a list of most commonly used module commands:

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

```text
module avail
```

Because of the hierarchical structure of the Lmod system you can not
load all installed modules using just one `module load` command. The
`avail` command does not show modules that can not be loaded due to
conflicts or unmet dependencies. Reason for these protective
restrictions is to prevent you from loading module combinations that do
not work.

You can get the list of all installed software packages using:

```text
module spider
```

You can also give the name or part of the name of the module as an
argument, for example:

```text
module spider int
```

will list all modules with string "int" in the name. More detailed
description of a module can be printed using the full module name with
version number, for example:

```text
module spider fftw/3.3.8
```

### Solving module dependencies

Some modules depend on other modules. In these cases the
information from the module system is an error message, for example:

```text
$ module load parallel-netcdf

Lmod has detected the following error:  These module(s) exist but
cannot be loaded as requested: "parallel-netcdf"
Try: "module spider parallel-netcdf" to see how to load the module(s).

$ module spider parallel-netcdf

----------------------------------------------------------------------------
  parallel-netcdf:
----------------------------------------------------------------------------
     Versions:
        parallel-netcdf/1.8.0

----------------------------------------------------------------------------
  For detailed information about a specific "parallel-netcdf" module
  (including how to load the modules) use the module's full name.
  For example:

$ module spider parallel-netcdf/1.8.0
----------------------------------------------------------------------------
```

In these cases the
`module avail` command does not even list the module and `module load`
command can not find it. Easiest way to check what environment is
required for the desired module is to use `module spider` command with
version information. For example:

```text
$ module spider parallel-netcdf/1.8.0
------------------------------------------------------------------
 parallel-netcdf: parallel-netcdf/1.8.0
------------------------------------------------------------------
 You will need to load all module(s) on any one of the lines below before
 the "parallel-netcdf/1.8.0" module is available to load.

 gcc/9.1.0  hpcx-mpi/2.4.0
 intel/19.0.4  hpcx-mpi/2.4.0
...
```

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

```text
$ module list
Currently Loaded Modules:
 1) gcc/9.1.0   2) hpcx-mpi/2.4.0   3) parallel-netcdf/1.8.0

$ module swap gcc intel
Due to MODULEPATH changes the following modules have been reloaded:
 1) hpcx-mpi/2.4.0     2) parallel-netcdf/1.8.0

$ module list
Currently Loaded Modules:
 1) intel/19.0.4   2) hpcx-mpi/2.4.0   3) parallel-netcdf/1.8.0
```

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

```text
module use $HOME/modulefiles
```

  [Lmod homepage]: https://lmod.readthedocs.io/en/latest/

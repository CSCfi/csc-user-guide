# The module system

The module system enables managing several mutually incompatible software environments
within one computer. Use the `module` command to query the available applications,
libraries or compiler suites, and dynamically initialize them.
The module system should be used for both interactive and batch jobs.

The **environment modules** provide a convenient way to set up everything
required by a particular application. The module system modifies the
environment variables of the user's shell so that the correct versions
of executables are in the path and the linker can find the correct version
of the required libraries. For example, the command `mpicc` points to
different compilers depending on the module loaded.

CSC uses **Lmod** environment modules. They are developed at the Texas Advanced Computing
Center (TACC) and implemented using the _Lua_ programming language. More technical
details can be found on the [Lmod homepage].

[TOC]

## Basic usage

The syntax of the module command:

```text
module command modulename
```

Listing the modules loaded (including your current environment):

```text
module list
```

The command `module help` provides general information about a module. For
example, to get more information about the module `intel-oneapi-compilers`, use:

```text
module help intel-oneapi-compilers
```

Load new modules to your environment with the command `load`. For
example, to load the `intel-oneapi-mpi` module, use:

```text
module load intel-oneapi-mpi
```

Note that you can only load modules that are compatible with the other
loaded modules. That is, you cannot load modules that are
conflicting with previously loaded modules, or modules that depend on
modules that have not been loaded.

Modules that are not needed or conflict with other modules
can be unloaded using `unload`:

```text
module unload intel-oneapi-mkl
```

### The most commonly used module commands {#module-commands-table}

|  Module command                   |  Description                                                                                        |
|-----------------------------------|-----------------------------------------------------------------------------------------------------|
| module help *modulename*          | Information about a module.                                                                         |
| module load *modulename*          | Loads the default version of the environment module.                                                |
| module load *modulename/version*  | Loads specific version of the module.                                                               |
| module unload *modulename*        | Unloads the given environment module.                                                               |
| module list                       | List the loaded modules.                                                                            |
| module avail                      | List all modules that are available to be loaded (i.e. compatible with your current environment).   |
| module spider                     | List all existing modules.                                                                          |
| module spider *modulename*        | Search the entire list of existing modules.                                                         |
| module spider *modulename/version*| Gives information on how to load the module (prerequisites etc).                                    |
| module swap *modulename1 modulename2* | Replaces a module with another (and tries to re-load compatible versions of other loaded modules).  |
| module show *modulename*          | Show commands in the module file.                                                                   |
| module purge                      | Unloads all modules.                                                                                |

### Finding modules

You can list the modules that are compatible with your current module
set by using:

```text
module avail
```

Because of the hierarchical structure of the _Lmod_ system, it is not possible to
load all installed modules simply using a single `module load` command. The
`avail` command does not show modules that cannot be loaded due to
conflicts or unmet dependencies. These protective
restrictions prevent the loading of incompatible module combinations.

List all installed software packages:

```text
module spider
```

List modules by name:

```text
module spider int
```

The above command will list all modules with the string _int_ in their name. A more detailed
description of a module can be printed using the full module name with a version number:

```text
module spider intel-oneapi-mkl/2022.1.0
```

### Solving module dependencies

Some modules depend on other modules. If a required module is missing, the module system
prints an error message:

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
        parallel-netcdf/1.12.2

----------------------------------------------------------------------------
  For detailed information about a specific "parallel-netcdf" module
  (including how to load the modules) use the module's full name.
  For example:

$ module spider parallel-netcdf/1.12.2
----------------------------------------------------------------------------
```

In such cases, the `module avail` command excludes the module from the list and the
`module load` command cannot find it. The easiest way to find out the required environment
is to use the `module spider` command with the version information. For example:

```text
$ module spider parallel-netcdf/1.12.2
------------------------------------------------------------------
 parallel-netcdf: parallel-netcdf/1.12.2
------------------------------------------------------------------
 You will need to load all module(s) on any one of the lines below before
 the "parallel-netcdf/1.12.2" module is available to load.

  gcc/11.3.0  openmpi/4.1.4
  gcc/9.4.0  openmpi/4.1.4
  intel-oneapi-compilers-classic/2021.6.0  intel-oneapi-mpi/2021.6.0
...
```

In this case, you will have to load one of the listed environments before
proceeding with `module load` command.

## Advanced topics

In general, applications and their dependencies should be compiled and
linked using the same compiler. In some cases this is a strict
requirement. For example, you can not use the _MPI Fortran90_ module
compiled with Intel compilers with _gfortran_. Environment modules
have several mechanisms that prevent the user from setting up an
incompatible environment.

The module hierarchy contributes to keeping the compiler and MPI library
settings compatible with each other. In practice, for each supported
compiler, there is a module for a supported MPI library. When the user
switches the compiler module, the module system tries to find the
correct versions of the loaded modules:

```text
$ module list
Currently Loaded Modules:
 1) gcc/11.3.0   2) openmpi/4.1.4   3) parallel-netcdf/1.12.2

$ module swap gcc intel-oneapi-compilers-classic

Inactive Modules:
 1) parallel-netcdf/1.12.2

Due to MODULEPATH changes the following modules have been reloaded:
 1) openmpi/4.1.4

$ module list
Currently Loaded Modules:
 1) intel-oneapi-compilers-classic/2021.6.0   2) openmpi/4.1.4

Inactive Modules:
 1) parallel-netcdf/1.12.2
```

If the correct version is not found, the module system _deactivates_ these
modules (see above). In practice, the module is unloaded, but it is marked so that
when the compiler/MPI configuration is changed, the system tries to find
the correct version automatically.

This hierarchy is implemented by changing the `$MODULEPATH` variable.
Every compiler module adds its own path to the module path so that
the software modules compatible with that specific compiler can be listed.
When the compiler module is unloaded, this path is removed from the
module path. The same applies to the MPI modules as well.

### Using your own module files

If you want to control the software packages using modules
installed by yourself, you can place your own module files in your home
directory. For example, if you include module files in
`$HOME/modulefiles`, you can access them after adding the path to the
module search path using the command:

```text
module use $HOME/modulefiles
```

If you want to study existing module files, `module show <modulename>` shows also the filename of the module file.

  [Lmod homepage]: https://lmod.readthedocs.io/en/latest/

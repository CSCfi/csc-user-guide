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

## Roihu GPU and CPU specific modules

On Roihu the GPU and CPU paritions exist in separate environments due to the
different base architecture of the CPU and GPU nodes, for more information see
[Getting started with Roihu](../support/tutorials/roihu.md).

Consequently, software must be built separately for the GPU and CPU node
architectures, therefore there are different, independent software modules
for the GPU and CPU parititions, accessible from the corresponding login nodes;
`roihu-gpu.csc.fi` and `roihu-cpu.csc.fi` respectively.

Both GPU and CPU environments have a collection of modules loaded by default, that
differ slightly.

### GPU default modules

The default modules in the GPU environment are as follows:

```bash
module list

Currently Loaded Modules:
  1) csc-tools/default (S)   2) gcc/14.3.0   3) cuda/12.9.1   4) openmpi/5.0.10   5) openblas/0.3.30   6) StdEnv

  Where:
   S:  Module is Sticky, requires --force to unload or purge
```

### CPU default modules

The default modules in the CPU environment are as follows:

```bash
module list

Currently Loaded Modules:
  1) csc-tools/default (S)   2) gcc/15.2.0   3) ucx/1.20.0   4) openmpi/5.0.10   5) openblas/0.3.30   6) StdEnv

  Where:
   S:  Module is Sticky, requires --force to unload or purge
```

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
example, to get more information about the module `openblas`, use:

```text
module help openblas
```

Load new modules to your environment with the command `load`. For
example, to load the `openblas` module, use:

```text
module load openblas
```

Note that you can only load modules that are compatible with the other
loaded modules. That is, you cannot load modules that are
conflicting with previously loaded modules, or modules that depend on
modules that have not been loaded.

Modules that are not needed or conflict with other modules
can be unloaded using `unload`:

```text
module unload openblas
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
module spider mpi
```

The above command will list all modules with the string _mpi_ in their name. A more detailed
description of a module can be printed using the full module name with a version number:

```text
module spider openmpi/5.0.10
```

### Solving module dependencies

Some modules depend on other modules. If a required module is missing, the module system
prints an error message:

```text
$ module load boost/1.88.0

Lmod has detected the following error:  These module(s) or extension(s) exist but cannot be loaded as requested:
"boost/1.88.0"
   Try: "module spider boost/1.88.0" to see how to load the module(s).
   Or load any one of these options:
      module load aocc/5.0.0 boost/1.88.0
      module load gcc/15.2.0 boost/1.88.0
```

In such cases, the `module avail` command excludes the module from the list and the
`module load` command cannot find it. The easiest way to find out the required environment
is to use the `module spider` command with the version information. For example:

```text
$ module spider boost/1.88.0

-----------------------------------------------------------------------------------------------------------------------------------
  boost: boost/1.88.0
-----------------------------------------------------------------------------------------------------------------------------------

    You will need to load all module(s) on any one of the lines below before the "boost/1.88.0" module is available to load.

      aocc/5.0.0
      gcc/15.2.0

    Help:
      Boost provides free peer-reviewed portable C++ source libraries,
      emphasizing libraries that work well with the C++ Standard Library.
      Boost libraries are intended to be widely useful, and usable across a
      broad spectrum of applications. The Boost license encourages both
      commercial and non-commercial use.
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
  1) gcc/15.2.0   2) ucx/1.20.0   3) openmpi/5.0.10   4) parallel-netcdf/1.14.1

$ module swap gcc aocc

Inactive Modules:
  1) openmpi     2) parallel-netcdf     3) ucx/1.20.0

$ module list

Currently Loaded Modules:
  1) aocc/5.1.0

Inactive Modules:
  1) ucx/1.20.0   2) openmpi   3) parallel-netcdf
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

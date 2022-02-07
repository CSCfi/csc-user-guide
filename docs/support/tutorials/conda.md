# Conda best practices

!!! warning "NOTE: Please do not use conda on CSC's supercomputers!"

    **CSC has deprecated the use of Conda installations** as these perform poorly on
    shared parallel file systems like those used in Puhti and Mahti. We also
    strongly recommend users moving away from their own Conda-based installations.
    Read more on our separate [Conda deprecation page](../deprecate-conda.md).

<br/>
<hr/>

## What is conda

[Conda] is

1. a software install tool that can manage software dependencies, and
2. a user (shell) environment management tool.

It is a bit similar to yum or apt, plus python virtual environments, if you are
familiar with those. Conda

- packages can contain software written in any language
- works the same in Linux, Mac OS and Windows
- works the same in machines from laptops to large clusters
- packages contain pre-compiled binaries, and the recipe they we built with
- does not require administrator privileges to run, unlike yum and apt
- can install software into multiple install roots, Conda environments
- is primarily designed for single user usage

Note, the term "Conda environment" relates to two somewhat separate concept. It
can refer either or both of

1. one of the user's conda software install root directories, and
2. the user's shell environment that has been modified with
   `conda activate ...` command.


## When to use Conda and what kind of software you should install with it?

Conda is well suited for installing desktop type software, and complex, possibly
conflicting, package dependencies in Python, LaTex, or R, for example. It is
designed to be used on personal software installs. Naturally, the software
installed with it can be made available to others, too. The configuration files,
[environment.yaml], for the conda software environments can be easily shared
with others.

### When to yum, apt, or brew

If you are running on a personal Linux machine, such as laptop, have
administrator privileges, and intend to run the program only on your personal
machine, using yum, apt or homebrew may be more convenient.

### When to build from the sources

If you are installing a MPI parallel and/or performance optimized application on
a HPC cluster, follow the instructions of the computing center about building
software from the sources. The software dependencies in HPC environments are
usually handled using environment module system. For development work, using a
laptop and possibly conda or yum/apt/homebrew for installing dependencies and
development tools, is still likely more convenient.

There are package and management tools for building and installing HPC software
from sources, such as [Spack]. Those are not as widely used as Conda, and often
require some knowledge of the software build process, but they do compile and
optimize the software for the particular architecture.

## Conda channels (package repositories)

Conda channels are similar to Linux distributions' repositories, such as Ubuntu,
CentOS or Debian. The most popular Conda channels are commercially maintained
Anaconda, and community maintained Conda-forge.

## How to install Conda

Install Conda by downloading the suitable installer script from [Miniconda], see
detailed instructions in the Example chapter below. Miniconda contains only a
minimal set of packages, that allow you to run conda commands and install
additional packages from different channels.

### Python versions in the install scripts

You can use python 3 version to install environments with python 2 interpreter,
and vice versa. I recommend downloading python 3 version, which by default
installs python 3 in Conda's `base` environment.

### Miniconda or Anaconda

On a personal workstation you can also install [Anaconda] distribution, which in
addition to minimal set of packages, installs also a large number of packages
from Anaconda channel. You can also install the same packages later from
Anaconda channel if you start with Miniconda. The only practical difference is
just in what is installed by default.

## How to find if there is a conda package for a software?

First, google `conda <name>`, where `<name>` is the name of the package. Similar
to using yum, apt or homebrew, guessing the name of the package that contains
particular application may be the most difficult task. If there is a Conda
package for the software, Google hits usually contain the exact names of the
packages and in which channel (repository) they can be installed from.

## What could possibly go wrong?

### Running different conda than you think

If you follow the example instructions below, conda command is actually set up
as a shell function, that refers to an environment variable `CONDA_EXE`. You can
see how it is defined with command `type conda`. It is possible to have other
conda command active by accident, too. They can sneak into shell environment
from an earlier miniconda or anaconda installs, or from some `module load ...`
command. Commands `which conda` and `echo $CONDA_EXE` may reveal those. The
lesson here is that make sure you are using only a single conda setup at a time.

### Shell initialization and other configuration files modifying user's shell environment

Many software install documentations and scripts, including Miniconda, give an
option of adding setup lines into user's shell initialization scripts,
`.bashrc`, `.profile`, etc, which modify user's shell environment so that a
particular software is automatically set up for each new shell or login. This is
convenient, but may lead to conflicts that are hard to find later. A safer
practice is to put all these setup commands in separate scripts, let's say into
user's `~/setup_scripts/` folder, and then explicitly source them only when
necessary.

### Messed up environment variables

There are many environment variables that are used to override or extend the
defaults in how commands and libraries are searched, or which directories
particular applications use. Examples of such environment variables are
`PATH`, `LD_LIBRARY_PATH`, `CONDA_*`, and `PYTHONPATH`.

As a general safe practice, try to rely on these environment variables as little
as possible. Some environment module systems, such as the one in puhti.csc.fi,
do extensively depend on modifying the values of environment variables. In
puhti.csc.fi it might be a good idea to run

```bash
module purge
```

before starting to use Conda.

### Mixing packages from different channels, or simply outdated packages

Please note that installing packages from different channels to a single Conda
environment does not always work. That is a bit similar to trying to mix
packages from Ubuntu and Debian. The solution is to simply set up separate Conda
environments for different tasks or projects if in doubt about the
compatibility.

Some of the smaller channels are not always up-to-date or properly maintained,
and packages from those may break your Conda environment. Fortunately you can do
rollbacks on Conda environments, or simply try new packages in testing/staging
environments before including them into your favorite environments.

### Sorting out configuration related problems

 The best friends to sort out conda configuration or shell environment related
 problems are the following commands:

```bash
# Are you using the version you think you are?
conda --version

# The single most useful command to check configuration settings?
conda info

# Is there something extra in the command or library search paths?
echo $PATH $LD_LIBRARY_PATH

# You may need to unload some modules?
module list

# Are some environment variables overriding the default conda configuration?
env | grep ^CONDA_

# Is something set up by default at every login or new shell?
cat ~/.bashrc ~/.bash_profile ~/.profile
```

### Sorting out unmaintained or otherwise broken packages

If you encounter a broken package, a package that does not have the feature you
need, or an outdated package, it is possible to re-build the binary package from
source by yourself. The details of this are slightly out of the scope of this
document, but building Conda packages is perfectly doable. Basically, you need
to install `conda-build` Conda package, modify the files `meta.yaml` and
`build.sh` in the `<condaroot>/pkgs/<package>/info/recipe` sub-folder, rebuild
the package, and install it into a local channel.

## Examples

The examples below should work without modifications in 
puhti.csc.fi. The basic usage is the same in other machines, other clusters,
laptops, etc.

### Installing conda

If you are planning to install your own Conda, instead of using system
applications that are installed with Conda by someone else, like bioconda or
geoconda in puhti.csc.fi, I recommend installing a project specific copy of Miniconda3.

As Conda packages may take significant storage space it is not recommended to 
to install Miniconda3 to your home directory. In stead you should install it to 
the [ProjAppl]( ../../computing/disk.md) directory of your Puhti project.

To get an overview of your directories in Puhti, run command:
```text
csc-workspaces 
```
You can pick the path of your ProjAppl directory from the output of the command above or if you 
are mostly using just one project in Puhti, you can set the environment variables 
$SCRATCH and $PROJAPPL to point to the scratch and projappl directories of a CSC project. 
This setting can be done with command:
```text
csc-workspaces set <project>
```
Below we assume that $PROJAPPL has been defined. After that the actual installation 
can be done with commands:

```
bash
cd $SCRATCH
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh -b -p $PROJAPPL/miniconda3
```

All conda files will be installed under the chosen Conda root install directory,
here `$PROJAPPL/miniconda3`, with the exception of `.condarc`, which
will be in the user's home directory. By default, which is also a recommended
practice, all files installed subsequently with conda go under the same install
root.

The option `-b` simply skips some questions and adding the automatic
initialization lines into user\'s `.bash_profile`.

The Conda install root directory contains basically the following
subdirectories:

- `bin`, `lib`, ... the usual Linux directories for the Conda `base`
  environment
- `envs` where all Conda environments will reside
- `pkgs` Conda package cache

### Activating conda tool

If you installed Conda into directory `$PROJAPPL/miniconda3`, you can
activate conda tool with the initialization script:

```bash
source $PROJAPPL/miniconda3/etc/profile.d/conda.sh
```

This simply sets couple of shell environment variables, and conda command as a
shell function. If you allowed the install script to modify your `.bashrc`, this
step is unnecessary.

When activating a new conda install first time, it's a good idea to run

```bash
conda info
```

to verify that the Conda configuration is ok.

### Installing packages, named environments, environment.yaml

I recommend

1. installing all conda packages into named environments, which go under the
   `envs` subdirectory, instead of installing them into the `base` environment
   directly under conda install root, and
2. using environment.yaml configuration files instead of adding packages to
   environments directly from the command line with `conda install ...`
   commands.

In practice, you only need to create a single environment.yaml file for each
your environments, see examples below, and then use a single conda command

```bash
conda env create -f <envname>.yaml
```

to create the whole environment.

Updating the packages, or adding new packages to the an existing environment is
done by modifying the environment.yaml file, and then running

```bash
conda env update -f <envname>.yaml
```

### Activating conda environment

Activating Conda environment is done simply by

```bash
conda activate <envname>
```

This prepends the path to the Conda environment's `bin` directory to your shell
environment's `PATH` environment variable, so that different commands are first
searched from the Conda environment, and modifies the prompt so that it shows
the name of the currently active Conda environment. This command also sources
the activation hooks for this Conda environment in directory
`<envroot>/etc/conda/activate.d/`, created by the installed packages to set
application specific environment variables.

In supercomputer environments similar tasks for system software are often done
using environment module system, and `module load ...` commands.

### Examples of environment.yaml files

As the first example, let's use the environment.yaml file [conda-docs-env.yaml],
that can be used to install [mkdocs] with couple of plugins:

```yaml
name: docs
channels:
  - conda-forge
dependencies:
  - python
  - pip
  - pip:
      - mkdocs
      - pymdown-extensions
      - mkdocs-windmill
```

The first field, `name`, simply defines the name of the Conda environment. The
second field, `channels`, list from which channels the packages are pulled from
to this environment. Field `dependencies` lists the actual Conda packages that
are installed into the environment. Note, that Conda integrates nicely with
Python pip, and you can also include pip packages, that are installed using pip,
into the Conda environment (Sometimes you need to clean pip caches that are not
under Conda's control).

Conda uses a "channel priority" for determining where to install packages from,
i.e. it tries first to install packages from the first listed channel. If no
package versions are specified, Conda always installs the latest versions.

As a second, more complex example, let's look at an environment for C program development, defined in file [c-ide.yaml]

```yaml
name: c-ide
channels:
  - /projappl/project_123456/conda/channels/csc-forge-based
  - conda-forge
  - defaults
  - anaconda
dependencies:
  - git
  - font-ttf-source-code-pro
  - emacs
  - global
  - ctags
  - clangdev
  - cmake
  - make
```

The first listed channel is in a local directory. In this case it is used as a
repository for a self created package, here [GNU Global], which does not(?) have
an existing Conda package in Anaconda or Conda-forge repositories. Naturally
this environment can only be created in machine puhti.csc.fi, if package
`global` is included. TODO: Move the local channel to CSC's Allas object
storage!

Adding the environment.yaml file to the source repository of your project is
probably an excellent idea. This allows an easy way to replicate the same
environment in multiple machines. For example, you can do development
conveniently in a local machine and then copy the environment to production
platform. Also, you can easily share the environment with other developers.

### Removing unused packages

Conda, as other software packaging solutions that install also all the
dependencies, tends to eat up disc space. If running out of space, it is quite
easy to remove old and unused packages.

Commands

```bash
conda env list
conda env remove -n <envname>
conda clean -a
```

list the created environments, remove the named environment `<envname>`, and
remove unused packages from the local package cache `pkgs`, respectively.

## Creating environments so that other user's can access them

Giving other users an access to your Conda environment is as easy as giving them
read access to the directory containing the environment, in principle. If you use $PROJAPPL in 
Puhti this is the defult setting.

In other environmnets, like a local server or a Virtual Machine it is very easy to update packages, 
and then forget to give read access to the updated files. Also, some additional considerations need to be made, if
multiple persons are maintaining the environment, and accidental overwrites
and other mistakes are to be avoided.

Probability of these mistakes can be minimized by creating a separate
project/Unix group and user accounts for environment maintainers, and then
performing the environment maintenance task within a special shell environment.
Some ideas for the shell environment setup can be found in file
[bash_profile_extras.sh]. 

[Conda]: https://docs.conda.io/en/latest
[environment.yaml]: https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file
[Spack]: https://spack.io
[Miniconda]: https://docs.conda.io/en/latest/miniconda.html
[Anaconda]: https://www.anaconda.com/distribution
[conda-docs-env.yaml]: conda/conda-docs-env-1.0.yaml
[mkdocs]: https://www.mkdocs.org
[c-ide.yaml]: conda/c-ide.yaml
[GNU Global]: https://www.gnu.org/software/global
[bash_profile_extras.sh]: conda/bash_profile_extras.sh

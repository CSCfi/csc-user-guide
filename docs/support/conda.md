# Using Conda to install packages best practices

*Juha Lento, 2019-05-21, CSC*

Please read the text, and do not immediately skip to the cooking book
instructions at the end :)

## What is conda

[Conda] is a software install tool that can manage software dependencies. It is
a bit similar to yum or apt, plus python virtual environments, if you are
familiar with those. Conda

- can be used to install packages in any language
- works the same in Linux, Mac OS and Windows
- works the same in machines from laptops to large clusters
- packages contain pre-compiled binaries, and the recipe they we built with
- does not require administrator privileges to run, unlike yum and apt
- can create multiple separate software stack roots, called Conda environments
- is designed for single user usage

NOTE: The term "environment" relates to two separate concepts, here. The term
*(1) Conda environment* (similar to virtual environment in Python) refers to the
root of one of the user's software stack root directories, basically. The
activation of a Conda environment simply means that the path to the `/bin`
directory of a Conda software stack root is appended to the user's *(2) shell
environment*'s `PATH` environment variable.

## When to use Conda and what kind of software you should install with it?

Conda is especially suitable for installing desktop type software, and complex,
possibly conflicting, package dependencies in Python, LaTex, or R, for example.
It is designed to be used on personal software installs, but the software
installed with it can be made available to others, too. The configuration files, [environment.yaml], for the conda software environments can be easily shared with others.

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

There are package and environment management tools for building and installing
HPC software from sources, such as [Spack]. Those are not as widely used as
Conda, but they do compile and optimize the software for the particular
architecture, and can do installs system wide.

## Conda channels (package repositories)

Conda channels are similar to Linux distribution's repositories, such as Ubuntu,
CentOS or Debian. The most popular Conda channels are Anaconda (commercially
maintained) and Conda-forge (community maintained).

## How to install conda

Install Conda by downloading the suitable installer script from [Miniconda].
Miniconda contains only a minimal set of packages, that allow you to run conda
commands and install additional packages from different channels.

### Python versions in the install scripts

You can use python 3 version to install environments with python 2 interpreter,
and vice versa. I recommend downloading python 3 version, which by default
installs python 3.

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

If you follow the instructions below, conda command is actually set up as a
shell function, that refers to an environment variable `CONDA_EXE`. You can see
how it is defined with command `type conda`. Now, depending on the value of the
environment variable `PATH`, there might be other conda commands in the path.
For example, if you load bioconda module in taito.csc.fi, you may see the
following confusing output:

```bash
$ echo $CONDA_EXE
/wrk/jle/DONOTREMOVE/conda/miniconda3/bin/conda
$ which conda
/homeappl/appl_taito/bio/bioconda/miniconda2/bin/conda
```

The lesson here is that make sure you are using only a single conda setup at a
time.

### Shell initialization and other configuration files modifying user's shell environment

Many software install documentations and scripts, including Miniconda, give an
option of adding setup lines into user's shell initialization scripts,
`.bashrc`, `.profile`, etc, which modify user's shell environment so that a
particular software is automatically set up for each new shell or login. This is
convenient, but may lead to conflicts that are hard to find later. A safer
practice is to put all these setup commands in separate scripts, let's say into
user's `~/setup_scripts/` folder, and then explicitly source them only when
necessary.

Note, that Conda also maintains it's own configuration file `~/.condarc`.

### Messed up environment variables

There are many environment variables that are used to override or extend the
defaults in how commands and libraries are searched, or which directories
particular applications use. Examples of such environment variables are
`PATH`, `LD\_LIBRARY\_PATH`, `CONDA\_\*`, and `PYTHONPATH`.

As a general safe practice, try to rely on these environment variables as little
as possible. Some environment module systems, such as the one in taito.csc.fi,
do extensively depend on modifying the values of environment variables. In
taito.csc.fi it might be a good idea to run

```bash
module purge
```

before starting to use Conda environments.

### Mixing packages from different channels, or simply outdated packages

Please note that installing packages from different channels to a single Conda
environment does not always work. That is a bit similar to trying to mix
packages from Ubuntu and Debian. The solution is to simply set up separate Conda
environments for different tasks if in doubt about the compatibility.

Some of the smaller channels are not always up-to-date or properly maintained,
and packages from those may break your environment. Fortunately you can do
rollbacks on Conda environments, or simply try new packages in separate
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

# You may need to purge some modules?
module list

# Are some environment variables overriding the default conda configuration?
for e in $(echo ${!CONDA_*}); do echo "$e=${!e}"; done

# Is something set up by default at every login or new shell?
cat ~/.bashrc ~/.bash_profile ~/.profile
```

### Sorting out broken packages

If you encounter a broken package, a package that does not have the feature you
need, or an outdated package, it is possible to re-build the package yourself.
The details of this are slightly out of the scope of this document, but building
Conda packages perfectly doable. Basically, you need to install `conda-build`
Conda package, modify the files `meta.yaml` and `build.sh` in the `info/recipe`
sub-folder in the Conda package.

## Examples

The examples below should work without modifications in taito.csc.fi. The basic
usage is the same in other machines, other clusters, laptops, etc.

### Installing conda

If you are planning to install Conda packages yourself, instead of using
applications that are installed with Conda by someone else, like bioconda or
geoconda, I recommend installing a personal copy of Miniconda3 as

```
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh -b -p $WRKDIR/DONOTREMOVE/miniconda3
```

All conda files will be installed under the chosen Conda root install directory,
here `$WRKDIR/DONOTREMOVE/miniconda3`, with the exception of `.condarc`, which
will be in the user's home directory. The option `-b` simply skips some
questions and adding fo the automatic initialization lines into user's
`.bash\_profile`.

The Conda install root directory contains basically the following
subdirectories:

- `/bin`, '/lib', ... the usual Linux directories for the Conda "base"
  environment
- `/envs` where all Conda environments will reside
- `/pkgs` Conda package cache (you can see how all packages were built by
  looking into `info/recipe/{meta.yaml,build.sh}` files)

### Installing packages 

I recommend

1. installing all conda packages into named environments under `/envs`, instead
   of installing them into the base environment, and
2. Using environment.yaml configuration files instead of adding packages to
   environments directly from the command line.

In practice, you only need to create a single environment.yaml file for each
your environments, and then use a single conda command

```
conda env create -f <envname>.yaml
```

to create the whole environment.

Updating the packages, or adding new packages to the an existing environment is
done by modifying the environment.yaml file, and then running

```
conda env update -f <envname>.yaml
```

### Examples of environment.yaml files

As an example, let's use the environment.yaml file [conda-docs-env.yaml]:

```
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

The first field, `name: docs`, simply defines the name (and the name of the
environment root directory under `/envs`) of the Conda environment. The second
field `channels:` list from which channels the packages are installed from.
Field `dependencies:` lists the actual Conda packages that are installed into
the environment. Note, that Conda integrates nicely with Python pip, and you can
also include pip packages, that are installed using pip, into the Conda
environment.

Conda uses a "channel priority" for determining where to install packages from,
i.e. it tries first to install packages from the first listed channel. If no
package versions are specified, Conda always installs the latest versions.


### Removing unused packages

### Installing packages so that other user's can access them


[Conda]: https://docs.conda.io/en/latest/
[environment.yaml]: https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file
[Spack]: https://spack.io/
[Miniconda]: https://docs.conda.io/en/latest/miniconda.html
[Anaconda]: https://www.anaconda.com/distribution/
[conda-docs-env.yaml]: ../../conda-docs-env.yaml

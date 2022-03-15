# Tykky

## Intro

Tykky is a set of tools which wrap installations inside 
an Apptainer/Singularity container to improve startup times, 
reduce IO load, and lessen the number of files on large parallel filesystems. 

Additionally, Tykky will generate wrappers so that installed
software can be used (almost) as if it were not containerized. Depending
on tool selection and settings, either the whole host filesystem or
a limited subset is visible during execution and installation. This means that
it's possible to wrap installation using e.g mpi4py relying on the host provided
mpi installation. 

This documentation covers a subset of the functionality and focuses on
conda and Python, a large part of the advanced use-cases
are not covered here yet.

!!! Warning
    As Tykky is still under development some of the more advanced features might change in exact usage and API.

## Basic conda installation

To access the tools provided by Tykky, simply load the module, `module load tykky`


Then we can run:
```bash
conda-containerize new --prefix <install_dir> env.yml
```

Where **env.yml** is a conda environment file.
This file can be written manually, e.g:

env.yaml
```yaml
channels:
  - conda-forge
dependencies:
  - python=3.8.8
  - scipy
  - nglview
```

Or generate them from an existing environment

```
conda env export -n <target_env_name> > env.yaml 
```
_Windows and MacOS will need to add the `--from-history` flag to the export command_

or 
```
conda list -n <target_env_name> --explicit > env.txt
```
_Using the `--explicit` option only works if the existing environment is
on a Linux machine with x86 CPU architecture. Otherwise the result will not be transferable to Lumi_  

After the installation is done you simply need to add 
the bin directory `<install_dir>/bin` to the path. 

```bash
export PATH="<install_dir>/bin:$PATH"
```
Then you can call python and any other executables conda has installed in the same way as if you had activated the environment. 

If you also need to install some additional pip packages you can do so by supplying
the `-r <req_file>` argument e.g: 

```
conda-containerize new -r req.txt --prefix <install_dir> env.yml
```

The tool also supports using [mamba](https://github.com/mamba-org/mamba) 
for installing packages. Enable this feature by adding the `--mamba` flag. 
`conda-containerize new --mamba ...`

Make sure that you have read and understood the license terms for miniconda and any used channels
before using the command. 

- https://www.anaconda.com/end-user-license-agreement-miniconda
- https://www.anaconda.com/terms-of-service
- https://www.anaconda.com/blog/anaconda-commercial-edition-faq

### End-to-end example 

Using the previous `env.yml`

```
mkdir MyEnv
conda-containerize new --prefix MyEnv env.yml 
```
After the installation finishes we can add the installation directory to our PATH
and use it like normal

```
$ export PATH="$PWD/MyEnv/bin:$PATH"
$ python --version
3.8.8
$ python3
Python 3.8.8 | packaged by conda-forge | (default, Feb 20 2021, 16:22:27) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import scipy
>>> import nglview
>>> 
```



## Modifying a conda installation

As Tykky installed software resides in a container, it can not be directly modified.
Small python packages can be added normally using `pip`, but then the python packages are
sitting on the parallel filesystem so this is not recommended for any larger installations.  

To actually modify the installation we can use the `update` keyword
together with the `--post-install <file>` option which specifies a bash script
with commands to run to update the installation. The commands are executed 
with the conda environment activated. 

```
conda-containerize update <existing installation> --post-install <file> 
```

Where `<file>` could e.g contain:

```
conda  install -y numpy
conda  remove -y pyyaml
pip install requests
```

In this mode the whole host system is available including all software and modules. 

## Plain pip installations

Sometimes you don't need a full blown conda environment or you might prefer pip
to manage python installations. For this case we can use: 

```
pip-containerize new --prefix <install_dir> req.txt
```
Where `req.txt` is a standard pip requirements file. 
The notes and options for modifying a conda installation apply here as well.

Note that the python version used by `pip-containerize` is the first python executable found in the path, so it's affected by loading modules. 

**Important:** This python can not be itself container-based as nesting is not possible.  

An additional flag `--slim` argument exists, which will instead use a pre-built minimal python
container with a much newer version of python as a base. Without the `--slim` flag, the whole host system is available,
and with the flag the system installations (i.e /usr, /lib64 ...) are no longer taken from the host, instead
coming from within container. 

## Existing containers 

Tykky also provides a tool to generate wrappers for existing containers, so that they can be used 
transparently (no need to prepend `singularity exec ...`, or modify scripts if switching between containerized versions of tools).

```
wrap-install -w </path/inside/container> <container> --prefix <install_dir> 
```
where `<container>` can be a filepath or any url accepted by singularity (e.g `docker//:` `oras//:` or any other singularity accepted format)
`-w` needs to be an absolute path (or comma separated list) inside the container. Wrappers will then be automatically
created for the executables in the target directories / for the target path.

## More complicated example

[Example in tool repository](https://github.com/CSCfi/hpc-container-wrapper/blob/master/examples/fftw.md)

## How it works

See the README in the source code repository. 
The source code can be found in the [GitHub repository](https://github.com/CSCfi/hpc-container-wrapper)



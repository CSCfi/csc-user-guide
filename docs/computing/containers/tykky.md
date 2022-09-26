# Tykky

## Intro

Tykky is a set of tools for easy installation of tools to HPC. 

Tykky use cases:

    * Conda installations, based on conda environment.yml 
    * Pip installations, based on pip requirements.txt
    * Container installations, based on existing Docker or Apptainer/Singularity images.

Tykky wraps installations inside 
an Apptainer/Singularity container to improve startup times, 
reduce IO load, and lessen the number of files on large parallel filesystems. 

Additionally, Tykky will generate wrappers so that installed
software can be used (almost) as if it was not containerized. Depending
on tool selection and settings, either the whole host filesystem or
a limited subset is visible during execution and installation. This means that
it's possible to wrap installation using e.g mpi4py relying on the host provided
mpi installation. 

This documentation covers a subset of the functionality and focuses on
conda and Pythony, a large part of the advanced use-cases
are not covered here yet.

!!! Warning
    As Tykky is still under development some of the more advanced features might change in exact usage and API.

## Tykky module

It is usually also good to unload other modules first: 

```
module purge
```

To access Tykky tools, load its module. 

```bash
module load tykky
```

## Conda installation

Make sure that you have read and understood the license terms for miniconda and any used channels
before using the command. 

- [Miniconda end user license agreement](https://www.anaconda.com/end-user-license-agreement-miniconda)
- [Anaconda terms of service](https://www.anaconda.com/terms-of-service)
- [A blog entry on Anaconda commercial edition](https://www.anaconda.com/blog/anaconda-commercial-edition-faq)

1) Create **conda environment file** env.yml: 
	* [Create manually a new file](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#create-env-file-manually) or 
	* [Create the file from existing conda installation](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#sharing-an-environment). 
		* Windows and MacOS might need the [`--from-history` flag](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#exporting-an-environment-file-across-platforms), to get a .yml file suitable for Linux.
		* If the existing environment is on a Linux machine with x86 CPU architecture, it is possible also to use [`--explicit` flag](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#building-identical-conda-environments)

2) Create new directory for installation <install_dir>. Likely /projappl/<your_project>/.. is a good place.

3) Create installation

```bash
conda-containerize new --prefix <install_dir> env.yml
```

4) Add the bin directory `<install_dir>/bin` to the path. 

```bash
export PATH="<install_dir>/bin:$PATH"
```

5) You can call python and any other executables conda has installed in the same way as if you had activated the environment. 

### pip with conda

To install some additional pip packages, add the `-r <req_file>` argument e.g: 

```
conda-containerize new -r req.txt --prefix <install_dir> env.yml
```

### mamba 
The tool also supports using [mamba](https://github.com/mamba-org/mamba) 
for installing packages. Enable this feature by adding the `--mamba` flag. 

```
conda-containerize new --mamba --prefix <install_dir> env.yml
```


### End-to-end example 


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

### Modifying a conda installation

Tykky installed software resides in a container, so it can not be directly modified.
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

## Pip installations

Sometimes you don't need a full blown conda environment or you might prefer pip
to manage Python installations. For this case we can use: 

```
pip-containerize new --prefix <install_dir> req.txt
```
Where `req.txt` is a standard pip requirements file. 
The notes and options for modifying a conda installation apply here as well.

Note that the Python version used by `pip-containerize` is the first Python executable found in the path, so it's affected by loading modules. 

**Important:** This python can not be itself container-based as nesting is not possible.  

An additional flag `--slim` argument exists, which will instead use a pre-built minimal python
container with a much newer version of python as a base. Without the `--slim` flag, the whole host system is available,
and with the flag the system installations (i.e /usr, /lib64 ...) are no longer taken from the host, instead
coming from within container. 

## Container installations

Tykky also provides an option to: 
	
	* Generate wrappers for tools in existing Apptainer/Singularity containers, so that they can be used 
transparently (no need to prepend `singularity exec ...`, or modify scripts if switching between containerized versions and "normal" installation).
	* Install tools available in Docker images, including generating wrappers.

```
wrap-container -w </path/inside/container> <container> --prefix <install_dir> 
```
where `<container>` can be a filepath or any [URL accepted by singularity](https://docs.sylabs.io/guides/3.7/user-guide/cli/singularity_pull.html) (e.g `docker://` `oras://` )
`-w` needs to be an absolute path (or comma separated list) inside the container. Wrappers will then be automatically
created for the executables in the target directories / for the target path.

If you do not know the path of executables in the container:

	* In case of existing local Apptainer/Singularity file, check the path with opening terminal inside the container: `singularity shell xxx.sif`
	* In case of Docker or non-local Apptainer/Singularity file, create first the installation with some path and then check with created `_debug_shell` where the executables are installed.

## More complicated example

[Example in tool repository](https://github.com/CSCfi/hpc-container-wrapper/blob/master/examples/fftw.md)

## How it works

See the README in the source code repository. 
The source code can be found in the [GitHub repository](https://github.com/CSCfi/hpc-container-wrapper)

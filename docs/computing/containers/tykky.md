# Tykky

## Intro

Tykky is a set of tools which make software installations on HPC systems easier and
more efficient using Apptainer containers.

Tykky use cases:

- Conda installations, based on Conda `environment.yml`.
- Pip installations, based on pip `requirements.txt`.
- Container installations, based on existing Docker or Apptainer/Singularity images.
    - This includes installations from the Bioconda channel, see [this tutorial for
      an example](../../support/tutorials/bioconda-tutorial.md).

Tykky wraps installations inside an Apptainer/Singularity container to improve startup
times, reduce I/O load, and lessen the number of files on large parallel file systems.
Additionally, Tykky will generate wrappers so that installed software can be used
(almost) as if it was not containerized. Depending on tool selection and settings,
either the whole host file system or a limited subset is visible during execution
and installation. This means that it's possible to wrap installations using e.g
`mpi4py` relying on the host-provided MPI installation.

This documentation covers a subset of the functionality and focuses on Conda and
Python. Most advanced use-cases are not covered here yet.

!!! Warning
    As Tykky is still under development, some of the more advanced features might
    change with respect to exact usage and API.

## Tykky module

To access Tykky tools:

1) Usually it is best to first unload all other modules:

```bash
module purge
```

2) Load the Tykky module:

```bash
module load tykky
```

## Conda-based installation

First, make sure that you have read and understood the license terms for Miniconda
and any used channels before using the command.

- [Miniconda end-user license agreement](https://legal.anaconda.com/policies/en?name=offering-specific-terms#miniconda).
- [Anaconda terms of service](https://legal.anaconda.com/policies/en/?name=terms-of-service#terms-of-service).
- [A blog entry on Anaconda commercial edition](https://www.anaconda.com/blog/anaconda-commercial-edition-faq).

1) Create a **Conda environment file** `env.yml`:

- [Create manually a new file](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#create-env-file-manually) or
- [Create the file from an existing Conda installation](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#sharing-an-environment). For example: `conda env export -n <target_env_name> > env.yml`.
  	- If the existing environment is on a Windows or MacOS machine, the [`--from-history` flag](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#exporting-an-environment-file-across-platforms) might be required to get a `.yml` file suitable for Linux.
  	- If the existing environment is on a Linux machine with x86 CPU architecture, it is also possible to use [`--explicit` flag](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#building-identical-conda-environments).

An example of a suitable `env.yml` file would be:

```yaml
channels:
  - conda-forge
dependencies:
  - python=3.8.8
  - scipy
  - nglview
```

!!! info
    The `channels` field lists which channels the packages should be pulled from
    to this environment, whereas the `dependencies` field lists the actual Conda
    packages that will be installed into the environment. Note that Conda uses a
    channel priority for determining where to install packages from, i.e. it tries
    to first install packages from the first listed channel. If no package versions
    are specified, Conda always installs the latest versions.

2) Create a new directory `<install_dir>` for the installation. `/projappl/<your_project>/...`
   is recommended.

3) Create the installation:

```bash
conda-containerize new --prefix <install_dir> env.yml
```

4) Add the `<install_dir>/bin` directory to your `$PATH`:

```bash
export PATH="<install_dir>/bin:$PATH"
```

5) Now you can call `python` and any other executables Conda has installed in the same
   way as if you had activated the environment.

### Using Jupyter with a Tykky installation

To use a Tykky installation with [Jupyter](https://jupyter.org/), include correct conda package in your Conda environment file: `jupyterlab` for [JupyterLab](https://jupyterlab.readthedocs.io/en/latest/) or `notebook` for [Jupyter Notebooks](https://jupyter-notebook.readthedocs.io/en/latest/) from `conda-forge` channel. Also additional JupyterLab extensions can be installed, for example [jupyterlab-git](https://github.com/jupyterlab/jupyterlab-git) or [dask-labextension](https://github.com/dask/dask-labextension). 

The best way to use Jupyter in Puhti or Mahti is with [the web interface](../webinterface/index.md). See [Jupyter application page](../webinterface/jupyter.md#tykky-installations) for details how to use your own Tykky installation with Puhti web interface Jupyter.

### Pip with Conda

To install some additional pip packages, add the `-r <req_file>` argument, e.g.:

```bash
conda-containerize new -r req.txt --prefix <install_dir> env.yml
```

### Mamba

The tool also supports using [Mamba](https://github.com/mamba-org/mamba) for installing
packages. Mamba often finds suitable packages much faster than Conda, so it is a good
option when the required package list is long. Enable this feature by adding the `--mamba`
flag.

```bash
conda-containerize new --mamba --prefix <install_dir> env.yml
```

### End-to-end example

Create a new Conda-based installation using the previous `env.yml` file.

```bash
mkdir MyEnv
conda-containerize new --prefix MyEnv env.yml
```

After the installation finishes, add the installation directory to your `PATH`
and use it like normal.

```bash
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

### Modifying a Conda installation

Tykky installations reside in a container, so they can not be directly modified.
Small Python packages can be added normally using `pip`, but then the Python packages
will be sitting on the parallel file system, which is not recommended for any larger
installations.

To actually modify the installation, we can use the `update` keyword together with
the `--post-install <file>` option, which specifies a bash script with commands to
run to update the installation. The commands are executed with the Conda environment
activated.

```bash
conda-containerize update <existing installation> --post-install <file> 
```

Where `<file>` could e.g. contain:

```bash
conda install -y numpy
conda remove -y nglview
pip install requests
```

In this mode the whole host system is available including all software and modules.

## Pip-based installations

Sometimes you don't need a full-blown Conda environment or you might prefer pip
to manage Python installations. In this case we can use:

```bash
pip-containerize new --prefix <install_dir> req.txt
```

where `req.txt` is a standard pip requirements file. The notes and options for
modifying a Conda installation apply here as well.

Note that the Python version used by `pip-containerize` is the first Python executable
found in the path, so it's affected by loaded modules.

**Important:** This Python can not be itself container-based as nesting is not possible!

An additional `--slim` flag exists, which will instead use a pre-built minimal Python
container with a much newer version of Python as a base. Without the `--slim` flag,
the whole host system is available, whereas with the flag the system installations (i.e.
`/usr`, `/lib64`, ...) are no longer taken from the host, but instead coming from
within the container.

## Container-based installations

Tykky also provides an option to:

- Generate wrappers for tools in existing Apptainer/Singularity containers so that
  they can be used transparently (no need to prepend `apptainer exec ...` or modify
  scripts if switching between containerized versions and "normal" installations).
- Install tools available in Docker images, including generating wrappers.

```bash
wrap-container -w /path/inside/container <container> --prefix <install_dir> 
```

- `<container>` can be a local filepath or any [URL accepted by
  Apptainer/Singularity](https://docs.sylabs.io/guides/3.7/user-guide/cli/singularity_pull.html)
  (e.g `docker://` `oras://`)
- `-w` needs to be an absolute path (or comma-separated list) inside the container.
  Wrappers will then be automatically created for the executables in the target
  directories / for the target path. If you do not know the path of the executables
  in the container, open a shell inside the container and use the [which
  command](https://linuxize.com/post/linux-which-command/). To open a shell:
  	- In case of existing local Apptainer/Singularity file: `singularity shell image.sif`.
  	- In case of Docker or non-local Apptainer/Singularity file, create first the
      installation with some path and then start with created `_debug_shell`.

## Memory errors

With very large installations the resources available on the login node might
not be enough, resulting in Tykky failing with a `MemoryError`. In this case, the
installation needs to be done on a compute node, for example using an [interactive
session](../../computing/running/interactive-usage.md#sinteractive-in-puhti):

```bash
# Start interactive session, here with 12 GB memory and 15 GB local disk (increase if needed)
sinteractive --account <project> --time 1:00:00 --mem 12000 --tmp 15

# Load Tykky
module purge
module load tykky

# Run the Tykky commands as described above, e.g.
conda-containerize new --prefix <install_dir> env.yml
```

## Moving and deleting Tykky installation

For deleting a Tykky installation, remove the <install_dir> folder.

Tykky installations can also be moved:

* Inside the same supercomputer, from folder to folder, move the <install_dir> folder with `mv` to new location. 
* Between Puhti and Mahti use `rsync`. For copying to Mahti, log in to Mahti and change to the folder where you want to move the Tykky installation, then use: 

```
rsync -al <username>@puhti.csc.fi:<install_dir> .
```

## More complicated example

[Example in tool repository](https://github.com/CSCfi/hpc-container-wrapper/blob/master/examples/fftw.md).

## How it works

See the `README` in the source code repository. The source code can be found in the
[GitHub repository](https://github.com/CSCfi/hpc-container-wrapper).

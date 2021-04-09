# Python
[Python](https://www.python.org/) programming language in CSC's Supercomputers
Puhti and Mahti.

## Available
Both Puhti and Mahti have a system Python available by default without loading
any module. By default are provided Python 2 - `python` (= 2.7.5) and for Python
3 - `python3` (= 3.6.8). The default Python does not include any optional Python
libraries. However, you can [install simple packages for yourself by the methods
explained below](python.md#installing-python-packages-to-existing-modules).

In Puhti there are several Python modules available that include different sets
of scientific libraries:

   * python-env - Anaconda Python with conda tools
   * [python-data](python-data.md) - for data analytics and machine learning
   * [MXNet](mxnet.md) - MXNet deep learning framework
   * [PyTorch](pytorch.md) - PyTorch deep learning framework
   * [RAPIDS](rapids.md) - for data analytics and machine learning on GPUs
   * [TensorFlow](tensorflow.md) - TensorFlow deep learning framework
   * [Bioconda](bioconda.md) - conda package manger for installing
     bioinformatics software
   * [BioPython](biopython.md) - biopython and other bioinformatics related
     Python libraries
   * [geoconda](geoconda.md) - for spatial data anlysis 
   * [Solaris](solaris.md) - deep learning pipeline for geospatial imagery
   * and several other modules may include Python...

In Mahti:

   * python-env - anaconda Python with conda tools
   * python-singularity - Singularity-based Python

To use any of the above mentioned modules, just load the appropriate module, for
example:

```bash
module load python-env
```

Typically, after activating the module, you can continue using the commands
`python` and/or `python3` but these will now point to different versions of
Python with a wider set of Python packages available. For more details, check
the corresponding application documentation (when available).


## Installing Python packages to existing modules

If you find that some package is missing from an existing module, you can often
install it yourself with: `pip install [newPythonPackageName] --user`

The packages are by default installed to your home directory under
`.local/lib/pythonx.y/site-packages` (where `x.y` is the version of Python being
used). If you would like to change the installation folder, for example to make
a project-wide installation instead of a personal one, you need to define the
`PYTHONUSERBASE` environment variable with the new installation local. For
example:

`export PYTHONUSERBASE=/projappl/<your_project>/python3.7_pip`

When later using those libraries you need to remember to add that path to
`PYTHONPATH` or use the same `PYTHONUSERBASE` definition as above. Naturally,
this also applies to slurm job scripts.

Alternatively you can create a separate virtual environment with
[venv](https://docs.python.org/3/library/venv.html), for example:

```
module load python-data
python -m venv --system-site-packages my-venv
source my-venv/bin/activate
pip install my_package_to_install
```

With `venv`, you can keep separate environments for each program. The next time
you wish to activate the environment you only need to run `source
my-venv/bin/activate`.

If you think that some important package should be included in a module provided
by CSC, you can send an email to <servicedesk@csc.fi>.

## Creating your own Python environments
It is also possible to create your own Python environments. The main options are
conda and Singularity. Singularity should be preferred at least when you know of
a suitable ready-made Singularity or Docker container. Conda is easy to use and
flexible, but it might create a huge number of files which is inefficient with
shared file systems. This can cause very slow library imports and in the worst
case slowdowns in the whole file system.

Please, see our Singularity documentation:

   * [Running Singularity containers](../computing/containers/run-existing.md)
   * [Creating Singularity containers](../computing/containers/creating.md),
     including how to convert Docker container to Singularity container.

For Conda:

   * [CSC conda tutorial](../support/tutorials/conda.md) describes in detail
     what conda is and how to use it.
   * [Bioconda](bioconda.md) provides conda tools preinstalled.


## Python development environments

Python code can be edited with a console-based [text editor directly on the
supercomputer](../support/tutorials/env-guide/text-and-image-processing.md).
Codes can also be edited on your local machine and copied to the supercomputer
with [scp](../data/moving/scp.md) or [graphical file transfer
tools](../data/moving/graphical_transfer.md).
You can also [edit Python scripts in Puhti from your local
PC](../support/tutorials/remote-dev.md) with some code editors like Visual
Studio Code.

Finally, several graphical programming environments can be used directly on the
supercomputer, such as Jupyter Notebooks and Spyder.

### Jupyter Notebooks
[Jupyter Notebooks](https://jupyter.org/) is a common way for organizing Python
code. Many of our modules, including python-env, python-singularity,
[python-data](python-data.md), the deep learning modules and
[geoconda](geoconda.md) have Jupyter notebook libraries included. See an example
of [how to set up and connect to a Jupyter Notebook in an interactive
session](../computing/running/interactive-usage.md#example-running-a-jupyter-notebook-server-via-sinteractive).

If you want to use a custom conda environment inside a Jupyter notebook, the
following workflow could be used (adapted to your situation):

```bash
# Set up PROJAPPL environtment variable, where to install your conda environment. 
# Add your project here
export PROJAPPL=/projappl/project_xxx
# Activate conda commands
module load bioconda
# Create conda environment with your packages
conda create --name gromacs-tutorials -c conda-forge -c bioconda gromacs=2020.4 matplotlib nglview notebook numpy requests pandas seaborn  
# Activate the new conda environment
source activate gromacs-tutorials
# Start Jupyter kernel, you will see a separate kernel with name "gromacs"
python -m ipykernel install --user --name gromacs-tutorials --display-name "gromacs" 
# load one of those packages that have jupyter
module load python-data
# Launch jupyter
start-jupyter-server 
```

### Spyder
[Spyder](https://www.spyder-ide.org/) is scientific Python development
environment. Modules python-env, [python-data](python-data.md) and
[geoconda](geoconda.md) have Spyder included. The best option for using it is
during an [interactive session](../computing/running/interactive-usage.md) with
[NoMachine](../support/tutorials/nomachine-usage.md).

## Python parallel jobs
Python has several different libraries for code parallellization:

   * [multiprocessing](https://docs.python.org/3/library/multiprocessing.html)
   * [joblib](https://joblib.readthedocs.io/en/latest/)
   * [dask](https://docs.dask.org)

The `multiprocessing` package is likely the easiest to use and is included in
all Python installations by default. `joblib` provides some more flexibility.
`multiprocessing` and `joblib` are suitable for one node (max 40 cores). `dask`
is the most versatile and has several options for parallelization. Please see
[CSC's Dask tutorial](../support/tutorials/dask-python.md) which includes both
single-node (max 40 cores) and multi-node examples.

See our GitHub repository for some [examples for using the different
parallelization options with
Puhti](https://github.com/csc-training/geocomputing/tree/master/python/puhti).


## License

Python packages usually are licensed under various free and open source licenses
(FOSS). [Python itself is licensed under the PSF
License](https://docs.python.org/3/license.html), which is also open source.

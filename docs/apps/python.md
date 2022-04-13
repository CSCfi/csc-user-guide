# Python
[Python](https://www.python.org/) programming language in CSC's Supercomputers
Puhti and Mahti.

## Available

* Puhti: various 2.x and 3.x versions
* Mahti: various 2.x and 3.x versions
 
System Python is available by default both in Puhti and Mahti without loading
any module. Python 2 (= 2.7.5) is available as `python` (= 2.7.5) Python
3 (= 3.6.8) as `python3`. The default system Python does not include any optional Python
packages. However, you can [install simple packages for yourself by the methods
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
example to add the package `pyarrow` to the `python-data` module:

```
module load python-data
export PYTHONUSERBASE=/projappl/<your_project>/my-python-env
pip install --user pyarrow
```

In the example, the package is now installed inside the `my-python-env`
directory in the project's projappl directory. Run `unset PYTHONUSERBASE` if you
wish to later install into your home directory again.

When later using those libraries you need to remember to add the `site-packages`
path to `PYTHONPATH` (or use the same `PYTHONUSERBASE` definition as above).
Naturally, this also applies to slurm job scripts. For example:

```
module load python-data
export PYTHONPATH=/projappl/<your_project>/my-python-env/lib/python3.9/site-packages/
python3 -c "import pyarrow"  # this should now work!
```

Alternatively you can create a separate virtual environment with
[venv](https://docs.python.org/3/library/venv.html), however this approach
doesn't work with modules installed with Singularity, which is now the default
approach at CSC.

If you think that some important package should be included in a module provided
by CSC, you can send an email to <servicedesk@csc.fi>.


## Creating your own Python environments

It is also possible to create your own Python environments. 

### Tykky
The easiest option is to use [Tykky](../computing/containers/tykky/) for conda or pip installations.

### Custom Singularity container
In some cases, for example if you know of a suitable ready-made Singularity or Docker container, also using custom Singularity container is an option. 

Please, see our Singularity documentation:

   * [Running Singularity containers](../computing/containers/run-existing.md)
   * [Creating Singularity containers](../computing/containers/creating.md),
     including how to convert Docker container to Singularity container.

### Conda
Conda is easy to use and flexible, but it might create a huge number of files which is inefficient with
shared file systems. This can cause very slow library imports and in the worst
case slowdowns in the whole file system. **Therefore CSC has deprecated the use of Conda installations at CSC supercomputers.**

   * [CSC conda tutorial](../support/tutorials/conda.md) describes in detail
     what conda is and how to use it. (Some parts of this tutorial may be helful also for Tykky installations.)


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
[Jupyter Notebook](https://jupyter.org/) allows one to run Python code via a web browser 
running on a local PC. The notebooks can combine code, equations, visualizations and narrative text
in a single document. Many of our modules, including python-env, python-singularity,
[python-data](python-data.md), the deep learning modules and
[geoconda](geoconda.md) include Jupyter notebook package. See the tutorial
[how to set up and connect to a Jupyter Notebook](../support/tutorials/rstudio-or-jupyter-notebooks.md)
for using Jupyter in CSC environment.

### Spyder
[Spyder](https://www.spyder-ide.org/) is scientific Python development
environment. Modules python-env, [python-data](python-data.md) and
[geoconda](geoconda.md) have Spyder included. The best option for using it is
through the [Puhti web interface remote desktop](../computing/webinterface/desktop.md).

## Python parallel jobs
Python has several different packages for parallel processing:

   * [multiprocessing](https://docs.python.org/3/library/multiprocessing.html)
   * [joblib](https://joblib.readthedocs.io/en/latest/)
   * [dask](https://docs.dask.org)
   * [mpi4py](https://mpi4py.readthedocs.io) - Python interface to MPI 

The `multiprocessing` package is likely the easiest to use and as it is part of the 
Python standard library it is included in all Python installations. `joblib` provides 
some more flexibility. `multiprocessing` and `joblib` are suitable for one 
node (max 40 cores). `dask` is the most versatile and has several options for 
parallelization. Please see [CSC's Dask tutorial](../support/tutorials/dask-python.md) 
which includes both single-node (max 40 cores) and multi-node examples. 

See our GitHub repository for some [examples for using the different
parallelization options with
Puhti](https://github.com/csc-training/geocomputing/tree/master/python/puhti).

The `mpi4py` is not included in the current Python environments in CSC supercomputers, 
however, for multinode jobs with non-trivial parallelization it is generally the most 
efficient option. For a short tutorial on `mpi4py` along with other approaches to improve
performance of Python programs see the free online course 
[Python in High Performance Computing](https://www.futurelearn.com/courses/python-in-hpc)

## License

Python packages usually are licensed under various free and open source licenses
(FOSS). [Python itself is licensed under the PSF
License](https://docs.python.org/3/license.html), which is also open source.

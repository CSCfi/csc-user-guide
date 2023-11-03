---
tags:
  - Free
---

# Python

[Python](https://www.python.org/) programming language in CSC's Supercomputers
Puhti and Mahti.

## Available

* Puhti: 3.x versions
* Mahti: 3.x versions

The basic system Python (`/usr/bin/python3`) available by default on
both Puhti and Mahti (without loading any modules) is **Python version
3.6.8**.  This can be launched simply with the command `python3`, but
this environment contains only a basic set of standard Python
packages. You can install additional packages yourself with the `pip`
command, see the section below [explaining how to install packages to
existing
modules](python.md#installing-python-packages-to-existing-modules).


## Using science area-specific Python modules

If you need a newer version of Python, or a wider set of Python
packages, Puhti and Mahti have several pre-installed modules containing
Python environments made for different science areas:

* [python-data](python-data.md) - for data analytics and machine learning
* [PyTorch](pytorch.md) - PyTorch deep learning framework
* [TensorFlow](tensorflow.md) - TensorFlow deep learning framework
* [JAX](jax.md) - Autograd and XLA for high-performance machine learning
* [geoconda](geoconda.md) - for spatial data anlysis
* [BioPython](biopython.md) (Puhti only) - biopython and other
  bioinformatics related Python libraries

To use any of the above mentioned modules, just load the appropriate
module, for example:

```bash
module load python-data
```

For more details about available Python versions and included
libraries, check the corresponding application documentation.

Typically, after activating a Python-based module, you can continue
using the `python3` command but this will now point to a newer version
of Python with a wider set of Python packages available. You can
always check the Python version with the command `python3 --version`,
and the full path of the command with `which python3` (to see if you
are using the system Python or one from the modules listed above).


## Installing Python packages to existing modules

If there is a CSC-provided module that covers _almost_ everything you
need, but it is missing a few Python packages, you may be able to
install those yourself with the Pip package manager.

If you think that some important package should be included by default
in a module provided by CSC, don't hesitate to contact our [Service
Desk](../support/contact.md).


### Using `venv`

The recommended way to add packages on top of an existing environment
is to use [venv](https://docs.python.org/3/tutorial/venv.html), which
is a standard Python module for creating a lightweight "virtual
environment". You can have multiple virtual environments, for example
one for each project.

For example to install a package called `whatsapp` on top of the
CSC-provided [python-data](python-data.md) module:

```bash
cd /projappl/<your_project>  # change this to the appropriate path for your project
module load python-data
python3 -m venv --system-site-packages my-venv
source venv/bin/activate
pip install whatsapp
```

!!! warning

    Don't forget to use the `--system-site-packages` flags when creating
    the virtual environment, otherwise the environment will not find the
    pre-installed packages from the base module (for example numpy from
    python-data).


Later when you wish to use the virtual environment you only need to
load the module and activate the environment:

```bash
module load python-data
source /projappl/<your_project>/venv/bin/activate
```

Naturally, this also applies to slurm job scripts.

**Note:** some older CSC installations are not compatible with Python
virtual environments. We are still working to update those. For these
you need to use the `pip install --user` approach described below.


### Using `pip install --user`

Another approach to install additional packages is to do a "user
installation" with the command `pip install --user`. This approach is
easy to use, as it doesn't require setting up a virtual environment,
but it can easily fill up your home directory if you install a lot of
packages. There are also other drawbacks, such as package-provided
commands not working out-of-the box.

With this approach packages are by default installed to your home
directory under `.local/lib/pythonx.y/site-packages` (where `x.y` is
the version of Python being used). If you would like to change the
installation folder, for example to make a project-wide installation
instead of a personal one, you need to define the `PYTHONUSERBASE`
environment variable with the new installation local. For example to
add the package `whatshap` to the `python-data` module:

```bash
module load python-data
export PYTHONUSERBASE=/projappl/<your_project>/my-python-env
pip install --user whatshap
```

In the example, the package is now installed inside the
`my-python-env` directory in the project's `projappl` directory. Run
`unset PYTHONUSERBASE` if you wish to later install into your home
directory again.

When later using those libraries you need to define `PYTHONUSERBASE`
again.  Naturally, this also applies to slurm job scripts. For
example:

```bash
module load python-data
export PYTHONUSERBASE=/projappl/<your_project>/my-python-env
```

Note that if the package you installed also contains executable files
these may not work as they refer to the Python path internal to the
container (and most of our Python modules are installed with
containers). You might see an error message like this:

```bash
whatshap --help
whatshap: /CSC_CONTAINER/miniconda/envs/env1/bin/python3.9: bad interpreter: No such file or directory
```

You can fix this by editing the first line of the executable (check
with `which whatshap` in our example) to point to the real python
interpreter (check with `which python3`). In our example we would edit
the file `~/.local/bin/whatshap` to have this as the first line:

```bash
#!/appl/soft/ai/tykky/python-data-2022-09/bin/python3
```

## Creating your own Python environments

It is also possible to create your own Python environments.

### Tykky

The easiest option is to use [Tykky](../computing/containers/tykky.md) for Conda or pip installations.

### Custom Apptainer container

In some cases, for example if you know of a suitable ready-made Apptainer or Docker container, also using
a custom Apptainer container is an option.

Please, see our Apptainer documentation:

* [Running Apptainer containers](../computing/containers/run-existing.md)
* [Creating Apptainer containers](../computing/containers/creating.md),
  including how to convert Docker container to Apptainer container.

### Conda

Conda is easy to use and flexible, but it usually creates a huge number of files which
is inefficient with shared file systems. This can cause very slow library imports and
in the worst case slowdowns in the whole file system. **Therefore, CSC has deprecated the
direct use of Conda installations on CSC supercomputers.** You can, however, still use
Conda environments granted that they are containerized. To easily containerize your Conda
(or pip) environments, please see the [Tykky container wrapper tool](../computing/containers/tykky.md).

* [CSC Conda tutorial](../support/tutorials/conda.md) describes in more detail
  what Conda is and how to use it. Some parts of this tutorial may be helpful also for
  Tykky installations.

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
supercomputer, such as Jupyter Notebooks, Spyder and Visual Studio Code, through
the [Puhti web interface](../computing/webinterface/index.md).

### Jupyter Notebooks

[Jupyter Notebooks](https://jupyter.org/) allows one to run Python code via a web
browser running on a local PC. The notebooks can combine code, equations,
visualizations and narrative text in a single document. Many of our modules, including
[python-data](python-data.md), the deep learning modules and [geoconda](geoconda.md)
include the Jupyter notebook package. See the tutorial [how to set up and connect to
a Jupyter Notebook](../support/tutorials/rstudio-or-jupyter-notebooks.md) for using
Jupyter in CSC environment.

### Spyder

[Spyder](https://www.spyder-ide.org/) is scientific Python development
environment. Modules [python-data](python-data.md) and [geoconda](geoconda.md)
have Spyder included. The best option for using it is through the [Puhti
web interface remote desktop](../computing/webinterface/desktop.md).

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

See our GitHub repository for some [examples for using the different parallelization
options with Puhti](https://github.com/csc-training/geocomputing/tree/master/python/puhti).

The `mpi4py` is not included in the current Python environments in CSC supercomputers,
however, for multinode jobs with non-trivial parallelization it is generally the most
efficient option. For a short tutorial on `mpi4py` along with other approaches to improve
performance of Python programs see the free online course [Python in High Performance
Computing](https://www.futurelearn.com/courses/python-in-hpc)

## License

Python packages usually are licensed under various free and open source licenses
(FOSS). [Python itself is licensed under the PSF
License](https://docs.python.org/3/license.html), which is also open source.

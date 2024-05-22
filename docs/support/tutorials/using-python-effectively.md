# Using Python effectively on CSC supercomputers

Some important aspects of using Python are notably different on CSC
supercomputers compared to usage on a personal device or in other
HPC environments. To make the most of the computational resources offered by
CSC, it is helpful to be aware of the differences.

For general information on the Python programming language and
Python tools on CSC supercomputers, please see the
[Python application page](../../apps/python.md).

<!--
https://a3s.fi/python-pkg-lists/biopythontools_3.10.6.txt
https://a3s.fi/python-pkg-lists/geoconda_3.10.9.yml
https://a3s.fi/python-pkg-lists/jax0.4.23_python3.9_cuda12.2_csc_fix1.txt
https://a3s.fi/python-pkg-lists/python-data-2023-11.yaml
https://a3s.fi/python-pkg-lists/pytorch_2.2.1_csc_fix2.txt
https://a3s.fi/python-pkg-lists/tensorflow_2.15.0_rocky3.txt
-->

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

For example to install a package called `whatshap` on top of the
CSC-provided [python-data](python-data.md) module:

```bash
cd /projappl/<your_project>  # change this to the appropriate path for your project
module load python-data
python3 -m venv --system-site-packages venv
source venv/bin/activate
pip install whatshap
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

<!--
## Installing Python libraries

While the pre-existing Python environments are quite extensive, projects
often require additional software not present in an environment.

### Complementing a pre-existing environment

In most cases, it is easiest to complement one of the pre-existing Python
environments. There are several ways to do this.

#### Virtual environments

The Python standard library includes the
[venv module](https://docs.python.org/3/library/venv.html), which supports the
creation of virtual environments. Python virtual environments are generally
very useful for managing packages for multiple projects, each with their
individual dependencies. On CSC supercomputers, this is very helpful, since
system-level installations are not possible for users.

While it is possible to create a complete Python environment inside the virtual
environment, it is typically more convenient to use them as extensions of
pre-existing environments. 

**Creating a venv**
```bash
module load <module name>
python3 -m venv --system-site-packages <env name>
source <env name>/bin/activate
pip install <package name>
```

!!! important
	Remember to use the `--system-site-packages` flag when
	creating the virtual environment, so that the environment
	finds pre-installed packages from any loaded module(s).

**Using a venv**
```bash
module load <module name>
source <env name>/bin/activate
```

!!! important
	When activating the virtual environment,
	remember to load the modules that were loaded when
	creating the environment, otherwise Python will probably
	not work as intended.

#### User installations 

Another way to use additional packages in tandem with pre-existing
environments is by doing a user installation.
The default installation directory for these is   
`.local/lib/python<x>.<y>/sitepackages` in the user's `$HOME` directory.

However, since the home directory has limited storage,
it usually makes more sense to install packages in the `projappl`
directory of a project. This is done by creating a new directory for the
installation and setting the `PYTHONUSERBASE` environment variable to
point to this directory.

```bash
mkdir /projappl/project_<id>/myenv
module load <module name>
export PYTHONUSERBASE=/projappl/project_<id>/myenv
pip install --user <package name>
```

`unset PYTHONUSERBASE`

```bash
module load <module name>
export PYTHONUSERBASE=/projappl/project_<id>/myenv
```
-->

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
Computing](https://www.futurelearn.com/courses/python-in-hpc).

# Using Python on CSC supercomputers

Some important aspects of working with the Python programming language
are notably different on CSC supercomputers compared to usage on a personal
device or in other HPC environments. To make the most of the computational
resources available to you, it is helpful to be aware of the differences.

See the
[Python application page](../../apps/python.md)
for general information on the Python language and
pre-installed Python environments on CSC supercomputers.

## Creating and managing Python environments

### Installing Python packages to existing modules

If there is a CSC-provided module that covers _almost_ everything you
need, but it is missing a few Python packages, you can try installing
those yourself with the pip package manager.

See the [package lists on our Python application
page](../../apps/python.md#pre-installed-python-environments) to find out
which packages are installed in existing modules.
If you think that some important package should be included by default
in a module provided by CSC, don't hesitate to contact our [Service
Desk](../contact.md).

=== "Using `venv`"

	The recommended way to add packages on top of an existing environment
	is to use [venv](https://docs.python.org/3/tutorial/venv.html), which
	is a standard Python module for creating a lightweight "virtual
	environment". You can have multiple virtual environments, for example
	one for each project.

	For example to install a package called `whatshap` on top of the
	CSC-provided [python-data](../../apps/python-data.md) module:

	```bash
	cd /projappl/<your_project>  # change this to the appropriate path for your project
	module load python-data
	python3 -m venv --system-site-packages venv
	source venv/bin/activate
	pip install whatshap
	```
	!!! note ""

	    Don't forget to use the `--system-site-packages` flag when creating
	    the virtual environment, otherwise the environment will not find the
	    pre-installed packages from the base module (for example `numpy` from
	    `python-data`).

	Later when you wish to use the virtual environment you only need to
	load the module and activate the environment:

	```bash
	module load python-data
	source /projappl/<your_project>/venv/bin/activate
	```
	!!! note ""

	    Likewise, when using the virtual environment, make sure
	    to actually have the base module loaded.

	Naturally, this also applies to Slurm job scripts.

	!!! info
		Some older CSC modules are not compatible with Python
		virtual environments. We are still working to update those.
		If you happen to be working with one of these modules, you
		need to use the `pip install --user` approach described on
		the other tab.

=== "Using `pip install --user`"

	Another approach to installing additional packages is to do a "user
	installation" with the command `pip install --user`. This approach is
	easy to use in principle, as it doesn't require setting up a
	virtual environment. However, package-provided commands may not
	work out-of-the-box (see the Info box at the end of this section).

	Packages are by default installed to your home
	directory under `.local/lib/pythonx.y/site-packages` (where `x.y` is
	the version of Python being used). **Please note that if you install a lot of
	packages, your home directory can easily run out of space.**
	This can be avoided by changing the installation folder to make
	a project-wide installation instead of a personal one. This is
	done by setting the `PYTHONUSERBASE` environment variable to
	refer to the new installation directory.

	For example, to add the package `whatshap` on top of the `python-data` module:

	```bash
	module load python-data
	export PYTHONUSERBASE=/projappl/<your_project>/my-python-env
	pip install --user whatshap
	```

	In the above example, the package is now installed inside the
	`my-python-env` directory in the project's `projappl` directory. Run  
	`unset PYTHONUSERBASE` if you wish to install packages into your home
	directory again.

	When using the libraries later, you need to define `PYTHONUSERBASE`
	again. Naturally, this also applies to Slurm job scripts. For example:

	```bash
	module load python-data
	export PYTHONUSERBASE=/projappl/<your_project>/my-python-env
	```

	!!! info
		If the package you installed also contains executable files
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

### Creating your own Python environments

It is also possible to create your own Python environments.

=== "pip"

	1. The easiest way to create a custom pip environment is by using the `venv`
	   module discussed in the
	   [previous
	   section](python-usage-guide.md#installing-python-packages-to-existing-modules),
	   which actually shows precisely how to do this. If you do not wish to use
	   packages from one of the existing modules, simply do not include
	   the  
	   `--system-site-packages` flag when creating the virtual environment.

	2. Another option is to create a pip environment inside a
	   [container](../../computing/containers/overview.md).
	   The most straightforward way to do so is by using the
	   [Tykky container wrapper](../../computing/containers/tykky.md).
	   To find out how to easily containerize your environment,
	   see the [Tykky instructions for pip-based
	   installations](../../computing/containers/tykky.md#pip-based-installations).

	3. An alternative to using Tykky is creating a pip environment
	   inside a custom Apptainer container. This is a practical choice if, for
	   example, you know of a suitable ready-made Apptainer or Docker container.
	   For more information about using Apptainer containers, please see the
	   related documentation:

		* [Running Apptainer containers](../../computing/containers/run-existing.md)
		* [Creating Apptainer containers](../../computing/containers/creating.md),
		including how to convert Docker containers to Apptainer containers.

=== "conda"

	Conda is easy to use and flexible, but it usually creates a huge number of files which
	is incompatible with shared file systems. The excess of files can cause
	very slow library imports and,
	in the worst case, slowdowns in the whole file system. Therefore,
	**CSC has deprecated the use of conda for direct installations on
	supercomputers**. However, you can still create and use
	[containerized](../../computing/containers/overview.md)
	conda environments.

	1. The most straightforward way to create a containerized conda
	   environment is by using the [Tykky container
	   wrapper](../../computing/containers/tykky.md).
	   To find out how to easily containerize your environment,
	   see the [Tykky instructions for conda-based
	   installations](../../computing/containers/tykky.md#conda-based-installations).

	2. An alternative to using Tykky is creating a conda environment
	   inside a custom Apptainer container. This is a practical choice if, for
	   example, you know of a suitable ready-made Apptainer or Docker container.
	   For more information about using Apptainer containers, please see the
	   related documentation:

		* [Running Apptainer containers](../../computing/containers/run-existing.md)
		* [Creating Apptainer containers](../../computing/containers/creating.md),
	  	including how to convert Docker containers to Apptainer containers.

	The [CSC conda tutorial](./conda.md) describes in more detail
	what conda is and how to use it. Some parts of the tutorial may
	also be helpful for Tykky installations.

## Python development environments

Python code can be edited with a console-based [text editor directly on the
supercomputer](./env-guide/text-and-image-processing.md).
Codes can also be edited on your local machine and copied to the supercomputer
with [scp](../../data/moving/scp.md) or [graphical file transfer
tools](../../data/moving/graphical_transfer.md).
You can also [edit Python scripts in Puhti from your local
PC](./remote-dev.md) with some code editors like Visual
Studio Code.

Finally, several graphical programming environments can be used directly on the
supercomputer, such as Jupyter Notebooks, Spyder and Visual Studio Code, through
the [Puhti web interface](../../computing/webinterface/index.md).

### Jupyter Notebooks

[Jupyter Notebooks](https://jupyter.org/) allows one to run Python code via a web
browser running on a local PC. The notebooks can combine code, equations,
visualizations and narrative text in a single document. Many of our modules, including
[python-data](../../apps/python-data.md), the deep learning modules and
[geoconda](../../apps/geoconda.md)
include the Jupyter notebook package. See the tutorial [how to set up and connect to
a Jupyter Notebook](./rstudio-or-jupyter-notebooks.md) for using
Jupyter in CSC environment.

### Spyder

[Spyder](https://www.spyder-ide.org/) is scientific Python development
environment. Modules [python-data](../../apps/python-data.md) and
[geoconda](../../apps/geoconda.md)
have Spyder included. The best option for using it is through the [Puhti
web interface remote desktop](../../computing/webinterface/desktop.md).

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
parallelization. Please see [CSC's Dask tutorial](./dask-python.md)
which includes both single-node (max 40 cores) and multi-node examples.

See our GitHub repository for some [examples for using the different parallelization
options with Puhti](https://github.com/csc-training/geocomputing/tree/master/python/puhti).

The `mpi4py` is not included in the current Python environments in CSC supercomputers,
however, for multinode jobs with non-trivial parallelization it is generally the most
efficient option. For a short tutorial on `mpi4py` along with other approaches to improve
performance of Python programs see the free online course [Python in High Performance
Computing](https://www.futurelearn.com/courses/python-in-hpc).

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

See the
[package lists on our Python application page](../../apps/python.md#pre-installed-python-environments)
to find out which packages are installed in existing modules.
If you think that some important package should be included by default
in a module provided by CSC, do not hesitate to contact our
[Service Desk](../contact.md).

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
    python3 -m venv --system-site-packages <venv_name>
    source <venv_name>/bin/activate
    pip install whatshap
    ```

    Unlike for example Tykky, `venv` creates a new directory for the
    environment, so there is no need for you to create one beforehand.
    Do not forget to use the `--system-site-packages` flag when creating
    the virtual environment, otherwise the environment will not find the
    pre-installed packages from the base module (for example `numpy` from
    `python-data`).

    Later when you wish to use the virtual environment you only need to
    load the module and activate the environment:

    ```bash
    module load python-data
    source /projappl/<your_project>/<venv_name>/bin/activate
    ```

    Likewise, when using the virtual environment, make sure
    to actually have the base module loaded.
    Naturally, this also applies to Slurm job scripts.

    !!! info "Compatibility with virtual environments"
        Some older CSC modules are not compatible with Python
        virtual environments. We are still working to update these
        modules, so if you happen to be working with one of them,
        you need to use the `pip install --user` approach described on
        the other tab.

    ---

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

    !!! info "Packages containing executable files"
        Most of our Python modules are implemented as containers.
        If a package you install also contains executable files,
        they may not work out of the box, since the executable
        may look for the Python interpreter using a path that is
        internal to the container.
        You might see an error message like this:

        ```bash
        whatshap: /CSC_CONTAINER/miniconda/envs/env1/bin/python3.9: bad interpreter: No such file or directory
        ```

        You can fix this by editing the first line of the executable
        (which in our example is located using `which whatshap`) to point
        to the real Python interpreter (can be found with `which python3`).
        In our example we would edit the file `~/.local/bin/whatshap`
        to have the following as its first line:

        ```bash
        #!/appl/soft/ai/tykky/python-data-2022-09/bin/python3
        ```

    ---

### Creating your own Python environments

It is also possible to create your own Python environments.

=== "pip"
    Pip is a good choice for managing Python environments that do not
    rely on complex dependency relationships.
    
    1. The easiest way to create a custom pip environment is by using the `venv`
       module discussed in the
       [previous section](python-usage-guide.md#installing-python-packages-to-existing-modules),
       which actually shows precisely how to do this. If you do not wish to use
       packages from one of the existing modules, simply do not include
       the  
       `--system-site-packages` flag when creating the virtual environment.

    2. Another option is to create a pip environment inside a
       [container](../../computing/containers/overview.md).
       The most straightforward way to do so is by using the
       [Tykky container wrapper](../../computing/containers/tykky.md).
       To find out how to easily containerize your environment,
       see the
       [Tykky instructions for pip-based installations](../../computing/containers/tykky.md#pip-based-installations).

    3. An alternative to using Tykky is creating a pip environment
       inside a custom Apptainer container. This is a practical choice if, for
       example, you know of a suitable ready-made Apptainer or Docker container.
       For more information about using Apptainer containers, please see the
       related documentation:

        * [Running Apptainer containers](../../computing/containers/run-existing.md)
        * [Creating Apptainer containers](../../computing/containers/creating.md),
        including how to convert Docker containers to Apptainer containers.

    ---

=== "conda"
    Conda is easy to use and flexible, but it usually creates a huge number of files which
    is incompatible with shared file systems. The excess of files can cause
    very slow library imports and,
    in the worst case, slows down the whole file system. Because of this,
    [**CSC has deprecated the use of conda**](conda.md)
    for direct installations on supercomputers.
    However, you can still create and use
    [containerized](../../computing/containers/overview.md)
    conda environments.

    1. The most straightforward way to create a containerized conda
       environment is by using the
       [Tykky container wrapper](../../computing/containers/tykky.md).
       To find out how to easily containerize your environment,
       see the
       [Tykky instructions for conda-based installations](../../computing/containers/tykky.md#conda-based-installation).

    2. An alternative to using Tykky is creating a conda environment
       inside a custom Apptainer container. This is a practical choice if, for
       example, you know of a suitable ready-made Apptainer or Docker container.
       For more information about using Apptainer containers, please see the
       related documentation:

        * [Running Apptainer containers](../../computing/containers/run-existing.md)
        * [Creating Apptainer containers](../../computing/containers/creating.md),
        including how to convert Docker containers to Apptainer containers.

    ---

## Python development environments

Python scripts can be edited directly on a CSC supercomputer using a
[console-based text editor](./env-guide/text-and-image-processing.md)
like `vim` or `emacs`. In addition to these terminal-based editors,
several graphical programming environments,
such as Jupyter notebooks, Visual Studio Code and Spyder,
can be used on a supercomputer through
[our web interface](../../computing/webinterface/index.md).

In addition to editing code directly on a supercomputer, it is also
possible to [develop code remotely](./remote-dev.md) using some
locally installable editors like Visual Studio Code.

Finally, one can of course edit code on a local device
and copy it to a supercomputer with command-line tools like
[`scp`](../../data/moving/scp.md) and
[`rsync`](../../data/moving/rsync.md),
or by using
[graphical file transfer tools](../../data/moving/graphical_transfer.md).

### Jupyter

[Jupyter notebooks](../../apps/jupyter.md) provide an interactive
programming environment where one can
write and run Python code in individual cells.
The notebooks combine code, equations, visualizations and narrative text
in a single document. 

The [Jupyter interactive application](../../computing/webinterface/jupyter.md)
on our web interface allows using Jupyter on CSC supercomputers.
Many of our Python environments, including
[`python-data`](../../apps/python-data.md), [`geoconda`](../../apps/geoconda.md)
as well as deep learning modules like [`pytorch`](../../apps/pytorch.md)
include the main Jupyter packages, so they can be used in the application.
The documentation page for the application includes a
[list of supported environments](../../computing/webinterface/jupyter.md#currently-supported-python-environments).

### Visual Studio Code

[Visual Studio Code](../../apps/vscode.md) (VSCode)
is a widely-used source code editor developed by Microsoft.
Unlike the other two development environments introduced here,
it does not rely on any Python packages, so it can be used by
default with all CSC- and custom-made Python environments.

There are two ways to run VSCode on CSC supercomputers:

1. [As an interactive app on our web interface](../../computing/webinterface/vscode.md)
2. [Remotely using the Remote-SSH plugin](./remote-dev.md#visual-studio-code-with-remote-ssh-plugin)

!!! info "Using custom environments in VSCode"
    Since only CSC modules are offered in the VSCode session launch form,
    using custom Python environments with built-in VSCode functions like
    debugging requires changing the path of the Python interpreter
    after the session has launched. This can be done by clicking on
    the Python version information displayed in the lower right corner
    of the VSCode window.

### Spyder

[Spyder](https://www.spyder-ide.org/) is a scientific Python development
environment. The [python-data](../../apps/python-data.md) and
[geoconda](../../apps/geoconda.md) modules
have Spyder included. The best option for using it is through the
[Puhti web interface remote desktop](../../computing/webinterface/desktop.md).

## Python parallel jobs

There are several Python libraries for parallel computing. Below are a few suggestions:

* [multiprocessing](https://docs.python.org/3/library/multiprocessing.html) – process-based parallelism
* [joblib](https://joblib.readthedocs.io/en/latest/) – running Python functions as pipeline jobs
* [dask](https://docs.dask.org) – general purpose parallel programming solution
* [mpi4py](https://mpi4py.readthedocs.io) – MPI bindings for Python

The `multiprocessing` package is likely the easiest to use. Being part of the
Python standard library, it is included in all Python installations by default.
`joblib` provides some more flexibility in comparison. These two packages are suitable for
single-node parallelization (max. 40 cores).

`dask` is the most versatile of the bunch and has several options for
parallelization. Please see the [CSC Dask tutorial](./dask-python.md) for
examples of both single-node (max. 40 cores) and multi-node parallelization.

In addition, there are examples of
[using different parallelization options on Puhti](https://github.com/csc-training/geocomputing/tree/master/python/puhti)
on our CSC Training GitHub organization. Of the above four packages, examples are
provided for `multiprocessing`, `joblib` and `dask`.

The `mpi4py` package is included in our [PyTorch environment](../../apps/pytorch.md).
It is generally the most efficient option for multinode jobs with non-trivial parallelization.
For a short tutorial on `mpi4py`, along with other approaches for improving the
performance of Python programs, please see the free
[Python in High Performance Computing](https://www.futurelearn.com/courses/python-in-hpc)
online course.

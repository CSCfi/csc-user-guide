---
tags:
  - Free
---

# Python Data

Collection of Python libraries for data analytics and machine learning.

!!! info "News"
     **2.5.2024** Installed `python-data/3.10-24.04` with newer packages of popular Python 
     modules.

    **28.11.2023** Installed `python-data/3.10-23.11` with newer packages of popular Python 
     modules.

     **28.11.2023** Installed `python-data/3.10-23.11` with newer packages of popular Python 
     modules.

     **4.7.2023** Installed `python-data/3.10-23.07` with newer packages of popular Python 
     modules.

    **28.10.2022** Module `python-data/3.8` was added for those who
    specifically need Python 3.8.


## Available

Versions are numbered as `X.Z-YY.MM`, where `X.Z` is the version of
the Python interpreter, and `YY.MM` is the year and month of the
installation. Typically the module will include the newest versions of
libraries at installation time, to the extent software dependencies
allow.

Current versions are:

- (default version) `python-data/3.10-24.04`: installed in April 2024,
  includes for example Scikit-learn 1.4.2, SciPy 1.13.0, Pandas 2.2.2
  and JupyterLab 4.1.6.

- `python-data/3.10-23.11`: installed in November 2023, includes for
  example Scikit-learn 1.3.2, SciPy 1.11.4, Pandas 2.1.3 and
  JupyterLab 4.0.9.

- `python-data/3.10-23.07`: installed in July 2023, includes for
  example Scikit-learn 1.2.2, SciPy 1.11.1, Pandas 2.0.3 and JupyterLab
  4.0.2.
- `python-data/3.10-22.09` or `python-data/3.10`:
  installed in September 2022, includes for example Scikit-learn
  1.1.2, SciPy 1.9.1, Pandas 1.4.4 and JupyterLab 3.4.6.
- `python-data/3.9-22.04` or `python-data/3.9`: installed in April
  2022, includes for example Scikit-learn 1.0.2, SciPy 1.8.0, Pandas
  1.4.2 and JupyterLab 3.3.4.
- `python-data/3.8-22.10` or `python-data/3.8`: added for those who
  specifically need Python 3.8.

Python-data tries to include a comprehensive selection of Python libraries for
data analytics and machine learning, for example:

- [Dask](https://dask.org/): Scalable analytics in Python
- [Gensim](https://radimrehurek.com/gensim/): Topic modelling
- [Jupyter](https://jupyter.org/index.html) and [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/)
- [NLTK](https://matplotlib.org/): Natural language toolkit
- [PyTables](http://www.pytables.org/)
- [SciPy](https://www.scipy.org/), including [NumPy](https://www.numpy.org/), [Matplotlib](https://matplotlib.org/) and [Pandas](https://pandas.pydata.org/)
- [Scikit-learn](https://scikit-learn.org/stable/): machine learning in Python
- [Seaborn](https://seaborn.pydata.org/): statistical data visualization

If you find that some package is missing, you can often install it
yourself with `pip install --user`.  See [our Python
documentation](python.md#installing-python-packages-to-existing-modules)
for more information on how to install packages yourself.

It is also possible to use [Python virtual
environments](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment).
To create a virtual environment use the command `python3 -m venv
--system-site-packages venv`.

If you think that some important package should be included in the
module provided by CSC, please [contact our
servicedesk](../support/contact.md). Note that some machine learning
frameworks have their own specific modules, for example:
[PyTorch](pytorch.md), [TensorFlow](tensorflow.md), [JAX](jax.md), and
[RAPIDS](rapids.md).

!!! info "Note about multi-threading"

    Loading the `python-data` module will set the environment variable
    `OMP_NUM_THREADS=1`, which essentially disables OpenMP multi-threading
    support. This is a reasonable setting in most cases, and fixes some
    issues related to multi-processing runs. If you know that you need to
    use OpenMP multi-threading, please set this variable manually, for
    example in your Slurm job script:

        export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK


## License

All packages are licensed under various free and open source licenses (FOSS).

## Usage

To use this software on Puhti, initialize it with:

```text
module load python-data
```

to access the default version, or if you wish to have a specific version ([see
above for available versions](#available)):

```text
module load python-data/3.10-2023.11
```

If you just want the most recent version with a specific Python version, you can also run:

```text
module load python-data/3.10
```

This will show all available versions:

```text
module avail python-data
```

To check the exact packages and versions included in the loaded module you can run:

```text
list-packages
```

!!! warning

    Note that Puhti login nodes are not intended for heavy computing, please use
    slurm batch jobs instead. See our [instructions on how to use the batch job
    system](../computing/running/getting-started.md).

Please also check [CSC's general Python documentation](python.md).

### Local storage

Some nodes in Puhti have fast local storage which is useful for
IO-intensive applications. See our [general instructions on how to
take the fast local storage into
use](../computing/running/creating-job-scripts-puhti.md#local-storage).

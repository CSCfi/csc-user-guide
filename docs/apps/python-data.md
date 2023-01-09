---
tags:
  - Free
---

# Python Data

Collection of Python libraries for data analytics and machine learning.

!!! info "News"

    **28.10.2022** Module `python-data/3.8` was added for those who
    specifically need Python 3.8.

    **5.10.2022** Together with Puhti's update to Red Hat Enterprise Linux
    8 (RHEL8), **we removed some old versions of Python Data, including all
    (previously deprecated) conda-based versions. We also changed the version naming of the
    modules.** Please [contact our servicedesk](../../support/contact/) if
    you really need access to older versions.

    **5.5.2022** Due to Mahti's update to Red Hat Enterprise Linux 8 (RHEL8),
    older versions of Python Data are no longer fully supported. Please [contact our
    servicedesk](../../support/contact/) if you really need access to older versions.

    **4.2.2022** All old Python Data versions which were based on direct Conda
    installations have been deprecated, and we encourage users to move to newer
    versions. Read more on our separate [Conda deprecation page](../support/deprecate-conda.md).


## Available

Versions are numbered as `X.Z-YY.MM`, where `X.Z` is the version of
the Python interpreter, and `YY.MM` is the year and month of the
installation. Typically the module will include the newest versions of
libraries at installation time, to the extent software dependencies
allow.

Current versions are:

- `python-data/3.10-22.09` or `python-data/3.10`: installed in
  September 2022, includes for example Scikit-learn 1.1.2, SciPy
  1.9.1, Pandas 1.4.4 and JupyterLab 3.4.6.
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
yourself with `pip install --user`. See [our Python
documentation](python.md#installing-python-packages-to-existing-modules)
for more information on how to install packages yourself. If you think
that some important package should be included in the module provided
by CSC, please [contact our servicedesk](../../support/contact/). Note
that some machine learning frameworks have their own specific modules,
for example: [PyTorch](pytorch.md), [TensorFlow](tensorflow.md),
[JAX](jax.md), and [RAPIDS](rapids.md).

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
module load python-data/3.9-2022.04
```

If you just want the most recent version with a specific Python version, you can also run:

```text
module load python-data/3.9
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
    system](../computing/running/index.md).

Please also check [CSC's general Python documentation](python.md).

### Local storage

Some nodes in Puhti have fast local storage which is useful for
IO-intensive applications. See our [general instructions on how to
take the fast local storage into
use](../computing/running/creating-job-scripts-puhti/#local-storage).

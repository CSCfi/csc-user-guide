# Python Data

Collection of Python libraries for data analytics and machine learning.

!!! News

    **5.5.2022** Due to Mahti's update to Red Hat Enterprise Linux 8 (RHEL8),
    older versions of Python Data are no longer fully supported. Please [contact our
    servicedesk](../support/contact.md) if you really need access to older versions.

    **4.2.2022** All old Python Data versions which were based on direct Conda
    installations have been deprecated, and we encourage users to move to newer
    versions. Read more on our separate [Conda deprecation page](../support/deprecate-conda.md).


## Available

Older versions of the `python-data` module are available on **Puhti only**.
Versions are numbered as `X.Y-N`, where `X.Y` is the version of the Python
interpreter included, and `N` is a running version number starting from 1.
Current versions are:

- `python-data/3.9-3` installed in April 2022, includes for example Scikit-learn
  1.0.2, SciPy 1.8.0, Pandas 1.4.2 and JupyterLab 3.3.4. Available on **both
  Puhti and Mahti**.
- `python-data/3.9-2` installed in January 2022, includes for example
  Scikit-learn 1.0.2, SciPy 1.7.3, Pandas 1.3.5 and JupyterLab 3.2.6.
- `python-data/3.9-1` installed in June 2021, includes for example: Scikit-learn
  0.24.2, Pandas 1.2.4 and JupyterLab 3.0.16. This is the first version of
  Python Data that has been installed using Singularity which should make
  loading times much faster. Thanks to wrapper scripts this change should be
  mostly invisible to users. If you still encounter any problems, don't hesitate
  to report them to [CSC's service desk](../support/contact.md).
- _(deprecated)_ `python-data/3.7.6-1` installed in June 2020, includes for example:
  Scikit-learn 0.23.1, Pandas 1.0.4 and JupyterLab 2.1.4.
- _(deprecated)_ `python-data/3.7.3-1` installed in July 2019.

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

If you find that some package is missing, you can often install it yourself with
`pip install --user`. See [our Python
documentation](python.md#installing-python-packages-to-existing-modules) for
more information on how to install packages yourself. If you think that some
important package should be included in the module provided by CSC, please
[contact our servicedesk](../support/contact.md). Note that some machine
learning frameworks have their own specific modules, for example:
[PyTorch](pytorch.md), [TensorFlow](tensorflow.md), [MXNet](mxnet.md) and
[RAPIDS](rapids.md).

## License

All packages are licensed under various free and open source licenses (FOSS).

## Usage

To use this software on Puhti, initialize it with:

```text
module load python-data
```

to access the default version.

This will show all available versions:

```text
module avail python-data
```

To check the exact packages and versions included in the loaded module you can run:

```text
list-packages
```

!!! note 

    Note that Puhti login nodes are not intended for heavy computing, please use
    slurm batch jobs instead. See our [instructions on how to use the batch job
    system](../computing/running/getting-started.md).

Please also check [CSC's general Python documentation](python.md).

### Local storage

Some nodes in Puhti have fast local storage which is useful for IO-intensive
applications. See our [general instructions on how to take the fast local
storage into
use](../computing/running/creating-job-scripts-puhti.md#local-storage).

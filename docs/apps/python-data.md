# Python Data

Collection of Python libraries for data analytics and machine learning.

## Available

The `python-data` module is available on Puhti only.

Activates a conda environment that comes with a recent version of Python, and includes several data analytics and machine learning libraries, for example:

- [Dask](https://dask.org/): Scalable analytics in Python
- [Gensim](https://radimrehurek.com/gensim/): Topic modelling
- [Jupyter](https://jupyter.org/index.html) and [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/)
- [NLTK](https://matplotlib.org/): Natural language toolkit
- [PyTables](http://www.pytables.org/)
- [SciPy](https://www.scipy.org/), including [NumPy](https://www.numpy.org/), [Matplotlib](https://matplotlib.org/) and [Pandas](https://pandas.pydata.org/)
- [Scikit-learn](https://scikit-learn.org/stable/): machine learning in Python
- [Seaborn](https://seaborn.pydata.org/): statistical data visualization

If you find that some package is missing, you can often install it yourself with `pip install --user`.

If you think that some important data analytics or machine learning package for Python should be included in the module provided by CSC, you can send an email to <servicedesk@csc.fi>.  Note that some deep learning frameworks have their own specific modules, for example: [PyTorch](pytorch.md), [TensorFlow](tensorflow.md) and [MXNet](mxnet.md).

## License

All packages are licensed under various free and open source licenses (FOSS).

## Usage

To use this software on Puhti, initialize it with:

```bash
$ module load python-data
```

to access the default version.

This will show all available versions:

```bash
$ module avail python-data
```

Versions are numbered as `X.Y.Z-N`, where `X.Y.Z` is the version of the Python interpreter included, and `N` is a running version number starting from 1.

To check the exact packages and version included a specific module, you can run for example:

```bash
$ module load python-data/3.7.3-1
$ conda list
```

!!! note 

    Note that Puhti login nodes are not intended for heavy
    computing. Please use slurm batch jobs instead.

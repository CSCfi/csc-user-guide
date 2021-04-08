# Python
[Python](https://www.python.org/) programming language in Puhti and Mahti.

## Available
Both Puhti and Mahti have system Python available by default without loading any module. By default are provided Python 2 - `python` (= 2.7.5) and for Python 3 - `python3` (= 3.6.8). The default Python does not include any optional Python libraries.

In Puhti there are several Python modules available that include different sets of scientific libraries: 

   * python-env - anaconda Python with conda tools
   * [python-data](python-data.md) - for data analytics and machine learning
   * [MXNet](mxnet.md) - MXNet deep learning framework
   * [PyTorch](pytorch.md) - PyTorch deep learning framework
   * [RAPIDS](rapids.md) - for data analytics and machine learning on GPUs
   * [TensorFlow](tensorflow.md) - TensorFlow deep learning framework
   * [Bioconda](bioconda.md) - conda package manger for installing bioinformatics software
   * [BioPython](biopython.md) - biopython and other bioinformatics related Python libraries
   * [geoconda](geoconda.md) - for spatial data anlysis 
   * [Solaris](solaris.md) - deep learning pipeline for geospatial imagery
   * and several other modules may include Python...

In Mahti:

   * python-env - anaconda Python with conda tools
   * python-singularity - 

## Jupyter Notebooks
[Jupyter Notebooks](https://jupyter.org/) is a common way for organizing Python code. python-env, python-singularity, [python-data](python-data.md), deep learning modules and [geoconda](geoconda.md) have Jupyter notebook libraries included. [Jupyter Notebook instructions](../computing/running/interactive-usage.md#example-running-a-jupyter-notebook-server-via-sinteractive) describe how to set up and connect to a Jupyter Notebook in computing node during interactive session.

If you want to use custom conda environment inside Jupyter notebook, the following workflow could be used:

```
# Set up PROJAPPL environtment variable, where to install your conda environment. 
# Add your project here
export PROJAPPL=/projappl/project_xxx   
# Activate conda commands
module load bioconda    
# Create conda environment with your packages
conda create --name gromacs-tutorials -c conda-forge -c bioconda gromacs=2020.4 matplotlib nglview notebook numpy requests pandas seaborn  
# Activate the new conda äenvironment
source activate gromacs-tutorials  
# Start Jupyter kernel, you will see a separate kernel with name "gromacs"
python -m ipykernel install --user --name gromacs-tutorials --display-name "gromacs" 
# load one of those packages that have jupyter
module load python-data  
# Launch jupyter
start-jupyter-server 
```

## Spyder
[Spyder](https://www.spyder-ide.org/) is scientific Python development environment. python-env, [python-data](python-data.md) and [geoconda](geoconda.md) have Spyder included. The best option for using it is during [interactive session](../computing/running/interactive-usage.md) with [NoMachine].

## Remote editing
You can also [edit Python scripts in Puhti from your local PC](../support/tutorials/remote-dev.md) with some code editors like Visual Studio Code.

## Python parallel jobs
Python has several different libraries for code parallellization:

   * [multiprocessing](https://docs.python.org/3/library/multiprocessing.html)
   * [joblib](https://joblib.readthedocs.io/en/latest/)
   * [dask](https://docs.dask.org). [CSC Dask tutorial](../support/tutorials/dask-python.md).

`multiprocessing` package is likely easiest to use and in included in all Python installations by default. `joblib` provides some more flexibility. `multiprocessing` and `joblib` are suitable for one node (max 40 cores). `dask` is the most versatile has several optins for parallelization, the examples here include both single-node (max 40 cores) and multi-node example.

[Examples for using the different options with Puhti.](https://github.com/csc-training/geocomputing/tree/master/python/puhti)


## Installing Python packages to existing modules
If you find that some package is missing from existing module, you can often install it yourself with:
`pip install [newPythonPackageName] --user`

The packages are by default installed to your home directory under `.local/lib/python3.7/site-packages`. If you would like to change the installation folder define `PYTHONUSERBASE` environmentvariable with new installation location first:

`export PYTHONUSERBASE=/projappl/<your_project>/python3.7_pip`

You should use the same export command then always also before using, inc in the batch job files.

Alternatively create a separate virtual environment with [venv](https://docs.python.org/3/library/venv.html), for example:

```
module load python-data
python -m venv --system-site-packages my-venv
source my-venv/bin/activate
pip install my_package_to_install
```

With venv, you can keep separate environments for each program. The next time you wish to activate the environment you only need to run `source my-venv/bin/activate`.

If you think that some important package should be included in a module provided by CSC, you can send an email to <servicedesk@csc.fi>. 

## Creating your own Python environments
It is also possible to create your own Python environments. The main options are conda and Singularity. Singularity could be preferred at least when you know a suitable ready Singularity or Docker container. conda is very easy to use and flexible, but it might create a lot of files that might be slow at library imports.

Singularity:

   * [Running Singularity containers](../computing/containers/run-existing.md)
   * [Creating Singularity containers](../computing/containers/creating.md), including how to convert Docker container to Singularity container.

Conda:

   * [CSC conda tutorial](../support/tutorials/conda.md) describes in detail what conda is and how to use it. 
   * [Bioconda](bioconda.md) provides conda tools preinstalled.


## License

Python packages usually are licensed under various free and open source licenses (FOSS).

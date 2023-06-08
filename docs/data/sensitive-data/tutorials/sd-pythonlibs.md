## Adding missing Python libraries to Pythion in SD Desktop

By default SD Desktop virtual machines have Python 2.7.5 (_python_) and Python 3.9.16 (_python3.9_) installed.
As Python 2 is mostly outdated, we recommend that you use python3.9 whenever possible and
also this tutorial focuses on that version only.

The Python3.9 in SD Desktop includes vide selection of commonly used libraries like _pandas_,  _numpy_ and _scipy_
but as there is huge amount of python libraries available, you quite often would like to 
use a library that is not available in SD Desktop.

In normal computers, the problem can be easily solved by adding the missing library using _pip install_ command. However, 
as SD Desktop virtual machines don't have internet connection, you can't run pip install command in the way they are normally used.

If you plan to use a complex python environment in SD Desktop, the best solution is to build an Apptainer container that 
includes all the Python libraries you need, and import that container to SD Desktop.

However, if you would need to add just few missing libraries to the Python 3.9 in SD Desktop, you could create a Python virtual environment
to ad the missing libraries. This tutorial demonstrates how you can import and install missing Python libraries to SD desktop. 
As an example we usr SciKit-Optimize library (https://scikit-optimize.github.io).



## 1. Building an installation file for SD Desktop

The first thing to do is to build a pip installation package file for the library you want to use.
This you must do outside of SD Desktop, in a machine that has internet access and  _python_ and _pip_ commands installed 
(if possible, use Python version that matches well with the Python version in SD Desktop).

In this machine, create a new directory, use _pip download_ to download the intallation files and then package 
this directory for transportation. In the case of user _asund_ in a Linux or Mac, _SciKit-Optimize_ library could be packaged 
with commands:

```text
mkdir scikit-optimize
pip download scikit-optimize -d "/home/asund/scikit-optimize"
tar cvfz scikit-optimize.tgz scikit-optimize
```
Next you should upload the installation package (_scikit-optimize.tgz_) to one of 
your data buckets in [SD Connect](https://sd-connect.csc.fi).


## 2. Installing the library

After uploading the installation package to SD Connect, you will do rest of the installation steps
in your SD Desktop environment.

1. Open terminal session and create a Python virtual environment with command
(this needs to be done only once):

```text
python3.9 -m venv $HOME/my-python
```

2. Activate your Python virtual environment and add the location of default python libraries to PYTHONPATH environment variable: 
(this you must do each time you start a new terminal session)

```text
source $HOME/my-python/bin/activate
export PYTHONPATH=/usr/local/lib/python3.9/site-packages
```

3. Open or refresh your DataGateway connection and copy _scikit-optiomize.tgz_ to your local disk.

4. Uncompress the package

```text
tar zxvf scikit-optimize.tgz
```

5. Move to the new directory:

```text
cd scikit-optimize
```

6. Install the package:

```text
pip install scikit_optimize-0.9.0-py2.py3-none -any-whl -f ./ --no-index --no-deps
```

Now python (pointing to $HOME/my-python/bin/python) should contain
_scikit_optimize_ library.

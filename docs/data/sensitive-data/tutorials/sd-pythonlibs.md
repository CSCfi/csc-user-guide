## Adding missing Python libraries to Pythion in SD Desktop

SD Desktop virtual machines have Pyhthon 2.7.5 (_python_) and Pyhthon 3.9.16 (_python3.9_).
As Python 2 is mostly outdated, we recommed that you use python3.9 whenever possible and
also this tutorial focuses on that version only.

The Pyhton3.9 in SD Desktop includes vide selection of commonly used libraries like _pandas_,  _numpy_ and _scipy_
but  as there is huge amount of pyhton libraries available, you quite often would would like to 
use a library that is not available in SD Desktop.

In normal computers, the problem can be easily solved by adding the missing library using _pip install_ command. However, 
as SD Desktop virtual machines don't have internet connection, you can't run pip install command in the way they are normally used.

If you plan to use a complex pyhton environment in Puhti, it may be most effective to build an Apptainer container that 
include all the Python libraries you need, and import that container to SD Desktop.

However, if you would need to add just few missing libraries to the Pyhton 3.9 in SD Desktop, you could Python virtual environments
to import and use these libraries. This tutorial demonstartes how you can import and install missing libraries to SD desktop. 
As an example we usr SciKit-Optimize library (https://scikit-optimize.github.io).



## 1. Building an installation file out side SD Deesktop

The first thing to do is to build a pip installation pakage file for the library you want to use.
This you can do out sede of SD Desktop, in a machine that has intrnet access and Python and  _pip_ commans installed 
(if possible use Python version that matches well the Pythonm version in SD Dektop).

In this machine create a new directory, use _pip download_ to download the intallataion files and then package 
this directory for transportation. In the case of user _asund_ in a Linux or Mac, _SciKit-Optimize_ could be packaged 
with commands:

```text
mkdir scikit-optimize
pip download skopt  -d "/home/aviuser/scikit-optimize"
tar cvfz scikit-optimize.tgz scikit-optimize
```
## 2. Installing the library

In your SD desktop VM:

1. Create python virtual environment with command
(this needs to be done only once)

python3.9 -m venv $HOME/my-python


2. Activate your python virtual environment and add the location of defaul python libraries to PYTHONPATH environment variable: 
(this you must do each time you start a new terminal session)

source $HOME/my-python/bin/activate
export PYTHONPATH=/usr/local/lib/python3.9/site-packages

3. Copy scikit-optiomize.tgz to your local disk

cp Projects/SD-Connect/project_*/tools-for-sd-desktop/apps/python/lib/scikit-optimize.tgz ./

4. Uncompress the package

tar zxvf scikit-optimize.tgz

5. Move to the new directory:

cd scikit-optimize

6. Install the package:

pip install scikit_optimize-0.9.0-py2.py3-none -any-whl -f ./ --no-index --no-debs

Now python (pointing to $HOME/my-python/bin/python) should contain
scikit_optimize library.

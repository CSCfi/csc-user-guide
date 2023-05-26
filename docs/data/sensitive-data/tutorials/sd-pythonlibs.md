## Adding missing Python libraries to Pythion in SD Desktop

SD Desktop virtual machines have Pyhthon 2.7.5 (_python_) and Pyhthon 3.9.16 (_python3.9_).
As Python 2 versions aree very outdated, we recommed that you use python3.9 whenever possiblke and
also this tutorial focuses on that version only.

The Pyhton3.9 in SD Desktop includes vide selection of commonly used libraries like _pandas_,  _numpy_ and _scipy_
but are there is huge amount of pyhton libraries availvalbe in pip repository, you quite often would would like to 
use a library that is not available. 

In normal computers, the problem can be easily solved by adding the missing library using _pip install_ command. However, 
as SD Desktop virtual machines don't have internet connection, you can't run pip install command like they ar normally used.

This tutorial demonstartes how you can import and install missing libraries to SD desktop. In this case we use 


## 1. Building an installation file.


The first thing to do is to build a pip installatio 

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

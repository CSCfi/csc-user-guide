# Adding missing Python libraries to Pythion in SD Desktop

By default, SD Desktop virtual machines based on Ubuntu 22.04 have Python 3.10.12 (`python3`) installed.

The Python3 in SD Desktop includes over 300 commonly used libraries like _pandas_, _numpy_ and _scipy_.
You can check the full list of installed libraries with command:

```text
pip list
```

As there is huge amount of python libraries available, you quite often would like to use a library that is not available in SD Desktop.

In normal computers, the problem can be easily solved by adding the missing library using `pip install` command. However, 
as SD Desktop virtual machines don't have internet connection, you can't run `pip install` command in the way it is normally used.

**If you plan to use a complex python environment in SD Desktop, the best solution is to build an Apptainer container that 
includes all the Python libraries you need, and import the container to SD Desktop**.

However, if you need to add just few missing libraries, you could create a Python virtual environment
to add the missing libraries. This tutorial demonstrates two ways to add missing Python libraries to the existing Python environment in SD desktop. As an example Python library we use [SciKit-Optimize library](https://scikit-optimize.github.io).

## Option 1: add-python-lib tool

_Add-python-lib_ is a help tool tha can be used to add python libraries to
a Python virtual environment in a SD Desktop virtual machine.
This tool can be added to your virtual machine with the [SD Sotware installer tool](./sd-software-installer.md).

Basic syntax of the command is:

```text
add-python-lib search_term 
```

The command looks for matching packages from the set of Python libraries that CSC has preloaded to SD Connect.
Note that the preloaded set of libraries is very small (some hundreds) compared to the over 300 000 libraries available through pip.
Please send a request to _servicedesk@csc.fi_ if you would need to have a library to be added to the selection.
Note that all python libraries are not compatible with this approach.

The selected library will added to a Python virtual environment that locates in _/shared-directory/sd-tools/python3-venv_.
This virtual environment is automatically created when _add-python-lib_ is used for the first time.

In the case of SciKit-Optimize, you could do the installation with command:

```text
add-python-lib scikit 
```

or 

```text
add-python-lib scikit_optimize 
```

Note that search term _SciKit-Optimize_ would not find any matching libraries as the search process is based on
the names of pip installation files, that use only small case letters and where dashes (-) are replaced with under scores (_).

If the search term you used, matches several Python libraries, the tool shows you a list of libraries from which you can
choose the library to be installed. 

After that, the tool asks, if also the dependencies of the selected library should be installed.
Normally you should try to install the dependencies too. 

Once the installation is ready, you can switch to use the Python virtual environment with commands:

```text
source /shared-directory/sd-tools/python3-venv/bin/activate
export PYTHONPATH=/usr/lib/python3/dist-packages:/usr/local/lib/python3.10/dist-packages
```


## Option 2: Importing the module through SD Connect

### 1. Downloading installation file for SD Desktop

The first thing to do is to download a pip installation package file for the library you want to use.
This you must do outside SD Desktop. You can search for the package from the [Pypi repository](https://pypi.org/)
or use _pip download_ command if you have python3 installed in your machine (if possible, use Python version that matches with the Python version in SD Desktop).

#### 1.1 Pypi repository 

In the case of SciKit-Optimize, search in the Pypi repository gives you a project list. SciKit-Optimize is the first item  on the list. You can continue to the  SciKit-Optimize project page, where the _download_ link provides a list of downloadable files. Here we could download the pre-build library file (scikit_optimize-0.10.2-py2.py3-none-any.whl ).

#### 1.2  pip in command line

In your local machine, create a new directory, use `pip download` to download the installation files and then package 
this directory for transportation. In the case of user _asund_ in a Linux or Mac, _SciKit-Optimize_ library could be packaged 
with commands:

```bash
mkdir scikit-optimize
pip download scikit-optimize -d "/home/asund/scikit-optimize"
tar cvfz scikit-optimize.tgz scikit-optimize
```

#### 1.3 Upload 

Next you should upload the installation package (`scikit_optimize-0.10.2-py2.py3-none-any.whl` or `scikit-optimize.tgz`) to one of 
your data buckets in [SD Connect](https://sd-connect.csc.fi).

### 2. Installing the library

After uploading the installation package to SD Connect, you will do rest of the installation steps
in your SD Desktop environment.

1. Open terminal session and create a Python virtual environment with command
(this needs to be done only once):

    ```bash
    python3 -m venv $HOME/my-python
    ```

2. Activate your Python virtual environment and add the location of default python libraries to `PYTHONPATH` environment variable: 
(this you must do each time you start a new terminal session)

    ```bash
    source $HOME/my-python/bin/activate
    export PYTHONPATH=/usr/local/lib/python3.10/site-packages
    ```

3. Open or refresh your DataGateway connection and copy `scikit-optimize.tgz` to your local disk.

4. Uncompress the package

    ```bash
    tar zxvf scikit-optimize.tgz
    ```

5. Move to the new directory:

    ```bash
    cd scikit-optimize
    ```

6. Install the package:

    ```bash
    pip install scikit_optimize-0.9.0-py2.py3-none -any-whl -f ./ --no-index --no-deps
    ```

Now python (pointing to `$HOME/my-python/bin/python`) should contain
_scikit_optimize_ library.

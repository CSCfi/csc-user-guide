# Jupyter
The Jupyter interactive app launches a Jupyter notebook that is accessible through the web interface.

In the app form you can select Python environment, Jupyter notebook type, working directory and some more advanced settings.

For more information about the Python environments in Puhti see the [documentation about Python](/apps/python). Note that the modules listed there are not guaranteed to work in the web interface and the installation of Python packages in Jupyter in the web interface works differently.

### Currently supported Python environments
 - geoconda
 - python-data
 - python-env (Notebook only)
 - pytorch
 - tensorflow

## Installing packages
It is possible to install packages in the Jupyter notebook using `pip`.
To install packages to your user packages directory use the following command in the notebook:  
`!{sys.executable} -m pip install --user <package>`  
Note that you should set the *User packages path* in the advanced settings if you use this option as the default is to install to your home directory, which is not recommended.

To install packages to a virtual environment you can use the command:  
`!{sys.executable} -m pip install <package>`

It it recommended to either use a virtual environment or set the Python user packages path to a directory under `/scratch` or `/projappl` when launching the app if you need to install packages.

## Customizing the environment
Custom Python environments can be created based on the Python modules or the system installed python.
The settings for customizing the Python environment are in the advanced settings in the app form.

To use a Python installation from a module that is not provided in the app form you can select *Custom* and enter your own modules in the *Custom Python module* field in the form.
You can also use it to load different versions of the modules provided by the form.
If the *Custom Python module* field is left blank, the system Python will be used. Note that this requires using virtual environments.

### Virtual environment

You can create a virtual environment by enabling the virtual environment in the app form and providing a path under `/scratch` or `/projappl` to where you want to store the environment.  
To launch a created virtual environment later you need to select the same Python module and virtual environment path as when creating the environment.
The virtual environments are currently not completely isolated as they use packages from the loaded modules.

To install packages in your virtual environment you can run the command `!{sys.executable} -m pip install <package>` in your Jupyter notebook.

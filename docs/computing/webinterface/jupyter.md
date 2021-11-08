# Jupyter
The Jupyter interactive app launches a Jupyter notebook that is accessible through the web interface.

In the app form you can select Python environment, Jupyter notebook type, working directory and some more advanced settings.

### Currently supported Python environments
 - geoconda
 - python-data
 - python-env (Notebook only)
 - pytorch (Notebook only)
 - tensorflow (Notebook only)

## Installing packages
It is possible to install packages in the Jupyter notebook using `pip`.  
If you only need some small packages you can install them in the notebook using the command:  
`!{sys.executable} -m pip install --user <package>`, for example `!{sys.executable} -m pip install --user numpy`.  
Note that this installs packages into your home folder, which is not recommended. For installing larger packages you should create a virtual environment for your Jupyter notebook, for more information see the [virtual environment](#virtual-environment) section. When installing packages to a virtual environment you should run the command without the `--user` flag.

## Customizing the environment
Custom Python environments can be created based on the Python modules or the system installed python.
The settings for customizing the Python environment are in the advanced settings in the app form.

To use a Python installation from a module that is not provided in the app form you can enter your own modules in the `Extra modules` field in the form. You can also use it to load different versions of the modules provided by the form.

### Virtual environment
For installing larger amounts of packages to your Python environment you should create a virtual environment.

You can do that by enabling the virtual environment in the app form and providing a path under `/scratch` or `/projappl` to where you want to store the environment. 
The virtual environments are currently not completely isolated as they use packages from the loaded modules. Make sure you select the same Python module when creating and loading your virtual environment.

To install packages in your virtual environment you can run the command `!{sys.executable} -m pip install <package>` in your Jupyter notebook.

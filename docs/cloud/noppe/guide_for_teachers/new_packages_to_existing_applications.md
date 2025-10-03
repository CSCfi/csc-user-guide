## Adding Python packages to an existing workspace 

You can add pip packages to existing Python applications without building a new image by installing them to your 
`my-work` or `shared` folders. The process is slightly tedious, because by principle Docker images are designed to be 
immutable, and building a new image with the needed installations is preferred.

The following steps are for `my-work` installation. Note that `my-work` is user specific and not shared with your course 
participants. If your course participants need to access the installed packages, use the `shared` folder, to which only 
the workspace owner has write permissions.

1. Open Terminal in JupyterLab.
2. Create a new folder for installation files in my-work.
3. Set `PYTHONUSERBASE` to direct to the new folder.
4. Add the new packages with pip.

```
mkdir -p /home/jovyan/my-work/<your_subdir>
export PYTHONUSERBASE=/home/jovyan/my-work/<your_subdir>
pip install --user the_new_package_name
```

Finally, exit and delete the existing session and open application settings under "Edit application".
Add `PYTHONUSERBASE=/home/jovyan/my-work/<your_subdir>` to Environment variables. Use the name of the folder you
created earlier. After this, new application sessions will have the installed packages available.

## Adding R packages to an existing RStudio application

You can add R packages to existing RStudio applications without building a new image by installing them to your 
`my-work` or `shared` folders. The process is slightly tedious, because by principle Docker images are designed to be 
immutable, and building a new image with the needed installations is preferred.

The process is as follows (detailed instructions below):

1. Open terminal in RStudio
2. Create a new folder for installation files in `my-work` or `shared`
3. Set the environment variable `R_LIBS_USER` to point to your newly created folder in application settings
4. Install the package to the newly created folder in `my-work` or `shared`

### Installation process in detail

The following steps are for `my-work` installation. Note that `my-work` is user specific and not shared with your course 
participants. If your course participants need to access the installed packages, use the `shared` folder, to which only 
the workspace owner has write permissions.

Start a session for your RStudio application, open the terminal and create a new folder for the installations (here 
named `R-packages`, but you can use a different name):
```
mkdir /home/rstudio/my-work/R-packages
```

Next, exit and delete the session. Open `Edit application` and set the following to "Environment variables":

```
R_LIBS_USER=/home/rstudio/my-work/R-packages
```

If you used a different name for your folder, remember to change it.

Open a new session for the application. The path set in the environment variable should be visible in `.libPaths()`:

```
> .libPaths()
[1] "/usr/local/lib/R/site-library" "/usr/local/lib/R/library" "/home/rstudio/my-work/R-packages"
```

Now you can install packages to the new folder, e.g.:

```
install.packages("jsonlite", lib="/home/rstudio/my-work/R-packages")
library(jsonlite)
```

The installed packages are available in all new sessions.
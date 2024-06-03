# Jupyter for courses
The Jupyter for courses app is a version of the [Jupyter app](jupyter.md) that makes using a custom
Python environment simple when hosting or participating in courses.

Python environments can be defined as modules in the project [ProjAppl directory](../disk.md#projappl-directory).
Default resources for the course Python environment can also be defined in the same directory.

## Using the app
In the form for launching the application:

 - Select the project and reservation used for the course. The reservation field will only be visible if you have an active reservation you have access to use.
 - Select the course module
 - Launch the application

## Creating a course environment

The files for course environments (modules) can be created in `/projappl/<project>/www_puhti_modules/` on Puhti and `/projappl/<project>/www_mahti_modules` on Mahti.
The directories can be created if they do not exist.

The course environment is only visible for the project that it was created for.
Note that you may need to *Restart Web Server* in the *Help* menu in the web interface if the course
environment is not visible in the form after creating the files and selecting the correct project.

Two files are needed for the course modules:

 - a `<course>.lua` file that defines the [module](../modules.md) that sets up the Python
    environment. Only files containing the text `Jupyter` will be visible in the app.
 - a `<course>-resources.yml` that defines the default resources used for Jupyter.

### Examples
Module (`/projappl/project_1234567/www_puhti_modules/some-course.lua`):
```
-- Jupyter
depends_on("module1","module2")
prepend_path("PATH","/path/to/installation/bin")
setenv("_COURSE_BASE_NAME","FolderName")
-- Relative to the course dir
setenv("_COURSE_NOTEBOOK","notebooks/tutorial.ipynb")
setenv("_COURSE_GIT_REPO","https://github.com/VeryCoolCode/projectA.git")
-- Anything valid for checkout
setenv("_COURSE_GIT_REF","")
-- lab / notebook / empty (defaults to jupyter)
setenv("_COURSE_NOTEBOOK_TYPE","notebook")
```
Resources (`/projappl/project_1234567/www_puhti_modules/some-course-resources.yml`):
```
cores: 4
time: "02:00:00"
partition: "interactive"
local_disk: 32
mem: "16GB"
reservation: "my-course-reservation"
```
Some of the resources can be omitted if they are not relevant, such as if you do not have a reservation or the partition does not have local disks.

### Tutorials
[Tutorial example for course organizers](https://github.com/CSCfi/Jupyter_www_puhti): This tutorial is useful for course organizers
who want to provide custom Jupyter notebooks *via* the web interfaces. 

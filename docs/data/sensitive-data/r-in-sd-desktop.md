# Adding RStudio and R libraries to SD Desktop

Using R and RStudio in SD Desktop virtual machines is based on an Apptainer/Singularity container that 
contains R and RStudio installations and over 1000 commonly used R libraries. However, as there 
are nearly 20 000 libraries in the CRAN repository and over 2000 libraries in the Bioconductor 
repository, it is quite common that some library that you would like to use is not included in the default selection.

This document describes the usage of help tools that you can use to add RStudio 4.2.2 and missing R libraries to your SD Desktop environment. 
The process described here is the first prototype implementation of this service and it is likely the change in the future.

## Requirements

In order to get access to the installation tool, you need to **send a request to [CSC Service desk](/support/contact/)**.
In the request, indicate that you wish that the SD Desktop software installation help tools would be made available for your project. 
You must also include to the message the **Project identifier string** of your project.

You can check this random string for example in the [SD Connect service](https://sd-connect.csc.fi). There you find the 
Project Identifier in the **User information** view. 

## Installing RStudio 4.2.2

Log in to your SD Desktop and open **Data Gateway**. If the software installation help tools are enabled for your project, then you should have folder: 
`tools-for-sd-desktop` included in the directory that Data Gateway created (in `Projects/SD Connect/your-project-name`).
Open `tools-for-sd-desktop` folder and from there, drag/copy file `sd-installer.desktop` to your desktop.

[![Installing-sd-installer](/data/sensitive-data/images/desktop/sd-installer1.png)](/data/sensitive-data/images/desktop/sd-installer1.png)

**Figure 1.** Copying `sd-installer.desktop` file to SD desktop.
 
Double click the copy of `sd-installer.desktop` to start the software installation tool. Use this tool to install _RStudio 4.2.2_ 
to your SD Desktop virtual machine if you have not yet done so. The installation takes several minutes. 

[![sd-installer](/data/sensitive-data/images/desktop/sd-installer2.png)](/data/sensitive-data/images/desktop/sd-installer2.png)

**Figure 2.** SD software installation tool.

Once the installation is done you can start RStudio by clicking the RStudio icon in the desktop or by executing command:

```text
start-rstudio
```

## Adding missing R libraries

Once the RStudio environment is installed, new libraries can be added by opening a terminal and executing command:

```text
add-R-library 
```

The command asks for a search term and shows the available R libraries that match the search string. 
If several libraries are found, you will be provided an enumerated list from which you can
select the library that should be installed.

This tool does not check for internal library dependencies, and quite often the first installation attempt fails. 
In these cases you should check the names of the missing libraries and install them first.

For example, search term _fusion_ finds 8 libraries. In this case we want to install _DNAfusion_ (`DNAfusion_1.0.0.tar.gz`), 
that is listed as the first in the list, so the installation is started by pressing _1_ and then _Enter_.

In this case, the installation however fails as DNAfusion depends on a library which is not yet installed. 
In this kind of situations you need to check the names of the missing libraries from the error message and install them first. 
You can give the name of the library as an argument to the add-R-library command. 
For example in this case the missing library, _bamsignals_, can be added with command:

```text
add-R-library bamsignals
```

After which you can install DNAfusion

```text
add-R-library DNAfusion
```

The additional libraries are installed to location `/shared-directory/sd-toold/apps/R/lib` where they are available for
all the users of the virtual machine. This is not a default location of R libraries so you must define the location in your 
R code with command:

```text
.libPaths(”/shared-directory/sd-tools/apps/R/lib/”)
```

After that you can take the library in use. e.g.

```text
library(DNAfusion)
```

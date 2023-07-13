# SD Desktop tool installer

As SD desktop virtual machiens are isolated from internet, installing additional software and libraries 
to your virtual machine is not straight forward. Adding extra software is possible, but it requires that 
you convert the installation processes into files that can be uploaded to SD Connect and from there 
copied to your SD Desktop environment for installation and usage.

In generally, we recommend using Apptainer containers for importing the software you need.

To make additional sofware installations easier, CSC has created **SD Software installer**, 
that provides an easy way to add few commonly used software packages and help tools to your Virtual machine. 
This document describes the usage of this help tool.


## Requirements ##

In order to get access to the installation tool, you need to **send a request to servicedesk@csc.fi**.
In the request, indicate that you wish that the SD software installer would be 
made available for your project. You must include to the message the  **Project identifier string** of your project.

You can check this 32 characters long random string for example in 
the [SD Connect service](https://sd-conenct.csc.fi). There you find the 
Project Identifier in the **User information** view. 

## Installing SD Software installer ##

Log in to your SD Desktop and open **Data Gateway**. If the software installation help tools are enabled for your project,
then you should have folder **tools-for-sd-desktop** included in the directory that Data Gateway created 
( in Projects/SD-Connect/_your-project-name_).

Open _tools-for-sd-desktop_ folder and from there, drag/copy file **sd-installer.desktop** to your desktop.

[![Installing-sd-installer](../images/desktop/sd-installer1.png)](./images/desktop/sd-installer1.png)

**Figure 1.** Copying sd-installer.desktop file to SD desktop.
 
Double click the copy of _sd-installer.desktop_ to start the software installation tool. 

[![sd-installer](./images/desktop/sd-installer2.png)](./images/desktop/sd-installer2.png)

## Usage ##

In order to use the installer, you must have an active Data Gateway connection running and 
mounting the SD Conncect data to the default location in the file system 
(_Projects_ in the users home directory). 

The installer shows a panels of buttons that allow you to install a software by just cliking the button.

The available software include graphical and command line applications. For graphical applications, a launching icon is added 
to the desktop. All software is installed to directory _/shared-directory/sd-tools/_ where the installaion is availale of all the
users of the virtual machine.

In case of some applications, part of the installation process occurs only when the application is started for the first time.
Thus you should start the application immediately after the installation, to make sure that the prcess is completed. After that
the installaled software should work also when Data Gateway has not been opened.


## Tool selection ##

Notes about the available tools. Note that this document may be out dated:

* [Rstudio 4.2.2](rstudio.md)





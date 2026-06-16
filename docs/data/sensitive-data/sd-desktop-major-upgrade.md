# SD Desktop: major service upgrade (CSC project- Academic type)

## Overview

The SD Desktop service has been upgraded to a new version and the changes and new features are not fully backward compatible. This guide explains the actions you need to take to continue accessing your virtual desktop and to restore import/export functionality using the new Data Gateway application. 

Your next steps depend on whether your virtual desktop currently has a volume attached.

## Step 1: Check if your virtual desktop has an external volume


1. Login to SD Desktop.
2. Select a CSC project from dropdown at the top left.
4. Checking **Volumes column** to see if the desktop has a volume attached. If number is "1" you have a volume attached and if it is "0" you don't have a volume attached.
5. Repeat for all projects. You can change CSC project from dropdown at the top left.


## Step 2: Choose the correct option for your needs

| Scenario | Recommended Action | Advantages | Disadvantages | Instructions |
|----------|------------------|------------|---------------|--------------|
| Virtual desktop **has a volume** and you don't need new features of SD Desktop | Keep the current virtual desktop and install the latest version of the  Data Gateway application| - Keep using your existing environment<br>- No need to reinstall the software<br>- Quick and simple solution |- Outated operating systehm without security patches<br>- Cannot attach/detach volumes while virtual desktop is running<br>- Cannot attach multiple volumes to the same virtual desktop<br>- Limited future compatibility<br>-  All project members must update the Data Gateway application to the new version | [Step by step guide](./sd-desktop-major-upgrade-option1.md) |
| Virtual desktop **has a volume** and you plan to continue the analysis long-term | Create a new virtual desktop and attach the existing volume to it | - Fully security-patched environment and newest operting systehm<br>- Supports attaching/detaching multiple volumes while desktop is running<br>- - Latest version of Data Gateway application is available by default<br>- Better solutin by long-term| - Requires some manual work<br>- Requires reinstalling the software<br>- Requires coodination across your reserch team | [Step by step guide](./sd-desktop-major-upgrade-option2.md) |
| Virtual desktop **has no volume** | Export your data to SD Connect, then import it to a new virtual desktop and volume | - Prevent losing data from vitual desktop failures<br>- Up to date and stable environment with latest operatign systhem<br>- Fully security-patched>br>- Supports attaching/detaching multiple volumes while desktop is running<br>- Access to the latest features | - Requires exporting all files<br>- Requires setting up a new environment Requires coodination across your reserch team | [Step by step guide](./sd-desktop-major-upgrade-option2.md) |


!!! Note
   If you need help choosing the right option or following the steps in the guides, please contact us. We are happy to provide online support with step-by-step guidance.



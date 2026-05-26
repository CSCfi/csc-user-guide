[Table of contents of user guide :material-arrow-right:](sd-services-toc.md)

# Accessing virtual desktop


* [Access virtual desktop](#access-virtual-desktop)
* [Log out from virtual desktop](#log-out-from-virtual-desktop)
* [Reconnecting to an analysis session](#reconnecting-to-an-analysis-session)
* [Connection limit](#connection-limit)


## Access virtual desktop

1. [Login](./sd-desktop-login.md) to SD Desktop. Select the correct CSC project in the top left corner. Now you can see all desktops in this project.

2. Make sure the virtual desktop you want to access is running. If it is paused, you need to [unpause](sd-desktop-manage.md#unpausing-a-virtual-desktop) it before you can access it.
  
3. Access virtual desktop by clicking **Access desktop** on right side of the desktop name.

When you open the connection, a virtual desktop will open in your browser in a new window. 

![Access virtual desktop.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew_AccessVM2.png)


## Log out from virtual desktop

1. Click **Power icon** in top right corner of the desktop. 
2. Click **Power icon** in the new window.
3. Clicking **Log Out** in the new window.
4. Confirm by clicking **Log Out** in the new window.
5. You will see a black sreen with two buttons. Click **Home** to return to SD Desktop home page. 

This will close all applications and disconnect the work session. You can access the same desktop anytime after logging in to SD Desktop.

![Log out from desktop](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew_Logout.png)


## Reconnecting to an analysis session

If you started the analysis programmatically (e.g., by running a script), you can safely close the browser window without interrupting the ongoing processes. Your tools and interfaces will remain open when you reconnect to your desktop, allowing you to continue working.


## Connection limit

**A maximum of 10** CSC project members can be logged in and use a virtual desktop at the same time. Additional users will not be able to access the desktop until one of the active members has logged out.
    
If user's connection to the desktop remains inactive for **two consecutive days**, the system will automatically log the user out to free up resources. Please [**log out**](#log-out-from-virtual-desktop) manually when you finish to avoid this.

## Your next steps in this guide

* [Working with your desktop: tips and essentials](./sd-desktop-working.md)
* [Customisation - software & tools](./sd-desktop-software.md)
* [Importing data ](./sd-desktop-access.md)
* [Exporting data  via user interface](./sd-desktop-export.md)
* [Export data programmatically](./sd-desktop-export-commandline.md)
* [Troubleshooting](./sd-desktop-troubleshooting.md)

[Table of contents of user guide :material-arrow-right:](sd-services-toc.md)

# Accessing virtual desktop

On this page: 

* [1. Access virtual desktop](#1-access-virtual-desktop)
* [2. Log out from virtual desktop](#2-log-out-from-virtual-desktop)
* [3. Reconnecting to an analysis session](#3-keeping-long-running-processes-active)
* [4. Limitations](#4-limitations)


## 1. Access virtual desktop

1. On the main page, select correct CSC project from dropdown on the left side. 
2. You will see a data table displaying the desktops in your project. Check that status of virtual desktop you want to access is **Running**.
3. Click **Access desktop**. 

The virtual desktop will open in your browser. If it's your first time using it, you'll see a **Getting Started** panel where you can adjust settings like screen resolution.

![Access desktop.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew_AccessVM2.png)


## 2. Log out from virtual desktop

1. Click **Power icon** in top right corner of the desktop. 
2. Select **Power Off/Log out**, then select **Log Out**.
3. In the confirmation window, select Log Out again.
4. Select **Home** to return to SD Desktop home page. 

This will close all applications and disconnect the work session. You can access the same desktop anytime after logging in to the services.
![Log out from desktop](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_LogOut1.png)

![Return to main view](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_LogOut2.png)

## 3. Keeping long-running processes active 

* If you started an analysis programmatically (for example, by running a script), you can use a **Byobu terminal session**. Processes running inside a Byobu session will continue even if you log out from the virtual desktop. When you reconnect to your desktop, your running processes will still be available, allowing you to resume work where you left off. 

* Alternatively, you can simply disconnect from the desktop by closing the browser without logging out if you want to keep your applications and session active. 

* In virtual desktop created before September 28, 2026, you can reconnect to a previous session only if the browser window is exactly the same size as when the original session was in use. This is typically only possible if you're using the SD Desktop in full-screen mode on the same machine. If the window size has changed, you will most likely be unable to reconnect to the old session.


## 4. Limitations

 * Each virtual desktop allows a **maximum of 10 simultaneous connections**. This means that up to 10 CSC project members can be logged in and using the system at the same time. If more than 10 CSC project members attempt to connect to the same virtual desktop, additional users will not be able to access the system until one of the active sessions is disconnected.
   
* If a connection remains inactive for two consecutive days, the system will automatically log the user out to free up resources. Please ensure you log out manually when you're finished to avoid this.

## Your next steps in this guide:

* [Working with your desktop: tips and essentials](./sd-desktop-working.md)
* [Customisation - software & tools](./sd-desktop-software.md)
* [Importing data ](./sd-desktop-access.md)
* [Exporting data  via user interface](./sd-desktop-export.md)
* [Export data programmatically](./sd-desktop-export-commandline.md)
* [Troubleshooting](./sd-desktop-troubleshooting.md)

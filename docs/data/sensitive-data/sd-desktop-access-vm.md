[Table of contents of user guide :material-arrow-right:](sd-services-toc.md)

# Accessing virtual desktop

* [Access virtual desktop](#access-virtual-desktop)
* [Log out from virtual desktop](#log-out-from-virtual-desktop)
* [Reconnecting to an analysis session](#reconnecting-to-an-analysis-session)


## Access virtual desktop

1. On the main page, select correct CSC project from dropdown on the left side. 
2. You will see a data table displaying the desktops in your project. Check that status of virtual desktop you want to access is **Running**.
3. Click **Access desktop**. 

The virtual desktop will open in your browser. If it's your first time using it, you'll see a **Getting Started** panel where you can adjust settings like screen resolution.

![Access desktop.](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew_AccessVM2.png)


## Log out from virtual desktop

1. Click **Power icon** in top right corner of the desktop. 
2. Select **Power Off/Log out**, then select **Log Ou**t.
3. Select **Log Out** in the new window.
4. Select **Home** to return to SD Desktop home page. 

This will close all applications and disconnect the work session. You can access the same desktop anytime after logging in to the services.

![Log out from desktop](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_LogOut1.png)

![Return to main view](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_LogOut2.png)

## Reconnecting to an analysis session

* **Closing the browser window:** If you started the analysis programmatically (e.g., by running a script), you can safely close the browser window without interrupting the ongoing processes. Your tools and interfaces will remain open when you reconnect to your desktop, allowing you to continue working.
* **Reconnecting to an old session:** You can reconnect to a previous session only if the browser window is exactly the same size as when the original session was in use. This is typically only possible if you're using the SD Desktop in full-screen mode on the same machine. If the window size has changed, you will most likely be unable to reconnect to the old session.

!!! Note
    Connection limit: each virtual desktop allows a maximum of 10 simultaneous connections. This means that up to 10 CSC project members can be logged in and using the system at the same time. If more than 10 CSC project members attempt to connect to the same virtual desktop, additional users will not be able to access the system until one of the active sessions is disconnected.
    If a connection remains inactive for two consecutive days, the system will automatically log the user out to free up resources. Please ensure you log out manually when you're finished to avoid this.

## Your next steps in this guide:

* [Login to SD Desktop](./sd-desktop-login.md)
* [Create virtual desktop](./sd-desktop-create.md)
* [Create volume](./sd-desktop-create-volume.md)
* [Manage virtual desktops](./sd-desktop-manage.md)
* [Manage volumes](./sd-desktop-manage-volume.md)
* [Access virtual desktop](./sd-desktop-access-vm.md)
* [Work with your desktop: tips and essentials](./sd-desktop-working.md)
* [Customisation - software & tools](./sd-desktop-software.md)
* [Import data ](./sd-desktop-access.md)
* [Export data via user interface](./sd-desktop-export.md)
* [Export data programmatically](./sd-desktop-export-commandline.md)
* [Troubleshooting](./sd-desktop-troubleshooting.md)

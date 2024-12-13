# Accessing virtual desktop

Here are instructions for accessing, reconnecting ang logging out.

## Access virtual desktop

1. After [login](./sd-desktop-login.md), you will see all your virtual desktops listed at the front page, under *All connections*.

2. Select project (e.g. `project_NNNNN`) and click the plus-sign.
  
3. Now you can see all desktops that belongs to this project (`desktopname-NNNNNNNNNN`). Access virtual desktop by clicking the name.

When you open the connection, a virtual computing environment will open in your browser. If you are accessing the virtual desktop for the first time, you will see the panel getting started, from which you can, for example, adjust the screen resolution.

![All connections](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_AllConnections.png)


## Log out from your desktop

*Log out* from the desktop (in the workspace view, top right corner of the browser, select your *username* and *log out*). This will close all applications and disconnect the work session. You can access the same desktop anytime after logging in to the services.

![Log out from desktop](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_LogOut1.png)

![Return to main view](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Desktop_LogOut2.png)

## Reconnecting to an analysis session

* Closing the browser window: If you started the analysis programmatically (e.g., by running a script), you can safely close the browser window without interrupting the ongoing processes. Your tools and interfaces will remain open when you reconnect to your desktop, allowing you to continue working.
* Reconnecting to an old session: You can reconnect to a previous session only if the browser window is exactly the same size as when the original session was in use. This is typically only possible if you're using the SD Desktop in full-screen mode on the same machine. If the window size has changed, you will most likely be unable to reconnect to the old session.

!!! Note
    Connection limit: each virtual desktop allows a maximum of 10 simultaneous connections. This means that up to 10 CSC project members can be logged in and using the system at the same time. If more than 10 CSC project members attempt to connect to the same virtual desktop, additional users will not be able to access the system until one of the active sessions is disconnected.
    If a connection remains inactive for two consecutive days, the system will automatically log the user out to free up resources. Please ensure you log out manually when you're finished to avoid this.
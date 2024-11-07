
**You can work with your virtual desktop like with a standard computer**, accessing several pre-installed programs from the applications menu bar (top left corner). Examples include Open Office, image-viewing applications, video and audio players, Jupyter Notebooks etc. You can also open a terminal and use Linux from the command line. For more information on accessing R-Studio, please [check the paragraph below](#accessing-rstudio).

### Security-related features of SD Desktop:

1. The computing environment i.e. virtual desktop (visible from your browser) is isolated from the internet. For example, you can open a Firefox web browser in your virtual desktop but not access any site online. At this moment, you will also not be able to access any repositories directly.

2. You can access or import files into the virtual desktop only by using the [Data Gateway](#accessing-encrypted-sensitive-data-within-sd-desktop) application;

3. Unencrypted files are not visible via the SD Desktop service. You can access and visualize only encrypted files. You can encrypt files with [SD Connect](./sd_connect.md) or programmatically with the service's public encryption key. [Read more about encryption](./sd-connect-introduction-to-data-encryption.md).

4. The copy-paste function from your computer/laptop to your virtual desktop is limited for security reasons. [Instructions how to copy-paste](#copy-paste-from-your-laptop-to-virtual-desktop).

5. Only files saved in the shared-directory or the external volume are accessible to all project members via the virtual desktop. Read more about [external volume](./sd-desktop-create.md#3-add-an-external-volume-virtual-external-hard-drive).

### You can close the connection to your virtual desktop in two ways:

1. _Log out_ from the desktop (in the workspace view, top right corner of the browser, select your _username_ and _log out_). This will close all applications and disconnect the work session. You can access the same desktop anytime after logging in to the services.

2. If you initiated an analysis programmatically (running a script), you can close the browser window. This doesn't interfere with the processes running. Thus, when you reconnect to your desktop, all your tools and interfaces are still open and you can continue working. However, log out from the desktop once the analysis is finished. If you leave more than ten connections open, you will be unable to re-access the services. 

!!! Note
    * SD Desktop supports only 10 simultaneous connections. 
    * You will be automatically logged out from the virtual desktop if a connection has been left accidentally active for two days.
 
 
 [![Access-virtual-Desktop](images/desktop/desktop-access.png)](images/desktop/desktop-access.png)

### Accessing RStudio 

Open the terminal and launch RStudio with:

```text
start-rstudio-server
```

This will return a URL and a service-specific password:

```text
RStudio Server - Sensitive Data Desktop Edition
---------------------------------------------------------------------------------------
Copy/Paste this URL into Firefox:

http://localhost:8787/

-----------------------------------------------------------------------------------------
Enter these at the RStudio Server sign-in screen
----------------------------------------------------------------------------------------
Username: accountname  Password: Example23241232
----------------------------------------------------------------------------------------
To stop RStudio Server: Ctrl+C
```

Next:

* paste the URL in Firefox 
* after a few seconds, you can input the username and password (service-specific) and access the server.

!!! Note
    Only files saved in shared-directory or external volume are accessible to other project members using RStudio.


[![Desktop-rstudio](images/desktop/desktop-rstudio.png)](images/desktop/desktop-rstudio.png)

### Copy-paste from your laptop to virtual desktop

The copy-paste function from your computer/laptop to your virtual desktop is limited for security reasons. However it is possible to copy-paste text with Clipboard. Copy-paste works only in one direction: from your computer to virtual desktop.

#### Step by step tutorial
1. Go to virtual desktop and open the Clipboard with a key combination **Cntrl+Alt+Shift** and click *Paste*.
2. Activate the copy-paste function by selecting input method ***Text input*** (the Clipboard panel will close automatically after the selection).
3. Now you can copy text normally from your computer (Cntrl+C or mouse right click).
4. Paste the text inside your virtual desktop (Cntrl+C).

Note: Don't close Clipboard panel with **Cntrl+Alt+Shift**, this might disable the copy-paste function. Please note you have to activate the copy-paste function again every time you use your virtual desktop. 

![SD Desktop Clipboard screenshot](images/desktop/SD-Desktop-Clipboard.png)
*Appearance of the Clipboard (Guacamole tools) may vary a bit depending on browser and local operating system.*


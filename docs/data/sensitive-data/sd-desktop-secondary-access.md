# Importing data for analysis

Once a virtual desktop is created, each CSC project member can access it through their browser. The virtual desktop is isolated from the internet, so data access must be done through the Data Gateway application. This application allows you to import data from SD Apply. Imported data is saved on the virtual desktop’s external volume for secure analysis.

## Prerequisites

* **What is an external volume?** Your virtual desktop’s local storage is limited, so it’s recommended to save large data files and collaborative work on the external volume. This volume acts like an external hard drive that can be detached and reattached to different desktops, allowing project members to share and edit files stored there.
* **Adding the external volume:** the external volume can only be added when creating a [new virtual desktop](../sensitive-data/sd-desktop-create.md)
* **Additional volume space:** if you need additional volume space (more than 200 GB), you can request it by writing to CSC Service Desk, (subject: SD Desktop), **please be aware that volume extensions are only possible before any data has been added to the volume**.

## Step by step

### Step 1: access virtual desktop

1. After [log in](./sd-desktop-login.md), you will see all your virtual desktops listed at the front page, under *All connections*.
   
2. Select project (e.g. `project_NNNNN`) and click the plus-sign.
   
3. Now you can see all desktops that belongs to this project (`desktopname-NNNNNNNNNN`). Connect with the virtual desktop by clicking the name.

When you open the connection, a virtual computing environment will open in your browser. If you are accessing the virtual desktop for the first time, you will see the panel getting started, from which you can, for example, adjust the screen resolution.

![check the paragraph below](../sensitive-data/images/desktop/SD-Desktop-Frontpage.png)

### Step 2: access data via the Data Gateway application

1. Locate the application on your desktop.
   
2. Select SD Apply (Accessible only if the data controller has granted you permission).
   
3. Click Login, then Continue.
   
4. In the next window, under Create Secure Access, select Create. This establishes a secure connection and creates a Projects folder visible on your desktop (and accessible from the terminal).
   
7. Click Open Folder to view all files stored in SD Apply. Files are available in read-only mode for secure access. to view their content, right-click the file and select the desired application to open it.

!!! Note
    The Projects folder is available only when the Data Gateway application is open. 


[![Data-gateway1](images/desktop/desktop-gateway-part1.png)](images/desktop/desktop-gateway-part1.png)

[![Data-gateway2](images/desktop/desktop-gateway-part2.png)](images/desktop/desktop-gateway-part2.png)

### Step 3: import a copy of the files on your virtual desktop's volume

1. Keep Data Gateway connection open: select and copy the files or folders from the Projects folder.
   
2. Paste them into the external volume within your virtual desktop, located on the left side menu.
   
3. Files or folders will automatically decrypt during the copy process and become available for analysis.

[![Desktop-data-import](images/desktop/desktop-gateway-import.png)](images/desktop/desktop-gateway-import.png)

### Step 4: setting permissions for shared access

After copying files to the external volume, adjust permissions to enable access for other project members. By default, permissions are limited to your access only, so these steps ensure that others can view and edit the data.

1. **Adjust folder permissions**:
    * Right-click the folder on the external volume, select Properties, and open the Permissions tab.
    * Set permissions to Create and Delete Files for each user to allow full access.
  
2. **Adjust file permissions**:
    * For individual files, right-click each file, select Properties, and change permissions to Read and Write.
    * For folders, set permissions to Create and Delete Files so they remain accessible when the volume is reattached to a different virtual desktop.

Once permissions are set, your files are ready for collaborative work, and all project members with access can view and analyze them.

### Step 5: close the Data Gateway application

You can now disconnect the Data Gateway connection if no further data import are needed.

!!! Note
    If more than 10 data gateway connection are left open, the data gateway will stop working. In this case, [contact CSC Service Desk](../../support/contact.md) (subject: SD Desktop).

### Step 6: disconnect from your desktop

1. *Log out* from the desktop (in the workspace view, top right corner of the browser, select your *username* and *log out*). This will close all applications and disconnect the work session. You can access the same desktop anytime after logging in to the services.
   
2. **Reconnecting to an analysis session**:
   
2.1 Closing the browser window: If you started the analysis programmatically (e.g., by running a script), you can safely close the browser window without interrupting the ongoing processes. Your tools and interfaces will remain open when you reconnect to your desktop, allowing you to continue working.

2.2 Reconnecting to an old session: You can reconnect to a previous session only if the browser window is exactly the same size as when the original session was in use. This is typically only possible if you're using the SD Desktop in full-screen mode on the same machine. If the window size has changed, you will most likely be unable to reconnect to the old session.




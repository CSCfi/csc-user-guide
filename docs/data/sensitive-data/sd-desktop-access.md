# Accessing and importing data in your virtual desktop 

<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/EhuAYNLS90g" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/7iGQ7gWb-Pk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


Once a virtual desktop has been created, each CSC project member can access the virtual desktop through their browser. Since it’s isolated from the internet, data access requires using the Data Gateway application, which imports data from SD Connect or SD Apply. Imported data is saved on the virtual desktop’s external volume for secure analysis.



## Prerequisite:

* **What is an external volume?** Your virtual desktop’s local storage is limited, so it’s recommended to save large data files and collaborative work on the external volume. This volume acts like an external hard drive that can be detached and reattached to different desktops, allowing project members to share and edit files stored there.

* **Adding the external volume:** the external volume can only be added when creating a [new virtual desktop](./sensitive-data/sd-desktop-create.md)

* **Additional voluem space:** if you need additional volume space (more than 200 GB), you can request it by CSC Service Desk, (subject: SD Desktop), please be aware that volume extensions are only possible before any data has been added to the volume.

   
## Step by step

### Step 1: access virtual desktop

1. After [log in](./sd-desktop-login.md), you will see all your virtual desktops listed at the front page, under *All connections*. 

2. Select project (e.g. `project_NNNNN`) and click the plus-sign.
  
3. Now you can see all desktops that belongs to this project (`desktopname-NNNNNNNNNN`). Access virtual desktop by clicking the name.
  

When you open the connection, a virtual computing environment will open in your browser. If you are accessing the virtual desktop for the first time, you will see the panel getting started, from which you can, for example, adjust the screen resolution.

![check the paragraph below](../sensitive-data/images/desktop/SD-Desktop-Frontpage.png)

### Step 2: access data via the Data Gateway application

1. Locate the application on your desktop.

2. Select connection method:
   
*  SD Connect: For data you’ve uploaded directly to CSC. Enter your CSC username and password (note that copy-paste is disabled for security, so type your password manually).
  
*  SD Apply: Accessible only if the data controller has granted you permission.

3. Click Login, then Continue.

4. In the next window, under Create Secure Access, select Create. This establishes a secure connection bewteen your virtual desktop and your data, and create a Projects folder visible on your desktop (and accessible from the terminal).

5. Click Open Folder to view all files stored in SD Connect or SD Apply. Files are available in read-only mode for secure access, but to view them, right-click the file and select the desired application to open it.


!!! Note
    In SD Desktop, **you can access only encrypted files.** Accessing unencrypted data or files encrypted only with your public encryption key will result in an error. 
 
[![Data-gateway1](images/desktop/desktop-gateway-part1.png)](images/desktop/desktop-gateway-part1.png)

[![Data-gateway2](images/desktop/desktop-gateway-part2.png)](images/desktop/desktop-gateway-part2.png)
 
 
### Step 3: import a copy of the files on your virtual desktop's volume

1. Keep Data Gateway connection open: select and copy the files or folders from the Projects folder.

2. Paste them into the external volume within your virtual desktop, located on the left side menu.
   
4. Files or folders will automatically decrypt during the copy process and become available for analysis.

 [![Desktop-data-import](images/desktop/desktop-gateway-import.png)](images/desktop/desktop-gateway-import.png)

### Step 4: setting permissions for shared access

After copying files to the external volume, adjust permissions to enable access for other project members. By default, permissions are limited to your access only, so these steps ensure that others can view and edit the data.

1. Adjust Folder Permissions:

* Right-click the folder on the external volume, select Properties, and open the Permissions tab.
  
* Set permissions to Create and Delete Files for each user to allow full access.
  
2. Adjust File Permissions:
   
* For individual files, right-click each file, select Properties, and change permissions to Read and Write.
  
* For folders, set permissions to Create and Delete Files so they remain accessible when the volume is reattached to a different virtual desktop.


Once permissions are set, your files are ready for collaborative work, and all project members with access can view and analyze them. 

### Step 5: close the Data Gateway application

You can now disconnect the Data Gateway connection if no further data accessor import are needed.

!!! Note
    If more than 10 data gateway connection are left open, the data gateway will stop working. In this case, contact us at servicedesk@csc.fi (subject: SD Desktop)

### Steo 6: logout from your desktop

1. _Log out_ from the desktop (in the workspace view, top right corner of the browser, select your _username_ and _log out_). This will close all applications and disconnect the work session. You can access the same desktop anytime after logging in to the services.

2. If you initiated an analysis programmatically (running a script), you can close the browser window. This doesn't interfere with the processes running. Thus, when you reconnect to your desktop, all your tools and interfaces are still open and you can continue working. However, log out from the desktop once the analysis is finished. If you leave more than ten connections open, you will be unable to re-access the services. 

!!! Note
    * SD Desktop supports only 10 simultaneous connections.
    * You will be automatically logged out from the virtual desktop if a connection has been left accidentally active for two days.



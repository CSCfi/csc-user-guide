# Accessing and importing data in yoru vrtual desktop 

<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/EhuAYNLS90g" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/7iGQ7gWb-Pk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


Once a virtual desktop has been created, each CSC project member can access the virtual desktop through their browser. Since it’s isolated from the internet, data access requires using the Data Gateway application, which imports data from SD Connect or SD Apply. Imported data is saved on the virtual desktop’s external volume for secure analysis.



## Prerequisite:

* **What is an external volume?** Your virtual desktop’s local storage is limited, so it’s recommended to save large data files and collaborative work on the external volume. This volume acts like an external hard drive that can be detached and reattached to different desktops, allowing project members to share and edit files stored there.

* **Adding the external volume:** the external volume can only be added when creating a [new virtual desktop](./sensitive-data/sd-desktop-create.md)

* **Additional voluem space:** if you need additional volume space (more than 200 GB), you can request it by CSC Service Desk, (subject: SD Desktop), please be aware that volume extensions are only possible before any data has been added to the volume.

   
## Step by step

## Step 1: access virtual desktop

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
 
[![Desktop-apply](images/desktop/desktop-apply.png)](images/desktop/desktop-apply.png)

 
### Step 2: import a copy of the files on your virtual desktop's volume

1. Keep Data Gateway connection open: select and copy the files or folders from the Projects folder.

2. Paste them into the external volume within your virtual desktop, located on the left side menu.
   
4. Files or folders will automatically decrypt during the copy process and become available for analysis.

 [![Desktop-data-import](images/desktop/desktop-gateway-import.png)](images/desktop/desktop-gateway-import.png)

### Step 3: setting permissions for shared access

After copying files to the external volume, adjust permissions to enable access for other project members. By default, permissions are limited to your access only, so these steps ensure that others can view and edit the data.

1. Adjust Folder Permissions:

* Right-click the folder on the external volume, select Properties, and open the Permissions tab.
  
* Set permissions to Create and Delete Files for each user to allow full access.
  
2. Adjust File Permissions:
   
* For individual files, right-click each file, select Properties, and change permissions to Read and Write.
  
* For folders, set permissions to Create and Delete Files so they remain accessible when the volume is reattached to a different virtual desktop.


Once permissions are set, your files are ready for collaborative work, and all project members with access can view and analyze them. 

### Step 4: close the Data Gateway application

You can now disconnect the Data Gateway connection if no further data accessor import are needed.

!!! Note
    If more than 10 data gateway connection are left open, the data gateway will stop working. In this case, contact us at servicedesk@csc.fi (subject: SD Desktop)

### Steo 5: logout from your desktop

1. _Log out_ from the desktop (in the workspace view, top right corner of the browser, select your _username_ and _log out_). This will close all applications and disconnect the work session. You can access the same desktop anytime after logging in to the services.

2. If you initiated an analysis programmatically (running a script), you can close the browser window. This doesn't interfere with the processes running. Thus, when you reconnect to your desktop, all your tools and interfaces are still open and you can continue working. However, log out from the desktop once the analysis is finished. If you leave more than ten connections open, you will be unable to re-access the services. 

!!! Note
    * SD Desktop supports only 10 simultaneous connections.
    * You will be automatically logged out from the virtual desktop if a connection has been left accidentally active for two days.














# Working with your virtual desktop


<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/EhuAYNLS90g" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Once a virtual desktop has been created, each CSC project member can access it via their browser and import files stored in SD Connect or SD Apply in teh secure enviroment. 


## Access virtual desktop

After [log in](./sd-desktop-login.md), you will see all your virtual desktops listed at the front page, under *All connections*. 

* **All connections**. Select project (e.g. `project_NNNNN`) and click the plus-sign. There you can see all desktops that belongs to this project (`desktopname-NNNNNNNNNN`). Access virtual desktop by clicking the name.
* **Recent connections**. Your recently used virtual desktops appear also here.

![check the paragraph below](../sensitive-data/images/desktop/SD-Desktop-Frontpage.png)


When you open the connection, a virtual computing environment will open in your browser. If you are accessing the virtual desktop for the first time, you will see the panel getting started, from which you can, for example, adjust the screen resolution.


## Accessing encrypted sensitive data within SD Desktop

As the virtual desktop is isolated from the internet, the only way to access data for analysis is by utilizing a specific application called _Data Gateway_.

This application will allow you to establish a secure connection with two other Sensitive Data Service components and:

* Access and analyze encrypted files directly uploaded via SD Connect by any of the project members
* Reuse published data under controlled access via the Sensitive Data (SD) Apply service.

Encrypted files are visible in read-only mode (similar to opening a PDF file or streaming a YouTube video). This solution allows you to process large amounts of data without storing additional copies on your virtual desktop. 

!!! Note
    In SD Desktop, **you can access only encrypted files.** Accessing unencrypted data or files encrypted only with your public encryption key will result in an error. 
   
### Accessing encrypted data stored in SD Connect using Data Gateway

<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/7iGQ7gWb-Pk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


You can access encrypted data stored in SD Connect by following these steps:

1. Open _Data Gateway_ (you can find the application on your desktop)

2. Select _SD Connect_

3. Add your CSC credentials (username and password). Note: we disabled the copy/paste options for security reasons; thus, you need to type in your password

4. Click on _Login_ and next click on _Continue_

5. In the new window, under _Create secure access_ click on _Create_. The application will create a secure connection with SD Connect, and a new folder called _Projects_ will be accessible from your desktop or programmatically from the terminal. Next, click on _Open folder_.

 
 [![Data-gateway1](images/desktop/desktop-gateway-part1.png)](images/desktop/desktop-gateway-part1.png)


You can directly access all the files stored in SD Connect in read-only mode from the project folder. The application will automatically decrypt them. The current streaming speed can be up to 50 MB/s. 

!!! Note 
    The _Projects_ folder is available only when the Data Gateway application is open. Thus, Data Gateway needs to be open during data processing in streaming mode.
    

 [![Data-gateway2](images/desktop/desktop-gateway-part2.png)](images/desktop/desktop-gateway-part2.png)

### Importing data inside the desktop

If during the analysis phase you need to edit or annotate files, you make a full copy of it on your virtual desktop following these steps: 

 1. Access the files of interest in the _Project folder_ using _Data Gateway_
 
 2. Select the files from the Project folder, make a copy and paste it in the virtual desktop home directory (the files will be visible only from your browser) or in the shared folder (in this case, the files will be accessible also by all the CSC project members). 

The files are automatically decrypted by the Data Gateway application during the copy/paste process and are directly available for analysis or editing. 

 
!!! Note
    Your private workspace in SD Desktop is completely isolated from the internet for security reasons. However, you can use the procedure described above if you need to import specific scripts into your desktop (for example, from GitHub or other trusted repositories).
    
     
 [![Desktop-data-import](images/desktop/desktop-gateway-import.png)](images/desktop/desktop-gateway-import.png)


### Accessing published data for reuse via SD Apply

<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/1cF_NQV6vyk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


Data Gateway can also be used to access data published under controlled access via other Sensitive Data Service components. To access a specific dataset for reuse on your virtual desktop, you must first apply for it using SD Apply service. When the data owner (or Data Access Committee) has granted you access, you can access the dataset in SD Desktop for a limited time.


You will encounter an error message if you still need to apply for access or if the access period has ended. 


 [![Desktop-apply](images/desktop/desktop-apply.png)](images/desktop/desktop-apply.png)


SD Apply is currently in the pilot phase. Don't hesitate to [contact CSC Service Desk](../../support/contact.md) (subject: sensitive data) for more information.

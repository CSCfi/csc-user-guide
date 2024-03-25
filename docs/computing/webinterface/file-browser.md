# File browser

The file browser can be opened using the _Files_ section on the top navbar (this displays a list of all project disk areas), or using 
the shortcut to the home folder at the bottom of the front page. In the file browser
you can upload/download files, create new files and directories, or open a shell in the current directory. 

!!! note
    Keep the tab with the file browser open while the file transfer is in progress to ensure that it completes successfully.
    Uploaded files will overwrite existing files with the same name without prompting.
    Currently the maximum size for individual file uploads is 10GB

Clicking on a file will open it in view only mode, for more options like editing, renaming and deleting, use the button with three dots next to the filename. 

The file browser comes with a basic text editor. Some important notes on that:

- If no changes have been made, the _save_ button is grayed out.
- There is no _save-as_ feature
- If a read-only file is opened no indication will be given to the user but no changes will be applied

## Using Allas

In the web interface, the [Allas object storage service](../../../computing/allas) can also be accessed
using the file browser.

To configure authentication for Allas it is recommended that you use the _Cloud storage configuration_ app available in the web interface.
Once you open the app, you will be prompted to enter your CSC password.
After you have authenticated using your password, you will be able to create both S3 and Swift connections, also known as remotes, to Allas.
The remotes are only valid for a single project, but you can create remotes for all of your projects.
The created remotes will be visible in the _Files_ dropdown in the navbar and in the file browser.
!!! note
    The Swift and S3 protocols are not fully compatible with each other, particularly with files larger than 5 GB.
    For more details about the differences between the protocols, see [Allas protocols](../../../data/Allas/introduction/#protocols).

Additionally, LUMI-O is also supported for use through the file browser and can be configured by
running _allas-conf_ as `allas-conf --lumi`.
After running the command, the web interface server must be restarted, which can be done by clicking
_Restart web server_ in the _Help_ menu in top right section of the navbar.
Once the server has been restarted, the `lumi-o` remote will be available in the _Files_ dropdown
in the navbar and in the file browser.

Configured remotes that are not accessible, for example, due to expired authentication or network
connection issues, are not be visible in the _Files_ dropdown menu.

The file browser works the same way when accessing Allas as it does when accessing the shared
filesystem on the supercomputer.
Note that uploading large files from your local computer to Allas is currently not recommended due
to technical limitations.


## Using IDA

The [IDA storage service](../../../data/ida/using_ida)
can also be used, although some key features, such as moving data from the
staging area to the frozen area, are only possible though the [IDA WWW-interface](https://ida.fairdata.fi).
To use IDA in the web interface, it must first be configured for use with Rclone on a login node as follows.
```
module load allas
rclone config
```
In the Rclone configuration interface, create a new remote with the following options:

1. Storage: WebDAV (#45)
2. URL: [https://ida.fairdata.fi/remote.php/webdav/](https://ida.fairdata.fi/remote.php/webdav/)
3. Vendor: Nextcloud (#1)
4. Username: Your CSC username
5. Password: Login to the [IDA WWW-interface](https://ida.fairdata.fi), go to the settings in the top right corner.
    Go to the _Security_ tab and create a new app password.
    Copy the password and paste it in the Rclone configuration interface.
6. Bearer token: Leave empty
7. Advanced config: No

After completing the Rclone configuration, the web interface server must be restarted, which can be done by clicking
_Restart web server_ in the _Help_ menu in top right section of the navbar in the web interface.
IDA can then be accessed in the file browser, where you will be able to upload, download, transfer and edit files in the staging area
and view and download files in the frozen area.


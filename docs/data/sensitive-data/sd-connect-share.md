[Table of contents of user guide :material-arrow-right:](sd-services-toc.md)

# Sharing buckets


!!! info "Share ID"

    With SD Connect, you can share a bucket and its entire content across different CSC projects. This is done by using Share ID, a unique 32-digit code associated with a CSC project. You can share a bucket and its entire content with multiple CSC projects and use different permission levels. 


## Sharing buckets options

SD Connect provides different ways to share a bucket and its entire content with another CSC project. Choose the option that best matches how the data will be used.

**Share for data transfer**: Share one or more buckets with another CSC project so its members can copy and download the data. Use this option when you want to transfer data to another project, research group, or organization. Before proceeding,[read about the use case here]](./sd-connect-share-tranfer-data.md).

**Share for collaboration and shared workspace**: Share a bucket with another CSC project so both projects can work with the same data. Members of both projects can upload, download, copy and delete files in the shared bucket. Use this option when multiple teams need to collaborate on a dataset. Before proceeding,[read about the use case here](./sd-connect-share-workspace.md)

**Share for Read-Only Access**: Allow another CSC project to one of more buckets content the data only via SD Desktop, so its members can only access it in a secure and isolated computing environment for analysis. Use this when you need maximum certainty that your files are not distributed further. Before proceeding,[read about the use case here](./sd-connect-share-read-to-sd-desktop.md) and ** note that you also have to be the project manager of the recipient project**.


!!! warning
   Assigning the wrong sharing option may grant unintended access to your data. If you are new to SD services, contact [contact CSC Service Desk](../../support/contact.md) to discuss this option before proceeding.



## Share buckets to another CSC project: step-by-step


1. Ask from recipient for their project Share ID. They find it from their SD Connect. The recipient should select correct CSC project from the top left corner, then click **Copy Share ID** next to the project number) and provide it to you via email. 
![(screenshot)](https://a3s.fi/docs-files/sensitive-data/SD_Connect/UseCase_ShareID.png)
2. Click “**Share**” button on the right side of the folder you want to share.
![screenshot](https://a3s.fi/docs-files/sensitive-data/SD_Connect/UseCase_ShareButton.png)
3. Add the recipient project's **Share ID** to the field.
![screenshot](https://a3s.fi/docs-files/sensitive-data/SD_Connect/UseCase_AddShareID.png)
4. Select suitable sharing permission. Click “**Share**”.
![screenshot](https://a3s.fi/docs-files/sensitive-data/SD_Connect/UseCase_SelectPermission.png)

### Change share permission

1. Click “**Share**” button on the right side of the folder.
2. Scroll down and under "This project is shared to" title select correct Share ID and then change permission from "Permissions" dropdown. 
![screenshot](https://a3s.fi/docs-files/sensitive-data/SD_Connect/UseCase_ChangePermissions.png)


## Features in SD Connect

* [Upload](./sd-connect-upload.md)
* [Share](./sd-connect-share.md)
* [Download](./sd-connect-download.md)
* [Delete](./sd-connect-delete.md)
* [Command line interface](./sd-connect-command-line-interface.md)
* [Troubleshooting](./sd-connect-troubleshooting.md)



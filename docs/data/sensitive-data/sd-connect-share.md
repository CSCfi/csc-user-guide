[Table of contents of user guide :material-arrow-right:](sd-services-toc.md)

# Sharing buckets


SD Connect provides different ways to share a bucket and its entire content with another CSC project. Choose the option that best matches how the data will be used.

**Share for data transfer**: Share one or more buckets with another CSC project so its members can copy and download the data. Use this option when you want to transfer data to another project, research group, or organization.

**Share for collaboration and shared workspace**: Share a bucket with another CSC project so both projects can work with the same data. Members of both projects can upload, download, copy and delete files in the shared bucket. Use this option when multiple teams need to collaborate on a dataset.

**Share for Read-Only Access**: Allow another CSC project to access the data through SD Desktop without modifying the original bucket contents. Use this option when you want others to analyze or review data while retaining control of the source data.



!!! info "Share ID"

    With SD Connect, you can share buckets across different CSC projects. This is done by using Share ID, a unique 32-digit code associated with a CSC project. You can share a bucket and its entire content with multiple CSC projects and use different permission levels. 

SD Connects provides you multiple ways to share a bucket and its entire content. Please read about permission rights and example use cases which demonstrate how the different permissions:

* [Transfer data](#transfer-data): the recipient project’s members can copy your folder in SD Connect and download files in decrypted format. Files are also accessible via SD Desktop. Use this when you want to transfer your data to another project.

[Read about use case: Transfer your data to another project](./sd-connect-share-tranfer-data.md)* [Collaborate](#collaborate)
* [Read to SD Desktop](#read-to-sd-desktop)


## Share buckets to another project


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

## Permission rights and example use cases

 Please read about permission rights and example use cases which demonstrate how the different permissions can be applied based on specific collaboration requirements and data sharing needs.

### Transfer data




### Collaborate

In addition to Transfer data permission, the recipient project’s members can upload new files or delete existing files from your folder in SD Connect. Use this when you want the folder to be your shared workspace.

[Read about use case: Use folder as your shared workspace](./sd-connect-share-workspace.md)



### Read to SD Desktop

The recipient project's members can only access the folder content in SD Desktop. Use this when you need maximum certainty that your files are not distributed further.

!!! warning
    Note that you also have to be the project manager of the recipient project. Please [contact CSC Service Desk](../../support/contact.md) to discuss this option before proceeding.

[Read about use case: Give access to folder content only in SD Desktop](./sd-connect-share-read-to-sd-desktop.md)

## Features in SD Connect

* [Upload](./sd-connect-upload.md)
* [Share](./sd-connect-share.md)
* [Download](./sd-connect-download.md)
* [Delete](./sd-connect-delete.md)
* [Command line interface](./sd-connect-command-line-interface.md)
* [Troubleshooting](./sd-connect-troubleshooting.md)



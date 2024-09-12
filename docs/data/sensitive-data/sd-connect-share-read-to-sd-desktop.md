# How to give access to folder content only in SD Desktop

!!! error-label

    Not yet available

## Use case

You (Team A) have data that other team (Team B) needs access to. They wish to view and analyse your data, but you want to restrict their ability to download a copy of the data directly.

## Solution

In this case you can share your data folder to Team B with **Read to SD Desktop** -permission. That way Team B members can view and analyse the data via SD Desktop, without downloading a copy of the original data.

You also don’t want Team B to export your original data from SD Desktop. That is why you need to create a project where they (Team B) are project members and you are the project manager - since only project manager can export data from SD Desktop.


![Transfer Data Infograph](https://a3s.fi/docs-files/sensitive-data/SD_Connect/UseCase_ReadToDesktop.png)

!!! warning
    Note that you have to be the project manager of the both projects. Please contact us at *servicedesk@csc.fi* subject: *Sensitive data* to discuss this share option before proceeding.

## Step by step tutorial

1. Log in to [MyCSC](https://my.csc.fi/login){ target="_blank" }.
2. Create two new projects: ***Project 1*** and ***Project 2***.
3. Manage ***Project 1***: enable service access for SD Connect. Do not add any project members. [See instructions](./sd-access.md)
4. Manage ***Project 2***: enable service access for SD Connect and SD Desktop. Add Team B to be the **project members.** [See instructions](./sd-access.md)
5. Log in to [SD Connect](./sd-connect-login.md).
6. Select ***Project 2*** and copy the **Share ID**. 
![screenshot](https://a3s.fi/docs-files/sensitive-data/SD_Connect/UseCase_ShareID2.png)
7. Select ***Project 1*** and upload your data folder there: [See upload instructions](./sd-connect-upload.md).
8. Click “**Share**” next to the folder you just uploaded.
![screenshot](https://a3s.fi/docs-files/sensitive-data/SD_Connect/UseCase_ShareButton2.png)
9. Add the **Share ID** of Project 2 to the field.
![screenshot](https://a3s.fi/docs-files/sensitive-data/SD_Connect/UseCase_AddShareID2.png)
10. Select sharing permission: “**Read to SD Desktop**”. Click “**Share**”.
![screenshot](https://a3s.fi/docs-files/sensitive-data/SD_Connect/UseCase_SelectPermission2.png)

Now, all the content in the folder is visible to Project 2 (Team B) and accessible only through SD Desktop. Project 2 members can access and analyse the shared folder content via SD desktop. However, they cannot export or download files, as all data exports are managed directly by the project manager - and you are the project manager of both projects.


## Features in SD Connect 

* [Upload](./sd-connect-upload.md)
* [Share](./sd-connect-share.md)
* [Download](./sd-connect-download.md)
* [Delete](./sd-connect-delete.md)


[Table of contents of user guide :material-arrow-right:](sd-services-toc.md)

# Sharing buckets

* [Sharing buckets to another CSC project: overview](#sharing-buckets-to-another-csc-project-overview)
* [Share buckets to another CSC project: step-by-step](#share-buckets-to-another-csc-project-step-by-step)
* [Change sharing permission](#change-sharing-permission)
* [Delete sharing permission](#delete-sharing-permission)


## Sharing buckets to another CSC project: overview


!!! info "Share ID"

    With SD Connect, you can share a bucket and all its contents with other CSC projects. Sharing is done using the **recipient project's Share ID**, a unique 32-digit identifier assigned to each CSC project. A bucket can be shared with multiple projects, and you can assign different permission levels to each shared project.

Before proceeding familiarize yourself with different use cases and choose the option that best matches how the data will be used:


<div class="grid cards csc-quick-links csc-quick-links--compact" markdown>

- **Share for data transfer**
  { .csc-grid-card-info }

    ---
    
    Share one or more buckets with another CSC project so its members can copy and download the data. 
    
    Use this option when you want to transfer data to another project, research group, or organization. 
    
    [**Read more about the use case**](./sd-connect-share-tranfer-data.md)


-   **Share for collaboration and shared workspace**
  { .csc-grid-card-info }

    ---
    
    Share a bucket with another CSC project so both projects can work with the same data. Members of both projects can upload, download, copy and delete files in the shared bucket. 
    
    Use this option when multiple teams need to collaborate on a dataset. 
    
    [**Read more about the use case**](./sd-connect-share-workspace.md)



- **Share for Read-only access**
  { .csc-grid-card-info }

    ---
    
    Allow another CSC project to access data via SD Desktop only. Members of the another project can only access data in a secure and isolated computing environment for analysis. 

    Use this when you need maximum certainty that your files are not distributed further. **Note that you also have to be the project manager of the recipient project**.
    
    [**Read more about the use case**](./sd-connect-share-read-to-sd-desktop.md)

</div>


!!! warning "Assigning the wrong sharing option may grant unintended access to your data. If you are new to SD services, contact [contact CSC Service Desk](../../support/contact.md) to discuss this option before proceeding."



____




### Share buckets to another CSC project: step-by-step 


1. **Ask from recipient for their project Share ID**. They can find it in the SD Connect user interface by selecting the correct CSC project from the top-left corner and clicking **Copy Share ID **next to the project number. Ask them to send the Share ID to you by email.
![(Copy Share ID)](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SD-ConnectNew_CopyShareID.png)

2. In your own project click **Share** button on the right side of the bucket you want to share.
![Share](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SD-ConnectNew_Share1.png)

3. Paste the recipient project's **Share ID** to the field, then select suitable sharing permission, [see options](#sharing-buckets-to-another-csc-project-overview). Finally click **Share**.
![Add share ID, select permissions and Share](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SD-ConnectNew_Share2.png)

____


### Change sharing permission

1. Select correct project from the top-left corner. Click **Share** button on the right side of the bucket.
![Share](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SD-ConnectNew_Share1.png)

2. In the Share window **scroll down to This project is shared to title**. Change permission from **Permissions** dropdown on the right side of the project.
![Change permissions](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SD-ConnectNew_ShareChangePermission1.png)


3. A notification will open above the project list. **You may have to scroll up to see it.** Confirm your choise by clicking **Change Permissions** button.
![Accept](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SD-ConnectNew_ShareChangePermission2.png)

____


### Delete sharing permission

1. Select correct project from the top-left corner. Click **Share** button on the right side of the bucket.
![Share](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SD-ConnectNew_Share1.png)

2. In the Share window **scroll down to This project is shared to title**. Delete permission by clicking **Delete** button on the right side of the project.
![Change permissions](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SD-ConnectNew_ShareDeletePermission1.png)

3. A notification will open above the project list. **You may have to scroll up to see it.** Confirm your choise by clicking **Delete Permissions** button.
![Accept](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SD-ConnectNew_ShareDeletePermission2.png)


## Features in SD Connect

* [Upload](./sd-connect-upload.md)
* [Share](./sd-connect-share.md)
* [Download](./sd-connect-download.md)
* [Delete](./sd-connect-delete.md)
* [Command line interface](./sd-connect-command-line-interface.md)
* [Troubleshooting](./sd-connect-troubleshooting.md)



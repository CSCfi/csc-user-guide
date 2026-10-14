[Table of contents of user guide :material-arrow-right:](sd-services-toc.md)

# How to use folder as your shared workspace with SD Connect

<iframe width="400" height="225" srcdoc="https://www.youtube.com/embed/Ih5PKZtPOCU" title="Introducing CSC Sensitive Data Services" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


## Use case

You (Team A) and other team (Team B) are actively collaborating. You both want to upload data to the same workspace and be able to modify content.

## Solution

In this case you can share your bucket to Team B with **Collaborate** -permission. That way both teams have equal rights to modify files inside the shared bucket.

![Collaborate Infograph](https://a3s.fi/docs-files/sensitive-data/SD_Connect/UseCase_Collaborate.png)


## Step by step tutorial

Both teams should have their own CSC project and SD Connect activated. If you don't have one yet, please follow instructions from [Start here](./sd-store-and-analyze-research-data.md) and return to this tutorial after you have set up the CSC project.

1. **Ask from recipient (Team B in this use case) for their project's Share ID**. They can find it in the SD Connect user interface by selecting the correct CSC project from the top-left corner and clicking **Copy Share ID** button next to the project number. Ask them to send the Share ID to you by email.
![(Copy Share ID](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SD-ConnectNew_CopyShareID.png)

2. Log in to [SD Connect](./sd-connect-login.md).

3. Upload your data to a bucket or create an empty bucket: [See upload instructions](./sd-connect-upload.md).

4. Click **Share** button on the right side of the bucket you want to share.
![Click Share](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SD-ConnectNew_Share1.png)

5. Add the Project B’s **Share ID** to the field. Select sharing permission **Collaborate**. Finally click **Share**.
![Collaborate](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SD-ConnectNew_ShareCollaborate.png)

Now all the content of the bucket is accessible for both projects (Project A and Project B). Members in both projects can modify the content of the bucket via SD Connect; everyone can upload, download, copy and delete the content. They can also access data via SD Desktop for analysis.

## Features in SD Connect 

* [Upload](./sd-connect-upload.md)
* [Share](./sd-connect-share.md)
* [Download](./sd-connect-download.md)
* [Delete](./sd-connect-delete.md)

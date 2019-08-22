## Using Funet FileSender to share and transport files 

Funet FileSender is a browser based service for sending large files to colleagues. It is provided as an alternative to e-mail attachments but it can also be used for moving files to CSC environment. The service allows you to upload and send files up to 300 GB size and is not intended for long-term storage, as the files are deleted automatically after the preservation time is exceeded. The maximum preservation time is 21 days.

Funet FileSender is available for all Haka-enabled organisations without any additional measures. For example a CSC user account is not needed to use the service. Both sending and receiving are possible without installing any additional programs.

You can use Funet FileSender to share your files with anybody. The receiver doesn't need any authentication for downloading the file from FileSender. If you don't belong to Haka, you need a colleague who can send you an _upload voucher_. The voucher is a one-time permit to use the service for sending a file.

#### Uploading data to FileSender

First login to the service with your web browser in URL: <https://filesender.funet.fi>. You should login to the system with your Haka credentials: first select your home organization and use your local user name and password to long in (not CSC user name and password).

After this you can specify the email address of the recipient or get a sharable link instead of sending to recipients. Use the _Select files_ button to choose the files you want to send. After the temporary storage time is defined (_Expiry date_:) and the usage terms are accepted press the **Send** button to upload the files. Once the files are uploaded the recipient will get an e-mail notification.

It is possible to administer your files while they are waiting for the pick-up. Click the _My Transfers_ button to do this.

 **Funet FileSender upload page**
 ![Funet FileSender upload page](/img/funet_upload.png){.center width=100%}


#### Download data from FileSender

The recipient will get an email that contains an URL to the download page of the submitted files. The sharable link will also point to the download page. You can start the download by pressing the "_Download_" button. 

 **Funet FileSender download page**
 ![Funet FileSender download page](/img/funet_download.png){.center width=100%}

You can also right click on the download buttons and "Copy Link Location" to get the download URL to the file. The URL can then be used to download the file using another tool, for example [wget](wget.md).

```bash
wget https://filesender.funet.fi/download.php?token=4da0-b98e-3290c6471469&files_ids=36805
```

[Table of contents of user guide :material-arrow-right:](sd-services-toc.md)

# Downloading buckets and files

## On this page

* [1. Download and automated decryption](#1-download-and-automated-decryption)
* [2. Downloading bucket content](#2-downloading-bucket-content)
* [3. Downloading individual files](#3-downloading-individual-files)
* [4. Problems downloading or opening files](#4-problems-downloading-or-opening-files)


___

### 1. Download and automated decryption


<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/SMnEkcS_HJw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


Via the SD Connect user interface you can download either [the entire bucket contents](#downloading-a-bucket), folders stored in it or [individual files](#downloading-individual-files). The user interface automatically decrypts the data during the download process, so the downloaded files are ready to use.

### 1.1 Download size 

The user interface supports downloads of up to 100 GB. For larger downloads, we recommend using the command-line tools. If you need assistance, contact the CSC Service Desk at servicedesk@csc.fi.

### 1.2 Download performance

**Download performance through the user interface depends largely on your internet connection speed and network availability**. Even with a fast fiber-optic connection, Wi-Fi performance between your router and computer can limit the overall download speed. As an example, downloading a single 20 GB file takes approximately 2 hours (observed download speed 40 Mbps). As actual download times depend on network conditions, Wi-Fi performance, browser overhead and other network traffic, for large downloads we  recommend connecting your computer to the network with an Ethernet cable whenever possible. 

### 1.2 Using a work laptop

If your laptop is managed by your organization, security settings may sometimes interrupt large downloads to the default Downloads or Documents folder. To avoid this, we recommend creating a dedicated folder.



___


### 2. Downloading bucket content

1. Find the correct bucket from **All buckets** tab.

2. Click **Download** button on the right side of the bucket you want to download.

3. **Accept cookies** if needed: A pop-up window may appear at the top of your browser asking for cookie consent. The download will not start until cookies have been accepted.

4. **Wait for the download to complete**: a progress bar will show the download status. Once finished, open **Downloads** folder on your computer, where you may see two files:

    * .tar file – This is the actual file containing your downloaded bucket.
    * .tar.part file – This is a temporary file created while the .tar file is still downloading.
    * If both the .tar and .tar.part files are present, the download is still in progress. Your browser will continue downloading in the background.
    * **Do not open or extract any files** until the .tar.part file disappears and the .tar file shows a proper file size (not 0 bytes). This ensures that the download has completed successfully.

5. Files are decrypted automatically. The downloaded bucket has a .tar extension, double-click it to extract the contents into a new folder.

![SD Connect Download bucket](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SD-ConnectNew_Download.png)

___

### 3. Downloading individual files

1. Find correct bucket from **All buckets tab** and click to open it.
   
2. Click **Download** button on the right side of each file you want to download. Note that files are downloaded **one-by-one.**

3. **Accept cookies** if needed: A pop-up window may appear at the top of your browser asking for cookie consent. The download will not start until cookies have been accepted.

4. **Wait for the download to complete**: a progress bar will show the download status. Once finished, open your local download folder, where you may see two files:

    * .tar file – This is the actual file containing your downloaded file.
    * .tar.part file – This is a temporary file created while the .tar file is still downloading.
    * If both the .tar and .tar.part files are present, the download is still in progress. Your browser will continue downloading in the background.
    * **Do not open or extract any files** until the .tar.part file disappears and the .tar file shows a proper file size (not 0 bytes). This ensures that the download has completed successfully.
    
5. Files are decrypted automatically and are now ready to be used.


![SD Connect Download files](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SD-ConnectNew_DownloadFiles.png)


### 4. Problems downloading or opening files


-  If you encounter an issue while downloading files, see the **[section for common solutions and instructions on how to report the issue](./sd-connect-troubleshooting.md).**

-  **"Some downloaded files need manual decryption."** If you see this message during the download, the files were either uploaded before October 2024  or were exported via SD Desktop before October 2026 and and require an additional decryption step. Please refer to [this documentation for guidance](./manual-encryption-decryption.md).

   ![Some requested files could not be decrypted.](https://a3s.fi/docs-files/sensitive-data/SD_Connect/Old_download_1.png)


___


## Features in SD Connect

- [Upload](./sd-connect-upload.md)
- [Share](./sd-connect-share.md)
- [Download](./sd-connect-download.md)
- [Delete](./sd-connect-delete.md)
- [Command line interface](./sd-connect-command-line-interface.md)
- [Troubleshooting](./sd-connect-troubleshooting.md)





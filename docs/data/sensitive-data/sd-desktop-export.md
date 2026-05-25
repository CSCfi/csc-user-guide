[Table of contents of user guide :material-arrow-right:](sd-services-toc.md)

# Exporting data from virtual desktop via user interface

## Prerequisites
* [Create virtual desktop](sd-desktop-create.md)
* [Access virtual desktop](sd-desktop-access-vm.md)

## Only project managers can export data

The virtual desktop is isolated from the internet, so data export must be done through either via the Data Gateway application or programmatically using the Airlock client.  Only the CSC project manager can export data. The results are exported to SD Connect, where they will be available for download.

    - Files larger than 30 GB need to be split into smaller parts before exporting.



## Step by step

### Exporting multiple files

Only one file can be exported at a time. To export multiple files, first compress them into a single folder, then encrypt as a single file.

1. Create a new folder. 
2. Place all files into the folder.
3. Right-click the folder, select **Compress**. Now your folder is a .zip file.

### 1. Export files from virtual desktop

??? default "Option A: Export via Data Gateway application"

    1. Open Data Gateway application.
    2. Select SD Connect and click **Continue**.
    3. Click on **Export** tab. It is available only to the project manager.
    4. Exported file will go to SD Connect. Choose the destination folder from existing folders in SD Connect. You can also first log in to SD Connect and create a new folder for exported files.
    5. Select file you want to export and click **Export**.
    6. Files are now in the folder you selected in SD Connect.


??? default "Option B: Export programmatically via Airlock client"

    1. Open the terminal (right-click) and use the following syntax:

        ```text
        airlock-client <<username>> <<data_output_bucket>> <<filename>>
        ```

        - `username` is your CSC account username.
        - `data_output_bucket` is the name you assign to the bucket where the results will be exported. The Airlock client will create this bucket automatically within the same CSC project as your Desktop.
        - `filename` is the name of the encrypted file you wish to export.

        **Example:**

        ```text
        airlock-client cscuser analysis-2022 results-03.csv.c4gh
        ```

    2. Press **Enter** and enter your password when prompted.

    !!! Note:
        If you attempt to upload an unencrypted file, the Data Gateway apploication or Airlock client will automatically encrypt it with the Sensitive Data services public key for security reasons and export it to SD Connect. You will be able to download this file, but you will not be able to decrypt it.



### 2. Download the files from SD Connect 


1. Access SD Connect and locate the file you need. Click on Download.

!!! Note
    If you need to decrypt a large number of files, please check the tutorial [Decrypting all files in a directory](./tutorials/decrypt-directory.md).
    
### Advanced: Back-up copies

If project members need to make back-up copies from important files, the project manager can launch a back-up server process that project members can utilse to have backups. For details, see: [SD Desktop Back-up server tutorial](./tutorials/backup_sd_desktop.md).


!!! info "Support available"
    Please reach out to us at servicedesk@csc.fi (subject: SD Desktop). We will guide you through the export process in an online meeting.

## Your next steps in this guide

* [Export data programmatically](./sd-desktop-export-commandline.md)
* [Troubleshooting](./sd-desktop-troubleshooting.md)




[Table of contents of user guide :material-arrow-right:](sd-services-toc.md)

# Exporting data from virtual desktop via user interface

## Prerequisites
* [Create virtual desktop](sd-desktop-create.md)
* [Access virtual desktop](sd-desktop-access-vm.md)

## Only project managers can export data

The virtual desktop is isolated from the internet, so data export must be done through either via the Data Gateway application or the command-line version. Only the CSC project manager can export data. The results are exported to SD Connect, where they will be available for download.



## Step by step

[Option A: Export files to a bucket via Data Gateway application](#option-a-export-files-to-a-bucket-via-data-gateway-application)
[Option B: Export files to a specific folder inside a bucket via Data Gateway application](#option-b-export-files-to-a-specific-folder-inside-a-bucket-via-data-gateway-application)
[Option C: Export files programmatically via Data Gateway](#option-c-export-files-programmatically-via-data-gateway)

### Option A: Export files to a bucket via Data Gateway application

1. Open your **volume** and move all data you want to export to it. 
2. Launch **Data Gateway** by clicking icon on the left side of desktop.
    * Select SD Connect and click **Continue**. 
    * In the next view you are asked to choose a folder for accessible files. Check that **Projects** folder is selected and click **Continue**.
    * In the next view click on **Export** tab. **It is available only to the project manager.**

    ![Open export tab](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew_Export1.png)

3. Files will be be exported to **SD Connect**. Now you need to create a new bucket or use an existing one via **Bucket name** field.
    * **Create a new bucket** by writing bucket's name to the field. Follow bucket naming conventions below or via user interface.
    * **Use an existing bucket** by clicking the field and select it from the dropdown. 

    ??? default "Bucket naming conventions"

        !!! Note
            Top-level folder (bucket) name can not be modified after their creation with SD Connect. 
            These rules apply only to top-level folders created in the service, not to subfolders or files uploaded from a local computer. 

        **Top-level folder (buckets) names must**:

        * start with a lowercase letter or a number.
        * be between 3 and 63 characters long.
        * use Latin alphabets (a-z), numbers (0-9) and dash (-).
        * be unique across all existing folders in all projects in SD Connect and Allas. If you can't create a new folder, another project may already use the name you have chosen. To avoid this situation, it is good practice to include project specific identifiers (e.g., project ID number or acronym) in the folder name.
            
        **Top-level folder (buckets) names must not contain**:

        * Uppercase letters, underscore  (_) and accent letters with diacritics or special marks (åäöe') are not allowed.
        * All folder names are public; please do not include any confidential information.

4. Click **Continue**.

5. **Drag and drop** or **select** files you want to export. 
    ![Open export tab](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew_Export3.png)

6. You can see files to be exported from the list and remove them if needed.
7. Finally click **Export**. Files will be encrypted and exported to the bucket you selected in SD Connect. Please note that files can now be downloaded by all project members via SD Connect. 


    ![Open export tab](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew_Export4.png)


### Option B: Export files to a specific folder inside a bucket via Data Gateway application

??? default "Step by step"

You can also create folders inside a bucket you create or an existing bucket. 

1. When you are in **Export files to SD Connec**t window, create a new bucket or select and existing one via **Bucket name** field.
2. Then click open **Export into a folder** from bottom of the window. 

Type for example "folder1/folder2" in **Folder names** field. Your files will be exported to: "the bucket you created or selected/folder1/folder2".

    ![Export to a folder inside a bucket](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/SD-DesktopNew_Export_to_folder.png)


### Option C: Export files programmatically via Data Gateway

??? default "Step by step"

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


1. Access SD Connect and locate the files you need. Click **Download**.

!!! Note
    If you need to decrypt a large number of files, please check the tutorial [Decrypting all files in a directory](./tutorials/decrypt-directory.md).
    
### Advanced: Back-up copies

If project members need to make back-up copies from important files, the project manager can launch a back-up server process that project members can utilse to have backups. For details, see: [SD Desktop Back-up server tutorial](./tutorials/backup_sd_desktop.md).


!!! info "Support available"
    Please reach out to us at servicedesk@csc.fi (subject: SD Desktop). We will guide you through the export process in an online meeting.

## Your next steps in this guide

* [Export data programmatically](./sd-desktop-export-commandline.md)
* [Troubleshooting](./sd-desktop-troubleshooting.md)




[Table of contents of user guide :material-arrow-right:](sd-services-toc.md)

# Exporting data from virtual desktop via user interface

## Prerequisites
* [Create virtual desktop](sd-desktop-create.md)
* [Access virtual desktop](sd-desktop-access-vm.md)

## Only project managers can export data

Your virtual desktop is isolated from the internet for security reasons. Only the CSC project manager can export results or data from the secure workspace using **Data Gateway** application. The results are exported to SD Connect, where they will be available for download to your computer and can be manually decrypted.
 
!!! Note
    - Only one file can be exported at a time. To export multiple files, first compress them into a single folder. 
    - Files larger than 30 GB need to be split into smaller parts before exporting.

## Step by step

1. Download and install the Crypt4GH application
2. Generate your encryption key pair
3. Upload your public key to SD Connect
4. Import the public key inside the virtual desktop
5. Encrypt the files with your public key
6. Export the files from SD Desktop
7. Download the file from SD Connect and change extension
8. Decrypt the file with crypt4GH application
9. Advanced: Backup copies


!!! info "Support available"
    Please reach out to us at servicedesk@csc.fi (subject: SD Desktop). We will guide you through the export process in an online meeting.

## 1. Download and install the Crypt4GH application

CSC provides an application that simplifies encryption key generation and data decryption. 

1. Download the appropriate version for your operating system from the [GitHub repository](https://github.com/CSCfi/crypt4gh-gui):

    * [Mac](https://github.com/CSCfi/crypt4gh-gui/releases/download/2024.7.0/crypt4gh-gui-python3.11-macos-arm64.zip)
    * [Windows](https://github.com/CSCfi/crypt4gh-gui/releases/download/2024.7.0/crypt4gh-gui-python3.11-windows-amd64.zip)
    * [Linux](https://github.com/CSCfi/crypt4gh-gui/releases/download/2024.7.0/crypt4gh-gui-python3.11-linux-amd64.zip)


2. Locate the Crypt4GH application in your **Downloads** folder.

!!! warning
    For Windows, verify that the tool is digitally signed by CSC - IT Center for Science. If you see an error upon opening, click More info, confirm the publisher, and select Run anyway.


## 2. Generate your encryption key pair

1. Open Crypt4GH and click **Generate Keys** (top right corner).
   
2. A new window will open, prompting you to enter a password (_Private Key Passphrase_). This password will be used to secure your secret key. Please use a strong password.

![Generate keys](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Generate_keys.png)

3. Click **OK** to generate the key pair. Crypt4GH will create:
   
        * A secret key (e.g., username_crypt4gh.key)
   
        * A public key (e.g., username_crypt4gh.pub)

4. The keys will be saved in the same folder where the application resides (e.g. **Downloads** folder).
  
5. We recommend saving the key pair in a dedicated folder and renaming them descriptive names (e.g., `export_public.pub` and `export_secret.key`). Common issues arise when keys are misplaced or mismatched.

6. We recommend testing if the key pair works:

* Encrypt a test file with Crypt4gh application
    1. Load your **public** key.
    2. Select a test file.
    3. Click **Encrypt file**.

![Test encrypt](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Encrypt_test.png)

* Decrypt a test file with Crypt4gh application
    1. Load your **private key**.
    2. Select the encrypted test file.
    3. Click **Encrypt file**. 
    4. Insert password.
    5. If you encrypted test file can be opened after decrypting you know that keys work and you can proceed.

![Test decrypt](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Decrypt_test.png)
   
!!! warning
    - If you lose or forget your secret key or password, you won’t be able to decrypt your files.
    - **Do not share** your secret key or password.
    - You need to **create your keys only once** for all encryption needs, but you may generate separate keys for different projects if desired.



## 3. Upload the public key to SD Connect 

1. Log in to SD Connect.
2. Select the correct CSC project in the top left corner.
3. Click **Upload** in the top right corner.
4. In the new window, name the destination folder for your files (e.g. **project_export**).
5. Click **Select Files** to open a browser window and choose the public enycrption key  (e.g. .pub file). Click **Upload** to start automatic encryption and upload.
6. Once the upload is finished, the encryption key will be now visible from your virtual desktop.

!!! info "Folder names"

    * Folder name should start with a lowercase letter or a number.
    * Folder name should be between 3 and 63 characters long.
    * Use Latin alphabets (a-z), numbers (0-9) and dash (-). 
    * Uppercase letters, underscore  (_) and accent letters with diacritics or special marks (åäöe') are not allowed.
    * Folder names must be unique across all existing folders in all projects in SD Connect and Allas. If you can't create a new folder, another project may already use the name you have chosen. To avoid this situation, it is good practice to include projec specific identifiers (e.g., project ID number or acronym) in the folder name.
    * Remember, all bucket names are public; please do not include any confidential information.
    * Folder names can't be modified afterwards.


## 4. Import the public key inside the virtual desktop

1. [Access](./sd-desktop-access-vm.md) your virtual desktop.
2. [Access the folder](./sd-desktop-access.md#1-access-data-via-the-data-gateway-application) with the public key.
3. Use the copy/paste function to paste your public key into the virtual desktop.

## 5. Encrypt the file

### Exporting multiple files

To export multiple files, first compress them into a single folder, then encrypt as a single file.

1. Create a new folder. 
2. Place all files into the folder.
3. Right-click the folder, select **Compress**. Now your folder is a .zip file.



### Encrypt the file or folder

1. Open the terminal (right-click) and use your public key to encrypt the files you want to export. Crypt4GH is pre-installed on each virtual desktop and accessible programmatically.

    The syntax for the encryption command is:

    ```text
    crypt4gh encrypt --recipient_pk public-key < input > output
    ```

    Here:
    - `public-key` is your public key file (e.g., `your-username.pub`).
    - `input` is the file you wish to export (e.g., `my_results.csv`).
    - `output` is the encrypted file (e.g., `my_results.csv.c4gh`).

    **Example:**

    ```text
    crypt4gh encrypt --recipient_pk your-username.pub < my_results.csv > my_results.csv.c4gh
    ```

## 6. Export the encrypted files from the virtual Desktop

Once the file is encrypted, only the CSC project manager can export them via the Data Gateway application or programmatically using the Airlock client.

### Option A: Export via data Gateway application

1. Open Data Gateway application.
2. Select SD Connect and enter CSC user name and password. Click **Login** and then click **Continue**.
3. Click on **Export** tab. This is available only to project manager. 
4. Exported file will go to SD Connect. Choose the destination folder from existing folders in SD Connect. You can also first log in to SD Connect and create a new folder for exported files.
5. Select file you want to export and click **Export**.
6. Files are now in the folder you selected in SD Connect.


### Option B: Export programmatically via Airlock client

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



## 7. Download the files from SD Connect and change extension


<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/SQJ8QEKV7BE" title="Create a virtual desktop in SD Desktop" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


1. Access SD Connect and locate the file you need. Click on Download.
2. The user interface will display the message: "Some requested files could not be decrypted."
3. After downloading the file, **you need to adjust the extension**:
    * Right-click the file
    * Choose "Rename," and add `.c4gh` to the end of the filename.
    * If opened with a text editor, the files will still be encrypted.


![Some requested files could not be decrypted.](https://a3s.fi/docs-files/sensitive-data/SD_Connect/Old_download_1.png)

![After downloading the files, you need to adjust their extensions.](https://a3s.fi/docs-files/sensitive-data/SD_Connect/Old_download_2.png)

### 8. Decrypt the files with the Crypt4gh application
 
Next, you can decrypt the file using the Crypt4GH application and your secret encryption key. Unfortunately, it is currently only possible to single files and compressed folders.

1. Open the Crypt4GH application and click **Load My Private Key** (export_secret.key)
2. Click **Select File** and upload the file you want to decrypt. Click **Open**.
3. Next, click **Decrypt File**. 
4. The tool will ask you to write the secret key's password. Click **Ok**.

 ![Test decrypt](https://a3s.fi/docs-files/sensitive-data/SD_Desktop/Decrypt.png)

If your decryption runs successfully, the activity log will display the following:
      ```text
      Decrypting..... Decryption has finished Decrypted file: C:/users/username/exampledirectory/examplefile
      ```

The decrypted file will no longer display the `.c4gh` extension and will be saved in the same folder from which the original file was uploaded.

!!! Note
    In the case of decryption, adding the public key is not mandatory. Decryption will be executed anyway, but the activity log will display        the following (the decryption will be executed anyway):
      ```text
      Sender public key has not been set, authenticity will not be verified.

!!! Note
    If you need to decrypt a large number of files, please check the tutorial [Decrypting all files in a directory](./tutorials/decrypt-directory.md).
    
## Advanced: Back-up copies

If project members need to make back-up copies from important files, the project manager can launch a back-up server process that project members can utilse to have backups. For details, see: [SD Desktop Back-up server tutorial](./tutorials/backup_sd_desktop.md).

## Your next steps in this guide

* [Export data programmatically](./sd-desktop-export-commandline.md)
* [Troubleshooting](./sd-desktop-troubleshooting.md)




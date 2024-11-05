# Export Data from SD Desktop

Your virtual desktop is isolated from the internet for security reasons. Only the CSC project manager can export results or data from the secure workspace using the _Data Gateway_ application. The results are exported to SD Connect, where they will be available for download to your computer and can be manually decrypted.
 
!!! Note:
    There are two limitations when exporting data:
    * Only one file can be exported at a time. To export multiple files, first compress them into a single folder.
    * Files larger than 30 GB need to be split into smaller parts before exporting.

## Step-by-Step 

1. Download and install the Crypt4GH application
2. Generate your encryption key pair
3. Upload your public key to SD Connect
4. Import the public key inside the virtual desktop
5. Encrypt the files with your public key
6. Export the files from SD Desktop
7. Download the file from SD Connect and change extension
8. Decrypt the file with crypt4GH application
9. Advanced: Back up copies


!!! info "Need assistance?"
    If you find these steps challenging, please reach out to us at servicedesk@csc.fi (subject: SD Desktop). We will gladly guide you through the export process in an online meeting.

## Step 1: Download and install the Crypt4GH application

CSC provides an application that simplifies encryption key generation and data decryption. 

1. Download the appropriate version for your operating system from the [GitHub repository](https://github.com/CSCfi/crypt4gh-gui):

   * [Mac](https://github.com/CSCfi/crypt4gh-gui/releases/download/2024.7.0/crypt4gh-gui-python3.11-macos-arm64.zip)
     
   * [Windows](https://github.com/CSCfi/crypt4gh-gui/releases/download/2024.7.0/crypt4gh-gui-python3.11-windows-amd64.zip)
     
   * [Linux](https://github.com/CSCfi/crypt4gh-gui/releases/download/2024.7.0/crypt4gh-gui-python3.11-linux-amd64.zip)


2. Locate the Crypt4GH application in your downloads folder.

!!! Note
    For Windows, verify that the tool is digitally signed by CSC - IT Center for Science. If you see an error upon opening, click More info,        confirm the publisher, and select Run anyway.


## Step 2: Generate your encryption key pair

1. Open Crypt4GH and click Generate Keys (top right corner).
   
2. A new window will open, prompting you to enter a password (_Private Key Passphrase_). This password will be used to secure your secret key. Please use a strong password.

3. Click OK to generate the key pair. Crypt4GH will create:
   
        * A secret key (e.g., username_crypt4gh.key)
   
        * A public key (e.g., username_crypt4gh.pub)

4. The keys will be saved in the same folder where the application resides (e.g. downloads folder).
  
5. We recommend saving the key pair in a dedicated folder and  renaming them descriptive names (e.g., `export_public.pub` and `export_secret.key`). Common issues arise when keys are misplaced or mismatched.

   
!!! Note
    - If you lose or forget your secret key or password, you won’t be able to decrypt your files.
    - **Do not share** your secret key or password.
    - You need to **create your keys only once** for all encryption needs, but you may generate separate keys for different projects if desired.



## Step 3: Upload the public key to SD Connect 

1. Log in to SD Connect and select the relevant CSC project (top left corner)
   
2. Click Upload and in the new window name a destination folder (e.g., project_export).

3. Click Select Files to open a browser window and choose the public enycrption key  (e.g. .pub file).
  
5. Click Upload to start the upload. The encryption key will be now visible from yoru virtual desktop


## Step 4: Import the public key inside the virtual desktop

1 Access your virtual desktop.

2. Open the Data Gateway application, select SD Connect, enter your CSC username and password, click on open folder and access the folder with the public key. 

3. You can now import a copy of your public key inside the virtual Desktop (via copy/paste function). 



## Step 5: Encrypt the file

No technical expertise is required for this step. To export multiple files, first compress them into a single folder, then encrypt as a single file.

### Compress Files (If Needed):

1. Place all files in a folder.
   
2. Right-click the folder, select Send to > Compressed (zipped) folder.

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

## Step 6: Export the encrypted files from the virtual Desktop

Once the file is encrypted, only the CSC project manager can export them  via the Data Gateway application or programmatically using the Airlock client.

### Option A: Export via data Gateway application

1. Open the data Gateway application
   
3. Select Sd Connect, enter uesanemane a passowr. If you are CSC projectmanager, click on export

4. 


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

2. Press Enter and enter your password when prompted.

!!! Note:
    If you attempt to upload an unencrypted file, the Data Gateway apploication or Airlock client will automatically encrypt it with the Sensitive Data services public key for security reasons and export it to SD Connect. You will be able to download this file, but you will not be able to decrypt it.



## Step 7: Downlaod the files from SD Connect and change extension


6. Follow [video](https://youtu.be/SQJ8QEKV7BE) and after downloading the file, change the extension.

1. Access SD Connect and locate the file you need. Click on download.

2. The user interface will display the message: "Some requested files could not be decrypted."

3. After downloading the files, you need to adjust their extensions. Right-click the file, choose "Rename," and add `.c4gh` to the end of the filename. If opened with a text editor, the files will still be encrypted.


![Some requested files could not be decrypted.](https://a3s.fi/docs-files/sensitive-data/SD_Connect/Old_download_1.png)

![After downloading the files, you need to adjust their extensions.](https://a3s.fi/docs-files/sensitive-data/SD_Connect/Old_download_2.png)

### Step 8: Decrypt the files wiht the Crypt4gh application
 
Next, you can decrypt the file using the Crypt4GH application and your secret encryption key. Unfortunately, it is currently only possible to single files.
 
1. Open the Crypt4GH application and click on _load Your Private Key_.
   
2. Click on _Select File_ and upload the file you want to decrypt.
   
3. Click on _Open_.
   
4. Next, click on _Decrypt File_.
   
5. The tool will ask you to write the secret key's password. Press _ok_.

The secret key must match the public key used to encrypt the data.

!!! Note
    In the case of decryption, adding the public key is not mandatory, but if you have the public key of the person who has encrypted        the file, you can use it to verify the encryption signature. If you don't select a public key, the activity log will display the         following (the decryption will be executed anyway):
      ```text
      Sender public key has not been set, authenticity will not be verified.
      ```

6. If your decryption runs successfully, the activity log will display the following:
      ```text
      Decrypting..... Decryption has finished Decrypted file: C:/users/username/exampledirectory/examplefile
      ```

The decrypted file will no longer display the `.c4gh` extension and will be saved in the same folder from which the original file was uploaded.


!!! Note
    * If you need to decrypt a large number of files, please check the tutorial [Decrypting all files in a directory](tutorials/decrypt-              directory.md).
    
## Adavanced: Back up copies
    
The fact that only project manager can export data from SD Desktop makes taking back-up copies of important files difficult for project       memebers. 

If needed, the project manager can launch a back-up server process that project memebers can utilse to have backups. For details, see: [SD Desktop Back-up server tutorial](tutorials/backup_sd_desktop.md).





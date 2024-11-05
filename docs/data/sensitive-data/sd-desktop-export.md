# Export Data from SD Desktop

Your virtual desktop is isolated from the internet for security reasons. Only the CSC project manager can export results or data from the secure workspace using the _Data Gateway_ application. The results are exported to SD Connect, where they will be available for download to your computer and can be manually decrypted.

## Step-by-Step Instructions

1. Download and install the Crypt4GH application.
2. Generate your encryption key pair.
3. Upload your public key.
4. Encrypt the files.
5. Export the files.
6. Change the file extension.
7. Decrypt with Crypt4GH.
8. Advanced: Back up copies.

!!! Note:
    There are two limitations when exporting data:
    
    * Only one file can be exported at a time. To export multiple files, first compress them into a single folder.
    
    * Files larger than 30 GB cannot be exported. For larger files, split them into smaller parts before exporting.


## 1. Download and install the Crypt4GH application

CSC has developed an easy-to-use application that allows you to generate encryption keys and decrypt data when needed. Download the version for your operating system from the [GitHub repository](https://github.com/CSCfi/crypt4gh-gui):

   * [Mac](https://github.com/CSCfi/crypt4gh-gui/releases/download/v1.3.0/crypt4gh-gui-python3.10-macos-amd64.zip)
   * [Windows](https://github.com/CSCfi/crypt4gh-gui/releases/download/v1.3.0/crypt4gh-gui-python3.10-windows-amd64.zip)
   * [Linux](https://github.com/CSCfi/crypt4gh-gui/releases/download/v1.3.0/crypt4gh-gui-python3.10-linux-amd64.zip)

Ensure that the Windows tool is digitally signed by CSC - IT Center for Science. After downloading, locate the Crypt4GH application in your downloads folder.

* When opening the application for the first time, you might see an error message. In this case, click on _More info_, verify that the publisher is CSC-IT Center for Science (or in Finnish, CSC-Tieteen tietotekniikan keskus Oy), and click _Run anyway_.



## 2. Generate your encryption key pair

2.1 Open the Crypt4GH application and click on _Generate Keys_ (located in the top right corner).

2.2 A new window will open, prompting you to enter a password (_Private Key Passphrase_). This password will be used to secure your secret key. Please use a strong password.

2.3 Click _OK_, and the tool will generate a key pair consisting of a secret key (`username_crypt4gh.key`) and a public key (`username_crypt4gh.pub`).

2.4 You’ll see the file names and keys listed in the Activity Log with a message like this:

    ```
    Key pair has been generated, and your private key will be auto-loaded the next time you launch this tool:
    Private key: username_crypt4gh.key
    Public key: username_crypt4gh.pub
    All fields must be filled before file encryption can be started.
    ```

2.5 The keys will be saved in the same folder where the application resides. We recommend saving the key pair in a dedicated folder and giving them descriptive names (e.g., `export_public.pub` and `export_secret.key`). Common issues arise when keys are misplaced or mismatched, so ensure names are clear.

!!! Note
    - If you lose or forget your secret key or password, you won’t be able to decrypt your files.
    - **Do not share** your secret key or password.
    - You need to **create your keys only once** for all encryption needs, but you may generate separate keys for different projects if desired.



## 3 Upload the public key to SD Connect 

3.1 Log in to SD Connect.

3.2 Select the correct CSC project in the top left corner.

3.3 Click Upload in the top right corner.

3.4 In the new window, name the destination folder for your files (e.g. proejct_export)

3.5 Click Select Files to open a browser window and choose the public enycrption key. Click Upload to start automatic encryption and upload.


## 4  Import the public key inside the virtual desktop

4.1 Once the upload process is completed, you can access your virtual Desktop.

4.2 Using the Data Gateway application, select SD Connect and access the folder with the public key. 

4.3 You can now import a copy of your public key inside the virtual Desktop (via copy/paste function). 



## 5 Encrypt the file

No technical expertise is required for this step. 


### Preparation:  Compress multiple files into a single folder 

Only one file can be exported at a time. To export multiple files, first compress them into a single folder:

* save all teh files into a folder

* right-click on the file or folder.

* move your cursor over the “Send to” option. This will open a new submenu. Select “Compressed (zipped) folder”.

### Encrpt teh file or compressed folder

1. Open the terminal (right-click) and use your public key to encrypt the files you want to export. Crypt4GH is pre-installed on each Desktop and accessible programmatically.

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

## 6 Export the encrypted files from the virtual Desktop

Once the file is encrypted, only the CSC project manager can export them  via the Data Gateway application or programmatically using the Airlock client.

### Export via data Gateway application

1. Open the data Gateway application
   
3. Select Sd Connect, enter uesanemane a passowr. If you are CSC projectmanager, click on export

4. 


### Export programmatically via Airlock client

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

> **Note:** If you attempt to upload an unencrypted file, the Airlock client will automatically encrypt it with the Sensitive Data public key for security reasons and export it to SD Connect. You will be able to download this file, but you will not be able to decrypt it.

    The fact that only project manager can export data from SD Desktop makes taking back-up copies of important files difficult for normal users. 
    If needed, the project manager can launch a back-up server process that normal users can utilize to do backups. For details, see:

    * [SD Desktop Back-up server tutorial](tutorials/backup_sd_desktop.md)

6. Download and decrypt the files.

    The exported file is now available in SD Connect/Allas. After downloading the file in your local environment, you can decrypt it with your secret encryption key, using the Crypt4GH application or programmatically. [See this page for specific guidance](sd-connect-download-old-version.md). 

    For more information and support, write to [CSC Service Desk](../../support/contact.md) (email subject Sensitive Data).


!!! Note
   The fact that only project manager can export data from SD Desktop makes taking back-up copies of important files difficult for project memebers. If needed, the project manager can launch a back-up server process that project memebers can utilse to have backups. For details, see: [SD Desktop Back-up server tutorial].     (tutorials/backup_sd_desktop.md)


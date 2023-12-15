# Uploading and encrypting data 

Your data is automatically encrypted when you upload data to SD Connect. This is suitable for all file types and formats. More information about encryption (link)

## File size less than 100 GB

# Upload and encrypt files to a new folder

1. Log in and select the correct CSC project in the top left corner.

2. Click **Upload** in the top right corner.

3. In the new window, name the destination folder for your files. 

   !!! info "Folder names"
       
         - Folder names must be unique across all existing folders in all projects in SD Connect and Allas (the cloud storage solution based on which SD Connect is developed). If you can't create a new folder, another project may already use the name you have chosen. To avoid this situation, it is good practice to include project-specific identifiers (e.g., project ID number or acronym) in the folder name.
         - Avoid spaces and special characters; use Latin alphabets (a-z), numbers (0-9), dash (-), underscore (_), and dot (.). Remember, all folder names are public; please do not include any confidential information.
         - Folder names can't be modified afterwards.

4. Click **Select Files** to open a browser window and choose files for upload. If you want to upload folders, drag and drop them into the window. Click **Upload** to start automatic encryption and upload.

5. Notification about the status of upload will appear and be visible until the upload is completed. Notification also includes a link to the destination folder.

6. Once the upload is finished, the encrypted files are accessible for downloading and sharing via SD Connect or for analysis, editing or annotation via SD Desktop.

# Upload and encrypt files to an existing folder

1. Select the correct folder (by double-click).

2. Click **Upload** in the top right corner and follow steps from 4 to 6 in above paragraph (link).

Note

Members in the same CSC project can download and decrypt data from SD Connect. This can be limited by sharing files in read-only mode. More information about read-only mode (link)

!!! info "Additional consideration"

      - Uploading large or numerous files may take several hours depending on the internet speed. Note that upload will be automatically stopped after 8 hours.
      - SD Connect user interface visualises the destination folders where your encrypted data is stored. Think of the destination folder like a virtual box on the internet where you keep your digital files—like photos or documents.
      - You can't edit files directly in SD Connect. Editing is possible after downloading files on your laptop or by accessing the files via SD Desktop.
      - Planning how to organise your files in SD Connect  folders is a crucial step for efficient data management. Carefully consider storing the files based on projects, themes, or logical structures to enhance accessibility and streamline workflow. A well-thought-out folder structure also facilitates collaboration when sharing access with others. If you have questions or need assistance, don't hesitate to contact our service desk (servicedesk@csc.fi, subject: sensitive data).




## File size more than 100 GB

As the workflow described above is still being developed, files up to 100 GB can be encrypted with an additional step with an application called Crypt4GH. Encrypted files can then be uploaded to CSC using SD Connect (via a web browser) and directly analysed using SD Desktop. This method is suitable for any file type and format. 

!!! Note
    With this workflow, it is possible to encrypt only single files. If you have any questions or the instructions below need clarification (e.g. encryption of multiple files), don't hesitate to contact us at servicedesk@csc.fi (subject: Sensitive Data). We also provide step-by-step guidance online (e.g. via Zoom). 

1. Download the Crypt4GH encryption application specific to your operating system from the [GitHub repository](https://github.com/CSCfi/crypt4gh-gui):

      * [Mac](https://github.com/CSCfi/crypt4gh-gui/releases/download/v1.3.0/crypt4gh-gui-python3.10-macos-amd64.zip)

      * [Windows](https://github.com/CSCfi/crypt4gh-gui/releases/download/v1.3.0/crypt4gh-gui-python3.10-windows-amd64.zip)

      * [Linux](https://github.com/CSCfi/crypt4gh-gui/releases/download/v1.3.0/crypt4gh-gui-python3.10-linux-amd64.zip)

2. After downloading and unzipping the Crypt4GH application, you can find it in your downloads folder. When you open it, you might encounter an error message. In this case, click **More info** and verify that the publisher is CSC-IT Center for Science (or in Finnish CSC-Tieteen tietotekniikan keskus Oy) and click **Run anyway**.

3. Open the Crypt4GH application and click Select file button. Select the file that needs to be encrypted from the browser window and click **Open**.

4. The file name will be displayed under File to encrypt. Click **Encrypt**.

5. The Crypt4GH application will create an encrypted file in the same folder as the original file, with the extension being `.c4gh`. For example, encrypting the file `my_data1.csv` will produce a new encrypted file named `my_data.csv.c4gh`. Unfortunately, the Cryp4GH application does not provide a progress bar, and the encryption process can last up to several minutes.
[![SDConnect-cryp4ghapplication](images/connect/connect_encryption_large.png)](images/connect/connect_encryption_large.png)

8. Now you can upload the encrypted file (or a folder containing encrypted data) to SD Connect. Follow steps in above paragraph (link).


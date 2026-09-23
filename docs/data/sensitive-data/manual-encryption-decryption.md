# Manual encryption and decryption


* [2. Download and manual decryption for files uploaded before October 2024](#2-download-and-manual-decryption-for-files-uploaded-before-october-2024)


## 1. Download and manual decryption for files uploaded before October 2024


If you see the message **"Requested files could not be decrypted"** during download, the file requires an extra decryption step. After downloading, use the **Crypt4GH application** on your laptop to decrypt the file by following the provided instructions.

Please note that you can only decrypt one file at a time. If you need to decrypt multiple files at once, a command line option is available. For further assistance, [contact CSC Service Desk](../../support/contact.md).

### 1.1 Preparation

- **Have your private encryption key available.** If you don’t remember the key used, please [contact CSC Service Desk](../../support/contact.md).

- **Download the Crypt4GH graphical user interface on your laptop.** This tool is necessary for decrypting the files. If you experience any issues installing the tool, especially on a laptop provided by your IT department, please [contact us for assistance](../../support/contact.md).
- **Install the Crypt4GH application:** CSC has developed a simple application that will allow you to generate your encryption keys and decrypt data when necessary. Download the version specific to your operating system from the [GitHub repository](https://github.com/CSCfi/crypt4gh-gui): <!-- (links need to be updated) -->
      - [Mac](https://github.com/CSCfi/crypt4gh-gui/releases/download/v1.3.0/crypt4gh-gui-python3.10-macos-amd64.zip)
      - [Windows](https://github.com/CSCfi/crypt4gh-gui/releases/download/v1.3.0/crypt4gh-gui-python3.10-windows-amd64.zip)
      - [Linux](https://github.com/CSCfi/crypt4gh-gui/releases/download/v1.3.0/crypt4gh-gui-python3.10-linux-amd64.zip)

      Please check that the tool for Windows has been digitally signed by CSC - IT Center for Science. After the download, you can find the Crypt4GH application in your downloads folder. When you open the application for the first time, you might encounter an error message. In this case, click on _More info_ and verify that the publisher is CSC-IT Center for Science (or in Finnish CSC-Tieteen tietotekniikan keskus Oy) and then click on _Run anyway_.

### 1.2 Download the files from SD Connect

Access SD Connect and locate the files you need. You can download either the entire bucket or individual files. At the end of the download, the user interface will display the message: "Some downloaded files need manual decryption."
   ![Some requested files could not be decrypted.](https://a3s.fi/docs-files/sensitive-data/SD_Connect/Old_download_1.png)

### 1.3 Change the file extension

After downloading the files, you need to adjust their extensions. Right-click the file, choose "Rename," and add `.c4gh` to the end of the filename. If opened with a text editor, the files will still be encrypted.
   ![After downloading the files, you need to adjust their extensions.](https://a3s.fi/docs-files/sensitive-data/SD_Connect/Old_download_2.png)





### 1.4 Decrypt the files with the Crypt4gh application

[Video](https://youtu.be/SQJ8QEKV7BE)

Next, you can decrypt the file using the Crypt4GH application and your secret encryption key. Unfortunately, it is currently only possible to single files.

1. Open the Crypt4GH application and click on _load Your Private Key_.
2. Click on _Select File_ and upload the file you want to decrypt.
3. Click on _Open_.
4. Next, click on _Decrypt File_.
5. The tool will ask you to write the secret key's password. Press _ok_.

The secret key must match the public key used to encrypt the data.

!!! Note
    In the case of decryption, adding the public key is not mandatory, but if you have the public key of the person who has encrypted the file, you can use it to verify the encryption signature. If you don't select a public key, the activity log will display the following (the decryption will be executed anyway):

    ```text
    Sender public key has not been set, authenticity will not be verified.
    ```

If your decryption runs successfully, the activity log will display the following:

```text
Decrypting..... Decryption has finished Decrypted file: C:/users/username/exampledirectory/examplefile
```

The decrypted file will no longer display the `.c4gh` extension and will be saved in the same folder from which the original file was uploaded.

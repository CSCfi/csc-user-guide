[Table of contents of user guide](sd-services-toc.md) 

# Export data programmatically from the virtual desktop

## Background information

### Data export from SD Desktop requires manual encryption

The SD Connect update on October 2024, added automated key management to SD Desktop. This feature enambel direct uploads and downloads via SD Connect. 
However the tools that export data (e.g. results) from SD Desktop to SD Connect are not yet compatible with the automatic key management.
Instead, *the data export from SD Desktop is still a manual process requiring Crypt4GH tools and generating your own encryption key pair*.
Since SD Connect may store files encrypted using these two methods, yet with the same .c4gh extension,
  we recommend creating a dedicated folder for SD Desktop exports. This helps distinguish:

- files encrypted manually with your own encryption key pair (exported from SD Desktop).
- files automatically encrypted files by using via SD Connect, with encryption keys managed by the service.

### Only project managers can export data

Your virtual desktop is isolated from the internet for security reasons. Only the CSC project manager can export results or data from the secure workspace using **Data Gateway** 
application or the airlock command line tool (command line). The results are exported to SD Connect, where they will be available for download to your computer.
After the download, the files must still manually decrypted.
 
!!! Note
    - Only one file can be exported at a time. To export multiple files, first compress them into a single folder. 
    - Files larger than 30 GB need to be split into smaller parts before exporting.

## Step by step

In this example, we first generate your key pair (a password-protected _private key_ and a _public key_ that can be shared with collaborators). We upload the public key to 
SD Connect and import it to SD Desktop. In SD Desktop, we encrypt the files to be exported with the public key and export them to SD Connect /Allas using the airlock CLI. 
Finally we download the files form Sd Connect/Allas and decrypt them on our local environment using the correspondent secret encryption key. 

1. Download and install the Crypt4GH encryption CLI tool
2. Generate your encryption key pair
3. Upload your public key to SD Connect /Allas
4. Import the public key inside the virtual desktop
5. Encrypt the files with your public key
6. Export the files from SD Desktop via airlock
7. Download the file from SD Connect /Allas and change extension
8. Decrypt the file with crypt4GH encryption CLI tool
9. Advanced: Backup copies and support


!!! info "Support available"
    Please reach out to us at servicedesk@csc.fi (subject: SD Desktop). We will guide you through the export process in an online meeting.


## 1. Download and install the Crypt4GH encryption CLI tool

For documentation and more information, you can check the [Crypt4GH Encryption Utility](https://github.com/EGA-archive/crypt4gh.git) page.

**Python 3.6+ is required** to use the Crypt4GH encryption utility. If you need help installing Python, please follow [these instructions](https://www.python.org/downloads/release/python-3810/).

1. Install the Crypt4GH encryption CLI tool

      You can install Crypt4GH directly with pip tool:

      ```bash
      pip install crypt4gh     
      ```

      or, if you prefer the latest sources from GitHub:

      ```bash
      pip install -r crypt4gh/requirements.txt
      pip install ./crypt4gh
      ```

      or even:

      ```bash
      pip install git+https://github.com/EGA-archive/crypt4gh.git
      ```

      The usual `-h` flag shows you the different options that the tool accepts:

      ```bash
      $ crypt4gh -h

      Utility for the cryptographic GA4GH standard, reading from stdin and outputting to stdout.

      Usage:
         {PROG} [-hv] [--log <file>] encrypt [--sk <path>] --recipient_pk <path> [--recipient_pk <path>]... [--range <start-end>]
         {PROG} [-hv] [--log <file>] decrypt [--sk <path>] [--sender_pk <path>] [--range <start-end>]
         {PROG} [-hv] [--log <file>] rearrange [--sk <path>] --range <start-end>
         {PROG} [-hv] [--log <file>] reencrypt [--sk <path>] --recipient_pk <path> [--recipient_pk <path>]... [--trim]

      Options:
         -h, --help             Prints this help and exit
         -v, --version          Prints the version and exits
         --log <file>           Path to the logger file (in YML format)
         --sk <keyfile>         Curve25519-based Private key.
                              When encrypting, if neither the private key nor C4GH_SECRET_KEY are specified, we generate a new key
         --recipient_pk <path>  Recipient's Curve25519-based Public key
         --sender_pk <path>     Peer's Curve25519-based Public key to verify provenance (akin to signature)
         --range <start-end>    Byte-range either as  <start-end> or just <start> (Start included, End excluded)
         -t, --trim             Keep only header packets that you can decrypt

      Environment variables:
         C4GH_LOG         If defined, it will be used as the default logger
         C4GH_SECRET_KEY  If defined, it will be used as the default secret key (ie --sk ${C4GH_SECRET_KEY})
      ```

      You may notice that crypt4gh uses `--sk` option for the private key. This might seem odd but apparently, crypt4gh uses term _secure key_ 
      for private key, hence `sk`, and consequently `pk` refers to public key instead of the private key.



## 2. Generate your encryption key pair


      You use `crypt4gh-keygen` command to create your private and public keys:

      ```bash
      $ crypt4gh-keygen --sk mykey.sec --pk mykey.pub
      Generating public/private Crypt4GH key pair.
      Enter passphrase for mykey.sec (empty for no passphrase): 
      Enter passphrase for mykey.sec (again): 
      Your private key has been saved in mykey.sec
      Your public key has been saved in mykey.pub
      ```

      where `--sk mykey.sec` is your private (secret, sk) key and `--pk mykey.pub` is your public key (pk). 
      The tool will ask you to enter a password (passphrase) for your private key. For security reasons, the password 
      is not shown when you type it, so the tool will ask you to enter it a second time to make sure you made no typing errors 
      (or, you make the same errors twice). Please, use a strong password!

    !!! Note
        If you lose or forget your private key, or the password to it, you will be unable to decrypt the files. Do not share your private key or your password.

    !!! Note
        You need to create your keys only once and use them for all your encryption needs, but you can of course, choose to generate separate keys for encryption as you wish.


   - The keys will be saved in the same folder where the application resides (e.g. **Downloads** folder). 
   - We recommend saving the key pair in a dedicated folder and renaming them descriptive names (e.g., `export_public.pub` and `export_secret.key`). Common issues arise when keys are misplaced or mismatched.
   - We recommend testing if the key pair works by encrypting and decrypting some test file.

   
!!! warning
    - If you lose or forget your secret key or password, you won’t be able to decrypt your files.
    - **Do not share** your secret key or password.
    - You need to **create your keys only once** for all encryption needs, but you may generate separate keys for different projects if desired.



## 3. Upload the public key to SD Connect 

You can import the public encryption key by uploading it via SD Connect user interface.

1. [Log in](./sd-connect-login.md) to SD Connect user interface.
2. Select the correct CSC project in the top left corner.
3. Click **Upload** in the top right corner.
4. In the new window, name the destination folder for your files (e.g. **project_export**).
5. Click **Select Files** to open a browser window and choose the public encryption key  (e.g. .pub file). Click **Upload** to start automatic encryption and upload.
6. Once the upload is finished, the encryption key will be now visible from your virtual desktop.


## 4. Import the public key inside the virtual desktop 

1. [Access](./sd-desktop-access-vm.md) your virtual desktop.
2. Open the Data Gateway application, access the directory where the public key was stored.
3. Use the copy/paste function to paste your public key into the virtual desktop (or the terminal), it will be automatically decrypted.

## 5. Encrypt the file

### Exporting multiple files 

To export multiple files, it is often handy to first collect them first into a single folder, then pack the folder with `tar` or `zip` commands. After that you can encrypt all the data as a single file.


### Encrypt the file or folder

1. Open the terminal (right-click) and use your public key to encrypt the files you want to export. Crypt4GH is pre-installed on each virtual desktop and accessible in command line.

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

Once the file are encrypted, only the CSC project manager can export them via the _Data Gateway_ application or using the _Airlock_ command line client.

!!! Note
    The Airlock client supports exporting files up to 30 GB. Larger files or datasets must be split into smaller segments before export.

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

!!! Note
    If you attempt to upload an unencrypted file, the Data Gateway application or Airlock client will automatically encrypt it with the Sensitive Data services public key for security reasons and export it to SD Connect. You will be able to download this file, but you will not be able to decrypt it. The file is however compatible with other SD Desktop virtual machines.



## 7. Download the files from SD Connect/ Allas programmatically and decrypt them with your encryption key

You can use any Allas compatible tool or interface to download the encrypted file to your local computer.
For example with _rclone_ command line tools, the download command (once the Allas connection has been opened)
could be for example following:

```text
rclone copy allas:analysis-2022/results-03.csv.c4gh ./
```
This command copies file _results-03.csv.c4gh_ to your local computer, After this you still need do the decryption as a separate step. (see below)

If you have the CSC developed Allas commands (`a-put` and `a-get`) installed in your local computer you can combine the download  and decryption
steps into single command. This is done by defining the secret key with option `--sk`. For example:

```text
a-get --sk export_secret.key analysis-2022/results-03.csv.c4gh
```
The command above asks the password of the secret key and produces a ready-to-use decrypted file to your local computer (_results-03.csv_ in this case).



## 8. Decrypt the files with the Crypt4gh CLI tools

!!! Note
    Below is a step by step example for decrypting one file.

To decrypt a file you will need a private key which corresponds to one of the public keys used in encryption phase. Let's assume in our example that the research group A is decrypting a file you've sent them. To decrypt a file they use `crypt4gh decrypt` command:

      ```bash
      crypt4gh decrypt --sk groupA.sec <dog.jpg.c4gh >dog.jpg
      ```

      where `--sk groupA.sec` is a corresponding private key to one of the public keys used in the encryption. The `crypt4gh` command uses only 
      standard input (stdin) and standard output (stdout) so you must use shell redirections: `<` denotes an input file and `>` and denotes an output file, 
      hence `<dog.jpg.c4gh` reads in an encrypted file called `dog.jpg.c4gh` and `>dog.jpg` writes out a decrypted file named `dog.jpg`.

      The command will ask the user to enter the password (passphrase) of your private key. For security reasons the password is not displayed when you type it.

!!! Note
    In case you are decrypting the file in SD Desktop and the CSC Sensitive Data public key has been used in encryption, decryption will be done automatically, and you do not need to specify any decryption keys.

If you need to decrypt a large number of files, please check the tutorial [Decrypting all files in a directory](./tutorials/decrypt-directory.md).

[More information about data encryption](sd-connect-command-line-interface.md)

    
## Advanced: Back-up copies

If project members need to make back-up copies from important files, the project manager can launch a back-up server process that project members 
can utilse to have backups. For details, see: [SD Desktop Back-up server tutorial](./tutorials/backup_sd_desktop.md).

## More support:

To encrypt and upload files via command line, please check [this tutorial](sequencing_center_tutorial.md) illustrating how to use the crpt4gh 
tool to upload files in Allas (visible from SD Connect).

Below more information about the crypt4GH CLI:

For documentation and more information, you can check the [Crypt4GH Encryption Utility](https://github.com/EGA-archive/crypt4gh.git) page.

If you need to decrypt a large number of files, please check the tutorial [Decrypting all files in a directory](./tutorials/decrypt-directory.md).

## Your next steps in this guide

* [Troubleshooting](./sd-desktop-troubleshooting.md)
    

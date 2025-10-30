[Table of contents of user guide :material-arrow-right:](sd-services-toc.md)

# Command Line Interface and automated key management

SD Connect command line tool, **sd-lock-util**, as well as **a-put** and **a-get** commands support SD Connect compatible data upload and download with automatic encryption and decryption. After upload, the data can be edited or analysed once imported in Sd Desktop. Small files (less than 50 GB) can also be downloaded via SD Connect user inertface, which provides also automated decryption.

Note that files have been uploaded ** before February 2025**  were manually encrypted using your encryption key pair and will still need to be decrypted manually after download.

!!! Note
     All members of the same CSC project have access to upload and download files stored via SD Connect. This can be limited by sharing files with **Read to SD Desktop** permission to a diferent CSC project Academic type. Please contact servicedesk@csc.fi (suject: SD Connect) for assistance.            




- [1. Background information](#1-background-information)
- [2. Plan the number of folders needed](#2-plan-the-number-of-folders-needed)
- [3. Plan folder names](#3-plan-folder-names)
- [Command line tools and automated key management](#command-line-tools-and-automated-key-management)
- [Command line tools and manual encryption](#command-line-tools-and-manual-decryption)
- [Tutorials](#tutorials)


## 1. Background information

SD Connect is part of CSC's Sensitive Data Services, offering a free and secure data processing environment for academic research projects at Finnish universities and research institutes. SD Connect enhances the Allas object storage system by adding an automatic encryption layer, enabling secure storage of sensitive data. Data stored in SD Connect can also be accessed through SD Desktop service. While SD Connect is typically accessed via the SD Connect Web interface, command-line tools may offer a more efficient way to manage data in certain situations.

This document provides instructions on how you can install SD Connect command line tools on your local environment (Linux, Mac) and how you can use them to upload and download to and from SD Connect.

!!! Note
    Allas itself does not differentiate between data uploaded via SD Connect (user interface or command line tools) and data uploaded to Allas using different methods. Data buckets may contain a mix of SD Connect data, other encrypted data, and regular data. It is the user's responsibility to manage data types within the buckets. However, it is recommended to store SD Connect data in separate buckets and folders to avoid mixing different data types.


## 2. Plan the number of folders needed

SD Connect is built on a cloud object storage infrastructure. Files can only be uplaoded into top-level or 'main folders' creatd with SD Connect:  a top-level 'container or bucket' used to store files or folders. This has several implications for how your data should be organized and managed:

- **Once files are uploaded to SD Connect, they cannot be edited or modified**.  It is therefore important to plan the folder structure in advance. To simplify data management and avoid issues, it is recommended to create a separate folder for each dataset or experiment. Avoid placing too many files in a single folder, each folder can contain up to 500.000 segmented files.

- **Subfolders not supported**: Uploading files into subfolders is not supported.

- **Upload duration**: Uploading large datstes or large batches may take several hours. Uploads are automatically stopped after 8 hours.
  
-  **File segmentation**: Uploaded files are automatically split into segments to optimize storage and performance. This segmentation is not visible in the user interface but can affect performance. 


## 3. Plan folder names
  
When creating folders in SD Connect, specific naming rules must be followed to ensure compatibility, which requires some planning. 

!!! Note
    Top level folder name can not be modified after their creation with SD Connect. 
    These rules apply only to top-level folders created in the service, not to subfolders uploaded from a local computer. 

**Folder names must**:

* start with a lowercase letter or a number.
* be between 3 and 63 characters long.
* use Latin alphabets (a-z), numbers (0-9) and dash (-).
* be unique across all existing folders in all projects in SD Connect and Allas. If you can't create a new folder, another project may already use the name you have chosen. To avoid this situation, it is good practice to include projec specific identifiers (e.g., project ID number or acronym) in the folder name.
    
**Folder names must not contain**:

* Uppercase letters, underscore  (_) and accent letters with diacritics or special marks (åäöe') are not allowed.
* all folder names are public; please do not include any confidential information.
* Folder names can't be modified afterwards.





## Command line tools and automated key management

### Step 1: Installing a-tools and sd-lock-util on your local environment

To upload and automatically encrypt sensitive data to SD Connect using command line, you need to install the [allas-cli-utils](https://github.com/CSCfi/allas-cli-utils) and [sd-lock-util](https://github.com/CSCfi/sd-lock-util) to your laptop or local environment (Mac or Linux). The installation may require root access and for this reason, you might need support from your organization’s IT unit.

[Here you can find step-by-step instructions](https://github.com/CSCfi/allas-cli-utils) for installing `a-commands` and  `sd-lock-util` command.

!!! Note
    If you need to upload non-sensitive data (such as scripts, containers, or software for use in SD Desktop), note that these tools are also available on CSC's supercomputers (Puhti, Mahti, and LUMI). However, these systems are intended to non-sensitive data only. Sensitive data must be uploaded to SD Connect through the appropriate channels.

### Step 2: Opening connection to SD Connect

To open SD Connect compatible Allas connection you must add option `--sdc` to the configuration command. In CSC supercomputers the connection is opened with commands:

```bash
module load allas
allas-conf --sdc
```

In local installations the connection is typically opened with commands like

```bash
export PATH=/some-local-path/allas-cli-utils:$PATH
source /some-local-path/allas-cli-utils/allas_conf -u your-csc-account --sdc
```

- The set up process asks first your CSC password (Haka or Virtu passwords can't be used here). After that you will select the CSC project to be used. This is identical to the normal login process for Allas.
- In the case of SD Connect, the process has an extra step where it asks you to give the **SD Connect API token**.

To retrieve the temporary SD Connect API token:

- Login to the [SD Connect web interface](https://sd-connect.csc.fi). If you have multiple CSC projects, make sure you have selected the same SD Connect project in both the command line and the web interface (top left corner).  
- In the top right corner of the web interface, click on **Support**, then select **Create API Token** from the dropdown menu.
- In the new dialog, **enter a name** for your temporary token. Avoid using special characters in the token name.
- Click on **Create Token**. The token will be displayed only once. Once you see the token, copy it (click the icon to the left of the token). Important: make sure to store it securely, as it will not be retrievable later.

    ![API token](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SDConnect_APItoken.png)

- The token will be valid for 24 hours and will be automatically deleted after this period. Paste the token into the command line and press Enter to use it.

The SD Connect compatible Allas connection is now valid for next eight hours. And you can use commands like `a-list` and `a-delete` to manage both normal Allas objects and SD Connect objects.

### Step 3: Data upload and automated encryption

Data can be uploaded to SD Connect by using command `a-put` with option `--sdc`.
For example to upload file `my-secret-table.csv` to location `2000123-sens/dataset2` in Allas use command:

```bash
a-put --sdc my-secret-table.csv -b 2000123-sens/dataset2
```

This will produce SD Connect object: `2000123-sens/dataset2/my-secret-table.csv.c4gh`

All other a-put options and features can be used too. For example directories are
stored as `tar` files, if `--asis` option is not used.

Command:

```bash
a-put --sdc my-secret-directory -b 2000123-sens/dataset2
```

Will produce SD connect object: `2000123-sens/dataset2/my-secret-directory.tar.c4gh`

For massive data uploads, you can use **sd-lock-util lock** command. For example you could upload local
directory `dataset3` to bucket `2000123-sens` with command:

```text
sd-lock-util lock dataset3 --container 2000123-sens --progress
```

sd-lock-util does not store the directory as a tar-archive file. Instead, all files in the
directory will be stored as individual objects, named according to the location in the directory.

You can use option `--prefix` to do define a specific location inside the target bucket:

```text
sd-lock-util lock dataset3 --container 2000123-sens --prefix case-study2 --progress
```

!!! Note
    Do not use special characters or spaces in the bucket name.

!!! Note
    Since SD Connect was updated in October 2024, it is no longer straightforward to determine which encryption method was used for an encrypted .c4gh file stored in Allas/SD Connect. If you are now using a new encryption method to upload files to an existing CSC project, please ensure you add a note to your folders indicating that the encryption protocol has changed. You can either share this information with your colleagues or clearly include it in the folder name. As a good practice, we advise creating a new folder and avoiding mixing files encrypted with different methods.

### Step 4: Data download and automated decryption

Data can be downloaded from SD Connect with command `a-get`. If SD Connect connection is enabled, a-get will automatically try to decrypt objects with suffix `.c4gh`.

So for example command:

```bash
a-get 2000123-sens/dataset2/my-secret-table.csv.c4gh
```

Will produce local file: `my-secret-table.csv`

And similarly command:

```bash
a-get 2000123-sens/dataset2/my-secret-directory.tar.c4gh
```

Will produce local directory: `my-secret-directory`

For large downloads you can use `sd-lock-util unlock` command. To download an entire bucket you can use command:

```text
sd-lock-util unlock --container bucket-name --progress
```

Like in the case of upload, option `--prefix` can be used to select a subset from the bucket.
For example, to download from bucket `2000123-sens` just the object names starting with `case-study2`
you can use command:

```text
sd-lock-util unlock --container 2000123-sens --prefix case-study2 --progress
```

Note that the automatic decryption with a-get or sd-lock-util works only for the files that have
been stored using the new SD Connect that was taken in use in October 2024.

For the older SD Connect files and other Crypt4gh encrypted files you still must use a-get and
provide the matching secret key with option `--sk`

```bash
a-get --sk my-key.sec  2000123-sens/old-data/sample1.txt.c4gh
```

Unfortunately there is no easy way to know, which encryption method has been used in
a .c4gh file stored in SD Connect.

## Command line tools and manual decryption

In this Chapter we discuss how to decrypt Crypt4GH encrypted files that are not compatible with current SD Connect version.
In these cases automatic decryption does not work. Instead the data needs first to be downloaded to your local computer after which the
decryption is done with **crypt4gh** command or [Crypt4GH graphical user interface](./sd-connect-download.md#14-decrypt-the-files-with-the-crypt4gh-application).

Typical cases where this manual decryption is needed are files that have been stored to SD Connect using the old protocol and files that are exported from SD Desktop.

In these cases it is mandatory that you have access to the secret key (often called as private key) that matches the public key that was used for encrypting the data.

Only the download and decryption of files uploaded with CLI and own encryption key pair is discussed in this section. To encrypt and upload files via command line, please check [this tutorial](../sensitive-data/sequencing_center_tutorial.md) illustrating how to use the crypt4gh tool to upload files in Allas (visible from SD Connect).

### 2.1 Preparation

You can use any Allas compatible tool to download encrypted files from Allas.
Commonly used command line tools include:

- [R-clone](../Allas/using_allas/rclone.md)
- [a-tools](../Allas/using_allas/a_commands.md)

In addition to Allas compatible tool, you need [Crypt4GH Encryption Utility](https://github.com/EGA-archive/crypt4gh.git).
Crypt4GH is a written in Python. **Python 3.6+ is required**. If you need help installing Python, please follow [these instructions](https://www.python.org/downloads/release/python-3810/).

1. Install the Crypt4GH encryption CLI tool. You can install Crypt4GH directly with pip tool:

      ```bash
      pip install crypt4gh
      ```

      or, if you prefer the latest sources from GitHub:

      ```bash
      pip install -r crypt4gh/requirements.txt pip install ./crypt4gh
      ```

      or even:

      ```bash
      pip install git+https://github.com/EGA-archive/crypt4gh.git
      ```

2. The usual `-h` flag shows you the different options that the tool accepts:

      ```console
      $ crypt4gh -h
      Utility for the cryptographic GA4GH standard, reading from stdin and outputting to stdout.

      Usage:
         crypt4gh [-hv] [--log <file>] encrypt [--sk <path>] --recipient_pk <path> [--recipient_pk <path>]... [--range <start-end>] [--header <path>]
         crypt4gh [-hv] [--log <file>] decrypt [--sk <path>] [--sender_pk <path>] [--range <start-end>]
         crypt4gh [-hv] [--log <file>] rearrange [--sk <path>] --range <start-end>
         crypt4gh [-hv] [--log <file>] reencrypt [--sk <path>] --recipient_pk <path> [--recipient_pk <path>]... [--trim] [--header-only]

      Options:
         -h, --help             Prints this help and exit
         -v, --version          Prints the version and exits
         --log <file>           Path to the logger file (in YML format)
         --sk <keyfile>         Curve25519-based Private key
                              When encrypting, if neither the private key nor C4GH_SECRET_KEY are specified, we generate a new key 
         --recipient_pk <path>  Recipient's Curve25519-based Public key
         --sender_pk <path>     Peer's Curve25519-based Public key to verify provenance (akin to signature)
         --range <start-end>    Byte-range either as  <start-end> or just <start> (Start included, End excluded)
         -t, --trim             Keep only header packets that you can decrypt
         --header <path>        Where to write the header (default: stdout)
         --header-only          Whether the input data consists only of a header (default: false)

      Environment variables:
         C4GH_LOG         If defined, it will be used as the default logger
         C4GH_SECRET_KEY  If defined, it will be used as the default secret key (ie --sk ${C4GH_SECRET_KEY})
      ```

      You may notice that crypt4gh uses `--sk` option for the private key. This might seem odd but apparently, crypt4gh uses term _secure key_ for private key, hence `sk`, and consequently `pk` refers to public key instead of the private key.

### 2.2 Download and decrypt a file

To decrypt a file you will need a secret key which corresponds to one of the public keys used in encryption phase. Let's assume in our example that you are decrypting a file `dog.jpg` that you have encrypted in SD Desktop with key `groupA-pub` after which you exported the file to bucket `2000123-export`.
To retrieve the file to your local computer you a can do both download and decryption with `a-put` command.

```bash
a-get --sk groupA.sec 2000123-export/dog.jpg.c4gh
```

The command above asks the password of key file after which it downloads the data and decrypts it.

Alternatively you could use for example `rclone` to download the data:

```bash
rclone copy allas:2000123-export/dog.jpg.c4gh ./dog.jpg.c4gh
```

After that use `crypt4gh decrypt` command for decryption:

```bash
crypt4gh decrypt --sk groupA.sec <dog.jpg.c4gh >dog.jpg
```

The `crypt4gh` command uses only standard input (stdin) and standard output (stdout) so you must use shell redirections: `<` denotes an input file and `>` and denotes an output file, hence `<dog.jpg.c4gh` reads in an encrypted file called `dog.jpg.c4gh` and `>dog.jpg` writes out a decrypted file named `dog.jpg`.

The command will ask the user to enter the password (passphrase) of your secret key. For security reasons the password is not displayed when you type it.

If you need to decrypt a large number of Crypt4GH encrypted files, you can check a [tutorial that describes how all the files in a directory can be decrypted](../sensitive-data/tutorials/decrypt-directory.md)

!!! Note
    In case you are decrypting the file in SD Desktop and the CSC Sensitive Data public key has been used in encryption, decryption will be done automatically, and you do not need to specify any decryption keys. If you need to decrypt a large number of files, please check the tutorial [Decrypting all files in a directory](tutorials/decrypt-directory.md).

Additional information about [data encryption](./sd-connect-introduction-to-data-encryption.md).

## Tutorials

- [Tools for client side encryption for Allas](../Allas/allas_encryption.md)
- [Decrypting all files in a directory](../sensitive-data/tutorials/decrypt-directory.md)
- [Using Allas storage service to receive sensitive research data](../sensitive-data/sequencing_center_tutorial.md)

## Features in SD Connect

- [Upload](./sd-connect-upload.md)
- [Share](./sd-connect-share.md)
- [Download](./sd-connect-download.md)
- [Delete](./sd-connect-delete.md)
- [Troubleshooting](./sd-connect-troubleshooting.md)

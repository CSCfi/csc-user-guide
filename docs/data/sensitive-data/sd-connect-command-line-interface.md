[Table of contents of user guide :material-arrow-right:](sd-services-toc.md)

# Command Line Interface and automated key management

The new SD Connect command line tools, available from February 2025, support file upload, download (with a-commands) and automated key management (with lock-unlock) during encryption and decryption. After programmatic encryption and upload, data can be viewed through the SD Connect user interface and SD Desktop. Coding skills are required to use the tools effectively, below is a step by step guide to get started. In contrast, files have been uploaded before February 2025, were manually encrypted using your encryption key and will need to be decrypted manually after download.

- [Background information](#background-information)
- [Command line tools and automated key management](#command-line-tools-and-automated-key-management)
- [Command line tools and manual encryption](#command-line-tools-and-manual-encryption)
- [Tutorials](#tutorials)

## Background information

SD Connect is part of CSC's Sensitive Data Services, offering a free and secure data processing environment for academic research projects at Finnish universities and research institutes. SD Connect enhances the Allas object storage system by adding an automatic encryption layer, enabling secure storage of sensitive data. Data stored in SD Connect can also be accessed through SD Desktop for secure virtual desktops. While SD Connect is typically accessed via the SD Connect Web interface, command-line tools may offer a more efficient way to manage data in certain situations.

This document provides instructions on how you can install on your local environment (Linux, Mac) and how you can use the a-commands from the allas-cli-utils package to upload and download with automated key management via command line with SD Connect.

!!! Note
    Allas itself does not differentiate between data uploaded via SD Connect (user interface or commandline tools) and data uploaded to Allas using different methods. Data buckets may contain a mix of SD Connect data, other encrypted data, and regular data. It is the user's responsibility to manage data types within the buckets. However, it is recommended to store SD Connect data in separate buckets and folders to avoid mixing different data types.

## Command line tools and automated key management

### Step 1: Installing a-tools on your local environment

To upload and automatically encrypt sensitive data to SD Connect programmatically, you need to install the command-line tools, which require root access to your laptop or local environment (Mac or Linux). For this reason, you might need support from your organization’s IT unit.

[Here you can find step-by-step instructions](https://github.com/CSCfi/allas-cli-utils). This guide provides installation instructions for the a-commands (used to upload and download files) as well as the lock and unlock commands (used to automatically encrypt and decrypt files via automated key management).

!!! Note
    If you need to upload non-sensitive data (such as scripts, containers, or software for use in SD Desktop), note that these tools are also available on CSC's supercomputers (Puhti, Mahti, and Lumi). However, these systems are restricted to non-sensitive data only. Sensitive data must be uploaded to SD Connect through the appropriate channels.

### Step 2: Opening connection to SD Connect

To open SD Connect compatible Allas connection you must add option *--sdc* the configuration command. In CSC supercomputers the connection is opened with commands:

```bash
module load allas
allas-conf --sdc
```

In local installations the connection is typically opened with commands like

```bash
export PATH=/some-local-path/allas-cli-utils:$PATH
source /some-local-path/allas-cli-utils/allas_conf -u your-csc-account --sdc
```

- The set up process asks first your CSC passwords (Haka or Virtu passwords can't be used here). After that you will select the CSC project to be used. This is the normal login process for Allas.
- However, when SD Connect is enabled, the process asks you to give the *SD Connect API token*.

To retrieve the temporary SD Connect API token:

- Login to the [SD Connect web interface](https://sd-connect.csc.fi). If you have multiple CSC projects, make sure you have selected the same SD Connect project in both the command line and the web interface (top left corner).  
- In the top right corner of the web interface, click on Support, then select Select API Token from the dropdown menu.
- In the new dialog, enter a name for your temporary token. Note: Tokens are project-specific, so the name must be unique. Avoid using special characters in the name.
- Click on Create Token. The token will be displayed only once. Once you see the token, copy it (click the icon to the left of the token). Important: make sure to store it securely, as it will not be retrievable later.

    ![API token](https://a3s.fi/docs-files/sensitive-data/SD_Connect/SDConnect_APItoken.png)

- The token will be valid for 24 hours and will be automatically deleted after this period. Paste the token into the command line and press Enter to use it.

The SD Connect compatible Allas connection is now valid for next eight hours. And you can use commands like *a-list* and *a-delete* to manage both normal Allas objects and SD Connect objects.

### Step 3: Data upload and automated encryption

Data can be uploaded to SD Connect by using command *a-put* with option *--sdc*.
For example to upload file *my-secret-table.csv" to location *2000123-sens/dataset2* in Allas use command:

```bash
a-put --sdc my-secret-table.csv -b 2000123-sens/dataset2
```

This will produce SD Connect object: 2000123-sens/dataset2/my-secret-table.csv.c4gh

All other a-put options and features can be used too. For example directories are
stored as tar files, if --asis option is not used.

Command:

```bash
a-put --sdc my-secret-directory -b 2000123-sens/dataset2
```

Will produce SD connect object: 2000123-sens/dataset2/my-secret-directory.tar.c4gh

For massive data uploads, you can use *allas-dir-to-bucket* in combination with option *--sdc*.

```bash
allas-dir-to-bucket --sdc my-secret-directory  2000123-new-sens
```

The command above will copy all the files from directory my-secret-directory to bucket 2000123-new-sens in SD Connect compatible format.

!!! Note
    Do not use special characters or spaces in the folder name.

!!! Note
    Since SD Connect was updated in October 2024, it is no longer straightforward to determine which encryption method was used for an encrypted .c4gh file stored in Allas/SD Connect. If you are now using a new encryption method to upload files to an existing CSC project, please ensure you add a note to your folders indicating that the encryption protocol has changed. You can either share this information with your colleagues or clearly include it in the folder name. As a good practice, we advise creating a new folder and avoiding mixing files encrypted with different methods.

### Step 4: Data download and automated decryption

Data can be downloaded from Allas with command a-get. If SD Connect connection is enabled, a-get will automatically try to decrypt objects with suffix *.c4gh*.

So for example command:

```bash
a-get 2000123-sens/dataset2/my-secret-table.csv.c4gh
```

Will produce local file: my-secret-table.csv

And similarly command:

```bash
a-get 2000123-sens/dataset2/my-secret-directory.tar.c4gh
```

Will produce local directory: my-secret-directory

Note that this automatic decryption works only for the files that have
been stored using the new SD Connect that was taken in use in October 2024.

For the older SD Connect files and other Crypt4gh encrypted files you still must
provide the matching secret key with option *--sk*

```bash
a-get --sk my-key.sec  2000123-sens/old-date/sample1.txt.c4gh
```

Unfortunately there is no easy way to know, which encryption method has been used in
a .c4gh file stored in Allas.

## Command line tools and manual encryption

### 2.1 Preparation

Several command line tools can be used to upload encrypted files to Allas, where they will be visible from SD Connect.

Examples are:

- R-clone
- a-tools

You can find more information in [Tools for client side encryption for Allas](../Allas/allas_encryption.md)

Download and decryption of files uploaded with CLI and own encryption key pair is discussed in this section. To encrypt and upload files via command line, please check [this tutorial](../sensitive-data/tutorials/decrypt-directory.md)illustrating how to use the crypt4GH tool to upload files in Allas (visible from SD Connect). Below is also more information about the crypt4GH CLI. For documentation and more information, you can also check the [Crypt4GH Encryption Utility](https://github.com/EGA-archive/crypt4gh.git) page.

In this example, we first generate your key pair (a password-protected private key and a public key that can be shared with collaborators). Next, we encrypt a file with public keys of two different collaborators (research group A and research group B).

**Python 3.6+ is required** to use the Crypt4GH encryption utility. If you need help installing Python, please follow [these instructions](https://www.python.org/downloads/release/python-3810/).

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

      You may notice that crypt4gh uses `--sk` option for the private key. This might seem odd but apparently, crypt4gh uses term *secure key* for private key, hence `sk`, and consequently `pk` refers to public key instead of the private key.

### 2.2 Decrypt a file

To decrypt a file you will need a private key which corresponds to one of the public keys used in encryption phase. Let's assume in our example that the research group A is decrypting a file you've sent them. To decrypt a file they use `crypt4gh decrypt` command:

```bash
crypt4gh decrypt --sk groupA.sec <dog.jpg.c4gh >dog.jpg Passphrase for groupA.sec:
```

where `--sk groupA.sec` is a corresponding private key to one of the public keys used in the encryption. The `crypt4gh` command uses only standard input (stdin) and standard output (stdout) so you must use shell redirections: `<` denotes an input file and `>` and denotes an output file, hence `<dog.jpg.c4gh` reads in an encrypted file called `dog.jpg.c4gh` and `>dog.jpg` writes out a decrypted file named `dog.jpg`.

The command will ask the user to enter the password (passphrase) of your private key. For security reasons the password is not displayed when you type it.

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

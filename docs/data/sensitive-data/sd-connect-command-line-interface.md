# Command Line Interface and automated key management

The new SD Copnnect command line tools, available from January 2025, support file upload, download (with a-commands) and automated key management (with lock-unlock) during encryption and decryption. After programmatic encryption and upload, data can be viewed through the SD Connect user interface and SD Desktop. Coding skills are required to use the tools effectively, below is a step by step guide to get started.


## Background information

SD Connect is part of CSC's Sensitive Data Services, offering a free and secure data processing environment for academic research projects at Finnish universities and research institutes. SD Connect enhances the Allas object storage system by adding an automatic encryption layer, enabling secure storage of sensitive data. Data stored in SD Connect can also be accessed through SD Desktop for secure virtual desktops. While SD Connect is typically accessed via the SD Connect Web interface, command-line tools may offer a more efficient way to manage data in certain situations.

This document provides instructions on how you can install on your local enviroment (Linux, Mac) and how you can use the a-commands from the allas-cli-utils package to upload and download with automated key management via command line with SD Connect. 


Please note: Allas itself does not differentiate between data uplaoded via SD Connect (user inetrface or commandline tools) and data uplaoded to Allas using different mothods. Data buckets may contain a mix of SD Connect data, other encrypted data, and regular data. It is the user's responsibility to manage data types within the buckets. However, it is recommended to store SD Connect data in separate buckets and folders to avoid mixing different data types.


## Step1: Insalling a-toold on your local enviroment

To upload and automatically encrypt sensitive data to SD Connect programmatically, you need to install the command-line tools, which require root access to your laptop or local environment (Mac or Linux). For this reason, you might need support from your organization’s IT unit.

Here you can find step-by-step instructions: https://github.com/CSCfi/allas-cli-utils. This guide provides installation instructions for the a-commands (used to upload and download files) as well as the lock and unlock commands (used to automatically encrypt and decrypt files via automated key management).

Note !!!
     If you need to upload non-sensitive data (such as scripts, containers, or software for use in SD Desktop), note that these tools are also available on CSC's supercomputers (Puhti, Mahti,        and Lumi). However, these systems are restricted to non-sensitive data only. Sensitive data must be uploaded to SD Connect through the appropriate channels.

## Step2: Opening connection to SD Connect

To open SD Connect compatible Allas connection you must add option *--sdc* the configurtion command. In CSC supercomputers the connecton is opened with commands:

```bash
module load allas
allas-conf --sdc
```
In local installations the connection is typically opened with commands like

```bash
export PATH=/some-local-path/allas-cli-utils:$PATH
source /some-local-path/allas-cli-utils/allas_conf -u your-csc-account --sdc
```

The set up process asks first your CSC passwords (Haka or Virtu passwords can't be used here).
After that you will select the CSC project to be used. This is the normal login process for Allas.
However, when SD Connect is enabled, the process asks you to give the *SD Connect API token*. This
token must be retrieved from the [SD Connect web interface](https://sd-connect.csc.fi). Note that the tokens
are project specific. Make sure you have selected the same SD Connect project in both command line and in web 
interface.

In the web interface the token can be created using dialog that opens by selecting *Create API tokens* from the *Support* menu.

Copy the token. paste it to command line and press enter.

The SD Connect compatible Allas connection is now valid for next eight hours. And you can use commands like
*a-list* and *a-delete* to manage both normal Allas objects and SD Connect objects.


## Step3: Data upload

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
    Since SD Connect was updated in October 2024, it is no longer straightforward to determine which encryption method was used for an encrypted .c4gh file stored in Allas/SD Connect. If you        are now using a new encryption method to upload files to an existing CSC project, please ensure you add a note to your folders indicating that the encryption protocol has changed. You can       either share this information with your colleagues or clearly include it in the folder name. As a good practive, we advise creating a new folder and avoiding mixing files encrypted with different methods.

!!! Note
    Do not use special characters or spaces in the folder name.



## Step 4: Data download

Data can be downloaded form Allas with command a-get. If SD Connect connection is enabled, a-get will automatically try to decrypt objects with suffix *.c4gh*.

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

Note that this automatic decryptions works only for the files that have
been stored using the new SD Connect that was taken in use in October 2024.

For the older SD Connect files and other Crypt4gh encrypted files you still must
provide the matching secret key with option *--sk*

```bash
a-get --sk my-key.sec  2000123-sens/old-date/sample1.txt.c4gh
```

Unfortunately there is no easy way to know, which encryption method has been used in
a .c4gh file stored in Allas. 




## Features in SD Connect

* [Upload](./sd-connect-upload.md)
* [Share](./sd-connect-share.md)
* [Download](./sd-connect-download.md)
* [Download files uploaded with previous version](./sd-connect-download-old-version.md)
* [Delete](./sd-connect-delete.md)
* [Troubleshooting](./sd-connect-troubleshooting.md)

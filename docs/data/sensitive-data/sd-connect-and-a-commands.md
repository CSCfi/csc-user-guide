[Table of contents of user guide :material-arrow-right:](sd-services-toc.md)

# Using SD Connect service with a-commands

SD Connect is part of the CSC sensitive data services that provide free-of-charge sensitive data processing environment for 
academic research projects at Finnish universities and research institutes. SD Connect adds an automatic encryption layer to the Allas object storage system of CSC, so that it can be used for securely storing sensitive data. Data stored to SD Connect can also be accessed for SD Desktop secure virtual desktops. 

In most cases SD Connect is used through the [SD Connect Web interface](https://sd-connect.csc.fi), but in some cases command line tools
provide more efficient way to manage data in SD Connect.

In this document we describe how you can use use the a-commands provided by [allas-cli-utils](https://github.com/CSCfi/allas-cli-utils) to upload and download data from SD Connect. These tools are available in CSC supercomputers (Puhti, Mahti and Lumi) and they can be installed in local Linux and Mac machines too. 

Note, that Allas itself does not separate data stored with SD connect from other data stored in 
Allas. Data buckets can contain a mixture of SD Connect data, other encrypted data and normal data 
and it is up to the user to know the type of the data. However, it is probably a good idea to keep SD Connect data 
in buckets and folders that don't contain other types of data. 


## Opening connection to SD Connect

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


## Data upload

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


## Data download

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

# Command Line Interface and automated key management

The new SD Copnnect command line tools, available from January 2025, support file upload, download (a-commands) and automated key management (lock-unlock) during encryption and decryption. All data can be viewed through the SD Connect user interface and SD Desktop. Coding skills are required to use them effectively. Below is a step by step guide to get started.


## Background information

SD Connect is part of CSC's Sensitive Data Services, offering a free and secure data processing environment for academic research projects at Finnish universities and research institutes. SD Connect enhances the Allas object storage system by adding an automatic encryption layer, enabling secure storage of sensitive data. Data stored in SD Connect can also be accessed through SD Desktop for secure virtual desktops. While SD Connect is typically accessed via the SD Connect Web interface, command-line tools may offer a more efficient way to manage data in certain situations.

This document provides instructions on how you can install on your local enviroment (Linux, Mac) and how you can use the a-commands from the allas-cli-utils package to upload and download with automated key management via command line with SD Connect. 


Please note: Allas itself does not differentiate between SD Connect data and other data stored within Allas. Data buckets may contain a mix of SD Connect data, other encrypted data, and regular data. It is the user's responsibility to manage data types within the buckets. However, it is recommended to store SD Connect data in separate buckets and folders to avoid mixing different data types.


## Insalling a-toold on your local enviroment

To uplaod and automatically encrypt sensitive data to SD Connect programamrticallty, you can Installing the command-line tools requires root access to your laptop or local environment (Mac or Linux), for this reason you mgiht need support from your orgnisation's IT unit. 

Here you can find step-bystep intrcutions: https://github.com/CSCfi/allas-cli-utils, where you can find the installation instructions for a-command (used to uplaod adn downlod files) as well as the lock and unlock commands (used to automatically encrpyt and decript the files, via automated key management).

Note !!!
If you need to upload non-sensitive data (such as scripts, containers, or software for use in SD Desktop), note that these tools are also available on CSC's supercomputers (Puhti, Mahti, and Lumi). However, these systems are restricted to non-sensitive data only. Sensitive data must be uploaded to SD Connect through the appropriate channels.

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


Note !!! 
     Since SD Connect was updated in October 2024, there is no easy way to determine which encryption method has been used for an encrypted .c4gh file stored in Allas/SD Connect. If you are using a       new encryption method to upload files to an existing CSC project, please make sure to add a note to your folders indicating that the encryption protocol has changed. You can either share this        information with your colleagues or clearly include it in the folder name.


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





## New command line tools, atomated key management

Requires coding skills or command line experience, if now pleae conatct csc
They need to be insatlled in the same place where the sensitive data are. But if you want to uplaod scripts and non sensitive data you can use Puhti. 

Install the command line tools, requires yout IT unit support, root access to your laptop (local enviroment? : https://github.com/CSCfi/allas-cli-utils (lock-unlock are included there)

follow this: https://docs.csc.fi/data/sensitive-data/sd-connect-and-a-commands/




### Move text below to SD Desktop; export via command line tools.

!!! Note
    Automated key management, encryption, and decryption are not yet available for export from SD Desktop. 

To encrypt and upload files via command line, please check [this tutorial](sequencing_center_tutorial.md) illustrating how to use the crpt4GH tool to upload files in Allas (visible from SD Connect).

Below more information about the crypt4GH CLI:

For documentation and more information, you can check the [Crypt4GH Encryption Utility](https://github.com/EGA-archive/crypt4gh.git) page.

In this example, we first generate your key pair (a password-protected private key and a public key that can be shared with collaborators). Next, we encrypt a file with public keys of two different collaborators (research group A and research group B).

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

      You may notice that crypt4gh uses `--sk` option for the private key. This might seem odd but apparently, crypt4gh uses term _secure key_ for private key, hence `sk`, and consequently `pk` refers to public key instead of the private key.

2. Generate your public-private key pair

      You use `crypt4gh-keygen` command to create your private and public keys:

      ```bash
      $ crypt4gh-keygen --sk mykey.sec --pk mykey.pub
      Generating public/private Crypt4GH key pair.
      Enter passphrase for meykey.sec (empty for no passphrase): 
      Enter passphrase for mykey.sec (again): 
      Your private key has been saved in mykey.sec
      Your public key has been saved in mykey.pub
      ```

      where `--sk mykey.sec` is your private (secret, sk) key and `--pk mykey.pub` is your public key (pk). The tool will ask you to enter a password (passphrase) for your private key. For security reasons, the password is not shown when you type it, so the tool will ask you to enter it a second time to make sure you made no typing errors (or, you make the same errors twice). Please, use a strong password!

    !!! Note
        If you lose or forget your private key, or the password to it, you will be unable to decrypt the files. Do not share your private key or your password.

    !!! Note
        You need to create your keys only once and use them for all your encryption needs, but you can of course, choose to generate separate keys for encryption as you wish.

3. Encrypt a file

      To encrypt files you will need the public keys of the recipients of the data. In this example we are sharing the data with two recipients: yourself and research group A. Your own public key (`mykey.pub`) was created in the previous step, and the public key of research group A (`groupA.pub`) we have received somehow (e.g. via email). To encrypt a file you use `crypt4gh encrypt` command:

      ```bash
      crypt4gh encrypt --recipient_pk mykey.pub --recipient_pk groupA.pub <dog.jpg >dog.jpg.c4gh
      ```

      The `crypt4gh` command uses only standard input (stdin) and standard output (stdout) so you must use shell redirections: `<` denotes an input file and `>` and denotes an output file, hence `<dog.jpg` reads in a file called `dog.jpg` and `>dog.jpg.c4gh` writes out an encrypted file named `dog.jpg.c4gh`.

4. Decrypt a file

      To decrypt a file you will need a private key which corresponds to one of the public keys used in encryption phase. Let's assume in our example that the research group A is decrypting a file you've sent them. To decrypt a file they use `crypt4gh decrypt` command:

      ```bash
      crypt4gh decrypt --sk groupA.sec <dog.jpg.c4gh >dog.jpg
      Passphrase for groupA.sec: 
      ```

      where `--sk groupA.sec` is a corresponding private key to one of the public keys used in the encryption. The `crypt4gh` command uses only standard input (stdin) and standard output (stdout) so you must use shell redirections: `<` denotes an input file and `>` and denotes an output file, hence `<dog.jpg.c4gh` reads in an encrypted file called `dog.jpg.c4gh` and `>dog.jpg` writes out a decrypted file named `dog.jpg`.

      The command will ask the user to enter the password (passphrase) of your private key. For security reasons the password is not displayed when you type it.

    !!! Note
        In case you are decrypting the file in SD Desktop and the CSC Sensitive Data public key has been used in encryption, decryption will be done automatically, and you do not need to specify any decryption keys.

      If you need to decrypt a large number of files, please check the tutorial [Decrypting all files in a directory](./tutorials/decrypt-directory.md).

      [More information about data encryption](sd-connect-command-line-interface.md)

## Features in SD Connect

* [Upload](./sd-connect-upload.md)
* [Share](./sd-connect-share.md)
* [Download](./sd-connect-download.md)
* [Download files uploaded with previous version](./sd-connect-download-old-version.md)
* [Delete](./sd-connect-delete.md)
* [Command line interface](./sd-connect-command-line-interface.md)
* [Troubleshooting](./sd-connect-troubleshooting.md)

# Using Allas storage service to receive sensitive research data


Allas storage service is a general purpose data storage service maintained by CSC. 
It provides free-of-charge storage space for academic research projects at Finnish universities and research institutes. 
Allas can be used for storing any kind of research data during the active working phase of a research project. 
Allas is however not intended for data archiving. You must remove your data from Allas when the research project ends.

There is no automatic backup processes in Allas. In technical level Allas is very reliable and fault-tolerant, 
but if you, or some of your project members, remove or overwrite some data in Allas, 
it is permanently lost. Thus, you might consider making a backup copy of your data to some other location.

This document provides an example of how a research group can use Allas service to receive **sensitive data** from external 
data provider like a sequencing center. 

The steps 1 (Obtaining storage space in Allas), and 2 (Generating encryption keys) require some work, 
but they need to be done only once. Once you have the keys in place you can move directly to step 3 when you 
need to prepare a new shared bucket. 


## 1. Obtaining a storage space in Allas

If you are already using Allas service, you can skip this chapter and start from [chapter 2](#2-generating-keys-for-encrypting-sensitive-data).
Otherwise, do following steps to get access to Allas.


### Step 1.1. Create a user account

If you are not yet CSC customer, register yourself to CSC. You can do these steps in the 
CSC’s customer portal [MyCSC](https://my.csc.fi). 

Create a CSC account by logging in to MyCSC with Haka or Virtu. 


### Step 1.2. Create or join a project

In addition to CSC user account, new users must either join a CSC computing project 
or set up a new computing project. You can use the same project to access other 
CSC services too like Puhti, cPouta, or SD desktop.

Create a CSC project in MyCSC and apply access to Allas. See if you are eligible to act as a project manager. 
If your work belongs to any of the free-of-charge use cases, select 'Academic' as the project type. 
As a project manager, you can invite other users as members to your project. 

If you wish to be joined to an existing project, please ask the project manager to add your CSC user account to the 
project member list.

### Step 1.3. Add SD Connect access for your project

Add _SD Connect_ service to your project in MyCSC. Only the project manager can add services. 
After you have added SD Connect, that enables Allas too, to the project, the other project members need to login to 
MyCSC and approve the terms of use for the service before getting access to Allas anf SD Connect. 

After these steps, your project has 10 TB storage space available in Allas. 
Please [contact CSC Service Desk](../../support/contact.md) if you need more storage space. 
The data in Allas can be downloaded to your local environment or to CSC computers. 
More information about different ways to access data in Allas can be found from [Allas user guide](../Allas/index.md).


## 2. Generating keys for encrypting sensitive data

### 2.1 What are encryption keys for?

In case of sensitive research data, for example human nucleotide sequence data, 
the data needs to be properly encrypted before it can be uploaded to Allas. 
The CSC Sensitive Data Services encrypts data by default with CSC specific 
key that can be used only in the CSC environment. If you want to use your 
sensitive data in other locations too you need to create a _Crypt4GH_ compatible key pair 
consisting of _secret key_ and _public key_ for your own use. You can use the same key pair 
several times, and normally it is practical to use the same keys for all data of a project so that 
key management does not get too complicated. 

Below you can find step-by-step instructions to create encryption keys using the Cryp4GH graphical user interface or via the command line.

Once the keys have been generated, you can send the public key to all data producers, 
so that they can then encrypt the data that they will send for you. After that, only the owners 
of the private key, i.e. project members, can decrypt the data.  

The potential danger with data encryption is that if the secret key or 
its password is lost, the data can’t be decrypted by any means anymore. 
Thus, you should store the keys and password so that the information will 
be preserved also when servers and project members change. On the other hand, 
the secret key should be moved only to those places where decryption is done,
and the password should remain unreachable for non-project members.

CSC does not provide an encryption key management system at the moment. If you
don't have access to a proper key management system, one solution is to 
store the secret key and a text file containing the password to _CSC Sensitive 
Data environment_ using _SD Connect_ interface. 
The interface encrypts this data with CSC public key, after which the project members, 
and only them, can use SD Desktop service to check, what were the keys and 
passwords the project uses. 

CSC Sensitive Data environment uses _Crypt4GH_ encryption tool that allows 
encryption with several public keys. Data encrypted with this way can be 
opened with several secure keys. If you utilize sensitive data services of 
CSC it is handy to use both project's public key and CSC public key in encryption. 
This way the data can be used both in users local environment and in the 
sensitive data services of CSC.

#### Creating _crypt4gh_ compatible keys via grafical user interface


1. Generate your encryption key pair (secret key and public key) with the Crypt4GH application (you can skip this paragraph if you already have a key pair).

      * Install the Crypt4GH application:

      CSC has developed a simple application that will allow you to generate your encryption keys and decrypt data when necessary. 
      Download the version specific to your operating system from the [GitHub repository](https://github.com/CSCfi/crypt4gh-gui):

      * [Mac](https://github.com/CSCfi/crypt4gh-gui/releases/download/v1.3.0/crypt4gh-gui-python3.10-macos-amd64.zip)
      * [Windows](https://github.com/CSCfi/crypt4gh-gui/releases/download/v1.3.0/crypt4gh-gui-python3.10-windows-amd64.zip)
      * [Linux](https://github.com/CSCfi/crypt4gh-gui/releases/download/v1.3.0/crypt4gh-gui-python3.10-linux-amd64.zip)

    Please check that the tool for Windows has been digitally signed by CSC - IT Center for Science. After the download, you can find the Crypt4GH application in your downloads folder.

    * When you open the application for the first time, you might encounter an error message. In this case, click on _More info_ and verify that the publisher is CSC-IT Center for Science (or in Finnish CSC-Tieteen tietotekniikan keskus Oy) and then click on _Run anyway_.

    * Generate your encryption keys:

        - Open the Crypt4GH application and click on _Generate Keys_ (in the top right corner).
        - The tool will open a new window and ask you to insert a password (_Private Key Passphrase_). This password will be associated with your secret key. Please, use a strong password.
        - When you click on _OK_, the tool will generate a key pair consisting of a secret key (`username_crypt4gh.key`) and a public key (`username_crypt4gh.pub`).
        - The keys/file names will be displayed in the Activity Log with the following message:

            ```
            Key pair has been generated, your private key will be auto-loaded the next time you launch this tool:
            Private key: username_crypt4gh.key
            Public key: username_crypt4gh.pub
            All the fields must be filled before file encryption will be started
            ```

            The keys will be generated and saved to the same folder in which the application resides.

        !!! Note
            * If you lose or forget your secret key, or the password, you will be unable to decrypt the files.
            * Do not share your secret key or your password.
            * You need to **create your keys only once** and use them for all your encryption needs, but you can of course, choose to generate separate keys for encryption as you wish.


#### Cretating encryption keys via command line tools

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


## 3. Project key generation  

### 3.1 Generating keys

In the example below, researcher _Tiina Tutkija_ wants to use Allas to receive and store human sequence 
data that she will use in her new research project. The project is called _AniMINE_. It
will last several years, and it will include several researchers and data sources. 
Tiina Tutkija already has a customer project with Allas access at CSC.   

Now she creates and stores encryption keys for the project. Tiina has _[cryp4gh-gui](https://github.com/CSCfi/crypt4gh-gui/blob/master/README.md)_ 
encryption program installed on her laptop. She uses the _Generate Keys_ option to 
create a new key pair that is protected with password (in this case `H8koGN3lzkke`).  
The key files generated are named based on the user account of the creator 
(secret key: `ttutkija_crypt4gh.key`, public key: `ttutkija_crypt4gh.pub`). 
As the keys will be used by several members of the project, Tiina renames the key 
files accordingly: `animine_crypt4gh.key` and `animine_crypt4gh.pub`.

### 3.2 Storing keys with SD Connect

Next, Tiina Tutkija logs in to [SD Connect service](https://sd-connect.csc.fi). 
After connecting she checks that **Current project** setting refers to the CSC project 
that AniMINE project will be using. After that she clicks the **Create folder** button to 
create a new folder called `animine_keys`. Then she uses the same button to create another 
bucket called `animine_data_import_1`.

Now SD Connect contains two new empty folders. Tiina opens the folder `amimine_keys` and uses **Upload** 
button to start upload process. Then she uses **Select files** to select both key files 
to be uploaded and starts the upload process by clicking button **Upload** in the bottom of the screen.

When the upload is ready, Tiina switches back to the _All folders_ list of SD Connect and moves to the bucket `animine_data_import_1` 
She clicks the _Upload_ button again and this time uploads **ONLY**  the public key (`animine_crypt4gh.pub`) to this bucket.


Finally, she opens a simple text editor to create short instructions file about the keys. 
The content of the file, named as `animine_key_instructions.txt`, is as follows:

```text
---------------------------------------------------------------------------------------------------------
AniMINE  encryption keys created on 9.10. 2024 by project manager Tiina Tutkija.
Following key files are used to encrypt sensitive data used by AniMINE project.
Keys are used with crypt4gh encryption tool.
Public key:   animine_crypt4gh.pub
Secret key:   animine_crypt4gh.key
The password of the secret key is:  H8koGN3lzkke
Note that the secret key and password should never be given or shown to 
users that are not members of this project.

You can find a readable copy of the public key in SD Connect in location
    animine_pub/animine_crypt4gh.pub

You can freely download and send this public key to persons and organizations 
that provide data for AniMINE project. If you want to use data, that has 
been protected using this key pair, locally, please contact project manager 
Tiina Tutkija to get your own copy of the secret key and instructions for 
local decryption. Please use this document, that is readable only in the 
SD Desktop environment of this project, as the only written reference 
for the password. 

Delete the local copy of the secret key when it is no longer actively used. 
------------------------------------------------
```

She uploads this text file to the `animine_keys` folder and then deletes the file from her local computer.

Now the folder `animine_keys` contain objects:

   * `animine_crypt4gh.pub.c4gh`
   * `animine_crypt4gh.key.c4gh`
   * `animine_key_instructions.txt.c4gh`

And folder `animine_data_import_1` contains object:

   * `animine_crypt4gh.pub`

## 3.3 Sharing a folder with data producer

Next Tiina shares the animine_data_import_1 folder with the CSC project of the data producer.
For this she needs to know the project ID string of the data producer. She has already earlier requested this 32 characters long 
random string form the data producer by email. 

Do to de sharing, Tiina goes back to the all folders list and press the share icon of the animine_data_import_1 folder.
The copies the project ID to the firts field of the sharing tool and selects **Collaborate** as the sharing permission type.

Now sharing is done and Tiina sends the name of the shared bucket to the data producer by email.


### 3.4 Revoke bucket sharing after data transport

Moving large datasets (several terabytes) of data to Allas can take a long time. 
After few days, data producer tells Tiina that all data has been imported to the shared _animine_data_import_1_ folder in Allas. 
Tiina can now remove the external access rights in SD Connect interface. She klicks the _share_ icon of the _animine_data_import_1_ 
folder and press **Delete** next to the project ID of the data producer.


## 4. Using encrypted data 

The data stored to CSC using the procedure above is accessible only to the members of the research group.
The data is encrypted with both CSC public key and research group's own public key. If the data is accessed 
through [SD Desktop](https://sd-desktop.csc.fi) the decryption of data is done automatically by the _Data Gateway_ 
tool when data is used in the working environment.

If the data is used in other environments, decryption must be done by the user.

In the example above, researcher _Tiina Tutkija_ shared a data bucket `animine_data_import_1` in Allas service 
to receive data from sequencing center. The sequencing center uploaded file `run_12_R1.fastq.c4gh` to the bucket. 
Tiina can now use [SD Connect](https://sd-connect.csc.fi) to download this file to her local computer. 

However, after downloading the file is still in encrypted format. To decrypt the file Tiina opens the _[cryp4gh-gui](https://github.com/CSCfi/crypt4gh-gui/blob/master/README.md)_ encryption tool that she previously installed to her computer to create the encryption keys. 

Now she uses this tool to decrypt the data. In crypt4gh interface she first clicks _Load My Private Key_ and the selects the `animine_crypt4gh.key` that is the secret key used by her research project. Then she uses _Select File_ to select the file `run_12_R1.fastq.c4gh` she just downloaded to her computer. Next she clicks _Decrypt File_ boutton. _crypt4gh-gui_ will now
ask the password of the secret key (`H8koGN3lzkke` in this case) after which a decrypted version of the file, `run_12_R1.fastq`, is created next to the encryprted file. Tiina can now remove `run_12_R1.fastq.c4gh` from her local computer and start working with the `run_12_R1.fastq` file.

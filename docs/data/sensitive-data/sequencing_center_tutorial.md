# Using Allas storage service to receive sensitive research data


Allas storage service is a general purpose data storage service maintained by CSC. 
It provides free-of-charge storage space for academic research projects at Finnish universities and research institutes. 
Allas can be used for storing any kind of research data during the active working phase of a research project. 
Allas is however not intended for data archiving. You must remove your data from Allas when the research project ends.

There is no automatic back-up processes in Allas. In technical level Allas is very reliable and fault tolerant, 
but if you, or some of your project members, remove or overwrite some data in Allas, 
it is permanently lost. Thus you might consider to make a back up copy of your data to some other location.

This document provides an example of how a research group can use Allas service to receive **sensitive data** from external 
data provider like a sequencing center. 

The steps 1 (Obtaining storage space in Allas), and 2. (Generating encryption keys) require some work, 
but they need to be done only once. Once you have the keys in place you can move directly to step 3. when you 
need to prepare a new shared bucket. 


## 1. Obtaining a storage space in Allas

If you are already using Allas service, you can skip this chapter and start from [chapter 2](./sequencing_center_tutorial.md#2. -generating-keys-for-encrypting-sensitive-data).
Otherwise do following steps to get access to Allas.


### Step 1. Create a user account

If you are not yet CSC customer, register you self to CSC. You can do these steps in the 
CSC’s customer portal _MyCSC_ ([https://my.csc.fi](https://my.csc.fi)). 

Create a CSC account by logging in MyCSC with Haka or Virtu. 


### Step 2. Create or join a project

In addition to CSC user account, new users must either join a CSC computing project 
or set up a new computing project. You can use the same project to access other 
CSC services too like Puhti, cPouta, or SD desktop.

Create a CSC project in MyCSC to apply access to Allas.  See if you are eligible to act as a project manager. 
If your work belongs to any of the free-of-charge use cases, select 'Academic' as the project type. 
As a project manager, you can invite other users as members to your project. 

If you wish to be joined to an existing project, please ask the project manager to add your CSC user account to the 
project member list.

### Step 3. Add Allas access for your project

Add _Allas_ service to your project in MyCSC. Only the project manager can add services. 
After you have added Allas to the project, the other project members need to login to 
MyCSC and approve the the terms of use for the service before getting access to Allas. 

After these steps, your project has 10 TB storage space available in Allas. 
Please contact CSC Service Desk (servicedesk@csc.fi) if you need more storage space. 
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
several times and normally it is practical to use the same keys for all data of a project so that 
key management does not get too complicated. 

Instructions for creating a _crypt4gh_ compatible keys can be found [here](./sd_connect.md#sensitive-data-encryption-and-upload-with-multiple-encryption-keys-less-than-100-gb).
(The key generation processes are described in the second steps of graphical user 
interface and command line client instructions).
Once the keys have been generated, you can send the public key to all data producers, 
so that they can then encrypt the data that they will send for you. After that, only the owners 
of the private key, i.e. project members, can decrypt the data.  

The potential danger with data encryption is that if the the secret key or 
its’ password is lost, the data can’t be decrypeted by any means anymore. 
Thus you should store the keys and password so that the information will 
be preserved also when servers and project members change. On the other hand, 
the secret key should be moved only to those places were decryption is done 
and the password should remain unreachable for non-project members.

CSC does not provide an encryption key management system at the moment. If you
don't have a acces to a proper key management system, one solution is to 
store the secret key and a text file containing the password to _CSC Sensitive 
Data environment_ using _SD Connect_ interface. 
The interface encrypts this data with CSC public key, after which the project members, 
and only them, can use SD Desktop service to check, what were the keys and 
passwords the project uses. 

CSC Sensitive Data environment uses _Crypt4GH_ encryption tool, that allows 
encryption with several public keys.  Data encrypted with this way can be 
opened with several secure keys.  If you will utilize sensitive data services of 
CSC it is handy to use both  projects' public key and CSC public key in encryption. 
This way the data can be used both in users local environment and in the 
sensitive data services of CSC.


## 2.2 Project key generation example:

### 2.2.1 Generating keys

In the example below, researcher _Tiina Tutkija_ wants to use Allas to receive and store human sequence 
data that she will use in her new research project. The project is called _AniMINE_. It
will last several years and it will include several researchers and data sources. 
Tiina Tutkija already has a customer project with Allas access at CSC.   

Now she creates and stores encryption keys for the project. Tiina has _[cryp4gh-gui](https://github.com/CSCfi/crypt4gh-gui/blob/master/README.md)_ 
encryption program installed on her laptop. She use the _Generate Keys_ option to 
create a new key pair that is protected with password (in this case _H8koGN3lzkke_).  
The key files generated are named based on the user account of the creator 
(secret key: _ttutkija_crypt4gh.key_, public key: _ttutkija_crypt4gh.pub_ ). 
As the keys will be used by several members of the project, Tiina renames the key 
files accordingly: _animine_crypt4gh.key_ and _animine_crypt4gh.pub_.

### 2.2.2 Storing keys with SD Connect

Next Tiina Tutkija logs in [SD Connect service](https://sd-connect.csc.fi). 
After connecting she checks that **Current project** setting refers to the CSC project 
that AniMINE project will be using. After that she clicks the **Create bucket** button to 
create a new bucket called _animine_keys_. Then she uses the same button to create another 
bucket called _animine_pub_.

Now SD Connect contains two new empty buckets. Tiina opens to bucket _amimine_keys_ and uses **Upload** 
button to start upload process. In the upload page she checks that options **Encrypt files before upload** 
is **on**  (which is the default setting). Then she uses **Select files for upload** to select both key files 
to be uploaded and starts the upload process by clicking button **Encrypt and upload** in the bottom of the page.
After upload she needs to press the _reload button_ of the browser to update the state of the browser.

When the upload is ready Tiina switches back to the _Browser view_ of SD Connect and moves to the bucket _animine_pub_. 
She clicks the _upload button_ again and this time turns **off** **Encrypt files before upload** and then uploads ONLY 
the public key (_animine_crypt4gh.pub_) to this bucket.

After upload she again needs to press the reload button of the browser to update the state of the browser.

Finally she opens a simple text editor to create short instructions file about the keys. 
The content of the file, named as _animine_key_instructions.txt_, is following:

```text
---------------------------------------------------------------------------------------------------------
AniMINE  encryption keys created on 16.3. 2022 by project manager Tiina Tutkija.
Following key files are used to encrypt sensitive data used by AniMINE project.
Keys are used with crypt4gh encryption tool.
Public key:   animine_crypt4gh.pub
Secret key:   animine_crypt4gh.key
The password of the secret key is:  H8koGN3lzkke
Note that the secret key and password should never be given or shown to users that are not members of this project.

You can find a readable copy of the public key in SD Connect in location
    animine_pub/animine_crypt4gh.pub

You can freely download and send this public key to persons and organizations that provide data for AniMINE project. 
If you want to use data, that has been protected using this key pair, locally, please contact project manager 
Tiina Tutkija to get your own copy of the secret key and instructions for local decryption.
Please use this document, that is readable only in the SD Desktop environment of this project, 
as the only written reference for the password. 
Delete the local copy of the secret key when it is no longer actively used. 
------------------------------------------------
```

Next the project manager uploads this text file to the _animine_keys_ bucket with 
the default encryption option on.

Now the bucket _animine_keys_ contain objects:
   * animine_crypt4gh.pub.c4gh
   * animine_crypt4gh.key.c4gh
   * animine_key_instructions.txt.c4gh

And bucket _animine_pub_ contains object:
   * animine_crypt4gh.pub


## 3. Opening a storage bucket for importing data from data producer.

Once you have access to Allas, you can create a new data bucket there and share this bucket with the data producer. 
This approach requires that the data producer too has a project at CSC. Usually the Finnish academic data producers, 
like sequencing centers, have a CSC project. You can copy the public key of your project to the shared bucket or 
sent the public key to the data producer by some other means.

We recommend that you ask the data producer to encrypt your data with _CSC public key_ and 
with the _key of your project_. This way you can use the data both in your local secure environment 
and in CSC Sensitive Data Services.

### 3.1 Using Puhti to create a shared bucket

If you know the project number of the data producer, you can easily create a shared Allas 
bucket using _a-tools_ commands in _Puhti_. First open terminal connection to _puhti.csc.fi_ 
(use ssh, PuTTy, or terminal connection from [https://puhti.csc.fi](https://puhti.csc.fi) ).

In chapter 2.2 we had researcher Tiina Tutkija who created encryption keys and stored them to Allas. 
In her case a shared bucket could be created with following commands.

First Tiina Tutkija opens connction to Puhti. In browser , she moves to URL:
[https://puhti.csc.fi](https://puhti.csc.fi).

And logs in with her CSC account. Once the web interface of Puhti is open she opens terminal connection with tool:

**Tools/Login node shell**

This tool provides terminal connection to Puhti. In the terminal, Tiina activates connection to Allas:
```text
module load allas
allas-conf
```

Then she downloads the public key to Puhti:

```text
a-get animine_pub/animine_crypt4gh.pub
```

And upload the key to a new bucket:
```text
a-put animine_crypt4gh.pub -b animine_data_import_1
```
Then she shares this bucket with a data producer. 
The project name of data producer is in this example _project_2000111_.

```text
a-access +rw project_2000111 animine_data_import_1
```

Finally Tiina sends the name of the shared bucket to the data producer 
and ask them to encrypt the data to be uploaded with both the public key 
that they can find form the bucket and the CSC public key.

Once all data has been imported, Tiina can close remove the external access rights from the bucket with command:

```text
a-access -rw project_2000111 animine_data_import_1
```

## 4. Using encrypted data 

The data stored to CSC using the procedure above is accessible only to the members of the research group.
The data is encrypted with both CSC public key and resreach groups own public key. If the data is accessed 
through [SD Desktop](https://sd-desktop.csc.fi) the decryption of data is done automatically by the _Data Gateway_ 
tool when data is used in the working environment.

If the data is used in other environments that decryption must be done by the user.

In the example above researcher _Tiina Tutkija_ shared a data bucket _animine_data_import_1_ in Allas service 
to receive data from sequencing center. The sequencing center uploaded file _run_12_R1.fastq.c4gh_ to the bucket. 
Tiina can now use [SD Connect](https://sd-connect.csc.fi) to download this file to her local computer. However, 
after download the file  is still in ecrypted format. To decrypt the file Tiina opens the  _[cryp4gh-gui](https://github.com/CSCfi/crypt4gh-gui/blob/master/README.md)_ encryption tool that she previously installed to her computer to create 
the encryption keys. 

Now she uses this tool to decrypt the data. In crypt4gh interfave she first clicks _Load My Private Key_ and the selects the _animine_crypt4gh.key_ that is the secret key used by her research project. Then se uses _Select File_ to select the file _run_12_R1.fastq.c4gh_ she just downloaded to her computer. Next she clicks _Decryp_ boutton. _crypt4gh-gui_ will now
ask the password of the secret key (H8koGN3lzkke in this case) after which a decryted version of the file, _run_12_R1.fastq_, is created next to the encryprted file. Tiina can now remove _run_12_R1.fastq.c4gh_ from her local computer and start working with the 
_run_12_R1.fastq_ file.


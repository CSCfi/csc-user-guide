# Data encryption for SD services 

## Sensitive data needs to be encrypted before upload

According to CSC policies and [general terms of use](https://research.csc.fi/general-terms-of-use), sensitive data always 
needs to be encrypted when uploaded or stored in CSC services. Sensitive data needs to be encrypted even if, for example, 
downloaded from public repositories. The encryption requirement applies to the SD Connect service too. 
Automatic encryption during data upload has not been implemented to SD Connect yet. Because of this, at the moment, 
you must encrypt all the sensitive data on your local environment before you start to upload it to SD Connect. 
Data, that is not sensitive, can be uploaded without encryption.

## SD Connect uses Crypt4CH for encryption

The SD Connect service is designed to support sensitive data that has been encrypted with **Cryp4GH** tool in 
combination with SD Connect specific encryption key. 
Crypt4GH was originally designed to encrypt and share human genetic data according to the 
Global Alliance for Genomics and Health (GA4GH) standard, but it can be 
used to encrypt any type of data.

Crypt4GH uses **asymmetric encryption**, an encryption method that is based on two interlinked encryption keys: 

   1) a **public key**, is used for ecryption but it can't decrypt the ecrypted data. You can share your public encryption key with your collaborators 
   (e.g. multiple data owners, sequencing facilities etc), they can encrypt the data with your public key and only you will be then able to decrypt the 
   data with your own secret key. 
   
   2) a **secret key**, (private key) is used for decrypting a file that is encrypted the with the corresponding public key. This key should not be made available to other users an normally it is password protected to ensure that it remains secret. 

In the case of SD Connect, you need to encrypt your data with the **CSC Sensitive Data Services public key** so that SD Desktop will be able to use it.
When the data is downloaded from SD connect to SD Desktop the data is automatically decrypted with **CSC Sensitive Data Services secret key"**.
This key is hosted securely by the SD Services and users never needs to do the decryption them selves.
  

!!! note
Files that have been ecrypted with the _CSC Sensitive Data Services public key_, can't be used in any other services as the corresponding
secret key is available only in the SD servises environment. If you wish to encrypt your data for some other service, you should do another 
ecrypted file that uses other public keys.


## Data encryption with Crypt4GH Command Line Interface (CLI) and _CSC Sensitive Data Services public key_

Here we describe how you can use Cryp4GC for storing data so that it can be used in CSC Sensitive data services.
For more general informatin about using Crypt4GH at CSC check: 
   * [crypt4gh GIT site](https://github.com/EGA-archive/crypt4gh.git)
   * [crypt4gh exmple](./crypt4gh_client.md)
   * [crypt4gh instructions for Puhti and Allas](../Allas/allas_encryption.md)


### Step 1: Install the latest version of Crypt4GH encryption tool

**Python 3.6+ required** to use the crypt4gh encryption utility. 
To install Python: https://www.python.org/downloads/release/python-3810/

If you have a working python installation and you have permissions to add libraries to your python installation, you can install Crypt4GH with command:

```text
pip install crypt4gh
```

### Step 2: Download CSC Sensitive Data services Public key

Download CSC Sensitive Data Services public key from the link [here](./csc-sd-services.pub), or copy/paste the three lines from the box below into a new file.
The file should be saved in text-only format. Here we assume that the key file is named as _csc-sd-services.pub_.

```text
-----BEGIN CRYPT4GH PUBLIC KEY-----
dmku3fKA/wrOpWntUTkkoQvknjZDisdmSwU4oFk/on0=
-----END CRYPT4GH PUBLIC KEY-----
```

### Step 3: Encrypt a file

Cryp4GH is able to use several public keys for encryption. This can be very handy in cases were the encrypted data needs to be used by several users or services. Unfortunately SD Connect is not yet compatible with encryption with multiple keys. Because of that you must do the encryption using the CSC Sensitive Data Services public key only, if you plan to upload the data to SD Connect. In this case the syntax of the encryption command is:

```text
crypt4gh encrypt --recipient_pk public-key < input > output
```
For example

```text
crypt4gh encrypt --recipient_pk csc-sd-services.pub < my_data1.csv > my_data1.csv.c4gh
```
The encrypted file (_my_data1.csv.c4gh_) can now be uploaded to SD Connect.
 

## Data encryption and upload with Allas help tool: a-put

The [allas client utilities](https://github.com/CSCfi/allas-cli-utils/) is a set of command line tools that can be installed and used in Linux and MacOSX machines. If you have these tools, you can use data upload command _a-put_ with command line option _--sdx_ to upload data to Allas/SD Connect so that the uploded files are automatically encrypted with the CSC Sensitive Data Services public key before the upload. The public key is included to the tool so that you don't need to download your own copy of the key.

You can upload a single file with command like:

```text
a-put --sdx my_data1.csv
```
By default _a-put --sdx_ uploads the encrypted file into bukect that has name _project-number-SD_CONNECT_ . 

You can also upload complete diretories and define a specific target bucket. For exmple the command below will encrypt and upload all the files in directory _my_data_ to SD Connect into bucket _1234_SD_my_data_.
```
a-put --sdx my_data -b 1234_SD_my_data
```





 

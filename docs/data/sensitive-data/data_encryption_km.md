# Data encryption for SD services 

## Sensitive data needs to be encrypted before upload

According to CSC policies and [general terms of use](https://research.csc.fi/general-terms-of-use), sensitive data always needs to be encrypted when uploaded or stored in CSC services. Sensitive data need to be encrypted even if, for example, downloaded from public repositories. The encryption requirement applies to the SD Connect service too. Automatic encryption during data upload has not been implemented to SD-Connect yet. Beacuse of this, at the moment, you must encrypt all the sensitive data on your local environment before you start to upload it to SD Connect. Data, that is not sensitive, can be uploaded without encryption.

## SD Connect uses Crypt4CH for encryption

The SD Connect service is designed to support sensitive data that has been encrypted with **Cryp4GH** tool in combination with SD Connect specific encryption key.  Crypt4GH was originally designed to encrypt and share human genetic data according to the Global Alliance for Genomics and Health (GA4GH) file format, but it can be used to encrypt any type of data.

Crypt4GH uses **asymmetric encryption**, an encryption method that is based on two interlinked encryption keys: 

   1) a **public key**, is used for ecryption but it can't decrypt the ecrypted data. You can share your public encryption key with your collaborators (e.g. multiple data owners, sequencing facilities etc), they can encrypt the data with your public key and only you will be then able to decrypt the data with your own secret key. 
   2) a **secret key**, (private key) is used for decrypting a file that is encrypted the with the corresponding public key. This key should now be made available to other users an normally it is password protected to ensure that it remains secret. 

In the case of SD Connect, you need to encrypt your data with the **CSC Sensitive Data Services public key** so that SD Desktop will be able to use it. When the data is downloaded from SD connect to SD Desktop the data is automatically decrypted with **CSC Sensitive Data Services secret key"**. This key is hosted securely by the SD Services and users never needs to do the decryption them selves.
  

!!! note
Files that have been ecrypted with the _CSC Sensitive Data Services public key_, can't be used in any other services as the corresponding secret key is available only in the SD servises environment. If you wish to encrypt your data for some other service, you should do another ecrypted file that uses other public keys.
 


## Crypt4GH graphical user interface GUI 

### Installation

CSC developed a simple graphical user interface (GUI) that you can download to your local enviroment to using Crypt4GH with CSC Sensitive Data Services public key. 

1. You can download the user interface specific to your operating system from the [GitHub repository](https://github.com/CSCfi/crypt4gh-gui/releases):  

Links here have not yet been updated
   - [Windows](https://kannu.csc.fi/s/iDiNR5HdwtFrXCY)
   - [Mac](https://kannu.csc.fi/s/88MFCb4wNRt2mwb)
   - [Linux](https://kannu.csc.fi/s/NAgiSeS8mFXKnC4)

1. Verify, that the program has been digitally signed by CSC - IT Center for Science.  
1. After the download, you can find the Crypt4GH application in your download folder. 


![SD_Screenshot1](data/sensitive-data/images/SDEnScreenShot_1.png)
**Fugure** Crypt4GH location
 
1. When you open the application your might encounter an error message. In this case, click on _More info_ and verify that the publisher is CSC-IT Center for Science (or in Finnish CSC-Tieteen tietokniikan keskus Oy) and then click on _Run anyway_. 


  ![](img/SDEnScreenshot_2.png)

  <img width="385" alt="SDEnScreenShoot_2" src="https://user-images.githubusercontent.com/83574067/121065507-82b62700-c7d1-11eb-84ab-e6745eb76289.png">


### Usage

The usage of the Encryption tool is very simple: Pressing __Select File__ button opens a file browser that you can use to select the file that will be encrypted. When the file is selected, press the __Encrypt__ button. This encryps the selected file with the _CSC Sensitive Data Services public key_ (the key is included to the tool, you don't need to import or specify it).

Encryption creates a new encrypted file that is named by adding to the end extension *.c4gh*. For example, encrypring file _my_data1.csv_ will produce a new, encrypted file with name _my_data.csv.c4h_.  Currently,Crypt4GH application does not provid a progress bar. If the file/zipped folder contains a big dataset, the encryption process can last for up to minutes.

The ecrypted file is now ready to be uploaded to _SD Connect_.


!["cryp4sds"](img/crypt4sds.png)
**Fugure** Crypt4GH GUI

With Crypt4GH GUI it is possible to encrypt only one file at the time.

* If you need to encrypt **multiple files**, save them in one directory/folder and zip the folder (right click on the folder and click on _Send to_, next select _Compressed (zipped) folder_).

<img width="468" alt="SDEnScreenshot_5" src="https://user-images.githubusercontent.com/83574067/121065613-a0838c00-c7d1-11eb-9326-c9f36d0503fc.png">

![](img/SDEnScreenshot_5.png)


* If you need to encrypt **large datasets**, check the instructions on how to programmatically encrypt files with Crypt4GH.

 
## Data encryption with Crypt4GH Command Line Interface (CLI)

### Step 1: Install the latest version of Crypt4GH encryption tool

For documentation and more information you can check [Crypt4GH](https://github.com/EGA-archive/crypt4gh.git)
**Python 3.6+ required** to use the crypt4gh encryption utility. 
To install Python: https://www.python.org/downloads/release/python-3810/

If you have a working python installation and you have permissions to add libraries to your python istallaation, you can install Crypt4GH with command:

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

## Step 3: Encrypt a file

Cryp4GH is able to use several public keys for incryption. This can be very handy in cases were the encrypted data needs to be used by several users or services. Unfortunately SD Connect is not yet compatible with encryption with multiple keys. Because of that you must do the incryption using the CSC Sensitive Data Services public key only if you plan to upload the data to SD Connect. In this case the syntax of the encryption is:

```text
crypt4gh encrypt --recipient_pk public-key < input > output
```
For example

```text
crypt4gh encrypt --recipient_pk csc-sd-services.pub < my_data1.csv > my_data1.csv.c4gh
```
The encrypted file (_my_data1.csv.c4gh_) can now be uploaded to SD connect.
 

## Data encryption and upload with Allas help tool: a-put

The [allas client utilities](https://github.com/CSCfi/allas-cli-utils/) is a set of command line tools that can be installed and used in Linux and  MacOSX machines. If you have these tools, you can use data upload command _a-put_ with command line option _--sdx_ to upload data to Allas/SD Connect so that the uploded files are automatically encrypted with the CSC Sensitive Data Services public key before the upload. The public key is included to the tool so that you don't need to download your own copy of the key.

You can upload a single file with command like:

```text
a-put --sdx my_data1.csv
```
By default _a-put --sdx_ uploads the encrypted file into bukect that has name _project-number-SD_CONNECT_ . 

You can also upload complete diretories and define a specific target bucket. For exmple the command below will encrypt and upload all the files in directory _my_data_ to SD Connect into bucket _1234_SD_my_data_.
```
a-put --sdx my_data -b 1234_SD_my_data
```

 






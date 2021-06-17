# Data encryption for SD services 

## Sensitive data needs to be encrypted before upload

According to CSC policies and [general terms of use](https://research.csc.fi/general-terms-of-use), sensitive data always needs to be encrypted when uploaded or stored in CSC services. Sensitive data need to be encrypted even if, for example, downloaded from public repositories. The encryption requirement applies to the SD Connect service too. Automatic encryption during data upload has not been implemented to SD-Connect yet. Beacuse of this, at the moment, you must encrypt all the sensitive data on your local environment before you start to upload it to SD Connect. Data, that is not sensitive, can be uploaded without encryption.

## SD Connect uses Crypt4CH for encryption

The SD Connect service is designed to support sensitive data that has been encrypted with **Cryp4GH** tool in combination with SD Connect specific encryption key.  Crypt4GH was originally designed to encrypt and share human genetic data according to the Global Alliance for Genomics and Health (GA4GH) file format, but it can be used to encrypt any type of data.

Crypt4GH uses **asymmetric encryption**, an encryption method that is based on two interlinked encryption keys: 

   1) a **public key**, is used for ecryption but it can't decrypt the ecrypted data. You can share your public encryption key with your collaborators (e.g. multiple data owners, sequencing facilities etc), they can encrypt the data with your public key and only you will be then able to decrypt the data with your own secret key. 
   2) a **secret key**, (private key) is used for decrypting a file that is encrypted the with the corresponding public key. This key should now be made available to other users an normally it is password protected to ensure that it remains secret. 

In the case of SD Connect, you need to encrypt your data with the **CSC Sensitive Data Services public key** so that SD Desktop computing environment will be able to use it. When the data is downloaded from SD connect to SD Desktop the data is automatically decrypted with **CSC Sensitive Data Services secret key"**. This key is hosted securely by the SD Services and users never needs to do the decryption them selves.
  

!!! note
Files that have been ecrypted with the _CSC Sensitive Data Services public key_, can't be used in any other services as the corresponding secret key is available only in the SD servises environmnet. If you wish to encrypt your data for some other service, you should do another ecrypted file that uses other public keys.
 


## Crypt4GH graphical user interface GUI 

### Installation

CSC developed a simple graphical user interface (GUI) that you can download to your local enviroment to using Crypt4GH with CSC Sensitive Data Services public key. 

1. You can download the user interface specific to your operating system from the [GitHub repository](https://github.com/CSCfi/crypt4gh-gui/releases):  

Links here have not yet been updates
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

For documentation and more information you can check [Crypt4GH](https://github.com/EGA-archive/crypt4gh.git)

**Python 3.6+ required** to use the crypt4gh encryption utility. To install Python: https://www.python.org/downloads/release/python-3810/

### Step 1: Install the latest version of Crypt4GH encryption tool

CSC Sensitive Data Services public key can be dowloaded [here](), or copy/paste the CSC Sensitive Data Services public key to a new file by copying the
three lines from the box below.

```text
-----BEGIN CRYPT4GH PUBLIC KEY-----
dmku3fKA/wrOpWntUTkkoQvknjZDisdmSwU4oFk/on0=
-----END CRYPT4GH PUBLIC KEY-----
```




### Step 2: Download CSC Sensitive Data services Public key

Download or copy the CSC


```
$ crypt4gh-keygen --sk examplename.sec --pk examplename.pub
```

where:

* _ sk examplename.sec_   is your private secrete (sk) key and

* _ pk examplename.pub_ is your public key (pk).

The tool will then ask you to input your private key password. Use a strong password.

```
Passphrase for examplename.sec: 
```


## Step 3: Encrypt the file or directory

To ecrypt the files:

* Load your private or secrete key (_sk exampl-your-name.sec_)

*  your public key (_pk example-your-name.pub_) 

*  a CSC sensitive data services public key (_pk csc-sd-services.pub_) or any other recipeint public key (e.g. public key of your collaborator)

*  and load the file or directory you want to encrypt. 


In this example we are loading two recipients public keys (_pk csc-sd-services.pub_) and (_pk second-recipientexample.pub_) and encrypting a file containing a dog image ( _dog.jpg_).

```
$ crypt4gh encrypt --sk example-your-name.sec --recipient_pk csc-sd-services.pub --recipient_pk second-recipeintexample.pub < dog.jpg 
```

The tool will ask the password for your private key and next the data will be encrypted.

```
Passphrase for example-your-name.sec: 
```

The tool will visualize the following and the extension of the original file will be changed to.c4gh, underlining that the encryption was successful.

```
total 48     
-rw--rwr--r--  1 daz  staff   115B Nov  6 21:03 exanplename.pub    
-rw-r--r--  1 daz  staff   235B Nov  6 21:03 examplename.sec 
-rw-r--r--  1 daz  staff   115B Nov  6 21:03 sds.pub   
-rw-r--r--  1 daz  staff   235B Nov  6 21:03 dsd.sec 
-rw-r--r--  1 daz  staff    17B Nov  6 21:05 dog.jpg  
-rw-r--r--  1 daz  staff   169B Nov  6 21:05 dog.jpg.c4gh
```

!!! Note 
If you add the CSC Sensitive Data Service public key your data to be decrypted automatically when uploaded to SD Desktop from SD Connect. Using SDS public key will also guarantee that in case you loose your private encryption key or your password, CSC could still help you to retrieve your data.

!!!Note
Programmatically you can add more than one public key (no limit?). This could be useful in case the data are originally encrypted by a data owner or a sequencing facility using your public key.


## Step 4: Data Decryption

If you did not use SDS public key you need to decrypt the data in SD Desktop. Login into your private computing environment and first install Crypt4GH:

```
$ crypt4gh -h
```

Next input your private key (_sk exaplename.sec_) and add the file that you want to decrypt (_ < dog.jpg.c4gh >_):

```
$ crypt4gh decrypt --sk exaple-your-name.sec < dog.jpg.c4gh
```

The tool will ask you to input your private key password:

```
Passphrase for example-your-name.sec:
```

And output the decripted file: 

```
> dog.jpg
```



As an example you can check:

* a [Video](https://asciinema.org/a/mmCBfBdCFfcYCRBuTSe3kjCFs) in which Bob sends an encrypted message to Alice

1. the message is encrypoted by Bob, using is own private key and Alice public key
2. the message is then decrypted by Alice using Alice private key
  
* a [Video](https://asciinema.org/a/y23ZPc6uQ9YBkts1gPZHjvfWT) in which Me and You exchange an encrypted text file

1. the file is encrypted by Me using my private key and your public key
2. the file is then decrypted by you, using your private key



 






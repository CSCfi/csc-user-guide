# Data encryption with Crypt4GH and use of SDS public encryption key 

For data encryption we suggest the use of **Crypt4GH**, a tool originally designed to encrypt and share human genetic data according to the Global Alliance for Genomics and Health (GA4GH) file format. Crypt4GH uses asymmetric encryption.   

!!!Note
If you include SDS public key during data encryption with Crypt4GH, the dataset will be automatically decrypted when uploaded into SD Desktop your computing environment from SD Connect.

 

## Background information 

According to CSC policies and [general terms of use](https://research.csc.fi/general-terms-of-use), sensitive data always need to be encrypted when uploaded or stored in CSC services for sensitive data management. Sensitive data need to be encrypted even if, for example, downloaded from public repositories. 

There are different encryption methods available that facilitate secure data sharing or data storage: 

*  **symmetric encryption**, which uses the same encryption key for encrypting and decrypting the data or files. In this case, if you need to share sensitive data with your colleagues or collaborators, you also need to share the same encryption key for them to be able to encrypt/decrypt the files. Sharing the encryption key (e.g. via email) increases security risks. 

* **asymmetric encryption**, which uses two encryption keys. A private (or secrete) encryption key, which is password protected and  remains secrete, and a public encryption key, that can be shared publicly. If you share your public encryption key with your collaborators (e.g. multiple data owners, sequencing facilities etc), they will encrypt the data including your public key and you will be then able to decrypt the data with your own secrete private key. Moreover, if you encrypt your data with the public key from a third party (or recipient), they will be able to decrypt the data using the corresponding private key pair.  


!!! Note. Nomenclature when using the GUI and CLI:

* a **private key** is abbreviated  to **sk**  (as secrete key) in the command line tool. When you generate a private secrete key with Crypt4GH the file extension is **.sec**
* a **public key** is abbreviated to **pk** in the command line tool. When you generate a public key the file extension is **.pub**


## Crypt4GH graphical user interface **(Beginner's guide to data encryption with Crypt4GH)**

CSC developed a simple graphical user interface (GUI) that will allow you to generate encryption keys, to encrypt and decrypt data using Crypt4GH. 

You can download the user interface specific to your operating system from the [GitHub repository](https://github.com/CSCfi/crypt4gh-gui/releases):  

*  [Windows](https://kannu.csc.fi/s/iDiNR5HdwtFrXCY)

*  [Mac](https://kannu.csc.fi/s/88MFCb4wNRt2mwb)
 
*  [Linux](https://kannu.csc.fi/s/NAgiSeS8mFXKnC4)

Verify, that the program has been digitally signed by CSC - IT Center for Science.  
After the download, you can find the Crypt4GH application in your download folder. 

 ![](img/SDEnScreenshot_1.png)

When you open the application your might encounter an error message. In this case, click on _More info_ and verify that the publisher is CSC-IT Center for Science (or in Finnish CSC-Tieteen tietokniikan keskus Oy) and then click on _Run anyway_. 
 

 ![](img/SDEnScreenshot_2.png)
 
 
Next you call follow these steps:

**Step 1. Generate your encryption keys.**

1. Open the application and	click on _Generate Keys_ (on the top right corner). 
2. The tool will open a new window and ask you to add a password (_Private Key Passphrase_). This password will be associated to your private key. Set a strong password.
3. When you click on _OK_, the tool will generate a key pair: 
   - a private key (nsurname_crypt4gh.key)
   - a public key (nsurname_crypt4gh.pub)


The keys/file names will be displayed in the Activity Log with the following message:

````
Key pair has been generated, your private key will be auto-loaded the next time you will launch this tool:
Private key: name_surname.crypt4gh.key
Public key: name_surname.crypt4gh.pub
All the fields must be filled before file encryption will be started
````
 ![](img/SDEnScreenshot_3.png)
 
The keys will be generated and saved in the the same folder in which the Application was downloaded.

![](img/SDEnScreenshot_4.png)

!!! Note
If you lose or forget your private key password you will be unable to decrypt the files. 
Do not share your private key and your password. 
Do not share your private key publicly.

!!! Note: the Crypt4GH application will automatically load your private key the next time you will access it /open it. 
You don’t need to generate new key pairs each time you open the application.


**Step 2. Prepare your files.**

With Crypt4GH GUI it is possible to encrypt only one file at the time.

If you need to encrypt multiple files, save them in one directory/folder and zip the folder (right click on the folder and click on _Send to_, next select _Compressed (zipped) folder_).

If you need to encrypt large datasets, check the instructions on how to programmatically encrypt files with Crypt4GH.


![](img/SDEnScreenshot_5.png)

**Step 3. Load the encryption keys.**

1. Click on _Load My Private Key_ button.
2. Select your private key (name_surname.crypt4gh.key).
3. Click on _Open_. If the upload is successful, the tool will show the current path in title bar.
4. Next, click on _Load Their Public Key_ button and select your public key (name_surname.crypt4gh.pub) or SDS public key () if you prefer your data to be compatible with SD Desktop automated decryption
5. Click on _Open_.

![](img/SDEnScreenshot_6.png)
 
**Step 4. Upload and encrypt the file /zipped folder.**

1. Click on _Select File_ and choose the file or zipped folder that you wish to encrypt. 
2. Click on _Open_ and on _Encrypt File_. 
3. The tool will ask the password for your personal private key and once you click on _OK_ the encryption process will begin.

If the encryption is successful the file/zipped folder extension will end with *.c4gh* and  the Activity Log will display the following message:

````
Encrypting....

Encryption has finished.

Encrypted file: C:/users/samesurname/exampledirectory/examplefile.c4gh
````

Currently,Crypt4GH application is not provided with a progress bar. If the file/zipped folder contains a big dataset, the encryption process can last for up to minutes.

![](img/SDEnScreenshot_7.png)


 
 **Step 5. Data decryption.**
 
 !!! Note. If you use SDS public key during encryption, the encrypted file/zipped folder will be decrypted in an automated manner when you will import the data from SD Connect to your own personal computing environment in SD Desktop. Thus, you can skip this step.
 
 
1. Access your secure computing environment in SD Destkop. If you did not install Crypt4GH yet .........
2. Next, open Crypt4GH and click on _load Your Private Key_.  
3. Click on _Select File_ and upload the file/zipped folder you want to decrypt.
4. Click on _Open_. 
5. Next click on _Decrypt File_. 
6. The tool will ask you to write the password of the private key, press _ok_. The file will be decrypted in the same location as the original file. 

If you don't select a public key, the activity log will display the following (the decryption will be executed anyway):

_Sender public key has not been set, authenticity will not be verified._

If your decryption runs successfully, the activity log will display the following:

````
Decrypting.....

Decryption has finished

Decrypted file: C:/users/samesurname/exampledirectory/examplefile
````


![](img/SDEnScreenshot_8.png)


 
## Crypt4GH Command Line Interface (CLI)

For documentation and more information you can check [Crypt4GH](https://github.com/EGA-archive/crypt4gh.git)
 
 **Step 1. Install the latest version of Crypt4GH encryption tool. ** 
 
 Choose one of the following options. Python 3.6+ required to use the crypt4gh encryption utility.
 
````
$ crypt4gh -h      
````
or if you prefer the latest sources from GitHub:

```
pip install -r crypt4gh/requirements.txt
pip install ./crypt4gh
```

or

```
pip install git+https://github.com/EGA-archive/crypt4gh.git
```

The usual -h flag shows you the different options that the tool accepts:

```
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


**Step 2. Generate a permanent public-private keypair**

```
$ crypt4gh-keygen --sk examplename.sec --pk examplename.pub
```
where _ sk examplename.sec_ is your private secrete (sk) key and _ pk examplename.pub_ is your public key (pk).

The tool will then ask you to input your private key password. Use a strong password.
```
Passphrase for examplename.sec: 
```


**Step 3. Encrypt the file or directory**

Load your private or secrete key (_sk examplename.sec_), your public key (_pk examplename.pub_) or a recipient public key and load the file or directory you want to encrypt. 
In this example we are loading two recipients public keys (_pk sds.pub_) and (_pk secondrecipientexample.pub_) and encrypting a file containing a dog image ( _dog.jpg_).

```
$ crypt4gh encrypt --sk examplename.sec --recipient_pk sds.pub --recipient_pk secondrecipeintexample.pub < dog.jpg 
```

The tool will ask the password for your private key and next the data will be encrypted.

```
Passphrase for bob.sec: 
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
If you add the SDS public key your data to be decrypted automatically when uploaded to SD Desktop from SD Connect. Using SDS public key will also guarantee that in case you loose your private encryption key or your password, CSC could still help you to retrieve your data.

!!!Note
Programmatically you can add more than one public key (no limit?). This could be useful in case the data are originally encrypted by a data owner or a sequencing facility using your public key.


**Step 4. Data Decryption**

If you did not use SDS public key you need to decrypt the data in SD Desktop. Login into your private computing environment and first install Crypt4GH:

```
$ crypt4gh -h
```

Next input your private key (_sk exaplename.sec_) and add the file that you want to decrypt (_ < dog.jpg.c4gh >_):

```
$ crypt4gh decrypt --sk exaplename.sec < dog.jpg.c4gh
```

The tool will ask you to input your private key password:

```
Passphrase for alice.sec:
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


## Errors:

add here possible erros?



Notes:
encryption with CLI requires to zip a folder also?
how do they install crypt4CH in SD Desktop? DO they need to install phyton first?
where do they find the data?
where do they find the sds public key and how to we call it?
video with data woner or seq facility or multiple data owners

 
 
 
 






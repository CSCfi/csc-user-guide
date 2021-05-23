# Data encryption with Crypt4GH and use of SDS public encryption key 

For data encryption we suggest the use of **Crypt4GH**, a tool originally designed to encrypt and share human genetic data according to the Global Alliance for Genomics and Health (GA4GH) file format. Crypt4GH uses asymmetric encryption.   

!!!Note
If you include SDS public key during data encryption with Crypt4GH, the dataset will be automatically decrypted when uploaded into SD Desktop your computing enviroment from SD Connect.

 

## Background information 

According to CSC policies and [general terms of use](https://research.csc.fi/general-terms-of-use), sensitive data always need to be encrypted when uploaded or stored in CSC services for sensitive data management. Sensitive data need to be encrypted even if, for example, downloaded from public repositories. 

There are different encryption methods available that facilitate secure data sharing or data storage: 

*  **symmetric encryption**, which uses the same encryption key for encrypting and decrypting the data or files. In this case, if you need to share sensitive data with your collogues or collaborators, you also need to share the same encryption key for them to be able to encrypt/decrypt the files. Sharing the encryption key (e.g. via email) increases security risks. 

* **asymmetric encryption**, which uses two encryption keys. A private encryption key, which is password protected and  remains secrete, and a public encryption key, that can be shared publicly. If you share your public encryption key with your collaborators (e.g. multiple data owners, sequencing facilities etc), they will encrypt the data including your public key and you will be then able to decrypt the data with your own secrete private key. Moreover, if you encrypt your data with the public key from a third party, he/she will be able to decrypt the data using the corresponding private key pair.  



## Crypt4GH graphical user interface 

CSC developed a simple graphical user interface (GUI) that will allow you to generate encryption keys, to encrypt and decrypt data using Crypt4GH. 

You can download the user interface specific to your operating system from the [GitHub repository](https://github.com/CSCfi/crypt4gh-gui/releases):  

*  [Windows](https://kannu.csc.fi/s/iDiNR5HdwtFrXCY)

*  [Mac](https://kannu.csc.fi/s/88MFCb4wNRt2mwb)
 
*  [Linux](https://kannu.csc.fi/s/NAgiSeS8mFXKnC4)

Verify, that the program has been digitally signed by CSC - IT Center for Science.  
After the download, you can find the Crypt4GH application in your download folder. 

SDD_Screenshot1

When you open the application your might encounter an error message. In this case, click on more info and verify that the publisher is CSC-IT Center for Science (or in Finnish CSC-Tieteen tietokniikan keskus Oy) and then click on _Run anyway_. 
 
 SDD_Screeshot2_3
 
 
Next you call follow these steps:

**Step1, Generate your encryption keys.**

Open the application and	click on _Generate Keys_ (on the top right corner). The tool will open a new window and ask you to add a password (_Private Key Passphrase_). This password will be associated to your private key. Set a strong password.

When you click on _OK_, the tool will generate a key pair: 
- a private key (nsurname_crypt4gh.key)
- a public key (nsurname_crypt4gh.pub)

 SDD_Screeshot4_5

The keys/file names will be displayed in the Activity Log with the following message:

_Key pair has been generated, your private key will be auto-loaded the next time you will launch this tool:
Private key: name_surname.crypt4gh.key
Public key: name_surname.crypt4gh.pub
All the fields must be filled before file encryption will be started_

The keys will be generated and saved in the the same folder in which the Application was downloaded.

SDD_Screeshot6_7

!!! Note
If you loose or forget the password you will be unable to decrypt the files. 
Do not share your private key and your password. 
Do not share your private key publicly.

!!! Note: the Crypt4GH application will automatically load your private key the next time you will access it /open it. 
You don’t need to generate new key pairs each time you open the application.


**Step2. Prepare your datsets and files.**

With Crypt4GH GUI is possible to encrypt only one file at the time.
If youneed to encrypt multiple file, save them in one directoty/folder and zip the folder (right click on the folder and click on _send to_, next select _compressed (zippped) folder_.
If you need to encrpyt large datasets, checl the intructions for progammatically encrypt files with Crypt4GH.

**Step2. Load the ecryption keys.**

Click on _Load my private key_ button and select your private key (name_surname.crypt4gh.key) and then click on _Open_ 
If the upload is successful, the tool will show the current path in title bar.
Next, click on _Load thir public key_ button and select your public key (name_surname.crypt4gh.pub) or SDS public key () if you prefer your data to be compatible ith SD Desktop atuomated decryption and then click on _Open_.
If the upload is successful, the tool will show the current path in title bar.

SDD_Screeshot7_8
 
**Step3. Upload and encrypt the the file /zipped folder.**

Next click on _Select file_ and choose the file or zipped folder that you wish to encrypt. Click on _Open_ and on _Encrypt file_. The tool will ask the password for your personal private key and once you click on _OK_ then the encryption process will begin.

If the ecryption is sucessful the file/zipped folder extention will change to *.c4gh* and  the activity Log display the following message:

_Encrypting....

Encryption has finished.

Encrypted file: C:/users/samesurname/exampledirectory/examplefile.c4gh_

Currently,Crypt4GH application is not provided with a progress bar. If the file/zipped folder contains a big dataset, the encryption process can last for up to minutes.

SDD_Screeshot8_9


 
 **Step4. Data decryption.**
 
 
Access your secure computing environment in SD Destkop. You can find the encrypted data in your home directory.

Next, open Crypt4GH, Load the private key. Select the file you want to decrypt and click on _Open_. Next click on _decrypt file_
Next you need to write the password of the private key, press _ok_
The file is decrypted in the same location of the original file. 

 
 
 
 ## Crypt4GH Command Line tool (CLI)
 
 **Step1. Install the latest version of Crypt4GH encryption tool. ** with

$ pip install https://github.com/EGA-archive/crypt4gh.git

**Step2.Generats a permanent public-private keypair**

$ crypt4gh-keygen --sk example.sec --pk example.pub


**Step3 Encrypt the data**

$ crypt4gh encrypt --sk example.sec --recipient_pk sds.pub --recipient_pk csc.pub < dog.jpg > dog.jpg.c4gh


**Step4. Data Decryption*:

$ crypt4gh decrypt --sk researcher.sec < dog.jpg.c4gh > dog-decrypted-researcher.jpg




 
 
 
 






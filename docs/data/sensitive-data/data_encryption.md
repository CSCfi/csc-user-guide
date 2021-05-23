# Data encryption with Crypt4GH and use of SDS public encryption key 

For data encryption we suggest the use of **Crypt4GH**, a tool originally designed to encrypt and share human genetic data according to the Global Alliance for Genomics and Health (GA4GH) file format. Crypt4GH uses asymmetric encryption.   

!!!Note
If you include SDS public key during data encryption with Crypt4GH, the dataset will be automatically decrypted when uploaded into SD Desktop your computing enviroment from SD Connect.

 

## Background information 

According to CSC policies and [general terms of use](https://research.csc.fi/general-terms-of-use), sensitive data always need to be encrypted when uploaded or stored in CSC services for sensitive data management. Sensitive data need to be encrypted even if, for example, downloaded from public repositories. 

There are different encryption methods available that facilitate secure data sharing or data storage: 

1._symmetric encryption_, which uses the same encryption key for encrypting and decrypting the data or files. In this case, if you need to share sensitive data with your collogues or collaborators, you also need to share the same encryption key for them to be able to encrypt/decrypt the files. Sharing the encryption key (e.g. via email) increases security risks. 

1._asymmetric encryption_, which uses two encryption keys. A private encryption key, which remains secrete and protected, and a public encryption key, that can be shared publicly. If you share your public encryption key with your collaborators (e.g. multiple data owners, sequencing facilities etc), they will encrypt the data including your public key and you will be then able to decrypt the data with your own secrete private key. Moreover, if you encrypt your data with the public key from a third party, he/she will be able to decrypt the data using the corresponding private key pair.  

 

 

## Crypt4GH graphical user interface 

CSC developed a simple graphical user interface (GUI) that will allow you to generate encryption keys, to encrypt and decrypt data using Crypt4GH. 

**Step1** You can download the user interface specific to your operating system from the [GitHub repository](https://github.com/CSCfi/crypt4gh-gui/releases):  

*For [Windows](https://kannu.csc.fi/s/iDiNR5HdwtFrXCY)

*For [Mac](https://kannu.csc.fi/s/88MFCb4wNRt2mwb)

*For [Linux](https://kannu.csc.fi/s/NAgiSeS8mFXKnC4)

Verify, that the program has been digitally signed by CSC - IT Center for Science.  
After the download, you can find the Crypt4GH application in your download folder. 

**SDD_Screenshot1**

 When you open the application your might encounter an error message. In this case, click on more info and verify that the publisher is CSC-IT Center for Science (or in Finnish CSC-Tieteen tietokniikan keskus Oy) and then click on Run anyway. 
 
 **SDD_Screeshot2_3**
 
 
Next you call follow these steps:

**Step1**	Open the application and	click on _Generate Keys_ (on the top right corner). The tool will open a new window and ask you to add a password (_Private Key Passphrase_). This password will be associated to your private key. Set a strong password.

When you click on _OK_, the tool will generate a key pair: 
- a private key (nsurname_crypt4gh.key)
- a public key (nsurname_crypt4gh.pub)

 **SDD_Screeshot4_5**

The keys/file names will be displayed in the Activity Log and saved in the the same folder in which the Application was downloaded.

 **SDD_Screeshot6**

!!! Note
If you loose or forget the password you will be unable to decrypt the files. 
Do not share your private key and your password. 








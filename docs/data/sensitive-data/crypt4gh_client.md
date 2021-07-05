
# Data encryption with own permanet encryption key pair

## Sensitive data needs to be encrypted before upload

According to CSC policies and [general terms of use](https://research.csc.fi/general-terms-of-use), sensitive data always 
needs to be encrypted when uploaded or stored in CSC services. Sensitive data needs to be encrypted even if, for example, 
downloaded from public repositories. The encryption requirement applies to the SD Connect service too. 
Automatic encryption during data upload has not been implemented to SD Connect yet. Because of this, at the moment, 
you must encrypt all the sensitive data on your local environment before you start to upload it to SD Connect. 
Data, that is not sensitive, can be uploaded without encryption.

##  Crypt4CGH based encryption

Crypt4GH was originally designed to encrypt and share human genetic data according to the 
Global Alliance for Genomics and Health (GA4GH) standard, but it can be 
used to encrypt any type of data.

Crypt4GH uses **asymmetric encryption**, an encryption method that is based on two interlinked encryption keys: 

   1) a **public key**, is used for encryption but it can't decrypt the encrypted data. You can share your public encryption key with your collaborators 
   (e.g. multiple data owners, sequencing facilities etc), they can encrypt the data with your public key and only you will be then able to decrypt the 
   data with your own secret key. 
   
   2) a **secret key**, (private key) is used for decrypting a file that is encrypted the with the corresponding public key. This key should not be made available to other users an normally it is password protected to ensure that it remains secret. 


**When using CSC Sensitive Data Services for analyzing sensitive data you have two possibilities:**

1) you can encrypt the data with the workflow described ealier in the SD Connect guide. With this workflow, you will encrypt a copy of your data using CSC Sensitive Data public encryption key (using the Crypt4GH user inetrfaces or programmatically). In this way, when you will import the data to SD Desktop, they will be decripted  in an automated manner in your own private computing enviroment.  The data are automatically decrypted with **CSC Sensitive Data Services secret key"**.
This key is hosted securely by the SD Services and users never needs to do the decryption them selves.
  

3) you can encrypt the data with your own permanent key pair, In this case, when imported in SD Desktop, the data needs o be manually descrypted. 


!!! note
Files that have been encrypted with the _CSC Sensitive Data Services public key_, can't be used in any other services as the corresponding
secret key is available only in the SD services environment. If you wish to encrypt your data for some other service, you should do another 
encrypted file that uses other public keys.


**When using SD Connect to safely share (or transfer) data with your collaborators, you need to plan data encryption in advance, as you need to encrypt the data with your collaborator's public encryption key**.




## Data encryption with Crypt4GH Command Line Interface (CLI) and your own permanen key pair

For documentation and more information you can check [Crypt4GH](https://github.com/EGA-archive/crypt4gh.git)

**Python 3.6+ required** to use the crypt4gh encryption utility. 
To install Python: https://www.python.org/downloads/release/python-3810/

 
 ## Step 1: Install the latest version of Crypt4GH encryption tool
 
 
 To install Crypt4GH you can choose one of the following options: 
 
````
$ pip install crypt4gh     
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


## Step 2: Generate a permanent public-private keypair


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



!!!Note
Programmatically you can add more than one public key. This could be useful in case you need to share your data with a collegue or collaborator: including thier public key will allow them to decryot the same dataset with thier private/public key pair. 


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

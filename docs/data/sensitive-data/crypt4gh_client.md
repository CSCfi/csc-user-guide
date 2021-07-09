
# Data encryption for data sharing

## Before you start

### Sensitive data needs to be encrypted before upload

According to CSC policies and [general terms of use](https://research.csc.fi/general-terms-of-use), sensitive data always
needs to be encrypted when uploaded or stored in CSC services. Sensitive data needs to be encrypted even if, for example,
downloaded from public repositories. The encryption requirement applies to the SD Connect service too.
Automatic encryption during data upload has not been implemented to SD Connect yet. Because of this, at the moment,
you must encrypt all the sensitive data on your local environment before you start to upload it to SD Connect.
Data that is not sensitive, can be uploaded without encryption.


### Crypt4GH based encryption

There are many valid methods to encrypt your data. In this document we focus on [Crypt4GH](https://crypt4gh.readthedocs.io/en/latest/) as that
is the default encryption tool in the **CSC Sensitive Data Services**. Crypt4GH was originally designed to encrypt and share human genetic data according to the
Global Alliance for Genomics and Health (GA4GH) standard, but it can be used to encrypt any type of data.

Crypt4GH uses **asymmetric encryption**, an encryption method that is based on two interlinked encryption keys:

   1) a **public key**, is used for encryption but it can't decrypt the encrypted data. You can share your public encryption key with your collaborators
   (e.g. multiple data owners, sequencing facilities etc), they can encrypt the data with your public key and only you will be then able to decrypt the
   data with your own secret key.
   
   2) a **secret key**, (private key) is used for decrypting a file that is encrypted with the corresponding public key. This key should not be made available to other users and normally it is password protected to ensure that it remains secret.


* **When using CSC Sensitive Data Services for analyzing sensitive data you have two possibilities:**

1) you can encrypt the data with the workflow described earlier in the [SD Connect guide](./sd_connect.md). With this workflow, you will encrypt a copy of your data using the _CSC Sensitive Data public encryption key_ (using the Crypt4GH user interfaces or programmatically). In this way, the data is automatically decrypted with **CSC Sensitive Data Services secret key"** when it is imported to SD Desktop. This key is hosted securely by the SD Services and users never need to do the decryption themselves. Futher, the data can't be decrypted in any other environment.
 

2) you can encrypt the data with one or several public keys. In this case, when imported in SD Desktop, you need to decrypt the data there manually. Note that in this case you need to have a corresponding secret key in SD Desktop. In practice this means that you have to encrypt your private key using the option 1 above and upload it to SD Desktop through SD Connect.


* **When using SD Connect to safely share (or transfer) data with your collaborators, you need to plan data encryption in advance, as you need to encrypt the data with your collaborator's public encryption key for them to be able to decrypt the data**. Using Crypt4GH CLI, it is possible to encrypt data with multiple public encryption keys. Thus, for example, the same dataset can be safely shared with multiple colleagues or collaborators.


!!! Note
    Files that have been encrypted only with the _CSC Sensitive Data Services public key_, can't be used in any other services as the corresponding secret key is             available only in the SD services environment. If you wish to encrypt your data for some other service, you should do another
    encrypted file that uses other public keys.





## Crypt4GH Command Line Interface (CLI)

For documentation and more information you can check [Crypt4GH](https://github.com/EGA-archive/crypt4gh.git)

In this example, first we generate your permanent key pair ( a private key password protected and a public key that can be shared with collaborators). Then, we encrypt a file with your public key (_my_key.pub_) and your collaborators public key (_her_key.pub_). In this way, both you and your collaborator will be able to decrypt the file in your safe environment whithout a need to share secret keys or passwords.
 
 


 
 ### Step 1: Install the latest version of Crypt4GH encryption tool


**Python 3.6 or newer is required** to use the Crypt4GH encryption utility.
To install Python: https://www.python.org/downloads/release/python-3810/
When you have a working python installation, you can install Crypt4GH with one of the following options:
 
````
$ pip install crypt4gh     
````

or if you prefer the latest sources from GitHub:

```
pip install git+https://github.com/EGA-archive/crypt4gh.git
pip install -r crypt4gh/requirements.txt
pip install ./crypt4gh
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


### Step 2: Generate a permanent public-private keypair


```
$ crypt4gh-keygen --sk my_key.sec --pk my_key.pub
```

where:

* _my_key.sec_ is your secret key and

* _my_key.pub_ is your public key.

When keys are generated the tool will then ask you to assign a password for your private key. Use a strong password.

```
Passphrase for my_key.sec:
```

Your collaborator should generate her own key pair in her own environment and send just the public key to you.
Typically the same keypair is used for several encryption tasks.

Keeping the amount of keys small is recommend as afterwards you can't check, what keys were used for encryption.
If you are not able to find the right secret key and password, your data can't be used any more.



### Step 3: Encrypt the file or directory


In this example we are using your and your collaborators public keys to encrypt a file containing a dog image ( _dog.jpg_).

```
$ crypt4gh encrypt --recipient_pk my_key.pub --recipient_pk her_key.pub < dog.jpg > dog.jpg.c4gh
```

The command above creates an encrypted file _dog.jpg.c4gh_ that can be decrypted only using a secret key matching one of the two public keys used.



### Step 4: Data Decryption

If you did not use Sensitive Data services public key you need to decrypt the data in SD Desktop. 
Firtst make sure that you have your secret key available in the SD Desktop. (Import it through SD Conncect if needed.)

Crypt4gh is available in the SD Desktop so you don't need to install it. 

```
$ crypt4gh -h
```

Next use _crypt4gh_ with your private key (_my_key.sec_) to decrypt the file you want to use (_dog.jpg.c4gh_):

```
$ crypt4gh decrypt --sk exaple-your-name.sec < dog.jpg.c4gh > dog.jpg
```

The tool will ask you to input your private key password:

```
Passphrase for example-your-name.sec:
```

After decryption you will have both the encrypted and decrypted file in SD Desktop. 

```
dog.jpg
dog.jpg.c4gh
```

















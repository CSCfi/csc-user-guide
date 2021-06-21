## Data encryption with Crypt4GH Command Line Interface (CLI) and your own permanen key pair

For documentation and more information you can check [Crypt4GH](https://github.com/EGA-archive/crypt4gh.git)

**Python 3.6+ required** to use the crypt4gh encryption utility. To install Python: https://www.python.org/downloads/release/python-3810/

 
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

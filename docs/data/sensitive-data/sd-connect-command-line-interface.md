## Command Line Interface: encryption for data sharing 

For documentation and more information, you can check the [Crypt4GH Encryption Utility](https://github.com/EGA-archive/crypt4gh.git) page.

In this example, we first generate your key pair (a password-protected private key and a public key that can be shared with collaborators). Next, we encrypt a file with your private key and the public keys of two different collaborators (research group A and research group B).

**Python 3.6+ is required** to use the Crypt4GH encryption utility. If you need help installing Python, please follow [these instructions](https://www.python.org/downloads/release/python-3810/).

1- Install the Crypt4GH encryption CLI tool

You can install Crypt4GH directly with pip tool:

```bash
pip install crypt4gh     
```

or, if you prefer the latest sources from GitHub:

```bash
pip install -r crypt4gh/requirements.txt
pip install ./crypt4gh
```

or even:

```bash
pip install git+https://github.com/EGA-archive/crypt4gh.git
```

The usual `-h` flag shows you the different options that the tool accepts:

```bash
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

You may notice that crypt4gh uses `--sk` option for the private key. This might seem odd but apparently, crypt4gh uses term _secure key_ for private key, hence `sk`, and consequently `pk` refers to public key instead of the private key.

2- Generate your public-private keypair

You use `crypt4gh-keygen` command to create your private and public keys:

```bash
$ crypt4gh-keygen --sk mykey.sec --pk mykey.pub
Generating public/private Crypt4GH key pair.
Enter passphrase for meykey.sec (empty for no passphrase): 
Enter passphrase for mykey.sec (again): 
Your private key has been saved in mykey.sec
Your public key has been saved in mykey.pub
```

where `--sk mykey.sec` is your private (secret, sk) key and `--pk mykey.pub` is your public key (pk). The tool will ask you to enter a password (passphrase) for your private key. For security reasons, the password is not shown when you type it so the tool will ask you to enter it a second time to make sure you made no typing errors (or, you make the same errors twice…). Please, use a strong password!

!!! Note
    If you lose or forget your private key, or the password to it, you will be unable to decrypt the files. Do not share your private key or your password.

!!! Note
    You need to create your keys only once and use them for all your encryption needs, but you can of course, choose to generate separate keys for encryption as you wish.

3- Encrypt a file

To ecrypt files you will need 1) your private and public keys, and 2) your recipients' public keys. As stated before, in this example we are sharing the data with two recipients (research groups A and B) and hence, we have received their public keys somehow (e.g. via email). To encrypt a file you use `crypt4gh encrypt` command:

```bash
$ crypt4gh encrypt --sk mykey.sec --recipient_pk groupA.pub --recipient_pk groupB.pub <dog.jpg >dog.jpg.c4gh
Passphrase for mykey.sec: 
```

where `--sk mykey.sec` is your private key, `--recipient_pk groupA.pub` is the research group A's public key, and `--recipient_pk groupB.pub` is the research group B's public key. The `crypt4gh` command uses only standard input (stdin) and standard output (stdout) so you must use shell redirections: `<` denotes an input file and `>` and denotes an output file, hence `<dog.jpg` reads in a file called _dog.jpg_ and `>dog.jpg.c4gh` writes out an encrypted file named _dog.jpg.c4gh`.

The command will ask you to enter the password (passphrase) of your private key. For security reasons, the password is not displayed when you type it.

!!! Note
    If you want to be able to decrypt the file yourself you must add your own public key also as a recipient.

4- Decrypt a file

To decypt a file you will need a private key which corresponds to one of the public keys used in encryption phase. Let's assume in our example that the research group A is decrypting a file you've sent them. To decrypt a file you use `crypt4gh decrypt` command:

```bash
crypt4gh decrypt --sk groupA.sec <dog.jpg.c4gh >dog.jpg
Passphrase for groupA.sec: 
```

where `--sk groupA.sec` is a corresponding private key to one of the public keys used in the encryption. The `crypt4gh` command uses only standard input (stdin) and standard output (stdout) so you must use shell redirections: `<` denotes an input file and `>` and denotes an output file, hence `<dog.jpg.c4gh` reads in an ecrypted file called _dog.jpg.c4gh_ and `>dog.jpg` writes out a decrypted file named _dog.jpg_.

The command will ask you to enter the password (passphrase) of your private key. For security reasons the password is not displayed when you type it.

!!! Note
    In case you are decrypting the file in SD Desktop and the CSC Sensitive Data public key has been used in encryption, decryption will be done automatically and you do not need to specify any decryption keys.
    
    
    

    
 
## Troubleshooting 




| Problem                                                       | Description                                                                                                                                                                   | Solution                                                                                                                                                                                                                                                                                                                                                                               |
|---------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Access                                                        | I can not access SD Connect                                                                                                                                                   | 1) Verify in the MyCSC portal if your CSC project  has service access to the  Allas and accepted CSC’s terms of use.  2) Link your Haka account to your CSC account 3) SD Connect is not supported during private browsing with Firefox (incognito mode).                                                                 |
|                                                               | I can not access files stored in SD Connect using SD Desktop                                                                                                                  | Unencrypted files are not accessible via the SD Desktop service. Only files encrypted using the SD service encryption key are visible in the secure computing environment (or encrypted using SD Connect default option). Refresh the Data Gateway application.                                                                                                                        |
| Bucket creation                                               | I can not create a new bucket.	                                                                                                                                                | 1) Check in the MyCSC portal that your current project has service access for Allas  2) Try using a unique bucket name that doesn’t contain special characters. 3) Select the correct project in the SD Connect user interface                                                                                                                                                         |
| Bucket not visible                                            | I cannot find my bucket.                                                                                                                                                      | Check if the bucket is stored under a different project. If someone has shared the bucket with you, you can find it under the ‘Shared to’ section and copy it. If someone shared the bucket with you, they could have revoked it.	                                                                                                                                          |
| Bucket deletion                                               | I can  not delete an empty bucket                                                                                                                                             | 1)This problem is due to a technical issue. It can be solved by clearing cookies in your browser. We are working on solving the underlying issue. If the bucket has been created in November or December 2022 contact us at servicedesk@csc.fi                                                                                                                                         |
| Decryption with Crypt4gh                                      | Cannot open or decrypt files downloaded from SD Connect.                                                                                                                      |  You can not decrypt files that have been encrypted with the SD Connect user interface and default option. In this case, the files have been encrypted with the service-specific encryption key and are automatically decrypted when accessed using the SD Desktop service. If the bucket has been created in November or December 2022 contact us at servicedesk@csc.fi               |
| Data upload                                                   | I am trying to upload a big file/folder with the user interface, and the upload is not responding.                                                                            |  Files or folders larger than 100 GB  should be uploaded programmatically. SD Connect user interface supports only data uploads that last up to 8 hours.                                                                                                                                                                                                                               |
| Data upload                                                   | I cannot upload data into my bucket                                                                                                                                           | Check if your CSC project has storage space left and apply for more quota (more info available in the first chapter of this guide under Accounts).                                                                                                                                                                                                                                     |
| Data upload                                                   | Low upload speed (programmatically)                                                                                                                                           |  The average upload speed can go from 100 to 200 MiB/s. Specific scripts can be used to optimize the upload of large files.                                                                                                                                                                                                                                                            |
| Data upload and empty bucket                                  | After uploading several files, the bucket looks empty, and the total number of files (object) is zero. However, if I open the bucket, I see the encrypted files stored in it. | This problem is due to a technical issue. It can be solved by clearing cookies in your browser. We are working on solving the underlying issue.                                                                                                                                                                                                                                        |
| Encryption with crypt4gh                                      | Encryption takes a long time.                                                                                                                                                 | Encryption can take up to several minutes for large files and datasets.                                                                                                                                                                                                                                                                                                                |
| Encrypting a folder with Crypt4g or SD Connect user interface | Can not select the folder I want to encrypt with the Crypt4GH application.                                                                                                    |  It is not possible to encrypt or decrypt all the files saved in one folder with the Crypt4GH application, only single files. However, we can provide specific scripts to help you with this operation. Moreover, uploading and encrypting all the files saved in one folder with the SD Connect user interface is possible. However, this option is available only via drag-and-drop. |
| Shared bucket                                                 | I cannot upload data into a shared bucket.                                                                                                                                    | Your colleague didn’t add editing rights when they shared the bucket.                                                                                                                                                                                                                                                                                                                  |
|                                                               | I cannot see the content of a shared bucket.                                                                                                                                  | Your colleague didn’t add reading rights when they shared the bucket.                                                                                                                                                                                                                                                                                                                  |


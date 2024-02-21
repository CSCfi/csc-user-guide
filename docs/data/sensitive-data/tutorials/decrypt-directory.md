
# Decrypting all files in a directory

The graphical Crypt4gh interface provides an easy way to encrypt and decrypt
individual files. However, the encrypted datasets may contain large amounts
of files and in those cases doing encryption or decryption file-by-file
can be too laborious.

This document provides simple scripting examples to
illustrate how decryption process can be automatized.
In practice automatized decryption process requires two
functionalities:

  1. Constructing a loop that finds encrypted files
  and executes decryption command.

  2. A method that automatically provides the decryption password to
  decryption commands.

In the examples below we assume that we have a directory
named as _data1_. The directory contains hundreds of files
of which the encrypted files have _.c4gh_ suffix. The encryption
is done so that decryption can be done with secret key _my-key.sec_
that is protected with password: _badpasswd_.


## Decryption using bash script in Mac and Linux

In Linux and Mac machines `crypt4gh`command line tool is able
to read the password of the private key from environment variable
C4GH_PASSPHRASE. Thus the first step is set this variable. In bash shell
this could in this case be done with commands:

```bash
read C4GH_PASSPHRASE
export C4GH_PASSPHRASE
```

Find command can be used to list all files that end with
_.c4gh_ in a given directory (_data1_) and its' subdirectories.
This list can be used as an input for a _for loop_.

```bash
find data1 -name *.c4gh
```

Inside the loop  we need to define a name for the decrypted file. I this case
we use command pipeline _rev | cut -c6- | rev_  to cut away the five last
character of the encrypted filename ( i.e .c4gh ) to define a filename
for decrypted data.

The actual decryption is done with command:

```bash
crypt4gh decrypt --sk my-key.sec < encrypted-file > decrypted-file
```

With these steps, the complete script could look like following:

```bash
#!/bin/bash

echo "Give the password of my-key.sec"
read C4GH_PASSPHRASE
export C4GH_PASSPHRASE

for f_encrypted in $(find data1 -name *.c4gh)
do
  echo "Decrypting $f_encrypted"
  #define the file name for the decrypted data
  f_decrypted=$(echo $f_encrypted | rev | cut -c6- | rev)
  crypt4gh decrypt --sk my-key.sec < "$f_encrypted" > $f_decrypted
done
```

The script could be executed with commands:

```bash
  chmod u+x decryption_script
  ./chmod u+x decryption_script
```


## Decryption using windows PowerShell

Cryp4gh is available for Windows machines too, but the windows version
is not able read the secret key password from environment variable.
Because  of that  we need to use _sda-cli.exe_ command instead.
In this case the password can be stored in variable C4GH_PASSWORD.

Sda-cli.exe command can be downloaded from:
[https://github.com/NBISweden/sda-cli/releases](https://github.com/NBISweden/sda-cli/releases)

Once the command is available, the decryption can be done with following
PowerShell commands. Here we assume that the data to be decrypted is in
directory _E:\data1_.

```powershell
$env:C4GH_PASSWORD = "badpasswd"
$files = (Get-ChildItem -Path 'E:\data1\'*.c4gh -Recurse).fullname

foreach ($f in $files) {
.\sda-cli decrypt -key .\my-key.sec $f  }
```

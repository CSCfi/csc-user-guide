# Tools for client side encryption for Allas

Allas is not certifed for high level security and thus you should not use it to store sensitive data in drectly readable format.
Howerver, if you use proper encryption, the sensitive data can be stored to Allas in encrypted format. However the ecrypytion must
be done before data is transported to Allas

This document describes some password based (symmetric) ecryption tools that help you to move your data to from a secure environmnet 
to Allas. When you use Allas with these scryption tools, remember that:
   1. You can only store the encrypted data in Allas, but not open it there. 
   2. You should use strong enough passwords
   3. If your forget the encryption password, the data is lost. 
      CSC can't provide you a new password to read your data  as the password is set by the users, not CSC.
   
   
  ## Encrypting single file with a-put
  
In you install [allas-cli-utils](https://github.com/CSCfi/allas-cli-utils/) to your can use a-put with option _--encrypt_ to encrypt the file or drectory you want to upload to Alls. For ecxample
 
```text
a-put --encrypt data_dir -b my_allas_bucket
``` 
With the emnryot option on the data is encrypted with _gpg_ command using _AES256_ enryption algorithm. When you launch the command it will ask for encryption password, and password confirmation. In this approach only that content of the file or directory is encrypted. Object name and metadata remain in human readable format. 

When you retrieve the data with _a-get_ command, you will be asked for the encryption password so that ecryption can be opened.

 ## Creating encrypted reposoitury with rclone
 
Rclone has client side encrypitoin feature, that allows you create an ecrypted datarepository to Allas. In this approach you need to once define an encrypted rclone connection to Allas and when this connection is used, all the data, cluding object names, will be automatically encrypted.

Let's assume that you are using a server where you have [rclone](https://rclone.org/) and [allas-cli-utils](https://github.com/CSCfi/allas-cli-utils/) installed. Once you have configured a normal swift connection to Allas with command the _allas_conf_ script you can configue and encrypted 
bucket to your Allas area. To stat process run command _rclone config_. As first step, choose opion: _n_ to createa new remote.
The configuration process will ask for a name for the new rclone _remote_. In this the new remote is named as named as _allas-crypt_.

<pre>
[kkayttaj@puhti-login1 ~]$ <b>rclone config</b>
Current remotes:

Name                 Type
====                 ====
allas                swift

e) Edit existing remote
n) New remote
d) Delete remote
r) Rename remote
c) Copy remote
s) Set configuration password
q) Quit config
e/n/d/r/c/s/q> <b>n</b>
name> <b>allas-crypt</b>
</pre>
Next the configuation process asks you to configure storage type.
Choose option 10 _Encrypt/Decrypt a remote_.
<pre>
Storage> <b>10</b>
</pre>
In the next step you need to define the bucket that will be used for encrypted data. 
Note that the bucket name should be unique among all Allas users. This case we use buket name _allas:2001659-crypt_
<pre>
Remote to encrypt/decrypt.
Normally should contain a ':' and a path, eg "myremote:path/to/dir",
"myremote:bucket" or maybe "myremote:" (not recommended).
Enter a string value. Press Enter for the default ("").
remote> <b>allas:2001659-crypt</b>
</pre>
Next, the configuration process asks if the object and directory names are encrypted. In this case we want to encrypt the names so we choose _1_ for both cases.

Next youy need to define passwords that will be useid in the encryption.

 
 
 
 ## Restic

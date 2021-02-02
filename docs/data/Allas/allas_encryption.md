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
 
 Rclone has client side encrypitoin feature, that allows you create an ecrypted datarepository to Allas. In this approach you need to once definen an encrypted rclone connection to Allas and when this connection is used, all the data, icluding object and bucket names will be automatically endrypted.
 
 
 ## Restic

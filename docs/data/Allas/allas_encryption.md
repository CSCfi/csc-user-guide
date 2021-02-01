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
  
  ## Creating encrypted reposoitury with rclone
  
  ## Restic

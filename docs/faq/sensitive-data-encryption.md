# Encryption

## Why do I need to encrypt my data?
According to the GDPR, the data controller and the data processor need to implement appropriate technical and organizational measures to ensure a level of security appropriate to the risk. Encryption is one of the required security measures that protect sensitive data. See: [Best practices for client-side encryption](https://research.csc.fi/best-practices-for-client-side-encryption).

## Do sensitive data always need to be encrypted during upload or data transfer (e.g., using an  SSH connection)?
Yes. According to CSC's [General terms of use](https://research.csc.fi/general-terms-of-use), sensitive data must be encrypted when stored in CSC services or transferred to CSC. Therefore, data needs to be encrypted if, for example, you are using an SSH connection for data transfer. 

## What methods can I use to encrypt the data? How can I use the CSC public encryption key?
Data can be encrypted with several methods. In our user guide, we suggest the use of Crypt4GH. You can use your encryption key pair or the CSC public encryption key in this tool. If the CSC public encryption key is used, in addition to your public key, the data will be automatically decrypted when accessed via data streaming or copied into your private Desktop. You can find detailed information in the user guide and video tutorials. 

## What data formats can be encrypted using Crypt4GH?
You can encrypt data in any format with Crypt4GH (e.g., video, images, text files, etc.). 

## What is the new extension added to my files after Crypt4GH encryption?
When encryption with Crypt4GH is successful, the file extension ends with .c4gh. The extension will be removed when once the file is decrypted. 

## Do CSC Sensitive Data services allow the use of customers' encryption keys?
Yes. You can encrypt the data with multiple encryption keys. For example, with your public encryption key and the Sensitive Data services encyption key (added by dafault during data upload via SD Connect). In this manner, the files can be directly accessed for data analysis via SD Desktop.

## Can I share my public encryption key with others?
Yes. You can share your public encryption key with your colleagues and collaborators. A public key can be used to encrypt data, and only the private key associated with it can decrypt it. 

## Can I share my private encryption key with others?
No. The private encryption key can be used to decrypt the data. Therefore, you should keep the encryption key in a safe environment. You should always set a strong password for your private encryption key.

## Do I need to generate a new key pair every time I encrypt a new dataset?
No. You can generate just one encryption key pair for each use case (e.g., to be research group-specific or project-specific) and always use the same key pair. If the private key is password protected (with a strong password) and kept in a secure and secrete place, using the same encryption key multiple times does not bring any additional risk. 

## Can I (or my collaborators) decrypt data encrypted only with the CSC public encryption key outside SD Desktop?
No. Data encrypted only with the CSC public encryption key is only decrypted in an automated manner when accessed via data streaming in SD Desktop. You can however encrypt your files with multiple encryption keys, using SD Connect or programmatically. If you need support, contact us at servicedesk@csc.fi

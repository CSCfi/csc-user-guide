# Encryption

## Why do I need to encrypt my data?
According to the GDPR, the data controller and the data processor need to implement appropriate technical and organizational measures to ensure a level of security appropriate to the risk. Encryption is one of the required security measures that protect sensitive data. See: [Best practices for client-side encryption](https://research.csc.fi/best-practices-for-client-side-encryption).
SD Connect provides automated data encryption and decryption, via a web user interface or programmatically. 

## Do sensitive data always need to be encrypted during upload or data transfer (e.g., using an  SSH connection)?
Yes. According to CSC's [General terms of use](https://research.csc.fi/general-terms-of-use), sensitive data must be encrypted when stored in CSC services or transferred to CSC. Therefore, data needs to be encrypted if, for example, you are using an SSH connection for data transfer. 

## What data formats can be encrypted using SD Connect?
You can encrypt data in any format (e.g., video, images, text files, etc.). 

## What is the new extension added to my files upload with SD Connect?
When encryption with SD Connect is successful, the file extension ends with .c4gh. The extension will be removed when once the file is decrypted. 

## Do CSC Sensitive Data services allow the use of customers' encryption keys?
Yes. You can encrypt the data with multiple encryption keys. Plese contac us at servciedesk@csc.fi (Subject: Sensitive data) for support.


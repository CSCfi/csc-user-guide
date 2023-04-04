# SD Connect

## What are the technical specifications of the service?

* Storage space: default 10 TiB. Additional quota, up to 200 TB, can be required at: servicedesk@csc.fi.

* Sensitive data uploaded to SD Connect must be encrypted according to [CSC General Terms of Use](https://research.csc.fi/general-terms-of-use).

* Encrypted data stored in SD Connect can be accessed and analyzed using SD Desktop.

* Automated encryption via browser available for files <1 GB. 


## How long can I store data in SD Connect? 
You can store data in SD Connect/Allas during the active phases of your research (data analysis and data collection) and for the duration of your CSC project. 
A typical research project using CSC services has a lifespan of several weeks to 1–2 years. A resource allocation for a project is for a maximum of one year at a time.

## What is the difference between SD Connect and Allas?
SD Connect is a web-user interface that facilitates sensitive data storage and sharing. 
In the future, SD Connect will also function as a hub from which you can manage your datasets at any stage of your research: 
collect data, share data or submit them to a specific repository.

SD Connect is a specific user interface that facilitates the use of Allas during sensitive data management. In contrast, Allas is a general cloud storage solution for non-sensitive and encrypted sensitive data. It is accessible through various clients or user interfaces. 

## Can I use SD Connect from command line?
You can operate (upload, download, delte) the SD Connect objects with any Allas interface. However to be compatible with the SD services you must encrypt the data also with CSC public key before upload. a-put command has an option that enables this. Alternatively you can do the encryption yourself with crypt4gh. Note that even though you are able to download the encrypted files to your local environment, you can't convert the data into readable format if it is encrypted with CSC public key only. 

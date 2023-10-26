# Introduction to data encryption compatible with Sensitive Data services


<iframe width="280" height="155" srcdoc="https://www.youtube.com/embed/dI1Py_1gA-k" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


Sensitive data uploaded to CSC's cloud services using SD Connect or programmatically must be encrypted. Files encrypted following the guidelines provided in this chapter will be compatible and accessible via all Sensitive Data (SD) Service components. This way, encrypted files stored in the SD Connect service will be available for analysis (using the SD Desktop service) or publishing and reuse under controlled access (via SD Submit, Federated EGA, or SD Apply). 

!!! Note
    Data encryption does not require technical expertise but requires you to become familiar with the following user guide and video tutorials. We also provide step-by-step guidance online or via the help desk. If you have any questions or the instructions below need clarification, don't hesitate to [contact us](../../support/contact.md) (subject: Sensitive Data). 

We integrated the encryption as an automated step in the SD Connect user interface, specifically for files smaller than 1 GB. All the data uploaded using SD Connect are automatically encrypted with the Sensitive Data services public encryption key. However, you can choose different options to encrypt your data for analysis or sharing. 

Briefly, the services use an encryption method called _asymmetric encryption_, based on two interlinked encryption keys:

   * A public key is used for data encryption. A public can not be used to decrypt the data. You can share your public key with others, e.g. your collaborators, and they will then be able to encrypt data with your public key. 

   * A secret key (also called a private key) is used to decrypt a file encrypted with the corresponding public key. This key is password protected and can not be shared with others. 


When using SD Connect to upload your data to CSC, you have several possibilities for encryption:

1. Default option for data analysis:

      * With the default encryption options, you can upload the data using SD Connect via your web browser for data analysis. The files will be automatically encrypted and accessible for analysis via SD Desktop. However, you cannot decrypt the files after downloading them to your laptop or organization's computing environment. Therefore, we are developing a new feature that provides automated decryption via SD Connect. For more information, [contact us](../../support/contact.md) (Sensitive Data).

2. Adding multiple encryption keys for data storage, sharing and transfer:
   
      *  You can upload the data using SD Connect via a web browser and add your public encryption key. The files will be encrypted with the SD services by default, but you can also add your encryption key. In this manner,  you will also be able to download and decrypt the data when necessary
         
      *  You can upload the data using SD Connect via your web browser and add several encryption keys. For example, your public encryption key and your collaborator's public encryption key. Also, in this case, the files will be encrypted with the SD services encryption key by default and available for data analysis via SD Desktop. Moreover, you and your collaborator can also download and decrypt the data when necessary.

   
This encryption method is based on Crypt4GH, a tool initially designed to encrypt and share human genetic data according to the [Global Alliance for Genomics and Health](https://www.ga4gh.org/) (GA4GH) standard. Crypt4GH can be used to encrypt any file (images, audio, video, text files, etc.).
CSC has developed a simple application that will allow you to **generate your encryption keys**. 

The following paragraphs illustrate all the necessary steps to generate encryption keys, upload and encrypt your data using SD Connect, and decrypt the files once downloaded back to your computer. Of course, you can also execute each of these steps programmatically.


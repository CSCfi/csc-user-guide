# Submitting secondary use health and social data for research use via SD Apply

These instructions are for data controllers who have issued a data permit for a research project and need to make their data available on SD Desktop.

!!! Note 
    The  first register data set must always be submitted in a collaboration with the CSC Sensitive Data (SD) services team. You can start a conversation with the SD services team by sending a message to the CSC service desk (servicedesk@csc.fi, subject: Sensitive Data).

After the process is established for the first time, the data controller can manage the subsequent data submissions on their own. Help is always available via the service desk.

## Submission process step by step:

**1)** The representative of the data controller signs in to [SD Apply service](https://sd-apply.csc.fi/) using Haka credentials. After the first log in, CSC service desk can create an organizational profile, which will be used for all the data submissions coming from this organization, and assign the representative as an owner of the organizational profile. There can also be multiple owners for one organization.

**2)** The owner can then create a workflow, forms and licenses for the organization in SD Apply. Workflow represents the data access management (defines who will accept the access applications in SD services). To forms, the owner can add the data permit information for each data submission. Licenses specify the terms of use for the data. For each of these, the Haka ePPN should be used as a title.

**3)** Next, the representative of the data controller who will do the data submission logs in to [the user administration portal](https://admin.sd.csc.fi/) with Haka credentials. Here they must **1)** add the IP address from which the data submission will be done (IP address can be checked with [CSC’s My IP app](https://apps.csc.fi/myip/)) and **2)** add their public SSH key. With this information, the CSC service desk will make the necessary preparations for data submission from the SD service side.

**4)** After the preparations are done, the representative of the data controller can test that the SFTP connection works with the command:

```
sftp -P 50527 username@eppn.fi@porin.lega.csc.fi
exit
```

**5)** Before transfer, the data must be encrypted with [a CSC public key](https://admin.sd.csc.fi/publickey/?instance=single%20registry). CSC provides a convenience tool that encrypts and uploads data automatically. SDA Uploader tool is available on [GitHub](https://github.com/CSCfi/sda-uploader/releases). Encryption and upload can also be done manually with crypt4gh and SFTP.

**6)** Now everything is ready for the data to be transferred to CSC. The representative of the data controller sends the encrypted data via SFTP to a directory which must be named according to the journal number from the data permit. The final dataset ID will be a combination of  the organization’s Haka ePPN and the journal number (e.g. eppn.fi/example_dataset_123). 

```
sdacli example_dataset_123 -host porin.lega.csc.fi -p 50527 -u username@eppn.fi -i ~/.ssh/id_rsa -pub registry.pub
```

**7)** After the data has been submitted successfully, it can be found in SD Apply with the dataset ID. The researcher who has received the data permit can contact the CSC service desk and ask for a CSC project with the data permit. After the project has been established, they can log in to SD Apply and apply for data access. The assigned representatives of the data controller will receive a notification of the application to their email. They can review and approve the application and set an end date for the data access in SD Apply. The permission can also be revoked manually in the future, but automated end date is preferred.

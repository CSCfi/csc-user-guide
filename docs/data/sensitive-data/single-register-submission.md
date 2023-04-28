# Submitting secondary use health and social data for research use via SD Apply

These instructions are for data controllers who have issued a data permit for a research project and need to make their data available on SD Desktop.

!!! Note 
    The  first register data set must always be submitted in collaboration with the CSC Sensitive Data (SD) services team. You can start a conversation with the SD services team by sending a message to the CSC service desk (servicedesk@csc.fi, subject: Sensitive Data).

After the process is established for the first time, the data controller can manage the following data submissions on their own. Help is always available via the service desk. Below are the submission process instructions.

## Step 1: CSC account and organizational profile in SD Apply

The representative of the data controller creates [CSC account]((../../accounts/how-to-create-new-user-account.md) by logging in with Haka or Virtu credentials at the [My CSC portal](https://my.csc.fi/). If the representative doesn't have Haka or Virtu credentials, they need to request an account from the service desk (servicedesk@csc.fi, subject: Sensitive Data).

When the representative has an CSC account, they can log in to [SD Apply service](https://sd-apply.csc.fi/). After the first log in, CSC service desk can create an organizational profile for the data controller, which will be used for all the data submissions coming from this organization, and assign the representative as an owner of the organizational profile. There can also be multiple owners for one organization.

## Step 2: Creating objects in SD Apply

The owner of the organization profile can then create a workflow, form and license for the organization in SD Apply. 

1. With a workflow, the owner defines who will manage the access applications of the organization in SD services. These named users will always receive a notification via email about new access applications and can approve or reject the applications in SD Apply.
2. To the form, the owner adds all the information needed for access applications. This information will be shown to the applicants in SD Apply. To the form, the owner can also add fields for the applicant to fill.
3. License specifies the terms of use for the data, which the applicants need to approve when they fill in the access application form. In the license, the owner can for example refer to the terms specified in the data permit.

## Step 3: Preparations for the data transfer

Next, the representative of the data controller, who will do the data submission, logs in to the [user administration portal](https://admin.sd.csc.fi/). In the administration portal, they must **1)** add the IP address from which the data will be transferred (IP address can be checked with [CSC’s My IP app](https://apps.csc.fi/myip/)) and **2)** add their public SSH key. With this information, the CSC service desk will make the necessary preparations for data submission from the SD service side.

After the service desk has confirmed that the preparations are done, the representative of the data controller can test the SFTP connection. This can be done with the following command (replace *username(a)org.fi* with your credentials and *X:\folder\filename.key* with the location of your SSH key):

```
sftp -i X:\folder\filename.key -P 50527 username@org.fi@porin.lega.csc.fi
exit
```

## Step 4: Data encryption and upload 

Before the data transfer, the data must be encrypted with a [CSC public key](https://admin.sd.csc.fi/publickey/?instance=single%20registry). CSC provides a convenience tool that encrypts and uploads data automatically. This SDA Uploader tool is available on [GitHub](https://github.com/CSCfi/sda-uploader/releases), and has both graphical user interface (GUI) and command line (CLI) options for Linux, Mac and Windows.

The representative of the data controller sends the encrypted data via SFTP to a directory which must be named according to the journal number from the data permit. The final dataset ID will be a combination of the organization’s identifier and the journal number (e.g. org.fi/example_dataset_123). Name the file to be uploaded with the journal number.

**With the GUI tool**, the user needs to add the [CSC public key](https://admin.sd.csc.fi/publickey/?instance=single%20registry), the file they want to upload, and their SSH key (SFTP key) to the interface. They also need to fill in their username (*username@org.fi*) and the SFTP server: porin.lega.csc.fi:50527

**With the CLI tool**, the user needs to add the following command to the command line (replace *example_dataset_123* with the journal number, *username(a)org.fi* with their credentials, and *X:\folder\filename.key* with the location of their SSH key):

```
sdacli example_dataset_123 -host porin.lega.csc.fi -p 50527 -u username@org.fi -i X:\folder\filename.key -pub registry.pub
```

**7)** After the data has been submitted successfully, it can be found in SD Apply with the dataset ID. The researcher who has received the data permit can contact the CSC service desk and ask for a CSC project with the data permit. After the project has been established, they can log in to SD Apply and apply for data access. The assigned representatives of the data controller will receive a notification of the application to their email. They can review and approve the application and set an end date for the data access in SD Apply. The permission can also be revoked manually in the future, but automated end date is preferred.

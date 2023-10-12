# Data submission

## Step 1: CSC account and organizational profile in SD Apply

Create [CSC account](../../accounts/how-to-create-new-user-account.md) by logging in with Haka or Virtu credentials at the [My CSC portal](https://my.csc.fi/). If you don't have Haka or Virtu credentials, you need to request an account from the service desk (servicedesk@csc.fi, subject: Sensitive Data).

When you have created an CSC account, you can log in to [SD Apply service](https://sd-apply.csc.fi/).

[![SD Apply login page](images/apply/apply_login.png)](images/apply/apply_login.png)

!!! note
    Always use the same identity provider when you log in to SD Apply because all your actions are connected to your login identity (i.e. use always only Haka/Virtu login or the CSC login).

After the first log in, CSC service desk can create an organizational profile for the data controller, which will be used for all the data submissions coming from this organization, and assign you as an owner of the organizational profile. There can also be multiple owners for one organization.

## Step 2: Creating objects in SD Apply

After you have been set as the owner of the organization profile, you can create a workflow, form and license for the organization in SD Apply.

1. With a workflow, you define who will manage the access applications of the organization in SD services. These named users will always receive a notification via email about new access applications and can approve or reject the applications in SD Apply.
2. To the form, you add all the information needed for access applications. This information will be shown to the applicants in SD Apply. To the form, you can also add fields for the applicant to fill, e.g. ask them to confirm the journal number by submitting it via the form.
3. License specifies the terms of use for the data, which the applicants need to approve when they fill in the access application form. In the license, you can for example refer to the terms specified in the data permit.

The forms and licenses are public in SD Apply, so these should not include sensitive information.

## Step 3: Preparations for the data transfer

Next, you can log in to the [user administration portal](https://admin.sd.csc.fi/). In the administration portal, you need to

1. add the IP address from which the data will be transferred (IP address can be checked with [CSC’s My IP app](https://apps.csc.fi/myip/)), and
2. add your public SSH key.

With this information, the CSC service desk will make the necessary preparations for data submission from the CSC side.

After the service desk has confirmed that the preparations are done, you can test the SFTP connection. This can be done with the following command (replace *username(a)org.fi* with your credentials and *X:\folder\filename.key* with the location of your SSH key):

```
sftp -i X:\folder\filename.key -P 50527 username@org.fi@porin.lega.csc.fi
exit
```

## Step 4: Data encryption and upload 

Before the data transfer, the data must be encrypted with a [CSC public key](https://admin.sd.csc.fi/publickey/?instance=single%20registry). CSC provides a convenience tool that encrypts and uploads data automatically. This SDA Uploader tool is available on [GitHub](https://github.com/CSCfi/sda-uploader/releases), and has both graphical user interface (GUI) and command line (CLI) options for Linux, Mac and Windows.

The encrypted data is sent via SFTP to a directory which should be named according to the journal number of the data permit. The final dataset ID will be a combination of the organization’s identifier and the journal number (e.g. org.fi/example_dataset_123). The file to be uploaded should also be named with the journal number.

**Option 1: With the GUI tool**, you add the [CSC public key](https://admin.sd.csc.fi/publickey/?instance=single%20registry), the file you want to upload, and your SSH key (SFTP key) to the interface. You also need to fill in your username (*username(a)org.fi*) and the SFTP server: ```porin.lega.csc.fi:50527```

**Option 2: With the CLI tool**, you add the following command to the command line (replace *example_dataset_123* with the journal number, *username(a)org.fi* with your credentials, and *X:\folder\filename.key* with the location of your SSH key):

```
sdacli example_dataset_123 -host porin.lega.csc.fi -p 50527 -u username@org.fi -i X:\folder\filename.key -pub registry.pub
```

After a successful upload, the dataset can be found in SD Apply.

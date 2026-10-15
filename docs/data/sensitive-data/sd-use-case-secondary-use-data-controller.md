[Table of contents of user guide :material-arrow-right:](sd-services-toc.md)

# Uploading secondary use health and social data for research use via SD Connect

## Use case

Your organisation has issued a data permit for a research group to process health and social data under the Secondary Use Act. You need to deliver the dataset to SD Desktop environment for the users.

!!! info "Important information before you start"
    - Before any data can be made available for researchers in the Sensitive Data services, you need to confirm that the necessary legal agreements are in place between the data controller and CSC.
    - The register dataset must always be uploaded in collaboration with the CSC Sensitive Data (SD) services team.
    - You can start a conversation with the SD services team by sending a message to the [CSC Service Desk](../../support/contact.md) (subject: Sensitive Data).

## Solution

1. [Create or apply for a CSC account](#1-create-or-apply-for-a-csc-account)
2. [Join a CSC project](#2-join-a-csc-project)
3. [Login to SD Connect](#3-login-to-sd-connect)
4. [Upload each dataset to a dedicated bucket](#4-upload-each-dataset-to-a-dedicated-bucket)
5. [Manage datasets](#5-manage-datasets)
6. [Data permit expiration and data deletion](#6-data-permit-expiration-and-data-deletion)

---

### 1. Create or apply for a CSC account

Creating a CSC account is possible only if you have a Haka or Virtu account. If you do not have one, contact CSC in order to apply for an account. [How to get an account without Haka or Virtu](../../accounts/how-to-create-new-user-account.md#getting-an-account-without-haka-or-virtu)

- **Go to [MyCSC portal](https://my.csc.fi){ target="_blank" }**
- Log in with Virtu or Haka, based on your home organization's federation. Select your home organization and log in to their identity service. [How to get an account with Haka or Virtu](../../accounts/how-to-create-new-user-account.md#getting-an-account-with-haka-or-virtu).
- Fill in your information on the Sign up page.
- You will receive with instructions how to complete the registration. 
- Create a password with at least 12 characters, including upper and lowercase letters and at least one number. No special characters allowed.
- Enable two-step authentication (MFA).

---

### 2. Join a CSC project

- CSC adds you to a CSC project that is created specifically for data transfers from your organisation.
- Check your email for a notification and log in to MyCSC to find the project. You will need the project number and project name to identify the correct project in SD Connect.

---

### 3. Login to SD Connect

Now all the preparations are ready and you can start using SD Connect service. Below you'll find links to related user guide:

- [SD Connect overview and key features](sd_connect.md)
- [SD Connect login instructions](sd-connect-login.md)

---

### 4. Upload each dataset to a dedicated bucket

CSC will create a bucket in SD Connect for each dataset, share the bucket name with you, and grant Read-only access to the bucket for the CSC project in which the data users will analyze the data in the isolated SD Desktop environment.

One bucket is created for each dataset based on a data permit. In other words, each bucket contains only one dataset and should include all data covered by the same data permit.

Data users create their CSC projects based on their data permits and can access only the data uploaded to the bucket shared with their project. If the same data users have multiple separate data permits, the datasets must be uploaded to separate buckets, and the users must have separate CSC projects for each data permit.

Follow these instructions to upload data to the buckets:

- [Upload and encrypt files to an existing bucket](sd-connect-upload.md#24-upload-and-encrypt-files-to-an-existing-bucket)
- [SD Connect command line tool for large datasets (over 50 GB)](sd-connect-command-line-interface.md)

---

### 5. Manage datasets

The datasets will remain in your control after they are uploaded to the buckets and shared to the users' projects. You can upload more data, remove files, and also remove the data access from the users anytime during the project lifetime.

1. **Delivering additional data**: You can add data to any existing dataset by [uploading new files to the bucket](#4-upload-each-dataset-to-a-dedicated-bucket) created for the data permit. Remember to use unique file names to avoid overwriting the old files.
2. **Removing corrupted or incorrect files**: You can remove data from aby existing dataset by [deleting files from the bucket](sd-connect-delete.md). NOTE! If the users are no longer allowed to use these files in their analysis, you need to also request that they remove any possible working copies of the files from their SD Desktop environment.
4. **Cancelling the data access**: You can terminate the data access any time by [removing the sharing of the bucket](sd-connect-share.md#4-delete-sharing-permission) and/or [deleting the data files](sd-connect-delete.md). However, same applies here as with removing files: if the data can no longer be used in any analysis, the users need to be instructed to remove all working copies of the data. In case the permission to process the data is withdrawn and user's access to the environment must be revoked, please contact the [CSC Service Desk](../../support/contact.md) (subject: Sensitive Data).

!!! Note ""
    ### 6. Data permit expiration and data deletion
    You can [delete datasets](sd-connect-delete.md) from your project independently in SD Connect. However, when a data permit expires, CSC will delete all files associated with the dataset from your project. The data will be deleted 90 days after the project in which the data users analyze the data is closed, which usually corresponds to the data permit's expiration date. However, if the project is closed earlier, the data will be removed regardless of whether the data permit remains valid. CSC, as the service provider of the processing environment, removes the data in accordance with the regulations and CSC's data retention policy (see [General Terms of Use for CSC's Services for Research and Education](https://research.csc.fi/general-terms-of-use)).

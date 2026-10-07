[Table of contents of user guide :material-arrow-right:](sd-services-toc.md)

# Uploading secondary use health and social data for research use via SD Connect

## Use case

Your organisation has issued a data permit for a research group to process health and social data under the Secondary Use Act. You need to deliver the dataset to SD Desktop environment for the users.

!!! Note 
    - Before any data can be made available for researchers in the Sensitive Data services, you need to confirm that the necessary legal agreements are in place between the data controller and CSC.
    - The register dataset must always be uploaded in collaboration with the CSC Sensitive Data (SD) services team.
    - You can start a conversation with the SD services team by sending a message to the [CSC Service Desk](../../support/contact.md) (subject: Sensitive Data).

## Solution

1. [Create or apply for a CSC account](#1-create-or-apply-for-a-csc-account)
2. [Join a CSC project](#2-join-a-csc-project)
3. [Login to SD Connect](#3-login-to-sd-connect)
4. [Upload each dataset to a dedicated bucket](#4-upload-each-dataset-to-a-dedicated-bucket)
5. [Manage datasets](#5-manage-datasets)

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

- The SD services team adds you to a CSC project that is created specifically for data transfers from your organisation.
- Check your email for a notification and log in to MyCSC to find the project.

---

### 3. Login to SD Connect

Now all the preparations are ready and you can start using SD Connect service. Below you'll find links to related user guide:

- [SD Connect overview and key features](sd_connect.md)
- [SD Connect login instructions](sd-connect-login.md)

---

### 4. Upload each dataset to a dedicated bucket

The SD services team will create a bucket in SD Connect for each dataset, share the bucket name with you, and share the bucket for Read-only access to the user's project. Each bucket will contain only one dataset, i.e. all data under the same data permit, and a bucket will be created for each dataset based on the data permit. Users create their projects based on data permits and can access the data only on the isolated virtual machines under that project.

Follow these instructions to upload data to the bucket:

- [Upload and encrypt files to an existing bucket](sd-connect-upload.md#24-upload-and-encrypt-files-to-an-existing-bucket)
- [SD Connect command line tool for large datasets (over 50 GB)](sd-connect-command-line-interface.md)

---

### 5. Manage datasets

The datasets will remain in your control after they are uploaded to the buckets and shared to the users' projects. You can upload more data, remove files, and also remove the data access from the users anytime during the project lifetime.

1. **Delivering additional data**: You can add data for a project by [uploading new files to the bucket](#4-upload-each-dataset-to-a-dedicated-bucket) created for the data permit. Remember to use unique file names to avoid overwriting the old files.
2. **Removing corrupted or incorrect files**: You can remove data from the bucket by [deleting the files](sd-connect-delete.md). NOTE! If the users are no longer allowed to use these files in their analysis, you need to also request that they remove any possible working copies of the files from their SD Desktop environment.
4. **Cancelling the data access**: You can terminate the data access any time by [removing the sharing of the bucket](sd-connect-share.md#4-delete-sharing-permission) and/or [deleting the data files](sd-connect-delete.md).

!!! Note 
    CSC will remove the datasets from SD Connect after the data permit has expired. The data will be removed from your project after 90 days from the user's project's closing date in accordance with the legislation and CSC’s data retention policy (see [General Terms of Use for CSC's Services for Research and Education](https://research.csc.fi/general-terms-of-use)).

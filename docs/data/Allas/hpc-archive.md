# How to access old HPC-archive data


## HPC-archive is closed

HPC-archive service was used in Sisu and Taito supercomputers to provide storage space for back-ups and long term data storage.
In these servers HPC-archive was used with iRODS commands like `iput` and `iget`.

As these supercomputers are now phased out, also HPC-archive has been closed. 
If HPC-archive contained some data that you want to preserve, the data can 
be made available in the Allas object storage environment. However, you should act now as the HPC-archive 
data will not be available after year 2020.

## Allas access is needed

To get access to your HPC-archive data, you need a CSC computing project 
that has access to [Allas storage service](./index.md).

You can use an existing CSC project or establish a new one. You 
don’t need to be the manager of the project that you will use for 
preserving your HPC-archive data. Note however, that all members of the Allas 
project will have access to your data.

You can check your current projects and services in the CSC customer portal:

*    [my.csc.fi](https://my.csc.fi)

Instructions for creating a project can be found here:

*    [Opening a new project](./../../accounts/how-to-create-new-project.md)
*    [Adding services to a project](./../../accounts/how-to-add-service-access-for-project.md)

## What to do

To start the migration process send a request to [ServiceDesk](mailto:servicedesk@csc.fi)  
The request should contain information about:

1. Your CSC user account.
2. Name of the project that you will use to host your HPC-archive data

**Please use your organizational e-mail address when you send the request**. 
Once the request is processed, you will get information about the Allas bucket 
that contains your HPC-archive data. This bucket is added to your Allas project. 
It will use the storage quota and billing units of your project just like any 
other data stored in Allas.


## Using HPC-archive data in Allas

The name of the bucket where your HPC-archive data is re-located starts with string `hpca-` followed 
by a random string. For example: `hpca-3ac9tfacfe8656ajad47b74495f42c54`.

The data has been transferred into this bucket using S3 protocol. In Puhti, Allas is used by default 
with a different protocol (Swift) and therefore the `hpca-`bucket requires some extra steps and settings.

First, when you connect the Allas area of your project, you should open the connection with both _Swift_ and _S3_ protocols.
This is done with command:
```text
allas-conf --mode both
```
After that you can access your Allas data with both protocols. 

In case of `hpca-` buckets the data can be downloaded with `s3cmd` command:
```text
s3cmd get s3://hpca-some_rand_string/file_name local_file_name
```
You can use `a-get` too, but in that case you need to add option `--s3cmd`  to the command.
```text
a-get --s3cmd hpca-some_rand_string/file_name
```
If you want to move some file from `hpca-` bucket to some another bucket, it is recommended 
that you first download the object to the scratch area of Puhti and then upload the data with
normal _a-put_ or _rclone_ commands to Allas:

```text
a-get --s3cmd hpca-some_rand_string/file_name
a-put file_name -b bucket-to-upload
```
This way the data is converted form S3 protocol to Swift protocol and it can be used with the normal Allas-commands in Puhti.


# Using Allas and Lumi-O from LUMI supercomputer

In this document we describe how you can install commonly used object storage clients 
to LUMI-C and how to configure connection to Allas object storage services. 

## Using Allas from Lumi supercomputer

In Lumi-C you can set up connection to Allas with commands:

```text
module use /appl/local/csc/modulefiles
module load allas
allas-conf
```
After that Allas can be accessed in the same ways as from Puhti and Mahti. The available 
command line tools include:

*   a-commmands
*   allas-backup
*   rclone
*   swift
*   s3cmd
*   restic

## Using Lumi-O with Allas tools

The tools provided by [allas-cli-utils](https://github.com/CSCfi/allas-cli-utils/) can be used to upload and download data from
Lumi-O. Running command _allas-conf_ in Puhti, Mahti or Lumi starts normal configuration process for a swift based connetion to Allas:

```text
allas-conf
```

If you want to configure connetion Lumi-O instead of Allas you must add option _--lumi_ to the command:
```text
allas-conf --lumi
```
If you have allas-cli-utils installed in your local environment, the configuration command would be something like:
```text
source allas-cli-utils/allas_conf --lumi
```

The cofiguration process asks you to connect with your browser to Lumi-O configuration sever, create credentials there and then copy the project number and keys for the setup tool. The setup process for Lumi-O will create environment variables needed for _S3_ command and confuguration files for _s3cmd_ and _rclone_. In addition you can define that _a-commands_ will use by default Lumi-O storage server in stead of Allas. After that commands like _a-list_, _a-put_ or _a-get_ will use your Lumi-O storage. If you don't set Lumi-O as the default storage service, you can add option _--lumi_ to a-commands to use Lumi-O instead of Allas. 

For _rclone_,  Lumi-O configuration provides two _rclone remotes_: _lumi-o:_ and _lumi-pub:_ . The buckets used by _lumi-pub_ will be publicly visible in URL: https://_project-number_.lumidata.eu/_bucket_name_.

Note, that you can have active connection to both Lumi-O and Allas in the same time.

For example, if you would first open Allas connection with command:

```text
allas-conf
```
And then open Lumi-O connection with:
```text
allas-conf --lumi
```
(when running the latter command we accept that Lumi-O will be the default erver for a-commands)
Now you can list the buckets available in Lumi-O with commands:

```text
a-list
```
or 
```text
rclone lsd lumi-o:
```
And in the same time you can list your buckets in Allas with commands:

```text
a-list --allas
```
or 
```text
rclone lsd allas:
```

Copying data from Allas to Lumi-O could now be done with command:

```text
rclone copyto -P allas:bucket-in-allas/object lumi-o:bucket-in-lumi-o/object
```
The command above will work only for files smaller than 5 GB.


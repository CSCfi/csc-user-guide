# Using Allas and LUMI-O from LUMI supercomputer

In this document we describe how you can install commonly used object storage clients 
to LUMI and how to configure connection to Allas object storage services. 

## Using Allas from LUMI supercomputer

In LUMI you can set up connection to Allas with commands:

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

## Using LUMI-O with Allas tools

The tools provided by [allas-cli-utils](https://github.com/CSCfi/allas-cli-utils/) can be used to upload and download data from
LUMI-O. Running command `allas-conf` in Puhti, Mahti or LUMI starts a normal configuration process for a swift based connection to Allas:

```text
allas-conf
```

If you want to configure connection to LUMI-O instead of Allas you must add option `--lumi` to the command:

```text
allas-conf --lumi
```

If you have allas-cli-utils installed in your local environment, the configuration command would be something like:

```text
source allas-cli-utils/allas_conf --lumi
```

The configuration process asks you to connect with your browser to LUMI-O configuration sever, create credentials there and then copy the project number and keys for the setup tool. The setup process for LUMI-O will create environment variables needed for _S3_ command and configuration files for `s3cmd` and `rclone`. In addition you can define that `a-commands` will use by default LUMI-O storage server instead of Allas. After that commands like `a-list`, `a-put` or `a-get` will use your LUMI-O storage. If you don't set LUMI-O as the default storage service, you can add option `--lumi` to a-commands to use LUMI-O instead of Allas. 

For `rclone`,  LUMI-O configuration provides two _rclone remotes_: _lumi-o:_ and _lumi-pub:_. The buckets used by _lumi-pub_ will be publicly visible in URL: `https://<project-number>.lumidata.eu/<bucket_name>`.

Note that you can have an active connection to both LUMI-O and Allas at the same time.

For example, if you would first open Allas connection with command:

```text
allas-conf
```

And then open LUMI-O connection with:

```text
allas-conf --lumi
```

(When running the latter command we accept that LUMI-O will be the default server for a-commands.)

Now you can list the buckets available in LUMI-O with commands:

```text
a-list
```

or 

```text
rclone lsd lumi-o:
```

And at the same time you can list your buckets in Allas with commands:

```text
a-list --allas
```

or 

```text
rclone lsd allas:
```

Copying data from Allas to LUMI-O could now be done with command:

```text
rclone copyto -P allas:bucket-in-allas/object lumi-o:bucket-in-lumi-o/object
```

The command above will work only for files smaller than 5 GB.

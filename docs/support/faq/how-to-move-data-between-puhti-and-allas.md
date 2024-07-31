# How to move data from Puhti to Allas and vice versa?

There are several options for moving data between Puhti and Allas. This page
summarizes how to move data using _a-commands_, _Swift_, _Rclone_ and _S3cmd_
clients.

All the required packages and software needed for the clients are already
installed on Puhti. To activate Allas and authenticate to a project you need to
run the commands:

```bash
module load allas
allas-conf
```

## Move data with a-commands

[a-commands](../../data/Allas/using_allas/a_commands.md) are easy-to-use tools
for basic usage of Allas. The main commands to use for moving data between
Puhti and Allas are:

* [`a-put`](../../data/Allas/using_allas/a_commands.md#a-put-uploads-data-to-allas):
  Move data from Puhti to Allas
* [`a-get`](../../data/Allas/using_allas/a_commands.md#a-get-retrieves-stored-data):
  Move data from Allas to Puhti 

## Move data with Swift

The Swift client provides the options `upload` and `download` for moving data:

```bash
swift upload <bucket name> <file name>
```

```bash
swift download <bucket name> <file name>
```

For more information, see
[Swift client](../../data/Allas/using_allas/swift_client.md).

## Move data with Rclone

Rclone is another client using which you can move data between Puhti and
Allas. For example, you could create a bucket called `2000620-raw-data` in
Allas using the command:

```bash
rclone mkdir allas:2000620-raw-data
```

Uploading a file called `file.dat` to that bucket can be done using the
`rclone copy` command:

```bash
rclone copy file.dat allas:2000620-raw-data/
```

Downloading the file back to Puhti is done with the same `rclone copy` command:

```bash
rclone copy allas:2000620-raw-data/file.dat .
```

!!! info "Note"
    Another destination directory can be specified in the `rclone copy` command
    as well. If this directory does not exist, Rclone will create it for you.

    ```bash
    rclone copy allas:2000620-raw-data/file.dat my-new-folder
    ```

For more information, see
[Using Allas with Rclone from Puhti](../../data/Allas/using_allas/rclone.md).

## Move data with S3cmd

For moving data between Puhti and Allas,
[S3cmd](../../data/Allas/using_allas/s3_client.md) provides the functions:

* [`s3cmd put`](../../data/Allas/using_allas/s3_client.md#create-buckets-and-upload-objects):
  Move data from Puhti to Allas

* [`s3cmd get`](../../data/Allas/using_allas/s3_client.md#download-objects-and-buckets):
  Move data from Allas to Puhti

For more information, see
[S3 client](../../data/Allas/using_allas/s3_client.md).

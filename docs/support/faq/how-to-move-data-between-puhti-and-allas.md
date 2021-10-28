# How to move data from Puhti to Allas and vice versa?

There are several options on how to move your data between Puhti and Allas. This page gives you guidance for the data movement with clients <i>a-commands</i>, _swift_, _rclone_ and _s3cmd_.

All the required packages and software needed for the clients are already installed on Puhti. To authenticate to a project you need to run command `source /appl/opt/allas_conf`.

## Move data with a-commands

[a-commands](../../data/Allas/using_allas/a_commands.md){target="_blank"} provides easy-to-use tools for basic usage of Allas. The functions to use for data movement between Puhti and Allas are:

* [a-put](../../data/Allas/using_allas/a_commands.md#a-put-uploads-data-to-allas){target="_blank"}: Move data from Puhti to Allas
* [a-get](../../data/Allas/using_allas/a_commands.md#a-get-retrieves-stored-data){target="_blank"}: Move data from Allas to Puhti 

## Move data with Swift

_Swift client_ provides functions _upload_ and _download_ for data movement:

```bash
swift upload <bucket name> <file name>
```
```bash
swift download <bucket name> <file name>
```
For more information, see [Swift client](../../data/Allas/using_allas/swift_client.md){target="_blank"}.

## Move data with rclone

Also, with client _rclone_ you can move data between Puhti and Allas. Creating a bucket called _2000620-raw-data_ to Allas can be done with command:

```bash
rclone mkdir allas:2000620-raw-data
```

Uploading a file called _file.dat_ to that bucket can be done with command `rclone copy`:

```bash
rclone copy file.dat allas:2000620-raw-data/
```

Downloading the file back to Puhti is done with the same `rclone copy` command:

```bash
rclone copy allas:2000620-raw-data/file.dat
```

**Note:** If you give a destination parameter name in the download command, rclone creates a directory where the download goes:

```bash
rclone copy allas:2000620-raw-data/file.dat doh
```

For further guidance for using rclone with Allas from Supercomputers, see [Using Allas with rclone from Puhti](../../data/Allas/using_allas/rclone.md){target="_blank"}.

## Move data with s3cmd

For data movement between Puhti and Allas [s3cmd](../../data/Allas/using_allas/s3_client.md){target="_blank"} provides functions:

* [put](../../data/Allas/using_allas/s3_client.md#create-buckets-and-upload-objects){target="_blank"} move data from Puhti to Allas

* [get](../../data/Allas/using_allas/s3_client.md#download-objects-and-buckets){target="_blank"}: move data from Allas to Puhti

More examples of using s3cmd from Supercomputers can be found [here](../../data/Allas/using_allas/s3_client.md){:target="_blank"}.

#How to move data from Puhti to Allas and vice versa?


There are several options how to move your data between Puhti and Allas. This page gives guidance for the clients: <i>a_commands</i>, _swift_, _rclone_ and _s3cmd_.

##Move data with a_commands

[a_commands](../../data/Allas/using_allas/a_commands.md){:target="_blank"} provides easy-to-use tools for basic usage of Allas. The functions to use for data movement between Puhti and Allas are:

* [a_put](../../data/Allas/using_allas/a_commands.md#a_put-uploads-data-to-allas){:target="_blank"}: Move data from Puhti to Allas

* [a_get](../../data/Allas/using_allas/a_commands.md#a_get-retrieves-the-stored-data){:target="_blank"}: Move data to Puhti from Allas


##Move data with Swift

_Swift client_ provides functions _upload_ and _download_ for data movement:

```bash
$ swift upload <bucket name> <file name>
```
```bash
$ swift download <bucket name> <file name>
```
For more information, see [Swift client](../../data/Allas/using_allas/swift_client.md){:target="_blank"}.


##Move data with rclone

Also with client _rclone_ you can move data between Puhti and Allas. Creating a bucket called _2000620-raw-data_ to Allas happens with command:

```bash
rclone mkdir allas:2000620-raw-data
```

Uploading a file called _file.dat_ to that bucket can be done with command _copy_:

```bash
rclone copy file.dat allas:2000620-raw-data/
```

Downloading the file back to Puhti happens with the same _copy_ command:

```bash
rclone copy allas:2000620-raw-data/file.dat
```

**Note:** If you give a destination parameter name in the download command, rclone creates a directory where the download goes:

```bash
rclone copy allas:2000620-raw-data/file.dat doh
```

For further guidance for using rclone with Puhti and Allas see [Using Allas with rclone from Puhti and Taito](../../data/Allas/using_allas/rclone.md){target="_blank"}


##Move data with s3cmd

For data movement between Puhti and Allas [s3cmd](../../data/Allas/using_allas/s3cmd.md){target="_blank"} provides functions:

* [put](../../data/Allas/using_allas/s3cmd.md#s3cmd-put){:target="_blank"}: move data from Puhti to Allas

* [get](../../data/Allas/using_allas/s3cmd.md#s3cmd-get){:target="_blank"}: move data to Puhti from Allas



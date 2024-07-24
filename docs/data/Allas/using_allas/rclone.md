# Using Allas with Rclone 

This chapter contains instructions for using Allas with [Rclone](https://rclone.org/) in the Puhti and Mahti computing environments. _Rclone_ provides a very powerful and versatile way to use Allas and other object storage services. It is able to use both the S3 and Swift protocols (and many others). At the moment, the Swift protocol is the default option on the CSC servers. 

> **WARNING:** Rclone should not be used to copy, move or rename objects **inside** Allas. Rclone provides commands for these operations but they don't work correctly for files larger than 5 GB.
> 
> **WARNING:** If a rclone data upload process for a over 5 GB file gets interrupted, please remove the partially uploaded object before restarting the upload process. Otherwise rclone sometimes reports a successful data upload even though not all data has been copied to Allas.



The basic syntax of Rclone:
<pre>
rclone <i>subcommand options source:path dest:path</i> 
</pre>

The most frequently used Rclone commands:

*    [rclone copy]( https://rclone.org/commands/rclone_copy/) – Copy files from the source to the destination, skipping what has already been copied.
*    [rclone sync](https://rclone.org/commands/rclone_sync/) – Make the source and destination identical, modifying only the destination.
*    [rclone move](https://rclone.org/commands/rclone_move/) – Move files from the source to the destination.
*    [rclone delete](https://rclone.org/commands/rclone_delete/) – Remove the contents of a path.
*    [rclone mkdir](https://rclone.org/commands/rclone_mkdir/) – Create the path if it does not already exist.
*    [rclone rmdir](https://rclone.org/commands/rclone_rmdir/) – Remove the path.
*    [rclone check](https://rclone.org/commands/rclone_check/) – Check if the files in the source and destination match.
*    [rclone ls](https://rclone.org/commands/rclone_ls/) – List all objects in the path, including size and path.
*    [rclone lsd](https://rclone.org/commands/rclone_lsd/) – List all directories/containers/buckets in the path.
*    [rclone lsl](https://rclone.org/commands/rclone_lsl/) – List all objects in the path, including size, modification time and path.
*    [rclone lsf](https://rclone.org/commands/rclone_lsf/) – List the objects using the virtual directory structure based on the object names.
*    [rclone cat](https://rclone.org/commands/rclone_cat) – Concatenate files and send them to stdout.
*    [rclone copyto](https://rclone.org/commands/rclone_copyto/) – Copy files from the source to the destination, skipping what has already been copied.
*    [rclone moveto](https://rclone.org/commands/rclone_moveto/) – Move the file or directory from the source to the destination.
*    [rclone copyurl](https://rclone.org/commands/rclone_copyurl/) – Copy the URL's content to the destination without saving it in the tmp storage.

A more extensive list can be found on the [Rclone manual pages](https://rclone.org/docs/) or by typing the command `rclone` in Puhti.

## Authentication 

The first step is to authenticate to a project in Allas. Rclone can use both Swift and S3 protocols but these connections will have different names in rclone commands. 

In this document we describe how Rclone is used in CSC computing environment (Puhti and Mahti). You can use rclone also in your local computer. Instructions of configuring locally installed Rclone are here

   * [Local Rclone configuration for Allas](./rclone_local.md)


### Rclone with swift on CSC supercomputers

The default protocol of Allas is Swift. In Puhti and Mahti Swift based Allas connection is activated  with commands:
```text
module load allas
allas-conf
```
The `allas-conf` command asks for your CSC password (University/Haka password will not work here). It lists
your projects in Allas and asks you to define the project that will be used. Then _allas-conf_ generates a Rclone configuration file for the Allas service and authenticates the connection to the selected project. In Rclone command this swift based connection is referred with remote name `allas:`. The authentication information is stored in the shell variables `OS_AUTH_TOKEN` and `OS_STORAGE_URL` that are valid for up to eight hours. However, you can refresh the authentication at any time by running _allas-conf_ again. The environment variables are available only for that login session, so if you login to Puhti in another session, you need to authenticate again to access Allas.

### Rclone with S3 on CSC supercomputers

If you want to use Allas with the S3 protocol instead, run the `allas-conf` command with the `--mode S3` option.
```text
module load allas
allas-conf --mode S3
```
This command opens permanent S3 based connection to Allas. Rclone can now refer to this connection with remote name `s3allas:`.
In the examples below the swift based `allas:` remote definition is used, but if you have S3 connection defined, you could replace it
with `s3allas:`. Note that you can have both `allas:` and `s3allas:` functional in the same time and that they can still use different Allas projects. However, you should avoid mixing protocols. If an object is loaded using `allas:` do also all operations with `allas:`.  

## Create buckets and upload objects

The data in Allas is arranged into containers called buckets. You can consider them as root-level directories. All buckets in Allas must have unique names – you cannot create a bucket if some other project has already used that bucket name. It is a good rule of thumb to have something project- or user-specific in the bucket name, e.g. _2000620-raw-data_. See the [checklist](../introduction.md#naming-buckets) for how to name a bucket.

In the case of _Rclone_, create a bucket:
```text
rclone mkdir allas:2000620-raw-data
```
Upload a file using the command ```rclone copy```:
```text
rclone copy file.dat allas:2000620-raw-data/
```
The command above creates an object _file.dat_ in the bucket _2000620-raw-data_.
If you use `rclone move` instead of `rclone copy`, the local version of the uploaded file (file.dat)
is deleted after copying.

The _copy_ and _move_ subcommands only work with files. If you would like to copy all files in a directory, use the _copyto_ or _moveto_ subcommands.

During upload, files that are larger than 5 GB will be split and stored as several objects. The objects are stored automatically in a distinct bucket called `<bucket-name>_segments`. For example, if you would upload a large file to  `2000620-raw-data`, the actual data would be stored in several pieces in the bucket `2000620-raw-data_segments`. The target bucket (`2000620-raw-data`) would contain just a manifest object stating which segments comprise the stored file. Operations performed on the manifest object are automatically reflected in the segments. Normally users don't need to operate with the segments buckets at all, and objects inside these buckets should not be deleted or modified.

## List buckets and objects

List all the buckets belonging to a project:
<pre><b>rclone lsd allas:</b>
0 2019-06-06 14:43:40         0 2000620-raw-data
</pre>

List the content of a bucket: 
<pre><b>rclone ls allas:2000620-raw-data</b>
677972 file.dat
</pre>

## Download objects

Use the same `rclone copy` and `rclone copyto` commands to download a file:
```text
rclone copy allas:2000620-raw-data/file.dat
```

If you include a destination parameter in the download command, Rclone creates a directory for the download:
```text
rclone copy allas:2000620-raw-data/file.dat doh
```

<pre><b>ls doh</b>
file.dat</pre>

<pre><b>ls -ld doh</b>
drwxr-xr-x  3 user  staff  96 Jun  6 14:58 doh
</pre>

## Synchronizing a directory

One way of moving data between Allas and the computing environment is synchronization. The difference between copying and synchronizing is that while copying only adds new objects or files from the source to the destination, synchronization can also remove data from the destination, in order to make the destination match the source. This feature makes synchronization very effective but also potentially very dangerous.

For example, a folder named _mydata_ has the following structure:
<pre>
<b>ls -R mydata</b>

mydata/:
file1.txt  setA  setB

mydata/setA:
file2.txt

mydata/setB:
file3.txt  file4.txt
</pre>

An example of using _sync_ (note that the destination parameter requires the folder name (_mydata_)):

```text
rclone sync mydata allas:2000620-raw-data/mydata
```

<pre><b>rclone ls allas:2000620-raw-data</b>
   677972 mydata/file1.txt
    10927 mydata/setA/file2.txt
     1116 mydata/setB/file3.txt
     5075 mydata/setB/file4.txt
</pre>

Let us assume that we are storing new data (_file5.txt_ and _file6.txt_) in the subdirectory _mydata/setC_ and simultaneously removing the file _mydata/setB/file3.txt_. When the _rclone sync_ command is executed again, the new data is added to Allas and the object _mydata/setB/file3.txt_ is removed.

<pre><b>rclone sync mydata allas:2000620-raw-data/mydata</b>

<b>rclone ls allas:2000620-raw-data</b>
   677972 mydata/file1.txt
    10927 mydata/setA/file2.txt
     5075 mydata/setB/file4.txt
     1265 mydata/setC/file5.txt
     4327 mydata/setC/file6.txt
</pre>

In the examples above, Allas has been used as the destination that is changed. However, the command can be used in the reverse direction as well:
```text
rclone sync allas:2000620-raw-data/mydata mydata
```

This command returns the uploaded data from Allas to the _mydata_ directory. Note however that if you have added new data to _mydata_ after synchronizing the directory with Allas, this data will be erased.


 

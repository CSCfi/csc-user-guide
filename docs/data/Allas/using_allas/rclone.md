# Using Allas with rclone from Puhti and Taito 

This chapter guides to use Allas with [rclone](https://rclone.org/) in Puhti or Taito computing environments. _rclone_ provides a very powerful and versatile way to use Allas and other object storage services. It is able to use both S3 and swift protocols (as well as many other protocols), but in the case of Allas, swift protocol is preferred and that is also the default option at CSC servers.

The basic syntax of rclone is
<pre>
rclone <i>subcommand optons source:path dest:path</i> 
</pre>

Below is a list of most frequently used rclone commands. You can check more extended list form the [Rclone manual pages]( https://rclone.org/docs/) or by typing command: `rclone` in Puhti or in Taito

*    [rclone copy]( https://rclone.org/commands/rclone_copy/)- Copy files from source to dest, skipping already copied.
*    [rclone sync](https://rclone.org/commands/rclone_sync/)- Make source and destination identical, modifying destination only.
*    [rclone move](https://rclone.org/commands/rclone_move/)- Move files from source to destination.
*    [rclone delete](https://rclone.org/commands/rclone_delete/)- Remove the contents of path.
*    [rclone mkdir](https://rclone.org/commands/rclone_mkdir/)- Make the path if it doesn’t already exist.
*    [rclone rmdir](https://rclone.org/commands/rclone_rmdir/)- Remove the path.
*    [rclone check](https://rclone.org/commands/rclone_check/)- Check if the files in the source and destination match.
*    [rclone ls](https://rclone.org/commands/rclone_ls/)- List all the objects in the path with size and path.
*    [rclone lsd](https://rclone.org/commands/rclone_lsd/)- List all directories/containers/buckets in the path.
*    [rclone lsl](https://rclone.org/commands/rclone_lsl/)- List all the objects in the path with size, modification time and path..
*    [rclone cat](https://rclone.org/commands/rclone_cat)/ - Concatenate any files and send them to stdout.
*    [rclone copyto](https://rclone.org/commands/rclone_copyto/) - Copy files from source to destination, skipping already copied.
*    [rclone moveto](https://rclone.org/commands/rclone_moveto/)- Move file or directory from source to destination.
*    [rclone copyurl](https://rclone.org/commands/rclone_copyurl/)- Copy urls content to destination without saving it in tmp storage.


## Authentication

The first step is to authenticate to a project in Allas. This can be done with commands:

```
module load allas
allas_conf
```

The `allas_conf` command above asks for your CSC password (the same that you use to login to CSC servers). After that it lists
your projects in Allas and asks you to define the project that will be used. After that _allas_conf_ generates rclone configuration file for Allas service and autheticates the connection to the selected project in Allas. The authentication information is stored into shell variables `OS_AUTH_TOKEN` and `OS_STORAGE_URL` that are valid for max 3 hours. Hoverver you can refresh the authentication at any time my running _allas_conf_ again. The environment variables are available only for that login session, so if you log into Puhti in another session, you need to authenticate again in there to access Allas.


## Create buckets and upload objects

Data in Allas is arranged into containers called buckets. You can simply think them as top level directories. All buckets in allas must have unique names  - you can not create a bucket if some other project has already used that bucket name. So it is a good rule of thumb to have something project or user specific in the bucket name, for instance: _2000620-raw-data_. See [checklist](../introduction.md#naming-buckets) for naming a bucket.

In the case of _rclone_ creating a bucket can be done with command:
```bash
rclone mkdir allas:2000620-raw-data
```
You can upload a file with command ```rclone copy```:
```bash
rclone copy file.dat allas:2000620-raw-data/
```
The command above creates object _file.dat_ in bucket _2000620-raw-data_.
If you you would use `rclone move` in stead of `rclone copy` the local version of the uploaded file (file.dat)
would be deleted after copying.

_copy_ and _move_ subcommands can only work with files. If you would like to copy all the files in directory, you 
should used _copyto_ or _moveto_ subcommands.


## List buckets and objects

You can list all the buckets belonging to the project:

```bash
$ rclone ls allas:
0 2019-06-06 14:43:40         0 2000620-raw-data
```

You can also list the content of a bucket: 

```bash
$ rclone ls allas:2000620-raw-data
677972 file.dat
```
&nbsp;

## Download objects

Downloading a file is done with the same `rclone copy` and `rclone copyto` commands:

```bash
rclone copy allas:2000620-raw-data/file.dat
```

If you give a destination parameter name in the download command, rclone creates a directory where the download goes:
```bash
rclone copy allas:2000620-raw-data/file.dat doh
```

```bash
$ ls doh
file.dat
```

```bash
$ ls -ld doh
drwxr-xr-x  3 user  staff  96 Jun  6 14:58 doh
```
&nbsp;

## Synchronizing a directory

One way of moving data between data Allas and computing environment is synchronization. The diffrerence between copying and synchronizing is that wile copying only adds new objects or files from source to the destination, synchronization can also remove data from the destination, in order to make the destination match the source. This feature makes synchronization very effective but also potentially very dangerous.

Consider a folder _mydata_  with the following structure:

```
$ ls -R mydata

mydata/:
file1.txt  setA  setB

mydata/setA:
file2.txt

mydata/setB:
file3.txt  file4.txt
```

An example of using sync (note that destination parameter needs the folder name _mydata_ at the end):

```bash
rclone sync mydata allas:2000620-raw-data/mydata
```

```
$ rclone ls allas:2000620-raw-data
   677972 mydata/file1.txt
    10927 mydata/setA/file2.txt
     1116 mydata/setB/file3.txt
     5075 mydata/setB/file4.txt
```
Now, let's assume that we got some new data (_file5.txt_ and _file6.txt_) that we stored to subdirectory _mydata/setC_ and in the same time remove file _mydata/setB/file3.txt_. When the same _rclone sync_ command is executed again, the new data is added to Allas and object _mydata/setB/file3.txt_ is removed.

```bash
rclone sync mydata allas:2000620-raw-data/mydata

rclone ls allas:2000620-raw-data
   677972 mydata/file1.txt
    10927 mydata/setA/file2.txt
     5075 mydata/setB/file4.txt
     1265 mydata/setC/file5.txt
     4327 mydata/setC/file6.txt
     
```
In the examples above Allas has been used as the destination that is changed. However the command can be used in the other direction too. Command:

```text
rclone sync mydata allas:2000620-raw-data/mydata mydata
```
Will bring the uploaded data back from Allas to _mydata_ directory. Note however that if you have added new data to _mydata_ after you have synchronizied the directory with Allas, this data will be erased.











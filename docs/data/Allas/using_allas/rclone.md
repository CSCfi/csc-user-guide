# Using Allas with rclone from Puhti and Taito 

This chapter guides to use Allas with [rclone](https://rclone.org/) in Puhti or Taito computing environments. _rclone_ provides a vere powerful and versatile way to use Allas and other object storage services. It is able to use both S3 and swift protocols (as well as many other protocols), but in the case of Allas, swift protocol is prefered and that is also the default option at CSC servers.

The basic syntax of rclone is
<pre>
rclone <i>subcommand optons source:path dest:path</i> 
</pre>

Below is a list of most frequently used rclone commands. You can check more extended list form the [Rclone manual pages]( https://rclone.org/docs/) or by typing command: `rclone` in Puhti or in Taito

*    [rclone copy]( https://rclone.org/commands/rclone_copy/)- Copy files from source to dest, skipping already copied.
*    [rclone sync](https://rclone.org/commands/rclone_sync/)- Make source and dest identical, modifying destination only.
*    [rclone move](https://rclone.org/commands/rclone_move/)- Move files from source to dest.
*    [rclone delete](https://rclone.org/commands/rclone_delete/)- Remove the contents of path.
*    [rclone mkdir](https://rclone.org/commands/rclone_mkdir/)- Make the path if it doesn’t already exist.
*    [rclone rmdir](https://rclone.org/commands/rclone_rmdir/)- Remove the path.
*    [rclone check](https://rclone.org/commands/rclone_check/)- Check if the files in the source and destination match.
*    [rclone ls](https://rclone.org/commands/rclone_ls/)- List all the objects in the path with size and path.
*    [rclone lsd](https://rclone.org/commands/rclone_lsd/)- List all directories/containers/buckets in the path.
*    [rclone lsl](https://rclone.org/commands/rclone_lsl/)- List all the objects in the path with size, modification time and path..
*    [rclone cat](https://rclone.org/commands/rclone_cat)/ - Concatenate any files and send them to stdout.
*    [rclone copyto](https://rclone.org/commands/rclone_copyto/) - Copy files from source to dest, skipping already copied.
*    [rclone moveto](https://rclone.org/commands/rclone_moveto/)- Move file or directory from source to dest.
*    [rclone copyurl](https://rclone.org/commands/rclone_copyurl/)- Copy urls content to destination without saving it in tmp storage.


## Authentication

The first step is to authenticate to a project in Allas. This can be done with commands:

```
module load allas
allas_conf
```

The `allas_conf` command above asks for your CSC password (the same that you use to login to CSC servers). After that it lists
your projectc in Allas and ask you to define the project that will be used. After that _allas_conf_ generates rclone configuration file for Allas service and autheticates the connections to a selected project in Allas. The authentication information is stored into shell variables `OS_AUTH_TOKEN` and `OS_STORAGE_URL`. The authentication is valid for max 3 hours. Hoverver you can refrresh the authentication at any time my running _allas_conf_ again. The environment variables are available only for that login session, so if you log into Puhti in another session, you need to authenticate again in there to access Allas.


## Create buckets and upload objects

Data in Allas is arranged into containers called buckets. You can simply think them as top level directories. All buckets in allas must have unique names  - you can not create a bucket if some other project has already used that bucket name. So it is a good rule of thumb to have something project or user specific in the bucket name, for instance: _2000620-raw-data_. See [checklist](../introduction.md#naming_bucket) for naming a bucket.

In the case of _rclone_ creating a bucket can be done with command:
```bash
rclone mkdir allas:2000620-raw-data
```
You can upload a file with command ```rclone copy```:
```bash
rclone copy file.dat allas:2000620-raw-data/
```
The command above creates object _file.dat_ in bucket _2000620-raw-data_.

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

Downloading a file is done with the same ```rclone copy``` command:

```bash
rclone copy allas:2000620-raw-data/file.dat
```

**Note:** If you give a destination parameter name in the download command, rclone creates a directory where the download goes:
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

## Copy a directory

Copying a directory can be done using the `rclone copy` command or the `rclone sync` command. Consider a folder with the following structure:

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




# Using Allas with rclone from Puhti and Taito 

This chapter guides to use Allas with _rclone_ when you are logged in to Puhti computing environment. The first step is to authenticate to a project in Allas.

```
source /appl/opt/allas_conf
```

The command above generates and stores authentication information into shell variables `OS_AUTH_TOKEN` and `OS_STORAGE_URL`. The authentication is valid for max 3 hours. **Note:** The environment variables are available only for that login session, so if you log into Puhti in another session, you need to authenticate again in there to access Allas.

Data in Allas is arranged into containers called buckets. You can simply think them as top level directories. The only drawback of buckets is that they must have unique names - you can not create a bucket if some other project has already used that bucket name. So it is a good rule of thumb to have something project or user specific in the bucket name, for instance: _2000620-raw-data_. See [checklist](../introduction.md#naming_bucket){:target="_blank"} for naming a bucket.

Guidance for using rclone with Allas is given below.
&nbsp;

## Create buckets and upload objects

Creating a bucket can be done with command:
```
$ rclone mkdir allas:2000620-raw-data
```

Upload a file with command _copy_:
```
$ rclone copy file.dat allas:2000620-raw-data/
```
&nbsp;

## List buckets and objects

You can list all the buckets belonging to the project:

```
$ rclone ls allas:
0 2019-06-06 14:43:40         0 2000620-raw-data
```

You can also list the content of a bucket: 

```
$ rclone ls allas:2000620-raw-data
677972 file.dat
```
&nbsp;

## Download objects

Downloading a file is done with the same _copy_ command:

```
$ rclone copy allas:2000620-raw-data/file.dat
```

**Note:** If you give a destination parameter name in the download command, rclone creates a directory where the download goes:
```
$ rclone copy allas:2000620-raw-data/file.dat doh

```

```
$ ls doh
file.dat
```

```
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
$ rclone sync mydata allas:2000620-raw-data/mydata
```

```
$ rclone ls allas:2000620-raw-data
   677972 mydata/file1.txt
    10927 mydata/setA/file2.txt
     1116 mydata/setB/file3.txt
     5075 mydata/setB/file4.txt
```




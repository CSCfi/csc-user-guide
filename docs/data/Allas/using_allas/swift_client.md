# The Swift client

The Python Swift client is a command line tool for using object storage systems such as Allas. If you use Allas on Puhti or Mahti, all required packages and software are already installed.
```text
module load allas

```
Open a connection to Allas:
```text
allas-conf
```

The _allas-conf_ command above asks for your CSC password (the same that you use to login to CSC servers). It lists your projects in Allas and asks you to define the project that will be used. _allas-conf_ generates and authenticates the connection to the selected project in Allas. The authentication information is stored in the shell variables *OS_AUTH_TOKEN* and *OS_STORAGE_URL* that are valid for up to eight hours. However, you can refresh the authentication at any time by running _allas-conf_ again. The environment variables are available only for that login session. If you open another session, you need to authenticate again to access Allas.

This chapter includes instructions for the following operations:

| Swift command | Function |
| :---- | :---- |
| post | Create a bucket |
| upload | Upload an object |
| list | List objects and buckets |
| download | Download objects and buckets |
| copy | Move object |
| delete | Remove objects or bucket |
| download --all | Download whole project |
| delete --all | Remove whole project |
| md5sum | Get the checksum |
| stat | View metadata |
| stat --meta | Add metadata |
| tempurl | Create a temporary URL |
| post -r, -w, --read-acl | Manage access rights |
| upload --use-slo | Upload files larger than 5 GB |

You can also install and use Swift outside the CSC computing environment. Make sure that your Swift version is not outdated, since the older Swift versions might not work with Allas.

## Create buckets and upload objects

Create a new empty bucket:
```text
swift post <new_bucket_name>
```

Create a new bucket and add a file to it:
```text
swift upload <new_bucket_name> <file_name>
```

Add a file to an existing bucket:
```text
swift upload <old_bucket_name> <file_name>
```
**Note:** This might trigger the warning  "_409 Conflict: BucketAlreadyExists_", but that does not necessarily mean that the upload has failed. 
If the next line displays the file name, the file was successfully uploaded to the existing bucket.

```text
$ swift upload my_fishbucket my_fish.jpg
Warning: failed to create container 'my_fishbucket': 409 Conflict: BucketAlreadyExists
my_fish.jpg
```

## List objects and buckets

List all buckets belonging to a project:
```text
$ swift list
my_fishbucket
my_bigfishes
```
List the content of a bucket:
```text
$ swift list my_fishbucket
my_fish.jpg
salmon.jpg
bass.png
```

## Download objects and buckets

Download an object:
```text
swift download <bucket_name> <file_name>
```
If you want to rename the object as you download it, you can include *-o new_name* in the end of the command:
```text
swift download <bucket_name> <file_name> -o <new_name>
```
Download an entire bucket:
```text
swift download <bucket_name>
```

## Move objects

You can copy data from one bucket to another using the command `swift copy`. The command below copies _file.txt_ from _bucket1_ to _bucket2_.
```text
swift copy --destination /bucket2 bucket1 file.txt
```
**Note:** If there is no bucket called _bucket2_, Swift creates a new bucket with that name. However, even if there is a bucket called _bucket2_, Swift claims that it created a new one, even though it simply copied the file to the existing bucket:
```text
$ swift copy --destination /other_bucket my_bigfishes bigfish.jpg
created container other_bucket
my_bigfishes/bigfish.jpg copied to /other_bucket/bigfish.jpg
$ swift list other_bucket
bigfish.jpg
other_file.txt
```

Rename a file while copying it:
```text
$ swift copy --destination /new_bucket/newname.jpg my_fishbucket my_fish.jpg
created container new_bucket
my_fishbucket/my_fish.jpg copied to /new_bucket/newname.jpg
```

For further information about the command _swift copy_, see the [OpenStack documentation](https://docs.openstack.org/python-swiftclient/latest/cli/index.html#swift-copy).

## Remove objects and buckets

Remove objects and buckets using the command `swift delete`:
```text 
swift delete <bucket_name> <object_name>
```
For example:
```bash
$ swift delete my_fishbucket useless_fish.jpg
useless_fish.jpg
```

Unlike with the web client and s3cmd, with Swift, you can **delete an entire bucket at once**:
```text
swift delete <my_old_bucket>
```
For example:
```text
$ swift delete old_fishbucket
old_fish.png
useless_salmon.jpg
too_tiny_bass.jpg
$ swift list old_fishbucket
Container u'old_fishbucket' not found
```
**Please note:** This deletes the bucket permanently, and the data is lost. Before using this command, make sure you do not need the data anymore or that you have a copy of the data.

## Download or delete projects

Download the entire project:
```text
swift download --all
```

Delete the entire project:
```text
swift delete --all
```
**Please note:** Be careful with this command since it deletes the entire content of the project. Before using this command, make sure you do not need the data anymore or that you have a copy of the data.

## Pseudo folders and checksums

In case you want to observe whether an object has changed, use [checksum](../terms_and_concepts.md#checksum) with the command ```md5sum```.

Pseudo folders can be handled by adding the name of the pseudo folder in front of the file name: <i>my_pseudo_folder_name/my_file</i>

Create a pseudo folder named _pictures_ in the bucket <i>my_bigfishes</i> and add the object _bass.png_ to it:
```text
$ swift upload my_bigfishes/pictures bass.png
pictures/bass.png
```

The example below uploads a file called _salmon.jpg_ to the pseudo folder called _fishes_ inside the bucket _my_fishbucket_. The file is then downloaded.
```text
$ md5sum salmon.jpg
22e44aa2b856e4df892b43c63d15138a  salmon.jpg
$ swift upload my_fishbucket/fishes salmon.jpg
fishes/salmon.jpg
$ swift list my_fishbucket
fishes/salmon.jpg
my_fish.jpg
$ swift download my_fishbucket fishes/salmon.jpg -o my_renamed_salmon.jpg
fishes/salmon.jpg [auth 0.664s, headers 0.925s, total 0.969s, 3.605 MB/s]
$ md5sum my_renamed_salmon.jpg
22e44aa2b856e4df892b43c63d15138a  my_renamed_salmon.jpg
```
**Note:** The checksums of the object <i>salmon.jpg</i> and the renamed version <i>my_renamed_salmon.jpg</i> are the same since the file is the same and has not changed. 

## Managing metadata

Define metadata for an object:
```text
swift post my_fishbucket my_fish.jpg --meta foo:bar
```

Display details about a bucket:
```text
$ swift stat my_fishbucket
                      Account: AUTH_$PROJECT_UUID
                    Container: my_fishbucket
                      Objects: 4
                        Bytes: 2162342
                     Read ACL:
                    Write ACL:
                      Sync To:
                     Sync Key:
                Accept-Ranges: bytes
                   X-Trans-Id: txUUID-cpouta-production-kaj
             X-Storage-Policy: default-placement
X-Container-Bytes-Used-Actual: 1167360
                  X-Timestamp: 1516776076.95812
```

Set a bucket as read-only to the world (make the content visible at the URL: <i>a3s.fi/bucket_name/object_name</i>) instead of the default (private to the project):
```text
swift post my_fishbucket --read-acl ".r:*"
```

Find more information about access management in the section [Giving another project read and write access to a bucket](#giving-another-project-read-and-write-access-to-a-bucket).

More details about a file:
```text
$ swift stat my_fishbucket fishes/salmon.jpg
         Account: AUTH_$PROJECT_ID
       Container: my_fishbucket
          Object: fishes/salmon.jpg
    Content Type: image/jpeg
  Content Length: 63220
   Last Modified: Wed, 24 Jan 2018 10:17:03 GMT
            ETag: a38f8db198e3fea43c83c465ffb0283b
Meta S3Cmd-Attrs: atime:1516788402/ctime:1513681753/gid:$LOCALGID/gname:$LOCALGROUP/md5:a38f8db198e3fea43c83c465ffb0283b/mode:33188/mtime:1513681747/uid:$LOCALUID/uname:$LOCALUSER
   Accept-Ranges: bytes
     X-Timestamp: 1516789023.84380
      X-Trans-Id: tx0000000000000000001d6-q-q-cpouta-production-kaj
```

Note that the above file was uploaded with the _s3cmd client_, and therefore there is the additional metadata _S3Cmd-Attrs_ compared to a file uploaded with Swift or S3. _ETag_ is the _hash_ when viewing the file details in the Pouta dashboard.

## Giving another project read and write access to a bucket

Give the project _project1_ read rights to the bucket <i>my_fishbucket</i>:
```text
swift post my_fishbucket -r "project1:*"
```

Write access can be given similarly by replacing _-r_ (_read_) with _-w_ (_write_):
```text
swift post my_fishbucket -w "project1:*"
```

The character _*_ after the project name defines that all project members in the project gain the rights.

Alternatively, you can give read and write access only to certain members of another project:
```text
swift post my_fishbucket -r "project2:member1"
swift post my_fishbucket -w \
   "project3:member1,project3:member2,project5:member1,project6:*"
```

**Please note:** If you have granted access for specific projects, making the shared project public and private again will remove any previous access permissions.

In case you allow _-w_ access for another project, the members of the other project can upload files to your bucket and remove your files. However, you do not have access to the uploaded files until either you or the sender shares the bucket with your project:
```text
swift post <your_bucket_name> -r "your_project:*"
```

For example:
```text
swift post my_fishbucket -r "project_1234:*,project_4567:*"
```

Alternatively, you can set the project public and then access the file.

## Files larger than 5 GB

Swift has a single-object size limit of 5 GiB. In order to upload files
larger than this, you must create a large object that consists of
smaller segments. To achieve this, you can use Swift to upload a
so-called _Static Large Object_ (SLO).

Try to upload a large file:
```text
$ md5sum /tmp/6GB.zero
9e6a77a2d5650b2e2a710a08e9e61a81  /tmp/6GB.zero
$ stat /tmp/6GB.zero
File: '/tmp/6GB.zero'
Size: 6424625152      Blocks: 12548104   IO Block: 4096   regular file
...
$ swift upload my_bigfishes /tmp/6GB.zero
Object PUT failed: https://a3s.fi:443/swift/v1/my_bigfishes/tmp/6GB.zero 400 Bad Request   EntityTooLarge
```

It fails with the message `EntityTooLarge`, so instead:
```text
$ swift upload my_bigfishes --use-slo --segment-size 1G /tmp/6GB.zero
tmp/6GB.zero segment 3
tmp/6GB.zero segment 5
tmp/6GB.zero segment 1
tmp/6GB.zero segment 0
tmp/6GB.zero segment 4
tmp/6GB.zero segment 2
tmp/6GB.zero
```

This creates a new bucket:
```text
$ swift list |grep my_bigfishes
my_bigfishes
my_bigfishes_segments
```

In this case the target bucket (my_bigfishes) contains just a front object that contains information what segments, stored in the segments bucket (my_bigfishes_segments) make the stored file. Operations performed to the front object are automatically reflected to the segments. Normally users don't need to operate with the segments buckets at all and objects inside these buckets should not be deleted or modified.

Download the entire 6GB.zero:

```text
$ swift download my_bigfishes tmp/6GB.zero -o /tmp/6GB.zero
tmp/6GB.zero [auth 0.594s, headers 0.881s, total 74.467s, 86.969 MB/s]
$ md5sum 6GB.zero
9e6a77a2d5650b2e2a710a08e9e61a81  6GB.zero
```

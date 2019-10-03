
# Swift client

Pythom Swift client is command line tool for using object storage systems like Allas. If you use Allas from a Puhti or Taito, all the required packages and software are already installed and you cat take them in use with command:

```text
module load allas
```
After that you need to open connection to allas with command:
```text
allas_conf
```
The allas_conf command above asks for your CSC password (the same that you use to login to CSC servers). After that it lists your projects in Allas and asks you to define the project that will be used. After that _allas_conf_ generates autheticates the connection to the selected project in Allas. The authentication information is stored into shell variables OS_AUTH_TOKEN and OS_STORAGE_URL that are valid for max 3 hours. Hoverver you can refresh the authentication at any time my running _allas_conf_ again. The environment variables are available only for that login session, so if you log into Puhti in another session, you need to authenticate again in there to access Allas.


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


You can install and use Swift also outside CSC computing environment, but in that case make sure that your Swift version is not too old, since the older Swift versions might not work with Allas.


## Create buckets and upload objects

Creating a new empty bucket can be done with command:
```bash
swift post <new_bucket_name>
```

You can also create a new bucket and add a file in it with command:
```bash
swift upload <new_bucket_name> <file_name>
```

Adding a file to a existing bucket can be done with the same command:
```bash
swift upload <old_bucket_name> <file_name>
```
**Note:** This might cause a warning  "_409 Conflict: BucketAlreadyExists_", but that does not necessarily mean that the upload failed. 
If the next line displays the file name, it was successfully uploaded to the already existing bucket.

```bash
$ swift upload my_fishbucket my_fish.jpg
Warning: failed to create container 'my_fishbucket': 409 Conflict: BucketAlreadyExists
my_fish.jpg
```
&nbsp;


## List objects and buckets

To list all the buckets belonging to the project use command:
```bash
$ swift list
my_fishbucket
my_bigfishes
```
Listing the content of a certain bucket:
```bash
$ swift list my_fishbucket
my_fish.jpg
salmon.jpg
bass.png
```
&nbsp;


## Download objects and buckets

Downloading an object can be done with command:
```bash
swift download <bucket_name> <file_name>
```
If you want to rename the object as you download it, you can add <i>-o new_name</i> at the end of the command:
```bash
swift download <bucket_name> <file_name> -o <new_name>
```
Additionally, you can download a whole bucket at once:
```bash
swift download <bucket_name>
```
&nbsp;

## Move objects

You can copy data from one bucket to another with command ```swift copy```. The command below copies <i>file.txt</i> from _bucket1_ to _bucket2_.
```bash
swift copy --destination /bucket2 bucket1 file.txt
```
**Note:** In case there is no bucket called _bucket2_, Swift will create a new bucket with that name. However, even if there is a bucket called _bucket2_, Swift will claim that it created a new one even though it just copied the file to the already existing one:
```bash
$ swift copy --destination /other_bucket my_bigfishes bigfish.jpg
created container other_bucket
my_bigfishes/bigfish.jpg copied to /other_bucket/bigfish.jpg
$ swift list other_bucket
bigfish.jpg
other_file.txt
```

You can also rename the file as you copy it:
```bash
$ swift copy --destination /new_bucket/newname.jpg my_fishbucket my_fish.jpg
created container new_bucket
my_fishbucket/my_fish.jpg copied to /new_bucket/newname.jpg
```
For further information about the command <i>swift copy</i>, see [OpenStack Docs](https://docs.openstack.org/python-swiftclient/latest/cli/index.html#swift-copy).


&nbsp;

## Remove objects and buckets

Removing objects and buckets can be done with command ```swift delete```. Deleting an object:
```bash 
swift delete <bucket_name> <object_name>
```
For example:
```bash
$ swift delete my_fishbucket useless_fish.jpg
useless_fish.jpg
```

Unlike with web client and s3cmd, with Swift you can **delete a whole bucket at once**:
```bash
swift delete <my_old_bucket>
```
For example:
```bash
$ swift delete old_fishbucket
old_fish.png
useless_salmon.jpg
too_tiny_bass.jpg
$ swift list old_fishbucket
Container u'old_fishbucket' not found
```
**Please note:** This deletes the bucket permanently and the data is lost if there is no backup of it, so before using this command make sure you do not need the data anymore or that you have a copy of the data in somewhere else.

&nbsp;


## Download or delete whole projects

You can download the whole project with command:
```bash
swift download --all
```

Deleting the whole project is done with:
```bash
swift delete --all
```
**Please note:** Be careful with this command since it deletes all the content of the project and there might not be any backup of the data. Before using this command, make sure you do not need the data anymore or that you have a copy of the data in somewhere else.

&nbsp;


## Pseudofolders and checksum

In case you want to observe whether the object has changed, you can use [checksum](../terms_and_concepts.md#checksum) with command ```md5sum```.

Pseudofolders can be handled by adding the name of the pseudofolder in front of the file name: <i>my_pseudofolder_name/my_file</i>

Creating a pseudofolder _pictures_ in to bucket <i>my_bigfishes</i> and adding object _bass.png_ in it can be done with command:
```bash
$ swift upload my_bigfishes/pictures bass.png
pictures/bass.png
```

The example below uploads a file called _salmon.jpg_ into a pseudo-folder called _fishes_ which is inside a bucket called _my_fishbucket_. After that the file is downloaded.
```bash
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
**Note** how the checksums with the object <i>salmon.jpg</i> and the renamed version <i>my_renamed_salmon.jpg</i> are the same since the file is same and has not changed. 


## Managing metadata

You can define metadata to an object with command:
```bash
swift post my_fishbucket my_fish.jpg --meta foo:bar
```


The following command provides details about a bucket:

```bash
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
Set a bucket to read-only to the world (make the content visible at URL: <i>object.pouta.csc.fi/bucket_name/object_name</i>) instead of the default which is private to project only:
```bash
swift post my_fishbucket --read-acl ".r:*"
```
More about the access management in section [Giving another project read and write access to a bucket](#giving-another-project-read-and-write-access-to-a-bucket).

More details about a file:
```bash
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

Note that the above file was uploaded with the _s3cmd client_ and therefore there is a extra metadata _S3Cmd-Attrs_ compared to one uploaded with Swift or S3. _ETag_ is the _hash_ when viewing the file details in the Pouta dashboard.

Removing a metadata field (in this case _Temp-URL-Key_, which is discussed in more detail in the next section) is done with command:
```bash
swift post -m "Temp-URL-Key:"
```
&nbsp;


## Temp URLs
 
If you want to share an object from a private (or public) bucket with somebody, you can create a temporary URL. This can be useful for a homepage where you want to share an object but not the whole bucket and only for a limited period of time. This can also be useful if you want to use a private object in a batch job on Puhti or Taito.
 
**Note:** Everyone who has access to the temporary URL has access to the object. While it is possible to add Meta Temp-URL-Key to a bucket or object, the Temp URL command can only be used in a project wide scope (see [OpenStack documentation of temp URLs](https://docs.openstack.org/python-swiftclient/latest/cli/index.html#swift-tempurl)).
 
Create a random key:
```bash
RANDOMKEY="my-super-secret-key"
```
Post a Temp-URL-Key to the whole project. **Please note:** If someone changes this project wide Temp Key, all Temp URLs stop working. You should coordinate changes like these within your computing project.
```bash
swift post -m "Temp-URL-Key:$RANDOMKEY" 
```
To get your <i>OS_PROJECT_ID</i> use command `env`:
```bash
$ env | grep -i project
OS_PROJECT_NAME=project_123456
OS_PROJECT_ID=<os_project_id>
```
Save the full path to the Swift object (Replace the part *"os_project_id"* with your OS_PROJECT_ID):

```bash
MYURL=https://object.pouta.csc.fi/swift/v1/AUTH_"os_project_id"/my_fishbucket/bigfish.jpg
```


Create a Temp-URL-Key valid for 86400 seconds (24 hours):
```bash
$ swift tempurl GET 86400 $MYURL $RANDOMKEY
https://object.pouta.csc.fi/swift/v1/AUTH_6e3f5db8e08940f481744240af8701e5/my_fishbucket/bigfish.jpg?temp_url_sig=9a118ddda22c83c7a6cd49c013389f0507c007ca&temp_url_expires=1514648675
```

Use the previously created Temp URL to download the object:
```bash
$ curl https://object.pouta.csc.fi/swift/v1/AUTH_6e3f5db8e08940f481744240af8701e5/my_fishbucket/bigfish.jpg?temp_url_sig=9a118ddda22c83c7a6cd49c013389f0507c007ca&temp_url_expires=1514648675> bigfish.jpg
```
You may set a second key by adding another metadata entry with title "*Temp-URL-Key-2*".

&nbsp;

## Giving another project read and write access to a bucket

You can give another project read and write rights to a bucket. Giving project _project1_ read right to bucket <i>my_fishbucket</i> is done with command:
```bash
swift post my_fishbucket -r "project1:*"
```
Write access can be given similarly by replacing the _-r_ (_read_) with _-w_ (_write_):
```bash
swift post my_fishbucket -w "project1:*"
```
The sign _*_ after the project name defines that all the project members in the project gets the rights.

Alternatively, you can give read and write access only to certain members of another project:
```bash
swift post my_fishbucket -r "project2:member1"
swift post my_fishbucket -w \
   "project3:member1,project3:member2,project5:member1,project6:*"
```

**Please note:** If you have allowed access for specific projects, making the shared project public and private again will remove the previous access permissions.

In case you allow _-w_ access for another project, the members of the other project can upload files to your bucket and remove your files. 
However, you have not access to those uploaded files until either you or the sender shares the bucket with your project:
```bash
swift post <your_bucket_name> -r "your_project:*"
```
For example:
```bash
swift post my_fishbucket -r "project_1234:*,project_4567:*"
```
Alternatively, you can set the project public and then access the file.


&nbsp;



## Files larger than 5 GB

Since the OpenStack command does not support uploading files larger than 5GB, we can use Swift to upload a so-called _Static Large Object_ (SLO).

According to [https://docs.openstack.org/python-swiftclient/latest/cli/index.html#more-complex-examples](https://docs.openstack.org/python-swiftclient/latest/cli/index.html#more-complex-examples):

"_Swift has a single object size limit of 5GiB. In order to upload files larger than this, we must create a large object that consists of smaller segments._"

Trying to upload a large file:
```bash
$ md5sum /tmp/6GB.zero
9e6a77a2d5650b2e2a710a08e9e61a81  /tmp/6GB.zero
$ stat /tmp/6GB.zero
File: '/tmp/6GB.zero'
Size: 6424625152      Blocks: 12548104   IO Block: 4096   regular file
...
$ swift upload my_bigfishes /tmp/6GB.zero
Object PUT failed: https://object.pouta.csc.fi:443/swift/v1/my_bigfishes/tmp/6GB.zero 400 Bad Request   EntityTooLarge
```
It failed with message `EntityTooLarge`, so instead you can do:
```bash
$ swift upload my_bigfishes --use-slo --segment-size 1G /tmp/6GB.zero
tmp/6GB.zero segment 3
tmp/6GB.zero segment 5
tmp/6GB.zero segment 1
tmp/6GB.zero segment 0
tmp/6GB.zero segment 4
tmp/6GB.zero segment 2
tmp/6GB.zero
```
This creates a new bucket as follow:
```bash
$ swift list |grep my_bigfishes
my_bigfishes
my_bigfishes_segments
```
Download of the whole 6GB.zero can be done with:

```bash
$ swift download my_bigfishes tmp/6GB.zero -o /tmp/6GB.zero
tmp/6GB.zero [auth 0.594s, headers 0.881s, total 74.467s, 86.969 MB/s]
$ md5sum 6GB.zero
9e6a77a2d5650b2e2a710a08e9e61a81  6GB.zero
```

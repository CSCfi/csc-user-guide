----------------
## Swift client

For basic operations we recommend using the _openstack command line client_. It can access the object storage, but it is limited in its features. The more advanced _Swift command line client_ is used in the examples. The instructions for the installation of the Swift command line client can be found from [https://research.csc.fi/pouta-install-client](https://research.csc.fi/pouta-install-client){:target="_blank"}.

Typical commands for first-time use might be:
```bash
$ swift auth
$ swift list
$ swift stat
$ swift download <bucket name> <file name>
```
The below example uploads a file called _salmon.jpg_ into a pseudo-folder called _pictures_ which is inside a bucket called _fishes_.
```bash
$ md5sum pictures/salmon.jpg
22e44aa2b856e4df892b43c63d15138a  pictures/salmon.jpg
$ swift upload fishes pictures/salmon.jpg
pictures/salmon.jpg
$ swift list fishes
pictures/salmon.jpg
$ swift download fishes pictures/salmon.jpg -o salmon.jpg
pictures/salmon.jpg [auth 0.664s, headers 0.925s, total 0.969s, 3.605 MB/s]
$ md5sum salmon.jpg
22e44aa2b856e4df892b43c63d15138a  salmon.jpg
```
Instructions for using _Swift_ when viewing and producing metadata, handling temporary URLs and processing large files (over 5 GB) are listed below.

&nbsp;

* **Metadata**

The following command provides details about a bucket:

```bash
$ swift stat fishes
                      Account: AUTH_$PROJECT_UUID
                    Container: fishes
                      Objects: 1
                        Bytes: 1162342
                     Read ACL:
                    Write ACL:
                      Sync To:
                     Sync Key:
                Accept-Ranges: bytes
                   X-Trans-Id: txUUID-cpouta-production-kaj
             X-Storage-Policy: default-placement
```
```bash
X-Container-Bytes-Used-Actual: 1167360
                  X-Timestamp: 1516776076.95812
```
Set a bucket to read-only to the world instead of the default which is private to project only:
```bash
swift post fishes --read-acl ".r:*"
```
More details about a file:
```bash
$ swift stat fishes pictures/salmon.jpg
         Account: AUTH_$PROJECT_ID
       Container: fishes
          Object: Pictures/salmon.jpg
    Content Type: image/jpeg
  Content Length: 63220
   Last Modified: Wed, 24 Jan 2018 10:17:03 GMT
            ETag: a38f8db198e3fea43c83c465ffb0283b
Meta S3Cmd-Attrs: atime:1516788402/ctime:1513681753/gid:$LOCALGID/gname:$LOCALGROUP/md5:a38f8db198e3fea43c83c465ffb0283b/mode:33188/mtime:1513681747/uid:$LOCALUID/uname:$LOCALUSER
   Accept-Ranges: bytes
     X-Timestamp: 1516789023.84380
      X-Trans-Id: tx0000000000000000001d6-q-q-cpouta-production-kaj
```

Note how the above file was uploaded with the _s3cmd client_ and it added the extra S3Cmd-Attrs metadata compared to one uploaded with Swift or S3. ETag is the "_hash_" when viewing the file details in the Allas dashboard.

Removing a metadata field (in this case _Temp-URL-Key_, which is discussed in more detail in the next section) with swift is done with:
```bash
$ swift post -m "Temp-URL-Key:"
```
You can alternatively use the openstack command for some of the metadata operations:
```bash
$ openstack object set --property foo=bar fishes salmon.jpg
```
&nbsp;

<a name="temp_urls"></a>  

 * **Temp URLs**

[http://docs.ceph.com/docs/luminous/radosgw/swift/tempurl/](http://docs.ceph.com/docs/luminous/radosgw/swift/tempurl/){:target="_blank"}
 
If you want to share an object from a private (or public) bucket with somebody, you can create a temporary URL. This can be useful for a homepage where you want to share an object but not the whole bucket and for a limited period of time. This can also be useful if you want to use a private object in a batch job on _Puhti_ or _Taito_.
 
**Note** that everybody who has access to the temporary URL has access to the object. While it is possible to add Meta Temp-URL-Key to a bucket or objects, the Temp URL command can only be used in a project wide scope (see [https://docs.openstack.org/python-swiftclient/latest/cli/index.html#swift-tempurl](https://docs.openstack.org/python-swiftclient/latest/cli/index.html#swift-tempurl){:target="_blank"}).
 
Create a random key
```bash
$ RANDOMKEY="my-super-secret-key"
```
Post a Temp-URL-Key to the whole project. **Please note:** If someone changes this project wide Temp Key, all Temp URLs stop working. You should coordinate changes like these within your computing project.
```bash
$ swift post -m "Temp-URL-Key:$RANDOMKEY" 
```
Create a Temp-URL-Key valid for 86400 seconds (24 hours):
```bash
$ swift tempurl GET 86400 https://object.pouta.csc.fi/swift/v1/AUTH_$PROJECT_ID/fishes/pictures/salmon.jpg $RANDOMKEY
/v1/fishes/pictures/salmon.jpg?temp_url_sig=9a118ddda22c83c7a6cd49c013389f0507c007ca&temp_url_expires=1514648675
```
Use the previously created Temp URL to download the object:
```bash
$ curl "https://object.pouta.csc.fi/swift/v1/fishes/pictures/salmon.jpg?temp_url_sig=9a118ddda22c83c7a6cd49c013389f0507c007ca&temp_url_expires=1514648675" > salmon.jpg
```
You may set a second key by adding another metadata entry with title "Temp-URL-Key-2".

&nbsp;

<a name="files_larger_than_5gb"></a>  

 * **Files larger than 5 GB**

Since the openstack command does not support uploading files larger than 5GB, we can use Swift to upload a so-called _Static Large Object_ (SLO).

According to [https://docs.openstack.org/python-swiftclient/latest/cli/index.html#more-complex-examples](https://docs.openstack.org/python-swiftclient/latest/cli/index.html#more-complex-examples){:target="_blank"}:

"_Swift has a single object size limit of 5GiB. In order to upload files larger than this, we must create a large object that consists of smaller segments._"

```bash
$ md5sum /tmp/6GB.zero
9e6a77a2d5650b2e2a710a08e9e61a81  /tmp/6GB.zero
$ stat /tmp/6GB.zero
File: '/tmp/6GB.zero'
Size: 6424625152      Blocks: 12548104   IO Block: 4096   regular file
...
$ swift upload fishes /tmp/6GB.zero
Object PUT failed: https://object.pouta.csc.fi:443/swift/v1/fishes/tmp/6GB.zero 400 Bad Request   EntityTooLarge
```
So instead you can do:
```bash
$ swift upload fishes --use-slo --segment-size 1G /tmp/6GB.zero
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
$ swift list |grep fishes
fishes
fishes_segments
```
Download of the whole 6GB.zero can be done with:

```bash
$ swift download fishes tmp/6GB.zero -o /tmp/6GB.zero
tmp/6GB.zero [auth 0.594s, headers 0.881s, total 74.467s, 86.969 MB/s]
$ md5sum 6GB.zero
9e6a77a2d5650b2e2a710a08e9e61a81  6GB.zero
```

------------------
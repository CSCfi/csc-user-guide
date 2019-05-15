# Using object storage

This document lists the different ways to access CSC object storage
and manage data. You might want to first check
the [Object storage main page](object-storage-main.md) before
getting into the command line.

[TOC]

[comment]: <> (I'd like to top header not to appear in the TOC, the following might solve it)
[comment]: <> (https://github.com/mkdocs/mkdocs/issues/318)

### Best practices

The object storage  service is provided over  two different protocols,
Swift and  S3. Data uploaded  using one  protocol is visible  with the
other protocol.   Each protocol has  serveral different tools  you can
use. Here is a quick list of generic recommendations.

-    If  you have  a  choice,  use  the  Swift protocol, it's  better
    supported.
-   In any case, settle on one protocol. Do not mix S3 and Swift.
-     Do   not   use   uppercase    characters   in   the   names   of
    containers/buckets.
-   It's better to store a few large objects than a lot of small
    objects.  

### Buckets contain pseudo-folders

The top level category for storing objects (files) is a bucket. You 
can not have buckets with another layer of buckets inside. You can
however make use of so called pseudo-folders.  
  
If an object name contains a forward slash "/", it is interpreted as a
folder separator. These  are shown as folders  listings when accessing
the  data  through  Pouta  web  interface.  These  pseudo-folders  are
automatically
added if you upload whole folders with command line clients.  
  
For example, if you add two objects to a container

    cats/cat1.png
    cats/cat2.png

listing the  container will show  a folder  called "cats" and  the two
files within it.  
  
!!! note
    This means you can not have empty pseudo-folders, since
    they require at least one object inside them.

### Object Storage Client Summary

There  are several  different ways  of accessing  object storage.   We
support both the  Swift and S3 protocols to manage  the data. The list below
contains just some existing tools. There are more.

|Client|Usable|Notes|
|--- |--- |--- |
|[Web  client](#web-client-openstack-horizon-dashboard)|Yes|Use via https://pouta.csc.fi|
|[python-swiftclient](#swift-client)|Yes|This is the recommended Swift client|
|[S3 client](#s3-client)|Yes|This  is  the  recommended  S3 client. Use version 2.0.2  or later.|
|[python-swift library](#access-via-python-library)|Yes|
|libs3|Yes||
|python-openstackclient|Yes||
|aws-cli|Yes|aws-cli and the boto3 python library.|
|nordugrid-arc-client|No|Can  be used for grid jobs. Bug reports submitted.|
|curl|Yes|Extremely simple to use with public  objects and temporary URLs|
|wget|Yes|Same as curl|


### Web client - Openstack Horizon Dashboard

The  OpenStack  documentation  on  managing containers  over  the  web
interface can be found here
<https://docs.openstack.org/horizon/latest/user/manage-containers.html>  
  
The openstack dashboard  has a **small** subset of  the Object Storage
functionalities:  Create,  delete  and  list  containers.  Upload  and
download  files.  Additionally,  you  can make  containers  public  or
private.

![Horizon web client](images/cats_horizon.png)

### Swift client

For basic  operation we recommend  using the "openstack"  command line
client. It  can access the  object storage, but  it is limited  in its
features. The  more advanced  "swift" command line  client is  used in
the examples.  
  
This assumes  that you  have the swift  command line  client installed
[Installation instructions](install-client.md), and your credentials
(username,  password) sourced.  Typical  commands  for first-time  use
might be:

    $ swift auth
    $ swift list
    $ swift stat
    $ swift download <bucket name> <file name>

  
The below example  uploads a file called cat.jpg  into a pseudo-folder
called Pictures which is inside a bucket called cats.

    $ md5sum Pictures/cat.jpg
    22e44aa2b856e4df892b43c63d15138a  Pictures/cat.jpg
    $ swift upload cats Pictures/cat.jpg
    Pictures/cat.jpg
    $ swift list cats
    Pictures/cat.jpg
    $ swift download cats Pictures/cat.jpg -o cat.jpg
    Pictures/cat.jpg [auth 0.664s, headers 0.925s, total 0.969s, 3.605 MB/s]
    $ md5sum cat.jpg
    22e44aa2b856e4df892b43c63d15138a  cat.jpg

### Object Storage Metadata

The following command provides details about a bucket:

    $ swift stat cats
                          Account: AUTH_$PROJECT_UUID
                        Container: cats
                          Objects: 2
                            Bytes: 1162342
                         Read ACL:
                        Write ACL:
                          Sync To:
                         Sync Key:
                    Accept-Ranges: bytes
                       X-Trans-Id: txUUID-cpouta-production-kaj
                 X-Storage-Policy: default-placement
    X-Container-Bytes-Used-Actual: 1167360
                      X-Timestamp: 1516776076.95812

                     Content-Type: text/plain; charset=utf-8
                       X-Trans-Id: txUUID-cpouta-production-kaj

Define some metadata for a bucket  (set read-only to the world instead
of the default which is private to project only):

    swift post cats --read-acl ".r:*"

  
More details about a file :

    $ swift stat cats Pictures/cat4.jpg
             Account: AUTH_$PROJECT_ID
           Container: cats
              Object: Pictures/cat4.jpg
        Content Type: image/jpeg
      Content Length: 63220
       Last Modified: Wed, 24 Jan 2018 10:17:03 GMT
                ETag: a38f8db198e3fea43c83c465ffb0283b
    Meta S3Cmd-Attrs: atime:1516788402/ctime:1513681753/gid:$LOCALGID/gname:$LOCALGROUP/md5:a38f8db198e3fea43c83c465ffb0283b/mode:33188/mtime:1513681747/uid:$LOCALUID/uname:$LOCALUSER
       Accept-Ranges: bytes
         X-Timestamp: 1516789023.84380
          X-Trans-Id: tx0000000000000000001d6-q-q-cpouta-production-kaj

  
Note how  the above  file was  uploaded with the  s3cmd client  and it
added the  extra S3Cmd-Attrs  metadata compared  to one  uploaded with
swift or s3. ETag  is the "hash" when viewing the  file details in the
cPouta
dashboard.  
  
Removing  a  metadata  field  (in this  case  Temp-URL-Key,  which  is
discussed in more detail in the next section) with swift is done with:

    $ swift post -m "Temp-URL-Key:"

You  can alternatively  use  the  openstack command  for  some of  the
metadata operations:

    $ openstack object set --property foo=bar cats cat3.jpg

### Temp URLs for objects

  
If you  want to share  a object from  a private (or  public) container
with somebody you can create a temporary url. This can be useful for a
homepage where you want to share an object but not the whole container
and for a limited period of time.  This can also be useful if you want
to use a private object in a batch job on Taito. For a more detailed
description, see [Ceph Documentation on temp urls](http://docs.ceph.com/docs/luminous/radosgw/swift/tempurl)
  
!! note
   Everybody who has access to the temporary url has access to
   the  object.* While  it  is possible  to add  Meta  Temp-Url-Key to  a
   container  or objects,  the Temp  Url command  can only  be used  in a
   project wide scope. See [OpenStack documentation of temp urls](https://docs.openstack.org/python-swiftclient/latest/cli/index.html#swift-tempurl)
  
Create a random key

    $ RANDOMKEY="my-super-secret-secret"

  
Post  a temp  url key  to  the whole  project. **Please  note that  if
someone  changes  this  project  wide  temp key  all  temp  urls  stop
working.  You  should  coordinate   changes  like  these  within  your
computing project!**

    $ swift post -m "Temp-URL-Key:$RANDOMKEY" 

  
Create a temp url key valid for 86400 seconds

    $ swift tempurl GET 86400 https://object.pouta.csc.fi/swift/v1/AUTH_$PROJECT_ID/cats/Pictures/cat.jpg $RANDOMKEY
    /v1/cats/Pictures/cat.jpg?temp_url_sig=9a118ddda22c83c7a6cd49c013389f0507c007ca&temp_url_expires=1514648675

  
Use the previously created temp url to download the object

    $ curl "https://object.pouta.csc.fi/swift/v1/cats/Pictures/cat.jpg?temp_url_sig=9a118ddda22c83c7a6cd49c013389f0507c007ca&temp_url_expires=1514648675" > cat.jpg

You may set a second key by adding another metadata entry with title
"Temp-URL-Key-2".  


### Files larger than 5 GB

The openstack  command does  not support  uploading files  larger than
5GB.  So we  use the python-swiftclient "swift" to  upload a so-called
Static
Large Object (SLO).  
  
The [OpenStack python-swiftclient documentation](https://docs.openstack.org/python-swiftclient/latest/cli/index.html#more-complex-examples)
says  "*Swift has  a single  object size  limit of  5GiB. In  order to
upload files  larger than  this, we  must create  a large  object that
consists of smaller segments.*"


    $ md5sum /tmp/6GB.zero
    9e6a77a2d5650b2e2a710a08e9e61a81  /tmp/6GB.zero
    $ stat /tmp/6GB.zero
      File: ‘/tmp/6GB.zero'
      Size: 6424625152      Blocks: 12548104   IO Block: 4096   regular file
    ...
    $ swift upload cats /tmp/6GB.zero
    Object PUT failed: https://object.pouta.csc.fi:443/swift/v1/cats/tmp/6GB.zero 400 Bad Request   EntityTooLarge

So instead you can do:

    $ swift upload cats --use-slo --segment-size 1G /tmp/6GB.zero
    tmp/6GB.zero segment 3
    tmp/6GB.zero segment 5
    tmp/6GB.zero segment 1
    tmp/6GB.zero segment 0
    tmp/6GB.zero segment 4
    tmp/6GB.zero segment 2
    tmp/6GB.zero

  
This creates a new bucket as follows:

    $ swift list |grep cats
    cats
    cats_segments

  
Download the whole 6GB.zero can be done with:

    $ swift download cats tmp/6GB.zero -o /tmp/6GB.zero
    tmp/6GB.zero [auth 0.594s, headers 0.881s, total 74.467s, 86.969 MB/s]
    $ md5sum 6GB.zero
    9e6a77a2d5650b2e2a710a08e9e61a81  6GB.zero

### S3 client

To utilize the S3 API, ec2 credentials are required. These are created
from the CLI with:

    $ openstack ec2 credentials create
    +----------------------------------+----------------------------------+----------------------------------+----------+
    | Access                           | Secret                           | Project ID                       | User ID  |
    +----------------------------------+----------------------------------+----------------------------------+----------+
    | 00000000001                      | 5000000000000000000              | 000000000000000000022            | $username|
    +----------------------------------+----------------------------------+----------------------------------+----------+

### s3cmd - command line tools

Please refer to <http://s3tools.org/download> and 
<http://s3tools.org/usage> for upstream documentation.

Fedora/RHEL derivatives:

    $ sudo yum install s3cmd

  
Debian derivatives:

    $ sudo apt install s3cmd

OSX:

    $ python3 virtualenv
    $ pip3 install s3cmd
    $ s3cmd

You need to use <span style="color: rgb(0, 0, 0);">ec2 credentials are
when using S3.  You can create S3 credentials by  sourcing your openrc
file  as per  instructions  in chapter 3.4.1.3. ANCHOR

If you  already have created ec2  credentials that you want  to reuse,
you can find them by issuing:

    openstack ec2 credentials list

Once you have your ec2 credentials you will need to use the Access and
Secret   in  the   next  command.   The  interactive   command  "s3cmd
--configure" is  good for  first-time use.  It creates  a $HOME/.s3cfg
file, adds  access keys  and ids  from above,  points to  pouta object
store and adds an encryption key. It is probably a good idea to create
a password when you get to the option.

Alternatively, you can create a working file by adding your Access and
Secret to the following oneliner:

    $ s3cmd --configure --access_key=YOUR_EC_ACCESS_KEY_HERE --secret_key=YOUR_EC_SECRET_KEY_HERE --host=object.pouta.csc.fi --region=regionOne --host-bucket='%(bucket)s.object.pouta.csc.fi'

Then you need to verify all the settings from the created file.

### s3cmd and public objects

    $ s3cmd put Pictures/cat2.jpg s3://cats/Pictures/cat2.jpg -P
    Public URL of the object is: http://object.pouta.csc.fi/cats/Pictures/cat2.jpg

  
*\*Note that the  above client outputs a URL which  has http:// (which
is not open in the object storage  firewall). A URL like this needs to
be
manually changed to https if such a client is used.\**  


### Giving another project read access to a bucket

"s3cmd setacl" command  needs to use the UUID of  the project you want
to grant access to.  
  
The ID  can be found at  <https://pouta.csc.fi/dashboard/identity/> or
with "openstack project show $project\_name". You need access
(membership) to the project to find out the UUID.  
  
In  the Pouta  Web UI  you only  see containers  that members  of your
project have  created. If your  project has been granted  project read
access to  a bucket with  the s3cmd  client, the following  applies to
other members of your project:

-   can list and fetch files with the python-swiftclient
-   "swift list" does not display the bucket
-   "s3cmd ls" does display the bucket.

  
Granting read access:

    $ s3cmd setacl --acl-grant=read:$other_project_uuid s3://cats

  
Revoking read access:

    $ s3cmd setacl --acl-revoke=read:$other_project_uuid s3://cats

  
View permissions:

    $ s3cmd info s3://cats|grep -i acl
       ACL:       other_project_uuid: READ
       ACL:       my_project_uuid: FULL_CONTROL

### Access via Python library

Some details about setting up the client with keystone authentication:
<https://docs.openstack.org/python-swiftclient/newton/client-api.html>  
  
Some usage examples in CEPH RadosGW swift documentation:
[http://docs.ceph.com/docs/jewel/radosgw/swift/python/]  
  
!!! tip
    CSC Instructions for how to [install](install-client.md) and [use the CLI](command-line-tools.md)
  
The python pip libraries needed for the example below are:
python-keystoneclient and python-swiftclient  
  
Then create this script:

    cat << EOF > list_swift.py
    from keystoneauth1 import session
    from keystoneauth1.identity import v3
    import swiftclient
    import os

    _authurl = os.environ['OS_AUTH_URL']
    _auth_version = os.environ['OS_IDENTITY_API_VERSION']
    _user = os.environ['OS_USERNAME']
    _key = os.environ['OS_PASSWORD']
    _os_options = {
        'user_domain_name': os.environ['OS_USER_DOMAIN_NAME'],
        'project_domain_name': os.environ['OS_USER_DOMAIN_NAME'],
        'project_name': os.environ['OS_PROJECT_NAME']
    }

    conn = swiftclient.Connection(
        authurl=_authurl,
        user=_user,
        key=_key,
        os_options=_os_options,
        auth_version=_auth_version
    )

    resp_headers, containers = conn.get_account()

    for container in containers:
      print container
    EOF

  
Use it to list objects:

    $ python list_swift.py
    {u'count': 1, u'bytes': 1099122, u'name': u'cats'}
    {u'count': 0, u'bytes': 0, u'name': u'cat.jpg'}

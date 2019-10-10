
# The S3 client

This chapter describes how to use the Allas object storage service with the **s3cmd** command line client. This client uses
the _S3_ protocol that differs from the _Swift_ protocol used in the [rclone](./rclone.md), [swift](./swift_client.md) and [a-commands](./a_commands.md) examples. Thus, data that has been uploaded to Allas using these tools should not be downloaded with s3cmd and vice versa.

From the user perspective, one of the main differences between s3cmd and Swift based tools is that rclone, swift and a-tools connections remain valid for three hours at a time but with s3cmd, the connection remains open permanently. The permanent connection is practical in many ways but it has a security aspect: if your CSC account is compromised, so is the object storage space.

In the object storage, files are stored as objects in buckets. Buckets resemble folders in normal file systems. There are, however, some differences. Firstly, the file structure in the object storage is flat: you cannot create a bucket inside another bucket. Secondly, all bucket names must be unique throughout the object storage system. You cannot use a bucket name that is already used by you or some other object storage user. See the [checklist](../introduction.md#naming-buckets) for how to name a bucket.

The most commonly used _s3cmd_ operations:

| s3cmd command | Function |
| :---- | :---- |
| mb | Create a bucket |
| put | Upload an object |
| ls | List objects and buckets |
| get | Download objects and buckets |
| cp | Move object |
| del | Remove objects or bucket |
| md5sum | Get the checksum |
| info | View metadata |
| signurl | Create a temporary URL |
| put -P | Make an object public |
| setacl --acl-grant | Manage access rights |

The syntax of the `s3cmd` command:
```
s3cmd -options command parameters
```

The table above lists the most essential s3cmd commands. For more complete list, visit the [s3cmd manual page](https://s3tools.org/usage) or type:
```bash
s3cmd -h
```
If you use Allas on Puhti or Taito, all required packages and software are already installed, and you can jump to the section [s3cmd with supercomputers](#s3cmd-with-supercomputers). You can skip the installation chapter *Getting started with s3cmd* below.

## Getting started with s3cmd

Instructions for installing and using s3cmd

**s3cmd installation:**

Fedora/RHEL derivatives:
```bash
sudo yum install s3cmd
```
Debian derivatives:
```bash
sudo apt install s3cmd
```
OSX:
```bash
python3 virtualenv
pip3 install s3cmd
s3cmd
```

Please refer to [http://s3tools.org/download](http://s3tools.org/download) and [http://s3tools.org/usage](http://s3tools.org/usage) for upstream documentation.

You need to use _ec2_ credentials when using S3. You can create ec2 credentials by sourcing your _openrc_ file as in the instructions in the [Pouta documentation](https://research.csc.fi/pouta-install-client).

Once you have the RC file, you can add the environment variables:
```bash
source <project_name_here>-openrc.sh
```

The ec2 credentials are created from the CLI (command line interface):

```bash
$ openstack ec2 credentials create
+----------------------------------+----------------------------------+----------------------------------+----------+
| Access                           | Secret                           | Project ID                       | User ID  |
+----------------------------------+----------------------------------+----------------------------------+----------+
| 00000000001                      | 5000000000000000000              | 000000000000000000022            | $username|
+----------------------------------+----------------------------------+----------------------------------+----------+
```

Display your ec2 credentials:
```bash
openstack ec2 credentials list
```
Once you have the ec2 credentials, you will need to use _Access_ and _Secret_ in the next command. The interactive command ```s3cmd --configure ``` is good for first-time use. It creates a _$HOME/.s3cfg_ file, adds access keys and IDs, points to the Pouta object storage, and adds an encryption key. It is recommended to create a password when prompted.
 
Alternatively, you can create a working file by including your Access and Secret:
```bash
s3cmd --configure --access_key=YOUR_EC_ACCESS_KEY_HERE --secret_key=YOUR_EC_SECRET_KEY_HERE --host=object.pouta.csc.fi --region=US --host-bucket='%(bucket)s.object.pouta.csc.fi'
```
You need to verify all settings in the created file.

## s3cmd with supercomputers

Configure `s3cmd` in Taito or Puhti:
```
module load allas
source /appl/opt/allas_conf --mode s3cmd
```

The configuration process asks first your CSC password. Then it lists your Allas projects and asks you to define the name of the project to be used. During the next configuration steps, the system asks you for values that will be used for the Allas connection. In most cases, you can accept the proposed default values, but there are two exceptions:

   1.  It is recommended that you define a password that is used to encrypt the data traffic to and from the object storage server. This password is not connected to any other passwords in the CSC environment, so you can freely define it. This password is, however, stored in the s3cmd configuration file in a human-readable format, so you should not use this password elsewhere. 
   2.  As the last question, the configuration process asks whether the configuration should be saved. The default is "*no*" but you should answer "*y (yes)*", so that the configuration information is stored in the file _$HOME/.s3cfg_.

This configuration needs to be defined only once. In the future, s3cmd will use the object storage connection described in the _.s3cfg_ file automatically. However, if you wish to change the Allas project that s3cmd uses, you only need to run the configuration command again.

## Create buckets and upload objects

You can create a new bucket with command:

```bash
s3cmd mb s3://my_bucket
```

Upload a file to a bucket:
```bash
s3cmd put my_file s3://my_bucket
```

## List objects and buckets

List all buckets in a project:
```bash
s3cmd ls
```

List all objects in a bucket:
```bash
s3cmd ls s3://my_bucket
```

Display information about a bucket:
```bash
s3cmd info s3://my_bucket
```

Display information about an object:
```bash
s3cmd info s3://my_bucket/my_file
```

## Download objects and buckets

Download an object:
```bash
s3cmd get s3://my_bucket/my_file new_file_name
```
The parameter *new_file_name* is optional. It defines a new name for the downloaded file.

Using the command `md5sum`, you can check that the file has not been changed or corrupted:
```bash
$ md5sum my_file new_file_name
   39bcb6992e461b269b95b3bda303addf  my_file
   39bcb6992e461b269b95b3bda303addf  new_file_name
```
In the above example, the checksums match between the original and the downloaded file.

Download an entire bucket:
```bash
s3cmd get -r s3://my_bucket/
```

## Move objects

Copy an object to another bucket:
```bash
s3cmd cp s3://sourcebucket/objectname s3://destinationbucket
```

For example:
```bash
$ s3cmd cp s3://bigbucket/bigfish s3://my-new-bucket
remote copy: 's3://bigbucket/bigfish' -> 's3://my-new-bucket/bigfish'
```

Rename the file while copying it:
```bash
$ s3cmd cp s3://bigbucket/bigfish s3://my-new-bucket/newname
remote copy: 's3://bigbucket/bigfish' -> 's3://my-new-bucket/newname'
```

## Delete objects and buckets

Delete an object:
```bash
s3cmd del s3://my_bucket/my_file
```

Delete a bucket:
```bash
s3cmd rb s3://my_bucket
```
**Note:** You can only delete empty buckets.

## s3cmd and public objects

In this example, the object _salmon.jpg_ in the pseudo folder _fishes_ is made public:
```bash
$ s3cmd put fishes/salmon.jpg s3://my_fishbucket/fishes/salmon.jpg -P
Public URL of the object is: http://a3s.fi/my_fishbucket/fishes/salmon.jpg
```

**Note:** The above client outputs a URL with `http://` (which is not open in the object storage firewall). The URL needs to be manually changed to `https` if this kind of a client is used.

## Giving another project read access to a bucket

You can control the access rights using the command ```s3cmd setacl ```. This command requires the UUID (_universally unique identifier_) of the project you want to grant access to. The ID can be found in <a href="https://pouta.csc.fi/dashboard/identity/" target="_blank">https://pouta.csc.fi/dashboard/identity/</a> or using the command ```openstack project show $project_name ```. You need access (membership) to the project to find out the UUID.
 
In the Pouta web UI, you can see only buckets that the members of your project have created. If your project has been granted project read access to a bucket with the s3cmd client: 
 
 * The members of your project can list and fetch files with _python-swiftclient_.
 * _swift list_ does <u>not</u> display the bucket.
 * _s3cmd ls_ displays the bucket.
 
Grant read access:
```bash
s3cmd setacl --acl-grant=read:$other_project_uuid s3://my_fishbucket
```

View permissions:
```bash
$ s3cmd info s3://my_fishbucket|grep -i acl
   ACL:       other_project_uuid: READ
   ACL:       my_project_uuid: FULL_CONTROL
```

Revoke read access:
```bash
s3cmd setacl --acl-revoke=read:$other_project_uuid s3://my_fishbucket
```

## Temporary URLs

With s3cmd, you can create temporary URLs for objects. They are called _signed URLs_. 

Create a signed URL valid for 3600 seconds (three hours):
```bash
$ s3cmd signurl s3://bigbucket/bigfish +3600
http://bigbucket.a3s.fi/bigfish?AWSAccessKeyId=0a69a52ea4bc3a36839bc1e&Expires=1565951124&Signature=YEIjLFCaexvJ7rhusMV7E%3D
```

!!! note 
	The given URL does not work that way, but fortunately it can be fixed easily: change _http_ to _https_, move _bucketname_ from the beginning to _object.pouta.csc.fi/_ and add "/" after it:
	http<span style="background-color: #A4D1F9">s</span>://object.pouta.csc.fi/<span style="background-color: #A4D1F9">bigbucket/</span>bigfish?AWSAccessKey
	Id=0a69a52ea4bc3a36839bc1e&Expires=1565951124&Signature=YEIjLFCaexvJ7rhusMV7E%3D

## Use example

In this example, we store a simple dataset in Allas using s3cmd.

First, create a new bucket. The command `s3cmd ls` reveals that the object storage is empty at first. Then, use the command `s3cmd mb` to create a new bucket called _fish-bucket_.

```shell
$ s3cmd ls
ls
 
```

```shell
$ s3cmd mb s3://fish-bucket
mb s3://fish-bucket/
Bucket 's3://fish-bucket/' created

$ s3cmd ls
ls
2018-03-12 13:01  s3://fish-bucket
```
It is recommended to collect the data to be stored as larger units and compress it before uploading it to the system.

In this example, we store the Bowtie2 indices and the genome of the Zebrafish (Danio rerio) in the fish bucket. Running `ls -lh` shows that the index files are available in the current directory:

```shell
$ ls -lh
total 3.2G
-rw------- 1 kkayttaj csc 440M Mar 12 13:41 Danio_rerio.1.bt2
-rw------- 1 kkayttaj csc 327M Mar 12 13:41 Danio_rerio.2.bt2
-rw------- 1 kkayttaj csc 217K Mar 12 13:20 Danio_rerio.3.bt2
-rw------- 1 kkayttaj csc 327M Mar 12 13:20 Danio_rerio.4.bt2
-rw------- 1 kkayttaj csc 1.3G Mar 12 13:13 Danio_rerio.GRCz10.dna.toplevel.fa
-rw------- 1 kkayttaj csc 440M Mar 12 14:03 Danio_rerio.rev.1.bt2
-rw------- 1 kkayttaj csc 327M Mar 12 14:03 Danio_rerio.rev.2.bt2
-rw------- 1 kkayttaj csc 599K Mar 12 13:13 log
```

The data is collected and compressed as a single file using the `tar` command:
```
$ tar zcf zebrafish.tgz Danio_rerio*
```

The size of the resulting file is about 2 GB. The compressed file can be uploaded to the fish bucket using the command `s3cmd put`:
```text
$ ls -lh zebrafish.tgz
-rw------- 1 kkayttaj csc 9.3G Mar 12 15:23 zebrafish.tgz

$ s3cmd put zebrafish.tgz s3://fish-bucket
put zebrafish.tgz s3://fish-bucket
upload: 'zebrafish.tgz' -> 's3://fish-bucket/zebrafish.tgz'  [1 of 1]
 2081306836 of 2081306836   100% in   39s    50.16 MB/s  done
 
$ s3cmd ls s3://fish-bucket
ls s3://fish-bucket
2019-10-01 12:11 9982519261   s3://fish-bucket/zebrafish.tgz
```

Uploading 2 GB of data takes some time. The uploaded file can be retrieved using the command
```
$ s3cmd get s3://fish-bucket/zebrafish.tgz
```

By default, this bucket can be accessed only by project members. However, with command `s3cmd setacl`, you can make the file publicly available.

First make the fish bucket public:
```
$ s3cmd setacl --acl-public s3://fish-bucket
```

Then make the zebrafish genome file public:
```
$ s3cmd setacl --acl-public s3://fish-bucket/zebrafish.tgz
```

The syntax of the URL of the file:
```
https://a3s.fi/bucket_name/object_name
```

In this case, the file would be accessible using the link
_https://a3s.fi/fish-bucket/zebrafish.tgz_

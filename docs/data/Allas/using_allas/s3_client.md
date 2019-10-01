
# S3 client

This chapter describes how you can use the Allas object storage service with **s3cmd** command-line client. This client uses
_S3_ protocol that differs from the _Swift_ protocol that is used in the [rclone](./rclone.md), [swift](./swift,md) and [a_ commands](./a_ commands.md) examples. Thus, data that has been uploaded to Allas with these tools should not be downloaded with s3cmd and vice versa.

From user perspective one of the main differences between s3cmd and Swift based tools is that rclone, swift and a-tools connections remain valid for three hours at a time but with s3cmd the connection will stay permanently open. The permanent connection is handy in many ways, but it includes a security aspect too: if your CSC account is compromised, the object storage space is too.

In object storage the files are stored as objects that locate in buckets. The buckets resemble folders in normal file systems. There are however some differences compared to folders. Firstly, the file structure in object storage is flat: you cannot create a bucket that is inside another bucket. Secondly, all bucket names must be unique throughout the object storage system. You cannot use a bucket name that is already used by you or some other object storage user. See [checklist](../introduction.md#naming-buckets) for naming a bucket.


This chapter gives guidance for the most commonly used s3cmd operations:

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



The syntax of the `s3cmd` command is:

```
s3cmd -options command parameters
```

The table above lists the most essential s3cmd commands. For more complete list, visit the [s3cmd manual page](https://s3tools.org/usage){:target="_blank"} or execute command:

```bash
s3cmd -h
```
If you use Allas from a Puhti or Taito, all the required packages and software are already installed and you can jump to the section [s3cmd with supercomputers](#s3cmd-with-supercomputers). You can skip the installation chapter *Getting started with s3cmd* below.


Instructions for installing and using s3cmd are given below.


&nbsp;


## Getting started with s3cmd

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

Please refer to [http://s3tools.org/download](http://s3tools.org/download){:target="_blank"} and  [http://s3tools.org/usage](http://s3tools.org/usage){:target="_blank"} for upstream documentation.

You need to use ec2 credentials when using S3. You can create ec2 credentials by sourcing your openrc file as in the instructions in [Pouta documentation](https://research.csc.fi/pouta-install-client){:target="_blank"}.

Once you have the RC file, you can add the environment variables with the following command:

```bash
source <project_name_here>-openrc.sh
```

The ec2 credentials are created from the CLI (command-line interface) with:

```bash
$ openstack ec2 credentials create
+----------------------------------+----------------------------------+----------------------------------+----------+
| Access                           | Secret                           | Project ID                       | User ID  |
+----------------------------------+----------------------------------+----------------------------------+----------+
| 00000000001                      | 5000000000000000000              | 000000000000000000022            | $username|
+----------------------------------+----------------------------------+----------------------------------+----------+
```



You can find your ec2 credentials by issuing:
```bash
openstack ec2 credentials list
```
Once you have your ec2 credentials you will need to use the _Access_ and _Secret_ in the next command. The interactive command ```s3cmd --configure ``` is good for first-time use. It creates a _$HOME/.s3cfg_ file, adds access keys and ids from above, points to Pouta object storage and adds an encryption key. It is probably a good idea to create a password when you get to the option.
 
Alternatively, you can create a working file by adding your Access and Secret to the following oneliner:
```bash
s3cmd --configure --access_key=YOUR_EC_ACCESS_KEY_HERE --secret_key=YOUR_EC_SECRET_KEY_HERE --host=object.pouta.csc.fi --region=US --host-bucket='%(bucket)s.object.pouta.csc.fi'
```
Then you need to verify all the settings from the created file.


&nbsp;


## s3cmd with Supercomputers

In Taito and Puhti, the `s3cmd` configuration process can be done by executing commands:

```
module load allas
source /appl/opt/allas_conf --mode s3cmd
```

The configuration process asks first your CSC password. Then it lists your Allas projects and asks you to define the name of the project to be used. During the proceeding configuration steps, the system asks you about the values that will be used for the Allas connection. In most cases you can just accept the proposed default values, but there are two exceptions:

   1.  It is recommended that you define a password that is used to encrypt the data traffic to and from object storage server. This password is not connected to any other passwords in the CSC environment, so you can freely define it. This password is however stored to the s3cmd configuration file in a human readable format, so you should not use this password elsewhere. 
   2.  As the last question the configuration process asks if the configuration is saved. The default is "*no*" but you should answer "*y (yes)*", so that configuration information is stored to the file _$HOME/.s3cfg_.

This configuration needs to be defined only once. In the future, s3cmd will use this object storage connection described in the _.s3cfg_ file automatically. However, if you wish to change the Allas projecr that s3cmd uses, you just need to run the configuration command again.

&nbsp;


## Create buckets and upload objects

You can create a new bucket with command:

```bash
s3cmd mb s3://my_bucket
```

Uploading a file into a bucket can be done with command:

```bash
s3cmd put my_file s3://my_bucket
```
&nbsp;


## List objects and buckets

You can list all the buckets belonging to the project with command:
```bash
s3cmd ls
```

And all the objects belonging to a bucket with:
```bash
s3cmd ls s3://my_bucket
```

To display information about a bucket use command:
```bash
s3cmd info s3://my_bucket
```
And information about an object:
```bash
s3cmd info s3://my_bucket/my_file
```

&nbsp;


## Download objects and buckets

You can download an object with command:
```bash
s3cmd get s3://my_bucket/my_file new_file_name
```
The parameter *new_file_name* is optional - it defines a new name for the downloaded file in case you want to rename it.

With command `md5sum` you can check that the file has not been changed or corrupted:
```bash
$ md5sum my_file new_file_name
   39bcb6992e461b269b95b3bda303addf  my_file
   39bcb6992e461b269b95b3bda303addf  new_file_name
```
Checksums are equal between the original and the downloaded file. So good so far.

You can also download a whole bucket at once with command:
```bash
s3cmd get -r s3://my_bucket/
```

&nbsp;

## Move objects

You can copy an object in to another bucket with command:
```bash
s3cmd cp s3://sourcebucket/objectname s3://destinationbucket
```
For example,
```bash
$ s3cmd cp s3://bigbucket/bigfish s3://my-new-bucket
remote copy: 's3://bigbucket/bigfish' -> 's3://my-new-bucket/bigfish'
```

In addition, you can rename the file when copying it:
```bash
$ s3cmd cp s3://bigbucket/bigfish s3://my-new-bucket/newname
remote copy: 's3://bigbucket/bigfish' -> 's3://my-new-bucket/newname'
```


&nbsp;

## Delete objects and buckets

You can delete an object with command
```bash
s3cmd del s3://my_bucket/my_file
```

Deleting a bucket can be done with command:
```bash
s3cmd rb s3://my_bucket
```
**Note:** You can only delete empty buckets.

&nbsp;


## s3cmd and public objects

An object _salmon.jpg_ belonging to a pseudofolder _fishes_ can be made public with command:
```bash
$ s3cmd put fishes/salmon.jpg s3://my_fishbucket/fishes/salmon.jpg -P
Public URL of the object is: http://a3s.fi/my_fishbucket/fishes/salmon.jpg
```

**Note:** The above client outputs an URL which has http:// (which is not open in the object storage firewall). An URL like this needs to be manually changed to https if such a client is used.

&nbsp;


## Giving another project read access to a bucket

You can control the access rights with command ```s3cmd setacl ```.
This command needs to use the UUID (_universally unique identifier_) of the project you want to grant access to.
The ID can be found at <a href="https://pouta.csc.fi/dashboard/identity/" target="_blank">https://pouta.csc.fi/dashboard/identity/</a> or with command
```openstack project show $project_name ```. You need access (membership) to the project to find out the UUID.
 
In the Pouta Web UI you can see only buckets that the members of your project have created. If your project has been granted project read access to a bucket with the s3cmd client, the following applies to the members of your project:
 
 * Can list and fetch files with the python-swiftclient 
 * "_swift list_" does <u>not</u> display the bucket
 * "_s3cmd ls_" does display the bucket.
 
Granting read access:
```bash
s3cmd setacl --acl-grant=read:$other_project_uuid s3://my_fishbucket
```

View permissions:
```bash
$ s3cmd info s3://my_fishbucket|grep -i acl
   ACL:       other_project_uuid: READ
   ACL:       my_project_uuid: FULL_CONTROL
```

Revoking read access:
```bash
s3cmd setacl --acl-revoke=read:$other_project_uuid s3://my_fishbucket
```

&nbsp;


## Temporary URLs

With s3cmd, you can create temporary URLs to objects. They are called _signed URLs_. Creating a signed URL valid for 3600 seconds (3 hours) can be done with command:
```bash
$ s3cmd signurl s3://bigbucket/bigfish +3600
http://bigbucket.a3s.fi/bigfish?AWSAccessKeyId=0a69a52ea4bc3a36839bc1e&Expires=1565951124&Signature=YEIjLFCaexvJ7rhusMV7E%3D
```
!!! note 
	The given URL does not work like that, but fortunately it can be fixed easily: just change _http_ to _https_ and move the _bucketname_ from the beginning after _object.pouta.csc.fi/_ and add "/" after it:
	http<span style="background-color: #A4D1F9">s</span>://object.pouta.csc.fi/<span style="background-color: #A4D1F9">bigbucket/</span>bigfish?AWSAccessKey
	Id=0a69a52ea4bc3a36839bc1e&Expires=1565951124&Signature=YEIjLFCaexvJ7rhusMV7E%3D


&nbsp;


## Usage example


In this example we store a simple dataset to Allas using s3cmd.

First we create a new bucket. The command `s3cmd ls` shows that in the beginning we do not have any data in the object storage. After that, we use command `s3cmd mb` to create a new bucket called _fish-bucket_.

```shell
$ s3cmd ls
ls
 
```

```shell
$ s3cmd mb s3://fish-bucket
mb s3://fish-bucket/
Bucket 's3://fish-bucket/' created
```

```shell
$ s3cmd ls
ls
2018-03-12 13:01  s3://fish-bucket
```
It is recommended to collect the data to be stored into larger units and compress the data before uploading it to the system.

In this example we will store the Bowtie2 indexes and genome of the Zebrafish (Danio rerio) to the fish-bucket. Running `ls -lh` shows that we have the index files available in the current directory:

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

The data is collected and compressed to a single file with `tar` command:

```
$ tar zcf zebrafish.tgz Danio_rerio*
```


The size of the resulting file is about 2 GB. Now the compressed file can be uploaded to the fish-bucket with command `s3cmd put`:

```shell
$ ls -lh zebrafish.tgz
-rw------- 1 kkayttaj csc 9.3G Mar 12 15:23 zebrafish.tgz
```

```shell
put zebrafish.tgz s3://fish-bucket
upload: 'zebrafish.tgz' -> 's3://fish-bucket/zebrafish.tgz'  [1 of 1]
 2081306836 of 2081306836   100% in   39s    50.16 MB/s  done
```


```shell
$ s3cmd ls s3://fish-bucket
ls s3://fish-bucket
2019-10-01 12:11 9982519261   s3://fish-bucket/zebrafish.tgz
```

Uploading 2 GB of data takes some time. The uploaded file could be retrieved with command:

```
$ s3cmd get s3://fish-bucket/zebrafish.tgz
```

By default, this bucket can be accessed only by the project members. However, with command `s3cmd setacl` you can make the file publicly available:

First make the fish-bucket public:

```
$ s3cmd setacl --acl-public s3://fish-bucket
```

And then make the zebrafish genome file public:
```
$ s3cmd setacl --acl-public s3://fish-bucket/zebrafish.tgz
```

The syntax of URL of the file is:

```
https://a3s.fi/bucket_name/object_name
```

So, in this case the file would be accessible through link:  
_https://a3s.fi/fish-bucket/zebrafish.tgz_

&nbsp;


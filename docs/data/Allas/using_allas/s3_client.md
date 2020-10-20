
# The S3 client

This chapter describes how to use the Allas object storage service with the **s3cmd** command line client. This client uses
the _S3_ protocol that differs from the _Swift_ protocol used in the [Rclone](./rclone.md), [swift](./swift_client.md) and [a-commands](./a_commands.md) examples. Normally data uploaded with S3 can be utilized with swift protocol too. However, over 5 GB files uploaded to Allas with swift can't be downloaded with S3 protocol. 

From the user perspective, one of the main differences between S3 and Swift protocols is that Swift based connections remain valid for eight hours at a time, but with S3, the connection remains permanently open. The permanent connection is practical in many ways but it has a security aspect: if your CSC account is compromised, so is the object storage space.

The syntax of the `s3cmd` command:
```text
s3cmd -options command parameters
```

The most commonly used _s3cmd_ commands:

| s3cmd command | Function |
| :---- | :---- |
| mb | Create a bucket |
| put | Upload an object |
| ls | List objects and buckets |
| get | Download objects and buckets |
| cp | Move object |
| del | Remove objects or buckets |
| md5sum | Get the checksum |
| info | View metadata |
| signurl | Create a temporary URL |
| put -P | Make an object public |
| setacl --acl-grant | Manage access rights |


The table above lists only the most essential _s3cmd_ commands. For more complete list, visit the [s3cmd manual page](https://s3tools.org/usage) or type:
```text
s3cmd -h
```
## Getting started with s3cmd

If you use Allas on Puhti or Mahti, all required packages and software are already installed. In this case you can skip this  chapter and proceed to the section [Configuring S3 connection in supercomputers](#configuring-s3-connection-in-supercomputers). 

To configure a s3cmd connection, you need to have _OpenStack_ and _s3cmd_ installed in your environment. 

**OpenStack s3cmd installation:**

Fedora/RHEL derivatives:
```text
sudo yum update
sudo yum install python3
sudo pip3 install python-openstackclient
sudo yum install s3cmd
```
Debian derivatives:
```text
sudo apt-get update
sudo apt install python-pip python-dev
sudo pip install python-openstackclient
sudo apt install s3cmd
```
OSX:
```text
python3 virtualenv
pip3 install s3cmd
s3cmd
```

Please refer to [http://s3tools.org/download](http://s3tools.org/download) and [http://s3tools.org/usage](http://s3tools.org/usage) for upstream documentation.

** Configuring S3 connection in local computer **

Once you have _OpenStack_ and _s3cmd_ installed in your environment, you can download the [allas_conf](https://raw.githubusercontent.com/CSCfi/allas-cli-utils/master/allas_conf)
script to set up the S3 connection to your Allas project. 
```text
wget https://raw.githubusercontent.com/CSCfi/allas-cli-utils/master/allas_conf
source allas_conf --mode s3cmd --user your-csc-username
```
Note that you should use the `--user` option to define your CSC username. The configuration command first asks for your 
CSC password and then for you to choose an Allas project. After that, the tool creates a key file for the S3 connection and stores it in the default location (_.s3cfg_ in home directory).

## Configuring S3 connection in supercomputers

To use _s3cmd_ in Puhti and Mahti, you must first configure the connection:
```text
module load allas
allas-conf --mode s3cmd
```
The configuration process first asks for your CSC password. Then it lists your Allas projects and asks to select the project to be used. The configuration information is stored in the file _$HOME/.s3cfg_. This configuration only needs to be defined once. In the future, _s3cmd_ will automatically use the object storage connection described in the _.s3cfg_ file. If you wish to change the Allas project that _s3cmd_ uses, you need to run the configuration command again.

You can use the S3 credentials, stored in the _.s3cfg_ file, in other services too. You can check the currently used _access key_ and _secret_key_ with command:
```
grep key $HOME/.s3cfg

```

If you use these keys in other services, your should make sure that the keys always remain private. Any person who has access to these two keys, can access and modify all the data that the project has in Allas.

In needed, you can deactivate an S3 key pair with command:

```
allas-conf --s3remove
```



## Create buckets and upload objects

Create a new bucket:
```text
s3cmd mb s3://my_bucket
```

Upload a file to a bucket:
```text
s3cmd put my_file s3://my_bucket
```

## List objects and buckets

List all buckets in a project:
```text
s3cmd ls
```

List all objects in a bucket:
```text
s3cmd ls s3://my_bucket
```

Display information about a bucket:
```text
s3cmd info s3://my_bucket
```

Display information about an object:
```text
s3cmd info s3://my_bucket/my_file
```

## Download objects and buckets

Download an object:
```text
s3cmd get s3://my_bucket/my_file new_file_name
```
The parameter *new_file_name* is optional. It defines a new name for the downloaded file.

Using the command `md5sum`, you can check that the file has not been changed or corrupted:
<pre>
$ <b>md5sum my_file new_file_name</b>
   39bcb6992e461b269b95b3bda303addf  my_file
   39bcb6992e461b269b95b3bda303addf  new_file_name
</pre>
In the above example, the checksums match between the original and downloaded file.

Download an entire bucket:
```text
s3cmd get -r s3://my_bucket/
```

## Move objects

Copy an object to another bucket. Note that should use these commands only for objects that were uploaded to Allas with S3 protocol:
```text
s3cmd cp s3://sourcebucket/objectname s3://destinationbucket
```

For example:
<pre>
$ <b>s3cmd cp s3://bigbucket/bigfish s3://my-new-bucket</b>
remote copy: 's3://bigbucket/bigfish' -> 's3://my-new-bucket/bigfish'
</pre>

Rename the file while copying it:
<pre>
$ <b>s3cmd cp s3://bigbucket/bigfish s3://my-new-bucket/newname</b>
remote copy: 's3://bigbucket/bigfish' -> 's3://my-new-bucket/newname'
</pre>

## Delete objects and buckets

Delete an object:
```text
s3cmd del s3://my_bucket/my_file
```

Delete a bucket:
```text
s3cmd rb s3://my_bucket
```
**Note:** You can only delete empty buckets.

## s3cmd and public objects

In this example, the object _salmon.jpg_ in the pseudo folder _fishes_ is made public:
<pre>
$ <b>s3cmd put fishes/salmon.jpg s3://my_fishbucket/fishes/salmon.jpg -P</b>
Public URL of the object is: https://a3s.fi/my_fishbucket/fishes/salmon.jpg
</pre>


## Giving another project read access to a bucket

You can control access rights using the command `s3cmd setacl `. This command requires the UUID (_universally unique identifier_) of the project you want to grant access to. Project members can check their project ID in <a href="https://pouta.csc.fi/dashboard/identity/" target="_blank">https://pouta.csc.fi/dashboard/identity/</a> or using the command ```openstack project show```. For example in Puhti and Mahti:

```text
module load allas
allas-conf -k --mode s3cmd
openstack project show $OS_PROJECT_NAME
```

In case of _s3cmd_ the read and write access can be controlled for both buckets and objects:

Following command gives project with UUID _3d5b0ae8e724b439a4cd16d1290_ read access to _my_fishbucket_ but not to the objects inside :
```text
s3cmd setacl --acl-grant=read:3d5b0ae8e724b439a4cd16d1290 s3://my_fishbucket
```
Similarly, following command gives write access to just single object:
```text
s3cmd setacl --acl-grant=write:3d5b0ae8e724b439a4cd16d1290 s3://my_fishbucket/bigfish
```
If you want to modify the access permissions of all the objects in a bucket, you can add option `--recursive` to the command:
```text
s3cmd setacl --recursive --acl-grant=read:3d5b0ae8e724b439a4cd16d1290 s3://my_fishbucket
```

You can check the access permissions with _s3cmd info_:
<pre>
$ <b>s3cmd info s3://my_fishbucket|grep -i acl</b>
   ACL:       other_project_uuid: READ
   ACL:       my_project_uuid: FULL_CONTROL
</pre>

Option _--acl-revoke_ can be used to remove a read or write access:
```text
s3cmd setacl --recursive --acl-revoke=read:$other_project_uuid s3://my_fishbucket
```

The shared objects and buckets can be used with both S3 and Swift based tools. Note howerver, that listing
commands show only buckets owned by your project. In the case of shared buckets and objects you must know the 
names of the buckets in order to use them.  

In the case of the example above, user from project _3d5b0ae8e724b439a4cd16d1290_ will not see _my_fishbucket_ , when it is shared, with command:

```text
s3cmd ls
```
However she can list the content of the bucket with command:
```text
s3cmd ls s3://my_fishbucket
```
In the Pouta web UI, user can move to a shared bucket by defining the bucket name in the URL. Move to some 
bucket of your project and replace the bucket name in the end of the URL with the name of the shared bucket:
```
https://pouta.csc.fi/dashboard/project/containers/container/my_fishbucket
```

## Use example

In this example, we store a simple dataset in Allas using s3cmd.

First, create a new bucket. The command `s3cmd ls` reveals that the object storage is empty at first. Then, use the command `s3cmd mb` to create a new bucket called _fish-bucket_.

<pre>
$ <b>s3cmd ls</b>
ls
 
$ <b>s3cmd mb s3://fish-bucket</b>
mb s3://fish-bucket/
Bucket 's3://fish-bucket/' created

$ <b>s3cmd ls</b>
ls
2018-03-12 13:01  s3://fish-bucket
</pre>
It is recommended to collect the data to be stored as larger units and compress it before uploading it to the system.

In this example, we store the Bowtie2 indices and the genome of the zebrafish (danio rerio) in the fish bucket. Running `ls -lh` shows that the index files are available in the current directory:

<pre>$ <b>ls -lh</b>
total 3.2G
-rw------- 1 kkayttaj csc 440M Mar 12 13:41 Danio_rerio.1.bt2
-rw------- 1 kkayttaj csc 327M Mar 12 13:41 Danio_rerio.2.bt2
-rw------- 1 kkayttaj csc 217K Mar 12 13:20 Danio_rerio.3.bt2
-rw------- 1 kkayttaj csc 327M Mar 12 13:20 Danio_rerio.4.bt2
-rw------- 1 kkayttaj csc 1.3G Mar 12 13:13 Danio_rerio.GRCz10.dna.toplevel.fa
-rw------- 1 kkayttaj csc 440M Mar 12 14:03 Danio_rerio.rev.1.bt2
-rw------- 1 kkayttaj csc 327M Mar 12 14:03 Danio_rerio.rev.2.bt2
-rw------- 1 kkayttaj csc 599K Mar 12 13:13 log
</pre>

The data is collected and compressed as a single file using the `tar` command:
```text
tar zcf zebrafish.tgz Danio_rerio*
```

The size of the resulting file is about 2 GB. The compressed file can be uploaded to the fish bucket using the command `s3cmd put`:
<pre>
$ <b>ls -lh zebrafish.tgz</b>
-rw------- 1 kkayttaj csc 9.3G Mar 12 15:23 zebrafish.tgz

$ <b>s3cmd put zebrafish.tgz s3://fish-bucket</b>
put zebrafish.tgz s3://fish-bucket
upload: 'zebrafish.tgz' -> 's3://fish-bucket/zebrafish.tgz'  [1 of 1]
 2081306836 of 2081306836   100% in   39s    50.16 MB/s  done
 
$ <b>s3cmd ls s3://fish-bucket</b>
ls s3://fish-bucket
2019-10-01 12:11 9982519261   s3://fish-bucket/zebrafish.tgz
</pre>

Uploading 2 GB of data takes time. Retrieve the uploaded file:
```text
s3cmd get s3://fish-bucket/zebrafish.tgz
```

By default, this bucket can only be accessed by the project members. However, using the command `s3cmd setacl`, you can make the file publicly available.

First make the fish bucket public:
```text
s3cmd setacl --acl-public s3://fish-bucket
```

Then make the zebrafish genome file public:
```text
s3cmd setacl --acl-public s3://fish-bucket/zebrafish.tgz
```

The syntax of the URL of the file:
```text
https://a3s.fi/bucket_name/object_name
```

In this case, the file would be accessible using the link
_https://a3s.fi/fish-bucket/zebrafish.tgz_


## Publishing objects temporarily with signed URLs

With command _s3cmd signurl_ an object in Allas can be temporarily published with URL that includes security increasing access token.

In the previous example object _s3://fish-bucket/zebrafish.tgz_ was made permanently accessible through simple static URL. 
With _signurl_ the same object could be shared more securely and only for a limited time. For example command:

```text
s3cmd signurl s3://fish-bucket/zebrafish.tgz +3600
```
would print out an URL that remains valid for 3600 s (1 h). In this case URL, produced by the command above, would look something like:
```text
https://fish-bucket.a3s.fi/zebrafish.tgz?AWSAccessKeyId=78e6021a086d52f092b3b2b23bfd7a67&Expires=1599835116&Signature=OLyyCY14s%2F0HxKOOd108mldINyE%3D
```

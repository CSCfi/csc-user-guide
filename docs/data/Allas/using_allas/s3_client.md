
# S3 client


You need to use ec2 credentials when using S3. You can create S3 credentials by sourcing your openrc file as in the instructions in [Pouta documentation](../../../cloud/pouta/install-client.md#configure-your-terminal-environment-for-openstack){:target="_blank"}.

Once you have the RC file, you can add the environment variables with the following command:

```bash
$ source <project_name_here>-openrc.sh
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
Instructions for installing and using s3cmd are given below. For more examples of s3cmd usage, see [s3tools.org](https://s3tools.org/s3cmd-howto){:target="_blank"}.

This chapter gives guidance for the following operations:

 * _Create_ buckets
 * _Upload_ objects
 * _List_ objects and buckets
 * _Download_ objects and buckets
 * _Move_ objects
 * _Delete_ objects and buckets
 * Make a bucket _public_
 * Use s3cmd with _Supercomputers_
 * Manage _access rights_

&nbsp;

## Getting started with s3cmd

Please refer to [http://s3tools.org/download](http://s3tools.org/download){:target="_blank"} and  [http://s3tools.org/usage](http://s3tools.org/usage){:target="_blank"} for upstream documentation.
 
Fedora/RHEL derivatives:
```bash
$ sudo yum install s3cmd
```
Debian derivatives:
```bash
$ sudo apt install s3cmd
```
OSX:
```bash
$ python3 virtualenv
$ pip3 install s3cmd
$ s3cmd
```

You can find your ec2 credentials by issuing:
```bash
$ openstack ec2 credentials list
```
Once you have your ec2 credentials you will need to use the _Access_ and _Secret_ in the next command. The interactive command "_s3cmd --configure_" is good for first-time use. It creates a $HOME/.s3cfg file, adds access keys and ids from above, points to pouta object store and adds an encryption key. It is probably a good idea to create a password when you get to the option. 
 
Alternatively, you can create a working file by adding your Access and Secret to the following oneliner:
```bash
$ s3cmd --configure --access_key=YOUR_EC_ACCESS_KEY_HERE --secret_key=YOUR_EC_SECRET_KEY_HERE --host=object.pouta.csc.fi --region=US --host-bucket='%(bucket)s.object.pouta.csc.fi'
```
Then you need to verify all the settings from the created file.


&nbsp;


## Create buckets and upload objects

You can create a new bucket with command:

```bash
$ s3cmd mb s3://my-bucket
```

Uploading a file into a bucket can be done with command:

```bash
$ s3cmd put my_file s3://my_bucket
```
&nbsp;


## List objects and buckets

You can list buckets belonging to the project with command:
```bash
$ s3cmd ls
```

And objects belonging to a bucket:
```bash
$ s3cmd ls s3://my_bucket
```

To display information about a bucket use command:
```bash
$ s3cmd info s3://my_bucket
```
And information about an object:
```bash
$ s3cmd info s3://my_bucket/my_file
```

&nbsp;


## Download objects and buckets

You can download an object with command:
```bash
$ s3cmd get s3://my_bucket/my_file new_file_name
```
*new_file_name* (optional) defines a name for the downloaded file in case you want to rename it.

With md5sum you can check that the file has not been changed or corrupted:
```bash
$ md5sum my_file new_file_name
   39bcb6992e461b269b95b3bda303addf  my_file
   39bcb6992e461b269b95b3bda303addf  new_file_name
```
Checksums are equal between the original and the downloaded file. So good so far.

You can also download a whole bucket at once with command:
```bash
$ s3cmd get s3://my_bucket/*
```

&nbsp;

## Move objects

You can copy an object to another bucket with command:
```bash
$ s3cmd cp s3://sourcebucket/objectname s3://destinationbucket
```
For example,
```bash
$ s3cmd cp s3://bigbucket/bigfish s3://my-new-bucket
remote copy: 's3://bigbucket/bigfish' -> 's3://my-new-bucket/bigfish'
```

In addition, you can rename the file when copying it:
```bash
$ s3cmd cp s3://bigbucket/bigfish s3://my-new-bucket/new-name
remote copy: 's3://bigbucket/bigfish' -> 's3://my-new-bucket/newname'
```


&nbsp;

## Delete objects and buckets

You can delete an object with command
```bash
$ s3cmd del s3://my_bucket/my_file
```

Deleting a bucket can be done with command:
```bash
$ s3cmd rb s3://my_bucket
```
**Note:** You can only delete empty buckets.

&nbsp;

<a name="s3cmd_public_objects"></a>

## s3cmd and public objects

You can make a bucket public with command:
```bash
$ s3cmd put fishes/salmon.jpg s3://my_fishbucket/fishes/salmon.jpg -P
Public URL of the object is: http://object.pouta.csc.fi/my_fishbucket/fishes/salmon.jpg
```

**Note:** The above client outputs an URL which has http:// (which is not open in the object storage firewall). An URL like this needs to be manually changed to https if such a client is used.

&nbsp;


## s3cmd with Supercomputers

Guidance for using s3cmd with the Supercomputers Taito and Puhti: [s3cmd](./s3cmd.md){:target="_blank"}

&nbsp;


## Giving another project read access to a bucket

"_s3cmd setacl_" command needs to use the UUID (_universally unique identifier_) of the project you want to grant access to.
The ID can be found at <a href="https://pouta.csc.fi/dashboard/identity/" target="_blank">https://pouta.csc.fi/dashboard/identity/</a> or with "_openstack project show $project_name_". You need access (membership) to the project to find out the UUID.
 
In the Pouta Web UI you only see buckets that members of your project have created. If your project has been granted project read access to a bucket with the s3cmd client, the following applies to other members of your project:
 
 * Can list and fetch files with the python-swiftclient 
 * "_swift list_" does <u>not</u> display the bucket
 * "_s3cmd ls_" does display the bucket.
 
Granting read access:
```bash
$ s3cmd setacl --acl-grant=read:$other_project_uuid s3://my_fishbucket
```
Revoking read access:
```bash
$ s3cmd setacl --acl-revoke=read:$other_project_uuid s3://my_fishbucket
```
View permissions:
```bash
$ s3cmd info s3://my_fishbucket|grep -i acl
   ACL:       other_project_uuid: READ
   ACL:       my_project_uuid: FULL_CONTROL
```

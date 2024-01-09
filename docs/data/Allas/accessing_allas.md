# Accessing Allas

## Gaining access

**Allas** access is based on CSC's customer projects. To be able to use Allas, you need to be a member of 
a CSC project that has the permission to use Allas. If you do not have a CSC account, you must first register as a CSC user
and join or start a computing project for which Allas has been enabled. This can be done in the
MyCSC user portal: [https://my.csc.fi]( https://my.csc.fi).

Once you have Allas enabled you can access it from any machine or server that is connected to internet. This can be a your laptop, supercomputer at CSC, virtual machine in cloud or enven your phone.


## Accessing Allas from the web browser

At the moment CSC provides two web browser interfaces for Allas:

The OpenStack Horizon web interface in **cPouta** provides easy-to-use basic functions for data management in Allas. This insterface can only be used for files smaller than 5 GB.

* [Web client – OpenStack Horizon Dashboard](./using_allas/web_client.md)


## Accessing Allas in the CSC computing environment and other Linux platforms

Puhti and Mahti servers at CSC support many different tools for using Allas, These include

* [**a-tools**](./using_allas/a_commands.md) for basic use: (Swift, optionally S3)
* [**rclone**](./using_allas/rclone.md) providing some advanced functions:** (Swift, optionally S3) 
* [**swift**](./using_allas/swift_client.md) python client that provides wide range of functionalities (Swift)
* [**s3cmd**](./using_allas/s3_client.md) an S3 client and persistent Allas connections:** (S3)

Note that the tools listed above utilize two different protocols: _Swift_ and _S3_. Data uploaded using one protocol is not necessary compatible with another protocol. 

The software listed above can be used in other Linux servers as well, e.g. a virtual machine running in cPouta or your own Linux-based laptop. In that case, you need to install the client software and configure the connection to Allas yourself. Instructions : [allas-cli-utils](https://github.com/CSCfi/allas-cli-utils)

In Puhti and Mahti the Allas tools listed above are installed by CSC and provided through _allas_ module.
In order to use Allas in Puhti or Mahti, first load the Allas module:
```text
module load allas
```
Allas access for a specific project can then be enabled:
```text
allas-conf
```
or 
```text
allas-conf project_name
```
The _allas-conf_ command prompts for your CSC password (the same that you use to login to CSC servers). It lists your Allas projects and asks you to define a project (if not already defined as an argument). _allas-conf_ generates an _rclone_ configuration file for the Allas service and authenticates the connection to the selected project. You can only be connected to one Allas project at a time in one session. The project you are using in Allas does not need to match the project you are using in Puhti or Mahti, and you can switch to another project by running _allas-conf_ again.

Authentication information is stored in the shell variables *OS_AUTH_TOKEN* and *OS_STORAGE_URL* and is valid for up to eight hours. However, you can refresh the authentication at any time my running _allas-conf_ again. The environment variables are available only for that login session, so if you start another shell session, you need to authenticate again in there to access Allas.

Once Allas connection is congigured, you can start using Allas with the tools listed above. 

Basic Allas operations with different tools.

| Tool	| List objects in bucket _buck_123_	| Upload file _data1.txt_ to bucket _buck_123_ |	Download file _data1.txt_ from bucket _buck_123_ |
|-------|-----------------------------------|----------------------------------------------|-------------------------------------------------|
| [a-commands](using_allas/a_commands.md) |`a-list buck_123` | `a-put data1.txt -b buck_123` | `a-get buck_123/data1.txt.zst` |
| [rclone](using_allas/rclone.md) |`rclone ls allas:buck_123` | `rclone copy data1.txt allas:buck_123/` |	`rclone copy allas:buck_123/data1.txt ./`| 
| [Swift](using_allas/swift_client.md) |`swift list buck_123` | `swift upload buck_123 data1.txt` |	`swift download buck_123 data1.txt` |
| [s3cmd](using_allas/s3_client.md)\*	 |`s3cmd ls s3://buck_123` |	`s3cmd put data1.txt s3://buck_123/` | `s3cmd get s3://buck_123/data1.txt` |

\*For s3cmd, open Allas connection with command`allas-conf -m s3cmd`



## Accessing Allas with Windows or Mac

In addition to the Web interfaces listed above, you can access Allas from you Windows or Mac computer with locally installed client software. 
For example following tools can be used:

* [Cyberduck](./using_allas/cyberduck.md) provides easy to use graphical interface for moving data between local computer and Allas.
* [Rclone](./using_allas/rclone_local.md) is an command line tool that provides very effective way to use Allas.
* [a-tools](./using_allas/a_commands.md) these Allas specific commands can be installed in Mac OSX machines but not to Windows

The list above is not complete or exclusive. Any tool that supports Swift or S3 protocols can in principle use Allas.

## Copying files directly between object storages

Rclone can also be used to directly copy files from another object storage (e.g. [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html), [Google cloud](https://cloud.google.com/learn/what-is-object-storage), [CREODIAS](https://creodias.eu/cloud/cloudferro-cloud/storage-2/object-storage/),...) to Allas. For this both credentials need to be stored in a Rclone configuration file in the users home directory (`.config/rclone/rclone.conf`). An example is shown below:

```
[s3allas]
type = s3
provider = Other
env_auth = false
access_key_id = xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
secret_access_key = xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
endpoint = a3s.fi
acl = private

[otherobjectstorage]
type = s3
provider = Other
env_auth = false
access_key_id = yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
secret_access_key = yyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
endpoint = yourotherendpoint.com
acl = private
```
The configuration for Allas is added automatically when configuring Allas in s3 mode 

`source allas_conf --mode s3cmd` .

After creating/updating this file, Rclone can be used to copy files

`rclone copy otherobjectstorage:bucket-x/object-y  s3allas:bucket-z/object-a`

or list files from either Allas or the other object storage by using the respective name

`rclone lsf otherobjectstorage: `.

## Other ways of accessing Allas

* [Python](using_allas/python_library.md) Programmatic access to Allas.
   * [Geoscience related examples how Allas can be used in Python scripts](https://github.com/csc-training/geocomputing/tree/master/python/allas)
* [Nextcloud front end](allas-nextcloud.md) Can be set up in Pouta to get additional functionality.
* [R](https://github.com/csc-training/geocomputing/blob/master/R/allas/working_with_allas_from_R_S3.R) (Geoscience related example how Allas can be used in R scripts)





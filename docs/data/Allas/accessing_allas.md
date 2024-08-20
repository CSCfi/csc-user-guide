# Accessing Allas

## Gaining access

**Allas** access is based on CSC's customer projects. To be able to use Allas, you need to be a member of 
a CSC project that has the permission to use Allas. If you do not have a CSC account, you must first register as a CSC user
and join or start a computing project for which Allas has been enabled. This can be done in the
MyCSC user portal: [https://my.csc.fi]( https://my.csc.fi).

Once you have Allas enabled you can access it from any machine or server that is connected to internet. This can be a your laptop, supercomputer at CSC, virtual machine in cloud or enven your phone.


## Accessing Allas from the web browser

At the moment CSC provides several web browser interfaces for Allas:

The **WWW interfaces of Puhti and Mahti** are connected to Allas. 
These interfaces allow you transfer files and directories between your local computer and Allas as well as
between CSC supercomputers and Allas.

* [Instructions for using Allas in Puhti and Mahti web interfaces](../../computing/webinterface/file-browser.md)
* [Puhti web interface](https://www.puhti.csc.fi)
* [Mahti web interface](https://www.mahti.csc.fi)


The OpenStack Horizon web interface in **cPouta** provides easy-to-use basic functions for data management in Allas. This interface can only be used for files smaller than 5 GB.

* [Web client – OpenStack Horizon Dashboard](./using_allas/web_client.md)
* [cPouta Web Interface](https://pouta.csc.fi)


**SD Connect** provides an interface for storing and sharing sensitive data. 
This service is based on Allas but we don't recommend it for other than sensitive data.

* [SD Connect instructions](../sensitive-data/sd_connect.md)
* [SD Connect interface](https://sd-connect.csc.fi)



## Accessing Allas in the CSC computing environment and other Linux platforms

CSC supercomputers Puhti and Mahti support many different command line tools for using Allas, These include

* [**a-tools**](./using_allas/a_commands.md) for basic use: (Swift, optionally S3)
* [**rclone**](./using_allas/rclone.md) providing some advanced functions:** (Swift, optionally S3) 
* [**swift**](./using_allas/swift_client.md) python client that provides wide range of functionalities (Swift)
* [**s3cmd**](./using_allas/s3_client.md) an S3 client and persistent Allas connections:** (S3)

Note that the tools listed above utilize two different protocols: _Swift_ and _S3_. Data uploaded using one protocol is not necessary compatible with another protocol. 

The software listed above can also be used on other devices, for example a virtual machine running in cPouta or your own laptop.

In Puhti and Mahti the Allas tools listed above are installed by CSC and provided through _allas_ module.
In order to use Allas in Puhti or Mahti, first load the Allas module:
```text
module load allas
```
Allas access for a specific project using swift protocol can then be enabled:
```text
allas-conf
```
To enable S3 protocol, use option `-m S3`
```text
allas-conf -m S3
```
The `allas-conf` command prompts for your CSC password (the same that you use to login to CSC servers). It lists your Allas projects and asks you to define a project (if not already defined as an argument). `allas-conf` generates an `rclone` configuration file for the Allas service and authenticates the connection to the selected project. `allas-conf` enables you to use only one Allas project at a time in one session. The project you are using in Allas does not need to match the project you are using in Puhti or Mahti, and you can switch to another project by running `allas-conf` again.

In the case of the Swift protocol, the authentication information is stored in the `OS_AUTH_TOKEN` and `OS_STORAGE_URL` environment variables and is valid for up to eight hours. However, you can refresh the authentication at any time by running `allas-conf` again. The environment variables are set only for the current login session, so you need to configure authentication individually for each shell with which you wish to access Allas.

In the case of the S3 protocol, the authentication information is stored in configuration files located in your home directory on the device. The same authentication is used for all login sessions and it does not have an expiration time.

Once an Allas connection is configured, you can start using the object storage with the tools listed above. 

Basic Allas operations with different tools.

| Tool	| List objects in bucket _buck_123_	| Upload file _data1.txt_ to bucket _buck_123_ |	Download file _data1.txt_ from bucket _buck_123_ |
|-------|-----------------------------------|----------------------------------------------|-------------------------------------------------|
| [a-commands](using_allas/a_commands.md) |`a-list buck_123` | `a-put data1.txt -b buck_123` | `a-get buck_123/data1.txt.zst` |
| [rclone (swift)](using_allas/rclone.md) |`rclone ls allas:buck_123` | `rclone copy data1.txt allas:buck_123/` |	`rclone copy allas:buck_123/data1.txt ./`|
| [rclone (S3)](using_allas/rclone.md) |`rclone ls s3allas:buck_123` | `rclone copy data1.txt s3allas:buck_123/` |	`rclone copy s3allas:buck_123/data1.txt ./`|
| [Swift](using_allas/swift_client.md) |`swift list buck_123` | `swift upload buck_123 data1.txt` |	`swift download buck_123 data1.txt` |
| [s3cmd](using_allas/s3_client.md)\*	 |`s3cmd ls s3://buck_123` |	`s3cmd put data1.txt s3://buck_123/` | `s3cmd get s3://buck_123/data1.txt` |



## Accessing Allas with Windows or Mac

In addition to the Web interfaces listed above, you can access Allas from you Windows or Mac computer with locally installed client software. 
For example following tools can be used:

* [Cyberduck](./using_allas/cyberduck.md) provides easy to use graphical interface for moving data between local computer and Allas.
* [Rclone](./using_allas/rclone_local.md) is a command line tool that provides a very effective way to use Allas on any operating system.
* [a-tools](./using_allas/a_commands.md) are Allas-specific commands that can be installed on macOS and Linux devices, but not ones running a Windows operating system.

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

* Python:
   * [Python with SWIFT](using_allas/python_swift.md)
   * [Python with S3 with `boto3`](using_allas/python_boto3.md).
   * [Geoscience related examples how Allas can be used in Python scripts](https://github.com/csc-training/geocomputing/tree/master/python/allas)
* [Nextcloud front end](allas-nextcloud.md) Can be set up in Pouta to get additional functionality.
* R
  * [aws.s3 R package](https://cloud.r-project.org/web/packages/aws.s3/index.html) can be used for working with Allas with S3 protocol
  * [Geoscience related example how Allas can be used in R scripts](https://github.com/csc-training/geocomputing/blob/master/R/allas/working_with_allas_from_R_S3.R), inc. aws.s3 set up.





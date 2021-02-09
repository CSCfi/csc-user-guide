# The Allas object storage

This Allas object storage service user guide consists of three parts:

## [Introduction](./introduction.md)

A technical overview of the service. Recommended reading before starting to use Allas.

   * [Common use cases](./using_allas/common_use_cases.md)

## [Accessing Allas](./accessing_allas.md)

A summary of the most commonly used Allas tools.

### Graphical user interfaces

   * [web client](using_allas/web_client.md) A part of the Pouta www interface. Limited performance. No configuration steps needed.
   * [CyberDuck](accessing_allas.md#cyberduck-functions) An easy-to-use graphical object storage client for Windows and MacOS.


### Command line tools 
Available in Puhti and Mahti. These can be installed to local Linux and Mac OSX too.

   * [a-commands](using_allas/a_commands.md) Easy-to-use command line tools developed for using Allas in the CSC computing environments.
   * [rclone](using_allas/rclone.md) A versatile command line client for Allas and other object storage systems. 
   * [Swift](using_allas/swift_client.md) A native Swift command line client. 
   * [s3cmd](using_allas/s3_client.md) A command line client for the S3 protocol. 
   * [Python](using_allas/python_library.md) Programmatic access to Allas.

### Sample commands for Puhti and Mahti 
Open connection:

```text
module load allas
allas-conf
```

Basic Allas operations with different tools.

| Tool	| List objects in bucket _buck_123_	| Upload file _data1.txt_ to bucket _buck_123_ |	Download file _data1.txt_ from bucket _buck_123_ |
|-------|-----------------------------------|----------------------------------------------|-------------------------------------------------|
| [a-commands](using_allas/a_commands.md) |`a-list buck_123` | `a-put data1.txt -b buck_123` | `a-get buck_123/data1.txt.zst` |
| [rclone](using_allas/rclone.md) |`rclone ls allas:buck_123` | `rclone copy data1.txt allas:buck_123/` |	`rclone copy allas:buck_123/data1.txt ./`| 
| [Swift](using_allas/swift_client.md) |`swift list buck_123` | `swift upload buck_123 data1.txt` |	`swift download buck_123 data1.txt` |
| [s3cmd](using_allas/s3_client.md)\*	 |`s3cmd ls s3://buck_123` |	`s3cmd put data1.txt s3://buck_123/` | `s3cmd get s3://buck_123/data1.txt` |

\*For s3cmd, open Allas connection with command`allas-conf -m s3cmd`

Other information

   * [Error messages](./using_allas/error_messages.md)
   * [Directory errors](./using_allas/directory_object_error.md )
   
## [Allas and cPouta object storage, what has changed?](./allas_cpouta_change.md) 
CSC has previously provided the Pouta object storage service that is now merged to the Allas service. This chapter explains the changes that this merging causes to existing Pouta object storage users.

### Tutorials: 

* [Using Allas interactively in Puhti and Mahti](./allas-examples.md) 
* [Using Allas in batch jobs](./allas_batchjobs.md)
* [Using Allas to host a data set for a research group](./allas_project_example.md)
* [Tools for client side encryption for Allas](./allas_encryption.md)
* [Accessing HPC-archive data in Allas](./hpc-archive.md)


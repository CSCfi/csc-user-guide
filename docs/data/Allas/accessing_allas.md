# Accessing Allas


![Allas access clients](img/allas-access-flavors.png)

The four main options for accessing Allas are:

* Web browser interfaces 
* Command-line tools 
* Graphical tools
* Other tools: Python and R libraries etc

The tool lists below are not complete or exclusive. Any tool that supports Swift or S3 protocols can in principle use Allas.
You can cross-use the Allas clients as long as you access Allas with the same protocol (Swift or S3).

When choosing the tool for accessing Allas, consider:

* Ease of getting started: web interfaces do not need installation and the connection configuration is easy.
* Ease of use: web interface and graphical tools are in general easier to get started for basic tasks.
* The amount of data you have to move, the web interfaces are not suitable for for big data transfers.
* Your other workflow, Python or R libraries may be useful, if you use these programming languages already for other tasks.
* The operating system of your local machine, some command-line and graphical tools support only Linux/Mac or Windows.
* [Allas protocol](introduction.md#protocols) of your choice, many of the command-line and graphical tools support only SWIFT or S3. 
* Packaging of files, in case of moving many filea, `a-tools` packages them by default to a .tar file and adds metadata, other tools usually move files as they are.
* Sensitity of your data, for sensitive data use [tools that support client side encryption](allas_encryption.md).

To use Allas from Puhti or Mahti, see [Tutorial for using Allas in CSC supercomputers](allas-hpc.md).

## Web browser interfaces

At the moment CSC provides several web browser interfaces for Allas:

**Allas Web UI** is a web-based interface designed to simplify the management of object storage in Allas. It provides an intuitive way to interact with your data without needing command-line tools.  
It is an ideal option for users who prefer a visual interface over command-line tools for basic object storage operations.  

* [Allas Web UI Guide](./using_allas/allas-ui.md)  
* [Access Allas Web UI](https://allas.csc.fi)  

It allows users to create and manage buckets, upload and download objects (up to 5 GiB per file), and configure sharing permissions. 

The **web-interfaces of Puhti and Mahti** are connected to Allas. 
These interfaces allow you to transfer files and directories between your local computer and Allas as well as
between CSC supercomputers and Allas.

* [Instructions for using Allas in Puhti and Mahti web interfaces](../../computing/webinterface/file-browser.md)
* [Puhti web interface](https://www.puhti.csc.fi)
* [Mahti web interface](https://www.mahti.csc.fi)


The OpenStack Horizon web interface in **cPouta** provides easy-to-use basic functions for data management in Allas. 

* [Web client – OpenStack Horizon Dashboard](./using_allas/web_client.md)
* [cPouta Web Interface](https://pouta.csc.fi)

This interface can only be used for files smaller than 5 GB and uploading/downloading only a single file at a time. 


**SD Connect** provides an interface for storing and sharing sensitive data. 
This service is based on Allas but we don't recommend it for other than sensitive data.

* [SD Connect instructions](../sensitive-data/sd_connect.md)
* [SD Connect interface](https://sd-connect.csc.fi)

## Commandline tools

To access Allas with **command line commands**, client software supporting the _Swift_ or _S3_ protocol is required. This is the most flexible way to access Allas, but it is a little bit more complicated to get started.  

| Tools | SWIFT support | S3 support | Linux/Mac | Windows |
| ----- | ------------- | ---------- | --------- | ------- |
| [a-commands](./using_allas/a_commands.md) | <font color="green">&#x2714;</font> | - | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> |
| [rclone](./using_allas/rclone.md)  | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> |  <font color="green">&#x2714;</font> | 
| [swift python-swiftclient](./using_allas/swift_client.md) | <font color="green">&#x2714;</font> |   | <font color="green">&#x2714;</font> |   |
| [s3cmd](./using_allas/s3_client.md) |  | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> |   |
| [aws-cli](https://s3browser.com/) |   | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> |

Additionally for exmple `curl` and `wget` can be used for downloading public objects or objects with temporary URLs.

Basic Allas operations with different tools.

| Tool	| List objects in bucket _buck_123_	| Upload file _data1.txt_ to bucket _buck_123_ |	Download file _data1.txt_ from bucket _buck_123_ |
|-------|-----------------------------------|----------------------------------------------|-------------------------------------------------|
| [a-commands](using_allas/a_commands.md) |`a-list buck_123` | `a-put data1.txt -b buck_123` | `a-get buck_123/data1.txt.zst` |
| [rclone (swift)](using_allas/rclone.md) |`rclone ls allas:buck_123` | `rclone copy data1.txt allas:buck_123/` |	`rclone copy allas:buck_123/data1.txt ./`|
| [rclone (S3)](using_allas/rclone.md) |`rclone ls s3allas:buck_123` | `rclone copy data1.txt s3allas:buck_123/` |	`rclone copy s3allas:buck_123/data1.txt ./`|
| [Swift](using_allas/swift_client.md) |`swift list buck_123` | `swift upload buck_123 data1.txt` |	`swift download buck_123 data1.txt` |
| [s3cmd](using_allas/s3_client.md)\*	 |`s3cmd ls s3://buck_123` |	`s3cmd put data1.txt s3://buck_123/` | `s3cmd get s3://buck_123/data1.txt` |



## Graphical tools

| Tools | SWIFT support | S3 support | Linux/Mac | Windows |
| ----- | ------------- | ---------- | --------- | ------- |
| [Cyberduck](./using_allas/cyberduck.md) | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> |
| [WinSCP](https://winscp.net/eng/index.php)  |  | <font color="green">&#x2714;</font> |  |  <font color="green">&#x2714;</font> | 
| [S3browser](https://s3browser.com/) |  |  <font color="green">&#x2714;</font> |  | <font color="green">&#x2714;</font>  |

WinSCP has generally rather slow data transfer speed for S3, so likely not suitable for bigger amounts of data.

## Other tools: Python and R libraries etc

* Python:
   * [Python with SWIFT](using_allas/python_swift.md)
   * [Python with S3 with `boto3`](using_allas/python_boto3.md).
   * [Geoscience related examples how Allas can be used in Python scripts](https://github.com/csc-training/geocomputing/tree/master/python/allas)
* [Nextcloud front end](allas-nextcloud.md) Can be set up in Pouta to get additional functionality.
* R
  * [aws.s3 R package](https://cloud.r-project.org/web/packages/aws.s3/index.html) can be used for working with Allas with S3 protocol
  * [Geoscience related example how Allas can be used in R scripts](https://github.com/csc-training/geocomputing/blob/master/R/allas/working_with_allas_from_R_S3.R), inc. aws.s3 set up.

These Python and R libraries can be installed to all operating systems.

## Clients comparison

A _web client_ is suitable for using the basic functions. *a-commands* offer easy-to-use functions for using Allas either via a personal computer or supercomputer. Power users might want to consider the clients _rclone_, _Swift_ and _s3cmd_. The table displays the core functions of the power clients concerning data management in Allas.

| | Allas Web UI | a-commands | rclone | Swift | s3cmd |
| :----- | :-----: | :----: | :----: | :-----: | :----: |
| Usage | _Basic_ | _Basic_ | _Power_ |_Power_ | _Power_ |
| **Create buckets** | <font color="green">&#x2714;</font> |<font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> |
| **Upload objects** | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> |
| **List** | | | | | |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; objects | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; buckets | <font color="green">&#x2714;</font>  | <font color="green">&#x2714;</font>| <font color="green">&#x2714;</font>  | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font>  |
| **Download** | | | | |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; objects | <font color="green">&#x2714;</font> |<font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; buckets | <font color="green">&#x2714;</font> | |<font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> |
| **Remove** | | | | | |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; objects | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; buckets | <font color="green">&#x2714;</font>&#8226;&#8226; | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font>&#8226;&#8226; |
| **Managing access rights** | | | | |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; public/private |  | <font color="green">&#x2714;</font>| | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; read/write access</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; to another project | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | | <font color="green">&#x2714;</font>| <font color="green">&#x2714;</font> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; temp URLs | | | | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> |
| **Set lifecycle policies** | | | | | <font color="green">&#x2714;</font> |
| **Move objects** | | | | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> |
| **Edit metadata** | | | | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> |
| **Download whole project** | | | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | |
| **Remove whole project** | | | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | |

<div align="right">&#8226;&#8226; Only empty buckets</div>

## Files larger than 5 GB

Files larger than 5 GB are divided into smaller segments during upload. 

* Most tools split large files automatically
* With _Swift_, you can use the _Static Large Object_: [swift with large files](./swift_client.md#files-larger-than-5-gb)

After upload, s3cmd connects these segments into one large object, but in case of swift based uploads (a-put, rclone , swift) the large files are also stored as several objects. This is done automatically to a bucket that is named by adding extension `_segments` to the original bucket name. For example, if you would use _a-put_ to upload a large file to bucket _123-dataset_ the actual data would be stored as several pieces into bucket _123-dataset_segments_. The target bucket _123_dataset_ would contain just a front object that contains information what segments make the stored file. Operations performed to the front object are automatically reflected to the segments. Normally users don't need to operate with the _segments_ buckets at all and objects inside these buckets should not be deleted or modified. 

It is important not to mix Swift and S3, as these protocols are not fully mutually compatible.
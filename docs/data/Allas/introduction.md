
# Introduction to Allas Storage service

&nbsp;


## What is Allas?

**Allas** is part of the _CSC storage portfolio_ and accessible from anywhere on the Internet. We provide various tools (see [Clients](./accessing_allas.md#clients){:target="_blank}) for storing and accessing your data. CSC can also work with you to solve comprehensive data management needs or support large scale data transfer cases.

Allas Object Storage is a storage service to host data for a project lifetime. The data from Allas can also be shared via Internet. Allas cannot be used directly for computing, but CSC computing environments (**Mahti** and **Puhti**) support easy data movements to and from Allas. **Please note:** The files which have not been touched in 90 days will automatically be cleaned from project's [Lustre scratch](../../computing/disk-environment.md){:target="_blank"} (similar mechanism was used in [Taito WRKDIR](https://research.csc.fi/taito-disk-environment#1.5.2){:target="_blank"}) and therefore the data must be moved to Allas after computing.

Allas is a modern object storage system - it comes with _S3_ and _Swift_ interfaces on _CEPH_ storage. In practice, this means that instead of files, the data is stored as objects within buckets. A bucket is simply a container for objects that may also include metadata describing the bucket. 

In [OpenStack Horizon web interface](./using_allas/web_client.md){:target="_blank"} objects and buckets can be created, deleted or updated. Objects can be either private (accessible only by project members) or public (accessible by anyone from Internet). The command-line options are far more richer on managing metadata and accessing to the buckets and objects. Examples of how to use buckets and objects within Allas are available below.

&nbsp;


## Allas Object Storage related terms and concepts  

&nbsp;

**Access Control List**

_Access Control List_ (ACL) mechanism can be used to control access to other Allas users.

&nbsp;


**Billing unit**

_Billing units_ describe the consumption of computing and storage resources on CSC systems. 
In Allas, the amount of data consumes billing units.
(See [Billing and Quotas](#billing-and-quotas))

&nbsp;


**Bucket**

A _bucket_ is simply a container for objects that may also include metadata describing the bucket.

&nbsp;

<a id="checksum"></a>

**Checksum**

_Checksum_ is a hashed string computed of an object to observe if the object has changed (data integrity). 
You can get the checksum with command _md5sum_.

&nbsp;


**Client**

_Client software_ is used to access the object storage service (Allas).

 * Web browser based access via _OpenStack Horizon_ for basic graphical usage (see [Web client](./using_allas/web_client.md){:target="_blank"})
 * Command-line clients such as _Swift_ and _s3cmd_ for power users (see [Swift client](./using_allas/swift_client.md){:target="_blank"} and [S3 client](./using_allas/s3_client.md){:target="_blank"})
 * _Programmable interface_ (API) for those who integrate software

&nbsp;


**Metadata**

_Metadata_ describes an object or bucket and it could be used, for example, to search objects. 
The basic usage is via _key-value_ pair (for example, name: John).

&nbsp;


**Object Storage**

_Object storage_ refers to a computer data storage that manages data as objects instead of files or blocks. Typically, an object consists of the data itself, metadata and a unique identifier. Generally, the data can be anything, for example an image or audio.

&nbsp;


**OpenStack**

_OpenStack cloud management middleware_ can be used to access Allas.
_Horizon web user interface_ offers some basic functionalities (see [Web client](./using_allas/web_client.md){:target="_blank"}).
For further information, see [OpenStack](https://www.openstack.org/){:target="_blank"}.

&nbsp;


**Pseudo-folder**

You cannot have buckets with other buckets inside them. You can however make use of so called _pseudo-folders_.

If an object name contains a forward slash "/", it is interpreted as a folder separator. These are shown as folders listings when accessing the data through Pouta web interface. These pseudo-folders are automatically added if you upload whole folders with command-line clients.

For example, if you add two objects to a bucket
```bash
fishes/salmon.png
fishes/bass.png
```
listing the bucket will show a folder called "_fishes_" and the two files within it.

&nbsp;


**Quota**

_Allas quota_ defines the maximum amount of data (capacity) which the project is allowed to store in Allas. 
(See [Billing and Quotas](#billing-and-quotas))

&nbsp;


## System Characteristics


The stored objects can be any data type, such as images or compressed data files. In general, you can think of objects as files. Object storage is generally used for different purposes than many other storage solutions. It has benefits but also limitations.

**Benefits**

 * The object storage can handle practically any static data
 * The data can be accessed from anywhere using the same URL
 * The data can have different levels of access control


**Limitations**

 * Object storage cannot be properly mounted on virtual machines. There are some tools to help this, but they have their limitations. For example, _svfs_ can be used to mount _swift_ as filesystem but it uses _FUSE_ which is slow
 * Unsuitable for objects/files that change during their lifetime (e.g. most databases)
 * The data cannot be modified while it is in Allas. It must be downloaded to a server for processing and then you can replace the previous version with the new one

More about the functionalities of Allas can be found from chapter [Using Allas](./using_allas/common_use_cases.md){:target="_blank"}.

The objects are stored in buckets. A bucket is simply a container for objects. These buckets should not be confused with _dockers_, or other containers used for computing. A bucket basically acts like a filesystem directory, but you can have only one level of them, so you cannot have buckets within buckets.

Each bucket has a name, which must be unique across all users. So if somebody else has a bucket called "_test_", you cannot create a bucket called "_test_". All the bucket names are public, so please <u>do not</u> put private information in the bucket name. You may use, for example, your project id in the bucket name, for example, _2000620-raw-data_.

URLs to objects can be in DNS format: _https://object.pouta.csc.fi/bucketname/objectname_ - for this reason use a valid DNS name (RFC 1035) for the bucket. Specifically, we recommend not using upper case characters or Scandic letters (&auml;, &ouml;, etc.) in the bucket name.

Data is spread across different servers, which protects against disk and server failures. **Please note:** This does not protect from e.g. accidental deletion, and you should still make backups of important data.

&nbsp;


## Billing and Quotas

Allas usage is based on project based storage quotas. All the project members have equal access rights to the storage area that has been granted for the project. In practice, this means that if one project member uploads data to Allas, all the other project members can read and also delete the data. Allas itself does not store any information about who has uploaded the data to Allas.

The default quotas for every project are:

| Resource | Limit |
| :-------- |:------- |
| Storage amount | 1 TiB |
| Buckets per project | 1000 |
| Objects per bucket | 100 000 |
| Object size | 5 GB |


Storing data in Allas consumes _billing units_. Accounting and billing information can be found under [Accounting principles and quotas](https://research.csc.fi/pouta-accounting){:target="_blank"}.

Unlike most other object storage providers, CSC does <u>not</u> charge for object storage network transfers or API calls.

&nbsp;

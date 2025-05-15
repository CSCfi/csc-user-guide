
# Introduction to the Allas storage service

## What is Allas?

**Allas** is CSC's general purpose research data storage server. It is a part of the CSC storage portfolio and can be accessed on the CSC servers as well as from anywhere on the internet. Allas can be used both for static research data that needs to be available for analysis and to collect and host cumulating or changing data. A CSC project is required to import data to Allas. Allas can be used to host data for as long as the CSC project is active.

From the technical point of view, Allas is a modern object storage system. It comes with the _S3_ and _Swift_ interfaces on a _CEPH_ storage. In practice, this means that instead of files, the data is stored as objects in buckets. A bucket is a container for objects that may also include metadata describing the bucket.

The stored objects can be of any data type, such as images or compressed data files. In general, objects are similar to files. The object storage can be used for a variety of purposes. It has benefits but also limitations.

**Benefits**

 * The object storage can handle practically any static data.
 * The data can be accessed from anywhere using the URL.
 * The data can have different levels of access control.
 * The data can have lifecycle policy set.
 * You can access Allas from any machine or server that is connected to internet. This can be a your laptop, supercomputer at CSC, virtual machine in cloud or enven your phone.

**Limitations**

 * Specific tools are required to use the object storage. The object storage cannot be properly mounted for local disk-like usage. There are some tools that can do this, but they have their limitations. For example, _svfs_ can be used to mount _Swift_ as a file system, but it uses _FUSE_ which is slow.
 * It is unsuitable for files that change constantly during their lifetime (e.g. most SQL databases).
 * The data cannot be modified while it is in Allas. It must be downloaded to a server for processing, and the previous version replaced with a new one.
 * In case of swift protocol, files larger than 5 GB are divided into smaller segments. Normally, this is done automatically during the upload. See [Files larger than 5 GB](./using_allas/common_use_cases.md#files-larger-than-5-gb).

See also the [common use cases](./using_allas/common_use_cases.md).

## System characteristics

In Allas, objects are stored in buckets. A bucket is a data object container. Buckets should not be confused with _dockers_ or other computing containers. A bucket functions similarly to a file system directory, except that there can only be one level, i.e. buckets cannot contain other buckets.

![Allas projects and buckets](img/allas_projects_and_buckets.PNG)
**Figure** Data structure in Allas

## Gaining access

To be able to use Allas, you need to have:

* [CSC account](../../accounts/how-to-create-new-user-account.md)
* [CSC a computing project](../../accounts/how-to-create-new-project.md) for which [Allas service has been enabled](../../accounts/how-to-add-service-access-for-project.md)


## Billing and quotas

Allas usage is based on CSC projects. All project members have equal access rights to the storage area that has been granted for the project. In practice, this means that if one project member uploads data to Allas, all other project members can also read, edit and delete the data. Allas itself does not store any information about who has uploaded the data to Allas.

The default quota for a new project is 10 TB, but that can be increased if needed. Allas is the preferred storage site for any large datasets in the CSC environment, so you should not hesitate to request a larger quota for Allas, if you work with larger data sets.

To increase your Allas quota, please send a request to: `servicedesk@csc.fi`
In the request, define what Allas project you are using, how large storage space is needed and what kind of data will be stored to Allas.

Note that the data stored in Allas
[consume billing units of the project](../../accounts/billing.md).


**The default quotas for projects:**

| Resource | Limit |
| :-------- |:------- |
| Storage amount | 10 TiB |
| Buckets per project | 1 000 |
| Objects per bucket | 500 000 |

The maximum for the "Objects per bucket" quota is 500 000. By exeeding the limit you might get your bucket in a situation where you can't make any operations. If you need more objects than this, please plan on spreading the objects across multiple buckets. Spreading data to multiple buckets will give a better performance whenever writing objects.

Storing data in Allas consumes _billing units_. In Allas, billing is based on the amount of data stored. The rate is 1 BU/TiBh, i.e. 1 TB of data stored in Allas consumes 24 BU in a day and 8760 BU in a year.

Unlike most other object storage providers, CSC does <u>not</u> charge for object storage network transfers or API calls.


## Different ways to use Allas

Allas can be used from CSC computing environment or any other laptop or server connected to Internet. There are many tools for working with Allas:

![Allas access clients](img/allas-access-flavors.png)

* Web browser interfaces
* Command-line tools
* Graphical locally installed tools
* Other tools: Python and R libraries etc

[The accessing Allas page](accessing_allas.md) describes the different options in detail.


## Protocols

The object storage service is provided over two different protocols, _Swift_ and _S3_. From the user perspective, one of the main differences between S3 and Swift is authentication. The token-based Swift authentication used in Allas remains valid for eight hours at a time, but in the key-based S3, the connection can stay permanently open. The permanent connection of S3 is practical in many ways, but it includes a security aspect: if the server where Allas is used is compromised, the object storage space will be compromised as well.

Due to this security concern, Swift is the recommended protocol for multiple-user servers such as Mahti and Puhti. Thus, for example, the CSC-specific _a-commands_, as well as the standard _rclone_ configuration in Puhti and Mahti, are based on Swift. However, in some cases, the permanent connections provided by the S3 protocol may be the most reasonable option, for example, in personal virtual machines running in cPouta.

The Swift and S3 protocols are <u>not</u> mutually compatible when handling objects. For small objects that do not need to be split during the upload, the protocols can be used interchangeably, but split objects can be accessed only with the protocol that was used for uploading them. The size limit for splitting an object depends on the settings and protocol. The limit is typically between 500 MB and 5 GB.

Generic recommendations for selecting the protocol:

 * If possible, use the _Swift_ protocol. It is better supported.
 * In any case, choose only one of the protocols. Do not mix _S3_ and _Swift_.
 * It is better to store a few large objects than many small objects.
 * Using over 100 GB objects may cause problems because of long upload/download times.
 
Note, that some [Allas clients](accessing_allas.md) support only one of these protocols.



## Naming buckets

Each bucket has a name that must be unique across all Allas users. If another user has a bucket called "_test_", another bucket called "_test_" cannot be created. All bucket names are public, so please do <u>not</u> include any confidential information in the bucket names. You may, for example, use your project ID, e.g. _2000620-raw-data_.

Object URLs can be in the DNS format, e.g. _https://a3s.fi/bucketname/objectname_. Please use a valid DNS name (RFC 1035). We recommend not using upper case or non-ASCII (&auml;, &ouml; etc.) characters.

It is <u>not</u> possible to rename a bucket.

The data is spread across various servers, which protects against disk and server failures. **Please note:** This does not protect the data from e.g. accidental deletion. Please make regular backups of important data.

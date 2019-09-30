
# Introduction to Allas storage service

&nbsp;


## What is Allas?

**Allas** is CSCs' general purpose storage server for research data. It is part of the CSC storage portfolio and it can be used from the CSC servers as well as from anywhere on the Internet. Allas can be used both for static research data that needs to be available for analysis as well as to collect and host data that is cumulating and/or changing from time to time. To be able to import data to Allas you must have a project at CSC. Allas can be used to host your data as long as your CSC project is active. 

From technical point of view, Allas is a modern object storage system - it comes with _S3_ and _Swift_ interfaces on _CEPH_ storage. In practice, this means that instead of files, the data is stored as objects within buckets. 
A bucket is simply a container for objects that may also include metadata describing the bucket. 

The stored objects can be of any data type, such as images or compressed data files. In general, you can think of objects as files. Object storage can be used for many different purposes. It has benefits but also limitations.

**Benefits**

 * The object storage can handle practically any static data.
 * The data can be accessed from anywhere using URL.
 * The data can have different levels of access control.


**Limitations**

 * You have to use specific tools to use object storage. Object storage cannot be properly mounted for local disk-like usage. There are some tools to help this, but they have their limitations. For example, _svfs_ can be used to mount _Swift_ as filesystem, but it uses _FUSE_ which is slow.
 * Unsuitable for files that change constantly during their lifetime (e.g. most SQL databases).
 * The data cannot be modified while it is in Allas. It must be downloaded to a server for processing and then you can replace the previous version with the new one.
 * Files larger than 5 GB must be divided into smaller segments ( normally this is done automatically during upload), see [Files larger than 5 GB](./using_allas/common_use_cases.md#files-larger-than-5-gb){:target="_blank"}.


## Different flavors for using Allas

You cannot mount Allas direcly to a computer.  This means that in order to use Allas you need software tools to access it. There are four flavors of tools to access Allas:

![Allas access flavors](/img/allas-access-flawors.png)

1. In CSC computing environment (e.g. **Puhti**) you have ready-to-use tools, provided by CSC, to access Allas. The tools are mostly the same you could also install to your local environment.  
In the CSC computing environment Allas should be used to store any data that needs to be preserved for longer than just few weeks. Supercomputer's own storage has a policy to delete idle data (see [Computing disk environment](../../computing/disk-environment.md){:target="_blank}), so your data must be moved to Allas after computing. The instructions for accessing and using Allas with CSC's supercomputers can be found from [Using Allas with Supercomputers](./using_allas/common_use_cases.md#using-allas-with-supercomputers){:target="_blank"}.

2. WWW access to Allas is provided by the web interface of cPouta cloud environment [https://pouta.csc.fi](https://pouta.csc.fi). To access Allas with a browser you naturally do not have to install anything special on your computer, so this is by far the simplest way to access Allas. On the other hand, the browser user interface has a bunch of limitations compared to other access flavors, most notable are less performance and upload/download only a single file at the time. The instructions for accessing and using Allas with a browser can be found from [OpenStack Horizon web interface](./using_allas/web_client.md){:target="_blank"}.

3. To access Allas with a GUI client you have to install a suitable GUI client in to your server/laptop. The client needs to be capable to use Swift or S3 access protocol. Instructions to use one such client can be found from [Accessing Allas with Windows and Mac](./accessing_allas.md#accessing-allas-with-windows-and-mac){:target="_blank"}.

4. To access Allas with command-line commands you need to install Swift or S3 protocol supporting client software in to your server/laptop. This is the most flexible way to access Allas, but it requires more effort from you than other access flavors. Instructions to use one such client can be found from [Accessing Allas with Linux](./accessing_allas.md#accessing-allas-with-linux){:target="_blank"} and [Protocols](./accessing_allas.md#protocols){:target="_blank"}.

In addition to these access flavors you can also see how to use Allas based on [Common Use Cases](./using_allas/common_use_cases.md){:target="_blank"}.


&nbsp;


## Billing and Quotas

Allas usage is founded on project based storage quotas. The default quota for a new project is 10 TB, but that can be increased if needed. Allas is the preferred storage site for any large datasets in CSC environment, so you should not hesitate to request larger quota for Allas, if you need to work with larger data sets. 

All the project members have equal access rights to the storage area that has been granted for the project. In practice, this means that if one project member uploads data to Allas, all the other project members can read, edit and also delete the data. Allas itself does not store any information about who has uploaded the data to Allas.

The default quotas for every project are:

| Resource | Limit |
| :-------- |:------- |
| Storage amount | 10 TiB |
| Buckets per project | 1 000 |
| Objects per bucket | 100 000 |


Storing data in Allas consumes _billing units_. Accounting and billing information can be found under [Accounting principles and quotas](https://research.csc.fi/pouta-accounting){:target="_blank"}.

Unlike most other object storage providers, CSC does <u>not</u> charge for object storage network transfers or API calls.

&nbsp;



## System Characteristics

The objects are stored in buckets. A bucket is simply a container for objects. These buckets should not be confused with _dockers_, or other containers used for computing. A bucket basically acts like a filesystem directory, but you can have only one level of them, so you cannot have buckets within buckets.

![Allas projects and buckets](/img/allas_projects_and_buckets.PNG)
**Figure** Data structure in Allas

Each bucket has a name, which must be unique across all Allas users. So, if somebody else has a bucket called "_test_", you cannot create a bucket called "_test_". All the bucket names are public, so please do <u>not</u> put private information in the bucket name. You may use, for example, your project id in the bucket name, such as _2000620-raw-data_.

URLs to objects can be in DNS format: _https://object.pouta.csc.fi/bucketname/objectname_ - for this reason use a valid DNS name (RFC 1035) for the bucket. Specifically, we recommend not using upper case characters or Scandic letters (&auml;, &ouml;, etc.) in the bucket name.

<a id="naming_bucket"></a>

Below is a short checklist concerning naming of a bucket.

**Checklist for naming a bucket:**

 * Do <u>not</u> use uppercase characters or Scandic letters (&auml;, &ouml;, etc.).
 * Do <u>not</u> include sensitive information (since the bucket names are public). 
 * Must be unique across all users (you may use your project id in the bucket name, for example, _2000620-raw-data_).
 * It is <u>not</u> possible to rename a bucket, so consider the name carefully. 

Data is spread across different servers, which protects against disk and server failures. **Please note:** This does not protect from e.g. accidental deletion, and you should still make backups of important data.

&nbsp;

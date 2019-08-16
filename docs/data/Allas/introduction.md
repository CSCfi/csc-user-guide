
# Introduction to Allas Storage service

&nbsp;


## What is Allas?

**Allas** is part of the CSC storage portfolio and accessible from anywhere on the Internet. It is a storage service to host data for a project lifetime. The data from Allas can also be shared via Internet.

Allas is a modern object storage system - it comes with _S3_ and _Swift_ interfaces on _CEPH_ storage. In practice, this means that instead of files, the data is stored as objects within buckets. A bucket is simply a container for objects that may also include metadata describing the bucket. This means also that in order to use Allas you need software tools to access it, you can not simply see it as an ordinary disk storage. There are four flavors of tools to access Allas:

![Allas access flavors](/img/allas-access-flawors.png)

1. To access Allas from CSC’ supercomputers (such as **Puhti**) you have ready to use tools preinstalled in the environment. The tools are mostly the same you could also install to your local environment to access Allas. **Please note:** Supercomputer's own storage has a policy to delete idle data (see [Computing disk environment](../../computing/disk-environment.md){:target="_blank}) so your data must be moved to Allas after computing. The instructions for accessing and using Allas with CSC's supercomputers can be found from [Using Allas with Supercomputers](./using_allas/common_use_cases.md#using-allas-with-supercomputers){:target="_blank"}.

2. To access Allas with a browser you naturally do not have to install anything special on your computer, so this is by far the simplest way to access Allas. On the other hand, the browser user interface has a bunch of limitations compared to other access flavors, most notable are less performance and upload/download only a single file at the time. The instructions for accessing and using Allas with a browser can be found from [OpenStack Horizon web interface](./using_allas/web_client.md){:target="_blank"}.

3. To access Allas with a GUI client you have to install a suitable GUI client in to your server/laptop. The client needs to be capable to use swift or s3 access protocol. Instructions to use one such client can be found from [Accessing Allas with Windows and Mac](./accessing_allas.md#accessing-allas-with-windows-and-mac){:target="_blank"}.

4. To access Allas with command-line commands you need to install such client software in to your server/laptop. This is the most flexible way to access Allas but requires more effort from you than other access flavors. The client software needs to be capable to use swift or s3 access protocol. Instructions to use one such client can be found from [Accessing Allas with Linux](./accessing_allas.md#accessing-allas-with-linux){:target="_blank"} and [Protocols](./accessing_allas.md#protocols){:target="_blank"}.

In addition to these access flavors you can also see how to use Allas based on [Common Use Cases](./using_allas/common_use_cases.md){:target="_blank"}.


&nbsp;


## Billing and Quotas

Allas usage is based on project based storage quotas. All the project members have equal access rights to the storage area that has been granted for the project. In practice, this means that if one project member uploads data to Allas, all the other project members can read, edit and also delete the data. Allas itself does not store any information about who has uploaded the data to Allas.

The default quotas for every project are:

| Resource | Limit |
| :-------- |:------- |
| Storage amount | 1 TiB |
| Buckets per project | 1 000 |
| Objects per bucket | 100 000 |
| Object size | 5 GB |


Storing data in Allas consumes _billing units_. Accounting and billing information can be found under [Accounting principles and quotas](https://research.csc.fi/pouta-accounting){:target="_blank"}.

Unlike most other object storage providers, CSC does <u>not</u> charge for object storage network transfers or API calls.

&nbsp;



## System Characteristics


The stored objects can be any data type, such as images or compressed data files. In general, you can think of objects as files. Object storage is generally used for different purposes than many other storage solutions. It has benefits but also limitations.

**Benefits**

 * The object storage can handle practically any static data.
 * The data can be accessed from anywhere using URL.
 * The data can have different levels of access control.


**Limitations**

 * Object storage cannot be properly mounted on virtual machines. There are some tools to help this, but they have their limitations. For example, _svfs_ can be used to mount _Swift_ as filesystem but it uses _FUSE_ which is slow.
 * Unsuitable for files that change during their lifetime (e.g. most databases).
 * The data cannot be modified while it is in Allas. It must be downloaded to a server for processing and then you can replace the previous version with the new one.

More about the functionalities of Allas can be found from chapter [Common Use Cases](./using_allas/common_use_cases.md){:target="_blank"}.

The objects are stored in buckets. A bucket is simply a container for objects. These buckets should not be confused with _dockers_, or other containers used for computing. A bucket basically acts like a filesystem directory, but you can have only one level of them, so you cannot have buckets within buckets.

![Allas projects and buckets](/img/allas_projects_and_buckets.PNG)
**Figure** Data structure in Allas

Each bucket has a name, which must be unique across all users. So if somebody else has a bucket called "_test_", you cannot create a bucket called "_test_". All the bucket names are public, so please do <u>not</u> put private information in the bucket name. You may use, for example, your project id in the bucket name, such as _2000620-raw-data_.

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

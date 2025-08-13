
# Terms and concepts

[TOC]

### Access Control List

The _Access Control List_ (ACL) mechanism can be used to control other Allas users' access to your buckets.

### Billing unit

_Billing units_ describe the consumption of computing and storage resources in the CSC systems. In Allas, the amount of data stored consumes billing units.

See [Billing and Quotas](./introduction.md#billing-and-quotas)

### Bucket

A _bucket_ is a container for objects that may also include metadata describing the bucket.

### Checksum

A _checksum_ is a hashed string computed of an object to observe whether the object has changed (data integrity).
You can display the checksum using the command `md5sum`.

### Client

The _client software_ is used to access an object storage service, such as Allas. Allas can be accessed with several different [clients](accessing_allas.md).

### Metadata

_Metadata_ describes an object or bucket. It can be used to search for objects.
It is used via _key-value_ pairs (for example, name: John).

### Object lifecycle

_Object lifecycle_ Can be configured to automatically remove objects from Allas. Lifecycle is configured in the bucket level, where multiple expiration periods can be defined. Lifecycle is applied to the objects in the bucket based on their matching tags and/or prefixes. See an example in the [s3 client tool documentation](./using_allas/s3_client.md#setting-up-an-object-lifecycle)

### Object storage

_Object storage_ refers to a computer data storage that manages data as objects instead of files or blocks. Typically, an object consists of the data itself, metadata and a unique identifier. In general, the data can be anything, e.g. an image or audio.

### OpenStack

The [OpenStack](https://www.openstack.org/) cloud management middleware_ can be used to access Allas.


### Pseudo folder

Buckets cannot contain other buckets. You can, however, use so-called _pseudo folders_.

If an object's name contains a forward slash `/`, it is interpreted as a folder separator. These are shown as folder listings when accessing the data via come clients, for example the web interfaces. These pseudo folders are automatically added if you upload whole folders using a command line client.

For example, if you add two objects
```bash
fishes/salmon.png
fishes/bass.png
```
in a bucket, listing the bucket will display a folder called _fishes_ and the two files in it.

## Quota

The _Allas quota_ defines the maximum amount of data (capacity) the project is allowed to store in Allas.

See [Billing and quotas](./introduction.md#billing-and-quotas)

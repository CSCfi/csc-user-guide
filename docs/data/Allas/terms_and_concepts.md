
# Allas object storage related terms and concepts  

&nbsp;

**Access Control List**

_Access Control List_ (ACL) mechanism can be used to control other Allas users' access to your buckets.

&nbsp;


**Billing unit**

_Billing units_ describe the consumption of computing and storage resources on CSC systems. 
In Allas, the amount of data consumes billing units.
(See [Billing and Quotas](./introduction.md#billing-and-quotas){:target="_blank"})

&nbsp;


**Bucket**

A _bucket_ is simply a container for objects and may also include metadata describing the bucket.

&nbsp;

<a id="checksum"></a>

**Checksum**

_Checksum_ is a hashed string computed of an object to observe if the object has changed (data integrity). 
You can get the checksum with command `md5sum`.

&nbsp;


**Client**

_Client software_ is used to access an object storage service, such as Allas. There are three types of clients:

 * Web browser based access via [OpenStack Horizon web interface](./using_allas/web_client.md){:target="_blank"} for basic graphical usage.
 * Command-line clients such as [Swift](./using_allas/swift_client.md){:target="_blank"} and [s3cmd](./using_allas/s3_client.md){:target="_blank"} for power users.
 * _Programmable interface_ (API) for those who integrate software.

More about the clients in section [Protocols](./accessing_allas.md#protocols){target="_blank"}.

&nbsp;


**Metadata**

_Metadata_ describes an object or bucket and it could be used, for example, to search objects. 
The basic usage is via _key-value_ pair (for example, name: John).

&nbsp;


**Object storage**

_Object storage_ refers to a computer data storage that manages data as objects instead of files or blocks. Typically, an object consists of the data itself, metadata and a unique identifier. In general, the data can be anything, for example an image or audio.

&nbsp;


**OpenStack**

_OpenStack cloud management middleware_ can be used to access Allas.
[OpenStack Horizon web interface](./using_allas/web_client.md){:target="_blank"} offers some basic functionalities for data management in Allas.
For further information, see [OpenStack](https://www.openstack.org/){:target="_blank"}.

&nbsp;


**Pseudo-folder**

You cannot have buckets with other buckets inside them. You can however make use of so called _pseudo-folders_.

If an object name contains a forward slash "/", it is interpreted as a folder separator. These are shown as folders listings when accessing the data through the web interface. These pseudo-folders are automatically added if you upload whole folders with command-line clients.

For example, if you add two objects:
```bash
fishes/salmon.png
fishes/bass.png
```
in to a bucket, listing the bucket will show a folder called _fishes_ and the two files within it.

&nbsp;


**Quota**

_Allas quota_ defines the maximum amount of data (capacity) which the project is allowed to store in Allas. 
(See [Billing and Quotas](./introduction.md#billing-and-quotas){:target="_blank"})

&nbsp;


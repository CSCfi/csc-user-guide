## Object Storage

Object storage is platform to store files so that they can be accessed from anywhere, inside and outside
the CSC environment over HTTPS. Files on object storage cannot be changed, so one needs to download, change, upload
instead. For those familiar with commercial cloud services, the
Amazon S3 is an example of an object storage service. The CSC object storage service is called Allas.

Files on object storage cannot be changed, so one needs to download, change, upload
instead. Object storage keeps files in buckets, and each bucket has a flat hierarchy,
i.e. no subfolders.

Currently cPouta access is needed  for Object Storage: [Instructions for getting access to Pouta].

The easiest way to get started is to the the web client: [Using object storage]
For advanced use see Swift and S3 protocols below.

[Common use cases](object-storage-use-cases.md)

[Quotas and billing](object-storage-quotas-and-billing.md)

[Using object storage](using-object-storage.md)

[Access the object storage from Taito](access-pouta-object-storage-from-taito.md)

[Common Error Messages](object-storage-error-msgs.md)


## Definition of object storage

The object storage service stores "objects". These are blobs of data,
and can be anything. In general you can think of objects as files.

The  data  objects  are  stored  in  containers  (or  buckets).  These
containers should  not be  confused with  Docker, or  other containers
used  for computing.  A  container basically  acts  like a  filesystem
directory, but you can have only one level of them, so you cannot have
containers
within containers.

Each container has  a name, which must be unique  across all users. So
if somebody  else has a container  called "test" you can  not create a
container called "test". All container  names are public, so please do
not put private information in the container name. URLs to objects can
be in DNS format: https://containername.object.pouta.csc.fi - for this
reason using  a valid DNS  name ([RFC 1035]) for the  container makes
things  easier.  Specifically  we   recommend  not  using  upper  case
characters
in the container name.

Data objects within  the containers are immutable once  they have been
uploaded. You can delete an object and upload a new one with the same
name, but you can't do changes to it.

There are  three copies of  the data you  store in the  service. These
copies are  spread across  different servers.  This protects  the data
against  disk and  server failures.  Please  note that  this does  not
protect  from e.g.  accidental  deletion, and  you  should still  make
backups of important data.

  [RFC 1035]: https://www.ietf.org/rfc/rfc1035.txt "Section 2.3.1"

## Pouta Object Storage Benefits

Object storage  is generally  used for a  different purpose  that many
other storage solutions.  It has  benefits but also limitations. These
are some of the  benefits, but once you start using  it, you are bound
to find more.

-   You do  not need to set  up a virtual machine to  serve or receive
    the data.
-   The data can be accessed from anywhere using the same URL.
-   The data can have different levels of access control.

## Limitations

-   Object  storage   can't   be  properly   mounted  on   virtual
    machines. There are  some tools to help this, but  they have their
    limitations.   For example  svfs can  be  used to  mount swift  as
    filesystem but it uses FUSE which is slow.
-   Unsuitable for  objects/files that  change during  their lifetime
    (e.g.  most databases).

The [Object Storage Use Cases](object-storage-use-cases.md) article gives
concrete examples.

## Common Object Storage Use Cases

This article lists typical use cases for Object Storage.

[TOC]

### Storing datasets

Object storage is  a great way to  store datasets that a  lot of nodes
need to access. You will need to copy over the data to the node before
computing on it.  
  
There are several cases where your compute nodes only need read access
to common  data. In  these cases  the practice of  staging in  data to
individual nodes from the object storage can be used instead of shared
file storage.

### Sharing data

With  object storage  you  can  easily share  data,  e.g. datasets  or
research results. You  can share these with other projects  or open up
access to
everybody.  
  
The data can be accessed and shared in several different ways.

### Private - default

By  default,  if   you  don't  specify  anything   else,  contents  of
containers/buckets can  only be  accessed by authenticated  members of
your project.

### Access Control Lists (ACLs)

ACLs work on containers/buckets, not objects.  
  
With  ACLs you  can share  your  data in  a limited  fashion to  other
projects.   You can  e.g.  enable  authenticated read  access to  your
datasets to a collaboration project.

### Public

You can also have ACLs granting  public read access to the data, which
is
useful for e.g. sharing public scientific results or public datasets.  
 

### Temp URLs

A temp URL is a unique URL to access an object. These URLs can be time
limited. Anybody  with the URL can  access the object, but  the URL is
not feasible  to just guess. This  is a good way  to somewhat securely
share data  to a limited  audience, who don't  need to have  their own
cPouta
accounts. Temp URLs are created per object, not per container.  
  
Temp URLs are  a feature of Swift. In S3  the corresponding feature is
called  a Signed  URL. Please  see the  differences between  using the
Swift and S3 protocols below.  

### Accessing the same data from multiple CSC platforms

Since the  data in object  store is  available from anywhere,  you can
[access the data from both the  CSC clusters] and cloud services. This
makes the object store a good place to store datasets and intermediate
and final  results in cases  where your  workflow requires the  use of
both Taito and cPouta, for example.  


### Static web content

A common  way to  use object  storage is to  store static  web content
there (images,  videos, audio,  pdfs, downloadable content),  and just
add links to it from your web page, which can run either inside cPouta
or somewhere else. [Here is an example].  


### "Big Data" storage

It's  easy to  push  data  to object  storage  from several  different
sources.
This data can then later be processed as needed.  
  
An  example of  this is  several data  collectors pushing  data to  be
processed. These can be for  example scientific instruments, meters or
software which  harvest social media streams  for scientific analysis.
These  can  push their  data  into  object  store, and  later  virtual
machines,
or compute jobs on Taito can process this data.  
 

### Self-service backups of data

Object  storage is  also  often used  as a  location  where you  store
backups.
It's a convenient place to push copies of for example database dumps.  
  
If you intend to use object storage to store backups of cPouta virtual
machine  data,  this  is  possible.  You  should  note  the  following
dependencies between the systems for risk evaluation purposes.

-    The same  user  account works  for both  services.  If your  user
    account is compromised, it affects both object storage and virtual
    machine management, i.e. backups and master data.
-   Both services are provided from the same datacenter.
-   The same system  administrators have administrational level access
    to both services.
-   The virtual machine service  and object storage service are backed
    by different hardware, but they  share some components. A critical
    system malfunction may affect both systems.
-   Using object storage for backup is self service.

  [access the data from both the CSC clusters]: https://research.csc.fi/csc-guide-object-storage
  [Here is an example]: https://homepage-in-object-storage.object.pouta.csc.fi/index.html

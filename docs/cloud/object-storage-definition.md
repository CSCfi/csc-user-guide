## Short definition of object storage

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
reason using  a valid DNS  name ([RFC  1035]) for the  container makes
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

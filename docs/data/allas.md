# Allas object storage service

Allas object storage is a cloud storage service, where you can store and use data over HTTPS.
Object storage environments, like Allas, manage data as static objects that contain the actual data and
related metadata. When a file is uploaded to Allas it is stored as an immutable object that can later be downloaded 
or removed, but which can't be directly modified while the object is in Allas. In practice this means that you
can use Allas to store your data, but if you want to modify your data, you must first download the data to 
a server where you do the modifications and then replace the original object with a new version. 

The benefit of object storage is that it can handle practically any static data and that the data
can be accessed over the internet from any location. Further the same data can be accessed through several
interfaces: (command line clients, WWW-interfaces, virtual disk mounts etc.). The data can also be made 
publicly accessible.

## Getting Access

Usage of Allas is based on CSC customer projects. To be able to use Allas you need to be a member in 
a CSC project that has permission to use Allas. If you don't have a CSC account, you must first register as CSC user
and join or start a computing project for which Allas has been enabled. All these steps can be done with the
MyCSC user portal: [https://my.csc.fi]( https://my.csc.fi){:target="_blank"}

Allas uses a project based storage areas which have quotas. By default the quota for one project is XXX Tb, but it can be increased if needed. Storing data in Allas consumes billing units with rate xxxx Bu/TbA. Note that in Allas the billing unit consumption is calculated based on the amount of stored data (this differs from the disk environments of Puhti and Mahti where the billing is based on the granted quota).

All the project members have equal access rights to the Allas storage area that has been granted for the project. In practice this means if one user uploads data all the other users can not just read, but also delete the data. Allas itself does not store any information about who has uploaded the data to Allas.

## Use cases

Allas object storage service is a general purpose storage service. It's usage can be, but does not have to be linked to other CSC services. Below are some sample cases where Allas could be considered to be used as a storage platform

*  <b>Storing datasets for distributed use. </b> There are several cases where you need to access to common data from several locations. In these cases, the practice of staging in data to individual servers or computers from the object storage can be used instead of shared file storage.

* <b>Sharing data</b> With object storage you can easily share data, e.g. datasets or research results. You can share these with other projects or open up access to everybody. The data can be accessed and shared in several different ways. By default, the contents of buckets can only be accessed by authenticated members of your project. By modifying the access control settings of a project, you can enable authenticated read access to your datasets to a collaboration project. You can also grant public read access to the data, which is useful for e.g. sharing public scientific results or public datasets.

* <b>Static web content</b> A common way to use object storage is to store static web content there (images, videos, audio, pdfs, downloadable content), and just add links to it from your web page, which can run either inside cPouta or somewhere else.

* <b>Collecting data from different sources</b>
It's easy to push data to object storage from several different sources. This data can then later be processed as needed.
An example of this is several data collectors pushing data to be processed. These can be for example scientific instruments, meters or software which harvest social media streams for scientific analysis. These can push their data into object store, and later virtual machines, or compute jobs on Puhti can process this data.
 
* <b>Self-service backups of data</b> Object storage is also often used as a location where you store backups. It's a convenient place to push copies of for example database dumps. 



## Technical details
 
### Storage quota and structure 
Data in Allas is arranged into containers called <i>buckets</i>. You can simply think them as top level directories. Some applications crate buckets automatically but Allas users can freely create new buckets too. By default a project is allowed to have 1000 buckets each of which can contain 100 000 objects.

All buckets must have a name that is unique in Allas. You can't create a bucket if some other project has already used that bucket name. So it is a good rule of thumb to have something project or user specific in the bucket name, for instance <i>2000620-raw-data</i>.

The logical structure of Allas is flat and simple: you have buckets containing objects. You can not have buckets with other buckets inside them and objets stored in a bucket don't have a hierarchy. Even though you can't create sub-directories inside a bucket, you can however make use of so called pseudo-folders, based on objet names.

If an object name contains a forward slash "/", it is in many applications interpreted as a folder separator. For example, they are shown as folders listings when accessing the data through Pouta web interface. These pseudo-folders are automatically added if you upload whole folders with command line clients.

For example, if you add two objects to a container

<pre>cats/cat1.png
cats/cat2.png</pre>

listing the container will show a folder called "cats" and the two files within it.

Please note! This means you can not have empty pseudo-folders, since they require at least one object inside them.
 

### Protocols

Allas storage service is provided over two different protocols, <b>Swift</b> and <b>S3</b>. From user perspective one of the main differences between S3 and Swift is in authentication. Token based <i>Swift</i> authentication, used in Allas, remains valid for three hours at a time but in the key based <i>S3</i> the connection can be permanently open. The permanent connection of S3 is handy in many ways, but it includes a security aspect too: if your server where you use Allas is compromised, the object storage space is compromised too.

Because of this security concern, <i>swift</i> is the recommended protocol to be used in many-user servers like Puhti and Mahti. Thus, for example the CSC specific <i>a_ commands</i> (e.g. a_put and a_get) as well as the standard <i>rclone</i> configuration in Puhti are based on Swift.  However, in some cases the the permanent connections provided by S3 protocol may be the most reasonable option. For example, in users own virtual machine running in cPouta.

Swift and S3 protocols are not compatible in handling objects. Small objects, that don't need to be split during upload, can be cross used, but a splitted object can be used only with the protocol that was used for upload. The size limit for splitting an object depends on the settings and the protocol. The limit is typically between 500 MB and 5 GB. 

Each protocol has several different tools you can use. Here is a quick list of generic recommendations.

*   If you have a choice, use the Swift protocol, it's better supported.
*   In any case, settle on one protocol. Do not mix S3 and Swift.
*   Avoid uppercase characters in the names of containers/buckets.
*   It's better to store a few large objects than a lot of small objects.



## Clients

There are several different ways of accessing object storage. We support both the Swift and S3 protocols to manage the data. Below is just a short list of tools. There are more.

| Client |	Usable |	Notes |
|------- |--------| ------|
| Web client |	Yes | Use via https://pouta.csc.fi |
| python-swiftclient |	Yes |	This is the recommended Swift client |
| s3cmd |	Yes | This is the recommended S3 client. |
| python-swift library |	Yes |	 |
| libs3 |	Yes | | 	  	 
| python-openstackclient |	Yes | |	  	 
| aws-cli |	Yes |	aws-cli and the boto3 python library. |
| nordugrid-arc-client |	No |	Can be used for grid jobs. Bug reports submitted.|
| curl |	Yes | Extremely simple to use with public objects and temporary URLs |
| wget |	Yes | 	Same as curl |




## Using Allas in Puhti and Taito

The first step to use Allas is to authenticate to a project in Allas. In Taito and Puhti you can do the authentication with command:

    [user@puhti ~] source /appl/opt/allas_conf

The command above generates and stores authentication information into shell variables OS_AUTH_TOKEN and OS_STORAGE_URL. The authentication is valid for max 3 hours. Note that environment variables are available only for that login session so if you log into Puhti in another session, you need to authenticate again there to use Allas.


 1.  [Quick and safe: a_put, a_get, a_find](./a_commands.md)

 2.  [Advanced tools: Rclone and swift](./rclone.md)

 3.  [Persistent allas connections: s3cmd](./s3cmd.md)

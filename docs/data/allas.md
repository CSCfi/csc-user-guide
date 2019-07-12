# Allas object storage

Allas object storage is a cloud storage service, where you can store and use data over HTTPS.
Object storage environts, like Allas, manage data as static objects that contain the actual data and
related metadata. When a file is uploaded to Allas it is stored as an object that can later be downloaded 
or removed, but which can't be directly modified while the object is in Allas. In parctice this means that you
can use Allas to store your data, but if you want to modify your data, you must first download the data to 
a server where you do the modifications and then replace the original object with a new version. 

The benefit of object storage is that it can handel paractically any static data and that the data
can be accessed over the internet from any location. Further the same data can be accessed through several
interfaces: ( command line clients, WWW-interfaces, virtual disk mounts etc.). The data can also be made 
publicly accessible.

## Getting Access

Usage Allas is based on CSC customer projects. To be able to use allas you need to be a memeber in 
a CSC project that has permission to use Allas. If you don't have a CSC accunt, you must first register as CSC user
and join or start a computing project for which Allas has been enabled. All these steps can be done with the
MyCSC user portal: [https://my.csc.fi]( https://my.csc.fi)


Allas uses an project based storage areas which have quotas. By default the quota is XXX Tb, but it can be increased if needed.
Storing data in Allas consumes billing units with rate xxxx Bu/TbA. Note that in Allas the billing unit consumption is calclulated directly based on the amount of sorted data ( this differs form the disk environments of Puhti and Mahti where the billing is based on the granted quota).


All the project members have equal access rights to the Allas storage area that has been granted for the project. In practice this means if one user uploads data all the other users can not just read, but also delete the data. Allas itself does not store any information about who has uploaded the data to allas.

## Tehcnical details
 
Data in Allas is arranged into containers called buckets. You can simply think them as top level directories. Some applications crate buckets automatically but Allas users can freely create new buckets too.  The only drawback of buckets is that they must have a name that is unique in Allas. You can't create a bucket if some other project has already used that bucket name. So it is a good rule of thumb to have something project or user spesific in the bucket name, for instance "2000620-raw-data".

By default a project is allowed to have 1000 buckets each of which can contain 100 000 objects.

Allas storage service is provided over two different protocols, <b>Swift</b> and <b>S3</b>. Data uploaded using one protocol is visible with the other protocol. 

Each protocol has serveral different tools you can use. Here is a quick list of generic recommendations.

*   If you have a choice, use the Swift protocol, it's better supported.
*   In any case, settle on one protocol. Do not mix S3 and Swift.
*   Avoind uppercase characters in the names of containers/buckets.
*   It's better to store a few large objects than a lot of small objects.
     

You can not have buckets with other buckets inside them. You can however make use of so called pseudo-folders.

If an object name contains a forward slash "/", it is in many applications interpreted as a folder separator. For example, they are shown as folders listings when accessing the data through Pouta web interface. These pseudo-folders are automatically added if you upload whole folders with command line clients.

For example, if you add two objects to a container

cats/cat1.png
cats/cat2.png

listing the container will show a folder called "cats" and the two files within it.

Please note! This means you can not have empty pseudo-folders, since they require at least one object inside them.
 

## Clients

There are several different ways of accessing object storage. We support both the Swift and S3 protocols to manage the data. Below is just a short list of tools. There are more.
Client 	Usable 	Chapter In This User Guide 	Notes
Web client 	Yes 	4.4.5.6 	Use via https://pouta.csc.fi
python-swiftclient 	Yes 	4.4.5.5 	This is the recommended Swift client
s3cmd 	Yes 	4.4.5.6 	

This is the recommended S3 client. Use version 2.0.2 or later.
python-swift library 	Yes 	4.4.5.7 	 
libs3 	Yes 	  	 
python-openstackclient 	Yes 	  	 
aws-cli 	Yes 	  	aws-cli and the boto3 python library.
nordugrid-arc-client 	No 	  	Can be used for grid jobs. Bug reports submitted.
curl 	Yes 	  	Extremely simple to use with public objects and temporary URLs
wget 	Yes 	  	Same as curl


## Using Allas in Puhti and Taito

The first step to use Allas is to authenticate to a project in Allas. In Taito and Puhti you can do the autentication with command:

    [user@puhti ~] source /appl/opt/allas_conf

The command above generates and stores authentication information into shell variables OS_AUTH_TOKEN and OS_STORAGE_URL. The authentication is valid for max 3 hours. Note that environment variables are available only for that login session so if you log into Puhti in another session, you need to authenticatate again there to use Allas.


 1.  [Quick and safe: a_put, a_get, a_find](./a_commands.md)

 2.  [Advanced tools: Rclone and swift](./rclone.md)

 3.  [Persistent allas connections: s3cmd](./s3cmd.md)

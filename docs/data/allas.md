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


## Using Allas in Puhti and Taito

The first step to use Allas is to authenticate to a project in Allas. In Taito and Puhti you can do the autentication with command:

    [user@puhti ~] source /appl/opt/allas_conf

The command above generates and stores authentication information into shell variables OS_AUTH_TOKEN and OS_STORAGE_URL. The authentication is valid for max 3 hours. Note that environment variables are available only for that login session so if you log into Puhti in another session, you need to authenticatate again there to use Allas.


 1.  [Quick and safe: a_put, a_get, a_find](./a_commands.md)

 2.  [Advanced tools: Rclone and swift](./rclone.md)

 3.  [Persistent allas connections: s3cmd](./s3cmd.md)

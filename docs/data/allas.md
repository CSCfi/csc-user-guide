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



## Tehcnical details
  

## Getting Access

Usage Allas is based on CSC customer projects. To be able to use allas you need to be a memeber in 
a CSC project that has permission to use Allas. If you don't have a CSC accunt, you must first register as CSC user
and join or start a computing project for which Allas has been enabled. All these steps can be done with the
MyCSC user portal: [https://my.csc.fi]( https://my.csc.fi)


Allas uses an project based storage areas which have quotas. By default the quota is XXX Tb, but it can be increased if needed.
Storing data in Allas consumes billing units with rate xxxx Bu/TbA. Note that in Allas the billing unit consumption is calclulated directly based on the amount of sorted data ( this differs form the disk environments of Puhti and Mahti where the billing is based on the granted quota).


All the project members have equal access rights to the Allas storage area that has been granted for the project. In practice this means if one user uploads data all the other users can not just read, but also delete the data. Allas itself does not store any information about who has uploaded the data to allas.


## Using Allas in Puhti and Taito



 1.  [Quick and safe: a_put, a_get, a_find](./a_commands.md)

 2.  [Advanced tools: Rclone and swift](./rclone.md)

 3.  [Persistent allas connections: s3cmd](./s3cmd.md)

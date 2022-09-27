# Getting started with DBaaS from the Web interface

You can log into DBaaS by going to https://pukki.dbaas.csc.fi .


## Creating a new database instance

On the left hand column you can go to `Database` -> `Instances` and press `Launch Instance` on the right hand side.
Now you can define what settings you want for your database

1.   Instance name - What ever you want to name the instance.
2.   Volume size - How much disk space you will need for your database. If you just want to test the DBaaS then 1 GiB is probably enough. To increase the disk size later will require downtime for the Database. If you already know how much data you will use then it is easy to estimate how big volume you need. 
3.   Volume type - This can be left empty.
4.   Datastore - What type of database you want. It is recommend to use the latest version of your prefered database, if you don't have a specific reason for using an older version.
5.   Flavor - How big database instances you want. For small usecases the `standard.small` is probably enough if you later find out that it is not big enough you can always change it later. Changing flavor will require downtime.
6.   Locality - Is not needed. In the future DBaaS will support clusterd database at that point anti-affinity should be the prefered option in most cases.

On the next page `Database access`

7. Is public - You need to check public checkbox.
8. Allowed CIDRs - Here you want to add your allowed IP-addresses in the format `$IP/32` if you want to allow multiple IP-address you need to seperate them by a comma `,` .

You don't need to use the Intialize Databases. It is not recommended to create an admin user.

If you have a backup that you want to restore from you can do it from the `Advance` tab. Then you choose the `Source for Initial State` -> `Restore from Backup` and then choose `Backup name`

9. Now you can press `Launch`


10. Once the database instance have launched. You can press on the database instance's name. 
11. From here you can choose the `Database` tab and press `+ Create Database` and fill in the Name and possible collection, and Character Set and press `Create Database`
12. Then you can go to the `Users` tab create a new database user. The database user needs a name and a strong password it is recommend that you generate a long random password. You can also specify from which Host the user is allowed to access the database instance from. You shoul also specify to which databases the users should have access to. When you are done you can press `Create user`

13. Now you can go to the database specific documentation to find out further instruction how to use the database

	* [PostGreSQL](postgresql.md)




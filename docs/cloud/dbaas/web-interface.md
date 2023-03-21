# Getting started with DBaaS from the Web interface
!!! error "Closed Beta"
    Pukki DBaaS is in closed beta. This means that services is probably not suitable for most users
    and there might be breaking changes. If you are still interested in using the service you can
    [contact us](../../support/contact.md) to see if the service would be suitable for you.

You can log into DBaaS by going to [pukki.dbaas.csc.fi](https://pukki.dbaas.csc.fi) .


## Creating a new database instance

On the column on the left hand side you can go to `Database` -> `Instances` and then press on the `Launch Instance` that can be found on your right hand side.
Now you can define what settings you want for your database

1.   `Instance name` - What ever you want to name the instance.
2.   `Volume size` - How much disk space you will need for your database. If you just want to test the DBaaS then 1 GiB is probably enough. To increase the disk size later downtime is require for the Database. If you already know how much data you will use then it is easy to estimate how big volume you need. 
3.   `Volume type` - This can be left empty.
4.   `Datastore` - What type of database you want. It is recommend to use the latest version of your preferred database, if you don't have a specific reason for using an older version. PostgreSQL is the only available database at the moment.
5.   `Flavor` - How big database instances you want. For small use cases the `standard.small` is probably enough if you later find out that it is not big enough you can always change it later. Changing flavor will require downtime.
6.   `Locality` - Is not needed. In the future DBaaS will support clustered database and at that point anti-affinity should be the preferred option in most cases.

On the next page `Database access`

7. `Is public` - You need to check the public checkbox.
8. `Allowed CIDRs` - Here you want to add your allowed IP-addresses in the format `$IP/32` if you want to allow multiple IP-address. You need to separate them by a comma `,` .

You don't need to use the `Intialize Databases` tab. It is not recommended to create an admin user.

If you have a backup that you want to restore, you can do it from the `Advanced` tab. Then you choose the `Source for Initial State` -> `Restore from Backup` and then choose `Backup name`

9. Now you can press `Launch`

10. Once the database instance have launched. You can press on the database instance's name. 
11. From here you can choose the `Database` tab and press `+ Create Database` and fill in the Name and possible collection, and Character Set and press `Create Database`
12. Then you can go to the `Users` tab create a new database user. The database user needs a name and a strong password it is recommend that you generate a long random password. You can also specify from which Host the user is allowed to access the database instance from. You should also specify to which databases the users should have access to. When you are done you can press `Create user`

13. Now you can go to the database specific documentation to find out further instruction how to use the database

	* [PostgreSQL](postgresql.md)

## Modify user accounts in the database instance

You can add, remove and modify users from the database instances view. From the users tab. You need to make sure that you use strong passwords for each and every user.

## Add and remove databases

You can add and remove databases from the `Database` tab of the database instances.



# Getting started with DBaaS from the Web interface

You can log into DBaaS by going to [pukki.dbaas.csc.fi](https://pukki.dbaas.csc.fi).

## Creating a new database instance

In the column on the left hand side you can go to `Database` -> `Instances` and then press on the `Launch Instance` that can be found on your right hand side.
Now you can define what settings you want for your database:

1. `Instance name` - What ever you want to name the instance.
2. `Volume size` - How much disk space you will need for your database. If you just want to test the DBaaS then 1 GiB is probably enough. To increase the disk size later, downtime is required for the database. If you already know how much data you will use then it is easy to estimate how large volume you need.
3. `Volume type` - This can be left empty.
4. `Datastore` - What type of database you want. It is recommend to use the latest version of your preferred database, if you don't have a specific reason for using an older version. PostgreSQL is the only available database at the moment.
5. `Flavor` - How large database instances you want. For small use cases the `standard.small` is probably enough. If you later find out that it is not large enough you can always change it later. Changing flavor will require downtime.
6. `Locality` - Is not needed. In the future DBaaS will support clustered databases and at that point anti-affinity should be the preferred option in most cases.

On the next page `Database access`:

7. `Allowed CIDRs` - Here you want to add your allowed IP-addresses in the format `$IP/32` if you want to allow multiple IP-addresses. You need to separate them by a comma `,`. By default the database are created without any `Allowed CIDRs` which means that you won't be able to connect to your database.

On the third page `Intialize Databases:

8. In the `Initial Databases` field you can write what databases should be initialized. You can add additional database after the instance have started.
9. `Initial Admin User` adding first user that you want to use to connect to the database. You can add more user accounts after the database instance have started.
10. `Password` for the you first user. Please make sure that this password is not used anywhere else.
11. `Allowed Host (optional)` , this feature is not supported at the moment but in the future it will possible to limit users access based on IP.

On the fourth page `Advanced`:

12. You don't need to do anything but it is possible to launch a new database from a backup. If you choose to launch a database from a backup you don't need to specify `Initial Admin User`, `Passowrd`, or `Initial Databases`
13. Now you can press `Launch`
14. Once the database instance has launched, you can click the name of the database instance and manage additional items, such as users, backups etc. But it might take a couple minutes before the instance is up and running.
15.  Now you can go to the database specific documentation to find out further instructions on how to use the database:

	* [PostgreSQL](postgresql.md)

## Modify user accounts in the database instance

You can add, remove and modify users from the users tab of the database instances view. You need to make sure that you use strong passwords for each and every user.

## Add and remove databases

You can add and remove databases from the `Database` tab of the database instances.

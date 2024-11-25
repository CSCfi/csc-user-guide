# MariaDB permissions and privileges
!!! warning "MariaDB in Pukki is still in beta"
    This means that we have not tested as extensively that everything works correctly and there
    might still be big changes how Pukki will manage MariaDB databases. We are hoping to be able
    to get out of beta in March 2025.


## About privileges

By default when creating a user in a MariaDB database the user does not have access to any
database, one need to specify to which database the user have access either from the web interface
or the openstack cli. 

When creating a new user:
```sql
openstack database user create $INSTNACE_ID myuser my_password --database my_database
```

When updating an existing user:

```sql
openstack database user grant access $DATABASE_ID username database_name
```

When give user access to a database from the openstack cli or web interface the user gets
`ALL PRIVILEGES` to that database.

If you want to crate a user with different privileges you need to use the
`openstack datbase enable root` command so that you can create a user manually. More information
in the next topic how to create a read-only user.


## Example of giving a user read-only access to a database
To be able to create a read-only user you will first need to enable root since read only users
are not able to be created from the Pukki interfaces.

1. First create the root user
```sh
openstack database root enable 1de0dbe4-eed7-4291-b8ae-156c3d74473b
```

2. Then you can access the database with the root user and password:
```sql
GRANT SELECT ON database_name.* TO 'reader'@'%';
FLUSH PRIVILEGES;
```
You can show the result with:
```
SHOW GRANTS FOR 'reader'@'%';
+-------------------------------------------------------------------------------------------------------+
| Grants for reader@%                                                                                   |
+-------------------------------------------------------------------------------------------------------+
| GRANT USAGE ON *.* TO `reader`@`%` IDENTIFIED BY PASSWORD '*2470C0C06DEE42FD1618BB99005ADCA2EC9D1E19' |
| GRANT SELECT ON `database_name`.* TO `reader`@`%`                                                     |
+-------------------------------------------------------------------------------------------------------+
```
If you would like to only give the `reader` user access to only a table you can do it by

```sql
GRANT SELECT ON database_name.table_name TO 'reader'@'%';
```

Be aware that when creating a read user the openstack cli tool will not show to what tables the user
have access to.


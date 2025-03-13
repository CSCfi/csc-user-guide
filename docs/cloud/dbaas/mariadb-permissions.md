# MariaDB permissions and privileges
!!! warning "MariaDB in Pukki is still in beta"
    This means that it hasn't been tested as extensively as PostgreSQL, and there might still be
    large changes to how Pukki manages MariaDB database instances. We hope to move out of beta in
    April 2025.


## About privileges

When creating a user through the web interface or via openstack cli, you can define which databases
it has access to. By default, a freshly created user doesn't have access to any databases.

When creating a new user:
```sql
openstack database user create $INSTANCE_ID my_user my_password --databases my_database
```

When updating an existing user:
```sql
openstack database user grant access $INSTANCE_ID my_user my_database
```
You can either specify a single database or a list of databases to these commands. The commands
also accept the database instance's name in place of the ID.

Giving a user access to a database via openstack cli or the web interface means it gets
`ALL PRIVILEGES` to that database.

If you want more control over a user's privileges, you have to enable root access (through
the web interface, or with `openstack database enable root` with the CLI client) and manually
modify user privileges.


## Example of giving a user read-only access to a database

1. Enable the root user:
```sh
openstack database root enable $DATABASE_ID
```

2. Access the database using the root user and password.

3. Grant `SELECT` privileges on a database to a user:
```sql
GRANT SELECT ON database_name.* TO 'reader'@'%';
FLUSH PRIVILEGES;
```

You can view the grant with:
```
SHOW GRANTS FOR 'reader'@'%';
+-------------------------------------------------------------------------------------------------------+
| Grants for reader@%                                                                                   |
+-------------------------------------------------------------------------------------------------------+
| GRANT USAGE ON *.* TO `reader`@`%` IDENTIFIED BY PASSWORD 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' |
| GRANT SELECT ON `database_name`.* TO `reader`@`%`                                                     |
+-------------------------------------------------------------------------------------------------------+
```

You can also grant table-specific access:
```sql
GRANT SELECT ON database_name.table_name TO 'reader'@'%';
```

Be aware that the openstack cli tool or the the web interface will not display grants given through root access. For more information on MariaDB's grants, refer to [the official MariaDB documentation](https://mariadb.com/kb/en/grant/).

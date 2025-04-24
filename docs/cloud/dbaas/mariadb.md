# MariaDB
!!! warning "MariaDB in Pukki is still in beta"
    This means that it hasn't been tested as extensively as PostgreSQL, and there might still be
    large changes to how Pukki manages MariaDB database instances. We have extended the MariaDB
    beta phase until the end of August 2025 because we found while stress testing our backup
    processes that it sometimes fails silently.



* [How to access your MariaDB database](mariadb-accessing.md)
* [How to create database users and modify user permissions](mariadb-permissions.md)

# Database engine and backups

MariaDB database instances on Pukki use InnoDB by default, as most testing has been done using it.
Changing to other engines such as Aria might cause issues with backups, so one should carefully
consider how necessary it is before switching from InnoDB.
More information on database engines can be found in the
[official MariaDB documentation](https://mariadb.com/kb/en/storage-engines/).

## Useful links when using MariaDB
  * [MariaDB client](https://mariadb.com/kb/en/mariadb-client/)
  * [MariaDB SQL statement structure](https://mariadb.com/kb/en/sql-statements-structure/)

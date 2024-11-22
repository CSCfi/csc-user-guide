# MariaDB
!!! warning "MariaDB in Pukki is still in beta"
    This means that we have not tested as extensively that everything works correctly and there
    might still be big changes how Pukki will manage MariaDB databases. We are hoping to be able
    to get out of beta in March 2025.
    


* [How to access your MariaDB database](mariadb-accessing.md)
* [How to create database users and modify user permissions](mariadb-permissions.md)

# Database engine and backups
Innodb is the default engine and it is the most test in Pukki. Using other
engines like Aria might cause issues while doing backups so one should consider it twich before
using anohter engine than InnoDB.
More info can be found in the MariaDB documenation:  https://mariadb.com/kb/en/aria-storage-engine/

## Useful links when using MariaDB
  * [MariaDB client](https://mariadb.com/kb/en/mariadb-client/)
  * [MariaDB SQL statement structur](https://mariadb.com/kb/en/sql-statements-structure/)

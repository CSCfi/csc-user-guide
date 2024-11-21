# MariaDB
!!! warning "MariaDB in Pukki is still in beta"
    This means that we have not tested as extensively that everything works correctly and there
    might still be big changes how Pukki will manage MariaDB databases. We are hoping to be able
    to get out of beta in March 2025.
    


* [How to access your MariaDB database](mariadb-accessing.md)
* [How to create database users and modify user permissions](mariadb-permissions.md)

# Database engine and backups
TOOD mention that Innodb is the default engine and that engine is the most test in Pukki and using
engine like Aria might cause usages issues while doing backups so one should think twice before
using anohter engine than InnoDB.
better infor:  https://mariadb.com/kb/en/aria-storage-engine/

TODO I would like out documentation to manetion how the backup works in the background e.g. 
  * pg_basebackup is compressed encrypted and streamed to Allas
  * mariadbbackup is compressed encyrpted and streamed to Allas

TODO We should add some links to mariadb documentation from here maybe these:
  * https://mariadb.com/kb/en/mariadb-client/
  * https://mariadb.com/kb/en/sql-statements-structure/
TODO postgreql.md would also benefit of similar links

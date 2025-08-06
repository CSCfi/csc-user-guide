# Accessing your MariaDB instance
!!! warning "MariaDB in Pukki is still in beta"
    This means that it hasn't been tested as extensively as PostgreSQL, and there might still be
    large changes to how Pukki manages MariaDB database instances. We have extended the MariaDB
    beta phase until the end of August 2025 because we discovered during stress testing that
    our backup process occasionally fails silently.

## Graphical user interface
You can find a non-comprehensive list of different graphical interfaces for using MariaDB on
[MariaDB's homepage](https://mariadb.com/kb/en/graphical-and-enhanced-clients/).

## MariaDB Connectors

MariaDB Connectors are used for creating database connections from applications,
and are available for many popular programming languages. You can find more information
regarding their usage and configuration in MariaDB's documentation:

  * [https://mariadb.com/docs/server/connect/ **FIXME**](https://mariadb.com/docs/server/connect/)
  * [https://mariadb.com/kb/en/connectors/](https://mariadb.com/kb/en/connectors/)

**Please pay special attention to SSL configuration** - as Pukki only allows SSL connections
to its MariaDB instances, you *will* have to set up configuration options related to that.

## Command-line client mariadb and mysql
[MariaDB's documentation on the command-line client](https://mariadb.com/kb/en/mariadb-command-line-client/)

The recommended CLI client to use is `mariadb`. The `mysql` client does still work, but is
usually a symbolic link to `mariadb`.

Example commands for accessing your database:

```
mariadb --ssl --password --host ${PUBLIC_IP} --user ${DATABASE_USER} ${DATABASE_NAME}
```

or

```
mysql --ssl --password --host ${PUBLIC_IP} --user ${DATABASE_USER} ${DATABASE_NAME}
```

  * `--ssl` means the MariaDB client connects using SSL. This is necessary as
Pukki database instances enforce encrypted connections.
  * `--password` means the client prompts for a password. You can specify one
on the command line (like `--password=password`), but that is considered insecure.
  * `--host` specifies the host address to connect to. In Pukki this is almost
always your database instance's public IP address.
  * `--user` specifies which user to connect to the database as.
  * `${DATABASE_NAME}` specifies which database on the server to connect to.


### Using command line with .my.cnf

If you are frequently connecting to the same database, it might be worthwhile to set up a
`.my.cnf` configuration file in your home directory to store the necessary flags and options.

1. Create an empty `.my.cnf` file in your home directory, and restrict its access permissions:

```
touch ~/.my.cnf; chmod 600 ~/.my.cnf
```

2. Edit the configuration file with your favorite editor and add the following options:
```
[client]
user = your_username
password = your_password
host = your_host
database = your_database
ssl
```

As storing the password in a plaintext file isn't recommended, you can leave it empty to
always prompt for the password when connecting:

```
[client]
user = your_user
host = your_database_public_ip
database = your_database
ssl
password
```


### Common issues with CLI connections

```
ERROR 2002 (HY000): Can't connect to MySQL server on '${PUBLIC_IP}' (115)
```

If a password prompt appears, but the client is afterwards stuck connecting for a long time, you should
double-check that the `host` argument is correct, and that the firewall allows connections from your client's
address.

```
ERROR 3159 (08004): Connections using insecure transport are prohibited while --require_secure_transport=ON.
```

You tried to connect to the database without `--ssl`.

```
ERROR 1045 (28000): Access denied for user 'username'@'yourhostname' (using password: YES)
```

Either your password or your username is wrong.

```
ERROR 1044 (42000): Access denied for user 'username'@'%' to database 'databasename'
```

Either the database specified does not exist, or the username specified has no access to it.


### Accessing your Pukki MariaDB database from Puhti

1. Ensure your database instance allows [network traffic from Puhti.](firewalls.md#puhti)
2. `ssh` onto Puhti and load the `mariadb` module
```
module load mariadb
```
3. Now you can connect to the database with the mariadb-client

<!-- ### Basic Puhti batch job example using mysql
// I'm too lacy to verify the same example as in postgres-accessing.md

1. This requires that you have configured `~/.my.cnf` correctly in the previous section.
2. Create a file named `my-first-mariadb-batch-job.bash`:
   ```bash title="my-first-mariadb-batch-job.bash"
   #!/bin/bash -l
   #SBATCH --job-name=mariadb_job
   #SBATCH --output=output_%j.txt
   #SBATCH --error=errors_%j.txt
   #SBATCH --time=00:01:00
   #SBATCH --account=$PROJECT_NUMBER
   #SBATCH --ntasks=1
   #SBATCH --partition=test
   #SBATCH --mem-per-cpu=1024

   module load mariadb
   mariadb -c 'SELECT 1' >> mariadb-results.txt
   ```
   Make sure that you have updated the following variables:
      * `$PROJECT_NUMBER` – your CSC project ID (e.g. project_2001234)
      * `$DB_USER_NAME` – your database username (same as in `~/.my.cnf`)
      * `$DB_IP_ADDRESS` – the public IP-address of your database
      * `$DATABASE_NAME` – name of your database
3. Once you are happy with the batch script, you can submit the job by running:
   ```
   sbatch my-first-mariadb-batch-job.bash
   ```
-->

##  Some useful SQL commands

List databases
```sql
SHOW DATABASES;
```

List tables
```sql
SHOW TABLES;
```

Show table descriptions
```sql
DESCRIBE $table_name;
```

Change database
```sql
USE DATABASE $database_name;
```

Example query
```sql
SELECT * FROM $table_name LIMIT 1;
```

Show all database settings
```sql
SHOW VARIABLES;
```

or if you want to show a subset you can use `LIKE`
```sql
SHOW VARIABLES LIKE 'innodb%';
```
Note that `%` here indicates a wildcard - this lists all variables that begin with `innodb`.

<!--- Extended display --->
Import database dump
```
cat your_database_dump.sql | mariadb
```

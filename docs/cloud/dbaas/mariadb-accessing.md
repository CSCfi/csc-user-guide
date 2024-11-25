# Accessing your MariaDB instance
!!! warning "MariaDB in Pukki is still in beta"
    This means that we have not tested as extensively that everything works correctly and there
    might still be big changes how Pukki will manage MariaDB databases. We are hoping to be able
    to get out of beta in March 2025.

## Graphical user interface
You can find a non-comprehensive list of different graphical interfaces for using MariaDB on
[MariaDB's homepage](https://mariadb.com/kb/en/graphical-and-enhanced-clients/)


## Command-line client mariadb and mysql
[MariaDB's documentation client](https://mariadb.com/kb/en/mariadb-command-line-client/)

Nowadays the recommend client to use is `mariadb` , `mysql` does still work but it usually a
symbolic link to `mariadb`.

To access your database the command you probably want to use a command like this:

```
mariadb --ssl --password --host ${PUBLIC_IP} --user ${DATABASE_USER} ${DATABASE_NAME}
```

or 

```
mysql --ssl --password --host ${PUBLIC_IP} --user ${DATABASE_USER} ${DATABASE_NAME}
```

  * `--ssl` means that MariaDB client will connect with SSL because the database in Pukki is
enforcing encrypted connections.
  * `--password` means that it will prompt for password
  * `--host` means what public IP address the client will connect to
  * `--user` means what database user you will connect as.
  * `${DATABASE_NAME}` is to which database you want to connect to.
 

### Using command line with .my.cnf

If you are frequently using the same database it might be easier to set up a `.my.cnf` file in
your home directory so you don't need to remember all flags when you connect to your database.

1. Create the `.my.cnf` in your home directory

```
touch ~/.my.cnf; chmod 600 ~/.my.cnf
```

2. Open the configuration file with your favorite editor and add foll in the following 
variables
```
[client]
user = your_username
password = your_password
host = your_host
database = your_database
ssl
```

If you don't want to store the password in the file which is recommended you can enforce MariaDB
to prompt you for the password like this:

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

If the client asks for your password but the connection is stuck for a long time it probably means
that you have either provided the wrong public IP or you have not opened the firewalls to where
you are trying to connect from.

```
ERROR 3159 (08004): Connections using insecure transport are prohibited while --require_secure_transport=ON.
```

You tired to connect to the database without `--ssl`

```
ERROR 1045 (28000): Access denied for user 'username'@'yourhostname' (using password: YES)
```
You password or username is wrong.

```
ERROR 1044 (42000): Access denied for user 'username'@'%' to database 'databasename'
```

This means that you are trying to connect to a database that does not exist or your user does not
have access to.


### Accessing your Pukki MariaDB database from Puhti

1. First you need to ensure that you allow [network traffic from Puhti.](firewalls.md#Puthi)
2. Once you have ssh into Puhti you need to load the `mariadb` module.
```
module load mariadb
```
3. Now you can connect the database with the mariadb-client

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
DESCRIBE $tables;
```
Change database
```sql
USE DATABASE $databas_name;
```
Example query
```sql
SELECT * FROM $table LIMIT 1;
```
Show all database settings
```sql
SHOW VARIABLES;
```
or if you want to show a subset you can use `LIKE`
```sql
SHOW VARIABLES LIKE 'innodb%';
```

<!--- Extended display --->
Import database dump
```
cat your_database_dump.sql | mariadb
```

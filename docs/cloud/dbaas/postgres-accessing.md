# Access your PostgreSQL database

See [the page on firewalls](firewalls.md) for instructions on opening access to your database.

## Graphical user interface

A popular tool for working with PostgreSQL databases is pgAdmin, which can be found [here](https://www.pgadmin.org/). It can be installed as a desktop application, or on a server to be accessed via its web GUI. Note that it can not be installed on the Pukki database instance, and the DBaaS team does not provide support for it, as we are more comfortable using the CLI tools.

## Command-line

1. Install the `postgresql` command line tool. Note that some Linux distributions might provide ancient versions of it by default. Please consult [this page](https://www.postgresql.org/download/) for detailed installation instructions.
2. Find the public IP of your database instance from its Overview tab in the web GUI, or with `openstack database instance list`.
3. Use the following commands to access your PostgreSQL instance from the command line:
   ```
   psql --user ${USERNAME} --host ${PUBLIC_IP} ${DATABASE_NAME}
   ```

   If your application is using a configuration file The syntax normally looks something like this:

   ```
   postgresql://${USERNAME}:${PASSWORD}@{PUBLIC_IP}:5432/${DATABASE_NAME}
   ```

   You can also use the latter syntax to access the database with `psql` but it will omit column names from query responses.

### Common issues with CLI connections

1. If the connection hangs and times out without a PostgreSQL prompt, or if you get an error like:
   ```
   psql: error: connection to server at "195.148.30.38", port 5432 failed: Connection refused
   Is the server running on that host and accepting TCP/IP connections?
   ```
   it means either the IP address is wrong or the database instance's firewall is blocking access.
2. If you get an error like:
   ```
   psql: error: connection to server at "$IP_ADDRESS", port 5432 failed: FATAL:  database "$DATABASE" does not exist
   ```
   it means you're trying to access the wrong database.
3. If `psql` asks for a password but rejects it, make sure you typed it correctly, and check that the database user exists, either through the Users tab in the web GUI or with `openstack database user list ${DATABASE_ID}`.

## Accessing your Pukki PostgreSQL database from Puhti

1. First make sure that your database's [firewall allows traffic from Puhti](firewalls.md#puhti).
2. [Log in to Puhti](../../computing/connecting/index.md).
3. To be able to use the `psql` command line tool you need to first load the module:
   ```
   module load psql
   ```
4. Store your database password in your home directory. This is needed if you want to use
   PostgreSQL from a batch job. You can do it by creating a file with the necessary credentials:
    1. Create a file `~/.pgpass` with the following content (modify the placeholder variables accordingly):
    ```
    $PUBLIC_IP:5432:*:$USERNAME:$PASSWORD
    ```
        * The `$PUBLIC_IP` should be the public IP-address of your instance.
        * `5432` is the port to use (in Pukki it is always 5432).
        * The `*` means that all databases in you database instance should use the same credentials.
        * The `$USERNAME` and `$PASSWORD` are your database username and password.
    2. Update the file permissions with `chmod 600 ~/.pgpass` to keep your credentials safe.
5. Now you can verify that you can access your database without entering your password:
   ```
   psql --user ${USERNAME} --host ${PUBLIC_IP} ${DATABASE_NAME}
   ```

### Basic Puhti batch job example using psql

1. This requires that you have configured `~/.pgpass` correctly in the previous section.
2. Create a file named `my-first-psql-batch-job.bash`:
   ```bash title="my-first-psql-batch-job.bash"
   #!/bin/bash -l
   #SBATCH --job-name=psql_job
   #SBATCH --output=output_%j.txt
   #SBATCH --error=errors_%j.txt
   #SBATCH --time=00:01:00
   #SBATCH --account=$PROJECT_NUMBER
   #SBATCH --ntasks=1
   #SBATCH --partition=test
   #SBATCH --mem-per-cpu=1024

   module load psql
   psql --user $DB_USER_NAME --host $DB_IP_ADDRESS $DATABASE_NAME -c 'SELECT 1' >> psql-results.txt
   ```
   Make sure that you have updated the following variables:
      * `$PROJECT_NUMBER` – your CSC project ID (e.g. project_2001234)
      * `$DB_USER_NAME` – your database username (same as in `~/.pgpass`)
      * `$DB_IP_ADDRESS` – the public IP-address of your database
      * `$DATABASE_NAME` – name of your database
3. Once you are happy with the batch script, you can submit the job by running:
   ```
   sbatch my-first-psql-batch-job.bash
   ```

## Some useful SQL commands

### List databases

```sql
\l
```

### List tables

```sql
\d
```

### Show table descriptions

```sql
\d $TABEL_NAME
```

### Change database

```sql
\c $DATABASE_NAME
```

Note that this is the same command as for creating a new database if it does not exist (and you have given yourself root permissions).

### Example query

```sql
SELECT row1, row2 FROM table1 ORDER_BY row3 DESC LIMIT 2;
```

### Show all database settings

```sql
SHOW ALL;
```

### Show all users

```sql
select * from pg_user;
```

This is also visible from the web interface or the OpenStack CLI. Note that the PostgreSQL user is a service user, i.e. the user that the DBaaS uses to communicate with your database.

### Extended display

This will show each column of the record on its own row. This is especially useful when you want to inspect a single record.

```sql
SELECT * FROM table1 LIMIT 1 \gx
```

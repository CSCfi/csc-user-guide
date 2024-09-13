# PostgreSQL

This documentation provides some hints on how to get started with PostgreSQL and some basic troubleshooting tips. Note that you are responsible for your databases.

## Graphical user interface

A popular tool for working with PostgreSQL is [pgAdmin that can be found here](https://www.pgadmin.org/). Note that the application can not be installed on the database instance, it needs to be installed on your computer or a server that you control. The DBaaS team does not provide support for this application. We are also more comfortable with using the CLI tools.

## Command-line

1. First you need to install the `postgresql` command line tool. Note that if you are using Linux, your distributions are usually shipped with an ancient version of PostgreSQL, so make sure that you install the most recent major version. For all operating systems you can [find instructions for installation here](https://www.postgresql.org/download/).
2. Once you have installed the PostgreSQL client you should be able to login into the database. You can find the `public` IP from the `Overview` tab or `openstack database instance list`. The command that you normally want to use from a Linux CLI to connect to your database is:

    ```
    psql --user ${USERNAME} --host ${PUBLIC_IP} ${DATABASE_NAME}
    ```

    The syntax normally used in configuration files is:

    ```
    psql postgresql://${USERNAME}:${PASSWORD}@{PUBLIC_IP}:5432/${DATABASE_NAME}
    ```

    Note that if you use this syntax to login to the database it will not return column names when you do queries.

3. The most common issues when accessing the database from the CLI are the following:
    1. If you get an error like:
       ```
       psql: error: connection to server at "195.148.30.38", port 5432 failed: Connection refused
         Is the server running on that host and accepting TCP/IP connections?
       ```
       it means that either your database IP-address is wrong or you forgot to open the firewall.
    2. If you get an error like:
       ```
       psql: error: connection to server at "$IP_ADDRESS", port 5432 failed: FATAL:  database "$DATABASE" does not exist
       ```
       it means that your database is wrong.
    3. If `psql` asks for a password, but it does not accept your password, then you either mistyped it
       or your database username does not exist in your database.
    4. If the connection seems to be hanging, and you don't get a PostgreSQL prompt, it means that either your IP or port is wrong or that you did not create a firewall opening from your host.
4. Now you should be able to use the database.

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

## Parameters that users can modify

The DBaaS allows users to modify some of the parameters.
If there are some parameters that you think you should be able to modify, [please contact us](../../support/contact.md) and we'll see if we can make it possible.
By default, we assume that default parameters are sane and that users should not, under normal circumstances, modify any of these parameters.

| Parameters           | Default | Requires restart | Comments |
|:--- |:---:|:---|:---|
| maintenance_work_mem | 64MB  | No  | |
| max_connections      | 100   | Yes |It is usually recommended to use connection pools instead of modifying this value |
| work_mem             | 4MB   | No  | |
| log_statement        | false | No  | This is useful if you want to figure out more how your database is utilized |
| log_statement_stats  | false | No  |This will also collect stats from your database, this is recommended to keep as false since it might affect performance |

## A note about privileges

If you have little or no prior experience with PostgreSQL, we recommend familiarizing yourself with how privileges in PSQL interact with Databases, Schemas, and Tables. [Here's one tutorial that might be of use.](https://www.postgresqltutorial.com/postgresql-administration/postgresql-schema/)

To avoid confusion, keep in mind that in PostgreSQL 14 the default privileges allow every user to connect to any database and create tables in the default 'public' schema. They cannot access existing tables or other schemas without explicit permission, however, and they cannot create new schemas.

You can use the `openstack database user grant access` command to grant users all permissions on a specified database, which allows them to create their own schemas. They still can't access schemas and tables in them that are owned by other users without being given privileges, however. Typically the owner of an object in PSQL 14 (which can be a database, a schema, a table, etc. etc.) is the only one with any privileges regarding it, unless otherwise specified. This, combined with privileges not flowing 'downwards' in the hierarchy, can lead to some confusion. Having privileges to a schema doesn't imply any privileges to the tables contained within. For further reading, [here's the official docs on privileges.](https://www.postgresql.org/docs/14/ddl-priv.html)

### Example usage of privileges

These queries would allow the example_user to select data from the example_table. Note that the two queries are identical, as long as the search path hasn't been modified.

```
GRANT SELECT ON example_table TO example_user;
GRANT SELECT ON public.example_table TO example_user;
```

Keep in mind example_user here means a role, which can also be a group. These queries would create a new group, assign a user to it, and grant privileges to select data from all tables in the public schema.

```
CREATE ROLE example_group;
GRANT example_group TO example_user;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO example_group;
```

For easier management of privileges, we recommend creating groups and assigning users to relevant ones instead of tweaking rights on a per-user basis.

## PostgreSQL extensions

It is not possible for users to add additional extensions that are not already installed. If there
are some extensions you would like to see available in Pukki, please be in contact with
[CSC Service Desk](../../support/contact.md).

### How to enable extensions

  1. You can enable extensions by first [enable root](operations.md#enable-root)
  2. After that you can [log in to the database with the root user](#command-line)
  3. Then you can enable the extension of your choice with:
    ```
    CREATE EXTENSION $EXTENSION_NAME ;
    ```
  4. After you are done, make sure that you disable root.



### Currently available extensions
 
<!-- This extension list can easily be generated with the following command:
SELECT '| ' || name  AS name, default_version, comment || ' |' as comment FROM pg_available_extensions ORDER BY name;
--->
| Name  | Extension version | Extension description |
|:--- |:--- |:--- |
 | address_standardizer           | 3.4.2           | Used to parse an address into constituent elements. Generally used to support geocoding address normalization step. |
 | address_standardizer-3         | 3.4.2           | Used to parse an address into constituent elements. Generally used to support geocoding address normalization step. |
 | address_standardizer_data_us   | 3.4.2           | Address Standardizer US dataset example |
 | address_standardizer_data_us-3 | 3.4.2           | Address Standardizer US dataset example |
 | adminpack                      | 2.1             | administrative functions for PostgreSQL |
 | amcheck                        | 1.3             | functions for verifying relation integrity |
 | autoinc                        | 1.0             | functions for autoincrementing fields |
 | bloom                          | 1.0             | bloom access method - signature file based index |
 | btree_gin                      | 1.3             | support for indexing common datatypes in GIN |
 | btree_gist                     | 1.6             | support for indexing common datatypes in GiST |
 | citext                         | 1.6             | data type for case-insensitive character strings |
 | cube                           | 1.5             | data type for multidimensional cubes |
 | dblink                         | 1.2             | connect to other PostgreSQL databases from within a database |
 | dict_int                       | 1.0             | text search dictionary template for integers |
 | dict_xsyn                      | 1.0             | text search dictionary template for extended synonym processing |
 | earthdistance                  | 1.1             | calculate great-circle distances on the surface of the Earth |
 | file_fdw                       | 1.0             | foreign-data wrapper for flat file access |
 | fuzzystrmatch                  | 1.1             | determine similarities and distance between strings |
 | hstore                         | 1.8             | data type for storing sets of (key, value) pairs |
 | insert_username                | 1.0             | functions for tracking who changed a table |
 | intagg                         | 1.1             | integer aggregator and enumerator (obsolete) |
 | intarray                       | 1.5             | functions, operators, and index support for 1-D arrays of integers |
 | isn                            | 1.2             | data types for international product numbering standards |
 | lo                             | 1.1             | Large Object maintenance |
 | ltree                          | 1.2             | data type for hierarchical tree-like structures |
 | moddatetime                    | 1.0             | functions for tracking last modification time |
 | old_snapshot                   | 1.0             | utilities in support of old_snapshot_threshold |
 | pageinspect                    | 1.9             | inspect the contents of database pages at a low level |
 | pg_buffercache                 | 1.3             | examine the shared buffer cache |
 | pg_freespacemap                | 1.2             | examine the free space map (FSM) |
 | pg_prewarm                     | 1.2             | prewarm relation data |
 | pg_stat_statements             | 1.9             | track planning and execution statistics of all SQL statements executed |
 | pg_surgery                     | 1.0             | extension to perform surgery on a damaged relation |
 | pg_trgm                        | 1.6             | text similarity measurement and index searching based on trigrams |
 | pg_visibility                  | 1.2             | examine the visibility map (VM) and page-level visibility info |
 | pgcrypto                       | 1.3             | cryptographic functions |
 | pgrowlocks                     | 1.2             | show row-level locking information |
 | pgstattuple                    | 1.5             | show tuple-level statistics |
 | plpgsql                        | 1.0             | PL/pgSQL procedural language |
 | postgis                        | 3.4.2           | PostGIS geometry and geography spatial types and functions |
 | postgis-3                      | 3.4.2           | PostGIS geometry and geography spatial types and functions |
 | postgis_raster                 | 3.4.2           | PostGIS raster types and functions |
 | postgis_raster-3               | 3.4.2           | PostGIS raster types and functions |
 | postgis_sfcgal                 | 3.4.2           | PostGIS SFCGAL functions |
 | postgis_sfcgal-3               | 3.4.2           | PostGIS SFCGAL functions |
 | postgis_tiger_geocoder         | 3.4.2           | PostGIS tiger geocoder and reverse geocoder |
 | postgis_tiger_geocoder-3       | 3.4.2           | PostGIS tiger geocoder and reverse geocoder |
 | postgis_topology               | 3.4.2           | PostGIS topology spatial types and functions |
 | postgis_topology-3             | 3.4.2           | PostGIS topology spatial types and functions |
 | postgres_fdw                   | 1.1             | foreign-data wrapper for remote PostgreSQL servers |
 | refint                         | 1.0             | functions for implementing referential integrity (obsolete) |
 | seg                            | 1.4             | data type for representing line segments or floating-point intervals |
 | sslinfo                        | 1.2             | information about SSL certificates |
 | tablefunc                      | 1.0             | functions that manipulate whole tables, including crosstab |
 | tcn                            | 1.0             | Triggered change notifications |
 | tsm_system_rows                | 1.0             | TABLESAMPLE method which accepts number of rows as a limit |
 | tsm_system_time                | 1.0             | TABLESAMPLE method which accepts time in milliseconds as a limit |
 | unaccent                       | 1.1             | text search dictionary that removes accents |
 | uuid-ossp                      | 1.1             | generate universally unique identifiers (UUIDs) |
 | xml2                           | 1.1             | XPath querying and XSLT |




## Some useful commands

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

### Import database dump

If you have a database dump, you can import it with the following command. Be aware that this might overwrite what you already have in the database:

```bash
psql -h $FLOATING_IP -d $DATABASE -U USERNAME -f file.sql
```

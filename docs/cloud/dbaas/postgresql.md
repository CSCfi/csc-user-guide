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
      * If the connection seems to be hanging and you don't get a PostgreSQL prompt it means that either your IP or port is wrong or that you did not create a firewall opening from your host.
      <!-- * TODO `INSERT EXAMPLE HERE` if you get this error message it means that your postgresql client is not new enough please redo step 1. -->
4. Now you should be able to use the database.

## How is DBaaS PostgreSQL different from normal PostgreSQL

There are a couple differences from installing PostgreSQL yourself and using DBaaS. Even if you can get admin permissions for the database, it is not recommended. It is better to manage the users and database access from the DBaaS interface. By following these guidelines you'll have a lower risk of shooting yourself in the foot. There is an `openstack database root enable` command, which can be useful in an education environment if a teacher wants all the students to get admin permissions in their database.

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

## PostgreSQL extensions

It is not possible for users to add additional extensions that are not already installed. If there
are some extensions you would like to see available in Pukki, please be in contact with
[CSC Service Desk](../../support/contact.md). Note that extensions are not very well tested by the
DBaaS-admin.

1. To enable extensions, you need to first enable root for the database instance and log in as root:

    ```
    openstack database root enable $INSTNACE_ID
    ```

2. After you have logged in as root, you can enable the extension of your choice with:

    ```
    CREATE EXTENSION $EXTENSION_NAME
    ```

3. After you have enable the extension of your choice, you can log out and disable root:

    ```
    openstack database root disable $INSTANCE_ID
    ```

### Currently available extensions

| Name               | Comment |
|:--- |:--- |
| moddatetime        | functions for tracking last modification time                           |
| earthdistance      | calculate great-circle distances on the surface of the Earth            |
| pgrowlocks         | show row-level locking information                                      |
| autoinc            | functions for autoincrementing fields                                   |
| dict_int           | text search dictionary template for integers                            |
| pg_visibility      | examine the visibility map (VM) and page-level visibility info          |
| btree_gist         | support for indexing common datatypes in GiST                           |
| pageinspect        | inspect the contents of database pages at a low level                   |
| tsm_system_time    | TABLESAMPLE method which accepts time in milliseconds as a limit        |
| sslinfo            | information about SSL certificates                                      |
| hstore             | data type for storing sets of (key, value) pairs                        |
| amcheck            | functions for verifying relation integrity                              |
| pg_surgery         | extension to perform surgery on a damaged relation                      |
| intagg             | integer aggregator and enumerator (obsolete)                            |
| tsm_system_rows    | TABLESAMPLE method which accepts number of rows as a limit              |
| dict_xsyn          | text search dictionary template for extended synonym processing         |
| old_snapshot       | utilities in support of old_snapshot_threshold                          |
| isn                | data types for international product numbering standards                |
| btree_gin          | support for indexing common datatypes in GIN                            |
| uuid-ossp          | generate universally unique identifiers (UUIDs)                         |
| pgstattuple        | show tuple-level statistics                                             |
| xml2               | XPath querying and XSLT                                                 |
| pgcrypto           | cryptographic functions                                                 |
| pg_freespacemap    | examine the free space map (FSM)                                        |
| intarray           | functions, operators, and index support for 1-D arrays of integers      |
| plpgsql            | PL/pgSQL procedural language                                            |
| insert_username    | functions for tracking who changed a table                              |
| tablefunc          | functions that manipulate whole tables, including crosstab              |
| pg_prewarm         | prewarm relation data                                                   |
| tcn                | Triggered change notifications                                          |
| postgres_fdw       | foreign-data wrapper for remote PostgreSQL servers                      |
| dblink             | connect to other PostgreSQL databases from within a database            |
| seg                | data type for representing line segments or floating-point intervals    |
| lo                 | Large Object maintenance                                                |
| adminpack          | administrative functions for PostgreSQL                                 |
| pg_trgm            | text similarity measurement and index searching based on trigrams       |
| pg_buffercache     | examine the shared buffer cache                                         |
| citext             | data type for case-insensitive character strings                        |
| bloom              | bloom access method - signature file based index                        |
| cube               | data type for multidimensional cubes                                    |
| fuzzystrmatch      | determine similarities and distance between strings                     |
| unaccent           | text search dictionary that removes accents                             |
| pg_stat_statements | track planning and execution statistics of all SQL statements executed  |
| refint             | functions for implementing referential integrity (obsolete)             |
| ltree              | data type for hierarchical tree-like structures                         |
| file_fdw           | foreign-data wrapper for flat file access                               |

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

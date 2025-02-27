# PostgreSQL extensions

## Enabling extensions

  1. [Enable the root user](operations.md#enable-root).
  2. [Log in to the database as root](postgres-accessing.md#command-line).
  3. Use the following command to enable extensions:
    ```
    CREATE EXTENSION $EXTENSION_NAME ;
    ```
  4. Disable root once you're done enabling extensions.

## Currently available extensions

If there are extensions missing here that you would like to see available in Pukki, please contact the [CSC Service Desk](../../support/contact.md).
Note that the extension list is based on the latest PostgreSQL version, the available extensions might differ in older versions.

<!-- This extension list can easily be generated with the following command:
SELECT '| ' || name  AS name, comment || ' |' as comment FROM pg_available_extensions ORDER BY name;
--->
| Extension name  | Extension description |
|:--- |:--- |
 | address_standardizer           | Used to parse an address into constituent elements. Generally used to support geocoding address normalization step. |
 | address_standardizer-3         | Used to parse an address into constituent elements. Generally used to support geocoding address normalization step. |
 | address_standardizer_data_us   | Address Standardizer US dataset example |
 | address_standardizer_data_us-3 | Address Standardizer US dataset example |
 | amcheck                        | functions for verifying relation integrity |
 | autoinc                        | functions for autoincrementing fields |
 | bloom                          | bloom access method - signature file based index |
 | btree_gin                      | support for indexing common datatypes in GIN |
 | btree_gist                     | support for indexing common datatypes in GiST |
 | citext                         | data type for case-insensitive character strings |
 | cube                           | data type for multidimensional cubes |
 | dblink                         | connect to other PostgreSQL databases from within a database |
 | dict_int                       | text search dictionary template for integers |
 | dict_xsyn                      | text search dictionary template for extended synonym processing |
 | earthdistance                  | calculate great-circle distances on the surface of the Earth |
 | file_fdw                       | foreign-data wrapper for flat file access |
 | fuzzystrmatch                  | determine similarities and distance between strings |
 | h3                             | H3 bindings for PostgreSQL |
 | h3_postgis                     | H3 PostGIS integration |
 | hstore                         | data type for storing sets of (key, value) pairs |
 | insert_username                | functions for tracking who changed a table |
 | intagg                         | integer aggregator and enumerator (obsolete) |
 | intarray                       | functions, operators, and index support for 1-D arrays of integers |
 | isn                            | data types for international product numbering standards |
 | lo                             | Large Object maintenance |
 | ltree                          | data type for hierarchical tree-like structures |
 | moddatetime                    | functions for tracking last modification time |
 | pageinspect                    | inspect the contents of database pages at a low level |
 | pg_buffercache                 | examine the shared buffer cache |
 | pg_freespacemap                | examine the free space map (FSM) |
 | pg_prewarm                     | prewarm relation data |
 | pg_stat_statements             | track planning and execution statistics of all SQL statements executed |
 | pg_surgery                     | extension to perform surgery on a damaged relation |
 | pg_trgm                        | text similarity measurement and index searching based on trigrams |
 | pg_visibility                  | examine the visibility map (VM) and page-level visibility info |
 | pg_walinspect                  | functions to inspect contents of PostgreSQL Write-Ahead Log |
 | pgcrypto                       | cryptographic functions |
 | pgrowlocks                     | show row-level locking information |
 | pgstattuple                    | show tuple-level statistics |
 | plpgsql                        | PL/pgSQL procedural language |
 | postgis                        | PostGIS geometry and geography spatial types and functions |
 | postgis-3                      | PostGIS geometry and geography spatial types and functions |
 | postgis_raster                 | PostGIS raster types and functions |
 | postgis_raster-3               | PostGIS raster types and functions |
 | postgis_sfcgal                 | PostGIS SFCGAL functions |
 | postgis_sfcgal-3               | PostGIS SFCGAL functions |
 | postgis_tiger_geocoder         | PostGIS tiger geocoder and reverse geocoder |
 | postgis_tiger_geocoder-3       | PostGIS tiger geocoder and reverse geocoder |
 | postgis_topology               | PostGIS topology spatial types and functions |
 | postgis_topology-3             | PostGIS topology spatial types and functions |
 | postgres_fdw                   | foreign-data wrapper for remote PostgreSQL servers |
 | refint                         | functions for implementing referential integrity (obsolete) |
 | seg                            | data type for representing line segments or floating-point intervals |
 | sslinfo                        | information about SSL certificates |
 | tablefunc                      | functions that manipulate whole tables, including crosstab |
 | tcn                            | Triggered change notifications |
 | tsm_system_rows                | TABLESAMPLE method which accepts number of rows as a limit |
 | tsm_system_time                | TABLESAMPLE method which accepts time in milliseconds as a limit |
 | unaccent                       | text search dictionary that removes accents |
 | uuid-ossp                      | generate universally unique identifiers (UUIDs) |
 | xml2                           | XPath querying and XSLT |


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



## Some useful commands

**List available extensions**

```sql
SELECT name, default_version, comment FROM pg_available_extensions ORDER BY name;
```

**List enabled extensions**

```sql
SELECT * from pg_extension ORDER BY extname;
```

**Create extension**

```sql
CREATE EXTENSION ${EXTENSION_NAME};
```

**Disable extension**
```sql
SELECT * FROM table1 LIMIT 1 \gx
```

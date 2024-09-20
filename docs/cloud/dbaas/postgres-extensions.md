# PostgreSQL extensions

It is not possible for users to add additional extensions that are not already installed. If there
are some extensions you would like to see available in Pukki, please be in contact with
[CSC Service Desk](../../support/contact.md).

## How to enable extensions

  1. You can enable extensions by first [enable root](operations.md#enable-root)
  2. After that you can [log in to the database with the root user](postgres-accessing.md#command-line)
  3. Then you can enable the extension of your choice with:
    ```
    CREATE EXTENSION $EXTENSION_NAME ;
    ```
  4. After you are done, make sure that you disable root.



## Currently available extensions
 
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

**List available extensions**

**List enabled extensions**

**Create extension**

**Disable extension**
```sql
SELECT * FROM table1 LIMIT 1 \gx
```

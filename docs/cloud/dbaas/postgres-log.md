# Database server log in PostgreSQL
 
PostgreSQL server log gives important information from the database server's current health and operation.

## How to access database server logs

[Via CLI](advanced.md#how-to-access-database-server-logs)

[Via Web UI](web-interface.md#how-to-access-database-server-logs)

If you think there are missing log lines, please [contact CSC Service Desk](/support/contact.md) for assistance.

## What to look for

PostgreSQL server log is more chatty than for example MariaDB. 

On idle database server there will be always information about checkpoints (forced buffer writes), see `log format` section below.

### Log format

Example snipped from log;

```
2026-01-09 08:28:40.077 UTC [43] LOG:  checkpoint starting: time
2026-01-09 08:28:40.118 UTC [43] LOG:  checkpoint complete: wrote 0 buffers (0.0%); 0 WAL file(s) added, 0 removed, 1 recycled; write=0.001 s, sync=0.001 s, total=0.042 s; sync files=0, longest=0.000 s, average=0.000 s; distance=16384 kB, estimate=16384 kB; lsn=0/BD0000B8, redo lsn=0/BD000060
```

Where 5th column (`LOG`) is the severity and everything after that is the message.

Possible severities from lowest to highest level and their description;

| Severity         | Usage                                                                                                |
|:-----------------|:-----------------------------------------------------------------------------------------------------|
| DEBUG1 .. DEBUG5 | Provides successively-more-detailed information for use by developers.                               |
| INFO             | Provides information implicitly requested by the user, e.g., output from VACUUM VERBOSE.             |
| NOTICE           | Provides information that might be helpful to users, e.g., notice of truncation of long identifiers. |
| WARNING          | Provides warnings of likely problems, e.g., COMMIT outside a transaction block.                      |
| ERROR            | Reports an error that caused the current command to abort.                                           |
| LOG              | Reports information of interest to administrators, e.g., checkpoint activity.                        |
| FATAL            | Reports an error that caused the current session to abort.                                           |
| PANIC            | Reports an error that caused all database sessions to abort.                                         |

By default only `WARNING` and higher level messages appear in the database server log.

### Common messages

These are common messages, but not an exhaustive list.

#### Checkpoints are happening continuously on background

Checkpoints are targeted to happen every five minutes by default;
```
2026-01-30 15:02:29.095 UTC [10] LOG:  checkpoint starting: time
2026-01-30 15:05:52.826 UTC [10] LOG:  checkpoint complete: wrote 2032 buffers (7.9%); 0 WAL file(s) added, 0 removed, 2 recycled; write=203.582 s, sync=0.036 s, total=203.732 s; sync files=35, longest=0.032 s, average=0.002 s; distance=47453 kB, estimate=47453 kB; lsn=0/E9E57A88, redo lsn=0/E9E579F8
2026-01-30 15:14:16.235 UTC [10] LOG:  checkpoint starting: force wait
2026-01-30 15:14:16.288 UTC [10] LOG:  checkpoint complete: wrote 0 buffers (0.0%); 0 WAL file(s) added, 0 removed, 1 recycled; write=0.001 s, sync=0.001 s, total=0.054 s; sync files=0, longest=0.000 s, average=0.000 s; distance=1697 kB, estimate=42878 kB; lsn=0/EA000080, redo lsn=0/EA000028
```

On idling database server the checkpoints can happen less frequently than every five minutes.

If there is too much write load, then checkpoints will happen more requently and the special `HINT` level message will be shown;
```
2026-03-06 15:07:27.231 UTC [10] HINT:  Consider increasing the configuration parameter "max_wal_size".
2026-03-06 15:07:27.231 UTC [10] LOG:  checkpoint starting: wal
2026-03-06 15:07:27.231 UTC [10] LOG:  checkpoints are occurring too frequently (18 seconds apart)
```

In Pukki `max_wal_size` is tied to instance's flavor size. 

This can also happen under heavy load caused by upgrade process or when manually reindexing. Occasional `HINT` about `max_wal_size` is still okay, but it means there is more than optimal amount of disk IO happening.

#### Database server shutdown messages

```
2026-01-30 14:51:39.364 UTC [1] LOG:  received fast shutdown request
2026-01-30 14:51:39.389 UTC [1] LOG:  aborting any active transactions
2026-01-30 14:51:39.396 UTC [1] LOG:  background worker "logical replication launcher" (PID 48) exited with exit code 1
2026-01-30 14:51:39.396 UTC [43] LOG:  shutting down
2026-01-30 14:51:39.566 UTC [1] LOG:  database system is shut down
```

Database server shutdown also generates `FATAL` level message if database connection exists, additionally `STATEMENT` level message is shown if some query was running during the shutdown;

```
2026-02-13 16:06:34.942 UTC [27] FATAL:  terminating connection due to administrator command
2026-02-13 16:06:34.942 UTC [27] STATEMENT:  select pg_sleep(60);
```

In above `STETAMENT` level log entry only query running will be logged not the whole transaction.

Checkpoint message can also possible during shutdown;

```
2026-01-30 14:51:39.401 UTC [43] LOG:  checkpoint starting: shutdown immediate
2026-01-30 14:51:39.558 UTC [43] LOG:  checkpoint complete: wrote 0 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.001 s, sync=0.001 s, total=0.163 s; sync files=0, longest=0.000 s, average=0.000 s; distance=0 kB, estimate=14745 kB; lsn=0/E7000168, redo lsn=0/E7000168
```

#### Database server deletion

The database server is shutdown and user looses access to instance's logs.

#### Database server startup messages

```

PostgreSQL Database directory appears to contain a database; Skipping initialization

2026-01-30 14:52:29.877 UTC [1] LOG:  starting PostgreSQL 17.6 (Debian 17.6-1.pgdg13+1) on x86_64-pc-linux-gnu, compiled by gcc (Debian 14.2.0-19) 14.2.0, 64-bit
2026-01-30 14:52:29.894 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
2026-01-30 14:52:29.894 UTC [1] LOG:  listening on IPv6 address "::", port 5432
2026-01-30 14:52:29.899 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
2026-01-30 14:52:29.916 UTC [12] LOG:  database system was shut down at 2026-01-30 14:51:39 UTC
2026-01-30 14:52:30.164 UTC [1] LOG:  database system is ready to accept connections
```

The last message `database system is ready to accept connections` means that the database's integrity check has passed and the database is ready for read-write operations.

If the database server is not ready to accept connections and there is an incoming connection the following will be also logged on the startup;

```
2026-02-13 16:06:36.222 UTC [13] FATAL:  the database system is starting up
```

Above `FATAL` error could be also caused by Pukki trying to ping the database server.

#### Volume & instance resize, instance rebuild and upgrade

These are from Pukki's logging point of view just a shutdown and startup. Upgrade does other actions on background but logs of these are not shown to the user.

The database server upgrade might complain about discrepancy of default collation version and databases' actual collation version on disk;

```
2026-07-31 14:32:51.739 UTC [17] WARNING:  database "postgres" has a collation version mismatch
2026-07-31 14:32:51.739 UTC [17] DETAIL:  The database was created using collation version 2.31, but the operating system provides version 2.36.
2026-07-31 14:32:51.739 UTC [17] HINT:  Rebuild all objects in this database that use the default collation and run ALTER DATABASE postgres REFRESH COLLATION VERSION, or build PostgreSQL with the right library version.
2026-07-31 14:32:52.260 UTC [22] WARNING:  database "template1" has a collation version mismatch
2026-07-31 14:32:52.260 UTC [22] DETAIL:  The database was created using collation version 2.31, but the operating system provides version 2.36.
2026-07-31 14:32:52.260 UTC [22] HINT:  Rebuild all objects in this database that use the default collation and run ALTER DATABASE template1 REFRESH COLLATION VERSION, or build PostgreSQL with the right library version.
```

On above both PostgreSQL internal (`postgres` and `template1`) databases are shown. The upgrade will give a warning about all the databases multiple times, but corrective actions are handled automatically by Pukki.

#### Database server creation and restore

Database server restore is essentially just a new database server creation from the Pukki's logging stand point. Creating a database server generates about 50 to 60 one-off log lines and it will end to same `database system is ready to accept connections` message like startup does.

#### When attaching configuration group

Changing `work_mem` parameter here as an example;
```
2026-06-12 14:06:19.490 UTC [1] LOG:  received SIGHUP, reloading configuration files
2026-06-12 14:06:19.491 UTC [1] LOG:  parameter "work_mem" changed to "8MB"
```

#### Error in configuration group


For example for `work_mem` the correct value would be `8MB` not `8M`;
```
2026-06-12 14:03:18.923 UTC [1] LOG:  received SIGHUP, reloading configuration files
2026-06-12 14:03:18.924 UTC [1] HINT:  Valid units for this parameter are "B", "kB", "MB", "GB", and "TB".
2026-06-12 14:03:18.924 UTC [1] LOG:  configuration file "/etc/postgresql/conf.d/20-user-001-common.conf" contains errors; unaffected changes were applied
2026-06-12 14:03:18.924 UTC [1] LOG:  invalid value for parameter "work_mem": "8M"
```

Note worthy here is that if database server has incorrect configurations during any startup then it will end in to restart loop without never successfully starting to serve connections;
```
PostgreSQL Database directory appears to contain a database; Skipping initialization

2026-06-12 14:29:30.314 UTC [1] FATAL:  configuration file "/etc/postgresql/conf.d/20-user-001-common.conf" contains errors
2026-06-12 14:29:30.314 UTC [1] HINT:  Valid units for this parameter are "B", "kB", "MB", "GB", and "TB".
2026-06-12 14:29:30.314 UTC [1] LOG:  invalid value for parameter "work_mem": "8M"
```

Above error will be looped until the parameter is changed to use valid value.


#### Trying to create a database with non-existing encoding or/and collation

Currently Pukki allows to create database using incorrect encoding and collation, but these do end up in error like we can see below. See PostgreSQL manual for correct encoding and collation if not using defaults.

Following commands in PostgreSQL client gives the default values;

```
SHOW server_encoding;
SHOW lc_collate;
```

Even though default `lc_collate` is now `en_US.utf8` and therefore `server_encoding` is `UTF8`, these are only guaranteed to stay same during the lifetime of the instance, not for new instances.

Both encoding and collation does not exits;
```
2026-07-30 13:36:53.141 UTC [56] ERROR:  foo is not a valid encoding name at character 26
2026-07-30 13:36:53.141 UTC [56] STATEMENT:  CREATE DATABASE "test1" ENCODING = 'foo' LC_COLLATE = 'bar'
```

Encoding is incorrect;
```
2026-07-30 13:39:44.842 UTC [71] ERROR:  foobar is not a valid encoding name at character 25
2026-07-30 13:39:44.842 UTC [71] STATEMENT:  CREATE DATABASE "test2" ENCODING = 'foobar'
```

Just collation is incorrect;

```
2026-07-30 13:40:12.169 UTC [77] ERROR:  invalid LC_COLLATE locale name: "foobar"
2026-07-30 13:40:12.169 UTC [77] HINT:  If the locale name is specific to ICU, use ICU_LOCALE.
2026-07-30 13:40:12.169 UTC [77] STATEMENT:  CREATE DATABASE "test3" LC_COLLATE = 'foobar'
```

#### Incorrect password

```
2026-02-13 15:36:07.576 UTC [80166] DETAIL:  Connection matched file "/etc/postgresql/pg_hba.conf" line 9: "host all all 0.0.0.0/0 md5"
2026-02-13 15:36:07.576 UTC [80166] FATAL:  password authentication failed for user "user"
```

These might be someone authorized trying manually connecting to the database server or maybe it is some background job failing to connect, which effects is not directly visible. Consider these also to be possible break-in attempts.

#### User does not exists

```
2026-02-13 15:49:25.063 UTC [80256] DETAIL:  Role "test" does not exist.
2026-02-13 15:49:25.063 UTC [80256] FATAL:  password authentication failed for user "test"
	Connection matched file "/etc/postgresql/pg_hba.conf" line 9: "host all all 0.0.0.0/0 md5"
```

These might be someone authorized trying manually connecting to the database server or maybe it is some background job failing to connect, which effects is not directly visible. Consider these also to be possible break-in attempts.

#### Transaction was committed or rollbacked and there was no transaction started in the first place

```
2026-02-13 16:00:16.900 UTC [35] WARNING:  there is no transaction in progress
```

Usually frameworks which applications are using should handle the start of transaction, but if the application does not use any framework, it is a simple batch job, or you typed the SQL manually then make sure that there is a `START TRANSACTION` commanced if you plan to use transactional `COMMIT` or `ROLLBACK` commands.

#### Typos when running SQLs manually

```
2026-01-30 14:58:32.882 UTC [64] ERROR:  syntax error at or near "test" at character 8
2026-01-30 14:58:32.882 UTC [64] STATEMENT:  CREATE test AS SELECT GENERATE_SERIES(1,500000) AS id, MD5(RANDOM()::TEXT) AS random_text;
```

Check the PostgreSQL manual for correct syntaxes, obviously in this example the command should been `CREATE TABLE test...`.

#### Connection was not closed properly from the client side

```
2026-02-13 16:32:56.591 UTC [60] LOG:  could not receive data from client: Connection reset by peer
```

Usually these are improperly closed connections. There is a possibility that network connection between the application and the server has been interrupted during transaction, causing resource intesive rollback, so these cannot be completely ignored either.

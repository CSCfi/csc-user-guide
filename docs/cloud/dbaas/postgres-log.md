# Server log in PostgreSQL
 
PostgreSQL server log gives important information from the database's current health and operation.

## How to access database logs

[Via CLI](advanced.md#how-to-access-database-logs)

[Via Web UI](web-interface.md#how-to-access-database-logs)

## What to look for

PostgreSQL server log is more chatty than for example MariaDB. 

On idle database there will be always information about checkpoints (forced buffer writes), see `server log format` section below.

### Server log format

Example snipped from server log;

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

By default only `WARNING` and higher level messages appear in the server log.

### Common messages

These are common messages, but not an exhaustive list.

!!! info "Note"
    This is as stub and will be appended later...

#### Checkpoints are happening continuously on background

Checkpoints are targeted to happen every five minutes by default;
```
2026-01-30 15:02:29.095 UTC [10] LOG:  checkpoint starting: time
2026-01-30 15:05:52.826 UTC [10] LOG:  checkpoint complete: wrote 2032 buffers (7.9%); 0 WAL file(s) added, 0 removed, 2 recycled; write=203.582 s, sync=0.036 s, total=203.732 s; sync files=35, longest=0.032 s, average=0.002 s; distance=47453 kB, estimate=47453 kB; lsn=0/E9E57A88, redo lsn=0/E9E579F8
2026-01-30 15:14:16.235 UTC [10] LOG:  checkpoint starting: force wait
2026-01-30 15:14:16.288 UTC [10] LOG:  checkpoint complete: wrote 0 buffers (0.0%); 0 WAL file(s) added, 0 removed, 1 recycled; write=0.001 s, sync=0.001 s, total=0.054 s; sync files=0, longest=0.000 s, average=0.000 s; distance=1697 kB, estimate=42878 kB; lsn=0/EA000080, redo lsn=0/EA000028
```

If there is too much write load, then checkpoints will happen more requently and the special `HINT` level message will be shown;
```
2026-03-06 15:07:27.231 UTC [10] HINT:  Consider increasing the configuration parameter "max_wal_size".
2026-03-06 15:07:27.231 UTC [10] LOG:  checkpoint starting: wal
2026-03-06 15:07:27.231 UTC [10] LOG:  checkpoints are occurring too frequently (18 seconds apart)
```

!!! info "Note"
    In Pukki `max_wal_size` is tied to instance's flavor size. On idling database the checkpoints can happen less frequently than every five minutes.

#### Database shutdown messages

```
2026-01-30 14:51:39.364 UTC [1] LOG:  received fast shutdown request
2026-01-30 14:51:39.389 UTC [1] LOG:  aborting any active transactions
2026-01-30 14:51:39.396 UTC [1] LOG:  background worker "logical replication launcher" (PID 48) exited with exit code 1
2026-01-30 14:51:39.396 UTC [43] LOG:  shutting down
2026-01-30 14:51:39.566 UTC [1] LOG:  database system is shut down
```

Database shutdown also generates `FATAL` level message if database connection exists, also `STATEMENT` level message if some query was running during the shutdown;

```
2026-02-13 16:06:34.942 UTC [27] FATAL:  terminating connection due to administrator command
2026-02-13 16:06:34.942 UTC [27] STATEMENT:  select pg_sleep(60);
```

Also checkpoint message is possible during shutdown;

```
2026-01-30 14:51:39.401 UTC [43] LOG:  checkpoint starting: shutdown immediate
2026-01-30 14:51:39.558 UTC [43] LOG:  checkpoint complete: wrote 0 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.001 s, sync=0.001 s, total=0.163 s; sync files=0, longest=0.000 s, average=0.000 s; distance=0 kB, estimate=14745 kB; lsn=0/E7000168, redo lsn=0/E7000168
```

!!! info "Note"
    Only query running will be logged not the whole transaction.


#### Database startup messages

```

PostgreSQL Database directory appears to contain a database; Skipping initialization

2026-01-30 14:52:29.877 UTC [1] LOG:  starting PostgreSQL 17.6 (Debian 17.6-1.pgdg13+1) on x86_64-pc-linux-gnu, compiled by gcc (Debian 14.2.0-19) 14.2.0, 64-bit
2026-01-30 14:52:29.894 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
2026-01-30 14:52:29.894 UTC [1] LOG:  listening on IPv6 address "::", port 5432
2026-01-30 14:52:29.899 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
2026-01-30 14:52:29.916 UTC [12] LOG:  database system was shut down at 2026-01-30 14:51:39 UTC
2026-01-30 14:52:30.164 UTC [1] LOG:  database system is ready to accept connections
```

If the database is not ready to accept connections and there is an incoming connection the following will be also logged on the startup;

```
2026-02-13 16:06:36.222 UTC [13] FATAL:  the database system is starting up
```

Above `FATAL` error could be also caused by Pukki trying to ping the database.

#### Volume & instance resize, instance rebuild and upgrade

These are from Pukki's database logging point of view just a shutdown and startup.

Upgrade does other actions on background but logs of these are not shown to the user.

#### Database creation and database restore

Database restore is essentially just database creation from the database's logging stand point.

Creating a database generates one-off log lines and it will end to same `database system is ready to accept connections` message like startup does;
```
The files belonging to this database system will be owned by user "postgres".
This user must also own the server process.

The database cluster will be initialized with locale "en_US.utf8".
The default database encoding has accordingly been set to "UTF8".
The default text search configuration will be set to "english".

Data page checksums are disabled.

fixing permissions on existing directory /var/lib/postgresql/data/pgdata ... ok
creating subdirectories ... ok
selecting dynamic shared memory implementation ... posix
selecting default "max_connections" ... 100
selecting default "shared_buffers" ... 128MB
selecting default time zone ... Etc/UTC
creating configuration files ... ok
running bootstrap script ... ok
performing post-bootstrap initialization ... ok
syncing data to disk ... ok

initdb: warning: enabling "trust" authentication for local connections
initdb: hint: You can change this by editing pg_hba.conf or using the option -A, or --auth-local and --auth-host, the next time you run initdb.

Success. You can now start the database server using:

    pg_ctl -D /var/lib/postgresql/data/pgdata -l logfile start

waiting for server to start....
2026-07-30 15:13:26.068 UTC [31] LOG:  starting PostgreSQL 17.6 (Debian 17.6-1.pgdg13+1) on x86_64-pc-linux-gnu, compiled by gcc (Debian 14.2.0-19) 14.2.0, 64-bit
2026-07-30 15:13:26.091 UTC [31] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
2026-07-30 15:13:26.121 UTC [34] LOG:  database system was shut down at 2026-07-30 15:13:25 UTC
2026-07-30 15:13:26.135 UTC [31] LOG:  database system is ready to accept connections
 done
server started

/usr/local/bin/docker-entrypoint.sh: ignoring /docker-entrypoint-initdb.d/*

waiting for server to shut down....
2026-07-30 15:13:26.260 UTC [31] LOG:  received fast shutdown request
2026-07-30 15:13:26.264 UTC [31] LOG:  aborting any active transactions
2026-07-30 15:13:26.268 UTC [31] LOG:  background worker "logical replication launcher" (PID 37) exited with exit code 1
2026-07-30 15:13:26.272 UTC [32] LOG:  shutting down
2026-07-30 15:13:26.275 UTC [32] LOG:  checkpoint starting: shutdown immediate
2026-07-30 15:13:26.320 UTC [32] LOG:  checkpoint complete: wrote 3 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.001 s, sync=0.006 s, total=0.048 s; sync files=2, longest=0.004 s, average=0.003 s; distance=0 kB, estimate=0 kB; lsn=0/14ED7F0, redo lsn=0/14ED7F0
2026-07-30 15:13:26.327 UTC [31] LOG:  database system is shut down
 done
server stopped

PostgreSQL init process complete; ready for start up.

2026-07-30 15:13:26.410 UTC [1] LOG:  starting PostgreSQL 17.6 (Debian 17.6-1.pgdg13+1) on x86_64-pc-linux-gnu, compiled by gcc (Debian 14.2.0-19) 14.2.0, 64-bit
2026-07-30 15:13:26.411 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
2026-07-30 15:13:26.411 UTC [1] LOG:  listening on IPv6 address "::", port 5432
2026-07-30 15:13:26.433 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
2026-07-30 15:13:26.442 UTC [45] LOG:  database system was shut down at 2026-07-30 15:13:26 UTC
2026-07-30 15:13:26.483 UTC [1] LOG:  database system is ready to accept connections
```

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

Note worthy here is that if database has incorrect configurations during any startup then it will end in to restart loop without never successully starting to serve connections;
```

PostgreSQL Database directory appears to contain a database; Skipping initialization

2026-06-12 14:29:30.314 UTC [1] FATAL:  configuration file "/etc/postgresql/conf.d/20-user-001-common.conf" contains errors
2026-06-12 14:29:30.314 UTC [1] HINT:  Valid units for this parameter are "B", "kB", "MB", "GB", and "TB".
2026-06-12 14:29:30.314 UTC [1] LOG:  invalid value for parameter "work_mem": "8M"

PostgreSQL Database directory appears to contain a database; Skipping initialization

2026-06-12 14:29:30.907 UTC [1] FATAL:  configuration file "/etc/postgresql/conf.d/20-user-001-common.conf" contains errors
2026-06-12 14:29:30.907 UTC [1] HINT:  Valid units for this parameter are "B", "kB", "MB", "GB", and "TB".
2026-06-12 14:29:30.907 UTC [1] LOG:  invalid value for parameter "work_mem": "8M"

PostgreSQL Database directory appears to contain a database; Skipping initialization

2026-06-12 14:29:31.630 UTC [1] FATAL:  configuration file "/etc/postgresql/conf.d/20-user-001-common.conf" contains errors
2026-06-12 14:29:31.630 UTC [1] HINT:  Valid units for this parameter are "B", "kB", "MB", "GB", and "TB".
2026-06-12 14:29:31.630 UTC [1] LOG:  invalid value for parameter "work_mem": "8M"
...
```

#### Trying to create a database with non-existing encoding or/and collation

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

!!! info "Note"
    Maybe someone authorized was trying manually to connect to the database or maybe it is some background job failing to connect, which effects was not visible. Consider these also to be possible break-in attempts.


#### User does not exists

```
2026-02-13 15:49:25.063 UTC [80256] DETAIL:  Role "test" does not exist.
2026-02-13 15:49:25.063 UTC [80256] FATAL:  password authentication failed for user "test"
	Connection matched file "/etc/postgresql/pg_hba.conf" line 9: "host all all 0.0.0.0/0 md5"
```

!!! info "Note"
    Maybe someone authorized was trying manually to connect to the database or maybe it is some background job failing to connect, which effects was not visible. Consider these also to be possible break-in attempts.


#### Transaction was committed or rollbacked and there was no transaction started in the first place

```
2026-02-13 16:00:16.900 UTC [35] WARNING:  there is no transaction in progress
```

#### Typos when running SQLs manually

```
2026-01-30 14:58:32.882 UTC [64] ERROR:  syntax error at or near "test" at character 8
2026-01-30 14:58:32.882 UTC [64] STATEMENT:  CREATE test AS SELECT GENERATE_SERIES(1,500000) AS id, MD5(RANDOM()::TEXT) AS random_text;
```


#### Connection was not closed properly from the client side

```
2026-02-13 16:32:56.591 UTC [60] LOG:  could not receive data from client: Connection reset by peer
```

!!! info "Note"
    Usually these are improperly closed connections, but there is a possibility that network connection between application and database has been interrupted during transaction, causing resource intesive rollback, so these cannot be completely ignored either.

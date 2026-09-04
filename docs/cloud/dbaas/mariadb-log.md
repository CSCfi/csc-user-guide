# Server log in MariaDB

Server log in MariaDB gives important information from database's current health and operation.

## How to access database logs

[Via CLI](advanced.md#how-to-access-database-logs)

[Via Web UI](web-interface.md#how-to-access-database-logs)

If you think there are missing log lines, please [contact CSC Service Desk](/support/contact.md) for assistance.

## What to look for
Error log in MariaDB should be quite quiet, having  `note` and some `warning` level messages related to DB's startup, shutdown, creation, upgrade or restore related operations.

MariaDB does not by default log anything performance related unlike PostgreSQL.

### Most important log entries

User authentication, idle connections and networking issues are what should be kept eye on.

#### Incorrect password or user does not exists

In this example the first attempt did not specify password when connecting and the second one used incorrect password.

The log line looks same in case of incorrect password or trying to connect with user that does not exists.

```
2026-09-04 13:45:54 10 [Warning] Access denied for user 'testuser'@'$random_container_id' (using password: NO)
2026-09-04 13:46:04 13 [Warning] Access denied for user 'testuser'@'$random_container_id' (using password: YES)
```

!!! info "Note"
    Maybe someone authorized was trying manually to connect to the database or maybe it is some background job failing to connect, which effects was not visible. Consider these also to be possible break-in attempts.

#### Idle connections

Session's `wait_timeout` or/and `interactive_timeout` is exceeded.

```
2026-09-04 14:13:43 nn [Warning] Aborted connection nn to db: 'test' user: 'testuser' host: '$random_container_id' (Got timeout reading communication packets)
```

!!! info "Note"
    Usually these are connections timing out due to inactivity, but there is a possibility that there is and open transaction and exceeding timeout would cause resource intesive rollback, so these cannot be completely ignored either.

#### Connection was not closed properly from the client side

Session's `wait_timeout` or/and `interactive_timeout` is exceeded.

```
2026-09-04 14:15:55 nn [Warning] Aborted connection nn to db: 'test' user: 'testuser' host: '$random_container_id' (Got an error reading communication packets)
```

!!! info "Note"
    Usually these are improperly closed connections, but there is a possibility that network connection between application and database has been interrupted during transaction, causing resource intesive rollback, so these cannot be completely ignored either.

### Other common messages

#### Database shutdown messages

```
2026-07-31 11:24:40 0 [Note] mariadbd (initiated by: unknown): Normal shutdown
2026-07-31 11:24:40 0 [Note] InnoDB: FTS optimize thread exiting.
2026-07-31 11:24:40 0 [Note] InnoDB: Starting shutdown...
2026-07-31 11:24:40 0 [Note] InnoDB: Dumping buffer pool(s) to /var/lib/mysql/data/ib_buffer_pool
2026-07-31 11:24:40 0 [Note] InnoDB: Buffer pool(s) dump completed at 260731 11:24:40
2026-07-31 11:24:40 0 [Note] InnoDB: Removed temporary tablespace data file: "./ibtmp1"
2026-07-31 11:24:40 0 [Note] Shutdown completed; log sequence number 45434; transaction id 15
2026-07-31 11:24:40 0 [Note] mariadbd: Shutdown complete
```

#### Database deletion

The database is shutdown and logs are removed.

#### Database startup messages

```
2026-07-31 11:25:03+00:00 [Note] [Entrypoint]: Entrypoint script for MariaDB Server 1:12.3.2+maria~ubu2404 started.
2026-07-31 11:25:04+00:00 [Note] [Entrypoint]: MariaDB upgrade not required
2026-07-31 11:25:04 0 [Note] Starting MariaDB 12.3.2-MariaDB-ubu2404 source revision 9f98f82b14a9b939834281672b6d0cf965db69a3 server_uid EyzeXj9hFGkY2KB6IldPXNvLAmI= as process 1
2026-07-31 11:25:04 0 [Note] InnoDB: Compressed tables use zlib 1.3
2026-07-31 11:25:04 0 [Note] InnoDB: Number of transaction pools: 1
2026-07-31 11:25:04 0 [Note] InnoDB: Using crc32 + pclmulqdq instructions
2026-07-31 11:25:04 0 [Note] mariadbd: O_TMPFILE is not supported on /var/tmp (disabling future attempts)
2026-07-31 11:25:04 0 [Warning] mariadbd: io_uring_queue_init() failed with ENOSYS: check seccomp filters, and the kernel version (newer than 5.1 required)
create_uring failed: falling back to libaio
2026-07-31 11:25:04 0 [Note] InnoDB: Using Linux native AIO
2026-07-31 11:25:04 0 [Note] InnoDB: innodb_buffer_pool_size_max=8388608m, innodb_buffer_pool_size=585m
2026-07-31 11:25:04 0 [Note] InnoDB: Completed initialization of buffer pool
2026-07-31 11:25:04 0 [Note] InnoDB: File system buffers for log disabled (block size=512 bytes)
2026-07-31 11:25:05 0 [Note] InnoDB: End of log at LSN=45434
2026-07-31 11:25:05 0 [Note] InnoDB: Opened 3 undo tablespaces
2026-07-31 11:25:05 0 [Note] InnoDB: 128 rollback segments in 3 undo tablespaces are active.
2026-07-31 11:25:05 0 [Note] InnoDB: Setting file './ibtmp1' size to 12.000MiB. Physically writing the file full; Please wait ...
2026-07-31 11:25:05 0 [Note] InnoDB: File './ibtmp1' size is now 12.000MiB.
2026-07-31 11:25:05 0 [Note] InnoDB: log sequence number 45434; transaction id 14
2026-07-31 11:25:05 0 [Note] Plugin 'FEEDBACK' is disabled.
2026-07-31 11:25:05 0 [Note] InnoDB: Loading buffer pool(s) from /var/lib/mysql/data/ib_buffer_pool
2026-07-31 11:25:05 0 [Note] Plugin 'wsrep-provider' is disabled.
2026-07-31 11:25:05 0 [Note] InnoDB: Buffer pool(s) load completed at 260731 11:25:05
2026-07-31 11:25:05 0 [Note] Server socket created on IP: '0.0.0.0', port: '3306'.
2026-07-31 11:25:05 0 [Note] Server socket created on IP: '::', port: '3306'.
2026-07-31 11:25:05 0 [Note] mariadbd: Event Scheduler: Loaded 0 events
2026-07-31 11:25:05 0 [Note] mariadbd: ready for connections.
Version: '12.3.2-MariaDB-ubu2404'  socket: '/var/run/mysqld/mysqld.sock'  port: 3306  mariadb.org binary distribution
```

#### Volume & instance resize and instance rebuild

These are from Pukki's database logging point of view just a shutdown and startup. 

#### Database creation

In reality it is a startup and shutdown of a temporary server, ending up to normal startup sequence.

```
2026-07-31 11:13:27+00:00 [Note] [Entrypoint]: Entrypoint script for MariaDB Server 1:12.3.2+maria~ubu2404 started.
2026-07-31 11:13:27+00:00 [Note] [Entrypoint]: Initializing database files
2026-07-31 11:13:28 0 [Warning] mariadbd: io_uring_queue_init() failed with ENOSYS: check seccomp filters, and the kernel version (newer than 5.1 required)
create_uring failed: falling back to libaio
2026-07-31 11:13:35+00:00 [Note] [Entrypoint]: Database files initialized
2026-07-31 11:13:35+00:00 [Note] [Entrypoint]: Starting temporary server
2026-07-31 11:13:35+00:00 [Note] [Entrypoint]: Waiting for server startup
2026-07-31 11:13:35 0 [Note] Starting MariaDB 12.3.2-MariaDB-ubu2404 source revision 9f98f82b14a9b939834281672b6d0cf965db69a3 server_uid egNqd3RMI8NBLcrM8AFVQ1ZmMnc= as process 69
2026-07-31 11:13:35 0 [Note] InnoDB: Compressed tables use zlib 1.3
2026-07-31 11:13:35 0 [Note] InnoDB: Number of transaction pools: 1
2026-07-31 11:13:35 0 [Note] InnoDB: Using crc32 + pclmulqdq instructions
2026-07-31 11:13:35 0 [Note] mariadbd: O_TMPFILE is not supported on /var/tmp (disabling future attempts)
2026-07-31 11:13:35 0 [Warning] mariadbd: io_uring_queue_init() failed with ENOSYS: check seccomp filters, and the kernel version (newer than 5.1 required)
create_uring failed: falling back to libaio
2026-07-31 11:13:35 0 [Note] InnoDB: Using Linux native AIO
2026-07-31 11:13:35 0 [Note] InnoDB: innodb_buffer_pool_size_max=8388608m, innodb_buffer_pool_size=585m
2026-07-31 11:13:35 0 [Note] InnoDB: Completed initialization of buffer pool
2026-07-31 11:13:35 0 [Note] InnoDB: File system buffers for log disabled (block size=512 bytes)
2026-07-31 11:13:35 0 [Note] InnoDB: End of log at LSN=45434
2026-07-31 11:13:35 0 [Note] InnoDB: Opened 3 undo tablespaces
2026-07-31 11:13:35 0 [Note] InnoDB: 128 rollback segments in 3 undo tablespaces are active.
2026-07-31 11:13:35 0 [Note] InnoDB: Setting file './ibtmp1' size to 12.000MiB. Physically writing the file full; Please wait ...
2026-07-31 11:13:35 0 [Note] InnoDB: File './ibtmp1' size is now 12.000MiB.
2026-07-31 11:13:35 0 [Note] InnoDB: log sequence number 45434; transaction id 14
2026-07-31 11:13:35 0 [Note] Plugin 'FEEDBACK' is disabled.
2026-07-31 11:13:35 0 [Note] Plugin 'wsrep-provider' is disabled.
2026-07-31 11:13:37 0 [Note] mariadbd: Event Scheduler: Loaded 0 events
2026-07-31 11:13:37 0 [Note] Replication not automatically started: --skip-slave-start was specified
2026-07-31 11:13:37 0 [Note] mariadbd: ready for connections.
Version: '12.3.2-MariaDB-ubu2404'  socket: '/var/run/mysqld/mysqld.sock'  port: 0  mariadb.org binary distribution
2026-07-31 11:13:37+00:00 [Note] [Entrypoint]: Temporary server started.
2026-07-31 11:13:37+00:00 [Note] [Entrypoint]: Securing system users (equivalent to running mysql_secure_installation)

2026-07-31 11:13:37+00:00 [Note] [Entrypoint]: Stopping temporary server
2026-07-31 11:13:37 0 [Note] mariadbd (initiated by: unknown): Normal shutdown
2026-07-31 11:13:37 0 [Note] InnoDB: FTS optimize thread exiting.
2026-07-31 11:13:37 0 [Note] InnoDB: Starting shutdown...
2026-07-31 11:13:37 0 [Note] InnoDB: Dumping buffer pool(s) to /var/lib/mysql/data/ib_buffer_pool
2026-07-31 11:13:37 0 [Note] InnoDB: Buffer pool(s) dump completed at 260731 11:13:37
2026-07-31 11:13:37 0 [Note] InnoDB: Removed temporary tablespace data file: "./ibtmp1"
2026-07-31 11:13:37 0 [Note] Shutdown completed; log sequence number 45434; transaction id 15
2026-07-31 11:13:37 0 [Note] mariadbd: Shutdown complete
2026-07-31 11:13:37+00:00 [Note] [Entrypoint]: Temporary server stopped

2026-07-31 11:13:37+00:00 [Note] [Entrypoint]: MariaDB init process done. Ready for start up.

2026-07-31 11:13:37 0 [Note] Starting MariaDB 12.3.2-MariaDB-ubu2404 source revision 9f98f82b14a9b939834281672b6d0cf965db69a3 server_uid LHJrEVwvk3gicX/VZJNJIPNtkBM= as process 1
2026-07-31 11:13:37 0 [Note] InnoDB: Compressed tables use zlib 1.3
2026-07-31 11:13:37 0 [Note] InnoDB: Number of transaction pools: 1
2026-07-31 11:13:37 0 [Note] InnoDB: Using crc32 + pclmulqdq instructions
2026-07-31 11:13:37 0 [Note] mariadbd: O_TMPFILE is not supported on /var/tmp (disabling future attempts)
2026-07-31 11:13:37 0 [Warning] mariadbd: io_uring_queue_init() failed with ENOSYS: check seccomp filters, and the kernel version (newer than 5.1 required)
create_uring failed: falling back to libaio
2026-07-31 11:13:37 0 [Note] InnoDB: Using Linux native AIO
2026-07-31 11:13:37 0 [Note] InnoDB: innodb_buffer_pool_size_max=8388608m, innodb_buffer_pool_size=585m
2026-07-31 11:13:37 0 [Note] InnoDB: Completed initialization of buffer pool
2026-07-31 11:13:37 0 [Note] InnoDB: File system buffers for log disabled (block size=512 bytes)
2026-07-31 11:13:38 0 [Note] InnoDB: End of log at LSN=45434
2026-07-31 11:13:38 0 [Note] InnoDB: Opened 3 undo tablespaces
2026-07-31 11:13:38 0 [Note] InnoDB: 128 rollback segments in 3 undo tablespaces are active.
2026-07-31 11:13:38 0 [Note] InnoDB: Setting file './ibtmp1' size to 12.000MiB. Physically writing the file full; Please wait ...
2026-07-31 11:13:38 0 [Note] InnoDB: File './ibtmp1' size is now 12.000MiB.
2026-07-31 11:13:38 0 [Note] InnoDB: log sequence number 45434; transaction id 14
2026-07-31 11:13:38 0 [Note] InnoDB: Loading buffer pool(s) from /var/lib/mysql/data/ib_buffer_pool
2026-07-31 11:13:38 0 [Note] Plugin 'FEEDBACK' is disabled.
2026-07-31 11:13:38 0 [Note] Plugin 'wsrep-provider' is disabled.
2026-07-31 11:13:38 0 [Note] InnoDB: Buffer pool(s) load completed at 260731 11:13:38
2026-07-31 11:13:38 0 [Note] Server socket created on IP: '0.0.0.0', port: '3306'.
2026-07-31 11:13:38 0 [Note] Server socket created on IP: '::', port: '3306'.
2026-07-31 11:13:38 0 [Note] mariadbd: Event Scheduler: Loaded 0 events
2026-07-31 11:13:38 0 [Note] mariadbd: ready for connections.
Version: '12.3.2-MariaDB-ubu2404'  socket: '/var/run/mysqld/mysqld.sock'  port: 3306  mariadb.org binary distribution
```

#### Database upgrade and restore

Database restore does not have MariaDB's previous version information available and therefore upgrade process is forced during the restore.

Database upgrade performs first normal shutdown which is not shown on below.


```
2026-07-31 12:12:13+00:00 [Note] [Entrypoint]: Entrypoint script for MariaDB Server 1:12.3.2+maria~ubu2404 started.
2026-07-31 12:12:13+00:00 [Note] [Entrypoint]: Starting temporary server
2026-07-31 12:12:13+00:00 [Note] [Entrypoint]: Waiting for server startup
2026-07-31 12:12:13 0 [Note] Starting MariaDB 12.3.2-MariaDB-ubu2404 source revision 9f98f82b14a9b939834281672b6d0cf965db69a3 server_uid Vnw/L/9Hmc/hL5x+5WL4PP9R2jY= as process 23
2026-07-31 12:12:13 0 [Note] InnoDB: Compressed tables use zlib 1.3
2026-07-31 12:12:13 0 [Note] InnoDB: Number of transaction pools: 1
2026-07-31 12:12:13 0 [Note] InnoDB: Using crc32 + pclmulqdq instructions
2026-07-31 12:12:13 0 [Note] mariadbd: O_TMPFILE is not supported on /var/tmp (disabling future attempts)
2026-07-31 12:12:13 0 [Warning] mariadbd: io_uring_queue_init() failed with ENOSYS: check seccomp filters, and the kernel version (newer than 5.1 required)
create_uring failed: falling back to libaio
2026-07-31 12:12:13 0 [Note] InnoDB: Using Linux native AIO
2026-07-31 12:12:13 0 [Note] InnoDB: innodb_buffer_pool_size_max=8388608m, innodb_buffer_pool_size=585m
2026-07-31 12:12:13 0 [Note] InnoDB: Completed initialization of buffer pool
2026-07-31 12:12:13 0 [Note] InnoDB: File system buffers for log disabled (block size=512 bytes)
2026-07-31 12:12:14 0 [Note] InnoDB: End of log at LSN=47629
2026-07-31 12:12:17 0 [Note] InnoDB: Opened 3 undo tablespaces
2026-07-31 12:12:17 0 [Note] InnoDB: 128 rollback segments in 3 undo tablespaces are active.
2026-07-31 12:12:17 0 [Note] InnoDB: Setting file './ibtmp1' size to 12.000MiB. Physically writing the file full; Please wait ...
2026-07-31 12:12:17 0 [Note] InnoDB: File './ibtmp1' size is now 12.000MiB.
2026-07-31 12:12:17 0 [Note] InnoDB: log sequence number 47629; transaction id 14
2026-07-31 12:12:17 0 [Note] Plugin 'FEEDBACK' is disabled.
2026-07-31 12:12:17 0 [Note] Plugin 'wsrep-provider' is disabled.
2026-07-31 12:12:19 0 [Note] Replication not automatically started: --skip-slave-start was specified
2026-07-31 12:12:19 0 [Note] mariadbd: ready for connections.
Version: '12.3.2-MariaDB-ubu2404'  socket: '/var/run/mysqld/mysqld.sock'  port: 0  mariadb.org binary distribution
2026-07-31 12:12:19+00:00 [Note] [Entrypoint]: Temporary server started.
2026-07-31 12:12:19+00:00 [Note] [Entrypoint]: Backing up system database to system_mysql_backup_11.5.2-MariaDB.sql.zst
2026-07-31 12:12:20+00:00 [Note] [Entrypoint]: Backing up complete
2026-07-31 12:12:20+00:00 [Note] [Entrypoint]: Starting mariadb-upgrade
The --upgrade-system-tables option was used, user tables won't be touched.
Major version upgrade detected from 11.5.2-MariaDB to 12.3.2-MariaDB. Check required!
Phase 1/8: Checking and upgrading mysql database
Processing databases
mysql
mysql.column_stats                                 OK
mysql.columns_priv                                 OK
mysql.db                                           OK
mysql.event                                        OK
mysql.func                                         OK
mysql.global_priv                                  OK
mysql.gtid_slave_pos                               OK
mysql.help_category                                OK
mysql.help_keyword                                 OK
mysql.help_relation                                OK
mysql.help_topic                                   OK
mysql.index_stats                                  OK
mysql.innodb_index_stats                           OK
mysql.innodb_table_stats                           OK
mysql.plugin                                       OK
mysql.proc                                         OK
mysql.procs_priv                                   OK
mysql.proxies_priv                                 OK
mysql.roles_mapping                                OK
mysql.servers                                      OK
mysql.table_stats                                  OK
mysql.tables_priv                                  OK
mysql.time_zone                                    OK
mysql.time_zone_leap_second                        OK
mysql.time_zone_name                               OK
mysql.time_zone_transition                         OK
mysql.time_zone_transition_type                    OK
mysql.transaction_registry                         OK
Phase 2/8: Installing used storage engines... Skipped
Phase 3/8: Running 'mysql_fix_privilege_tables'
Phase 4/8: Fixing views... Skipped
Phase 5/8: Fixing table and database names ... Skipped
Phase 6/8: Checking and upgrading tables... Skipped
Phase 7/8: uninstalling plugins
Phase 8/8: Running 'FLUSH PRIVILEGES'
OK
2026-07-31 12:12:30+00:00 [Note] [Entrypoint]: Finished mariadb-upgrade
2026-07-31 12:12:30+00:00 [Note] [Entrypoint]: Stopping temporary server
2026-07-31 12:12:30 0 [Note] mariadbd (initiated by: unknown): Normal shutdown
2026-07-31 12:12:30 0 [Note] InnoDB: FTS optimize thread exiting.
2026-07-31 12:12:30 0 [Note] InnoDB: Starting shutdown...
2026-07-31 12:12:30 0 [Note] InnoDB: Removed temporary tablespace data file: "./ibtmp1"
2026-07-31 12:12:30 0 [Note] Shutdown completed; log sequence number 47629; transaction id 18
2026-07-31 12:12:30 0 [Note] mariadbd: Shutdown complete
2026-07-31 12:12:30+00:00 [Note] [Entrypoint]: Temporary server stopped
2026-07-31 12:12:30 0 [Note] Starting MariaDB 12.3.2-MariaDB-ubu2404 source revision 9f98f82b14a9b939834281672b6d0cf965db69a3 server_uid MN96or91SZL7RSSRjfx8aZgd768= as process 1
2026-07-31 12:12:30 0 [Note] InnoDB: Compressed tables use zlib 1.3
2026-07-31 12:12:30 0 [Note] InnoDB: Number of transaction pools: 1
2026-07-31 12:12:30 0 [Note] InnoDB: Using crc32 + pclmulqdq instructions
2026-07-31 12:12:30 0 [Note] mariadbd: O_TMPFILE is not supported on /var/tmp (disabling future attempts)
2026-07-31 12:12:30 0 [Warning] mariadbd: io_uring_queue_init() failed with ENOSYS: check seccomp filters, and the kernel version (newer than 5.1 required)
create_uring failed: falling back to libaio
2026-07-31 12:12:30 0 [Note] InnoDB: Using Linux native AIO
2026-07-31 12:12:30 0 [Note] InnoDB: innodb_buffer_pool_size_max=8388608m, innodb_buffer_pool_size=585m
2026-07-31 12:12:30 0 [Note] InnoDB: Completed initialization of buffer pool
2026-07-31 12:12:30 0 [Note] InnoDB: File system buffers for log disabled (block size=512 bytes)
2026-07-31 12:12:30 0 [Note] InnoDB: End of log at LSN=47629
2026-07-31 12:12:30 0 [Note] InnoDB: Opened 3 undo tablespaces
2026-07-31 12:12:30 0 [Note] InnoDB: 128 rollback segments in 3 undo tablespaces are active.
2026-07-31 12:12:30 0 [Note] InnoDB: Setting file './ibtmp1' size to 12.000MiB. Physically writing the file full; Please wait ...
2026-07-31 12:12:30 0 [Note] InnoDB: File './ibtmp1' size is now 12.000MiB.
2026-07-31 12:12:30 0 [Note] InnoDB: log sequence number 47629; transaction id 14
2026-07-31 12:12:30 0 [Note] InnoDB: Loading buffer pool(s) from /var/lib/mysql/data/ib_buffer_pool
2026-07-31 12:12:30 0 [Note] Plugin 'FEEDBACK' is disabled.
2026-07-31 12:12:30 0 [Note] Plugin 'wsrep-provider' is disabled.
2026-07-31 12:12:30 0 [Note] InnoDB: Buffer pool(s) load completed at 260731 12:12:30
2026-07-31 12:12:30 0 [Note] Server socket created on IP: '0.0.0.0', port: '3306'.
2026-07-31 12:12:30 0 [Note] Server socket created on IP: '::', port: '3306'.
2026-07-31 12:12:30 0 [Note] mariadbd: Event Scheduler: Loaded 0 events
2026-07-31 12:12:30 0 [Note] mariadbd: ready for connections.
Version: '12.3.2-MariaDB-ubu2404'  socket: '/var/run/mysqld/mysqld.sock'  port: 3306  mariadb.org binary distribution
```

The restore process also prints following which is not an issue;
```
2026-07-31 11:36:35 0 [Note] InnoDB: Cannot open '/var/lib/mysql/data/ib_buffer_pool' for reading: No such file or directory
```

#### SQL level errors

For instance, typos entered in command-line interface (CLI), in MariaDB's case nothing will be logged in server log.

Committing or rolling back a transaction when transaction was not explicitly started does not cause an error and transaction control language (TCL) is just performed.

MariaDB's behaviour differs from for example PostgreSQL in these cases.

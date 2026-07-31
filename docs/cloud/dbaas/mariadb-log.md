# Server log in MariaDB

Server log in MariaDB gives important information from database's current health and operation.

## How to access database logs

[Via CLI](advanced.md#how-to-access-database-logs)

[Via Web UI](web-interface.md#how-to-access-database-logs)

If you think there are missing log lines, please [contact CSC Service Desk](/support/contact.md) for assistance.

## What to look for
Error log in MariaDB should be quite quiet, having  `note` and some `warning` level messages from startup and from possible shutdown.

What other messages can be usually seen in error log;

* **Aborted connection:** Usually these are connections timing out due to inactivity. There is a possibility that network connection between application and database has been interrupted during transaction, causing resource intesive rollback, so these cannot be completely ignored either.
* **Access denied:** Maybe someone authorized was trying manually to connect to the database or maybe it is some background job failing to connect, which effects was not visible. Consider these also to be possible break-in attempts.

Any other message that requires attention (including `note` and `warning` level messages) are usually related to performance of the database.

### Common messages

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

In reality it is just a startup and shutdown of temporary server, ending up to normal startup sequence.

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

#### Rewrite What to look for section

#### Incorrect password???

#### User does not exists????

#### Transaction was committed or rollbacked and there was no transaction started in the first place???

#### Typos when running SQLs manually???

#### Connection was not closed properly from the client side

#### Database deletion

Shutdown and logs are removed also. Add to PG too.
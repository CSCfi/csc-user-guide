# Error log in MariaDB

Error log in MariaDB gives important information from database's current health and operation.

## How to access database logs

**Note:** If the system does not return any log lines in either methods then that means there are no log entries within the 1 month retention period which is common to MariaDBs.

### OpenStack CLI

Onces you got your OpenStack running, you can list your databases;

```
$ openstack database instance list
+--------------------------------------+---------------------------+------------+-------------------+--------+------------------+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------+------+------+
| ID                                   | Name                      | Datastore  | Datastore Version | Status | Operating Status | Public | Addresses                                                                                                                                                | Flavor ID                            | Size | Role |
+--------------------------------------+---------------------------+------------+-------------------+--------+------------------+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------+------+------+
| 0a8b6df2-140d-4932-b477-b3d3a881fecf | mariadb-12-12-14:03:13    | mariadb    | 11.4.8            | ACTIVE | HEALTHY          | True   | [{'address': '192.168.240.106', 'type': 'private', 'network': '51e07f88-483a-4aaf-a349-2277f6afaabe'}, {'address': '195.148.20.137', 'type': 'public'}]  | d4a2cb9c-99da-4e0f-82d7-3313cca2b2c2 |    1 |      |
+--------------------------------------+---------------------------+------------+-------------------+--------+------------------+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------+------+------+

```

Using the ID from above command you can get the database log;

```
$ openstack database log list -f value -c Status 0a8b6df2-140d-4932-b477-b3d3a881fecf | sort
```

In Unix-like systems you can use `tail` command to output only last n lines;
```
$ openstack database log list -f value -c Status 0a8b6df2-140d-4932-b477-b3d3a881fecf | sort | tail -10
```

### Web UI

Access the Web UI in [https://pukki.dbaas.csc.fi/project](url), click the `instance name` and go to `logs` tab.

**Note:** If log lines are with same `timestamp` then log lines may be displayd in bit of a mixed order.

## What to look for
Error log in MariaDB should be quite quiet, having  `note` and some `warning` level messages from statup and from possible shutdown.

What other messages can be usually seen in error log;

* **Aborted connection:** Usually these are connections timing out due to inactivity. There is a possibility that network connection between application and database has been interrupted during transaction, causing resource intesive rollback, so these cannot be completelly ignored either.
* **Access denied:** Maybe someone authorized was trying manually to connect to the database or maybe it is some background job failing to connect, which effects was not visible. Consider these also to be possible break-in attempts.

Any other message that requires attention (including `note` and `warning` level messages) are usually related to performance of the database.

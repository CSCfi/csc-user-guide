# Server log in MariaDB

Server log in MariaDB gives important information from database's current health and operation.

## How to access database logs

Link to openstack cli page

Link to web ui page

## What to look for
Error log in MariaDB should be quite quiet, having  `note` and some `warning` level messages from statup and from possible shutdown.

What other messages can be usually seen in error log;

* **Aborted connection:** Usually these are connections timing out due to inactivity. There is a possibility that network connection between application and database has been interrupted during transaction, causing resource intesive rollback, so these cannot be completely ignored either.
* **Access denied:** Maybe someone authorized was trying manually to connect to the database or maybe it is some background job failing to connect, which effects was not visible. Consider these also to be possible break-in attempts.

Any other message that requires attention (including `note` and `warning` level messages) are usually related to performance of the database.

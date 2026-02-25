# PostgreSQL 14 end-of-life in Pukki

As PostgreSQL 14's end-of-life date is set to arrive on 12th of November, 2026, support for it will be removed from Pukki by then. Creating new PostgreSQL 14 instances or restoring backups created from such instances will be unavailable afterwards.

Any database instances remaining on PostgreSQL 14 will be upgraded to PostgreSQL 17 by Pukki admins starting on the EOL date. However, we strongly recommend performing the upgrade yourself, so that you have control over the resulting downtime, and can make sure everything that depends on the database continues to function.

You can find more information on upgrading database instances in Pukki on the [database operations page here](operations.md), and some information regarding PostgreSQL versions on the [PostgreSQL versions page here](postgres-versions.md).

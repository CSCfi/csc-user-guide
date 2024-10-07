# PostgreSQL versions

Currently Pukki supports two major versions of PostgreSQL, 14 and 17. We recommend always using
the most recent version available when creating new database instances, and existing ones can
be upgraded to use newer minor or major versions. For more detailed information on differences
between all PostgreSQL versions, consult the
[PostgreSQL documentation](https://www.postgresql.org/docs/release/).

## Minor version upgrades

Minor version upgrades in PostgreSQL (e.g. from 14.12 to 14.13) should have no breaking changes.
The upgrade process itself happens automatically in the background once initiated, and should only
take a couple of minutes. It involves shutting down the existing server, installing the new version,
and starting the server back up, without modifying the data itself in any way.

## Major version upgrades

Major version upgrades shouldn't be visibly different from minor version upgrades to a Pukki user,
but there's a lot more going on under the hood, and an increased risk of something going wrong in
the process. There's a real risk of data loss, and the user should be ready to create a new
database instance from a backup in such a case.

Before upgrading your database to a new major version, we heavily recommend using a backup of it
to create a new database instance just for testing the upgrade first. Upgrading between major
versions requires significantly more disk space than minor version upgrades, and if there isn't
enough disk space available, the upgrade will fail. In these cases increasing volume size before
attempting a major version upgrade is necessary.

Downgrading to a previous major version is not possible in Pukki. The only way to return to an
older major version is to restore an old backup from before the upgrade.

## Changes between PostgreSQL 14 and 17

Most of the changes to PostgreSQL between versions 14 and 17 won't be visible to the user. Many of
them are focused on server side performance, logging, and more advanced and specific SQL features.
However, PostgreSQL 15 brought a very specific change to default permissions, which affects how
Pukki manages users and their access rights.

It is important to know if you update a PostgreSQL database 14 to 17 the permissions continues
to work in the same way as the 14 database. So if you have a production database that was updated
from a PostgreSQL 14 to 17 and a development database that was created as a PostgreSQL 17 database
their permissions might work differently.

### Differences in how Pukki manages database access


On PostgreSQL 14 database instances, the default permissions allow all database users to connect
to any database and create tables in the public schema.

On PostgreSQL 17 database instances, you need to explicitly grant users access to a database to
allow them to create tables in the public schema of the specified database. This can be done as
follows with the command line tools. This makes it a lot easier to create read-only users in
PostgreSQL 17.




## Some useful commands

### Show the current database version

```sql
SELECT 1;
```

### Import database dump

If you have a database dump, you can import it to your Pukki database with the following command. Be aware that this might overwrite what you already have in the database:

```bash
psql -h $FLOATING_IP -d $DATABASE -U USERNAME -f file.sql
```

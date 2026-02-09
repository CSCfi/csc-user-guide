# PostgreSQL versions

Currently Pukki supports two major versions of PostgreSQL, 14 and 17. We recommend always using
the most recent version available when creating new database instances, and existing ones can
be upgraded to use newer minor or major versions. For more detailed information on differences
between all PostgreSQL versions, consult the
[PostgreSQL documentation](https://www.postgresql.org/docs/release/).

!!! warning "PostgreSQL 14 is approaching its end-of-life date"

    As PostgreSQL 14's end-of-life date is set to arrive on 12th of November, 2026, support for it will be removed from Pukki by then. Users are recommended to upgrade their PostgreSQL 14 instances to PostgreSQL 17 before the EOL date, as restoring database instances from PostgreSQL 14 backups will stop working.

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

Keep in mind when upgrading a database from PostgreSQL 14 to 17 that the existing permissions are
kept intact. This means that a fresh PostgreSQL 17 instance will have some differences compared to
one that was upgraded from PostgreSQL 14. You can read more about this on the
[permissions page](postgres-permissions.md).

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

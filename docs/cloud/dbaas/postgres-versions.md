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
them are focused on serverside performance, logging, and more advanced and specific SQL features.
However, PostgreSQL 15 brought a very specific change to default permissions, which affects how
Pukki manages users and their access rights.

### Differences in how Pukki manages database access

In PostgreSQL 14, the default privileges granted to database users allowed them to create new
tables in any database's public schema on that database instance. PostgreSQL 15 revoked the
`create` permission from all database users (except a database owner) from the public schema,
which is used as the default schema. Now new users need to be explicitly given the `create`
permission to a schema, usually the database's default `public` schema.

In a nutshell, when revoking or granting a user access to a PostgreSQL 14 database in Pukki, the
query modifying permissions looks something like this:

```sql
GRANT|REVOKE ALL ON DATABASE ${DATABASE} TO|FROM ${USER};
```

On a PostgreSQL 17 database instance, the same web GUI or CLI-tool commands would result in this
kind of a permissions-modifying query:

```sql
GRANT|REVOKE ALL ON SCHEMA public TO|FROM ${USER};
```

You can always enable root access on a database instance and log in as the root user to modify
permissions more freely.

### Permissions

On PostgreSQL 14 database instances, the default permissions allow all database users to connect
to any database and create tables in the public schema.

On PostgreSQL 17 database instances, you need to explicitly grant users access to a database to
allow them to create tables in the public schema of the specified database. This can be done as
follows with the command line tools.

When creating a new user, you can use the `--database` flag to grant access:
```sh
openstack database user create $INSTNACE_ID $USER_NAME $USER_PASSWORD --database $DATABASE_NAME
```

The command to grant access to an existing database user:
```sh
openstack database user grant access $INSTNACE_ID $USER_NAME $DATABASE_NAME
```

The web interface also allows creating users and modifying their permissions.

To create a new user with database access:
    1. Choose an instance from the Instances page
    2. Go to its Users tab
    3. Press Create User

You can also edit permissions of existing users from the Users tab, by choosing 'Manage Access'
from the dropdown menu in the 'Actions' column.

What Pukki does in the background is basically

### Giving a user read-only access to a table
As the table owner or root user you can do the following SQL command:

```sql
GRANT SELECT ON ${table} TO ${user};
```

### Giving a user read-write access to a table

If you want to give allow users to add, modify, remove and read rows in your database you can give the
user following permissions:

```sql
GRANT SELECT, INSERT, UPDATE, DELETE ON ${table} TO ${user};
```

## Parameters that users can modify

The DBaaS allows users to modify some of the parameters.
If there are some parameters that you think you should be able to modify, [please contact us](../../support/contact.md) and we'll see if we can make it possible.
By default, we assume that default parameters are sane and that users should not, under normal circumstances, modify any of these parameters.

| Parameters           | Default | Requires restart | Comments |
|:--- |:---:|:---|:---|
| maintenance_work_mem | 64MB  | No  | |
| max_connections      | 100   | Yes |It is usually recommended to use connection pools instead of modifying this value |
| work_mem             | 4MB   | No  | |
| log_statement        | false | No  | This is useful if you want to figure out more how your database is utilized |
| log_statement_stats  | false | No  |This will also collect stats from your database, this is recommended to keep as false since it might affect performance |

## A note about privileges

If you have little or no prior experience with PostgreSQL, we recommend familiarizing yourself with how privileges in PSQL interact with Databases, Schema, and Tables. [Here's one tutorial that might be of use.](https://www.postgresqltutorial.com/postgresql-administration/postgresql-schema/)

To avoid confusion, keep in mind that in PostgreSQL 14 the default privileges allow every user to connect to any database and create tables in the default 'public' schema. They cannot access existing tables or other schema without explicit permission, however, and they cannot create new schema.

Typically the owner of an object in PSQL (an object can be a database, a schema, a table, etc. etc.) is the only one with any privileges regarding it, unless otherwise specified. This, combined with privileges not flowing 'downwards' in the hierarchy, can lead to some confusion. Having privileges to a schema doesn't imply any privileges to the tables contained within. For further reading, [here's the official docs on privileges.](https://www.postgresql.org/docs/14/ddl-priv.html)

### Example usage of privileges

These queries would allow the example_user to select data from the example_table. Note that the two queries are identical, as long as the search path hasn't been modified.

```
GRANT SELECT ON example_table TO example_user;
GRANT SELECT ON public.example_table TO example_user;
```

Keep in mind example_user here means a role, which can also be a group. These queries would create a new group, assign a user to it, and grant privileges to select data from all tables in the public schema.

```
CREATE ROLE example_group;
GRANT example_group TO example_user;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO example_group;
```

For easier management of privileges, we recommend creating groups and assigning users to relevant ones instead of tweaking rights on a per-user basis.




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

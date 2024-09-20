# PostgreSQL

Currently Pukki provides two major versions of PostgreSQL 14 and 17. If you are creating a new
database you should always strive to use the latest version. Be aware that if major versions of
PostgreSQL are only supported for about 5 years and if you are planning on using your database
longer than that you will need to do a major version upgrade. 14 end of life is November 2026
and 17 is November 2029. Major versions are often easy to do in Pukki but require a bit of downtime
but sometimes it might be a big challenge so you need to make sure that you start thinking about
upgrading well in advance.

## PostgreSQL versions

### Main changes between 14 and 17

When comparing differences between PostgreSQL 14 and 17 the main source of information is the
[PostgreSQL documentation](https://www.postgresql.org/docs/release/) for most users they won't
notice a difference but it is very important to read the documentation if short downtime
is important to you or you know that you are using more advanced features than the most basic SQL
commands.

### Difference how Pukki manage PostgreSQL 14 and 17

The role permissions for the public schema work differently between 14 and 17. This means that
in PostgreSQL 14 all database users could create new tables in any database. This changes in
PostgreSQL 17, now when you create a new user you need to specify in "database access" in which
database's public schema the users is allowed to create new tables. In short in PostgreSQL 17
users need to explicitly allowed to create new tables where in PostgreSQL 14 users where allowed by
default to create new tables.

### Upgrading between minor PostgreSQL versions

It is usually very easy and quick to upgrade between minor versions of PostgreSQL. Since the process
in the background is shutdown PostgreSQL remove the old PostgreSQL and install the new PostgreSQL.

Usually the upgrade takes only a couple of minutes. When you do major upgrade you can usually just
upgrade to the latest minor version, it is okay to jump over minor versions in between.
There is seldom a reason to use an older minor version even if it usually possible to downgrade.

### Upgrading between major PostgreSQL versions

Major upgrade might feel very similar to minor version upgrades for small database but in the
background there is a lot more going on, and there is a lot bigger risks for errors. There is a
real risk for data loss so you need to be prepared for creating a new database from backup.

Before upgrading your main database it is a must to test the upgrade on another database that you
have created from backup. The nice thing with doing upgrades in Pukki is that it is really easy to
test them multiple times. You can also test have the volume size and flavor size affects the time
it takes to do the upgrade. If you have too little disk space the upgrade might fail so you might
need to increase the disk space before doing the upgrade. If you think your upgrades takes to long
while testing it might be a good idea to test using a bigger flavor as well.

Once you have done a major upgrade you can no longer do a downgrade, the only way to do a downgrade
is restoring from an old backup.


## PostgreSQL permissions
### Allow users to create tables
(In PostgreSQL 14 all user are by default allowed to create new tables)

In PostgreSQL 17 you need to specify in which database (public schema) users are allowed to create
tables.

This can be done with the command line. When creating a new user by:

```sh
openstack database user create $INSTNACE_ID $USER_NAME $USER_PASSWORD --database $DATABASE_NAME
```

You can also add permissions after the user have been create by modify the users permissions:

```sh
openstack database user grant access $INSTNACE_ID $USER_NAME $DATABASE_NAME
```

The same thing can also be done from the web interface by creating a new user:

Choose instance -> User tab -> Create user

You can also edit existing user

Choose instance -> User tab -> Choose a user and in the pull down in the Action column choose
Manage Access -> Grant or Revoke access from databases.


What Pukki does in the background is basically this:
```sql
'GRANT ALL ON SCHEMA "public" TO "${user}";
```


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



### Granting permissions to database in PostgreSQL 14
<!-- TODO is this needed --->
In PostgreSQL 14 you seldom need to give "database access to users but if you choose to do that
what you actually are doing on the background is giving the user permissions to create new
schema.

grant access affects the database

```sql
GRANT ALL ON DATABASE "${database}" TO "${user}";
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

You can use the `openstack database user grant access` command to grant users all permissions on a specified database, which allows them to create their own schema. They still can't access schema and tables in them that are owned by other users without being given privileges, however. Typically the owner of an object in PSQL 14 (which can be a database, a schema, a table, etc. etc.) is the only one with any privileges regarding it, unless otherwise specified. This, combined with privileges not flowing 'downwards' in the hierarchy, can lead to some confusion. Having privileges to a schema doesn't imply any privileges to the tables contained within. For further reading, [here's the official docs on privileges.](https://www.postgresql.org/docs/14/ddl-priv.html)

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

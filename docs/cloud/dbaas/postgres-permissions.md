# PostgreSQL permissions

On PostgreSQL database instances, you need to explicitly grant users access to a database
to allow them to connect to it and to create tables in its public schema.

When creating a new user, you can use the `--database` flag to accomplish this:
```sh
openstack database user create $INSTANCE_ID $USER_NAME $USER_PASSWORD --database $DATABASE_NAME
```

To grant a user access to an existing database, you can use the following command:
```sh
openstack database user grant access $INSTANCE_ID $USER_NAME $DATABASE_NAME
```

The web interface also allows creating users and modifying their permissions.

To create a new user with database access:

  1. Choose an instance from the Instances page
  2. Go to its Users tab
  3. Press Create User

You can also edit permissions of existing users from the Users tab, by choosing 'Manage Access'
from the drop down menu in the 'Actions' column.

### Giving a user read-only access to a table
As the table owner or root user you can do the following SQL command:

```sql
GRANT SELECT ON ${table} TO ${user};
```

### Giving a user read-write access to a table

If you want to allow users to add, modify, remove and read rows in your database you can give the
user following permissions:

```sql
GRANT SELECT, INSERT, UPDATE, DELETE ON ${table} TO ${user};
```

### For database instances created before 2026-11-23

By default, PostgreSQL allows the `PUBLIC` role to connect to any database on the server, though it's
restricted from creating, reading, or modifying any schemas or tables. Pukki's PostgreSQL instances
kept this behaviour until an update on 2026-11-23.

Old database instances that have not been rebuilt after this date continue to allow the `PUBLIC`
role to connect to newly created databases. On newly created instances, however, or older instances
that have been rebuilt, the following additional query is executed when creating a new database:
```
REVOKE CONNECT ON DATABASE $new_database FROM PUBLIC'
```

### Databases created on PostgreSQL 14 have different default permissions

In PostgreSQL 14, the default privileges granted to database users allowed them to create new
tables in any database's public schema on that database instance. PostgreSQL 15 revoked the
`create` permission from all database users (except a database owner) from the public schema,
which is used as the default schema.

If your Pukki database instance was originally using PostgreSQL 14, databases created on the instance
before the upgrade to PostgreSQL 17 might allow users with the `PUBLIC` role to connect to and create
tables in the public schema. They still cannot modify or read tables created by other users without
being granted access through the usual means, however.

## A note about privileges

If you have little or no prior experience with PostgreSQL, we recommend familiarizing yourself with how privileges in PSQL interact with Databases, Schema, and Tables. [Here's one tutorial that might be of use.](https://www.postgresqltutorial.com/postgresql-administration/postgresql-schema/)

Typically the owner of an object in PSQL (an object can be a database, a schema, a table, etc. etc.) is the only one with any privileges regarding it, unless otherwise specified. This, combined with privileges not flowing 'downwards' in the hierarchy, can lead to some confusion. Having privileges to a schema doesn't imply any privileges to the tables contained within. For further reading, [here's the official docs on privileges.](https://www.postgresql.org/docs/17/ddl-priv.html)

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

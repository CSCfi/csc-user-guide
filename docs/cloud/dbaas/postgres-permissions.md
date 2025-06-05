# PostgreSQL permissions

## PostgreSQL 17 permissions

In PostgreSQL 17 database instances, you need to explicitly grant users access to a database to
allow them to create tables in the public schema of the specified database. This can be done as
follows with the command line tools.

When creating a new user, you can use the `--database` flag to grant user access to create new
table in the public schema in a specific database:

```sh
openstack database user create $INSTANCE_ID $USER_NAME $USER_PASSWORD --database $DATABASE_NAME
```

The command to grant permissions for a user to create tables to an existing database user:
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

What Pukki does in the background is basically

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


## Changes between PostgreSQL 14 and 17

PostgreSQL 15 brought a very specific change to default permissions, which affects how Pukki
manages users and their access rights.

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


## A note about privileges

If you have little or no prior experience with PostgreSQL, we recommend familiarizing yourself with how privileges in PSQL interact with Databases, Schema, and Tables. [Here's one tutorial that might be of use.](https://www.postgresqltutorial.com/postgresql-administration/postgresql-schema/)

To avoid confusion, keep in mind that in PostgreSQL 14 the default privileges allow every user to connect to any database and create tables in the default 'public' schema. They cannot access existing tables or other schema without explicit permission, however, they cannot create new schema.

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


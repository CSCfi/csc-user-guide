# PostgreSQL

- TODO Some changes between versions
- There are selldom a reason to use an older database version than the newest when creating a new database
- Upgrading between minor versions are usually pretty easy but there is always some risks involved.
- Upgrading a major version are a bit more tricky and it is recommended that you try to test the upgrade
  by upgrading a database instance created from backup before you upgrade your main database.



## PostgreSQL roles and users

Pukki tries to use be as similar as upstream.

Some mention of schemas with link about more information, also mention that our documentation always
assumes that you are using the public schemas and that will probably be suitable for over 90 procents  of the users

Also mention table owner can give permissions also the root user can give permissions some many
people get confused by how the privilages works.

## Giving a user read-only access to a table

## Giving a user read-write access to a table


## Pukki granting permissions to database in PostgreSQL 17

### Giving users permissions to create tables in a database in PostgreSQL 17
"the public schema in the database"

grant access affects schema which means that the users with database access can create tables.

```sql
'GRANT ALL ON SCHEMA "public" TO "${user}";
```




## Pukki granting permissions to database  in PostgreSQL 14

grant permisisons to create schemas in the database"


grant access affects the database 

```sql
GRANT ALL ON DATABASE "${database}" TO "${user}";
```

### Revoking a user to create



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

If you have little or no prior experience with PostgreSQL, we recommend familiarizing yourself with how privileges in PSQL interact with Databases, Schemas, and Tables. [Here's one tutorial that might be of use.](https://www.postgresqltutorial.com/postgresql-administration/postgresql-schema/)

To avoid confusion, keep in mind that in PostgreSQL 14 the default privileges allow every user to connect to any database and create tables in the default 'public' schema. They cannot access existing tables or other schemas without explicit permission, however, and they cannot create new schemas.

You can use the `openstack database user grant access` command to grant users all permissions on a specified database, which allows them to create their own schemas. They still can't access schemas and tables in them that are owned by other users without being given privileges, however. Typically the owner of an object in PSQL 14 (which can be a database, a schema, a table, etc. etc.) is the only one with any privileges regarding it, unless otherwise specified. This, combined with privileges not flowing 'downwards' in the hierarchy, can lead to some confusion. Having privileges to a schema doesn't imply any privileges to the tables contained within. For further reading, [here's the official docs on privileges.](https://www.postgresql.org/docs/14/ddl-priv.html)

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

### Import database dump TODO

If you have a database dump, you can import it with the following command. Be aware that this might overwrite what you already have in the database:

```bash
psql -h $FLOATING_IP -d $DATABASE -U USERNAME -f file.sql
```

# Database operations

## Keeping your database up to date

The DBaaS service provides tools for you to upgrade your database yourself. Before you do an upgrade you need to be aware of the risks and implications. Upgrading the database will cause a short downtime. The downtime might depend on the version upgrade and how large database you have. It is a good idea to test the upgrade first by creating a new database instance from a backup and upgrade the new database instance first, or just continue using the new database instance. This allows you to better understand the implications.

When you do a database upgrade,

1. Your database instance will pull the new database version.
2. Your database instance will stop your database.
3. Your database instance will start the new database version.

At the moment it is not possible to upgrade a database instance from the web interface, you must use the CLI-tool.

The commands to use:

1. Figure out which database you want to upgrade, take note of the `Datastore` and `Datastore Version`:

    ```
    openstack database instance list
    ```

2. With your preferred tool make sure that your database is working as expected. Take note on what command you used so that you can use the same command/process to verify that everything works after the upgrade.
3. Find out what datastore versions are available:

    ```
    openstack datastore version list $Datastore
    ```

4. You most likely want to choose the latest version:

    ```
    openstack database instance upgrade $Instance $Datastore_version
    ```

5. Verify with your preferred tool that your database is working as expected.

## Deleting a database in your database instance

By default, your database user account does not have permissions to delete databases. If you want to delete a database in your database instance you need to use the web-GUI or the OpenStack CLI:

```
openstack database db delete $INSTANCE_UUID $DATABASE_NAME
```

If you want to allow your database users too be able to manage the databases of your database instance you will need to enable root permissions for your instance:

```
openstack database root enable $INSTANCE_UUID
```

Then create a user with your `root` account that have suitable permission (in PostgreSQL the permission is `CREATEDB`). Once you are done you can disable your root user:

```
openstack database root disable $INSTANCE_UUID
```

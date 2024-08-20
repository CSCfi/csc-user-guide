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


## Enable root

Sometimes you need to make changes to the database that is not supported from the web interface nor
the openstack command line tool, like creating extensions or make more advanced user permissions.
It is worth keeping in mind that with the root credentials you can make changes that might break
your database, it is recommended to use the root user only when you need to make changes that
actually require the user.

### How to enable root from the Web interface

1. Log into the web interface where you can see all your existing instances.
2. From the instances row you can find the action column on the right hand side choose `Manage Root Access` ![Manage root access](../../img/dbaas-enable-root.png)
3. Once you are at the root view you can press the `Enable root` button.
4. The root password is now visible and you can now access the your database with the psql-client, with the root password with the user name `root` .
5. Once you don't need root access anymore you can press `Disable root`.

### How to enable root from the CLI


1. Enable root
    ```
    openstack database root enable $INSTANCE_ID
    ```
2. The root password is now visible and you can now access the your database with the psql-client, with the root password with the user name `root` .

3. Once you don't need to access your database with root anymore you can disable it by:

    ```
    openstack database root disable $INSTANCE_ID
    ```

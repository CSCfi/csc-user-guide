# Database operations

## Minor version database upgrades

Pukki DBaaS provides tools for you to upgrade your database yourself. Before you do an upgrade you need to be aware of the risks and implications. Upgrading the database will cause a short downtime, the length of which depends on the datastore versions involved and the size of the database. It's advisable to create a new database instance from a recent backup to test the upgrade on first.

When you do a minor database upgrade,

1. Your database instance will pull the new database version.
2. Your database instance will stop your database.
3. Your database instance will start the new database version.

The commands to use:

1. Figure out which database you want to upgrade, take note of the `Datastore` and `Datastore Version`:

    ```
    openstack database instance list
    ```

2. With your preferred tool make sure that your database is working as expected. Take note of what command you used so that you can use the same command/process to verify that everything works after the upgrade.
3. Find out what datastore versions are available:

    ```
    openstack datastore version list $Datastore
    ```

4. You most likely want to choose the latest version:

    ```
    openstack database instance upgrade $Instance $Datastore_version
    ```

5. Verify with your preferred tool that your database is working as expected.

!!! warning "Certain PostgreSQL upgrades will cause databases to be reindexed"
    The libraries used by PostgreSQL internally for collation (sorting, comparing, and ordering data) might change between datastore versions.
    When this happens, a full reindex of all databases is required to prevent issues with data consistency.
    This reindexing can take a considerable amount of time, especially with large databases containing complex indexes.
    Currently upgrading from 17.5 or earlier to 17.6 or newer triggers the reindexing. Upgrading between
    minor versions of PostgreSQL 14 also triggers the reindexing, as does upgrading from major version 14 to 17.
    Please plan your database upgrades accordingly.

## Major database upgrades

Major version upgrades are no different from the user's point of view, but there's a bit more happening in the background, which creates more possible points of failure.

Things that you need to take into account when doing a major database version upgrade:
1. You have a recent enough backup that you can use if the upgrade fails.
2. You have tested doing the upgrade on a database instance restored from a backup.
3. You have reserved plenty of time for the upgrade.
4. You have considered if you'd benefit from using a larger instance flavor while upgrading.
5. You have checked that your database instance has enough free disk space before starting the upgrade - we recommend having around twice as much free space as is being used.

We recommend creating a new database instance from a recent backup and upgrading that instance to the desired database version, as you can then switch over to using the new database instance with the new database version at your leisure after making sure no problems cropped up. Drawbacks include having to switch to using a new IP address to connect to the database, though, and any changes made to the original database after the backup was taken will be lost.

## Deleting a database in your database instance

By default, your database user account does not have permissions to delete databases. If you want to delete a database in your database instance you need to use the web-GUI or the OpenStack CLI:

```
openstack database db delete $INSTANCE_UUID $DATABASE_NAME
```


## Enable root

Some changes, such as enabling extensions or modifying more advanced user permissions,
aren't accessible via the web interface or the OpenStack command line tools.
It's worth keeping in mind that with the root credentials enabled you can make
breaking changes to your database. It's recommended to only use the root user when
you need to make changes that actually require it.

Keep in mind that when you create a new database instance by restoring from a backup,
any parameter changes done with root access via `ALTER SYSTEM` commands in the original
instance are discarded.

### How to enable root from the Web interface

1. Log in to the web interface where you can see all your existing instances.
2. Find the 'Actions' dropdown in the rightmost column, and choose `Manage Root Access`. ![Manage root access](../../img/dbaas-enable-root.png)
3. On the Manage Root Access page, press the `Enable Root` button in the rightmost column of the instances table.
4. The root password is now visible on that same Manage Root Access page. You can access the database with the password shown, and with `root` as username.
5. Once you no longer need root access, press `Disable Root` on the Manage Root Access page.

### How to enable root from the CLI


1. Enable root
    ```
    openstack database root enable $INSTANCE_ID
    ```

2. Use the password shown with the username `root` to access the database.

3. Once you no longer need root access, run the following command to disable it:

    ```
    openstack database root disable $INSTANCE_ID
    ```

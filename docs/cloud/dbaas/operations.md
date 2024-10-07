# Database operations

## Minor version database upgrades

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

## Major database upgrades
Major version database upgrades works from the users point the same way but in the background
happens more stuff, and is therefor more riskily.

Things that you need to take into account when doing a major database version upgrade:
1. You have a recent enough backup that you can use if the upgrade fails.
2. You have tested doing the upgrade on database restored from the backup.
3. You reserve plenty of time for the upgrade.
4. You have considered if you benefit of using a bigger flavor while doing the upgrade.
5. You have ensured that your database have plenty of free disk space before starting the upgrade,
you should aim for you volume be three times bigger than the used size.

An even safer way than upgrading your main database is creating a new database from backup and
upgrade that database and once it is done, you can start using that as your main database. The
drawback of this way is that your IP changes and the latest changes to your old database will not
be added to the new database if you have not blocked all traffic to your old database before
taking the backup.



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

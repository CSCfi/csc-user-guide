# Database operations

## Keeping your database up to date

The DBaaS service provides the tools for you to the database upgrade yourself. Before you do an upgrade you need to be aware of the risks and implications. Upgrading the database will cause a short downtime. The downtime might depend on the version upgrade and how big database you have. It might be a good idea to test the upgrade first from an backup. This allows you to better understand the implications. 

What happens when you do an database upgrade:
1. Your database instance will pull the new database version.
2. Your database instance will stop your database.
3. Your database instance will start the new database version.

At the moment it is not possible to upgrade the database instance from the web interface, you must use the CLI-tool.

The commands to use:


1. Figure out which database you want to upgrade, take note of the `Datastore` and `Datastore Version`

```
openstack database instance list
```

2. With your preferred tool make sure that your database is working as expected. Take note on what command you used so that you can use the same command/process to verify that everything works after the upgrade.

3. Find out what datastore versions are available

```
openstack datastore version list $Datastore
```

4. You most likely want to choose the latest version:

```
openstack database instance upgrade $Instance $Datastore_version
```

5. Verify with your refereed tool that your database is working as expected

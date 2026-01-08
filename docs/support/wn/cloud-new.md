# Cloud services
## New Volume Type available in Pouta: Capacity Volumes, 14.1.2026

We are releasing a new volume type in Pouta: Capacity Volumes. Capacity Volumes are designed for workloads that require large amounts of storage at a lower cost, such as data archiving, backups, and big data applications. Capacity Volumes offer a cost-effective solution for storing large datasets.

You can check this [link](../../cloud/pouta/persistent-storage.md#capacity-volumes) for more information about Capacity Volumes.

## Small changes in Pouta's cloud images creation, 2.12.2025

Since end of November of 2025, newly created Public images in Pouta will create the ephemeral partitions as ext4 instead of vfat. This won't be
an issue for most people but in some cases, you might expect a certain file system format.

## New database minor versions available in Pukki, 25.11.2025

PostgreSQL 17.7 and 14.20 and MariaDB 11.4.8 are now available in Pukki DBaaS. See [PostgreSQL's](https://www.postgresql.org/about/news/postgresql-181-177-1611-1515-1420-and-1323-released-3171/) and [MariaDB's](https://mariadb.com/docs/release-notes/community-server/11.4/11.4.8) documentation for release notes.

## Allas Web UI improvements, 14.11.2025

[Allas-UI](../../data/Allas/using_allas/allas-ui.md) has been updated with several new features that make managing data in Allas easier:

- You can now create empty folders, either using the “New folder” button or by drag-and-dropping an empty directory during upload.
- Bulk deletes are now supported — buckets or subfolders no longer need to be empty before deletion.
- Files uploaded are now saved to the correct folder path instead of always going to the root of the bucket.
- A new "back" button allows you to easily navigate back to the parent folder/bucket when browsing your data.

## New Pouta VM launcher

We deployed a new VM launcher when creating a VM on Pouta. Our [documentation](../../cloud/pouta/launch-vm-from-web-gui.md#launching-a-virtual-machine) has been updated accordingly. Take a look at it!

## Application credentials got more features in Pouta 7.7.2025

Fine grained Access Rules are now supported on Pouta Application credentials. This allows to create very granular credentials that only allow very specific actions. You can visit the [Application Credentials](../../cloud/pouta/application-credentials.md) article to start improving your security when interacting with Pouta's API.

## Pukki now supports MariaDB, 7.1.2025
Pukki now supports MariaDB as well as PostgreSQL. The MariaDB version we support in Pukki is
MariaDB 11.4. More information can be found in the
[Pukki MariaDB documentation](../../cloud/dbaas/mariadb.md)


## Pukki now supports PostgreSQL 17, 9.10.2024
The default database in Pukki is now PostgreSQL 17 instead of the previous PostgreSQL 14. You can
still use PostgreSQL 14 but we recommend that if you are creating a new database you start using
PostgreSQL 17. More information can be found in the
[Pukki PostgreSQL documentation](../../cloud/dbaas/postgresql.md)


## Pukki DBaaS now supports PostGIS extensions, 28.08.2024
It is now possible to enable PostGIS extensions in the new PostgreSQL 14.13 databases.
[PostgreSQL documentation](../../cloud/dbaas/postgresql.md)

## CSC Notebooks service renamed as Noppe, 21.8.2024

CSC Notebooks service has been renamed as Noppe.
[Noppe](https://noppe.csc.fi) offers web applications for self-learning,
hosting courses and collaboration. The applications are accessed through a web
browser and run in CSC cloud.
[Read the documentation for more information](../../cloud/noppe/index.md)!

## Pukki DBaaS now available for all users, 28.3.2024

[Pukki](../../cloud/dbaas/index.md) is a Database as a Service (DBaaS),
suitable for most database use cases. With Pukki you can easily and
effortlessly set up a database with a few clicks and manage it as a
self-service, instead of manually setting up and maintaining your own database
environment.

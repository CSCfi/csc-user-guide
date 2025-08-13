# Cloud services

## Pukki DBaaS replaces Kaivos database service, 13.8.2025

Kaivos database service (kaivos.csc.fi) will shut down on XX.XX.202X. We
recommend taking [Pukki DBaaS](../../cloud/dbaas/index.md) into use if
you need to run SQL databases at CSC.

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

# PostgreSQL

This documentation provides some hints how to use PostgreSQL as well as some information that might
be important when you are trying to do a little bit more advanced stuff in Pukki than the basics.

!!! warning "PostgreSQL 14 is approaching its end-of-life date"

    As PostgreSQL 14's end-of-life date is set to arrive on 12th of November, 2026, support for it will be removed from Pukki by then. Users are recommended to upgrade their PostgreSQL 14 instances to PostgreSQL 17 before the EOL date, as restoring database instances from PostgreSQL 14 backups will stop working.

  * [How to access your PostgreSQL database](postgres-accessing.md)
  * [How to work with extensions](postgres-extensions.md) This documentation is interesting to you if
you want to use extensions for example PostGIS.
  * [How to create database users and modify user permissions](postgres-permissions.md)
  * [PostgreSQL versions](postgres-versions.md) What kind of changes there are between the major
versions that are supported in Pukki. This documentation is important if you are planning to
do a major version upgrade.
  * [How to migrate a PostgreSQL database to Pukki](../../support/tutorials/pukki_data_migration.md)


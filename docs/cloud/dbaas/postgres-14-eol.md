# PostgreSQL 14 end-of-life in Pukki

As PostgreSQL 14's end-of-life date is set to arrive on 12th of November, 2026, support for it will be removed from Pukki by then.

## What will happen and when?

On the end-of-life date, 2026-11-12:

* PostgreSQL 14 will be disabled and cannot be used for new database instances
    * This also means backups created from PostgreSQL 14 instances cannot be restored as new instances
* Pukki admins will start upgrading remaining PostgreSQL 14 instances to PostgreSQL 17

## What actions should I take?

Our recommendation is for users with PostgreSQL 14 instances to upgrade them to PostgreSQL 17 well before the end-of-life date. This way you have control over the resulting downtime, and can make sure everything that depends on the database continues to function as before. Instructions for performing the upgrade can be found below this paragraph or on the [database operations page here](operations.md), and some information regarding PostgreSQL versions on the [PostgreSQL versions page here](postgres-versions.md).

> Our recommended procedure for major version upgrades:

> 0. Reserve plenty of time for the upgrade process and familiarize yourself with any changes between the database versions
> 1. Create a new backup of the database instance (or use the most recent automatic backup)
> 2. Restore the freshly created backup into a new database instance
> 3. Upgrade the new database instance to your target datastore version (we recommend using the most recent version available)
> 4. Test that connections to the new instance work as expected and that your data looks correct

> After this, you can either move to use the new instance and delete the original one, or continue with
> upgrading the original instance and deleting the new one.
> Drawbacks with changing to the new instance include having to switch to use the new IP address
> for connections, and any changes made to the original database instance after the backup was taken
> will be lost.

 Any PostgreSQL 14 instances not upgraded to 17 by the end-of-life date will be upgraded by Pukki admins. This will result in some unscheduled downtime for the database instance, and we have no way of checking that any database connections recover afterwards.

## About email reminders

We are planning on sending monthly email reminders to users with PostgreSQL 14 instances. They will mostly repeat information found on this page. As soon as you have no instances remaining using PostgreSQL 14, you will no longer receive the reminders.

Additionally, email notifications will be sent to users with instances that were upgraded to PostgreSQL 17 by admins after the end-of-life date.

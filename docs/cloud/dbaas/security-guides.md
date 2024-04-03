# Security guidelines for DBaaS

## Firewalls

All database instances have their own firewalls. Users are responsible for making sure that the firewall rules are strict. The firewall rules should only be open to those IP-addresses that is needed. Relaxed firewall rules are probably some of the largest security risks and you need to take it seriously. Even if you don't have any "secret" data in your database, you are not allowed to have it open to the world. If you want to share your data, you should do it through a proxy or other services that might use the database as a backend. Leaving a database port open on the internet is an sure-fire way to attract malicious actors to target your database.

You can find out more about how to use firewalls in the [Firewall section](firewalls.md)

## Authentication

You can log in to the DBaaS service with many different authentication methods as long as you have a [CSC account](../../../accounts/how-to-create-new-user-account/) and belong to a project that has applied for DBaaS access.

From the web interface, you can create application credentials if you like to automate your database management from another application.

You can not use your CSC account to authenticate to your databases. The databases require their own username and password that you can manage when you create a new database instance. You can also add, remove and modify the database user accounts after the database creation. It is important that you create strong passwords for your database accounts.

## Database security

All database instances are running in their dedicated virtual machines. The reason for this is to minimize the risks careless users pose on other users that take their security seriously.

The DBaaS admins are allowed to shutdown, lock, or firewall database instances that are suspected to be used maliciously, as well as disable user access to the service.

## Backups

Backups are taken automatically once a day. Users are not allowed to delete their own backups.
Backups are deleted automatically after 90 days. Backups are stored encrypted in Allas. Therefore, if
you want to store additional backups of your database it is advised to use other services than
Allas and cPouta. [More information about backups can be found in the backups section](backups.md).

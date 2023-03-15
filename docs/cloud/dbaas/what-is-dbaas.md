## What is DBaaS
!!! error "Closed Beta"
    Pukki DBaaS is in closed beta. This means that services is probably not suitable for most users
    and there might be breaking changes. If you are still interested in using the service you can
    contact service-desk to see if the service would be suitable for you.

Database as a Service (DBaaS) is a self service on-demand database service, this means that you can launch a new database "at a push of a button". The goal with the DBaaS is to automate away the database maintenance and administrative tasks of other services so that the  developers/administrators can focus on the stuff that actually brings "value" to the services.

Instead of manually setting up your own database that you have to maintain yourself you can use DBaaS to manage the tedious tasks of provisioning, configure, maintaining, updating, documenting  and backing up your database.

The DBaaS service is based on Openstack. DBaaS services is running on top of cPouta this means that any issue that affects cPouta might also affect DBaaS.

Each database instances is running in its own virtual machine, this means that all database instances are segregate from each other through virtualization. All database instances also have their own public IP that is accessible over the internet and its own firewall configuration, that the user can define. It's the users responsibility to make sure that their database instances have strict firewalls and following good password policies.
DBaaS is a generic database service, this means that it should be suitable for most use cases. Where the added value of a DBaaS service is the greatest are for homepages, small services, research projects, developing projects.  The DBaaS is not "database-admin as a services" this means that the DBaaS does not provide support for how to optimize your database queries or how to structure your database.

# What is DBaaS

!!! error "Closed Beta"
    Pukki DBaaS is in closed beta. This means that the service is probably not suitable for most users
    and there might be breaking changes. If you are still interested in using the service you can
    [contact us](../../support/contact.md) to see if the service would be suitable for you.

Database as a Service (DBaaS) is a self service on-demand database service, that means you can launch a new database "with a simple click". The goal of the DBaaS is to automate away the database maintenance and administrative tasks of other services so that the developers/administrators can focus on the stuff that actually brings "value" to the services.

Instead of manually setting up your own database that you have to maintain yourself, you can use DBaaS to manage the tedious tasks of provisioning, configuring, maintaining, updating, documenting and backing up your database.

The DBaaS service is based on OpenStack. DBaaS service is running on top of cPouta, which means any issue that affects cPouta might also affect DBaaS.

Each database instance is running in its own virtual machine, which means that all database instances are segregated from each other through virtualization. All database instances also have their own public IP that is accessible over the internet and its own firewall configuration that the user can define. It is the users responsibility to make sure that their database instances have strict firewall rules and following good password policies.

DBaaS is a generic database service, which means that it should be suitable for most use cases. The added value of a DBaaS service is the greatest for homepages, small services, research projects and development projects. The DBaaS is not "database-admin as a service", which means the DBaaS does not provide support, whether how to optimize your database queries or how to structure your database.

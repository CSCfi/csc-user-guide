## What is DBaaS

DBaaS is a self service on-deman database. The goal with the services is to automate away the datbase maintance and administrative tasks so that services developeres/administrators can foucs on the stuff that acutally brings "value" to the services.

Instead of manually setting up a databse in a virtualmachine that you have to maintain yourself you can use DBaaS to manage the tidious tasks of provisioning, configure, maintaining, updating and backing up your database.

The DBaaS service is based on OpenStack. DBaaS services is running on top of cPouta this means that any issue that affects cPouta might also affect DBaaS.

Each database instances is running in its own virtual machine, this means that all database instances is segregate from each other through virtualisation. All database instances also have their own public IP that is accessable from the internet and its own firewall configuration, that the user can define. It's the users responsibility to make sure that their database instances have strict firewalls and good username and passwords.
DBaaS is a generic database service, this means that it should be suitable for most use cases. Where the added value of a DBaaS service is the greatest is for homepages, small services, research projects, developing projects. The DBaaS is not database-admin as a services this means that the DBaaS does not provide support for how to optimise your database queries or how to structure your database.

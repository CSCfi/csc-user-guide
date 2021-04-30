# I need a Database, where can I deploy it?

If you need a Database that needs to be accesible from other systems (like Puhti or Mahti), the best option is to deploy it in the cPouta cloud. You can request a Virtual machine and then just follow the instructions provided by the database of your choice. Then you just need to use security groups to give network access to your database.

!!! Warning
    Pay special attention to when using the [security groups](/cloud/pouta/launch-vm-from-web-gui/#firewalls-and-security-groups) to open only the necessary port(s) to the necessary IP(s).

## When is Rahti a good place to deploy a Database?

Rahti is a good choice only if the application that needs to connect to the database is already deployed in Rahti. Rahti only accepts network connections from outside Rahti using the HTTP(s) protocol in ports 80 and 443.

## Do you need a MySQL/MariaDB database?

You could also consider the [Kaivos Database service](../..//data/kaivos/overview.md) hosted by CSC,
which provides the server where you can apply for an account and an empty database will be 
available for you. This way you don't need to manage the virtual machine.


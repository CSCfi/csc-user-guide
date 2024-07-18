# I need a Database, where can I deploy it?

If you need a Database that needs to be accessible from other systems (like
Puhti or Mahti), the best and easiest option is the
[Pukki DBaaS service](../../cloud/dbaas/index.md), which currently supports
PostgreSQL databases. Other types are under consideration.

If you need another type of database, you may deploy it yourself in
[cPouta cloud](../../cloud/pouta/index.md). In this case, you should request a
virtual machine and then just follow the instructions provided by the database
of your choice. Use security groups to give network access to your database.

!!! warning "Important"
    When using
    [security groups](/cloud/pouta/launch-vm-from-web-gui/#firewalls-and-security-groups),
    pay special attention to open only the necessary port(s) to the necessary
    IP(s).

## When is Rahti a good place to deploy a Database?

Rahti is a good choice if the application that needs to connect to the database
is already deployed in Rahti. Rahti only accepts network connections from
outside Rahti using the HTTP(s) protocol in ports 80 and 443.

One way to connect to Rahti from CSC supercomputers is to establish a TCP
tunnel over an HTTP-compatible WebSocket connection. See
[Accessing databases on Rahti from CSC supercomputers](../../cloud/tutorials/connect-database-hpc.md)
for more details about this workaround.

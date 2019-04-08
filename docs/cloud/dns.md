## DNS services in cPouta

cPouta does not currently offer integrated nameservice management.

All our floating IPs are mapped to a default hostname, for example

    vm0120.kaj.pouta.csc.fi

To use  your own DNS name  for your virtual machine,  simply configure
your own DNS server  to point the domain name to  the floating IP that
the virtual machine is using.

For most services these forward  DNS records are enough. Some services
also require reverse  DNS lookups to work. This means  that we have to
configure our  DNS server to  say that the  floating IP you  are using
resolves to the domain name your are using.

You can request reverse DNS mappings.

-   Point the DNS name to the server you want.
-   Send  a mail to cloud-support@csc.fi  with the IP /  hostname pair
    you want to  be mapped. Also send the UUID  on the virtual machine
    it  should be  mapped to.  You do  not need  to send  mail if  the
    floating IP  is moved to  another machine,  as long as  the domain
    info for the floating IP still is correct.
-     When  you   no   longer  need   the   mapping,  please   contact
    cloud-support@csc.fi so we can remove the reverse DNS entry.

We reserve  the right to  clean up old  reverse DNS records  where the
forward DNS  records do  not match  anymore. We  will also  remove the
reverse records when closing the project.

# Using Firewalls in Pukki

All database instances have their own firewalls. Users are responsible for making sure that the firewall rules are strict. The firewall rules should only be open to those IP-addresses that is needed. Relaxed firewall rules are probably some of the largest security risks and you need to take it seriously. Even if you don't have any "secret" data in your database, you are not allowed to have it open to the world. If you want to share your data, you should do it through a proxy or other services that might use the database as a backend. Leaving a database port open on the internet is an sure-fire way to attract malicious actors to target your database.

## How to manage firewalls

You can change the firewalls from the [web interface](https://pukki.dbaas.csc.fi) on existing
instances by pressing the "Update Instance".

With the [openstack CLI](cli.md) tool you can use the `opsenstack database instance update --help` command.
Note that the command override the existing firewalls rules which means that you need to set all
the firewall opening each time you update the firewalls for an instance with `--allowed-cidr` flag.

## Single IP or subnet

By adding the "CIDR notion" `/32` to the end of an IP like `192.168.0.1/32` it means that you only
allow that specific IP.

It is also possible to allow a subnet for example `/24` if you want to allow a whole network e.g.
your office network. The smallest mask that is allowed is `/22` that is 1024 IP addresses.
Pukki does not allow `0.0.0.0/0` since it would be too easy to set this value and forget that your
database instance is accessible from the whole internet.

## Firewall openings from other CSC-services

To be able to access your database from other CSC services you need to allow some ingress traffic.
This is done by allowing subnets.

### cPouta

* If your server from where you want to connect to your database instances have a "floating IP"
(public IP) you want to allow that IP in Pukki.
* If your server does not have a floating IP you need to allow the routers "External Fixed IPs".
You can find the IP from the Pouta web interface under Network -> Routers -> The specific router ->
"External Fixed IPs"


### ePouta

It is important to remember that all traffic from ePouta to Pukki will be going over "the internet"
which might be in conflict with why you have chosen to use ePouta in first place.

1. If you still want to allow access to Pukki. You must ensure that your home organization firewalls
will allow traffic to your database instance in Pukki.
2. If you are using a "public IP range" in ePouta then you can just update your database instance
with the new IP address with the "CIDR notation" (suffix) `/32`.

### Rahti

Rahti is using a `86.50.229.150/32` as a shared outgoing IP address. Note that if you are using
Rahti with the shared outgoing IP-address all other Rahti customers can access to your database
which makes it even more important to use a strong username and password for your database.

More information can be found in [Rahti security guide](../rahti2/security-guide.md)



### Noppe
If you need to access your Pukki database instance from Noppe then you need to allow this IP
`193.167.189.137/32` . Note that all other Notebook users will be able to access your database
instances as well so it is important to use strong passwords for your database user.

### Puhti

Accessing your Pukki database from login and compute nodes you can allow this:

```
86.50.164.176/28
```

<!--
If one would like to have even strictre rules one could limit it only these
puhti-nat-[1,2].csc.fi and puhti-login[11-15].csc.fi
-->

### Mahti

Accessing your Pukki database from Mahti from both login nodes and compute node you can allow this:

```
86.50.165.192/27
```

<!--
Some alternatives:
86.50.165.192/27
86.50.165.200/30 + 86.50.165.208/28
86.50.165.200/30 + 86.50.165.208/29 + 86.50.165.216/32
86.50.165.200/30 + 86.50.165.211/32 + 86.50.165.212/30 + 86.50.165.216/32
-->
### LUMI

Accessing your Pukki database from LUMI you need to allow the follow CIDR:

```
193.167.209.160/28
```

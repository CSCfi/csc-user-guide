# Additional services

This article gives two examples on how to access some additional supporting services
in Pouta. These services are not strictly part of cPouta, but they provide extra
functionality to make the service more useful.

[TOC]

## Sending e-mail from cPouta

Sometimes you need to be able to send e-mail from a cPouta virtual
machine. This might be notifications when something happens or
registration confirmation e-mails.

We're now providing a service to do this. The service is still in the
evaluation stages, and we might make changes to the service based on
our experience and any feedback we get.

To use this service, you need to configure your mail transfer agent
(MTA) to use the following SMTP relay server (a.k.a. smarthost):

```
smtp.pouta.csc.fi:25
```

The server does not require authentication.

When sending e-mail, you need a valid _Sender_ address in your e-mails,
such as your university e-mail address, since this will be validated by
the SMTP server. Please note that this is a different e-mail header
attribute from the _From_ attribute.

If you want to set up any services on cPouta that generate a large
amount of SMTP traffic (e.g. public mailing lists), please contact
the CSC Service Desk to coordinate this.

### About Sender Policy Framework (SPF)

You might need to add CSC's SPF record to your own domain existing DNS record, if SPF is already configured in use. 
Even if SPF is not configured, it should be anyway considered because some email domains reject emails from email domains where SPF is not configured.

Please note that taking SPF in use, or just by modifying existing record incorrectly, affects the whole domain email traffic functionality.
Also it's good to understand that you may only add/edit SPF record of a domain for which your organization manages its DNS records.

The part which should be added to SPF record is "include:hosted-at.csc.fi".
Your domain SPF record should look then something like this:
```
domain.of.the.sending.email.address.    IN    TXT    "v=spf1 include:hosted-at.csc.fi ~all"
```

## DNS services in cPouta

cPouta does not currently offer integrated name service management.

All our floating IPs are mapped to a default hostname, for example:

```
vm0120.kaj.pouta.csc.fi
```

To find the hostname of a floating IP, you can use `host` command:
```sh
host -a <floating IP address>
```

And the result is `vmXXXX.kaj.pouta.csc.fi` listed in output:

```
...
;; ANSWER SECTION:
x.x.x.x.in-addr.arpa. xxx IN     PTR     vmXXXX.kaj.pouta.csc.fi.
```

To use your own DNS name for your virtual machine, simply configure
your own DNS server to point the domain name to the floating IP that
the virtual machine is using.

For most services, these forward DNS records are enough. Some services
also require reverse DNS lookups to work. This means that we have to
configure our DNS server to say that the floating IP you are using
resolves to the domain name you are using.

You can request reverse DNS mappings.

- Point the DNS name to the server you want.
- Send a mail to servicedesk@csc.fi with the IP/hostname pair
 you want to be mapped. Also send the UUID on the virtual machine
 it should be mapped to. You do not need to send a mail if the
 floating IP is moved to another machine, as long as the domain
 info for the floating IP still is correct.
- When you no longer need the mapping, please contact
 servicedesk@csc.fi so we can remove the reverse DNS entry.

We reserve the right to clean up old reverse DNS records where the
forward DNS records do not match anymore. We will also remove the
reverse records when closing the project.

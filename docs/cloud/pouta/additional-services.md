# Additional services

This article gives two examples on how to access some additional supporting services
in Pouta. These services are not strictly part of cPouta, but they provide extra
functionality to make the service more useful.

[TOC]

## Sending e-mail from cPouta

Sometimes you need to be able to send e-mail from a cPouta virtual
machine. This might be notifications when something happens or
registration confirmation e-mails.

We're now providing a service to do this. It is provided as-is. The service is still in the
evaluation stages, and we might make changes to the service based on
our experience and any feedback we get.

To use this service, you need to configure your mail transfer agent
(MTA) to use the following SMTP relay server (a.k.a. smarthost):

```
smtp.pouta.csc.fi:25
```

The server does not require authentication.

```python
import smtplib

sender = 'sender@domain.com'
receivers = ['destination@domain.com']

message = """From: SENDER NAME <%s>
To: DESTINATION NAME <%s>
Subject: SMTP e-mail test

This is a test e-mail message.
""" % (sender, receivers[0])

try:
   smtpObj = smtplib.SMTP('smtp.pouta.csc.fi')
   smtpObj.sendmail(sender, receivers, message)
   print("Successfully sent email")
except SMTPException:
   print("Error: unable to send email")
```

When sending e-mail, you need a valid _Sender_ address in your e-mails,
such as your university e-mail address, since this will be validated by
the SMTP server.

If you want to set up any services on cPouta that generate a large
amount of SMTP traffic (e.g. public mailing lists), please contact
the CSC Service Desk to coordinate this.

### About Sender Policy Framework (SPF) and others

You might need to add CSC's SPF record to your own domain existing DNS record, if SPF is already configured in use. 
Even if SPF is not configured, it should be anyway considered because some email domains reject emails from email domains where SPF is not configured.

!!! info "Authenticated SMTP server"
    In some situation, instead of configuring the SPF record, it is better to simply use an external authenticated SMTP server. Preferably the SMTP server provided by your email provider.

    Also it's good to understand that you may only add/edit SPF record of a domain for which your organization manages its DNS records.

!!! warning "Silent email discards"
    A badly configured SPF record might have the effect that emails are silently discarded by some email providers. 

    Please note that taking SPF in use, or just by modifying existing record incorrectly, affects the whole domain email traffic functionality.

The part which should be added to SPF record is "include:hosted-at.csc.fi".
Your domain SPF record should look then something like this:

```
domain.of.the.sending.email.address.    IN    TXT    "v=spf1 include:hosted-at.csc.fi ~all"
```

You can use the `dig` command to check if the entry already exists in your domain existing DNS record:
```
dig domain.of.the.sending.email.address TXT

;; ANSWER SECTION:
domain.of.the.sending.email.address.    IN    TXT    "v=spf1 include:hosted-at.csc.fi ~all"
```

There are other protocols to take into account, like Domain-based Message Authentication, Reporting and Conformance [DMARC](https://en.wikipedia.org/wiki/DMARC) and DomainKeys Identified Mail [DKIM](https://en.wikipedia.org/wiki/DomainKeys_Identified_Mail), but the details are out of scope for this document.

Here is a simplified summary of the different DNS records for a domain sending emails:  
  - SPF tells from where you can send emails using a "SMTP Sender" in that domain  
  - DKIM signature records specify public keys that are used to sign the email messages with a "From" in that domain  
  - DMARC specifies how messages that fail any of the above should be handled  

If you are using `smtp.pouta.csc.fi`, the SPF record specifies that emails with an "SMTP sender" in csc.fi can be sent. The messages with a "From" in csc.fi are signed with our key and the DMARC record for csc.fi specifies that the messages that fail any of the above should be quarantined.

If you want the services such as Google, Microsoft, etc to check and identify your emails, you can register a new domain for this purpose, host email services with appropriate forwarding, create SPF/DKIM/DMARC records for it and use this domain in the email headers.

## DNS services in cPouta

cPouta does not currently offer integrated name service management.

### Predefined DNS names

All our floating IPs are by default mapped to a hostname, for example:

```
vm0120.kaj.pouta.csc.fi has address 86.50.168.120
```

These default DNS records do also have the reverse DNS entry. To find the hostname of a floating IP, you can use `host` command:

```sh
host -a <floating IP address>
```

And the result is `vmXXXX.kaj.pouta.csc.fi` listed in the output:

```
...
;; ANSWER SECTION:
x.x.x.x.in-addr.arpa. xxx IN     PTR     vmXXXX.kaj.pouta.csc.fi.
```

### Custom DNS name

In some cases you would like to use your own DNS name, a different one to the predefined one explained above, for example `mywesite.myuniversity.fi`. To create this new DNS name, you need to contact your DNS provider (in the example the administrators of `myuniversity.fi`) and request the new DNS record to point to your floating IP. Once created, the DNs record will take few minutes to propagate through the internet and will be visible globally.


In most cases, these forward DNS records (`name -> IP`) are enough.But some services will also require the reverse DNS lookups (`IP -> name`) to work. This means that we have to
configure Pouta's DNS server to say that the floating IP you are using
resolves back to the domain name you set up (`mywebsite.myuniversity.fi`).

You can request a reverse DNS mapping by sending an email to <servicedesk@csc.fi> with this information:

1. The DNS name that you already configured to point to the desired floating IP.
1. The Project name where the Virtual machine is.
1. A short description of the use case that creates the need for this reverse record.

!!! info ""
    You do not need to let us know if the floating IP is moved to another machine within the same project. The reverse DNS record will stay as it is.

When you no longer need the mapping, please contact us again in <servicedesk@csc.fi> so we can remove the reverse DNS entry.

!!! warning "Obsolete records will be purged"
    We reserve the right to clean up old reverse DNS records where the forward DNS records do not match anymore, or when the project is closed.

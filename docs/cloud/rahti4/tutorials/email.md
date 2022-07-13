# Sending e-mail from Rahti

The procedure is the same as for [sending an e-mail from cPouta](/cloud/pouta/additional-services/).

you need to configure your mail transfer agent (MTA) to use the following SMTP relay server (a.k.a. smarthost):

```
smtp.pouta.csc.fi:25
```

The server does not require authentication.

When sending e-mail, you need a valid `Sender` address in your e-mails, such as your university e-mail address, since this will be validated by the SMTP server. Please note that this is a different e-mail header attribute from the `From` attribute.

If you want to set up any services on _Rahti_ that generate a large amount of SMTP traffic (e.g. public mailing lists), please contact the CSC Service Desk to coordinate this.

## Example

This python script could be used:

```python
#!/usr/bin/env python

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

* You should replace `sender@domain.com` with your email, or the email you want to receive replies to.
* You should replace as well `destination@domain.com` with the destination email.
* The relay SMTP server will only allow to send emails from clients from centain IPs, like from Rahti nodes. In other words, the script above will not work from your desktop/laptop.

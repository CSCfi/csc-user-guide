!!! warning "Medium level"
    A knowledge of Python is a plus.
   
    This tutorial implies that you have a running [Pod](../../usage/kubernetes-concepts.md#pod) and you want to add a SMTP configuration.

# Sending e-mail from Rahti

The procedure is the same as for [sending an e-mail from cPouta](../../../pouta/additional-services.md).

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
* The relay SMTP server will only allow to send emails from clients from certain IPs, like from Rahti nodes. In other words, the script above will not work from your desktop/laptop.

## Before deploying in production ⚠️

Here is some recommendations to follow before deploying your email server on Rahti:

- Check that the sender address exists, not like a generic `noreply@`
- Check the recipient address(es) are real and correct, not a value copied from a template/tutorial
- You have received the test email you sent
- You are monitoring your application logs for SMTP errors after deployment

### Why is it important?

If your sender address doesn't accept replied, and your recipient address is wrong, the bounce has nowhere to go and the failure will never surface on its own. Our admins will eventually flag persistent delivery failures from your workload.

If you got a message from CSC about failed email delivery, search for hardcoded/default email adresses in env vars, app settings, and re-verify

We recommend that you set up a minimal delivery monitoring on your side or use a sender address that actually forwards bounces to someone who'll look at them.
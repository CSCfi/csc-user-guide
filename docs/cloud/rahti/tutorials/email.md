# Sending e-mail from Rahti

The procedure is the same as for [sending an e-mail from cPouta](/cloud/pouta/additional-services/).

you need to configure your mail transfer agent (MTA) to use the following SMTP relay server (a.k.a. smarthost):

```
smtp.pouta.csc.fi:25
```

The server does not require authentication.

When sending e-mail, you need a valid `Sender` address in your e-mails, such as your university e-mail address, since this will be validated by the SMTP server. Please note that this is a different e-mail header attribute from the `From` attribute.

If you want to set up any services on _Rahti_ that generate a large amount of SMTP traffic (e.g. public mailing lists), please contact the CSC Service Desk to coordinate this.


# Do you offer in Rahti SSL certificates?

Yes, a wildcard certificate for the DNS names `*.2.rahtiapp.fi` and `*.rahtiapp.fi` is installed and can be used directly by the user.

So if the DNS name of your service is under the subdomain `rahtiapp.fi`, simply enable the *TLS encryption* of the route, and automatically the route will have a valid certificate. The certificate is managed by the Rahti team, this includes the renewal and installation.

If the DNS name is not under the subdomain `rahtiapp.fi`, you need to provide your own certificate. You need to take care of obtaining the certificate, adding it to the `Route` object, and afterwards renew it before it expires.

You can read more about this in our [Custom domain names and secure transport](../../cloud/rahti/tutorials/custom-domain.md) tutorial.

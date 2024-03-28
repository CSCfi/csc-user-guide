# Do you offer in Rahti 2 SSL certificates?

Yes, a wildcard certificate for the DNS names `*.2.rahtiapp.fi` is installed and can be used directly by the user.

So if the DNS name of your service is under the subdomain `2.rahtiapp.fi`, simply enable the *TLS encryption* of the route, and automatically the route will have a valid certificate. The certificate is managed by the Rahti team, this includes the renewal and installation.

If the DNS name is not under the subdomain `2.rahtiapp.fi`, you need to provide your own certicate. You need to take care of obtaining the certiciate, adding it to the `Route` object, and afterwards renew it before it expires.

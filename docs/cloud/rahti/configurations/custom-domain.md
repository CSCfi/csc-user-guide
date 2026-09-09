# Custom domains

You can bring your own domain to Rahti and expose your web applications under that domain. You are responsible for managing the domain's DNS settings as well as its certificates. For more information on configuring a custom domain, see the [Custom domain names and secure transport](../tutorials/intermediate/custom-domain.md) tutorial.

* **DNS configuration:** you need to configure a `CNAME` record pointing to `router-default.apps.2.rahti.csc.fi`. In cases where this is not possible, another option is to configure an `A` record containing the IP address of `router-default.apps.2.rahti.csc.fi`. The way this is done depends on the registrar of the DNS record.

    ```console
    $ host <your-domain>
    <your-domain> is an alias for router-default.apps.2.rahti.csc.fi.
    router-default.apps.2.rahti.csc.fi has address 195.148.21.61
    ```

* **Certificates:** any certificate provider can be used, for example the free certificates provided by the [Let's Encrypt controller](../tutorials/intermediate/custom-domain.md#acme-protocol-automatic-certificates).

A Route that uses a custom domain supports the same features as any other Route. For example, you can restrict which clients are able to reach it with [IP allow-listing](../usage/networking.md#ip-allow-listing).

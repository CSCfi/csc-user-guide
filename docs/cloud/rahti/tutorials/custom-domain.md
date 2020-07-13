## Custom domain names and secure transport

Custom domain names and HTTPS secure data transport are implemented in the
route object level. They are controlled with the keywords `spec.host` and
`spec.tls`.

The public DNS CNAME record of the custom domain name should point to `rahtiapp.fi`,
and the custom DNS name is placed in the `spec.host` entry of the route object:

*`route-with-dns.yaml`*:

```yaml
apiVersion: v1
kind: Route
metadata:
  labels:
    app: serveapp
  name: myservice
spec:
  host: my-custom-dns-name.replace.this.com
  to:
    kind: Service
    name: serve
    weight: 100
```

The TLS certificates and private keys are placed in the `spec.tls` field, for
example:

```yaml
apiVersion: v1
kind: Route
metadata:
  labels:
    app: serveapp
  name: myservice
spec:
  host: my-custom-dns-name.replace.this.com
  to:
    kind: Service
    name: serve
    weight: 100
  tls:
    insecureEdgeTerminationPolicy: Redirect
    termination: edge
    certificate: |-
      -----BEGIN CERTIFICATE-----
      ...
      -----END CERTIFICATE-----
      -----BEGIN CERTIFICATE-----
      ...
      -----END CERTIFICATE-----
    key: |-
      -----BEGIN PRIVATE KEY-----
      ...
      -----END PRIVATE KEY-----
```

This definition creates a route with the private key placed in
`spec.tls.key` and the certificates placed in `spec.tls.certificate`. In this example,
HTTP traffic is redirected to use the HTTPS protocol due to the `Redirect` setting in
`spec.tls.insecureEdgeTerminationPolicy`, and the TLS termination is handled by the
route object, in the sense that traffic coming from the service `serve` is assumed
to be non-encrypted (the `spec.tls.termination: edge`). Other termination policies:

* `passthrough`: Assume that the TLS connection is terminated internally in the
  pod and forward the encrypted traffic.
* `reencrypt`: Terminate the TLS connection in the router and open another
  secure connection that must be terminated at the pod.

!!! Caution

    Always treat the contents of the field `spec.tls.key` in the route objects with
    special care, since the private TLS key should be never exposed to
    non-trusted parties.

!!! Hint

    letsencrypt.org provides free and open certificates. Routes can be
    automated to be secure with a third-party
    [openshift-acme controller](https://github.com/tnozicka/openshift-acme)
    by annotating the route objects.

    Another way of utilizing the certificates provided by Let's Encrypt is to
    use the [`certbot`](https://certbot.eff.org/) tool on the debug console and
    renewing the certificate with e.g. the CronJob controller.

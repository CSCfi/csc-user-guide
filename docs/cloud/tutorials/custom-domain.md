# Custom domain names and secure transport

Custom domain names and HTTPS secure data transport are implemented in the
route object level. They are controlled with the keywords `spec.host` and
`spec.tls`.

Let's say that you want to use `my-custom-dns-name.replace.this.com` as the custom domain. The public DNS CNAME record of the custom domain name (`my-custom-dns-name...`) should point to `router.2.rahtiapp.fi`. The update of the DNS entry is up to the customer and depends on the domain registar procedures. Then the custom DNS name itself is placed in the `spec.host` entry of the route object:

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

!!! Info "Test DNS"

    Before the  DNS record is updated and live, it is possible to use the [hosts file](https://en.wikipedia.org/wiki/Hosts_\(file\)) to create that DNS record into your own computer.

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
`spec.tls.insecureEdgeTerminationPolicy`. The TLS termination is handled by the
route object, in the sense that traffic coming to and from he service `serve` is going to be non-encrypted (the `spec.tls.termination: edge`). Other termination policies:

* `passthrough`: Assume that the TLS connection is terminated internally in the
  pod and forward the encrypted traffic.
* `reencrypt`: Terminate the TLS connection in the router and open another secure connection that must be terminated at the pod.

See the explanation in the [Networking routes](../rahti2/networking.md#routes) page.

!!! warning

    Always treat the contents of the field `spec.tls.key` in the route objects with
    special care, since the private TLS key should be never exposed to
    non-trusted parties.

## Let's Encrypt

[letsencrypt.org](https://letsencrypt.org/) provides free and open certificates. Routes can automatically obtain a "let's encrypt" certificate using the third-party [openshift-acme controller](https://github.com/tnozicka/openshift-acme). The process is simple:

* Clone the [openshift-acme controller](https://github.com/tnozicka/openshift-acme) repository.

```sh
git clone https://github.com/tnozicka/openshift-acme.git
```

* The whole process is documented in the [README.md](https://github.com/tnozicka/openshift-acme/blob/master/README.md) file. We recommend the [Single namespace](https://github.com/tnozicka/openshift-acme/tree/master/deploy#single-namespace) method. It will deploy the controller inside your Rahti 2 project and it will only work for the `Route` you have defined inside said project:

```sh
cd openshift-acme
oc apply -f deploy/single-namespace/{role,serviceaccount,issuer-letsencrypt-live,deployment}.yaml
oc create rolebinding openshift-acme --role=openshift-acme --serviceaccount="$( oc project -q ):openshift-acme" --dry-run -o yaml | oc apply -f -
```

* Add an annotation to the Route you need the certificate for.

```sh
oc annotate route <route_name> kubernetes.io/tls-acme='true'
```

* Wait for few minutes. The controller will see that the annotation has been added, and it will start the process of requesting the certificate, validating the request, issuing the certificate, and finally adding it to the Route. It will also add an annotation to the `Route` with the status:

```yaml
  annotations:
    acme.openshift.io/status: |
      provisioningStatus:
        earliestAttemptAt: "2021-02-09T10:26:15.006145385Z"
        orderStatus: valid
        orderURI: https://acme-v02.api.letsencrypt.org/acme/order/XXXXXXXXX/XXXXXXXXXX
        startedAt: "2021-02-09T10:26:15.006145385Z"
    kubernetes.io/tls-acme: 'true'
```

The certificate is ready. The controller will take care of checking the validity of the certificate, and of renewing it when necessary (every 3 months).

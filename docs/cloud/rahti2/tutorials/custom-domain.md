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

See the explanation in the [Networking routes](../networking.md#routes) page.

!!! warning

    Always treat the contents of the field `spec.tls.key` in the route objects with
    special care, since the private TLS key should be never exposed to
    non-trusted parties.

## Cloud native certificate management

[**cert-manager**](https://cert-manager.io/docs/) is a powerful and extensible X.509 certificate controller for Kubernetes and OpenShift workloads. It will obtain certificates from a variety of Issuers, both popular public Issuers as well as private Issuers, and ensure the certificates are valid and up-to-date, and will attempt to renew certificates at a configured time before expiry.

One of the supported certificate authorities is [letsencrypt.org](https://letsencrypt.org/), which provides free and open certificates. The process has 3 steps:

1. First you need to configure an `Issuer`. You only need to confogure one per `NameSpace`

    ```yaml
    apiVersion: cert-manager.io/v1
    kind: Issuer
    metadata:
      name: letsencrypt
    spec:
      acme:
        # You must replace this email address with your own.
        # Let's Encrypt will use this to contact you about expiring
        # certificates, and issues related to your account.
        email: <<YOUR_EMAIL>>
        server: https://acme-v02.api.letsencrypt.org/directory
        privateKeySecretRef:
          # Secret resource that will be used to store the account's private key.
          name: example-issuer-account-key
        # Add a single challenge solver, HTTP01 using nginx
        solvers:
        - http01:
            ingress:
              ingressClassName: openshift-default
    ```

    You need to replace `<<YOUR_EMAIL>>` by your email. This is to automatically create a free Let's Encrypt account.

1. Then you need to create the `Certificate` object. You can create an many certificates as needed:

    ```yaml
    apiVersion: cert-manager.io/v1
    kind: Certificate
    metadata:
        name: nginx
    spec:
        secretName: tutorial-tls
        duration: 2160h # 90d
        renewBefore: 360h # 15d
        issuerRef:
            name: letsencrypt-staging
            kind: Issuer
        commonName: <<DNS_NAME>>
        dnsNames:
          - <<DNS_NAME>>
    ```

    You need to replace `<<DNS_NAME>>` by the name of the DNS you need the certificate for. The certificates will be stored in the `Secret` called `tutirial-tls`, you can change the name of the secret on the YAML above to any name that makes sense for you.

1. Finally you just need to create the `Ingress`:

    ```yaml linenums="1"
    apiVersion: networking.k8s.io/v1
    kind: Ingress
    metadata:
        name: tuto
        annotations:
          cert-manager.io/issuer: letsencrypt
    spec:
        rules:
        - http:
            paths:
            - path: /test
              pathType: Prefix
              backend:
                service:
                  name: echo-service
                  port:
                    number: 9000
      tls:
      - hosts:
        - <<DNS_NAME>>
        secretName: tutorial-tls
    ```

    The key lines on the `Ingress` objects are:

    - Line `6` (`cert-manager.io/issuer`) must point to the same name of the `Issuer` you created.
    - Line `20` (`hosts` array), the `<<DNS_NAME>>` must be the same as before.
    - Line `21` (`secretName`) must point to same secret you used before.

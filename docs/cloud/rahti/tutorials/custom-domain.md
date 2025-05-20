!!! warning "Middle level"
    You need a knowledge of OpenShift CLI tool [oc](../usage/cli.md) and OpenShift [Routes](../concepts.md#route) API  
    A knowledge on how internet certificates work is a plus.

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

## ACME protocol, automatic certificates

The Automatic Certificate Management Environment (ACME) protocol is a communications protocol for automating interactions between certificate authorities and their users' servers. [letsencrypt.org](https://letsencrypt.org/) is a non-profit Certificate Authority, that provides **free** and **open** certificates using the ACME protocol. It is possible to **get** and **renew** automatically valid certificates from Let's Encrypt. There are other certificates providers that support the ACME protocol, but we will focus on Let's Encrypt because it is the most known of them. Here we will document two methods, the **cert-manager** and the **ACME controller**.

### Cert-manager

This is the recommended option to obtain and renew Let's Encrypt certificates. The process to get a certificate involves creating 3 API objects: `Issuer`, `Certificate` and `Ingress`. We can do this using the Web interface, or the Command Line Interface. As in this case the web interface is not much easier than the CLI, we will use the Command Line Interface.

![Cert manager](../../img/cert-manager.png)

1. First, as usual, you need to [install oc](../usage/cli.md#how-to-install-the-oc-tool) and [login into Rahti](../usage/cli.md#how-to-login-with-oc). Then you need to [create a Rahti project](../usage/projects_and_quota.md#creating-a-project). Finally make sure you are in the correct project: `oc project <project_name>`.

1. Double check that the domain name exists. Let's Encrypt needs to verify that you indeed control said domain name, and it does that by issuing a HTTP request to the actual Domain Name and it expects it to respond accordingly. To test it, enter the Domain name in your browser and see that Rahti answers accordingly.

1. Then you need to create an `Issuer`:

    ```sh
    echo "apiVersion: cert-manager.io/v1
    kind: Issuer
    metadata:
      name: letsencrypt
    spec:
      acme:
        # You must replace this email address with your own.
        # Let's Encrypt will use this to contact you about expiring
        # certificates, and issues related to your account.
        email: <EMAIL>
        server: https://acme-v02.api.letsencrypt.org/directory
        privateKeySecretRef:
          # Secret resource that will be used to store the account's private key.
          name: example-issuer-account-key
        # Add a single challenge solver, HTTP01 using nginx
        solvers:
        - http01:
            ingress:
              ingressClassName: openshift-default" | oc create -f -
    ```

    - You need to replace `<EMAIL>` by your own email. This is to create automatically an account with Let's Encrypt and to send notification emails.
    - If you want to use a different provider than Let's Encrypt, you will need to setup a different `server` parameter and perhaps add some means of authentication. This is directly dependent on the provider used so we are not able to help you with that, but it should only require to change few lines in the example above.  

1. After the `Issuer` is created, you can create the certificate:

    ```sh linenums="1"
    echo "apiVersion: cert-manager.io/v1
    kind: Certificate
    metadata:
        name: nginx
    spec:
        secretName: hostname-tls
        duration: 2160h # 90d
        renewBefore: 360h # 15d
        issuerRef:
            name: letsencrypt
            kind: Issuer
        commonName: <HOSTNAME>
        dnsNames:
          - <HOSTNAME>" | oc create -f -
    ```

    - You need to replace `<HOSTAME>` in both lines **12** and **14**, by the Domain that you want to get the certificate.

1. If all went as expected a new `Secret` called `hostname-tls` was just created. The secret should have two data entries: `tls.crt` and `tls.key`. Now the only step left is to create an `Ingress`:

    ```sh
    echo "apiVersion: networking.k8s.io/v1
    kind: Ingress
    metadata:
      name: nginx
    spec:
      rules:
      - host: <HOSTNAME>
        http:
          paths:
          - backend:
              service:
                name: <SERVICE>
                port:
                  number: <PORT>
            path: /
            pathType: Prefix
      tls:
      - hosts:
        - <HOSTNAME>
        secretName: hostname-tls
    status: {}" | oc create -f -
    ```

    - You need to replace `<HOSTNAME>` by the same host name that you used in the `Certificate`.
    - You need to replace `<SERVICE>` and `<PORT>` by the corresponding service and the port that provide the website you need the certificate for.

!!! Info "Ingress vs Route"
    `Ingress` and `Route` are two ways of solving the same use case. They approach it differently

If all went well, you should have a valid Certificate.

### OpenShift ACME controller

!!! Info "Deprecated"
    The OpenShift ACME controller has been archived since 2023. This means that while it does still work (at the time of writing this), it may stop working if for example, Let's Encrypt makes any change in their API implementation of ACME.

Routes can automatically obtain a "let's encrypt" certificate using the third-party [openshift-acme controller](https://github.com/tnozicka/openshift-acme). The process is simple:

* Clone the [openshift-acme controller](https://github.com/tnozicka/openshift-acme) repository.

```sh
git clone https://github.com/tnozicka/openshift-acme.git
```

* The whole process is documented in the [README.md](https://github.com/tnozicka/openshift-acme/blob/master/README.md) file. We recommend the [Single namespace](https://github.com/tnozicka/openshift-acme/tree/master/deploy#single-namespace) method. It will deploy the controller inside your Rahti project and it will only work for the `Route` you have defined inside said project:

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

### Troubleshooting

If your certificate hasn't been renewed automatically, you can check its status in the `annotations` section from the `Route`. There is a bug with the date changing from December 31st to January 1st, the year will reset to **0001**. If it's the case, simply delete this section from the annotations (you can find it by browsing **Administrator view** > **Networking** > **Routes** > Select your route > YAML tab):

```yaml
    acme.openshift.io/status: |
      provisioningStatus:
        earliestAttemptAt: "0001-01-01T00:00:01.006145385Z"
        orderStatus: valid
        orderURI: https://acme-v02.api.letsencrypt.org/acme/order/XXXXXXXXX/XXXXXXXXXX
        startedAt: "0001-01-01T00:00:01.006145385Z"
```

**Save** and reload the configuration. The date should be fixed.

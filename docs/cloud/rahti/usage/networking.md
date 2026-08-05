# Networking in Rahti

Rahti provides an integrated IPv4 software-defined network (SDN) layer that allows Pods to communicate inside the cluster and with the outside world. In this network, every Pod gets its own IP address, allowing it to communicate with other Pods directly. By default, a Pod can communicate only with Pods running in the same namespace (i.e. Rahti project) unless the default [NetworkPolicies](../configurations/netpol.md) are changed. When a Pod is restarted or moved, its IP address changes. Therefore, in order to provide stable IPs to applications, `Services` are used to dynamically map the IPs of one or more Pods to fixed IPs and DNS records, which can then be used to reach the Pods. The IPs of Pods and Services are reachable within the cluster only. If a Service is to be exposed to the internet, you will need to create `Routes`. Hereafter, we explain these concepts in detail.

## Pod IPs

Each Pod receives an IP address from the Rahti network (CIDR: 10.128.0.0/14). By default, Pods can communicate with other Pods in the same Rahti project (i.e. namespace), and cross-node Pod communication is ensured dynamically by the Rahti network. However, it is not advisable to use the Pod IPs directly to reach Pods, as the IPs are ephemeral and can change when Pods are recreated. You can check the IP addresses assigned to your Pods using the following command:

```bash
oc get pods -o wide -n <rahti-project-name>
```

## Pod ports

A Pod can run one or more containers, and each container may expose one or more ports. Ports define which network endpoints inside the container are intended to receive traffic. While ports inside a Pod are not required to be explicitly declared when creating a Pod, doing so improves clarity, enables tools to introspect the application, and helps define how **Services** or other Pods should connect to it. Two different containers within the same Pod cannot listen to traffic on the same port. You can declare the ports exposed by your containers as in the following example:

```yaml
apiVersion: v1
kind: Pod
metadata:
  labels:
    app: my-app
  name: web-app
  namespace: my-rahti-project
spec:
  securityContext:
    runAsNonRoot: true
    seccompProfile:
      type: RuntimeDefault
  containers:
    - name: httpd
      image: 'image-registry.openshift-image-registry.svc:5000/openshift/httpd:latest'
      ports:
        - containerPort: 8080
          protocol: TCP
      securityContext:
        allowPrivilegeEscalation: false
        capabilities:
          drop:
            - ALL
```

## Services

A Service is an abstraction that provides a stable way to access a group of Pods. Because Pods are temporary and can be replaced at any time, their IP addresses are temporary as well. A Service solves this by assigning the group of Pods a consistent virtual IP and DNS name. The Service automatically keeps track of which Pods should receive traffic, based on labels, and forwards traffic to them, acting as **load balancers**. This allows applications to communicate with each other reliably even as individual Pods are replaced, restarted, or scaled.

The following YAML definition creates a Service object that points to all Pods with the label **app: my-app**, using the `.spec.selector` field:

```yaml
apiVersion: v1
kind: Service
metadata:
  labels:
    app: my-svc
  name: my-service
  namespace: my-rahti-project
spec:
  ports:
  - name: my-http-port
    port: 80
    targetPort: 8080
  selector:
    app: my-app
  sessionAffinity: None
  type: ClusterIP
```

The Service definition above targets port `8080` in the matching Pods and exposes it as port `80`. This means that all traffic sent to `<service-ip-or-dns>:80` is forwarded to a matching Pod at `<matched-pod-ip>:8080`.

Every Service in Rahti receives a DNS name following this hierarchy:

`<service-name>.<Rahti-project>.svc.cluster.local`

For example, a Service named `backend` in the Rahti project `my-project` will have the following DNS name:

`backend.my-project.svc.cluster.local`

This is the fully qualified domain name (FQDN) inside the cluster. Kubernetes also provides shorter aliases, like `backend`, which can be used to refer to the Service named `backend` from any application running inside the same Rahti project where the Service is created. Similarly, `backend.my-project` can be used to refer to the Service from other Rahti projects.

## Routes

All the IP addresses assigned to Pods and Services are private and non-routable. If you want to expose your **HTTP** application to the internet, you will need to create a [Route](https://docs.redhat.com/en/documentation/openshift_container_platform/4.19/html/ingress_and_load_balancing/routes). A Route allows you to map a public and routable hostname to a Service object created inside your Rahti project. In the following example, all `HTTP` traffic sent to the hostname `myapp.rahtiapp.fi` is redirected to the Service named `my-service`, which in turn forwards it to the appropriate Pods:

```yaml
apiVersion: route.openshift.io/v1
kind: Route
metadata:
  name: my-route
spec:
  host: myapp.rahtiapp.fi
  to:
    kind: Service
    name: my-service
  port:
    targetPort: 80  # This can also refer to the name of the port on the service: my-http-port
```

The `.spec.host` field can be set to any value. However, the Route works out of the box only if you use a `*.rahtiapp.fi` suffix for your hostname. Otherwise, more configuration is needed for setting [custom domain names](../configurations/custom-domain.md).

You can also configure the TLS termination for your Route. Three options are available:

* **Edge:** this is the simplest TLS termination to configure, and the one used in most Rahti applications. The TLS connectivity is terminated at the Rahti router, which means that the router decrypts the incoming connection and forwards plain HTTP to the backend Service/Pod. Use this termination if your application does not need to manage TLS certificates and does not require end-to-end encryption. A Route that has no `tls` section, like the example above, is served over plain HTTP only, so edge termination has to be requested explicitly:

    ```yaml
    spec:
      # ...
      tls:
        termination: edge
        insecureEdgeTerminationPolicy: Redirect
    ```

    The optional `insecureEdgeTerminationPolicy: Redirect` setting makes the router redirect plain HTTP requests to HTTPS.

* **Passthrough:** the Rahti router does not terminate TLS at all. It simply forwards encrypted traffic directly to the Service/Pod. The Pod is responsible for TLS decryption. Use this if your application needs to manage its own TLS certificates and requires end-to-end encrypted traffic. Add the following configuration to your Route to use _passthrough_:

    ```yaml
    spec:
      # ...
      tls:
        termination: passthrough
    ```

* **Re-encrypt:** this is a hybrid mode. The router terminates TLS from the client, then initiates a new TLS connection to the Pod. Pods mapped to the Service are expected to have a valid certificate for the DNS name of the Service. This is used, for example, when you want the default Rahti router certificate to be used for client TLS sessions, while a private certificate is used to encrypt the traffic inside the Rahti cluster. Add the following configuration to your Route to use _re-encrypt_:

    ```yaml
    spec:
      # ...
      tls:
        termination: reencrypt
        destinationCACertificate: |
          <CA for backend certificate>
    ```

    The `destinationCACertificate` CA certificate is used to validate the private Pod/Service certificate.

Routes support several configurations and features like rate limiting, IP allow-listing (firewall), HTTP-to-HTTPS redirection, and other options that can be explored in the [external documentation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.19/html/ingress_and_load_balancing/routes). However, note that the TLS termination in use can limit the available features.

!!! warning "Re-encrypt"

    For _re-encrypt_ to work, it is necessary to provide your own certificate. Three things are required: (1) a certificate/key pair in PEM-encoded files, where the certificate is valid for the Route host, (2) optionally, a separate CA certificate in a PEM-encoded file that completes the certificate chain, and (3) a separate destination CA certificate in a PEM-encoded file. If one of these is not provided correctly, the Route will not work.

### IP allow-listing

An important feature of Routes is the IP allowlist, i.e. allowing only a single IP or a range of IPs to access the `Route`. This can be achieved by creating an annotation in the Route object with the key `haproxy.router.openshift.io/ip_allowlist`, and by setting the value to a space-separated list of IPs and/or network ranges. See the examples below.

!!! info "Note"

    The list of the IPs is in the format of **space-separated** values.
    For example: `"192.168.1.0/24 10.0.0.1"`

!!! warning

    If the allowlist entry is malformed, Rahti will discard the allowlist and allow all traffic.
    Example of malformed `"192.168.0"` or `'192.168.1.0/24 '` -> Note the extra whitespace!

* This first example will allowlist a network IP range (`193.166.0.0/16`):

    ```bash
    oc annotate route <route_name> haproxy.router.openshift.io/ip_allowlist='193.166.0.0/16'
    ```

* It is possible to allowlist only a specific IP:

    ```bash
    oc annotate route <route_name> haproxy.router.openshift.io/ip_allowlist='188.184.9.236'
    ```

* It is also possible to allowlist multiple IPs and networks at the same time:

    ```bash
    oc annotate route <route_name> haproxy.router.openshift.io/ip_allowlist='193.166.0.0/15 193.167.189.25'
    ```

Alternatively, you can set the annotation directly in the `Route` resource when creating it for the first time.

```yaml
apiVersion: route.openshift.io/v1
kind: Route
metadata:
  name: my-route
  namespace: my-rahti-project
  annotations:
     haproxy.router.openshift.io/ip_allowlist: '192.168.1.0/24 10.0.0.1'
spec:
  host: my-app-name.rahtiapp.fi
  to:
    kind: Service
    weight: 100
    name: my-service
  tls:
    insecureEdgeTerminationPolicy: Redirect
    termination: edge
status:
  ingress: []
```

## More information on networking

  * [Custom domains](../configurations/custom-domain.md)
  * [Egress IPs](../configurations/egress-ip.md)
  * [LoadBalancer Service (Ingress IPs)](../configurations/loadbalancer-service.md)
  * [Network Policy](../configurations/netpol.md)

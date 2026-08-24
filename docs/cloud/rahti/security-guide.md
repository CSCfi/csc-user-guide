# Security guide

Rahti applications are exposed to the internet, and their security should be treated with appropriate care. The user on whose account a service is running in Rahti is responsible for its security. See the [terms of use](https://rahti.csc.fi/terms_of_use.html) for details about the responsibilities.

This guide should be treated as the baseline that must be taken into account, rather than as a checklist for perfect security.

Measures that tighten the security of the services running in Rahti can be divided roughly into the categories described below.

## Cluster policy

By default, Rahti applies the following  policies:

- **No root enforced**: this means that a container cannot run with root privileges. It will fail to start.

- **Random UID/GID**: when your Pod is deployed in Rahti, a UID from the range allocated to your Rahti project is assigned automatically. The number is usually something like `1000620000`. You cannot assign a UID/GID outside that range, for example `1001`, as it requires special privileges.

- **[Restricted-v2 policy](https://connect.redhat.com/en/blog/important-openshift-changes-pod-security-standards)**:
    - `allowPrivilegeEscalation` cannot be set to `true`. Leave it empty or set it to `false`.
    - All capabilities must be dropped by setting `capabilities.drop` to `ALL`. The only capability that may be added back is `NET_BIND_SERVICE`.
    - Either leave `seccompProfile` empty or set `seccompProfile.type` to `RuntimeDefault`.

- **[Default Pod resource limits](./configurations/resource-quota.md#default-pod-resource-limits)**

## Securing routes

Enable the **TLS encryption** of routes. The router supports the modern and secure TLS versions, TLS v1.3 and TLS v1.2. TLS v1.1 and below are no longer considered secure. If the DNS name of your service is under the subdomains `*.rahtiapp.fi` or `*.2.rahtiapp.fi` (e.g. `coolservice.rahtiapp.fi`), the default wildcard TLS certificate provided by Rahti can be used directly. Otherwise, you need to add your certificate data in the route object, as described on the [Custom domains](./configurations/custom-domain.md) page.

Access to the services should be limited to selected networks with an **allowlist** whenever applicable, as described in [IP allow-listing](./usage/networking.md#ip-allow-listing). This is relevant whenever access can be restricted in terms of IP addresses.

Secure routes thwart eavesdropping attacks that target, for example, service passwords and usernames, and other critical data sent over the internet.

It is recommended to activate the HSTS header. The HTTP Strict-Transport-Security response header (HSTS for short) tells the browser to always use HTTPS and never HTTP for a given Route. It can be activated by running this command:

```sh
oc annotate route test-route haproxy.router.openshift.io/hsts_header="max-age=31536000;includeSubDomains;preload"
```

The value of the annotation is the header itself, and `max-age`, in seconds, is mandatory. The header only takes effect on Routes that terminate TLS, that is, on routes using edge or re-encrypt termination.

It is also recommended to configure rate limits on your public Routes. This allows you to control how many requests a client can send to your application exposed via a route over a given period of time. It is typically used to protect applications from abuse, accidental overload, or denial-of-service scenarios. Add the following annotations to your Route:

```sh
oc annotate route <route-name> \
  haproxy.router.openshift.io/rate-limit-connections="true" \
  haproxy.router.openshift.io/rate-limit-connections.concurrent-tcp="10" \
  haproxy.router.openshift.io/rate-limit-connections.rate-http="50"
```

* The annotation `rate-limit-connections=true` enables connection rate limiting on the router.
* The annotation `rate-limit-connections.concurrent-tcp=10` allows a single client IP to have at most 10 concurrent TCP connections.
* The annotation `rate-limit-connections.rate-http=50` allows a single client IP to make at most 50 HTTP requests in a 3-second period. The equivalent annotation for TCP connections is `rate-limit-connections.rate-tcp`.

!!! info "FAQ Rate Limiting"

    Refer to [Protect your application against DDoS Attacks](../../support/faq/DDos.md).

## Image security

Outdated container images are prone to exploits via security vulnerabilities, and unfamiliar images may contain malicious code. For these reasons, a given container image should be used only if:

1. It is from a known and trusted source, so that the known security vulnerabilities are patched and you can trust it not to contain malicious code.
2. You have reviewed its Dockerfile build configuration, and its base image satisfies condition 1 or has been reviewed in the same way.

Other things to keep in mind:

* Use curated images.
* Prefer images that regularly receive security updates.
* Use static container image analysis tools if available. For support, ask your local IT support.
* The smaller the image, the less "surface area" there is for attacks:
    * Utilize the builder pattern in your images if you use compiled languages: build the binary in a different image from where the application is deployed. In Docker, this can be achieved with [multi-stage builds](https://docs.docker.com/develop/develop-images/multistage-build/), and in OKD, directories of other images may be mounted during the build process by [chaining builds](https://cloud.redhat.com/blog/chaining-builds). This way, only essential pieces of the software are present in the final image.
    * If the application is written in an interpreted language, use language based images. Instead of installing Node.js on top of the Alpine image, use for example `node:22-alpine`.

## IP addresses for firewall openings

The IP address for all outgoing customer traffic is `86.50.229.150`. By opening a firewall to this IP, you let in all traffic coming from any Rahti project, not only from your own. It is therefore advised not to rely on IP filtering alone, but to use it as a secondary measure, together with an authentication system such as OAuth.

If your application needs to be identified by a single IP address of its own, a dedicated egress IP can be requested for your Rahti project. See the [Egress IPs](./configurations/egress-ip.md) page for details and for how the IP may change in the future.

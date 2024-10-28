Rahti 2 applications are exposed to the Internet, and
their security should be treated with an appropriate care.
The user on whose account a service is running in Rahti 2 is
responsible for its security. See the [terms of use](https://rahti.csc.fi/terms_of_use.html) for details about the
responsibilities.

This guide should be treated as the baseline which must be taken
in account rather than a checklist for perfect security.

Measures that tighten the security of the services running in Rahti 2 can be
roughly divided in two categories.

## Cluster policy

By default, our cluster applies default security policies:  

- **No root enforced**: That means that you cannot run a container with root privileges. It will fail.  

- **Random UID/GID**: When your pod is deployed in our cluster, a random UID will be generated. You cannot assigned a UID/GID out of this range (for example, `1001`), it will require special privileges. Usually, the number is like `1000620000`.  

- **[Restricted-v2 policy](https://connect.redhat.com/en/blog/important-openshift-changes-pod-security-standards)**: Since Openshift 4.11, the new SCC policies are introduced according to the [Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/).  
  - What is the difference between v1 and v2 SCC (Security Context Constraints) policies?  
    - V2 does not permit *allowPrivilegeEscalation=true*  
        - Empty or false is compatible with v1 SCC and therefore works on OCP versions < 4.11  
    - V2 requires you to leave the dropped capabilities empty, set it to *ALL*, or add only *NET_BIND_SERVICE*  
        - By being accepted as v2 the SCC will always drop *ALL*. V1 only dropped *KILL*, *MKNOD*, *SETUID*, *SETGID* capabilities.  
        - V2 still allows explicitly adding the *NET_BIND_SERVICE* capability  
    - V2 requires you to either leave *SeccompProfile* empty or set it to *runtime/default*  
        - Empty is compatible with v1 and works on OCP versions < 4.11  

- **[Default Pod resource limits](../rahti2/usage/projects_and_quota.md#default-pod-resource-limits)**

## Securing routes

Enable the **TLS encryption** of routes. The router supports modern and secure TLS versions, TLS v1.3 and TLS v1.2. TLS v1.3 is currently the latest version. TLS v1.1 and below are no longer considered secure. If the DNS name of your service is under
the subdomain `*.2.rahtiapp.fi` (e.g. `coolservice.2.rahtiapp.fi`), the default
wildcard TLS certificate provided by Rahti 2 can be used directly. Otherwise,
you need to add your certificate data in the route object.

Access to the services should be limited to selected networks with
**whitelists** whenever applicable (See the chapter
[Routes](../tutorials/elemental_tutorial.md#route)). This is relevant whenever
access can be restricted in terms of IP addresses.

Secure routes thwart eavesdropping attacks that target e.g. service passwords
and usernames, and other critical data sent over the internet.

## Image security

Outdated container images are prone to exploits via security vulnerabilities,
and unfamiliar images may contain malicious code. For these reasons, a given container
image should be used only if:

1. It is from a known and trusted source so that the known security
   vulnerabilities are patched and you can trust it not to contain malicious
   code.
2. You have reviewed its Dockerfile build configuration and the base layer
   satisfies Rule #1 or #2.

Other things to keep in mind:

* Use curated images.
* Prefer images that regularly receive security updates.
* Use static container image analysis tools if available. For support, ask your
  local IT support.
* The smaller the image, the less "surface area" there is for attacks:
  * Utilize the builder pattern in your images if you use compiled languages:
    Build the binary in a different image from where the application is
    deployed. In Docker, this can be achieved with [multi-stage
    builds](https://docs.docker.com/develop/develop-images/multistage-build/),
    and in OpenShift, directories of other images may be mounted during the build
    process by [chaining
    builds](https://cloud.redhat.com/blog/chaining-builds).
    This way, only essential pieces of the software are present in the
    final image.
  * If the application is written in an interpreted language, use language
    based images. Instead of installing Node.js on top of the Alpine image, use
    e.g., `node:21-alpine`.

## IP addresses for firewall openings

The IP for all outgoing customer traffic is `86.50.229.150`. By opening a firewall to this IP, you will let in all traffic coming from any Rahti 2 project. It is advised to not solely rely in IP filtering for security, but use this a secondary measure, like for example an OAuth authentication system.

There is no plan to change this IP, but it is not possible to give a 100% assurance that an unforeseeable event will ever force us to change it. If this IP ever changes, it will be properly announced in advance.

It is possible, for selected namespaces that need it, to configure a dedicated IP. Each request is reviewed individually due to the fact that there is a limited pool of virtual IPs available. For more information, please create a ticket to <servicedesk@csc.fi>.

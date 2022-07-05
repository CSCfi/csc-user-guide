<style>
.admonition-title { background-color: rgba(255, 145, 0, 0.1) !important; }
.admonition { background-color: white !important; }
</style>
!!! Attention "⚠️ Rahti 3 is deprecated"

    This page is about a deprected version of Rahti, please consult the [updated documentation article](cloud/rahti4/security-guide/)

# Security guide

Rahti applications are exposed to the Internet, and
their security should be treated with an appropriate care.
The user on whose account a service is running in Rahti is
responsible for its security. See the [terms of use](https://rahti.csc.fi/agreements/terms_of_use/) for details about the
responsibilities.

This guide should be treated as the baseline which must be taken
in account rather than a checklist for perfect security.

Measures that tighten the security of the services running in Rahti can be
roughly divided in two categories.

## Securing routes

Enable the **TLS encryption** of routes. If the DNS name of your service is under
the subdomain `rahtiapp.fi` (e.g. `coolservice.rahtiapp.fi`), the default
wildcard TLS certificate provided by Rahti can be used directly. Otherwise,
you need to add your certificate data in the route object.

Access to the services should be limited to selected networks with
**whitelists** whenever applicable (See the chapter
[Routes](../tutorials/elemental_tutorial#route)). This is relevant whenever 
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
    builds](https://docs.okd.io/3.11/dev_guide/builds/advanced_build_operations.html#dev-guide-chaining-builds).
    This way, only essential pieces of the software are present in the
    final image.
  * If the application is written in an interpreted language, use language
    based images. Instead of installing Node.js on top of the Debian image, use
    e.g., `node:8-debian`.

## IP addresses for firewall openings

The IP for all outgoing customer traffic is `193.167.189.25`. By opening a firewall to this IP, you will let in all traffic coming from any Rahti project. It is advised to not solely rely in IP filtering for security, but use this a secondary measure, like for example an OAuth authentication system.

There is no plan to change this IP, but it is not possible to give a 100% assurance that an unforeseeable event will ever force us to change it. If this IP ever changes, it will be properly announced in advance.

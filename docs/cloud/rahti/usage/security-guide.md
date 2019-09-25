# Security guide

Rahti applications are exposed to the Internet and
their security should be treated with an appropriate care.
The user on whose account a service is running in Rahti, is
responsible of its security. See [Terms of Service]() for details about
responsibilities.

This guide should be treated as the baseline which must be taken
in to account rather than checklist for a perfect security.

Measures that harden the security of the services running in Rahti can be
roughly split in the following two categories.

## Securing routes

Enable **TLS encryption** of routes. If the DNS name of your service is under
subdomain `rahtiapp.fi` (like `coolservice.rahtiapp.fi`) then the default
wildcard TLS certificate provided by Rahti can be used directly. Otherwise,
you need to add your certificate data in the Route object.

Access to the services should be limited to selected networks through
**whitelists** whenever applicable (See Chapter
"[Routes](/cloud/rahti/tutorials/elemental_tutorial#routes)"). This is relevant whenever
the access can be restricted in terms of IP addresses.

Secure routes thwart eavesdropping attacks that target, e.g., service passwords
and usernames, and other critical data sent over the Internet.

## Image security

Outdated container images are prone to exploits via security vulnerabilities,
and unfamiliar images may contain malicious code. For these reasons, a given container
image should be used only if

1. It is from a known and trusted source so that the known security
   vulnerabilities are patched and one can trust it not to contain malicious
   code
2. You have reviewed its Dockerfile build configuration and the base layer
   satisfies Rule #1 or #2

Other things to keep in mind:

* Use curated images.
* Prefer images that regularly receive security updates.
* Use static container image analysis tools if available. For support, ask your
  IT organization.
* The smaller the image, the less "surface area" there is for attacks:
  * Utilize the builder pattern in your images if you use compiled languages:
    Build the binary in a different image than where the application is
    deployed to. In Docker, this can be achieved with [multi-stage
    builds](https://docs.docker.com/develop/develop-images/multistage-build/),
    and in OpenShift, directories of other images may be mounted during build
    process by [chaining
    builds](https://docs.okd.io/3.11/dev_guide/builds/advanced_build_operations.html#dev-guide-chaining-builds).
    This way, only the essential pieces of software are present in the
    final image.
  * If the application is written in an interpreted language, use language
    based images—instead of installing Node.js on top of Debian image use,
    e.g., `node:8-debian`.

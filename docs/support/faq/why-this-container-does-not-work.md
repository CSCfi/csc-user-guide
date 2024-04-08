# Why this container report permission denied errors?

The most common reason for a container to fail to run in Rahti 2, is that the container image expects to be run as `root`. As Rahti 2 does not run images as root, permission denied errors will stop the execution.

The solution is to use a different image. The first option is to find another image that is prepared to be run as a non root user. If there is not an image already prepared to run in OpenShift, or it is not provided by a trustable source, the other option is to modify the current image to make it work with a non root user, for example as described in the [Creating images](../../cloud/rahti2/images/creating.md) section.

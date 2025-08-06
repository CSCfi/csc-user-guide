# Advanced

## Base images and system package managers

RHEL based, DNF package manager (RPM): [rockylinux](https://hub.docker.com/_/rockylinux), [almalinux](https://hub.docker.com/_/almalinux), [redhat/ubi8](https://hub.docker.com/r/redhat/ubi8), [redhat/ubi9](https://hub.docker.com/r/redhat/ubi9), [centos](https://hub.docker.com/_/centos) (legacy)

SUSE based, Zypper (RPM): [opensuse/leap](https://hub.docker.com/r/opensuse/leap)

Debian based, APT (DEB): [ubuntu](https://hub.docker.com/_/ubuntu), [debian](https://hub.docker.com/_/debian)

## Building complex container images

- definition file sections
- where to install software
- using makefiles for building, [Makefile Tutorial](https://makefiletutorial.com/)
- user-space package managers (pip, conda, spack)

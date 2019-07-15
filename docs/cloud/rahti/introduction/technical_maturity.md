# Technical maturity

The Rahti container cloud is currently in **beta**. This page lists various
aspects of the technical maturity of the system to give you an idea of what
kinds of workloads it is suitable for at the moment.

!!! note
    OpenShift relases are based on Kubernetes versions so that OpenShift 3.6 is
    based on Kubernetes 1.6, OpenShift 3.7 is based on Kubernetes 1.7 and so on.

| Maturity indicator          | Current value                                       | Best feasible value                                              |
|-----------------------------|-----------------------------------------------------|------------------------------------------------------------------|
| **OpenShift version**       | 3.11 {: class='td_ok'}             | 3.11{: class='td_ok'}                                             |
| **Service level**           | JHS174 level A (97%, service times weekdays 8-16){: class='td_ok'}      | JHS174 level B (99%, service times weekdays 7-19){: class='td_ok'}        |
| **GlusterFS storage class** | Technical preview{: class='td_warn'}                | Technical preview{: class='td_warn'}                             |

## Work remaining before production

We're working on several fronts to make Rahti ready for production.
These include:

  * Storage
  * Networking
  * Billing
  * Customer processes

We will describe the details of these areas here.

### Storage

The GlusterFS storage that is used for all persistent volumes in
Rahti at the moment is only a technology preview according to Red
Hat, and it has to do additional 2x replication on top of the 3x replication
already done by Ceph. Thus we have 6x replication of all data, which is
unnecessary and would be prohibitively expensive for a larger system.

Before going into production, we want to have another storage class that would
not have these limitations and that we could scale up as the system grows.

We've also seen some stability issues with the storage in heavy use, though not
issues that would affect data consistency. GlusterFS will remain as an option
for at least some time after a new storage system is in place, and there will be
instructions for migrating data from the GlusterFS storage class to the final
production ready storage class. We will still need some solution for
ReadWriteMany volumes when in production, and that solution may be the current
GlusterFS installation.

### Networking

All end user traffic to and from the cluster currently goes via a
single VM. We have some ideas about how to create a more scalable load
balancing setup, but we still need to implement these ideas before going
to production. While the current solution provides enough bandwidth for
a limited number of users, it will quickly become a bottleneck when
usage of the system grows.

### Billing

Currently usage of the system is free, but before going to production we need
to have some way of billing for use in place. Work on implementing this has
started, and we hope to have it ready before going to open beta. Usage will
consume the same billing units that are also in use in CSC's Pouta and Taito
systems.

### Customer processes

We'll need to make the system visible on the CSC web pages and make it possible
to apply for access to it via the web page. This will require integrations in
the customer process and other areas.

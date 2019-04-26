# Scope and description of the service

The Rahti container cloud service is a cloud computing service. The Rahti
service is based on OKD, which is a distribution of Kubernetes. The Rahti
service allows its Users to run their own containerized applications on top of
it. The Rahti service provides, but is not necessarily limited to, these
resources:

* Hosting of User Applications comprised of container instances and groups of
  container instances
* Storage services
* Virtual networks for connecting container instances
* Load balancing of traffic to User Applications
* Features for replication, rolling updates, auto-recovery and auto-scaling of User Applications
* Basic default domain name and TLS for hosted User Applications (under rahtiapp.fi)

Users can manage their resources using a web interface accessible through a web
browser and through a set of APIs which allow programmatic management of
resources. In order to access and use the service the User must have a CSC user
account.

The User's applications are isolated from other Users’ applications from a
network, storage and computational view.

The Rahti service accounts for service usage based on the resources used. Up to
date resource cost information is found in the [Rahti
documentation](https://rahti.csc.fi).

## What is Pouta?

cPouta and ePouta are the IaaS cloud services at CSC. The cPouta
cloud is the public cloud which is easily accessible via the
internet. The ePouta cloud is a virtual private cloud designed to meet
the security requirements of handling sensitive data. Both the cPouta
and ePouta clouds run on the OpenStack cloud software. The Pouta cloud
services are suitable for most kinds of computational workloads and
any other supporting services these workloads might need.

The cPouta virtual machines can be connected to external IP addresses,
and in this case they can be directly accessed on the internet. This
helps customers run widely available services, but the customers must
also take care to secure their machines. The virtual machines do not
have access to any other part of CSC's infrastructure, other than what
is already visible on the internet. Application data and software must
be uploaded either via the internet or copied from CSC's existing
shared storage services.
 
The ePouta cloud services are well suited for computational workloads
involving sensitive data as well as extending a customer's existing IT
infrastructure. The ePouta cloud services are attached to the customer's
infrastructure and can be used to analyse sensitive data which may
require large amounts of memory or clustered I/O performance, a remote
desktop for processing sensitive data etc. The virtual machines in the
ePouta cloud may optionally have network access to specific sensitive
data repositories at CSC.

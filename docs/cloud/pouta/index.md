# Overview

Pouta is an umbrella term for cPouta and ePouta services, which are the 
IaaS cloud services at CSC. The cPouta cloud is the public cloud which 
is easily accessible via the internet. The ePouta cloud is a virtual 
private cloud designed to meet the security requirements of handling 
sensitive data. Both the cPouta and ePouta clouds run on the OpenStack 
cloud software. The Pouta cloud services are suitable for most kinds of 
computational workloads and any other supporting services these workloads 
might need.

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

## Accessing the Pouta services

Due to the nature of ePouta, it is not available as a self-service. Questions regarding ePouta should be directed to our helpdesk (<servicedesk@csc.fi>).

cPouta is self-service and you can find more information on how to get access here: [Applying for cPouta access](../../accounts/how-to-add-service-access-for-project.md).

The web interfaces of the Pouta clouds are available at following addresses:

| URL | Service name | Access |
| :-------------| :-------------| :-----|
| [https://pouta.csc.fi](https://pouta.csc.fi) | cPouta web interface | Accessible on the internet using Haka, Virtu, etc. |
| [https://epouta.csc.fi](https://epouta.csc.fi) | ePouta web interface | Accessible only from IPs provided for accessing the management interfaces of ePouta using CSC account. |

Login is available for [supported account types](../../accounts/how-to-create-new-user-account/) like Haka and Virtu.

![Pouta web login page](../img/pouta_overview_web_login.png)

Once you have successfully logged in, you can continue with the [Getting Started Guide](getting-started/).

If you are already familiar with the basics of OpenStack, please go directly to the [Configuration](configuration/) and [Advanced](advanced/) sections of the Pouta documentation.

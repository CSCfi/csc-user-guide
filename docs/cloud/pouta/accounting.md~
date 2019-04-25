## Accounting Principles and Quotas

This document describes how resource usage is calculated as Billing Units (BUs).

Academic research  customers can have their resource use paid  for by
the Ministry  of Education  and Culture.  For commercial  customers or
academic  customers who  require more  than what  is granted  from the
Ministry  paid-for  allocation,  we  have billing  unit  packages  for
purchase.

For more  information about  which category  your project  falls into,
please visit the [Accounts and Projects] page.

[TOC]

### Accounting of resources

Currently,  we account  for virtual  machines, volume  storage, object
storage and floating IPs.

| Resource | Cost |
|------------------|--------------------|
| Virtual machines | See [flavors page] |
| Storage volumes  | 3,5 BU / TiB hour  |
| Object storage   | 3,5 BU / TiB hour  |
| Floating IPs     | 0,2 BU / hour      |



Please note that virtual machines consume BUs regardless you are using
them or not. This means that  a shut down or suspended virtual machine
still  consumes BUs.  You can  find more  information about  different
states of virtual machine and their BU consumption on [virtual machine
lifecycle page] The minimum accounting time for a virtual machine is
one hour. Another source for estimating usage is the [Resource Calculator]

Storage volumes consume billing units based on their size. The unit of
measure is [TebiByte] hours. Storage  volumes consume BUs even if they
are not attached to virtual machines.

Objects  storage  consumes billing  units  based  on the  stored  data
amounts.  The billing units are consumed until the data is removed.

Floating  IPs are  billed  if they  are allocated  to  the project  or
assigned  to a  virtual machine.  Any  extra routers  you create,  and
connect to  the external  network, will also  billed for  one floating
IP.  The default  router you  get with  the project  does not  consume
billing units.

### Other costs

If you have  a contract with CSC, you will  always be billed according
to  the  contract if  it  differs  from these  practices.   Commercial
customers  are usually  also  billed  a fee  for  each  member of  the
project.

## Quotas

Each  cPouta and  ePouta project  have  a cloud  computing quota  that
limits the  use of simultaneous  cloud resources. There is  a default
cPouta project  quota which is  quite small, but  users can  apply for
extensions                through                the                <a
href="https://sui.csc.fi/group/sui/my-projects"
class="external-link">resource allocation process</a> of CSC.

**Table 3.3** Default size of the cPouta project quota.

| Resource type  | default |
|----------------|:-------:|
| Instances      |    8    |
| Cores          |    8    |
| Memory         |  32 GB  |
| Floating IPs   |    2    |
| Storage        |   1 TB  |


With   the  default   resources,  a   cPouta  user   could  launch   8
*standard.tiny*  instances   or  2  *standard.large* instances   or  1
*hpc-gen1.8core*  instance. The  purpose of  the quota  is to  prevent
individual users from reserving the entire cluster and thus preventing
access for other users.

Storage is also limited by a quota. The default quota for new projects
is  1 TB.  Additional  allocations  can be  requested  through our  <a
href="https://sui.csc.fi/group/sui/my-projects"
class="external-link">resource allocation process</a>.

<span  style="text-align:  justify;">The  initial  quotas  for  ePouta
projects are agreed on when starting a new project.</span>

Please note  that having free  quota does not guarantee  that specific
resources are available.

Specific virtual machine flavors may be full, so you can not provision
them even  if you have the  quota to do  so. We always strive  to have
free computing  resources in  some flavors. We  will be  improving the
visibility of what flavors are available in the future.

We try to always have free storage and floating IP resources, if quota
for them has been allocated.

  [Accounts and Projects]: https://research.csc.fi/accounts-and-projects
  [flavors page]: https://research.csc.fi/pouta-flavours
  [virtual machine lifecycle page]: https://research.csc.fi/pouta-vm-lifecycle
  [TebiByte]: https://en.wikipedia.org/wiki/Tebibyte
  [Resource Calculator]: https://research.csc.fi/pricing-of-computing-services

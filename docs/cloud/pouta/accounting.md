# Accounting principles and quotas

This document describes how resource usage in Pouta is calculated as Billing Units (BUs).

Academic research customers can have their resource use paid for by
the Ministry of Education and Culture. For commercial customers and
academic customers who require more than what is granted from the
ministry's paid-for allocation, CSC has billing unit packages for
purchase.

For more information about which category your project falls into,
please see
[Accounts and projects](https://research.csc.fi/accounts-and-projects){ target="_blank" }.

[TOC]

## Accounting for resources

Currently, we account for virtual machines, volume storage, object
storage and floating IPs.

| Resource | Cost |
|------------------|--------------------|
| Virtual machines | See [Flavors](vm-flavors-and-billing.md) |
| Storage volumes | 3,5 BU / TiB hour |
| Floating IPs | 0,2 BU / hour |

Please note that virtual machines consume BUs regardless whether you are using
them or not. This means that a shut down or suspended virtual machine
still consumes BUs. You can find more information about the different
states of virtual machines and their BU consumption in
[Virtual machine lifecycle](vm-lifecycle.md). The minimum accounting time for a
virtual machine is one hour. Another source for estimating usage is the
[Resource calculator](https://research.csc.fi/billing-units/#buc).

Storage volumes consume billing units based on their size. The unit of
measure is [TebiByte](https://en.wikipedia.org/wiki/Tebibyte) hours. Storage
volumes consume BUs even if they are not attached to virtual machines.

Objects storage consumes billing units based on the stored data
amounts. The billing units are consumed until the data is removed.

Floating IPs are billed if they are allocated to a project or
assigned to a virtual machine. Any extra routers you create and
connect to the external network will be also billed for one floating
IP. The default router included in the project does not consume
billing units.

## Other costs

If you have a contract with CSC, you will always be billed according
to the contract even if it differs from these practices. Commercial
customers are usually also billed a fee for each member of the
project.

## Quotas

Each cPouta and ePouta project has a cloud computing quota that
limits the use of simultaneous cloud resources. There is a default
cPouta project quota which is quite small, but users can apply for
extensions by sending email to [CSC Service Desk](../../support/contact.md).

**Default size of the cPouta project quota.**

| Resource type | default |
|----------------|:-------:|
| Instances | 8 |
| Cores | 8 |
| Memory | 32 GB |
| Floating IPs | 2 |
| Storage | 1 TB |

With the default resources, a cPouta user could launch eight
*standard.tiny* instances or two *standard.large* instances or one
*hpc-gen1.8core* instance. The purpose of the quota is to prevent
individual users from reserving the entire cluster and thus preventing
other users from accessing it.

Storage is also limited by a quota. The default quota for new projects
is 1 TB. Additional allocations can be requested by sending email
to [CSC Service Desk](../../support/contact.md).

The initial quotas for ePouta projects are agreed upon when starting a new project.

Please note that having free quota does not guarantee that specific
resources are available.

Specific virtual machine flavors may be full, so you cannot provision
them even if you have the quota to do so. We always strive to have
free computing resources in some flavors. We are planning to improve the
visibility of which flavors are available in the future.

We try to always have free storage and floating IP resources, if quota
for them has been allocated.

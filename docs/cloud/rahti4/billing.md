
# Rahti billing

## Terminology

* Billing unit (BU): A unit used for billing at CSC - each resource consumes a given amount of BUs per hour.
* CSC computing project: A placeholder for the user's resources information - including: the number of BUs and the CSC
services which are available for use.
* OpenShift project: A Kubernetes namespace with additional annotations.

## Billing model

Billing units are calculated by scraping usage data from all of the OpenShift projects owned by the user.
These calculations are based on:

* Pod core usage (per core hour)
* Pod memory usage (per RAM GB hour)
* Persistent volumes (per TiB hour)

The rate at which billing units are consumed depends on the size of the
resources. Billing units are consumed as follows:

| Resource         | Billing units |
|------------------|---------------|
| Pod core hour    | 0,5           |
| Pod RAM GB hour  | 1             |
| Storage TiB hour | 3             |

------------------------------------------------------------------------------------------------------------------------
Cost will be calculated based on actual resources request with cpu, ram and storage rather than actual usage.
Currently, Rahti does not bill for the stored images.
------------------------------------------------------------------------------------------------------------------------

For example, let's say you create a pod with the following specs:

* 0.2 cores
* 512 MiB RAM

You also create a persistent volume of size 10 GiB and attach it to the pod. The
cost in BUs can be calculated as follows:

![BU calculation](img/BU-calculation.drawio.svg)

[Billing Unit calculator](https://my.csc.fi/buc)

<iframe srcdoc="https://my.csc.fi/buc" style="width: 100%; height: 1300px; border: 0"></iframe>


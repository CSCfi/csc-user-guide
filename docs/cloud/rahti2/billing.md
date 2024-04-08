## Terminology

* Billing unit (BU): A unit used for billing at CSC - each resource consumes a given amount of BUs per hour.
* CSC computing project: A placeholder for the user's resources information - including: the number of BUs and the CSC
services which are available for use.
* Rahti 2 project: A Kubernetes namespace with additional annotations.

## Billing model

Billing units usage of given CSC project are calculated by scraping the usage data from all Rahti 2 projects associated with that CSC project.
These calculations are based on:

* Pod core.
* Pod memory.
* Persistent volumes.

If the current usage is lower than the minimum requested resource, the requested resource is used for the calculations.

The rate at which billing units are consumed depends on the size of the
resources. Billing units are consumed as follows:

| Resource         | Billing units |
|------------------|---------------|
| Pod core hour    | 1             |
| Pod RAM GB hour  | 1,5           |
| Storage TiB hour | 3             |


!!! info

    Currently, Rahti 2 does not bill for the stored images.

Let's see an example. You create a pod with the following specs:

* 1 core
* 512 MiB RAM

and the current real usage is:

* 0.5 cores
* 1 GiB RAM

You also create a persistent volume of size 10 GiB and attach it to the pod. The
cost in BUs can be calculated as follows:

The core usage is 0.5 cores and the request is 1 cores. According to the BU consumption rate 1 > 0.5 so 1 is used.

The memory usage is 1 GiB and the request is 512 MiB. The same goes for memory usage 1 GiB > 512 MiB so 1 GiB is used

![BU calculation](../img/BU-calculation.drawio.svg)

## Billing unit calculator

For an estimate of the billing units the services you plan on using will consume, please refer to the
billing unit calculator below. The [billing unit calculator can also be found at MyCSC](https://my.csc.fi/buc/).

<iframe srcdoc="https://my.csc.fi/buc" style="width: 100%; height: 1300px; border: 0"></iframe>

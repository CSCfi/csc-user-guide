# Billing

## Terminology

* Billing Unit (BU): A unit used for billing at CSC - each resource consumes a given amount of BUs per hour.
* Cloud Billing Unit (Cloud BU): Billing Units assigned to Cloud resource usage.
* CSC computing project: A placeholder for the user's resources information - including: the number of Cloud BUs and the CSC
services which are available for use.
* Rahti project: A Kubernetes namespace with additional annotations.

## Billing model

Cloud Billing Units usage of given CSC project are calculated by scraping the usage data from all Rahti projects associated with that CSC project.
These calculations are based on:

* Pod core.
* Pod memory.
* Persistent volumes.

If the current usage is lower than the minimum requested resource, the requested resource is used for the calculations.

The rate at which Cloud Billing Units are consumed depends on the size of the
resources. 
Please note that there will be slight adjustment in BU consumption rates of Rahti from year 2026 as shown in the table:

| Resource         | Cloud Billing Units |
|------------------|---------------------|
| Pod core hour    | 1.05                |
| Pod RAM GB hour  | 1.6                 |
| Storage TiB hour | 3.6                 |


!!! info

    Currently, Rahti does not bill for the stored images.

## Example calculation

You create a pod with the following specs:

* 1 core
* 512 MiB RAM

and the current real usage is:

* 0.5 cores
* 1 GiB RAM

You also create a persistent volume of size 10 GiB and attach it to the pod. The
cost in Cloud BUs can be calculated as follows:

The core usage is 0.5 cores and the request is 1 cores. According to the Cloud BU consumption rate 1 > 0.5 so 1 is used.

The memory usage is 1 GiB and the request is 512 MiB. The same goes for memory usage 1 GiB > 512 MiB so 1 GiB is used

![BU calculation](../img/BU-calculation.drawio.svg)

## Billing Unit calculator

For an estimate of the Billing Units the services you plan on using will consume, please refer to the
Billing Unit calculator below. The [Billing Unit calculator can also be found at MyCSC](https://my.csc.fi/buc/).

<iframe srcdoc="https://my.csc.fi/buc" style="width: 100%; height: 1300px; border: 0"></iframe>

!!! info "\* **Cloud BU**: Cloud Billing Unit"

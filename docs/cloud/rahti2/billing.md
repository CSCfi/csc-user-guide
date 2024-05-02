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

<!--
## Billing unit calculator

For an estimate of the billing units the services you plan on using will consume, please refer to the
billing unit calculator below. The [billing unit calculator can also be found at MyCSC](https://my.csc.fi/buc/).

<iframe srcdoc="https://my.csc.fi/buc" style="width: 100%; height: 1300px; border: 0"></iframe>

-->
## Cost Change when migrating from Rahti 1 to Rahti 2

While migrating from Rahti 1 to Rahti 2, BU calculation will be changed. The main differences in calculation are:

* In Rahti 1, BU’s are calculated based on requested resources while in Rahti 2, BU’s are calculated based on current uses. If current uses is lower than the minimum requested resource, requested resource is used for the calculation.
* BU for Pod core hour in Rahti 1 is 0.5 and in Rahti 2 it is 1.
* BU for Pod RAM GiB hour in Rahti 1 is 1 where in Rahti 2 It is 1.5.

Note : BU for Storage TiB hour is same i.e. 3.

So, in case of the above example the BU calculation for Rahti 1 is

![BU calculation for Rahti 1](./images/Rahti1BU.drawio.svg)


Default limits in Rahti 2 can be set lower than the default quota. Where in Rahti 1 default limit is same as default quota. For more details [Migration to Rahti 2](../rahti/rahti-migration.md). This can decrease the default costs for the user. For the same example the BU For Rahti 1:

![Default cost for Rahti 1](./images/Rahti1Requests.drawio.svg)

and for Rahti 2 BU will lie between 
limits:

![Default limits for Rahti 2](./images/Rahti2Limits.drawio.svg)

and requests:

![Default requests for Rahti 2](./images/Rahti2Request.drawio.svg)

Note : BU for Storage TiB hour is considered same i.e. 3.
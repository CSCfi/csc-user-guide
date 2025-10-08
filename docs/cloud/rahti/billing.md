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
Please note that there will be some adjustment in BU prices of Rahti for 2026 as shown in the table:

| Resource         | Cloud Billing Units<br>(current) |Cloud Billing Units<br>(2026) |
|------------------|------------------|---------------------|
| Pod core hour    | 1                   |1.05
| Pod RAM GB hour  | 1.5                 |1.6
| Storage TiB hour | 3                   |3.5


!!! info

    Currently, Rahti does not bill for the stored images.

Let's see an example. You create a pod with the following specs:

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

<!--
## Billing Unit calculator

For an estimate of the Billing Units the services you plan on using will consume, please refer to the
Billing Unit calculator below. The [Billing Unit calculator can also be found at MyCSC](https://my.csc.fi/buc/).

<iframe srcdoc="https://my.csc.fi/buc" style="width: 100%; height: 1300px; border: 0"></iframe>

-->
## Cost Change when migrating from Rahti 1 to Rahti

While migrating from Rahti 1 to Rahti, Cloud BU calculation will be changed. The main differences in calculation are:

* In Rahti 1, they are calculated based on requested resources while in Rahti,  they are calculated based on current uses. If current uses is lower than the minimum requested resource, requested resource is used for the calculation.
* Cloud BU for Pod core hour in Rahti 1 is 0.5 and in Rahti it is 1.
* Cloud BU for Pod RAM GiB hour in Rahti 1 is 1 where in Rahti It is 1.5.

Note: Cloud BU for Storage TiB hour is same i.e. 3.

So, in case of the above example the Cloud BU calculation for Rahti 1 is

![Cloud BU calculation for Rahti 1](./images/Rahti1BU.drawio.svg)

Default limits in Rahti can be set lower than the default quota. Where in Rahti 1 default limit is same as default quota. For more details [Migration to Rahti](../rahti/rahti-migration.md). This can decrease the default costs for the user. For the same example the Cloud BU For Rahti 1:

![Default cost for Rahti 1](./images/Rahti1Requests.drawio.svg)

and for Rahti Cloud BU will lie between 
limits:

![Default limits for Rahti](./images/RahtiLimits.drawio.svg)

and requests:

![Default requests for Rahti](./images/RahtiRequest.drawio.svg)

Note : Cloud BU for Storage TiB hour is considered same i.e. 3.

!!! info "\* **Cloud BU**: Cloud Billing Unit"

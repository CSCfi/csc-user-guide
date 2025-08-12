# Questions and answers related to the billing unit renewal (2025)

## 1. What are the new billing units?

The new billing unit (BU) types are **HPC**, **HPC GPU**, **Cloud** and
**Storage**. In other words, CSC's services for research will consume different
billing units based on the kind of services used. A summary of which service
uses which units is depicted below:

* **HPC billing unit**
    * Puhti, Mahti and Roihu jobs *without GPU*
* **HPC GPU billing unit**
    * Puhti, Mahti and Roihu jobs *with GPU*
* **Cloud billing unit**
    * cPouta, ePouta, Rahti, Pukki DBaaS, SD Desktop
* **Storage billing unit**
    * Puhti, Mahti and Roihu Lustre storage, Allas, Shared fileservice, SD
      Connect

## 2. When are the new billing units taken into use?

The new billing units will be taken into use in September 2025. The exact date
will be announced later.

## 3. What will happen to my old billing units?

Old unused billing units already granted to projects will be migrated to the
new units, i.e. no granted resources are lost. The mapping of old BUs to new
BUs will be based on the past usage of the project. In other words, e.g.
projects only running GPU jobs on Puhti will not get cloud billing units which
they have no use for.

## 4. How will the new billing units affect resource applications?

Resource applications will be done in the four new billing units in the future.
This means that users have to consider what kind of resources and services they
need before applying for them.

Moreover, the application limits for different resources will be separated
based on the capacity available under every billing unit type. So far, all
billing unit applications have been processed based on whether they are S-, M-,
or L-sized applications. However, 1 million BUs used in cPouta has a much
larger impact on the service capacity compared to the same amount of BUs used
on Mahti CPU nodes. Thus, the size limits for resource applications will be
based on the type of billing unit applied for.

## More information

* Blog: [Mapping out the future of billing units](https://csc.fi/en/blog/mapping-out-the-future-of-billing-unit/) (CSC.fi)
* Blog: [Billing unit renewal schedule and changes](https://csc.fi/en/blog/billing-unit-renewal-schedules-and-changes/) (CSC.fi)
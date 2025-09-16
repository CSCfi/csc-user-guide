# Questions and answers related to the billing unit renewal (2025)

## 1. What are the new billing units?

The new billing unit (BU) types are **CPU**, **GPU**, **Cloud** and
**Storage**. In other words, CSC's services for research will consume different
billing units based on the kind of services used. A summary of which service
uses which units is depicted below:

* **CPU billing unit**
    * Puhti, Mahti and Roihu jobs *without GPU*
* **GPU billing unit**
    * Puhti, Mahti and Roihu jobs *with GPU*
* **Cloud billing unit**
    * cPouta, ePouta, Rahti, Pukki DBaaS, SD Desktop
* **Storage billing unit**
    * Puhti, Mahti and Roihu Lustre storage, Allas, Shared fileservice, SD
      Connect

!!! info "Note"
    This billing unit renewal does **not** affect LUMI billing. However, a
    similar resource cutter as detailed [below](#cutter) will also be taken into
    use on LUMI starting October 1st, 2025.

## 2. When are the new billing units taken into use?

The new billing units will be rolled out starting **September 29th, 2025**. The
exact schedule is detailed below:

* **Mon 29.9.** Billing Unit applications in MyCSC are temporarily closed
* **Wed 1.10.** Old applications are processed and projects are granted new
  Billing Units
* **Thu 2.10.** New Billing Units are taken into use in MyCSC and services,
  resource applications for new Billing Units are opened

## 3. Will I need to do something? What will happen to my old billing units?

No, you do not need to do anything. Old unused billing units already granted to
projects will be migrated to the new units, i.e. no granted resources are lost.
The mapping of old BUs to new BUs will be based on the past usage of the
project. In other words, e.g. projects only running GPU jobs on Puhti will not
get cloud billing units which they have no use for.

You can check your current BU budget in [MyCSC](https://my.csc.fi), as well as
using the `csc-projects` command on Puhti and Mahti.

## 4. How will the BU renewal affect CSC's services?

The migration to new billing units will have minimal effect on service usage
and services will be available as usual. However, resource applications will be
unavailable during the migration when old billing units are converted into new
ones.

## 5. How will the new billing units affect resource applications?

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

## 6. Will I lose billing units to the new BU cutter even if my projects use billing units? <a id="cutter"></a>

The billing unit renewal introduces a "cutter" that will depreciate unused BUs.
The billing unit cutter only affects projects that have used **less than 40% of their
billing units** in a 6 month period counted from the last billing unit grant
or depreciation check. If a project has used more than that, no resources are
cut. The billing unit cutter affects only academic projects with student
projects being exempt.

## 7. When will the first billing unit depreciation happen?

The billing unit cutter is taken into use at the same time as the new units, so
the first cuts would happen in **March 2026 at the earliest**. The billing unit
usage of projects is checked six months after either the latest billing unit
grant or the latest depreciation check.

## More information

* Blog: [Billing unit renewal schedule and changes](https://research.csc.fi/2025/06/02/billing-unit-renewal-schedule-and-changes/) (Research.csc.fi)

# Questions and answers related to the Billing Unit renewal (2025)

## 1. What are the new Billing Units?

The new Billing Unit (BU) types are **CPU**, **GPU**, **Cloud** and
**Storage**. In other words, CSC's services for research will consume different
Billing Units based on the kind of services used. A summary of which service
uses which units is depicted below:

* **CPU Billing Unit**
    * Puhti, Mahti and Roihu jobs *without GPU*
* **GPU Billing Unit**
    * Puhti, Mahti and Roihu jobs *with GPU*
* **Cloud Billing Unit**
    * cPouta, ePouta, Rahti, Pukki DBaaS, SD Desktop
* **Storage Billing Unit**
    * Puhti, Mahti and Roihu Lustre storage, Allas, Shared fileservice, SD
      Connect

!!! info "Note"
    This Billing Unit renewal does **not** affect LUMI billing. However, a
    similar resource cutter as detailed [below](#cutter) will also be taken into
    use on LUMI starting October 1st, 2025.

## 2. When are the new Billing Units taken into use?

The new Billing Units will be rolled out starting **September 29th, 2025**. The
exact schedule is detailed below:

* **Mon 29.9.** Billing Unit applications in MyCSC are temporarily closed
* **Wed 1.10.** Old applications are processed and projects are granted new
  Billing Units
* **Thu 2.10.** New Billing Units are taken into use in MyCSC and services,
  resource applications for new Billing Units are opened

## 3. Will I need to do something? What will happen to my old Billing Units?

No, you do not need to do anything. Old unused Billing Units already granted to
projects will be migrated to the new units, i.e. no granted resources are lost.
The mapping of old BUs to new BUs will be based on the past usage of the
project. In other words, e.g. projects only running GPU jobs on Puhti will not
get Cloud Billing Units which they have no use for.

You can check your current BU budget in [MyCSC](https://my.csc.fi), as well as
using the `csc-projects` command on Puhti and Mahti.

## 4. How will the BU renewal affect CSC's services?

The migration to new Billing Units will have minimal effect on service usage
and services will be available as usual. However, resource applications will be
unavailable during the migration when old Billing Units are converted into new
ones.

## 5. How will the new Billing Units affect resource applications?

Resource applications will be done in the four new Billing Units in the future.
This means that users have to consider what kind of resources and services they
need before applying for them.

Moreover, the application limits for different resources will be separated
based on the capacity available under every Billing Unit type. So far, all
Billing Unit applications have been processed based on whether they are S-, M-,
or L-sized applications. However, 1 million BUs used in cPouta has a much
larger impact on the service capacity compared to the same amount of BUs used
on Mahti CPU nodes. Thus, the size limits for resource applications will be
based on the type of Billing Unit applied for.

## 6. Will I lose Billing Units to the new BU cutter even if my projects use Billing Units? <a id="cutter"></a>

The Billing Unit renewal introduces a "cutter" that will depreciate unused BUs.
The Billing Unit cutter only affects projects that have used **less than 40% of their
Billing Units** in a 6 month period counted from the last Billing Unit grant
or depreciation check. If a project has used more than that, no resources are
cut. The Billing Unit cutter affects only academic projects with student and
course projects being exempt.

## 7. When will the first Billing Unit depreciation happen?

The Billing Unit cutter is taken into use at the same time as the new units, so
the first cuts would happen in **March 2026 at the earliest**. The Billing Unit
usage of projects is checked six months after either the latest Billing Unit
grant or the latest depreciation check.

## More information

* Blog: [Billing unit renewal schedule and changes](https://research.csc.fi/2025/06/02/billing-unit-renewal-schedule-and-changes/) (Research.csc.fi)

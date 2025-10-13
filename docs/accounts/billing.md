---
search:
  boost: 2
---

# Billing

CSC's services are free of charge for academic research, teaching or training for members of Finnish higher education institutions and state research institutes. **Billing Units** (BUs) are used to allocate resources for users' projects using our services. CSC's services consume four different Billing Units (CPU, GPU, Cloud, Storage) based on the service and type of usage. You can [apply for Billing Units in MyCSC portal](how-to-apply-for-billing-units.md) and CSC grants BUs to projects. Usage consumes Billing Units but **no actual payment** is required.

<!-- See the [Billing Unit and price calculator](https://research.csc.fi/billing-units#buc){:target="_blank"} at research.csc.fi. -->

**The billing rates for the services are as follows:**

* [Puhti and Mahti billing](../computing/hpc-billing.md)
* Allas object storage billing:  1 TiB consumes **1** Storage BU per hour currently and from year 2026, 1 TiB will consume 1.05 Storage BU per hour. Only actual
   data stored in Allas is billed.
* [Pouta billing](../cloud/pouta/vm-flavors-and-billing.md)
* [Rahti billing](../cloud/rahti/billing.md)
* [SD Connect and SD Desktop billing](../data/sensitive-data/sd-use-case-new-user-project-manager.md#sd-connect-bu-consumption)



!!! info "Note"

    For LUMI billing, [see the LUMI documentation](https://docs.lumi-supercomputer.eu/runjobs/lumi_env/billing/){ target=_blank }.

    The use of Fairdata IDA and Kaivos doesn't consume Billing Units.

## Monitoring Billing Unit consumption

In the _My Projects_ page in [MyCSC](https://my.csc.fi) you can study the
Billing Unit consumption and apply for more Billing Units. There you can easily
check who consumed the Billing Units, when they were consumed and in which
service. Note that storage-related Billing Unit consumption (in Puhti/Mahti Scratch folders and in
Allas) is not linked to a specific user account and is reported as "other" or "system".



## Restricted service access and CSC Project closure when Billing Units have been consumed

When all Billing Units (CPU, GPU, Storage or Cloud) in your CSC Project have been consumed, service usage can be limited in services that consume Billing Units. You can track your CSC Project's Billing Unit usage via MyCSC as described above. You can regain full access to your services by [applying for additional Billing Units using the MyCSC portal](how-to-apply-for-billing-units.md).

You will be notified before your CSC Project's Billing Units run out. When an academic CSC project has run out of of Billing Units, the project members have 60 days to apply for additional Billing Units. If the Billing Units run out and after 60 days, the CSC project still has a negative amount of Billing Units, it will be closed.

Detailed information on how services are currently limiting the use when Billing Units run out:

* [Puhti and Mahti](../computing/usage-policy.md#running-out-of-billing-units)
* [Sensitive Data Desktop](../data/sensitive-data/sd-use-case-new-user-project-manager.md#what-happens-if-your-project-runs-out-of-billing-units)







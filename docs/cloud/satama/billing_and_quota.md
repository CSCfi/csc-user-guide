# Billing 

## Terminology

* Billing Unit (BU): A unit used for billing at CSC - each resource consumes a given amount of BUs per hour.

* Storage Billing Unit: Billing Units assigned to usage of storage.

* CSC Project: A placeholder for the user's resources information - including: the number of Cloud BUs and the CSC services which are available for use.

* Satama Project: A Satama project is one which is created at https://satama.csc.fi after satama service is activated at CSC project.

## Billing Model

Currently, Satama will bill for storage only. Billing is based on the amount of data stored. The account of resource usage is provided in one-hour increments. The rate is 3 Storage BU/TiBh i.e. 1 Tib of data stored at Satama will consume 3 Storage BU per hour and 72 Storage BU in a day.

If 10GB of storage is consumed, BU can be calculated using the following formula 
```
(10/1024) * 3 ~= 0.029 BUs per hour
```
A good way to estimate usage cost is the [Billing Unit calculator](https://research.csc.fi/resources/#buc) utility. For more information about Billing in CSC, visit the [Billing](../../accounts/billing.md) page.

# Quota

The default quota for a new project is **50 GB**, but this can be increased if needed. If you need more resources than the defaults, you can apply for more quota by contacting the Service Desk. See the [Contact page](../../support/contact.md) for instructions. Quota requests are handled on a case-by-case basis depending on the currently available resources in Satama and the use case.
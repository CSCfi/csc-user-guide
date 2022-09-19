# How to increase disk quotas

## Increasing the storage capacity in Puhti and Mahti

The quotas of the [scratch](../../computing/disk/#scratch-directory) and [projappl](../../computing/disk/#projappl-directory) directories of Puhti and Mahti servers can be
increased if needed.

You can use MyCSC to manage these quotas.

1. Login to [MyCSC](https://my.csc.fi) and **select the project** you want to
   modify.
1. In the Services list, click Configuration for **Puhti** or **Mahti** service as needed. This opens a page where the project manager can modify the quotas.

You can check the default limits of scratch and projappl areas from the table below. Values in parenthesis indicate automatically approved limits. Applications with higher values will be determined in the next resource allocation meeting.
  
| Directory | Default size | Maximum size | Default file number limit | Maximum file number limit |
|-----------|--------------|--------------|---------------------------|---------------------------|
| projappl  |   50 GiB     |  200&nbsp;GiB&nbsp;(<&nbsp;100&nbsp;GiB)    | 100 000                   | 2 000 000 (<&nbsp;500&nbsp;000)                 |
| scratch   |   1 TiB      |  100&nbsp;TiB&nbsp;(<&nbsp;20&nbsp;TiB)    | 1 000 000                 | 10 000 000 (<&nbsp;5&nbsp;000&nbsp;000)               |

Note that the extended quota consumes your CSC billing units regardless of how
much data you actually have in the directory. [See billing](billing.md) for
details. Furthermore, even after the quota is increased, the automatic cleaning
process will continue removing idle files from the scratch directory.

## Increasing the storage capacity in Allas

The default quota for a new project is 10 TB, but that can be increased if needed. Allas is the preferred storage site for 
any large datasets in the CSC environment, so you should not hesitate to request a larger quota for Allas, if you work with larger data sets.

To increase your Allas quota, please send a request to: servicedesk@csc.fi 
In the request, define what Allas project you are using, how large storage space is needed and what kind of data will be stored to Allas.

Note that storing data in Allas consumes billing units. In Allas, billing is based on the amount of data stored. The rate is 1 BU/TiBh, 
i.e. 1 TB of data stored in Allas consumes 24 BU in a day and 8760 BU in a year. [How to apply for billing units](how-to-apply-for-billing-units.md)

## Increasing the storage capacity in IDA

[About Monitoring and Adjusting Project Quota in IDA User Guide](https://www.fairdata.fi/en/user-guides/user-guide/#project-quota)

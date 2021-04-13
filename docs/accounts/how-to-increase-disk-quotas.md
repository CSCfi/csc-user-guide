# How to increase disk quotas

## Increasing the storage capacity in Puhti and Mahti

The quotas of the scratch and projappl directories of Puhti and Mahti servers can be
increased if needed.

You can use MyCSC to manage these quotas.

1. Login to [MyCSC](https://my.csc.fi) and **select the project** you want to
   modify.
1. In the Services list, click edit configuration (gearwheel symbol) for **Puhti** or **Mahti** service as needed. This
   opens a page where the project manager can modify the quotas.

You can check the default limits of scratch and projappl areas from the table
below.
  
| Directory | Default size | Maximum size | Default file number limit | Maximum file number limit |
|-----------|--------------|--------------|---------------------------|---------------------------|
| projappl  |   50 GiB     |  200 GiB     | 100 000                   | 2 000 000                 |
| scratch   |   1 TiB      |  100 TiB     | 1 000 000                 | 10 000 000                |

Note that the extended quota consumes your CSC billing units regardless of how
much data you actually have in the directory. [See billing](billing.md) for
details. Furthermore, even after the quota is increased, the automatic cleaning
process will continue removing idle files from the scratch directory.

# Roihu data migration guide

## General guidelines

1. **Review and clean up your data.**
    * Like on Puhti and Mahti, Roihu scratch disk is not intended for long-term
      data storage, but should only be used for data that is in active use.
      Thus, only move data that you truly need.
    * Roihu will implement a similar disk cleaning policy as Puhti, meaning
      that files that have not been accessed in 180 days will be deleted.

2. **Ensure that you have enough disk space available on Roihu.**
    * After you have identified the data you need to transfer, check that it
      fits within the default disk quotas on Roihu:

        | Disk area | Default size | Maximum size | Default file number limit | Maximum file number limit |
        |-----------|-------------:|-------------:|--------------------------:|--------------------------:|
        | home      | 15 GiB       | 15 GiB       | 150k                      | 150k                      |
        | projappl  | 15 GiB       | 250 GiB (< 100 GiB) | 150k               | 2.5M (< 1M)         |
        | scratch   | 1 TiB       | 100 TiB (< 20 TiB) | 1M            | 10M (< 5M)  |

        Values is parentheses indicate automatically approved limits.

    * Please note that existing quota extensions on Puhti/Mahti will not
      automatically carry over to Roihu, so you must separately apply for
      increased disk quota via MyCSC beforehand if your data does not fit
      within the default limits.

3. **Please transfer your data directly from Puhti and/or Mahti to Roihu.**
    * For performance and capacity management reasons, it is best to avoid
      transferring data to Roihu via Allas or your local workstation. Instead,
      CSC recommends using command-line based tools such as `rsync` or `rclone`
      to directly push or pull data from Puhti/Mahti to Roihu.
    * Moving data directly from Puhti/Mahti to Roihu requires forwarding your
      SSH agent including a valid SSH certificate to the system on which the
      data transfer process is initiated.

## Small data

## Medium data

## Large data
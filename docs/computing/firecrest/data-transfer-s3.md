# Large file transfer using S3

FirecREST HPC API implements asynchronous large file transfer model using an S3 object storage as a staging medium. On Roihu, the S3 storage used is [Allas](../../data/Allas/index.md). FirecREST uses its own dedicated tenant with dynamically created user-specific buckets.

## How it works

Upon sending an API request to [upload](https://api.roihu.csc.fi/v1/docs#/filesystem/post_upload_filesystem__system_name__transfer_upload_post) or [download](https://api.roihu.csc.fi/v1/docs#/filesystem/post_download_filesystem__system_name__transfer_download_post) task, FirecREST:

- Creates a user-specific bucket in its own Allas tenant.
- Generates pre-signed S3 URLs for the data transfer, using multi-part model if necessitated by the given `fileSize`.
- Schedules a new Slurm DataTransferJob using `account` (your project) defined in the API request, to either transfer files from Allas to Roihu after your upload is completed, or from Roihu to Allas for you to download.
- Returns pre-signed URLs to API client for transferring the data.

## Examples

Various detailed examples for implementing S3 data transfer using bash, .NET and PyFirecREST can be found in [FirecREST v2 user guide](https://eth-cscs.github.io/firecrest-v2/user_guide/#using-s3-transfer-method).

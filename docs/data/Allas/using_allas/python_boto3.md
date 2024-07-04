# Using Allas with the `boto3` Python library and S3 protocol

[`boto3`](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
is a Python library for working with
[Amazon S3](https://aws.amazon.com/s3/) storage and other AWS services.
It can be used to access Allas with the
[S3 protocol](../introduction.md#protocols).

The general workflow for using Python to analyze Allas data looks like
this:

1. Upload the input data to Allas using `boto3` or another client.
2. Download the data from Allas to a local device (personal workstation or CSC
supercomputer) using `boto3`.
3. Analyze the local copy of the data.
4. Write the results to local storage.
5. Upload the results to Allas using `boto3`.

Some Python libraries might also support direct reading and writing with S3,
for example
[AWS SDK for Pandas](https://aws-sdk-pandas.readthedocs.io/en/stable/)
and
[GDAL-based Python libraries](https://github.com/csc-training/geocomputing/blob/master/python/allas/working_with_allas_from_Python_S3.py)
for spatial data analysis.

!!! note ""
    Remember to avoid handling the same objects with both S3 and SWIFT, as
    [they work differently with large objects](../introduction.md#protocols).

## Installation

`boto3` is available for Python 3.8 and higher.
It can be
[installed on a personal device](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#installation)
with `pip` or `conda`.

```bash
# pip
pip install boto3

# conda
conda install boto3
```

### `boto3` on CSC supercomputers

The pre-existing
[`geoconda`](../../../apps/geoconda.md) and
[`biopythontools`](../../../apps/biopython.md)
Python modules have `boto3` installed. 
It is also possible to
[add `boto3` on top of other modules](../../../support/tutorials/python-usage-guide.md#installing-python-packages-to-existing-modules)
using `pip`.

## Configuring S3 credentials

The easiest way to set up S3 credentials for using `boto3` is by
[configuring an S3 connection on a CSC supercomputer](s3_client.md#configuring-s3-connection-in-supercomputers).
After running `allas-conf --mode s3cmd`, the credentials are stored on the
supercomputer in `~/.aws/credentials`, where `boto3` looks for them
automatically.

If you are accessing Allas from a personal workstation,
you can copy `.aws` and its contents to your workstation home directory
[using a file transfer tool](../../moving.md), e.g. by running
`scp -r <username>@puhti.csc.fi:~/.aws $HOME`. As above, `boto3` automatically
looks for your credentials in your local home directory.

Note that only one set of credentials can be stored in `~/.aws/credentials`.
If you wish to use `boto3` with multiple projects simultaneously, you can write the
generated credentials to another file and manually pass them to
`boto3.resource()` as individual parameters. Otherwise, you can simply rerun
`allas-conf --mode s3cmd` to overwrite the credentials file for accessing
the object storage of another project. If you are using `boto3` on a personal
workstation, you obviously need to copy the rewritten credentials file from
the supercomputer.

## `boto3` usage

### Create `boto3` resource

```python
import boto3

# Only include `aws_access_key_id` and `aws_secret_access_key` if
# you do not want `boto3` to get the keys from `~/.aws/credentials`.
# See previous section for explanation.

s3_resource = boto3.resource(
    's3',
    endpoint_url='https://a3s.fi',
    aws_access_key_id='<AWS_ACCESS_KEY_ID>',  # input your S3 access key
    aws_secret_access_key='<AWS_SECRET_ACCESS_KEY>'  # input your S3 secret key
)
```

!!! note ""
    Each subsequent step supposes that a `boto3` resource has been created.

### Create a bucket

Create a new bucket using the following script:

```python
s3_resource.create_bucket(Bucket="examplebucket")
```

### List buckets and objects

List all buckets belonging to a project:
```python
for bucket in s3_resource.buckets.all():
    print(bucket.name)
```

List all objects belonging to a bucket:
```python
my_bucket = s3_resource.Bucket('examplebucket')

for my_bucket_object in my_bucket.objects.all():
    print(my_bucket_object.key)

```

### Download an object

Download an object:
```python
s3_resource.Object('examplebucket', 'object_name_in_allas.txt').download_file('local_file.txt')
```

### Upload an object

Upload a small file called `my_snake.txt` to the bucket `snakebucket`:

```python
s3_resource.Object('examplebucket', 'object_name_in_allas.txt').upload_file('local_file.txt')
```

### Remove buckets and objects

Delete all objects from a bucket:

```python
my_bucket = s3_client.Bucket('examplebucket')
my_bucket.objects.all().delete()

```

Delete a bucket, must be empty:
```python
s3_resource.Bucket('examplebucket').delete()
```

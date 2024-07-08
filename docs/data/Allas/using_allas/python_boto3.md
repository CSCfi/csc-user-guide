# Using Allas with Python over the S3 protocol

You can use the [AWS SDK for Python](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
(`boto3`) to access Allas over the [S3 protocol](../introduction.md#protocols).
`boto3` is a Python library developed for working with
[Amazon S3 storage](https://aws.amazon.com/s3/) and other AWS services.

Below is the general workflow for using Python to analyze data stored in Allas:

1. Upload the input data to Allas using `boto3` or [another
   client](../accessing_allas.md).
2. Download the data from Allas to a local device (personal workstation or CSC
supercomputer) using `boto3`.
3. Analyze the local copy of the data.
4. Write the results to local storage.
5. Upload the results to Allas using `boto3`.

Some Python libraries support direct reading and writing over S3,
such as the
[AWS SDK for pandas](https://aws-sdk-pandas.readthedocs.io/en/stable/)
(general data analysis)
and
[GDAL-based Python libraries](https://github.com/csc-training/geocomputing/blob/master/python/allas/working_with_allas_from_Python_S3.py)
(geospatial data analysis).

!!! note ""
    Remember to avoid handling the same objects with both S3 and SWIFT, as
    [they work differently with large objects](../introduction.md#protocols).

## Installation

### Installing on a personal workstation

`boto3` is available for Python 3.8 and higher.
It can be
[installed on a personal device](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#installation)
using `pip` or `conda`.

```bash
# pip
pip install boto3

# conda
conda install anaconda::boto3
```

### Installing on a CSC supercomputer

The pre-existing [`geoconda`](../../../apps/geoconda.md) and
[`biopythontools`](../../../apps/biopython.md) modules already have `boto3`
installed. If you wish to use the library in another Python environment, you can
use `pip` to
[add it on top of an existing module](../../../support/tutorials/python-usage-guide.md#installing-python-packages-to-existing-modules).

## Configuring S3 credentials

The easiest way to set up S3 credentials for using `boto3` is by
[configuring an S3 connection on a CSC supercomputer](s3_client.md#configuring-s3-connection-in-supercomputers).
After running `allas-conf --mode s3cmd`, the credentials are stored in
`~/.aws/credentials`, which is the default location where `boto3` looks for
them. You can also define another location for the credentials file with
the `AWS_SHARED_CREDENTIALS_FILE` environment variable.

If you wish to access Allas from a personal workstation,
you can copy the credentials file to your device
[using a file transfer tool](../../moving/index.md) like `scp`.

```bash
# Copy the credentials file and its parent directory to your home directory
scp -r <username>@<hostname>.csc.fi:~/.aws $HOME
```

### Configuring credentials for multiple projects

If you wish to use `boto3` with multiple projects simultaneously,
you can do so by saving credentials
[under different profiles](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html#shared-credentials-file):

1. Start by loading the utilities for Allas command-line access, if you have not
   done so yet.
```bash
module load allas
```

2. Since `allas-conf --mode s3cmd` overwrites `.aws/credentials` when it is run,
it is necessary to create another file for storing your S3 credentials.
```bash
touch ~/my_s3_credentials.txt
```

3. Configure credentials for a project.
```bash
allas-conf --mode s3cmd
```

4. Copy the generated credentials to the file you created in step 2.
```bash
cat ~/.aws/credentials >> ~/my_s3_credentials.txt
```

5. Repeat steps 3 and 4 for each desired project.

6. Open the file you created in step 2. and define a profile name for each set
of credentials.
```
[default]  # Change this line to e.g. [my-project]
AWS_ACCESS_KEY_ID=foo
AWS_SECRET_ACCESS_KEY=bar
AWS_DEFAULT_REGION = baz
```

7. If you wish to use `boto3` on a personal workstation,
copy the file you created in step 2 to your workstation.

8. When using `boto3`, you can use the `os` Python module to define which
credentials to use.
```python
import os

# If these are not set, boto3 will get credentials from
# the default profile in ~/.aws/credentials

os.environ['AWS_SHARED_CREDENTIALS_FILE'] = '~/my_s3_credentials.txt'
os.environ['AWS_PROFILE'] = 'my-project'
```

    Of course, you can also set these environment variables in the shell.

## `boto3` usage

### Create `boto3` resource

```python
import boto3
s3_resource = boto3.resource('s3', endpoint_url='https://a3s.fi')
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

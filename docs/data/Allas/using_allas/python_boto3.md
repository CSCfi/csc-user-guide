# Using Allas with Python over the S3 protocol

You can use the [AWS SDK for Python](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
(`boto3`) to access Allas over the [S3 protocol](../introduction.md#protocols).
`boto3` is a Python library developed for working with
[Amazon S3 storage](https://aws.amazon.com/s3/) and other AWS services.

## General data analysis workflow

1. Upload the input data to Allas using `boto3` or [another
   client](../accessing_allas.md).
2. Download the data from Allas to a local device
(i.e. personal workstation or CSC supercomputer) using `boto3`.
3. Analyze your local copy of the data.
4. Write the analysis results to your local storage.
5. Upload the results to Allas using `boto3`.

Some Python libraries support direct reading and writing over S3,
such as
[AWS SDK for pandas](https://aws-sdk-pandas.readthedocs.io/en/stable/)
and
[GDAL-based libraries](https://github.com/csc-training/geocomputing/blob/master/python/allas/working_with_allas_from_Python_S3.py)
(for working with geospatial data).

!!! note ""
    Remember to avoid handling the same objects with both S3 and SWIFT, as
    [they work differently with large objects](../introduction.md#protocols).

## Installation

### Installation on a personal workstation

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

### Installation on a CSC supercomputer

The pre-existing [`geoconda`](../../../apps/geoconda.md) and
[`biopythontools`](../../../apps/biopython.md) modules already have `boto3`
installed. If you wish to use the library in another Python environment, you can
use `pip` to
[add it on top of an existing module](../../../support/tutorials/python-usage-guide.md#installing-python-packages-to-existing-modules).

## Configuring S3 credentials

### Credentials for accessing a single project

The easiest way to set up S3 credentials for using `boto3` is by
[configuring an S3 connection on a CSC supercomputer](s3_client.md#configuring-s3-connection-in-supercomputers).
After running `allas-conf --mode s3cmd`, the credentials are stored in
`~/.aws/credentials`, which is the default location where `boto3` looks for
them. You can also define another location for the credentials file by
modifying the `AWS_SHARED_CREDENTIALS_FILE` environment variable.

If you wish to access Allas from a personal workstation,
you can simply copy the credentials file to your device
[using a file transfer tool](../../moving/index.md) like `scp`.
If you want `boto3` to find the credentials automatically
without having to modify `AWS_SHARED_CREDENTIALS_FILE`,
make sure that you also copy the parent directory as in the example
below.

```bash
# Copy the credentials file and its parent directory to your home directory
scp -r <username>@<hostname>.csc.fi:~/.aws $HOME
```

### Credentials for accessing multiple projects

Using `allas-conf --mode s3cmd` is straightforward,
but it overwrites the existing credentials file when run,
making it somewhat tedious to work with multiple projects.
Therefore, it is recommended to use the 
[Cloud storage configuration](../../../computing/webinterface/file-browser.md#accessing-allas-and-lumi-o)
app in the [Puhti](https://puhti.csc.fi) or [Mahti](https://mahti.csc.fi)
web interface to configure S3 connections, since these configurations are
stored under
[individual S3 profiles](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html#shared-credentials-file).

1. Use *Cloud storage configuration* to configure S3 connections,
or _remotes_, for the projects whose Allas storage you wish
to access. The configurations are stored in `~/.config/rclone/rclone.conf` on
the supercomputer whose web interface you used for generating them.

2. The S3 configuration entries for the access key ID and secret access key
need to be prefixed with `aws_` for `boto3` to recognize them as S3
credentials, but we do not want to make changes directly to
`~/.config/rclone/rclone.conf`, as it is used by other programs.
Instead, use the `sed` utility to read the contents of the configuration file,
make the necessary changes, and write the modified contents to a new file,
for example `~/.boto3_credentials`. This can all be done with the following command.

    ```bash
    sed -E 's/^(access|secret)/aws_\1/g' ~/.config/rclone/rclone.conf > ~/.boto3_credentials
    ```

After completing these steps, your S3 credentials for using `boto3` are stored
under project-specific S3 profiles in the file you created in step 2. The profile names
have the format `s3allas-<project>`, e.g. `s3allas-project_2001234`.
You can now use these credentials to
[create a `boto3` resource](#create-boto3-resource).

## `boto3` usage

### Create `boto3` resource

S3 credentials configured only for one project:
```python
# Create resource using credentials from the default location
import boto3

s3_resource = boto3.resource('s3', endpoint_url='https://a3s.fi')
```
S3 credentials configured for multiple projects:
```python
# Create resource using credentials from a profile
import boto3
import os

s3_credentials = '<credentials-file>'   # e.g. '~/.boto3_credentials'
s3_profile = 's3allas-<project>'        # e.g. 's3allas-project_2001234'

os.environ['AWS_SHARED_CREDENTIALS_FILE'] = s3_credentials
s3_session = boto3.Session(profile_name=s3_profile)
s3_resource = s3_session.resource('s3', endpoint_url='https://a3s.fi')
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

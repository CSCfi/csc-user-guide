# Using Allas with Python over the S3 protocol

You can use the [AWS SDK for Python](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
(`boto3`) to access Allas over the [S3 protocol](../introduction.md#protocols).
`boto3` is a Python library developed for working with
[Amazon S3 storage](https://aws.amazon.com/s3/) and other AWS services.

## General workflow for data analysis

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
(general data analysis)
and
[GDAL-based Python libraries](https://github.com/csc-training/geocomputing/blob/master/python/allas/working_with_allas_from_Python_S3.py)
(geospatial data analysis).

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
without having to set `AWS_SHARED_CREDENTIALS_FILE`,
make sure that you also copy the parent directory as in the example
below.

```bash
# Copy the credentials file and its parent directory to your home directory
scp -r <username>@<hostname>.csc.fi:~/.aws $HOME
```

### Credentials for accessing multiple projects

Using `allas-conf --mode s3cmd` is very straightforward,
but it overwrites the credentials file when it is run.
If you wish to use `boto3` with multiple projects,
it is recommended to store your credentials
[under different S3 profiles](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html#shared-credentials-file).
This is best done using the 
[Cloud storage configuration](../../../computing/webinterface/file-browser.md#accessing-allas-and-lumi-o)
app in the Puhti or Mahti web interface.

1. Configure connections, or _remotes_, for the projects whose Allas storage you wish
to access. The configurations will be stored in `~/.config/rclone/rclone.conf` on
the supercomputer whose web interface you used for generating them.

2. Copy the contents of `~/.config/rclone/rclone.conf` to a new file,
for example `~/.config/s3allas/credentials`.

    ```bash
    cp ~/.config/rclone/rclone.conf ~/.config/s3allas/credentials
    ```

3. The arguments that contain the access key and secret key need to be prefixed
   with `aws_` for `boto3` to recognize them as S3 credentials.

    ```bash
    sed --in-place --regexp-extended 's/^(access|secret)/aws_\1/g' ~/.config/s3allas/credentials
    ```

4. If you wish to use `boto3` on a personal workstation, copy the file you
created in step 2 to your workstation using e.g. `scp`.

5. Credentials that are configured using *Cloud storage configuration*
are stored under project-specific S3 profiles whose names have the format
`s3allas-project_2001234`. To find out how to use S3 profiles to access the
Allas storage of different projects, see the instructions on
[creating a `boto3` resource](#create-boto3-resource).

## `boto3` usage

### Create `boto3` resource

```python
# Basic usage (credentials configured only for one project)
import boto3

s3_resource = boto3.resource('s3', endpoint_url='https://a3s.fi')
```

```python
# Usage with S3 profiles (credentials configured for multiple projects)
import boto3
import os

s3_credentials = '<credentials-file>'   # e.g. '~/.config/s3allas/credentials'
s3_profile = '<profile-name>'           # e.g. 's3allas-project_2001234'

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

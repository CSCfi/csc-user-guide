# Using Allas with S3 using Python boto3 library

[boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) is a Python library for working S3 storage and other AWS services. `boto3` works with Allas over [S3 protocol](../introduction.md#protocols). 

This page shows how to:

* Install `boto3`
* Set up S3 credentials
* Create `boto3 client` 
* List buckets and objects 
* Create a bucket
* Upload and download an object 
* Remove buckets and objects 

Note, that S3 and SWIFT APIs should not be mixed.

## Installation

`boto3` is available for Python 3.8 and higher and can be [installed](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#installation) with `pip` or `conda`.

```
pip install boto3
```

### `boto3` in CSC supercomputers
Some existing [Python modules](../../../apps/python.md#using-science-area-specific-python-modules) might have `boto3` pre-installed, for example [geoconda](../../../apps/geoconda.md). 
To other modules, it is possible to add `boto3` with [pip](../../../apps/python.md#installing-python-packages-to-existing-modules).


## Configuring S3 credentials

If you have not used Allas with S3 before, then first [create S3 credentials](s3_client.md#getting-started-with-s3cmd). The credentials are saved to `~/.aws/credentials` file, so they need to be set only once from a new computer or when changing project. The credential file can be also copied from one computer to another.

In CSC supercomptuers [`allas` module](s3_client.md#configuring-s3-connection-in-supercomputers) can be used with `allas-conf --mode s3cmd` to configure the credentials.

## `boto3` usage

### Create boto3 resource
For all next steps, first boto3 resource must be created.

```python
import boto3
s3_resource = boto3.resource('s3', endpoint_url='https://a3s.fi')
```

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

And all objects belonging to a bucket:
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

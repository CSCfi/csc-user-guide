# Using Allas with S3 using Python boto3 library

[boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) is a Python library for working S3 storage and other AWS services.

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

### boto3 in CSC supercomputers
Some existing [Python modules](../../../apps/python.md#using-science-area-specific-python-modules) might have `boto3` pre-installed, for example [geoconda](../../../apps/geoconda.md). 
To other modules, it is possible to add `boto3` with [pip](../../../python.md#installing-python-packages-to-existing-modules).


## Set up S3 credentials

If you have not used Allas with S3 before, then first [create S3 credentials](s3_client.md#getting-started-with-s3cmd). The credentials are saved to a file, so they need to be set only once from a new computer or when changing project.

## Create boto3 client
For all next steps, first boto3 cilent is needed.

```python
s3_client = boto3.client("s3", endpoint_url='https://a3s.fi')

TODO. or resource?
```

## Create a bucket

Create a new bucket using the following script:

```python
response = s3_client.create_bucket(Bucket='examplebucket')
```

## List buckets and objects

List all buckets belonging to a project:
```python
response = client.list_buckets()
for bucket in response['Buckets']:
    print(bucket['Name'])
```

And all objects belonging to a bucket:
```python
response = s3_client.list_objects_v2(Bucket='examplebucket')
files = response.get("Contents")
for file in files:
    print(f"file_name: {file['Key']}, size: {file['Size']}")
```

## Download an object

Download an object:
```python
with open("local_file.txt", 'wb') as f:
    s3_client.download_fileobj('examplebucket', 'object_name_in_allas.txt', f)
```

## Upload an object

Upload a small file called `my_snake.txt` to the bucket `snakebucket`:

```python
s3.upload_fileobj('local_file.txt', 'examplebucket', 'object_name_in_allas.txt')
```

## Remove buckets and objects

Delete all objects from a bucket:

```python
bucket = s3_client.Bucket('my-bucket')
bucket.objects.all().delete()

# First list all files in folder
response = s3_client.list_objects_v2(Bucket='examplebucket')

files_in_folder = response["Contents"]
files_to_delete = []
# We will create Key array to pass to delete_objects function
for f in files_in_folder:
    files_to_delete.append({"Key": f["Key"]})

# This will delete all files in a folder
response = s3_client.delete_objects(
    Bucket=bucket_name, Delete={"Objects": files_to_delete}
)
```

Delete a bucket, must be empty:
```python
response = client.delete_bucket(Bucket='examplebucket')
```

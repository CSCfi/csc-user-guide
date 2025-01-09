# Setting up a pipeline for images

## Objectives

* Get familiarity on how to use multiple cloud services together.
* Get familiarity on how to use cloud services using their command-line interfaces.

The tutorial focuses on the following services:

* Allas
* cPouta
* Pukki

## Introduction

We want to set up a simple pipeline which transforms the images that are given in input to it.

![image-pipeline-diagram](../../img/image-pipeline-diagram.png)

We use Allas as the place where to upload our images in input.
The pipeline uploads its transformed images to Allas too.
A virtual machine in cPouta takes care of downloading, transforming, and re-uploading the images received in input.
Once it has transformed an image, the virtual machine also logs the event to a database hosted in Pukki.

For the sake of this tutorial, the transformed image simply corresponds to the input image whose colors are inverted.

## Step 1: creating buckets in Allas

To create buckets in Allas, we need to have a working command-line interface for it.
If we haven't set up such interface before on our workstation, we follow the [instructions on how to install and configure s3cmd](https://docs.csc.fi/data/Allas/using_allas/s3_client/#getting-started-with-s3cmd).

We can test the correct functioning of the command-line interface by simply listing all the buckets currently in our project. An example of the output of the command follows:
```
$ s3cmd ls
2021-07-14 15:14  s3://bucket1
2020-01-14 17:40  s3://bucket2
...
```
Please note that the list can also be empty, if we haven't created any bucket in our project before.

We create the input and the output buckets for our pipeline using the following commands:
```
$ s3cmd mb s3://input_bucket
Bucket 's3://input_bucket/' created
$ s3cmd mb s3://output_bucket
Bucket 's3://output_bucket/' created
```

!!! warning
    Bucket names must be unique.
    If another user has already selected the same name, bucket creation command will fail:
    ```
    $ s3cmd mb s3://input_bucket
    ERROR: Bucket 'input_bucket' already exists
    ERROR: S3 error: 409 (BucketAlreadyExists)
    ```
    In such case, we can just select a different name and retry the command.

In the rest of the tutorial, we assume:

* the name of the bucket used for uploading images to the pipeline is `input_bucket`
* the name of the bucket used by the pipeline to make available its outputs is `output_bucket`

## Step 2: creating database in Pukki

## Step 3: creating virtual machine in cPouta

## Step 4: configuring the virtual machine

## Step 5: testing the pipeline

## Conclusion

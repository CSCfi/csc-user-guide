# Common use cases

## Processing data in CSC supercomputers

The CSC supercomputers provide disk environments for working with large datasets. These storage areas are however not intended for storing data that is not actively used. For example in the _scratch_ area of Puhti the un-used files are automatically removed after 90 days. 

One of the main use cases of Allas is to store data while it is not actively used in the CSC supercomputers. When you start
working, you stage in the data from Allas. And when the data is no longer actively used, it can be staged out to Allas. 

In CSC supercomputers, connection to Allas can be established with commands:
```text
module load allas
allas-conf
```
After that you can:

**Copy data from Allas to a supercomputer (Puhti or Mahti) (stage in):** For downloading we recommend [a-get](./a_commands.md#a-get-retrieves-stored-data) 
```text
a-get bucket/object_name
```
or [rclone copy](./rclone.md):
```text
rclone copy allas:bucket/object_name ./
```

**Copy data from a Supercomputer to Allas (stage out):** For uploading we recommend [a-put](./a_commands.md#a-put-uploads-data-to-allas) 
```text
a-put filename
```
or [rclone copy](./rclone.md):
```test
rclone copy file.dat allas:/bucket_name 
```

!!! note
    Both a-put/a-get and rclone use Swift protocol on Allas. It is important not to mix Swift and S3, as these protocols are not fully mutually compatible.

## Sharing data

Sharing data, e.g. datasets or research results, is easy in the object storage. You can share these either with a limited audience, e.g. other projects, or allow access for everybody by making the data public.

The data can be accessed and shared in a variety of ways:

* **Private – default:** By default, if you do not specify anything else, the contents of buckets can only be accessed by authenticated members of your project. **Private**/**Public** settings can be managed with:
	* [Web client](./web_client.md#view-objects-via-the-internet)
	* [S3 client](./s3_client.md#s3cmd-and-public-objects)

* **Access control lists:** Access control lists (ACLs) work on buckets, not objects. With ACLs, you can share your data in a limited manner to other projects. You can e.g. grant a collaboration project authenticated read access to your datasets.

 * **Public:** You can also have ACLs granting public read access to data, which is useful e.g. for sharing public scientific results or public datasets.

## Static web content

A common way to use the object storage is storing static web content, such as images, videos, audio, pdfs or other downloadable content, and adding links to it on a web page, which can run either inside Allas or somewhere else. [An example](https://a3s.fi/my_fishbucket/my_fish)

Uploading data to Allas can be done with any of the following clients: [web client](./web_client.md#upload-an-object), [a-commands](./a_commands.md#a-put-uploads-data-to-allas), [Swift](./swift_client.md#create-buckets-and-upload-objects) or [S3](./s3_client.md#create-buckets-and-upload-objects).

## Storing data for distributed use

There are several cases where you need to access data in several locations. In these cases, the practice of staging in the data to individual servers or computers from the object storage can be used instead of a shared file storage.

## Accessing the same data via multiple CSC platforms

Since the data in the object storage is available anywhere, you can access the data via both the CSC clusters and cloud services. This makes the object storage a good place to store data as well as intermediate and final results in cases where the workflow requires the use of e.g. both Allas and Puhti.

## Collecting data from different sources

It is easy to push data to the object storage from several different sources. This data can then later be processed as needed.

For example, several data collectors may push data to be processed, e.g. scientific instruments, meters, or software that harvests social media streams for scientific analysis. They can push their data into the object storage, and later virtual machines and computing jobs on Puhti can process the data.
 
## Self-service backups of data

The object storage is also often used as a location for storing backups. It is a convenient place to push copies of database dumps.

[allas-backup](./a_backup.md) is a part of *a-commands*. It works as a tool for creating backup copies of files in Allas. **Please note:** allas-backup is not a real backup service. It only copies the data to another bucket in Allas which can be easily removed or overwrited by any authenticated user.

## Files larger than 5 GB

Files larger than 5 GB must be divided into smaller segments before uploading. 

* The *a-command a-put* splits large files automatically: [a-put](./a_commands.md#a-put-uploads-data-to-allas)

* Using _Swift_, you can use the _Static Large Object_: [swift with large files](./swift_client.md#files-larger-than-5-gb)

* _s3cmd_ splits large files automatically: [s3cmd put](./s3_client.md#create-buckets-and-upload-objects)

## Viewing

If you are using the _s3cmd client_, check your project's object storage usage:
```bash
s3cmd du -H
```

If you use the _Swift client_:
```bash 
swift stat
```

Display how much space a bucket has used:
```bash
swift stat $bucketname
```

Please contact servicedesk@csc.fi if you have questions.

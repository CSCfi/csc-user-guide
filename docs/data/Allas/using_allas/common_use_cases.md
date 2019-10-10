
# Common use cases


## Processing data in HPC systems

To use the computing environment in Taito or Puhti, use the open source parallel file system [Lustre](http://lustre.org/). In these file systems, files are automatically removed after 90 days. One of the main use cases of Allas is to store data that is not in active in the HPC systems. Before beginning, stage the data in. When the data is no longer actively used, it can be staged out. 

* **Copying data from the object storage to Lustre (stage-in):** Copy the data to the parallel file system Lustre before computing. We recommend [a_get](./a_commands.md#a-get-retrieves-stored-data) or [swift download](./swift_client.md#download-objects-and-buckets) for downloading objects from Allas.

* **Copying data from Lustre to the object storage (stage-out):** After computing, copy the files to Allas. We recommend [a_put](./a_commands.md#a-put-uploads-data-to-allas) or [swift upload](./swift_client.md#create-buckets-and-upload-objects) for uploading the data to Allas.


!!! note
    We recommend using the Swift protocol on Allas. It is important not to mix Swift and S3, as these protocols are not fully mutually compatible.


## Sharing data

Sharing data, e.g. datasets or research results, is easy in the object storage. You can share these either with a limited audience, e.g. other projects, or allow access for everybody by making the data public.
 
The data can be accessed and shared in a variety of ways:
 
* **Private - default:** By default, if not specified otherwise, the contents of buckets can only be accessed by authenticated members of the project. **Private**/**Public** settings can be managed using
	* [Web client](./web_client.md#view-objects-via-internet)
	* [Swift client](./swift_client.md#temp-urls)
	* [S3 client](./s3_client.md#s3cmd-and-public-objects)
 
* **Access Control Lists:** Access control lists (ACLs) work on buckets, not objects. With ACLs, you can share your data in a limited way to other projects. You can e.g. grant a collaboration project authenticated read access to your datasets.

 * **Public:** You can also have ACLs granting public read access to the data, which is useful for e.g. sharing public scientific results or public datasets.
 
* **Temp URLs:** A temp URL is a unique URL for accessing an object. These URLs are time-limited, and the duration can be determined. Anyone can access the object with the URL, but the URL is not feasible to guess. This is a good way to somewhat securely share data to a limited audience that does not need to have personal Allas accounts. Temp URLs are created per object, not per bucket. You can create temp URLs with [Swift](./swift_client.md#temp-urls) or [S3](./s3_client.md#temporary-urls).

## Static web content

A common way to use the object storage is storing static web content, such as images, videos, audio, pdfs or other downloadable content, and adding links to it on a web page, which can run either inside Allas or somewhere else. [An example](https://object.pouta.csc.fi/my_fishbucket/my_fish)

Uploading data to Allas can be done with any of the following clients: [web client](./web_client.md#upload-an-object), [a_commands](./a_commands.md#a-put-uploads-data-to-allas), [Swift](./swift_client.md#create-buckets-and-upload-objects) or [S3](./s3_client.md#create-buckets-and-upload-objects).

## Storing data for distributed use

There are several cases where you need to access data in several locations. In these cases, the practice of staging in the data to individual servers or computers from the object storage can be used instead of a shared file storage.

## Accessing the same data via multiple CSC platforms

Since the data in the object storage is available anywhere, you can access the data via both the CSC clusters and cloud services. This makes the object storage a good place to store data as well as intermediate and final results in cases where the workflow requires the use of e.g. both Allas and Puhti.

## Collecting data from different sources

It is easy to push data to the object storage from several different sources. This data can then later be processed as needed.

For example, several data collectors may push data to be processed, e.g. scientific instruments, meters, or software that harvests social media streams for scientific analysis. They can push their data into the object storage, and later virtual machines and computing jobs on Puhti can process the data.
 
## Self-service backups of data

The object storage is also often used as a location for storing backups. It is a convenient place to push copies of database dumps.

[a_backup](./a_backup.md) is a part of *a_commands*. It works as a tool for creating backup copies of files to Allas. **Please note:** a_backup is not a real backup service. It only copies the data to another bucket in Allas which can be easily removed or overwrited by any authenticated user.

## Files larger than 5 GB

Files larger than 5 GB must be divided into smaller segments before uploading. 

* *a_command a_put* splits large files automatically: [a_put](./a_commands.md#a-put-uploads-data-to-allas)

* Using _Swift_, you can use _Static Large Object_: [swift with large files](./swift_client.md#files-larger-than-5-gb)

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

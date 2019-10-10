
# Common Use Cases

&nbsp;


## Processing data on HPC systems

To use the computing environment in Taito or Puhti, you need to use the open-source, parallel file system [Lustre](http://lustre.org/). On these filesystems your files will be automatically removed after 90 days. One main use case of Allas is to store data that is not in active in the HPC systems. Before you start to work on it you need to stage the data in, and after the data is not in active use you can stage it out. 



* **Copying data from object storage to Lustre (stage-in):** You need to copy data to the parallel file system Lustre before computing. To download objects from Allas we recommend [a_get](./a_commands.md#a-get-retrieves-the-stored-data) or [swift download](./swift_client.md#download-objects-and-buckets).

* **Copying data from Lustre to object storage (stage-out):** After computation you should copy the files to Allas. To upload the data to Allas we recommend [a_put](./a_commands.md#a-put-uploads-data-to-allas) or [swift upload](./swift_client.md#create-buckets-and-upload-objects). 

!!! note
    We recommend using the Swift protocol on Allas. It is important not to mix the usage of Swift and S3, these protocols are not completely compatitable.




## Sharing data

With object storage you can easily share data, e.g. datasets or research results. You can share these either with limited audience, for example other projects, or open up access to everybody by making the data public.
 
The data can be accessed and shared in several different ways:
 
* **Private - default:** By default, if you do not specify anything else, contents of buckets can only be accessed by authenticated members of your project. **Private**/**Public** settings can be managed with:
	* [Web client](./web_client.md#view-objects-via-the-internet)
	* [Swift client](./swift_client.md#temp-urls)
	* [S3 client](./s3_client.md#s3cmd-and-public-objects)
 

* **Access Control Lists:** Access Control Lists (ACLs) work on buckets, not on objects. With ACLs you can share your data in a limited fashion to other projects. You can e.g. enable authenticated read access to your datasets to a collaboration project.

 
* **Public:** You can also have ACLs granting public read access to the data, which is useful for e.g. sharing public scientific results or public datasets.

 
* **Temp URLs:** A temp URL is a unique URL to access an object. These URLs are time-limited and the duration can be determined. Anyone with the URL can access the object, but the URL is not feasible to just guess. This is a good way to somewhat securely share data to a limited audience, who do not need to have their own Allas accounts. Temp URLs are created per object, not per bucket. You can create temp URLs with [Swift](./swift_client.md#temp-urls) or [S3](./s3_client.md#temporary-urls).

&nbsp;


 
## Static web content

A common way to use object storage is to store static web content there, such as images, videos, audio, pdfs or downloadable content, and just add link to it from your web page, which can run either inside Allas or somewhere else. [Here is an example](https://object.pouta.csc.fi/my_fishbucket/my_fish)

Uploading data to Allas can be done with any of the clients: [Web client](./web_client.md#upload-an-object), [a_commands](./a_commands.md#a-put-uploads-data-to-allas), [Swift client](./swift_client.md#create-buckets-and-upload-objects) or [S3 client](./s3_client.md#create-buckets-and-upload-objects).
 
&nbsp;


## Storing data for distributed use

There are several cases where you need to access to common data from several locations. In these cases, the practice of staging in data to individual servers or computers from the object storage can be used instead of shared file storage.

&nbsp;


## Accessing the same data from multiple CSC platforms

Since the data in object storage is available from anywhere, you can access the data from both the CSC clusters and from the cloud services. This makes the object storage a good place to store data and intermediate and final results in cases where your workflow requires the use of, for example, both Allas and Puhti.

&nbsp;


## Collecting data from different sources

It is easy to push data to object storage from several different sources. This data can then later be processed as needed.


An example of this could be several data collectors pushing data to be processed. These could be, for example, scientific instruments, meters or software which harvest social media streams for scientific analysis. These can push their data into object storage, and later virtual machines or compute jobs on Puhti can process this data.
 
&nbsp;


## Self-service backups of data

Object storage is also often used as a location where you store backups. It is a convenient place to push copies of such as database dumps.

[a_backup](./a_backup.md) is part of the *a_commands* and it works as a tool for creating backup copies of files to Allas. **Please note:** a_backup is not a real backup service. It only copies the data in to another bucket in Allas which can be easily removed or overwrited by any authenticated user.

&nbsp;


## Files larger than 5 GB

Files larger than 5 GB must be divided into smaller segments before uploading. 

* *a_command a_put* splits large files automatically: [a_put](./a_commands.md#a-put-uploads-data-to-allas)

* With _Swift_ you can make use of _Static Large Object_: [swift with large files](./swift_client.md#files-larger-than-5-gb)

* _s3cmd_ splits large files automatically: [s3cmd put](./s3_client.md#create-buckets-and-upload-objects)

&nbsp;


## Viewing usage

If you are using _s3cmd client_, you can check your project's object storage usage with command:
```bash
s3cmd du -H
```

In case you use _Swift client_, you can check the usage with command:
```bash 
swift stat
```

To see how much space a bucket has used, use command:
```bash
swift stat $bucketname
```

Please contact servicedesk@csc.fi if you have questions.

&nbsp;

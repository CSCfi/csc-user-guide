# Common use cases

## Storage for CSC computing projects

The CSC supercomputers provide disk environments for working with large datasets. These storage areas are however not intended for storing data that is not actively used. The inactive data should be moved to Allas. See [Allas HPC tutorial](allas-hpc.md) for further information.

## Sharing data

Sharing data, e.g. datasets or research results, is easy in the object storage. You can share these either with a limited audience, e.g. other projects, or allow access for everybody by making the data public.

The data can be accessed and shared in a variety of ways:

* **Private – default:** By default, if you do not specify anything else, the contents of buckets can only be accessed by authenticated members of your project. **Private**/**Public** settings can be managed with:

    * [swift client](./swift_client.md#giving-another-project-read-and-write-access-to-a-bucket) Use this for buckets created/used by `a-put/a-get` or `rclone`.
    * [Pouta web UI](./web_client.md#view-objects-via-the-internet)
    * [S3 client](./s3_client.md#s3cmd-and-public-objects)

* **Access control lists:** Access control lists (ACLs) work on buckets, not objects. With ACLs, you can share your data in a limited manner to other projects. You can e.g. grant a collaboration project authenticated read access to your datasets.

 * **Temporary signed links** can be created with [s3cmd](./s3_client.md#publishing-objects-temporarily-with-signed-urls) . This kind of links can be used in cases where the data needs to be accessed over the internet without credentials, but is not supposed to remain publicly accessible.
 
 * **Public:** You can also have ACLs granting public read access to data, which is useful e.g. for permanently sharing public scientific results or public datasets.

## Publishing static web content

A common way to use the object storage is storing static web content, such as images, videos, audio, pdfs or other downloadable content, and adding links to it on a web page, which can run either inside Allas or somewhere else, [like this example](https://a3s.fi/my_fishbucket/my_fish).

To publish a some content, first move it with a [Allas client](accessing_allas.md) to Allas and then [make the files public](#sharing-data).


## Storing data for distributed use

There are several cases where you need to access data in several locations. In these cases, the practice of staging in the data to individual servers or computers from the object storage can be used instead of a shared file storage.

## Accessing the same data via multiple CSC platforms

Since the data in the object storage is available anywhere, you can access the data via both the CSC supercomputers and cloud services. This makes the object storage a good place to store data as well as intermediate and final results in cases where the workflow requires the use of e.g. both cPouta and Puhti.

## Collecting data from different sources

It is easy to push data to the object storage from several different sources. This data can then later be processed as needed.

For example, several data collectors may push data to be processed, e.g. scientific instruments, meters, or software that harvests social media streams for scientific analysis. They can push their data into the object storage, and later virtual machines and computing jobs on Puhti can process the data.
 
## Self-service backups of data

The object storage is also often used as a location for storing backups. It is a convenient place to push copies of database dumps.

[allas-backup](./a_backup.md) is a part of *a-commands*. It works as a tool for creating backup copies of files in Allas.
!!! note 
    Allas-backup is not a real backup service.
    It only copies the data to another bucket in Allas which can 
    be easily removed or overwrited by any authenticated user.

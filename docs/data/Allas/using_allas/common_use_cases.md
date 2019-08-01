
# Common Use Cases

&nbsp;


## Processing data

To use the computing environment, you need to use the open-source, parallel file system [Lustre](http://lustre.org/){:target="_blank"}.

* **Copying data from object storage to Lustre (stage-in):** You need to copy data to the parallel file system Lustre before computing. To download objects from Allas we recommend a_command [a_get](./a_commands.md#a_get-retrieves-the-stored-data){:target="_blank"}, [swift download](./swift_client.md#download-objects-and-buckets){:target="_blank"} or [s3cmd get](./s3_client.md#download-objects){:target="_blank"}.

* **Copying data from Lustre to object storage (stage-out):** After computation you should copy the files to Allas. To upload the data to Allas we recommend a_command [a_put](./a_commands.md#a_put-uploads-data-to-allas){:target="_blank"}, [swift upload](./swift_client.md#create-buckets-and-upload-objects){:target="_blank"} or [s3cmd put](./s3_client.md#create-buckets-and-upload-objects){:target="_blank"}. **Please note:** your files will be automatically removed from Lustre scratch if they have not been touched for 90 days.

**Please note:** As discussed in the [Protocols section](../accessing_allas.md#protocols){:target="_blank"}, we recommend to use just one protocol - do not mix Swift and S3.

Please take a look also at [Using Allas in Supercomputers](#using-allas-in-supercomputers).

&nbsp;


## Sharing data

With object storage you can easily share data, e.g. datasets or research results. You can share these with other projects or open up access to everybody.
 
The data can be accessed and shared in several different ways:
 
* **Private - default:** By default, if you do not specify anything else, contents of buckets can only be accessed by authenticated members of your project. **Private**/**Public** settings can be managed with:
	* [Web client](./web_client.md#web_public){:target="_blank"}
	* [Swift client](./swift_client.md#temp_urls){:target="_blank"}
	* [S3 client](./s3_client.md#s3cmd_public_objects){:target="_blank"}
 

* **Access Control Lists:** Access Control Lists (ACLs) work on buckets, not on objects. With ACLs you can share your data in a limited fashion to other projects. You can e.g. enable authenticated read access to your datasets to a collaboration project.

 
* **Public:** You can also have ACLs granting public read access to the data, which is useful for e.g. sharing public scientific results or public datasets.

 
* **Temp URLs:** A temp URL is a unique URL to access an object. These URLs can be time-limited. Anyone with the URL can access the object, but the URL is not feasible to just guess. This is a good way to somewhat securely share data to a limited audience, who do not need to have their own Allas accounts. Temp URLs are created per object, not per bucket. [Temp URLs](./swift_client.md#temp-urls){:target="_blank"} are a feature of Swift. In S3 the corresponding feature is called *a Signed URL*. See the differences between using the [Swift and S3 protocols](../accessing_allas.md#protocols){:target="_blank"}.

&nbsp;


## Using Allas in Supercomputers

The first step is to authenticate to a project in Allas. In Taito and Puhti you can do the authentication with command:
```bash
    [user@puhti ~] source /appl/opt/allas_conf
```

The command above generates and stores authentication information into shell variables OS_AUTH_TOKEN and OS_STORAGE_URL. The authentication is valid for max 3 hours.  

**Please note:** The environment variables are available only for that login session, so if you log into Puhti in another session, you need to authenticate again in there to use Allas.

You can find some guidance for using Allas from Puhti and Taito below:

 * **Easy tools for basic usage:** [Quick and safe: a_put, a_get, a_find](./a_commands.md){:target="_blank"}


 * **Advanced functions with rclone:** [Advanced tool: rclone](./rclone.md){:target="_blank"}


 * **s3cmd and persistent Allas connections:** [s3cmd](./s3cmd.md){:target="_blank"}

&nbsp;

 
## Static web content

A common way to use object storage is to store static web content there, such as images, videos, audio, pdfs or downloadable content, and just add links to it from your web page, which can run either inside Allas or somewhere else. [Here is an example](https://object.pouta.csc.fi/my_fishbucket/my_fish){:target="_blank"}

Uploading data to Allas can be done with any of the clients: [Web client](./web_client.md#adding-an-object-to-a-bucket){:target="_blank"}, [Swift client](./swift_client.md#create-buckets-and-upload-objects){:target="_blank"} or [S3 client](./s3_client.md#create-buckets-and-upload-objects){:target="_blank"}.
 
&nbsp;


## Storing data for distributed use

There are several cases where you need to access to common data from several locations. In these cases, the practice of staging in data to individual servers or computers from the object storage can be used instead of shared file storage.

&nbsp;


## Accessing the same data from multiple CSC platforms

Since the data in object storage is available from anywhere, you can access the data from both the CSC clusters and from the cloud services. This makes the object storage a good place to store data and intermediate and final results in cases where your workflow requires the use of, for example, both Allas and Taito.

&nbsp;


## Collecting data from different sources

It is easy to push data to object storage from several different sources. This data can then later be processed as needed.


An example of this is several data collectors pushing data to be processed. These could be, for example, scientific instruments, meters or software which harvest social media streams for scientific analysis. These can push their data into object store, and later virtual machines or compute jobs on Puhti can process this data.
 
&nbsp;


## Self-service backups of data

Object storage is also often used as a location where you store backups. It is a convenient place to push copies of such as database dumps.

[a_backup](./a_backup.md){:target="_blank"} is a tool for creating backup copies of files to Allas. **Please note:** <i>a_backup</i> is not a real backup service. It only copies the data to one bucket in Allas which can be removed by any authenticated user.

&nbsp;


## Viewing usage

If you are using _s3cmd client_, you can check your project's Object Storage usage with command:
```bash
$ s3cmd du -H
```

In the case you use _Swift client_, you can check it with command:
```bash 
$ swift stat
```

To see how much space a bucket has used
```bash
$ swift stat $bucketname
```

Please contact servicedesk@csc.fi if you have questions.

&nbsp;

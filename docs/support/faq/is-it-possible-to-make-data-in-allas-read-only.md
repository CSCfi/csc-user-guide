# Is it possible to make data in Allas read-only?

 ** &#8226; Inside a project**  
Inside a project there is currently no _read-only_ mode in Allas. Each project member has full access to the data, which causes a risk: one can accidentally overwrite or delete data.


** &#8226; Between projects**  
You can give another project read-only access to your bucket with [Swift](../../data/Allas/using_allas/swift_client.md#giving-another-project-read-and-write-access-to-a-bucket){target="_blank"} or
[s3cmd](../../data/Allas/using_allas/s3_client.md#giving-another-project-read-access-to-a-bucket){target="_blank"}.


** &#8226; Sharing URL**  
In addition, it is possible to make a bucket public, which makes the content available for viewing ('_read-only_') via URLs. The URL to an object in a public bucket is in form of <i>object.pouta.csc.fi/bucket_name/object_name</i> and it can be shared only to wanted audience.

Here is guidance for setting the bucket public with:

* [Web client](../../data/Allas/using_allas/web_client.md#viewing-objects-via-internet){target="_blank"}
* [Swift client](../../data/Allas/using_allas/swift_client.md#temp-urls){target="_blank"}
* [S3 client](../../data/Allas/using_allas/s3_client.md#s3cmd-and-public-objects){target="_blank"}
* [a_commands](../../data/Allas/using_allas/a_commands.md#a_publish){target="_blank"}

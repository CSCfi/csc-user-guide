# Is it possible to make data in Allas read-only?

There is currently no _read-only_ mode in Allas. Each project member has full access to the data, which causes a risk: one can accidentally overwrite or delete data.

However, it is possible to make your bucket public, which makes the content available for viewing ('read-only') via URLs. The URL to an object in a public bucket is in form of <i>object.pouta.csc.fi/bucket_name/object_name</i>.

Here is guidance for setting the bucket public with:

* [Web client](../../data/Allas/using_allas/web_client.md#viewing-objects-via-internet){target="_blank"}
* [Swift client](../../data/Allas/using_allas/swift_client.md#temp-urls){target="_blank"}
* [S3 client](../../data/Allas/using_allas/s3_client.md#s3cmd-and-public-objects){target="_blank"}
* [a_commands](../../data/Allas/using_allas/a_commands.md#a_publish){target="_blank"}

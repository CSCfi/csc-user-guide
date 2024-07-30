# Is it possible to make data in Allas read-only?

## Inside a project

Inside a project there is currently **no** read-only mode in Allas. Each
project member has full access to the data, which causes a risk: any project
member can accidentally overwrite or delete data.

## Between projects

You can give another project read-only access to your bucket using
[Swift](../../data/Allas/using_allas/swift_client.md#giving-another-project-read-and-write-access-to-a-bucket)
or
[S3cmd](../../data/Allas/using_allas/s3_client.md#giving-another-project-read-access-to-a-bucket).

## Sharing URL

In addition, it is possible to make a bucket public, which makes the content
available for viewing ("read-only") via URLs. The URL to an object in a
public bucket is of the form `https://<bucket_name>.a3s.fi/<object_name>` or
`https://a3s.fi/swift/v1/AUTH_<project_id>/<bucket_name>/<object_name>` where
`<project_id>` is the identifier of your computing project in
[UUID](../../data/Allas/using_allas/s3_client.md#giving-another-project-read-access-to-a-bucket)
format.

## Additional guidance for making buckets public

* [Web client](../../data/Allas/using_allas/web_client.md#view-objects-via-the-internet)
* [Swift client](../../data/Allas/using_allas/swift_client.md#giving-another-project-read-and-write-access-to-a-bucket)
* [S3 client](../../data/Allas/using_allas/s3_client.md#s3cmd-and-public-objects)
* [a-commands](../../data/Allas/using_allas/a_commands.md#a-publish)

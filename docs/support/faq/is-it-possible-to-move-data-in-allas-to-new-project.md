# Is it possible to move data in Allas to new project?

In Allas, data movement between projects can be done by giving the receiving
project read or write access to the bucket containing the data. The other
project can then either read the data directly from the shared bucket or copy
the data to its own bucket.

You can give read access to a bucket for another project with
[S3cmd](../../data/Allas/using_allas/s3_client.md#giving-another-project-read-access-to-a-bucket),
or read and write access with
[Swift](../../data/Allas/using_allas/swift_client.md#giving-another-project-read-and-write-access-to-a-bucket).

Another way of moving data between projects could be to first download the data
from the original project and then uploading it to the new project. Please see
[instructions for moving data between Puhti and Allas](how-to-move-data-between-puhti-and-allas.md).
Instead of Puhti, you could also use another supercomputer, cloud environment,
virtual machine, or your local computer as the intermediate host. See
[Accessing Allas](../../data/Allas/accessing_allas.md).

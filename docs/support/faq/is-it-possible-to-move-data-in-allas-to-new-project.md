# Is it possible to move data in Allas to new project?

Data movement in Allas between projects happens by giving the other project read or write rights to the bucket including the data. The other project can then either read the data directly from the shared bucket or copy the data to own bucket.

You can give read rights to another project with s3cmd:

[s3cmd: Giving another project read access to a bucket](../../data/Allas/using_allas/s3_client.md#giving-another-project-read-access-to-a-bucket){:target="_blank"}

or with Swift:

[Swift: Giving another project read and write access to a bucket](../../data/Allas/using_allas/swift_client.md#giving-another-project-read-and-write-access-to-a-bucket){:target="_blank}


&nbsp;


Another way to move data between projects could be first downloading the data from the original project and then uploading it to the new project.
[Instructions](how-to-move-data-between-puhti-and-allas.md){:target="_blank"} for moving data between Puhti and Allas can be applied here.
Basically, first download the data from Allas to somewhere (for example: cloud environment, local computer, supercomputer (Puhti, Taito, Mahti) or virtual machine) and then upload it back to Allas in to another project. 
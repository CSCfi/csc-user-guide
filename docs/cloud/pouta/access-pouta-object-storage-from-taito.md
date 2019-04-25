## Accessing the object storage from Taito

!!! note
    This page is a placeholder as Allas will replace current pouta object storage.
    This info probably should not be on its own page, but be part of Allas
    documentation, and pouta documentation would have a link to it.

The usage will strongly depend on what  you will do with the data. The
"swift", "s3" and "s3cmd" command  line tools are already installed on
Taito.

|Command  line tool|Requirements|
|--- |--- |
|swift|Computing  project  `openrc.sh`  file downloaded <br> from https://pouta.csc.fi &  sourced to shell.|
|s3|Following environment variables present in environment: <br> S3_ACCESS_KEY_ID <br> S3_SECRET_ACCESS_KEY <br> S3_HOSTNAME<br> [(More info here)](persistent-volumes.md)
|s3cmd|Configuration  file .s3cfg populated [(more info here)][general].|


  
You can  use any  of the  commands to stage  in the  data you  need to
process  to the  project/scratch disk  and process  the data  like you
would process
any other data.  
  
For S3 use cases, you can also store the ec2 credentials with the job.
This is the  recommended way of accessing objects from  a compute job.
When you don't need the credentials anymore you can delete them with:

    $ openstack credential delete

Please note that ec2 credentials do not work against other Openstack
services.  
  
There is also the possibility to  create temp URLs for the objects you
need to  access, and use  those URLs to  access the data  from compute
jobs from Taito. One benefit of using temp URLs is that no credentials
need to be stored in Taito for retrieving the object.

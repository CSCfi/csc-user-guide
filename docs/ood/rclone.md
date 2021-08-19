# Rclone
The Rclone interactive app lets you access and transfer files between Puhti and Allas.
Currently, only the S3 protocol is supported in OOD for connecting to Allas.
To be able to access files on Allas you need to configure the authentication for Allas.
That can be done by executing the following commands in Puhti.
```
module load allas
allas-conf -m s3cmd
```

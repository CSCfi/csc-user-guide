# Rclone
The Rclone interactive app is used for accessing and transferring files between Puhti and Allas.

## Accessing Allas
Currently, only the S3 protocol is supported in OOD for connecting to Allas.
For more informations about the S3 protocol and limitations see the [docs](https://docs.csc.fi/data/Allas/using_allas/s3_client/).
To be able to access files on Allas you need to configure the authentication for Allas.
That can be done by executing the following commands in Puhti.
```
module load allas
allas-conf -m s3cmd
```
The project that will be accessed through Rclone can be selected with `allas-conf`.
To access another project's Allas you need to run `allas-conf` again and restart the Rclone interactive app.

## Using Rclone
The explorer tab in Rclone is used for accessing the files on Puhti and Allas.
The home directory, scratch and projappl for each project have been added as remotes in Rclone for easy access.
Allas is accessed using the remote `s3allas`.

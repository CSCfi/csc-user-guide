# Rclone
The Rclone interactive app is used for accessing and transferring files between Puhti and [Allas](../data/Allas).

## Accessing Allas
To access allas using Rclone you first have to generate the authentication token.
After filling in the app form you will see a command that you need to run in the shell to authenticate:
```
module load allas
allas-conf --store-token -p <project>
```
After you have generated the authentication token you can launch Rclone.  
It is recommended that you select the Swift protocol for connecting to Allas.
Note that the maximum time for Swift connections is 8 hours.  
To access another project's Allas you need to run `allas-conf` again and restart the Rclone interactive app.

## Using Rclone
The explorer tab in Rclone is used for accessing the files on Puhti and Allas.
The home directory, scratch and projappl for each project have been added as remotes in Rclone for easy access.
Allas is accessed using the remote `allas`, or `s3allas`, depending on the protocol selected.

# Is Pouta backed up?

Mostly not. The servers that control and manage the service are backed up so we can restore the service in case of failures. However all the places where users can store data including  Volumes, Images, Virtual machines and Ephemeral storage are not backed up. It's the users  responsibility to make backups of data as needed.

Some other CSC services have backup, so depending on the type and amount of data users can consider copying data elsewhere.

| Service              | Backup policy                                                                             | How to use                                           |
|----------------------|-------------------------------------------------------------------------------------------|------------------------------------------------------|
| HPC home directories | Varies. WRKDIR is not backed up. See the [computing environment user guide] for details. | [Instructions](how-to-access-home-wrkdir-projdir-from-epouta.md) |
| CSC Archive (IDA)    | Yes. This is a long term data archive service.                                           | [Sign up here](http://openscience.fi/ida)   |

[computing environment user guide](https://research.csc.fi/csc-guide) for details.



# Disk areas

In Puhti there are three main disk areas: **home**, **projappl** and
**scratch**. These directories have specific purpose and you should be
familiar with them before you start using Puhti.

|              | Default quota | Owner    | Environment variable | Path                                            | Cleaning      |
| ------------ | ------------- | -------- | -------------------- | ----------------------------------------------- | ------------- |
| **home**     | 10 GiB        | Personal | `$(HOME)`            | <small>`/home/<user-name>`</small>              | No            |
| **projappl** | 50 GiB        | Project  | Not available        | <small>`/projappl/project_<project_id>`</small> | No            |
| **scratch**  | 1 TiB         | Project  | Not available        | <small>`/scratch/project_<project_id>`</small>  | Yes - 90 days |



## Home directory

Each Puhti user has a home directory (`$HOME`) that can contain up to 10 GB of
data.

Home directory is the default directory into which you end up when you login
to Puhti. However, typically you should change to your projects *scratch*
directory when working with Puhti. This is because your
**home directory is not meant for data analysis or computing**. Instead, it is
meant just for storing configurations files and other small personal data. If
you fill up your home directory so that no new files can be created there, it
will cause many problems for your account.

Home directory is the only user specific directory in Puhti. Other directories
are project specific. If you are a member in several projects you have access
to several *scratch* or *projappl* directories, but still have just one home
directory.

!!! note
    Home directory is not automatically backed up by CSC (the same applies to
    all directories in Puhti), so if some data is accidentally deleted by the
    user, it can't be recovered.


## Scratch directory

Each project has 1 TB of scratch disk space in directory
`/scratch/<project_id>`.

This fast parallel scratch space is intended to be used as a temporary storage
space for the data that is used in Puhti. Scratch directory is not meant for
long term data storage and **files that have not been used for 90 days will
be automatically removed**.

## ProjAppl directory

Each project has also a 50 GB project application disk space in the directory
`/projappl/project_<project_id>`.

It is meant for storing applications you have compiled yourself, libraries
etc. that you share among the project. It is not a personal storage space, but
is shared with all the members of the project team.

It is not meant for running applications, use scratch instead for that
purpose.

## Using Scratch and ProjAppl directories

As the paths of the project specific directories is dependent on the project
ID, you must first find out the project number you want to use. You can check
the project names from [MyCSC portal](https://my.csc.fi).

To get an overview of your directories in Puhti, run command:
```text
csc-workspaces
```
For example, if you are member in two projects: *project_2002291*
and *project_3587167*, then you have access to their scratch directories:
```text
/scratch/project_2002291
/scratch/project_3587167
```
Moving to the scratch directory of project_2002291 is done with the command:
```text
cd /scratch/project_2002291
```
Please note that not all CSC projects do have Puhti access so you won't
necessary find a *scratch* or *projappl* directory for all your CSC projects.

If you are mostly using just one project in Puhti, you can set the
environment variables $SCRATCH and $PROJAPPL to point to the *scratch* and
*projappl* directories of a CSC project. This setting can be done with
command:
<pre>
csc-workspaces set <i>project_ID</i>
</pre>

Scratch and ProjAppl directories are shared by **all the members of the
project**. Also all new files and directories are fully accessible for other
group members (including read, write and execution permissions). If you want
to restrict access from your group members, you can reset the permissions with
*chmod* command.

For example, to set read-only permissions for your group members for directory
*my_directory*, you can use command:
```text
chmod -R g-w my_directory
```

As mentioned earlier, scratch directory is intended for only processing data.
Any data that should be preserved for a longer time should be copied to the
Allas storage server. Instructions for backing up files from Puhti to Allas
will appear here, once the Allas storage service becomes available.


## Increasing Quotas


The size of the scratch directory can be increased, but only if the
analysis task requires that all the data is simultaneously available
on the disk environment of Puhti. In these cases, send a request to
*servicedesk@csc.fi*.  In the request, please indicate the project,
storage size needed, purpose and duration of the scratch quota
extension. In the future, the process for increase quotas will be
improved.

Data that is not under active computing should be stored in the  Allas
storage service.

Note that the extended scratch quota consumes your CSC Billing unit
quota regardless of how much data you actually have in the scratch
directory. See [billing](../accounts/billing.md) for details.
Furthermore, even after quota is increased, the automatic cleaning
process will continue removing idle files from the scratch directory.

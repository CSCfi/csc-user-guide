# Disk areas

In puhti there are three main disk areas: home, projappl and scratch. 


**Home:** Each user can store up to 10 GB of data in their home directory
(`$HOME`). This is meant for storing configurations files, and other
small personal data. 

It is not meant for running applications, use scratch for that
purpose.

**Projappl:** Project application folder for storing applications you have compiled yourself, libraries,
etc. there is also a persistent **project based** storage with a
default quota of 50 GB. It is located under
`/projappl/project_<project_id>`.  Project based means that this is
not a personal storage space, but is shared with all members of the
project team.

It is not meant for running applications, use scratch for that
purpose.


**Scratch:** Fast parallel scratch space. the **project based** shared storage can be found under
`/scratch/project_<project_id>`.  Note that this folder is shared by
**all users** in a project. This folder is not meant for long term
data storage and files that have not been used for 90 days will be
automatically removed. The default quota for this folder is 1 TB. 



|        |  Default quota   | Personal/project |  Environment variable |  path                          | Cleaning       |
|--------|------------------|------------------|-----------------------|--------------------------------|----------------|  
| Home   | 10 GiB           | Personal         | $(HOME)               | /home/<user-name>              |  No            | 
| Projappl | 50 GiB         | Project          |   Not available       | /projappl/project_<project_id> | No             |
| Scratch | 1 TiB           | Project          |   Not available       | /scratch/project_<project_id>  | Yes - 90 days  |




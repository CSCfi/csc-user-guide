# Disk quota exceeded

This warning means that you have exceeded your disk space quota or have too many files on the disk area. To see which quota is used up, type:

```
csc-workspaces
```

An example output is shown below:

```
Personal home folder        Quota
--------------------------------------------------------------------------
/users/jdoe                 Capacity:     653M/10G   Files:    .68k/100k

Project applications        Quota
--------------------------------------------------------------------------
/projappl/project_2000040   Capacity:   283.5M/50G   Files:    .37k/100k

Project scratch             Quota
--------------------------------------------------------------------------
/scratch/project_2000040    Capacity:   1.098T*/1T   Files:   .02k/1000k
```

The asterisk (`*`) indicates which quota is exceeded. To be able to create
new files in this file area, delete or re-arrange files or apply for more
quota.

!!! warning "Note"
     If you exceed disk quota in your HOME or PROJAPPL directory upon Conda-based
     installations of your software on Puhti/Mahti, we recommend using containerised 
     applications instead. The Conda-based installations unfortunately result in 
     the creation of excessive number of files which can cause extra overhead on 
     Lustre parallel file system in HPC environment. In some cases, you can clearly 
     see the inordinate delays in the activation time of Conda environment. When 
     possible, adapt container-based installation as the choice of installation 
     method for better performance. We support HPC-compliant Singularity containers 
     on Puhti/Mahti. 

If you are new to the concept of containers, you can consult the following relevant 
sections of tutorials which are collected as part of previous CSC courses:

 - [Using CSC HPC Environment Efficiently course](https://csc-training.github.io/csc-env-eff/)
 - [Containers and Workflows in Bioinformatics course](https://yetulaxman.github.io/containers-workflows/)

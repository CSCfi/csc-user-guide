# Disk quota exceeded

This warning means that you have exceeded your disk space quota or have too many
files on the disk area. To see which quota is used up, type:

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
     A common reason for exceeding your `$HOME` or `/projappl` disk quota is the
     usage of Conda-based installations. Conda environments result in the creation
     of excessive numbers of files which cause extra overhead on the Lustre parallel
     file system used in the HPC environment. This manifests as prolonged startup
     times and disk slowness affecting all users. If you need to use Conda on CSC
     supercomputers, we require that you containerize your environment, see
     [usage policy](../../computing/usage-policy.md#conda-installations).
     To easily containerize your Conda environments, please see the
     [Tykky container wrapper tool](../../computing/containers/tykky.md).

If you are new to the concept of containers, you can consult the following relevant 
sections of tutorials which are collected as part of previous CSC courses:

 - [Using CSC HPC Environment Efficiently course](https://csc-training.github.io/csc-env-eff/)
 - [Containers and Workflows in Bioinformatics course](https://yetulaxman.github.io/containers-workflows/)

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

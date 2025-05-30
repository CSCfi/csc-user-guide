# Disk quota exceeded

This warning means that you have exceeded your disk space quota or have too
many files on the disk area. To see which quota is used up, type:

```bash
csc-workspaces
```

An example output is shown below:

```text
[kkayttaj@puhti-login11 ~]$ csc-workspaces 

Disk area               Capacity(used/max)  Files(used/max)  Cleanup
----------------------------------------------------------------------
Personal home folder

/users/kkayttaj                 4.4G/10G         24K/100K        n/a
----------------------------------------------------------------------
Project: project_2000123 "Project X"

/projappl/project_2000123        24G/50G         36K/100K        n/a
/scratch/project_2000123        103G/1.0T       389K/1.0M       180d
----------------------------------------------------------------------
Project: project_2001234 "Project Y"

/projappl/project_2001234        85G/100G       282K/600K        n/a
/scratch/project_2001234       7.2T*/7.0T       2.7M/5.0M        90d
----------------------------------------------------------------------
```

The asterisk (`*`) indicates which quota is exceeded. To be able to create
new files in this disk area you need to delete or move files elsewhere, e.g. to
[Allas](../../data/Allas/index.md). If moving/deleting data is infeasible, you
can [apply for more quota](../../accounts/how-to-increase-disk-quotas.md).

!!! warning "Conda"
    A common reason for exceeding your `$HOME` or `/projappl` disk quota is the
    usage of Conda-based installations. Conda environments result in the
    creation of excessive numbers of files which cause extra load on the Lustre
    parallel file system used in the HPC environment. This manifests as
    prolonged startup times and disk slowness affecting all users.

    If you need to use Conda on CSC supercomputers, we require that you
    [containerize](../../computing/containers/overview.md) your environment,
    see [usage policy](../../computing/usage-policy.md#conda-installations). To
    easily containerize your Conda environments, please see the
    [Tykky container wrapper tool](../../computing/containers/tykky.md).

If you are new to containers, you can consult the following relevant sections
of tutorials which are collected as part of previous CSC courses:

* [Using CSC HPC Environment Efficiently course](https://csc-training.github.io/csc-env-eff/)
* [Containers and Workflows in Bioinformatics course](https://yetulaxman.github.io/containers-workflows/)

## I have deleted many files, but still get disk quota exceeded warning?

It is common for some software to create hidden directories starting with a dot
(`.`), such as `.cache`, `.cargo` or `.local`. These are often created by
default in your personal home folder and may cause confusion if they make you
exceed your disk quota. As hidden files are not shown by regular `ls` command,
it may seem like moving/deleting most folders/files does not have any effect.

To also see all hidden files/directories in a given folder, you need to use
`ls -a` option. [LUE (Lustre Usage Explorer)](../tutorials/lue.md) is another
recommended tool for finding where you have a lot of data that by default also
checks for hidden files and directories. Please use it if you exceed your disk
quota and have a hard time figuring out where the files might be hiding. For
example:

```bash
module load lue
lue $HOME
```

[See also this LUE tutorial](https://csc-training.github.io/csc-env-eff/hands-on/disk-areas/disk-areas-tutorial-lue.html).

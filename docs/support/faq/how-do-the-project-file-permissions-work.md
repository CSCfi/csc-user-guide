# How do the project and scratch file permissions work?

CSC sets the permissions of project and scratch directories so that
all project members have access to the folders. More specifically, the
folders are owned by the system administrator account, but the associated
Unix group has read and write rights. In addition, the set GID
permission is also enabled so that any new files and folders are owned
by the project group by default. Note that also the set GID permissions is
inherited to all new folders.

You can check the permissions using `ls -l` command. Correct default
permissions for a subfolder are `drwxrws---`. Note the small `s`
letter instead of `x` in the group permissions. If you see a capital `S`
instead, the directory doesn't have execute permissions which are
needed for group-level access.

If the set GID permission of any subdirectory
is removed on purpose or by accident, all new files and folders within
that subdirectory will be owned by the user's default personal group
and other group members can't access them. If the access is needed,
then the owner of those files and folders should change the group and
fix the permissions. Note that many tools and installation scripts do
modify the default permissions.

Example of missing SGID permission:

```bash
[maijam@puhti project_2009999]$ mkdir -m 00770 demofolder
[maijam@puhti project_2009999]$ ls -l
total 0
drwxrwx---. 2 maijam project_2009999       4096 Feb 15 14:52 demofolder
[maijam@puhti project_2009999]$ touch demofolder/my-file
[maijam@puhti project_2009999]$ ls -l demofolder/
total 0
-rw-rw----. 1 maijam maijam 0 Feb 15 14:52 my-file
[maijam@puhti project_2009999]$ chmod g+s demofolder/
[maijam@puhti project_2009999]$ touch demofolder/my-other-file
[maijam@puhti project_2009999]$ ls -l demofolder/
total 0
-rw-rw----. 1 maijam maijam          0 Feb 15 14:52 my-file
-rw-rw----. 1 maijam project_2009999 0 Feb 15 14:53 my-other-file
```

Example of fixing the permissions:

```bash
[maijam@puhti project_2009999]$ chgrp -R project_2009999 demofolder/
[maijam@puhti project_2009999]$ lfs find demofolder -type d -0 | xargs -0 chmod 2770
[maijam@puhti project_2009999]$ lfs find demofolder -type f -0 | xargs -0 chmod g+rwX
```

More about Linux file permissions at RedHat documentation:
[Linux permissions: SUID, SGID, and sticky bit](https://www.redhat.com/sysadmin/suid-sgid-sticky-bit).

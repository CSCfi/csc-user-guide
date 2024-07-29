# Examples for using Allas in CSC supercomputers 

CSC supercomputers, Puhti and Mahti, do not provide permanent storage space for
research data. Data that needs to be stored for a longer time than just a few
weeks should be copied to Allas object storage service. Allas provides a
platform that you can use to store your data as long as your CSC project is
active. In addition to storage, Allas can be used for transporting data between
different servers and sharing data with other users.

* [Allas user guide](index.md)

This tutorial provides four examples for using Allas on Puhti and Mahti. The
examples are based on interactively executed commands, and thus apply only for
relatively small datasets (max. some hundreds of GBs).

1. [The first example](#example-1-using-allas-with-a-commands) uses the
   *a-commands* (`a-put`, `a-get`) for uploading data from Mahti to Allas, and
   then downloading the data to Puhti.
2. [The second example](#example-2-using-allas-with-rclone) transfers the same
   data using *Rclone*.
3. [The third example](#example-3-uploading-large-files-to-allas) focuses on
   uploading large files to Allas.
4. [The fourth example](#example-4-uploading-complex-directory-structures-to-allas)
   handles the case in which the dataset to be copied includes a large amount
   of files.

The a-commands are better suited for cases where the data is mainly used within
the CSC computing environment (Puhti, Mahti). The second option, Rclone, is
good for cases when the data will be used outside CSC too.

## Getting access to Allas

By default, CSC computing projects do not have access to Allas. Thus, the first
thing is to
[add the Allas service to your project](../../accounts/how-to-add-service-access-for-project.md).
This is done in the [MyCSC](https://my.csc.fi) portal. Note that only the
project manager can apply for access.

The default storage quota in Allas is 10 TB. As this space is shared with all
project members, it is possible that the space is not sufficient. In that case,
you should estimate how much space is needed and request more space. The
request should be sent to [CSC Service Desk](../../support/contact.md). Please
include in your quota request:

1. The ID/name of your project
2. The amount of Allas space needed
3. A short description of the data to be stored 

Note that the data stored in Allas
[consume billing units of the project](../../accounts/billing.md).

## Example 1: Using Allas with a-commands

### A. Uploading data from Mahti to Allas

The a-commands are Allas-specific tools that allow an easy start with Allas.
The a-commands archive and move data automatically. You can also compress your
data before storage. For example, for text-formatted data compression reduces
the storage space needed, but on the other hand makes the transfer process
slightly slower. The a-commands are a good option for miscellaneous data that
is mostly used in the CSC environment.

In this example, we have a subdirectory `genomes/zebrafish` in the scratch
directory of a project in Mahti (`/scratch/project_2001659`). The `zebrafish`
directory contains eight files listed below:

```bash
[kkayttaj@mahti-login11 ~]$ ls /scratch/project_2001659/genomes/zebrafish
Danio_rerio.GRCz10.91.1.bt2      Danio_rerio.GRCz10.91.2.bt2  
Danio_rerio.GRCz10.91.3.bt2      Danio_rerio.GRCz10.91.4.bt2  
Danio_rerio.GRCz10.91.rev.1.bt2  Danio_rerio.GRCz10.91.rev.2.bt2  
Danio_rerio.GRCz10.fa            Danio_rerio.GRCz10.fa.fai
```

To copy the content of this directory to Allas, we first set up the Allas
environment:

```bash
module load allas
```

Then, we open a connection to Allas using the command `allas-conf`. The command
asks for the user's CSC password and then lists the Allas projects that are
accessible. In this case, we select `project_2001659`.

```bash
[kkayttaj@mahti-login11 ~]$ allas-conf
Mode swift
Please enter CSC password for account kkayttaj: <password>
Checking projects available for your account.
Please wait.
1) project_2000982     2) project_2001659     3) project_2000136      4) abort allas_conf
Please choose a project by giving an item number from the list above: 2
Configuration will be done for project: project_2001659
Protocols:
  swift
Connection stays active for eight hours.
```

`allas-conf` opens a connection to the specified Allas project for eight hours.
If we want to start using another project, we need to run `allas-conf` again.
However, in a single shell session `allas-conf` enables only one Allas project
to be active at a time. Note that certain tools, for example `rclone`, can
nonetheless be set up to use several Allas projects at the same time.

Next, we enter the `zebrafish` directory:

```bash
cd /scratch/project_2001659/genomes/zebrafish
```

We can now upload files one by one to Allas using the `a-put` command:

```bash
a-put Danio_rerio.GRCz10.fa
```

At the end of the upload process, the command reports:

```text
-------------------------------------------------------------------------------
1 files from Danio_rerio.GRCz10.fa uploaded to bucket 2001659-mahti-SCRATCH in Allas as one file: 
2001659-mahti-SCRATCH/genomes/zebrafish/Danio_rerio.GRCz10.fa
-----------------------------------------------------------------

Upload summary:
              Date                      Name  Files Size(kB)         Location in allas
 12.10.20 12:10:50     Danio_rerio.GRCz10.fa      1  1330852 2001659-mahti-SCRATCH/genomes/zebrafish
-----------------------------------------------------------------
OK
```

Moving data to Allas file by file is slow and produces a large amount of
objects. It is often more efficient to upload data to Allas one directory at a
time and store the data in bigger chunks. For example, to upload the
`zebrafish` directory, we first enter the parent directory `genomes`:

```bash
cd /scratch/project_2001659/genomes/
```

Then, we use `a-put` to upload the whole `zebrafish` directory to Allas as a
single object:

```bash
a-put zebrafish/
```

At the end of the upload process, the command reports:

```text
-------------------------------------------------------------------------------
8 files from zebrafish uploaded to bucket 2001659-mahti-SCRATCH in Allas as one tar file: 
2001659-mahti-SCRATCH/genomes/zebrafish.tar
-----------------------------------------------------------------

Upload summary:
              Date                      Name  Files Size(kB)         Location in allas
 12.10.20 14:10:47                 zebrafish      8  3191656 2001659-mahti-SCRATCH/genomes
-----------------------------------------------------------------
OK
```

After this, we have another object in the `2001659-mahti-SCRATCH` bucket:

```bash
[kkayttaj@mahti-login11 genomes]$ a-list 2001659-mahti-SCRATCH
2001659-mahti-SCRATCH/genomes/zebrafish.tar
2001659-mahti-SCRATCH/genomes/zebrafish/Danio_rerio.GRCz10.fa
```

Note that the file `Danio_rerio.GRCz10.fa` is in fact now stored in Allas
twice; both as an individual object (`genomes/zebrafish/Danio_rerio.GRCz10.fa`)
and as part of the `genomes/zebrafish.tar` object.

### B. Downloading to Puhti

Next, we download the same data to Puhti. After connecting to Puhti, we go to
the scratch directory of project 2001659 and load the `allas` module:

```bash
cd /scratch/project_2001659
module load allas
```

In this case, we want to use Allas with the project `project_2001659`, so we
can give the project name as an argument for the `allas-conf` command:

```bash
allas-conf project_2001659
```

Now the configuration process asks only for the CSC password and then sets up
the connection to Allas for project 2001659. As the Puhti scratch directory is
shared by all project members, we create a user-specific subdirectory
`kkayttaj`:

```bash
mkdir -p kkayttaj
cd kkayttaj/
```

With the command `a-list`, we can now see the objects that were just uploaded
from Mahti to Allas:

```bash
[kkayttaj@puhti-login12 kkayttaj]$ a-list
2001659-mahti-SCRATCH
[kkayttaj@puhti-login12 kkayttaj]$ a-list 2001659-mahti-SCRATCH
2001659-mahti-SCRATCH/genomes/zebrafish.tar
2001659-mahti-SCRATCH/genomes/zebrafish/Danio_rerio.GRCz10.fa
```

Locating data is easy as there are only two objects in the bucket, but as more
data is added to Allas, locating a specific file among dozens of buckets
containing hundreds of objects may be difficult. In that case, you can search
for a specific file using the command `a-find`. In this example, we can check
if an object contains the file `Danio_rerio.GRCz10.fa`:

```bash
[kkayttaj@puhti-login12 kkayttaj]$ a-find -a Danio_rerio.GRCz10.fa
----------------------------------------------
Checking bucket: 2001659-mahti-SCRATCH
Object: 2001659-mahti-SCRATCH/genomes/zebrafish.tar 
includes 2 file names that that match query: Danio_rerio.GRCz10.fa
Object: 2001659-mahti-SCRATCH/genomes/zebrafish/Danio_rerio.GRCz10.fa
includes 1 file names that that match query: Danio_rerio.GRCz10.fa
------------------------------------------------ 
Query: Danio_rerio.GRCz10.fa
Total of 3 hits were found in 2 objects
-------------------------------------------------
```

The `a-find` report above tells, for example, that the object
`2001659-mahti-SCRATCH/genomes/zebrafish.tar` contains two files whose names
match `Danio_rerio.GRCz10.fa` (the other file is `Danio_rerio.GRCz10.fa.fai`).
Note that `a-find` finds matches only among objects that were uploaded with
`a-put`.

Next, we download the data to Puhti using the `a-get` command:

```bash
[kkayttaj@puhti-login12 kkayttaj]$ a-get 2001659-mahti-SCRATCH/genomes/zebrafish.tar
Starting to copy data from allas...
Object:
  2001659-mahti-SCRATCH/genomes/zebrafish.tar
copied and uncompressed from allas into:
  zebrafish
```

After this, the current working directory in Puhti has a new directory
`zebrafish` that contains the files that were previously uploaded from Mahti to
Allas:

```bash
[kkayttaj@puhti-login12 kkayttaj]$ ls zebrafish/
Danio_rerio.GRCz10.91.1.bt2      Danio_rerio.GRCz10.91.3.bt2  
Danio_rerio.GRCz10.91.2.bt2      Danio_rerio.GRCz10.91.4.bt2
Danio_rerio.GRCz10.91.rev.1.bt2  Danio_rerio.GRCz10.fa
Danio_rerio.GRCz10.91.rev.2.bt2  Danio_rerio.GRCz10.fa.fai
```

## Example 2: Using Allas with Rclone

### A. Uploading data with Rclone

Rclone is the power-user tool for Allas. It is good in cases where the data
must be stored such that each file is a separate object.

!!! warning
    Rclone provides a fast and efficient way to use Allas, but you should use
    it carefully as Rclone operations can **overwrite** and **remove** data
    both in Allas and in the local disk environment without notifying or asking
    for confirmation.

    * [Using Allas with Rclone from Puhti and Mahti](./using_allas/rclone.md)

This example uses the same data as the previous case: in the scratch directory
of Mahti, we have a subdirectory `genomes/zebrafish` that contains the eight
files listed below:

```bash
[kkayttaj@mahti-login11 ~]$ ls /scratch/project_2001659/genomes/zebrafish
Danio_rerio.GRCz10.91.1.bt2      Danio_rerio.GRCz10.91.2.bt2  
Danio_rerio.GRCz10.91.3.bt2      Danio_rerio.GRCz10.91.4.bt2  
Danio_rerio.GRCz10.91.rev.1.bt2  Danio_rerio.GRCz10.91.rev.2.bt2  
Danio_rerio.GRCz10.fa            Danio_rerio.GRCz10.fa.fai
```

To copy the content of this directory to Allas, we first set up the Allas
environment:

```bash
module load allas
```

Then, we open a connection to Allas using the command `allas-conf`. The command
asks for the user's CSC password and then lists the Allas projects that the
user can access. In this case, we select `project_2001659`:

```bash
[kkayttaj@mahti-login11 ~]$ allas-conf
Please enter CSC password for account kkayttaj: <password>
Checking projects available for your account.
Please wait.
1) project_2000982     2) project_2001659     3) project_2000136      4) abort allas_conf
Please choose a project by giving an item number from the list above: 2
Configuration will be done for project: project_2001659
Protocols:
  swift
Connection stays active for eight hours.
```

The `allas-conf` procedure above defines an Allas connection that is valid for
eight hours. Next, we go to the `genomes` directory:

```bash
cd /scratch/project_2001659/genomes
```

Instead of `a-put` that was used in the previous example, we use command
`rclone copyto` to copy all files from the given directory to Allas. In the
case of `rclone`, there is no default bucket. Instead, we have to define a
bucket. In this example, we use the bucket name `2001659-genomes` and define
each object name to have the prefix `zebrafish`.

```text
rclone copyto zebrafish/ allas:2001659-genomes/zebrafish
```

After copying the files, we can use `rclone ls` to see what has been uploaded
to Allas:

```bash
[kkayttaj@mahti-login11 genomes] rclone ls allas:2001659-genomes/zebrafish
450646234 Danio_rerio.GRCz10.91.1.bt2
334651392 Danio_rerio.GRCz10.91.2.bt2
   187325 Danio_rerio.GRCz10.91.3.bt2
334651387 Danio_rerio.GRCz10.91.4.bt2
450646234 Danio_rerio.GRCz10.91.rev.1.bt2
334651392 Danio_rerio.GRCz10.91.rev.2.bt2
1362788082 Danio_rerio.GRCz10.fa
      715 Danio_rerio.GRCz10.fa.fai
```

### B. Downloading the data to Puhti

Next, we download the same data to Puhti. After connecting to Puhti, we go to
the scratch directory of `project_2001659` and load the `allas` module:

```bash
cd /scratch/project_2001659
module load allas
```

In this case, we want to use Allas with the project 2001659, so we can give the
project name as an argument for the `allas-conf` command:

```bash
allas-conf project_2001659
```

Now the configuration process asks only for the CSC password and then sets up
the connection to Allas for project 2001659. As the Puhti scratch directory is
shared by all project members, we create a user-specific subdirectory
`kkayttaj` and go there:

```bash
mkdir -p kkayttaj
cd kkayttaj/
```

We can now use the command `rclone lsd` to check the available buckets in
Allas:

```bash
[kkayttaj@puhti-login12 kkayttaj]$ rclone lsd allas:
  3268222761 2020-10-03 10:01:42         8 2001659-genomes
  2576778428 2020-10-03 10:01:42         4 2001659-mahti-SCRATCH
```

Now we see two buckets. `2001659-genomes` is the one that was just created in
this example, while `2001659-mahti-SCRATCH` originates from the previous
a-command example. Next, we list the objects in the `2001659-genomes` bucket:

```bash
[kkayttaj@puhti-login12 kkayttaj]$ rclone ls allas:2001659-genomes
450646234 zebrafish/Danio_rerio.GRCz10.91.1.bt2
334651392 zebrafish/Danio_rerio.GRCz10.91.2.bt2
   187325 zebrafish/Danio_rerio.GRCz10.91.3.bt2
334651387 zebrafish/Danio_rerio.GRCz10.91.4.bt2
450646234 zebrafish/Danio_rerio.GRCz10.91.rev.1.bt2
334651392 zebrafish/Danio_rerio.GRCz10.91.rev.2.bt2
1362788082 zebrafish/Danio_rerio.GRCz10.fa
      715 zebrafish/Danio_rerio.GRCz10.fa.fa
```

Finally, we use the `rclone copyto` command to copy the data from Allas to
Puhti into a new directory `zebrafish2`: 

```bash
[kkayttaj@puhti-login12 kkayttaj]$ rclone -P copyto allas:2001659-genomes/zebrafish zebrafish2
Transferred:        3.044 GiB / 3.044 GiB, 100%, 323.600 MBytes/s, ETA 0s
Transferred:            8 / 8, 100%
Elapsed time:        9.6s

[kkayttaj@puhti-login12 kkayttaj]$ ls zebrafish2
Danio_rerio.GRCz10.91.1.bt2      Danio_rerio.GRCz10.91.3.bt2  
Danio_rerio.GRCz10.91.2.bt2      Danio_rerio.GRCz10.91.4.bt2
Danio_rerio.GRCz10.91.rev.1.bt2  Danio_rerio.GRCz10.fa
Danio_rerio.GRCz10.91.rev.2.bt2  Danio_rerio.GRCz10.fa.fai
```

## Example 3: Uploading large files to Allas

In the previous two examples, the actual amount of data was rather moderate,
only a few gigabytes. If the size of an individual data file is hundreds of
gigabytes or more, transporting only a few files may take longer than the
duration of the token-based Allas authentication.

In this example, we use `a-put` to upload a set of large files from Mahti to
Allas.

The first thing to do is to open a Mahti connection that can remain running for
a long time. In this example, we use `screen` command to open a session that
can be left running in the background:

```bash
ssh <username>@mahti.csc.fi
screen
```

The `screen` command starts a virtual session on the login node of Mahti. You
can leave this virtual `screen` session running in the background and log out
from Mahti, but you should check which login node (`mahti-login[11,12,14,15]`) 
your session is running on because you need to log in to the same node to
reconnect to your `screen` session later on.

In the `screen` session, first load the `allas` module and use `allas-conf` to
establish a connection to Allas.

```bash
module load allas
allas-conf -k
```

Here, `allas-conf` is used with the option `-k` that saves your CSC password in
an environment variable (`$OS_PASSWORD`) so that the connection to Allas can
later be automatically reconfigured without needing to give the password again.

After opening the Allas connection, we move to a directory `my_data` where we
have three subdirectories (`50`, `90`, `100`). We list the gzip-compressed
files in these directories:

```bash
[kkayttaj@mahti-login11 ~] cd /scratch/project_2001659/my_data
[kkayttaj@mahti-login my_data] ls -lh */*.gz
-rw-rwxr-x 1 kkayttaj csc  45G May  8 12:57 100/uniref100.fasta.gz
-rw-rwxr-x 1 kkayttaj csc  61G Jun  5 13:09 100/uniref100.xml.gz
-rw-rwxr-x 1 kkayttaj csc 589M Jun  5 13:09 50/uniref50.fasta.gz
-rw-rwxr-x 1 kkayttaj csc  17G Jun  5 13:09 50/uniref50.xml.gz
-rw-r-xr-x 1 kkayttaj csc 4.2G Jul  6 09:46 90/uniref90.fasta.gz
-rw-rwxr-x 1 kkayttaj csc  33G Jun  5 13:09 90/uniref90.xml.gz
```

Next, we launch the upload process. In this case, we do not use the default
bucket name, but assign the name to be `2001659-uniref`:

```bash
a-put -b 2001659-uniref */*.gz
```

This command uploads the files listed above to Allas. Alternatively, we could
launch the same upload with `rclone copy`:

```bash
for f in */*.gz
do
    rclone copy $f allas:2001659-uniref
done
```
 
We can leave the session running in the background by pressing `Ctrl-A D`. Now,
we can log out from Mahti with the `screen` session remaining active in the
Mahti login node we used (in this case, `mahti-login11`).

To re-connect to this session, we first connect to the Mahti node where the
`screen` session is running:

```bash
ssh <username>@mahti-login11.csc.fi
```

Then, we reattach the `screen` session:

```bash
screen -r
``` 

Once the `a-put` command is finished, we will run `a-check` command to check if
all the data objects have been created. `a-check` needs to be executed with the
exact same options that were used with the `a-put` command. So in this case the
command would be:

```bash
a-check -b 2001659-uniref */*.gz
```

The `a-check` command compares the item names to be uploaded to the matching
objects in Allas. The files or directories that don't have a target object in
Allas are reported and stored in a file. In this case, if some objects in the
`a-put` command above would be missing, then `a-check` would list the missing
files and directories in a file `missing_2001659-uniref_63449` (the number at
the end is just a random number).

The file of missing items can then be used with `a-put` option `--input-list`
to continue the failed upload process:

```bash
a-put -b 2001659-uniref --nc --input-list missing_2001659-uniref_63449
```

You should note that `a-check` does not check if the actual contents of the
object is correct. It checks only the object names, which might as well
originate from some other sources.

## Example 4: Uploading complex directory structures to Allas

Some workflows and software create complex directory structures to store and
manage data. You might have directories that have thousands or even millions of
individual files. Copying such datasets to Allas takes time and is not always
straightforward. The most reasonable way to upload this kind of data depends on
the case. This example introduces a few alternatives.

First, we open a `screen` session on Puhti and set up an Allas connection just
like in the previous example:

```bash
ssh <username>@puhti.csc.fi
screen
module load allas
allas-conf -k
```

Suppose we have a directory structure that contains images from road condition
cameras from ten locations with an interval of ten minutes from the years
2014–2018. The data is located in the directory `road_cameras` where each
location has its own subdirectory (ten directories). Inside each subdirectory,
there is another layer of subdirectories, one for each year (five
subdirectories), each containing subdirectories for every day of the year
(further 365 subdirectories), each containing 144 small image files.

For example:

```bash
road_cameras/site_7/2017/day211/image_654887.jpg
```

Thus, the total number of files in the `road_cameras` directory is
`10 * 5 * 365 * 144 = 2 628 000`.

In principle, we could copy all 2.6 million files as separate objects to Allas,
but in that case, we should split the data into multiple buckets as one bucket
can have at most 0.5 million objects. You could, for example, run a separate
`rclone` command for each `site_*` directory and put the data from each site to
a site-specific bucket. For example:

```bash
rclone copyto road_cameras/site_1 allas:2001659_road_cameras_site_1/
```

This way, you would end up creating ten buckets each containing 262 800
objects. This approach could be the most efficient way for storing and reusing
the data if you know that you will need to access individual images randomly.

As another extreme option, we could use `a-put` and collect all data into a
single archive object. In order to do that, you must add the option
`--skip-filelist` to the `a-put` command. By default, `a-put` collects detailed
metadata of **each** file in an `ameta` file. However, if you have millions of
files, collecting this information takes a long time. If you need to know the
file names, you can use the `--simple-fileslist` option to collect the names –
but **no** other information – of the files in the metadata file. This already
speeds up the preprocessing significantly. However, as in this case the naming
has been systematic, storing the file names to the metadata files can be just
ignored altogether (`--skip-filelist`), which is the fastest option.

```bash
a-put --skip-filelist road_cameras/
```

This approach would store all 2,6 million files as a single object.

In practice, however, the optimal way of storing the data is often something
between these two extremes. As a compromise, you could apply packing at a
higher level in the hierarchy. For example:

```bash
a-put --skip-filelist road_cameras/site_*
```

This would produce ten objects, each containing all information from a single
camera site. Alternatively, you could do the archiving so that data from each
year from each camera is collected as a single object:

```bash
a-put --skip-filelist road_cameras/site_*/20*
```

This option would store the data as 50 objects. Day-based objects for each
camera might be the most practical option for using the data later on, but as a
downside, preprocessing the data into `10 * 5 * 365 = 18250` objects probably
takes quite a long time.

Copying millions of files to Allas takes a long time regardless of the method.
If we have started the `a-put` command inside a `screen` session, we can detach
from the virtual session by pressing `Ctrl-A D`, log out from Puhti and leave
the upload process running for days.

Once the `a-put` command is finished, we will run `a-check` command to check if
all the data objects have been created. `a-check` needs to be executed with the
exact same options that were used with the `a-put` command. So in this case the
command would be:

```bash
a-check --skip-filelist road_cameras/site_*/20*
```

The `a-check` command compares the item names to be uploaded to the matching
objects in Allas. The files or directories that don't have a target object in
Allas are reported and stored in a file. In this case, if some objects in the
`a-put` command above would be missing, then `a-check` would list the missing
files and directories in a file `missing_<bucket_name>_<number>` (the number at
the end is just a random number).

The file of missing items can then be used with `a-put` option `--input-list`
to continue the failed upload process:

```bash
a-put -b 2001659-uniref --nc --input-list missing_<bucket_name>_<number>
```

You should note that `a-check` does not check if the actual contents of the
object is correct. It checks only the object names, which might as well
originate from some other sources.

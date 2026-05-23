# Tutorial for using Allas in Roihu supercomputer

One of the main use cases of Allas is to store data while it is not actively used in the CSC supercomputers. When you start working, you stage in the data from Allas. And when the data is no longer actively used, it can be staged out to Allas.The _sratch disk area_ of Roihu allow you to analyze large datasets. However  scartch disk in not intended for long-term storage fo research data. Data that needs to be stored for a longer time than just a few weeks should be copied to Allas or Lumi-O object storage service instead. Allas provides a platform that you can use to store your data as long as your CSC project is active. In addition to storage, Allas can be used for transporting data between different servers and sharing data with other users.

If you have not used Allas before, then start with reading **[Allas general introduction](introduction.md)**, which includes many important things to know.

Note that CSC computing projects do not have access to Allas automatically. The project manager has to active the Allas service in [MyCSC](https://my.csc.fi/) before project can start using Allas. [Allas introduction page](introduction.md#) describes how to do it and also about default quotas and how to apply for more storage space.

Additional information regarding:

* [Using Allas in batch jobs](allas_batchjobs.md)
* [Using Allas and LUMI-O from LUMI supercomputer](allas_lumi.md)

There are several alternative tools to move data between Allas and Roihu. You can use [Puhti or Mahti web interface](accessing_allas.md#web-browser-interfaces), [commandline tools](accessing_allas.md#commandline-tools) or [Python, R or other tools](accessing_allas.md#graphical-tools). In Roihu, the Allas commandline tools are installed by CSC and provided through **allas module**.

   * [Allas module in Roihu](../../computing/allas-in-roihu.md)


## Examples

This tutorial provides four examples for using Allas in Roihu. The
examples are based on interactively executed commands, and thus examples 1, 2 and 4 apply only for
relatively small datasets (max. some hundreds of GBs). The third example suits also for bigger datasets.

1. [The first example](#example-1-using-allas-with-a-commands) uses the
   *a-commands* (`a-put`, `a-get`) for uploading data from Roihu to Allas, and
   then downloading the data back to Roihu.
2. [The second example](#example-2-using-allas-with-rclone) transfers the same
   data using *Rclone*.
4. [The third example](#example-3-uploading-complex-directory-structures-to-allas)
   handles the case in which the dataset to be copied includes a large amount
   of files.

The a-commands are better suited for cases where the data is mainly used within
the CSC computing environment (Roihu, Lumi). The second option, Rclone, is
good for cases when the data will be used outside CSC too. Note that **s3cmd** and **aws s3** are totally valid alternatives
for rclone and a-commands, even though they are not used in this tutorial.

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
[kkayttaj@roihu-cpu-login1 ~]$ ls /scratch/project_2001659/genomes/zebrafish
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
Mode s3cmd
Please enter CSC password for account kkayttaj: <password>
Checking projects available for your account.
Please wait.
1) project_2000982     2) project_2001659     3) project_2000136      4) abort allas_conf
Please choose a project by giving an item number from the list above: 2
Configuration will be done for project: project_2001659
Protocols:
  S3
s3cmd configuration updated

Remote endpoints configured for rclone

Rclone remote name       Protocol
--------------------------------------------------------
s3allas:                 s3    
s3allas-project_2001659: s3    
--------------------------------------------------------
rclone remote s3allas: now provides an S3 based connection to project project_2001659 in Allas
aws licent and s3cmd use now project_2001659
a-commands use now project_2001659 when used in S3 mode
```

`allas-conf` stores S3 authentication keys to your home directory-
If we want to start using another project, we need to run `allas-conf` again.

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

Files or directories to be uploaded: zebrafish/
Processing: zebrafish/
Checking total size of zebrafish. Please wait.

zebrafish contains 8 files or directories that take 2585920K of disk space
Collecting data from directory zebrafish to archive file: zebrafish.tar
zebrafish/
zebrafish/Danio_rerio.GRCz10.fa.fai
zebrafish/Danio_rerio.GRCz10.91.3.bt2
zebrafish/Danio_rerio.GRCz10.91.4.bt2
zebrafish/Danio_rerio.GRCz10.fa
zebrafish/Danio_rerio.GRCz10.91.rev.2.bt2
zebrafish/Danio_rerio.GRCz10.91.rev.1.bt2
zebrafish/Danio_rerio.GRCz10.91.2.bt2
zebrafish/Danio_rerio.GRCz10.91.1.bt2
Packing successful.
Uploading data to s3allas.
Transferred:        3.044 GiB / 3.044 GiB, 100%, 62.753 MiB/s, ETA 0s
Transferred:            1 / 1, 100%
Elapsed time:        46.9s
Confirming upload...

Adding metadata for uploaded zebrafish
Transferred:            975 B / 975 B, 100%, 0 B/s, ETA -
Transferred:            1 / 1, 100%
Elapsed time:         0.0s

-------------------------------------------------------------------------------
8 files from zebrafish uploaded to bucket 2001659-roihu-scratch in Allas as one tar file: 
2001659-roihu-scratch/genomes/zebrafish.tar
-----------------------------------------------------------------

Upload summary:
              Date                      Name  Files Size(kB)         Location in Allas
 06.05.26 13:05:05                 zebrafish      8  2585920 2001659-roihu-scratch/genomes
-----------------------------------------------------------------
OK
```

After this, we have another object in the `2001659-roihu-scratch` bucket:

```bash
[kkayttaj@roihu-cpu-login1 genomes]$ a-list 2001659-roihu-scratch
2001659-roihu-scratch/genomes/zebrafish.tar
2001659-roihu-scratch/genomes/zebrafish/Danio_rerio.GRCz10.fa
```

Note that the file `Danio_rerio.GRCz10.fa` is in fact now stored in Allas
twice; both as an individual object (`genomes/zebrafish/Danio_rerio.GRCz10.fa`)
and as part of the `genomes/zebrafish.tar` object.

### B. Downloading data to Roihu

Next, we download the same data back to Roihu. In this example we assume that zebrafish genome data has been removed from Roihu, either by the user or because of the automatic cleanong process. 

After connecting to Roihu, we go to the scratch directory of project 2001659 and load the `allas` module:

```bash
cd /scratch/project_2001659
module load allas
```

From the output of the `module load allas` command you can check of the a-commands use the right Allas, in ths case `project_2001659`. If needed you can take the project in use with allas-conf command:

```bash
allas-conf project_2001659
```

In the case of the command above the configuration process asks only for the CSC password and then sets up
the connection to Allas for project 2001659. As the Roihu scratch directory is
shared by all project members, we create a user-specific subdirectory
`kkayttaj`:

```bash
mkdir kkayttaj
cd kkayttaj/
```

With the command `a-list`, we can now see the objects that were previosly uploaded to Allas:

```bash
[kkayttaj@roihu-cpu-login2 kkayttaj]$ a-list
2001659-roihu-scratch
[kkayttaj@roihu-login1 kkayttaj]$ a-list 2001659-roihu-scratch
2001659-roihu-scratch/genomes/zebrafish.tar
2001659-roihu-scratch/genomes/zebrafish/Danio_rerio.GRCz10.fa
```

Locating data is easy as there are only two objects in the bucket, but as more
data is added to Allas, locating a specific file among dozens of buckets
containing hundreds of objects may be difficult. In that case, you can search
for a specific file using the command `a-find`. In this example, we can check
if an object contains the file `Danio_rerio.GRCz10.fa`:

```bash
[kkayttaj@rouhu-cpu-login2 kkayttaj]$ a-find -a Danio_rerio.GRCz10.fa
Checking bucket: 2001659-roihu-scratch

Matching object names:
2001659-roihu-scratch/genomes/zebrafish/Danio_rerio.GRCz10.fa
----------------------------------------------
a-put generated objects that include matching file name:

 Object: 2001659-roihu-scratch/genomes/zebrafish.tar
 includes 2 file names that that match query: Danio_rerio.GRCz10.fa

 Object: 2001659-roihu-scratch/genomes/zebrafish/Danio_rerio.GRCz10.fa
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
`a-put`. Further, `a-find` searches objects with object name only. Don't include the bukcet name to the search term.
Instead use option `-b <bucket-name>` if you wish to serach the object from just one bucket.

Next, we download the data to Roihu using the `a-get` command:

```bash
[kkayttaj@roihu-cpu-login2 kkayttaj]$ a-get 2001659-roihu-scratch/genomes/zebrafish.tar
Starting to copy data from allas...
Object:
  2001659-roihu-scratch/genomes/zebrafish.tar 
copied and uncompressed from s3allas into:
  zebrafish
```

After this, the current working directory in Roihu has a new directory
`zebrafish` that contains the files that were previously uploaded from Roihu to
Allas:

```bash
[kkayttaj@roihu-cpu-login2 kkayttaj]$ ls zebrafish/
Danio_rerio.GRCz10.91.1.bt2  Danio_rerio.GRCz10.91.rev.1.bt2
Danio_rerio.GRCz10.91.2.bt2  Danio_rerio.GRCz10.91.rev.2.bt2
Danio_rerio.GRCz10.91.3.bt2  Danio_rerio.GRCz10.fa
Danio_rerio.GRCz10.91.4.bt2  Danio_rerio.GRCz10.fa.fai
``

## Example 2: Using Allas with Rclone

### A. Uploading data with Rclone

Rclone is the power-user tool for Allas. It is good in cases where the data
must be stored such that each file is a separate object.

!!! warning
    Rclone provides a fast and efficient way to use Allas, but you should use
    it carefully as Rclone operations can **overwrite** and **remove** data
    both in Allas and in the local disk environment without notifying or asking
    for confirmation.

    * [Using Allas with Rclone from Roihu](./using_allas/rclone.md)

This example uses the same data as the previous case: in the scratch directory
of Roihu, we have a subdirectory `genomes/zebrafish` that contains the eight
files listed below:

```bash
[kkayttaj@roihu-cpu-login2 ~]$ ls /scratch/project_2001659/genomes/zebrafish
Danio_rerio.GRCz10.91.1.bt2  Danio_rerio.GRCz10.91.rev.1.bt2
Danio_rerio.GRCz10.91.2.bt2  Danio_rerio.GRCz10.91.rev.2.bt2
Danio_rerio.GRCz10.91.3.bt2  Danio_rerio.GRCz10.fa
Danio_rerio.GRCz10.91.4.bt2  Danio_rerio.GRCz10.fa.fai
```

To copy the content of this directory to Allas, we first set up the Allas
environment:

```bash
module load allas
```

From the output of the `module load allas` command you can check of the a-commands use the right Allas, in ths case `project_2001659`. If needed you can take the project in use with allas-conf command:

```bash
allas-conf project_2001659
```

In the case of the command above the configuration process asks only for the CSC password and then sets up
the connection to Allas for project 2001659. After configuration you can use the Allas area of the defined
project using two rclone endpoints: s3allas:, s3allas-project_name. In this example the endpoints are **s3allas:** and **s3allas-project_2001659:**.

After configuration, these two endpoints are in use in all Roihu sessions, including batch jobs. 
The short endpoint is nicer to use in command line, but it changes if you run allas-conf to use another project.
Thus the project specific endpoint (s3allas-project_2001659) would be better option for batch jobs and project specific scripts.

To start the download, we go to the `genomes` directory:

```bash
cd /scratch/project_2001659/genomes
```

Instead of `a-put` that was used in the previous example, we use command
`rclone copy` to copy all files from the given directory to Allas. In the
case of `rclone`, there is no default bucket. Instead, we have to define a
bucket. In this example, we use the bucket name `2001659-genomes` and define
each object name to have the prefix `zebrafish`.

```text
rclone copy -P zebrafish/ s3allas:2001659-genomes/zebrafish
```

After copying the files, we can use `rclone ls` to see what has been uploaded
to Allas:

```bash
[kkayttaj@roihu-cpu-login2 genomes] rclone ls s3allas:2001659-genomes/zebrafish
450646234 Danio_rerio.GRCz10.91.1.bt2
334651392 Danio_rerio.GRCz10.91.2.bt2
   187325 Danio_rerio.GRCz10.91.3.bt2
334651387 Danio_rerio.GRCz10.91.4.bt2
450646234 Danio_rerio.GRCz10.91.rev.1.bt2
334651392 Danio_rerio.GRCz10.91.rev.2.bt2
1362788082 Danio_rerio.GRCz10.fa
      715 Danio_rerio.GRCz10.fa.fai
```

### B. Downloading the data to Roihu

Next, we download the same data back to Roihu. After connecting to Roihu, we go to
the scratch directory of `project_2001659` and load the `allas` module:

```bash
cd /scratch/project_2001659
module load allas
```

If rclone is still configured for project 2001659, there is no need to run `allas-conf`. 

As the Roihu scratch directory is shared by all project members, we create a user-specific subdirectory
`kkayttaj` and go there:

```bash
mkdir kkayttaj
cd kkayttaj/
```

We can now use the command `rclone lsd` to check the available buckets in
Allas:

```bash
[kkayttaj@roihu-cpu-login2 kkayttaj]$ rclone lsd s3allas:
  3268222761 2026-05-03 10:01:42         8 2001659-genomes
  2576778428 2026-05-03 10:01:42         4 2001659-roihu-SCRATCH
```

Now we see two buckets. `2001659-genomes` is the one that was just created in
this example, while `2001659-mahti-SCRATCH` originates from the previous
a-command example. Next, we list the objects in the `2001659-genomes` bucket:

```bash
[kkayttaj@roihu-cpu-login2 kkayttaj]$ rclone ls s3allas:2001659-genomes
450646234 zebrafish/Danio_rerio.GRCz10.91.1.bt2
334651392 zebrafish/Danio_rerio.GRCz10.91.2.bt2
   187325 zebrafish/Danio_rerio.GRCz10.91.3.bt2
334651387 zebrafish/Danio_rerio.GRCz10.91.4.bt2
450646234 zebrafish/Danio_rerio.GRCz10.91.rev.1.bt2
334651392 zebrafish/Danio_rerio.GRCz10.91.rev.2.bt2
1362788082 zebrafish/Danio_rerio.GRCz10.fa
      715 zebrafish/Danio_rerio.GRCz10.fa.fa
```

Finally, we use the `rclone copy` command to copy the data from Allas to
Roihu into a new directory `zebrafish2`: 

```bash
[kkayttaj@roihu-cpu-login2 kkayttaj]$ rclone -P copy s3allas:2001659-genomes/zebrafish zebrafish2
Transferred:        3.044 GiB / 3.044 GiB, 100%, 323.600 MBytes/s, ETA 0s
Transferred:            8 / 8, 100%
Elapsed time:        9.6s

[kkayttaj@roihu-cpu-login1 kkayttaj]$ ls zebrafish2
Danio_rerio.GRCz10.91.1.bt2      Danio_rerio.GRCz10.91.3.bt2  
Danio_rerio.GRCz10.91.2.bt2      Danio_rerio.GRCz10.91.4.bt2
Danio_rerio.GRCz10.91.rev.1.bt2  Danio_rerio.GRCz10.fa
Danio_rerio.GRCz10.91.rev.2.bt2  Danio_rerio.GRCz10.fa.fai
```

## Example 3: Uploading complex directory structures to Allas

Some workflows and software create complex directory structures to store and
manage data. You might have directories that have thousands or even millions of
individual files. Copying such datasets to Allas takes time and is not always
straightforward. The most reasonable way to upload this kind of data depends on
the case. This example introduces a few alternatives.

First, we open a `screen` session on Roihu and set up an Allas connection just
like in the previous example:

```bash
ssh <username>@puhti.csc.fi
screen
module load allas
allas-conf
```

Suppose we have a directory structure that contains images from road condition
cameras from ten locations with an interval of ten minutes from the years
2021–2025. The data is located in the directory `road_cameras` where each
location has its own subdirectory (ten directories). Inside each subdirectory,
there is another layer of subdirectories, one for each year (five
subdirectories), each containing subdirectories for every day of the year
(further 365 subdirectories), each containing 144 small image files.

For example:

```bash
road_cameras/site_7/2022/day211/image_654887.jpg
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
However, you would then need to use some other tools than rclone or a-commands,
ase rclone has a bug that makes it fail in cases where one bucket contains huge number
of object names (typically this starts to affect in cases where the number of objects is over 15 000- 50 000).

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
from the virtual session by pressing `Ctrl-A D`, log out from Roihu and leave
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

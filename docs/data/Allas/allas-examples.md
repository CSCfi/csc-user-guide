# Examples for using Allas in CSC supercomputers 

CSC supercomputers, Puhti and Mahti, do not provide permanent storage space for research data. 
The data that needs to be stored for a longer time than just few weeks, should be copied to Allas object storage service.
Allas provides a platform that you can use to store your data as long as you CSC project is active. In addition 
to storing, Allas can be used for transporting data between different servers and sharing data with other users.

*    [Allas user guide](./index.md)

This tutorial provides four examples for using Allas in Puhti and Mahti. The examples are based on interactively 
executed commands and thus apply only for relatively small datasets (max some hundreds of GBs).

1.   [The first example](#e1) uses the *a-commands* (a-put, a-get) for uploading data from Mahti to Allas and then downloading the data to Puhti.
2.   [The second example](#e2) transports the same data using _rclone_.
3.   [The third example](#e3) focuses on uploading large files to Allas.
4.   [The fourth example](#e4) handles the case in which the dataset to be copied includes a *large* amount of files.

The _a-commands_ are better suited for cases when the data is mainly used within the CSC computing environment (Puhti, Mahti). 
The second option, _rclone_, is good for cases when the data will be used outside CSC too.



## Get access to Allas

By default, CSC computing projects do not have access to Allas. Thus, the first thing is to add 
the Allas service to your project. This is done in the [MyCSC](https://my.csc.fi) interface. 
Note that only the project manager can apply for access. Once access is granted, all project 
members must visit the MyCSC and accept the terms of use for Allas before they can use the Allas 
storage area.

The default storage quota in Allas is 10 TB.  As this space is shared with all project members, it is  
possible that the space is not sufficient. In that case, you should estimate how much space is needed 
and request more space. The request should be sent to **servicedesk@csc.fi**.
Please include in your quota request:

   *    The ID/name of your project
   *    The amount of Allas space needed
   *    A short description of the data to be stored 

Note that the data stored in Allas consume billing units of the project.



# Example 1: Using Allas with a-commands <a name="e1"></a>

## A. Uploading data from Mahti to Allas

The a-commands are Allas-specific tools that allow an easy start with Allas.  
The a-commands pack,and move data automatically. You can also apply compression for your data before storage.
For e.g. text formatted data compression reduces the storage space needed but on
the other hand makes the storage process bit slower. The a-commands are a good option for miscellaneous data 
that is mostly used in the CSC environment.

In this example, we have the sub directory _genomes/zebrafish_ in the _scratch_ directory of a project in Mahti (/scratch/project_2001659). 
The zebrafish directory contains eight files listed below:

<pre><b>ls genomes/zebrafish</b>
Danio_rerio.GRCz10.91.1.bt2  Danio_rerio.GRCz10.91.2.bt2  
Danio_rerio.GRCz10.91.3.bt2  Danio_rerio.GRCz10.91.4.bt2  
Danio_rerio.GRCz10.91.rev.1.bt2  Danio_rerio.GRCz10.91.rev.2.bt2  
Danio_rerio.GRCz10.fa  Danio_rerio.GRCz10.fa.fai
</pre>

To copy the content of this directory to Allas, I first set up the Allas environment:
```text
module load allas
```
Then I open a connection to Allas using the command `allas-conf`. The command asks for users' CSC password (xxxxxxxxxxx) and 
then lists the Allas projects that are accessible. In this case, we select _project_2001659_.

<pre>[kkayttaj@mahti-login11 ~]$ <b>allas-conf</b>
Please enter CSC password for account kkayttaj: 
<b>xxxxxxxxxx</b>
Checking projects available for your account.
Please wait.
1) project_2000982     2) project_2001659     3) project_2000136      4) abort allas_conf
Please choose a project by giving an item number from the list above: <b>2</b>

allas connection configured successfully.
Connection stays active for eight hours.
</pre>

`allas-conf` opens a connection to the specified Allas project for eight hours. If you want to start using 
another project, you need to run `allas-conf` again. However, in one shell session you can have only one Allas project active at a time.

Next I enter the _zebrafish_ directory:
```text
cd /scratch/project_2001659/genomes/zebrafish
```
I can now upload files one by one to Allas with the `a-put` command:
```text
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
</pre>

Moving data to Allas file by file is slow and produces large amounts of objects. It is often more efficient to 
upload data to Allas one directory at a time and store the data in bigger chunks. For example, to upload the 
zebrafish directory, we first enter the _genomes_ directory
```text
cd /scratch/project_2001659/genomes/
```
and then use `a-put` to upload the whole zebrafish directory to Allas as one object.
```text
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

After this, we have another object in the _2001659-mahti-SCRATCH_ bucket:

<pre>[kkayttaj@mahti-login11 genomes]$ <b>a-list 2001659-mahti-SCRATCH</b>
2001659-mahti-SCRATCH/genomes/zebrafish.tar
2001659-mahti-SCRATCH/genomes/zebrafish/Danio_rerio.GRCz10.fa
</pre>

Note that, in fact, the file _Danio_rerio.GRCz10.fa_ is now stored in Allas twice: 
As an individual object (genomes/zebrafish/Danio_rerio.GRCz10.fa)
and as part of the _genomes/zebrafish.tar_ object.

## B. Downloading to Puhti
Next we download the same data to Puhti. After connecting to _puhti.csc.fi_, I go to the scratch directory of 
the project 2001659 and load the _allas_ module:
```text
cd /scratch/project_2001659
module load allas
```
In this case, we want to use Allas with the project *project_2001659*, so we can give the project name as an 
argument for the `allas-conf` command: 
```text
allas-conf project_2001659
```
Now the configuration process asks only for the CSC password and then sets up the connection to the Allas project project_2001659.
As the Puhti scratch directory is shared by all project members, we create a user specific subdirectory (kkayttaj):
```text
mkdir kkayttaj
cd kkayttaj/
```
With the command `a-list`,we can now see the objects that were just uploaded from Mahti to Allas:

<pre>[kkayttaj@puhti-login2 kkayttaj]$ <b>a-list</b> 
2001659-mahti-SCRATCH
[kkayttaj@puhti-login2 kkayttaj]$ <b>a-list 2001659-mahti-SCRATCH</b>
2001659-mahti-SCRATCH/genomes/zebrafish.tar
2001659-mahti-SCRATCH/genomes/zebrafish/Danio_rerio.GRCz10.fa
</pre>

Locating data is easy as there are only two objects in the bucket, but as more data is added to Allas, 
locating a specific file among dozens of buckets containing hundreds of objects may be difficult. 
In that case, you can search for a specific file with the command `a-find`. In this example, I can check if 
an object contains the file Danio_rerio.GRCz10.fa:

<pre>[kkayttaj@puhti-login2 kkayttaj]$ <b>a-find -a Danio_rerio.GRCz10.fa</b> 
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
</pre>

The `a-find` report above tells that, for example, the object _2001659-mahti-SCRATCH/genomes/zebrafish.tar_ contains 
two files whose names match Danio_rerio.GRCz10.fa (the other file is _Danio_rerio.GRCz10.fa.fai_). Note that `a-find` finds 
matches only among objects that were uploaded with `a-put`.

Next we download the data to Puhti using the `a-get` command:

<pre>[kkayttaj@puhti-login2 kkayttaj]$ <b>a-get 2001659-mahti-SCRATCH/genomes/zebrafish.tar</b>
Starting to copy data from allas...
Object:
  2001659-mahti-SCRATCH/genomes/zebrafish.tar
copied and uncompressed from allas into:
  zebrafish</pre>

After this, the current working directory in Puhti has a new directory, _zebrafish_, that contains the files that 
were previously uploaded from Mahti to Allas.

<pre>[kkayttaj@puhti-login2 kkayttaj]$ <b>ls zebrafish/</b>
Danio_rerio.GRCz10.91.1.bt2  Danio_rerio.GRCz10.91.3.bt2  
Danio_rerio.GRCz10.91.2.bt2  Danio_rerio.GRCz10.91.4.bt2
Danio_rerio.GRCz10.91.rev.1.bt2  Danio_rerio.GRCz10.fa
Danio_rerio.GRCz10.91.rev.2.bt2  Danio_rerio.GRCz10.fa.fai
</pre>

# Example 2: Using Allas with rclone <a name="e2"></a>

## A. Uploading data with rclone

Rclone is the power user tool for Allas. It is good in cases where the data must be stored as each file being a separate object.

!!! warning
    Rclone provides a fast and effective way to use Allas, but you should use it carefully as rclone operations can _overwrite_ 
    and _remove_ data both in Allas and in the local disk environment without notifying or asking for confirmation.

*    [Using Allas with rclone from Puhti and Mahti](./using_allas/rclone.md)

This example uses the same data as the previous case: in the _scratch_ directory of Mahti, we have a sub directory
_genomes/zebrafish_  that contains the eight files listed below:

<pre><b>ls /scratch/project_2001659/genomes/zebrafish</b>
Danio_rerio.GRCz10.91.1.bt2  Danio_rerio.GRCz10.91.2.bt2  
Danio_rerio.GRCz10.91.3.bt2  Danio_rerio.GRCz10.91.4.bt2  
Danio_rerio.GRCz10.91.rev.1.bt2  Danio_rerio.GRCz10.91.rev.2.bt2  
Danio_rerio.GRCz10.fa  Danio_rerio.GRCz10.fa.fai
</pre>

To copy the content of this directory to Allas, we first login to *mahti.csc.fi* and set up the Allas environment:
```text
module load allas
```
Then we open a connection to Allas with the command `allas-conf`. The command asks for the CSC password (xxxxxxxxxxx) and 
then lists the Allas projects that are accessible for the user. In this case, we select *project_2001659*.

<pre>[kkayttaj@mahti-login11 ~]$ <b>allas-conf</b>
Please enter CSC password for account kkayttaj: 
<b>xxxxxxxxxx</b>
Checking projects available for your account.
Please wait.
1) project_2000982     2) project_2001659     3) project_2000136      4) abort allas_conf
Please choose a project by giving an item number from the list above: <b>2</b>

allas connection configured successfully.
Connection stays active for eight hours.
</pre>

The `allas-conf` procedure above defines an Allas connection that is valid for eight hours. 
Next, I go to the _zebrafish_ directory.
```text
cd /scratch/project_2001659/genomes/zebrafish
```

Instead of `a-put` that was used in the previous example, we use command `rclone copyto` to copy all  
files from the given directory to Allas. In the case of `rclone`, there is no default bucket. Instead, we have 
to define a bucket. In this example, I use the bucket name _2001659-genomes_ and
define each object name to have the prefix _zebrafish_.

```text
rclone copyto zebrafish/ allas:2001659-genomes/zebrafish
```

After copying the files, I use `rclone ls` to see what has been uploaded to Allas. 

<pre>[kkayttaj@mahti-login11 genomes] <b>rclone ls allas:2001659-genomes/zebrafish</b>
450646234 Danio_rerio.GRCz10.91.1.bt2
334651392 Danio_rerio.GRCz10.91.2.bt2
   187325 Danio_rerio.GRCz10.91.3.bt2
334651387 Danio_rerio.GRCz10.91.4.bt2
450646234 Danio_rerio.GRCz10.91.rev.1.bt2
334651392 Danio_rerio.GRCz10.91.rev.2.bt2
1362788082 Danio_rerio.GRCz10.fa
      715 Danio_rerio.GRCz10.fa.fai
</pre>

## B. Downloading the data to Puhti

Next, we download the same data to Puhti. After connecting to _puhti.csc.fi_, we go to the scratch directory of 
project_2001659 and load the allas module:
```text
cd /scratch/project_2001659
module load allas
```
In this case, we want to use Allas with the project project_2001659, so we can give the project name as an argument for the `allas-conf` command: 
```text
allas-conf project_2001659
```
Now the configuration process asks only for the CSC password and then sets up the connection to the Allas project *project_2001659*.
As the Puhti scratch directory is shared by all project members, we create a user specific subdirectory (kkayttaj), if it is not yet created, and go there:
```text
mkdir kkayttaj
cd kkayttaj/
```
we can now use the command `rclone lsd` to check the available buckets in Allas:

<pre>[kkayttaj@puhti-login2 kkayttaj]$ <b>rclone lsd allas:</b>
  3268222761 2020-10-03 10:01:42         8 2001659-genomes
  2576778428 2020-10-03 10:01:42         4 2001659-mahti-SCRATCH
</pre>

Now we see two buckets. _2001659-genomes_ is the one that was just created in this 
example, while _2001659-mahti-SCRATCH_ originates from the previous a-command example.  
Next, we list the objects in the _2001659-genomes_ bucket:

<pre>[kkayttaj@puhti-login2 kkayttaj]$ <b>rclone ls allas:2001659-genomes</b>
450646234 zebrafish/Danio_rerio.GRCz10.91.1.bt2
334651392 zebrafish/Danio_rerio.GRCz10.91.2.bt2
   187325 zebrafish/Danio_rerio.GRCz10.91.3.bt2
334651387 zebrafish/Danio_rerio.GRCz10.91.4.bt2
450646234 zebrafish/Danio_rerio.GRCz10.91.rev.1.bt2
334651392 zebrafish/Danio_rerio.GRCz10.91.rev.2.bt2
1362788082 zebrafish/Danio_rerio.GRCz10.fa
      715 zebrafish/Danio_rerio.GRCz10.fa.fa
</pre>

Finally, we use the `rclone copyto` command to copy the data from Allas to Puhti in a new directory _zebrafish2_. 

<pre>[kkayttaj@puhti-login2 kkayttaj]$ <b>rclone -P copyto allas:2001659-genomes/zebrafish zebrafish2</b>
Transferred:        3.044G / 3.044 GBytes, 100%, 323.600 MBytes/s, ETA 0s
Errors:                 0
Checks:                 0 / 0, -
Transferred:            8 / 8, 100%
Elapsed time:        9.6s

[kkayttaj@puhti-login2 kkayttaj]$ <b>ls zebrafish2</b>
Danio_rerio.GRCz10.91.1.bt2  Danio_rerio.GRCz10.91.3.bt2  
Danio_rerio.GRCz10.91.2.bt2  Danio_rerio.GRCz10.91.4.bt2
Danio_rerio.GRCz10.91.rev.1.bt2  Danio_rerio.GRCz10.fa
Danio_rerio.GRCz10.91.rev.2.bt2  Danio_rerio.GRCz10.fa.fai</pre>

# Example 3: Uploading large files to Allas <a name="e3"></a>

In the previous two examples, the actual amount of data was rather moderate, only some gigabytes. If the size of an individual data file is 
hundreds of gigabytes or more, the transport of only a few files may take longer than the duration 
of the token-based Allas authentication.

In this example, I use `a-put` to upload a set of large files from Mahti to Allas.

The first thing to do is to open a Mahti connection that can remain running for a long time.
In this example, I use _screen_ command to open a session that I can leave running in the background.
```text
ssh csc-username@mahti.csc.fi
screen
```
The `screen` command starts a virtual session in the login node of Mahti. You can leave this virtual screen session
running in the background and log out from Mahti but you should check which login node (mahti-login11, mahti-login12, mahti-login13 or mahti-login14) 
your session is running on because you need to log in to the same node to reconnect to your `screen` session later on.

In the screen session, I first load the _allas module_ and use `allas-conf` to establish a connection to Allas.
```text
module load allas
allas-conf -k
```
Here, `allas-conf` is used with the option `-k` that saves the Allas password in an environment variable ($OS_PASSWORD), 
so that the connection to Allas can later be automatically reconfigured without the need to define the password again.

After opening the Allas connection, we move to the directory _my_data_ where I have a set of subdirectories (50, 90, 100). I list the gzip-compressed files in these directories: 

<pre>[kkayttaj@mahti-login11 ~] <b>cd /scratch/project_2001659/my_data</b>
[kkayttaj@mahti-login my_data] <b>ls -lh */*.gz</b>
-rw-rwxr-x 1 kkayttaj csc  45G May  8 12:57 100/uniref100.fasta.gz
-rw-rwxr-x 1 kkayttaj csc  61G Jun  5 13:09 100/uniref100.xml.gz
-rw-rwxr-x 1 kkayttaj csc 589M Jun  5 13:09 50/uniref50.fasta.gz
-rw-rwxr-x 1 kkayttaj csc  17G Jun  5 13:09 50/uniref50.xml.gz
-rw-r-xr-x 1 kkayttaj csc 4.2G Jul  6 09:46 90/uniref90.fasta.gz
-rw-rwxr-x 1 kkayttaj csc  33G Jun  5 13:09 90/uniref90.xml.gz
</pre>


Next, I launch the upload process. In this case, I do not use the default bucket name but assign the name to be _2001659-uniref_
```text
a-put -b 2001659-uniref  */*.gz
```
This command uploads the files listed above to Allas.

We could launch the same upload alternative with `rclone copy`:
```text
for f in */*.gz
do
rclone copy $f allas:2001659-uniref
done
```
 
we can leave the session running in the background by pressing `Ctrl-a d`.

Now, we can log out from Mahti, but the screen session remains active in the Mahti login node I use (in this case, _mahti-login11_).

To connect to this session, we first connect to the Mahti node where the screen session is running:
```text
ssh csc-username@mahti-login11.csc.fi
```
Then, we reattach the screen session:
```
screen -r
``` 

Once the _a-put_ command is finished, we will run `a-check` command to check if all the data objects have been created.
_a-check_ needs to be executed with exactly the same options that  were used with the _a-put_ command.  
So in this case the command would be:

```text
a-check -b 2001659-uniref  */*.gz
```

The _a-check_ command compares the item names to be uploaded to the matching objects in Allas. 
The files or directories that don't have a target object Allas, are reported and stored to a file. 
In this case, if some of the objects in the _a-put_ command above would be missing, then a-check would list the missing 
files and directories in file _missing_2001659-uniref_63449_ (the number in the end is just a random number).

This file of missing items can be used with a-put option `--input-list`, to continue the failed upload process:
```text
a-put -b 2001659-uniref --nc --input-list missing_2001659-uniref_63449
```
You should note, that _a-check_ does does not check if the actual contents of the object is correct. 
It checks only the object names, which may originate from some other sources.



#Example 4: Uploading complex directory structures to Allas <a name="e4"></a>

Some workflows and software create complex directory structures to store and manage data. You might have directories that have 
thousands or even millions of individual files. Copying these kinds of datasets to Allas takes time and is not
always straightforward. The most reasonable way to upload this kind of data depends on the case. This example introduces a few alternatives.

First, I open a `screen` session on Puhti and set up an Allas connection just like in the previous example:
```text
ssh csc-username@puhti.csc.fi
screen
module load allas
allas-conf -k
```

Suppose we have a directory structure that contains images of road condition cameras from ten locations with an interval of ten minutes 
from the years 2014–2018. The data is located in the directory *road_cameras* where each location has its own subdirectory (ten directories). 
Inside each subdirectory, there is another layer of subdirectories, one for each year (five subdirectories), each containing subdirectories for every day of the year (further 365 subdirectories), each containing 144 small image files. 

For example:
```text
road_cameras/site_7/2017/day211/image_654887.jpg
```
Thus, the total number of files in the _road_cameras_ directory is 10 * 5 * 365 * 144 = 2 628 000.

In principle, you could copy all 2,6 million files as separate objects to Allas, but in that case, you should split the data into multiple buckets as one bucket can have at most 0,5 million objects. You could, for example, run a separate `rclone` command for each _site_ directory 
and put the data from each site to a site-specific bucket:

```text
rclone copyto road_cameras/site_1 allas:2001659_road_cameras_site_1/
```
This way, you would end up creating ten buckets each containing 262 800 objects. 
This approach could be the most effective way for storing and reusing the data, if you know that you will need to
access individual images randomly.

As another extreme option, your could use `a-put` and collect all data into one compressed object. In order to do that, you
must add the option _--skip-filelist_ to the `a-put` command. By default, `a-put` collects detailed metadata of **each** file in a _ameta_ file. 
However, if you have thousands of files, collecting this information takes a long time. If you need to know the file names, 
you can use the _--simple-fileslist_ option to collect the names – but **no** other information – of the files in the metadata file. 
This already speeds up the preprocessing significantly. However, as in this case the naming has been systematic, storing the file names to the metadata files can be just ignored altogether (`--skip-filelist`), which is the fastest option.

```text
a-put --skip-filelist road_cameras/
```
This approach would store all 2,6 million files as one object.

In practice, the optimal way of storing the data is often between these two extremes. As a compromise, you could apply packing at a higher level in the hierarchy.

For example:
```text
a-put --skip-filelist road_cameras/site_*
```
This would produce ten objects, each containing all information from one camera site.
Alternatively, you could do the compression so that data from each year from each camera is collected as one object:
```text
a-put --skip-filelist road_cameras/site_*/20*
```
This last option would store the data as 50 objects. Day-based objects for each camera might be the most practical 
option for using the data later on but, as a downside, preprocessing the data into 10 * 5 * 365 = 18250 objects 
probably takes quite a long time.

Copying millions of files to Allas takes a long time regardless of the method. If you have started the `a-put` command inside a `screen` session, you can detach from the virtual session by pressing `Ctrl-a-d` to log out from Puhti and leave the upload process running for days. 

Once the _a-put_ command is finished, you can run `a-check` command to check if all the data objects have been created. 
You should run _a-check_ using exactly the same options that you used with _a-put_.  So in this case the command could be:

```text
a-check --skip-filelist road_cameras/site_*/20*
```

The _a-check_ command compares the item names to be uploaded to the matching objects in Allas. 
The files or directories that don't have a target object Allas, are reported and stored to a file. 
In this case, if some of the objects in the a-put command above would be missing, then a-check would list the missing 
files and directories in file _missing_bucket_name_number_ (the number in the end is just a random nuber).

This file of missing items can be used with a-put option `--input-list`, to continue the failed upload process:
```text
a-put -b 2001659-uniref --nc --input-list missing_bucket_name_number
```
You should note, that _a-check_ does does not check if the actual contents of the object is correct. 
It checks only the object names, which may originate from some other sources.


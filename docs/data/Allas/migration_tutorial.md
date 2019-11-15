# Using Allas to migrate your data from Taito to Puhti 

Taito.csc.fi cluster will be closed at the end of 2019. If you have some data that you want 
to preserve in the directories of Taito (including $HOME, $WRKDIR and project directories) 
you have to copy the data elsewhere before 1.1. 2020. 

The new Allas object storage service provides a platform that you can use to store your data that is currently in the disks of Taito. 

*    [Allas user guide](./index.md)

The new Puhti server, that is replacing Taito, does not provide permanent storage space for research data. Even if you would continue your work immediately in Puhti, it is good to make a longer term copy of your data to Allas. This is achieved by migrating your data from Taito to Puhti through Allas.

*    [Puhti quick start guide](../../support/tutorials/puhti_quick.md)

This tutorial provides four examples of moving data first from Taito to Allas and then from Allas to Puhti.

1.   [The first example](#e1) uses a-commands (a-put, a-get) for moving data from Taito to Puhti
2.   [The second example](#e2) the same data is transported using rclone.
3.   [The third example](#e3) focuses in uploading large files from Taito to Allas 
4.   [The fourth example](#e4) studies case where the dataset to be copied includes large amount iof files

The first approach is useful in cases where the data is mainly used in the CSC computing environment (Taito, Puhti, Mahti). While
the second option (rclone) is good for cases where the data will be used outside CSC too.

The tutorials are based on interactively executed commands and thus they apply only for relatively small datasets (max some hundreds of GBs).

## NEW! Datamangler

A new temporary service, Datamangler, was taken in use on Novmber 12th 2019 to support data migration from Taito to Allas.
Datamangler includes a set of nodes that have access to the Taito disk area and fast connection to Allas service. Datamangler should be used for data transport only. 

To access Datamangler, use address: datamangler.csc.fi. For example

```text
  ssh csc-user-account@datamangler.csc.fi
```

We recommend you to use Datamangler to transfer your files to Allas, as their transfer capacity is significantly greater
than from Taito login node or Taito-shell. All of them have the same data transport commands and procedures.



## 1. Get access to Allas
By default the CSC computing projects do not have access to Allas. Thus, the first thing is to add 
Allas service for your project.  This is done with the [MyCSC](https://my.csc.fi) interface. 
Note that only the project manager can apply for the access. Once access is granted all project 
members must visit MyCSC service and accept the term of use for Allas, before they can use the Allas 
storage area.


The default storage quota in Allas is 10 TB.  As this space is shared with all project members it is quite 
possible that this is not enough. In that case you should estimate how much space is needed and then send 
a request for more space. Note, that files stored in Allas consume billing units.
The request should be sent to **servicedesk@csc.fi**.
Please include to your quota request:

   *    ID/name of your project
   
   *    amount Allas space needed
   
   *    a shot description of the data to be stored 

# Migration example 1: A-commands <a name="e1"></a>

## A. Uploading data from Taito to Allas

A-commands are Allas specific help tools that allow you to have an easy start with Allas.  
A-commands pack, compress and move data automatically. This reduces the storage space needed, but on
the other hand, makes the storage process slower. A-commands are a good option for miscellaneous data 
that compresses well and is mostly used in CSC environment. 


In this example in my Taito $WRKDIR I have a sub directory: _genomes/zebrafish_ that contains eight files listed below:
<pre><b>ls $WRKDIR/genomes/zebrafish</b>
Danio_rerio.GRCz10.91.1.bt2  Danio_rerio.GRCz10.91.2.bt2  
Danio_rerio.GRCz10.91.3.bt2  Danio_rerio.GRCz10.91.4.bt2  
Danio_rerio.GRCz10.91.rev.1.bt2  Danio_rerio.GRCz10.91.rev.2.bt2  
Danio_rerio.GRCz10.fa  Danio_rerio.GRCz10.fa.fai
</pre>

To copy the content of this directory to Allas, I first login to datamangler.csc.fi and set up the Allas environment in with command:
```text
module load allas
```
Then I open connection to Allas with command `allas-conf`. The command asks for my CSC password (xxxxxxxxxxx)  and 
then lists those Allas projects that are accessible for me. In this case I select project_2001659.
<pre>[kkayttaj@datamangler03:~><b> allas-conf</b>
Please enter CSC password for account kkayttaj: 
xxxxxxxxxx
Checking projects available for your account.
Please wait.
1) project_2000982     2) project_2001659     3) project_2000136      4) abort allas_conf
Please choose a project by giving an item number form the list above: <b>2</b>

allas connection configured successfully.
Connection stays active for eight hours.
</pre> 

Allas-conf opens a connection to the specified Allas project for eight hours. If you want to start using some
other project, you need to run allas-conf again. However in one shell session, you can have only one Allas project active at a time.
    

Next I go to the _zebrafish_ directory.
```text
cd $WRKDIR/genomes/zebrafish
```
I can now upload files one-by-one to Allas with `a-put` command. For example:
```text
a-put Danio_rerio.GRCz10.fa
```
In the end of the upload process the command reports:
```text
-------------------------------------------------------------------------------
1 files from Danio_rerio.GRCz10.fa uploaded to bucket kkayttaj-2001659-taito-WRKDIR in Allas as one compressed file: 
kkayttaj-2001659-taito-WRKDIR/genomes/zebrafish/Danio_rerio.GRCz10.fa.zst
-----------------------------------------------------------------

Upload summary:
              Date                      Name  Files Size(kB)         Location in allas
 15.11.19 09:11:53     Danio_rerio.GRCz10.fa      1  1330852 kkayttaj-2001659-taito-WRKDIR/genomes/zebrafish
-----------------------------------------------------------------
OK
```
So in this case the file was uploaded to Allas into bucket:
   _kkayttaj-2001659-taito-WRKDIR_
as object:
  _genomes/zebrafish/Danio_rerio.GRCz10.fa.zst_ .
In this case I used the default bucket and object names assigned by `a-put`, but other bucket and object 
names coulud be defined with command line options `-b`  and `-o`.
Now command _a-list_ shows that I have one bucket in Allas and that the bucket contains one object.
<pre>[kkayttaj@datamangler03:zebrafish><b> a-list</b>
kkayttaj-2001659-taito-WRKDIR
[kkayttaj@datamangler03:zebrafish><b> a-list kkayttaj-2001659-taito-WRKDIR</b>
kkayttaj-2001659-taito-WRKDIR/genomes/zebrafish/Danio_rerio.GRCz10.fa.zst</pre>

Moving data to Allas file-by-file is slow and produces large amounts of objects. It is often more efficient to 
upload data to Allas one directory at a time and store the data in bigger chunks. For example, to upload the 
zebrafish directory I first go to the _genomes_ directory:
```text
cd $WRKDIR/genomes
```
and then use `a-put` to upload the whole zebrafish directory to Allas as one object.
```text
a-put zebrafish/
```
In the end of the upload process the command reports:
```text

-------------------------------------------------------------------------------
8 files from zebrafish uploaded to bucket kkayttaj-2001659-taito-WRKDIR in Allas as one compressed file: 
kkayttaj-2001659-taito-WRKDIR/genomes/zebrafish.tar.zst
-----------------------------------------------------------------

Upload summary:
              Date                      Name  Files Size(kB)         Location in allas
 15.11.19 09:11:39                 zebrafish      8  3191664 kkayttaj-2001659-taito-WRKDIR/genomes
-----------------------------------------------------------------
OK
```
After this I have another object in kkayttaj-2001659-taito-WRKDIR bucket:
<pre>[kkayttaj@datamangler03:genomes><b> a-list kkayttaj-2001659-taito-WRKDIR</b>
kkayttaj-2001659-taito-WRKDIR/genomes/zebrafish.tar.zst
kkayttaj-2001659-taito-WRKDIR/genomes/zebrafish/Danio_rerio.GRCz10.fa.zst</pre>

Note that in fact the file _Danio_rerio.GRCz10.fa_ is now stored to Allas two times: 
As an individual compressed object (genomes/zebrafish/Danio_rerio.GRCz10.fa.zst)
and as part of the _genomes/zebrafish.tar.zst_ object.

## B. Download in Puhti
Next I download the same data to Puhti. After connecting to puhti.csc.fi I go to the scratch directory of 
project  2001659 and load allas module:
```text
cd /scratch/project_2001659
module load allas
```
In this case I know that I want to use Allas with project project_2001659 so I can give the project name as an 
argument for allas-conf command: 
```text
allas-conf project_2001659
```
Now the configuration process asks just for the CSC password and then sets up the connection to Allas project project_2001659.
As the Puhti scratch directory is shared by all project members, I make a my own subdirectory (kkayttaj) and go there:
```text
mkdir kkayttaj
cd kkayttaj/
```
With command _a-list_ I can now see the objects I just uploaded from Taito to Allas

<pre>[kkayttaj@puhti-login2 kkayttaj]$ <b>a-list</b> 
kkayttaj-2001659-taito-WRKDIR
[kkayttaj@puhti-login2 kkayttaj]$ <b>a-list kkayttaj-2001659-taito-WRKDIR</b>
kkayttaj-2001659-taito-WRKDIR/genomes/zebrafish.tar.zst
kkayttaj-2001659-taito-WRKDIR/genomes/zebrafish/Danio_rerio.GRCz10.fa.zst</pre>

Locating my data is easy as there are just two objects in the bucket, but as more data is added to Allas, 
locating a specific file from dozens of buckets containing hundreds of objects, may be difficult. 
In that case, you can search for a specific file with command: `a-find`. In this case I could check if 
some object contains file Danio_rerio.GRCz10.fa with command:

<pre>[kkayttaj@puhti-login2 kkayttaj]$ <b>a-find -a Danio_rerio.GRCz10.fa</b>
----------------------------------------------
Checking bucket: kkayttaj-2001659-taito-WRKDIR
Object: kkayttaj-2001659-taito-WRKDIR/genomes/zebrafish.tar.zst 
includes 2 file names that that match query: Danio_rerio.GRCz10.fa
Object: kkayttaj-2001659-taito-WRKDIR/genomes/zebrafish/Danio_rerio.GRCz10.fa.zst
includes 1 file names that that match query: Danio_rerio.GRCz10.fa
------------------------------------------------ 
Query: Danio_rerio.GRCz10.fa
Total of 3 hits were found in 2 objects
-------------------------------------------------</pre>

The _a-find_ report above tells that for example object _kkayttaj-2001659-taito-WRKDIR/genomes/zebrafish.tar.zst_ contains 
two files whose names match Danio_rerio.GRCz10.fa ( the other file is _Danio_rerio.GRCz10.fa.fai_). Note that `a-find` finds 
matches only from objects that were uploaded with `a-put`.

Now lets’ download the data to Puhti. This is done with `a-get` command:
<pre>[kkayttaj@puhti-login2 kkayttaj]$<b> a-get kkayttaj-2001659-taito-WRKDIR/genomes/zebrafish.tar.zst</b>
Starting to copy data from allas...
Object:
  kkayttaj-2001659-taito-WRKDIR/genomes/zebrafish.tar.zst 
copied and uncompressed from allas into:
  zebrafish</pre>
After this, the current working directory in Puhti has a new directory, _zebrafish_, that contains the files that 
were previously uploaded from Taito to Allas.

<pre>[kkayttaj@puhti-login2 kkayttaj]$<b> ls zebrafish/</b>
Danio_rerio.GRCz10.91.1.bt2  Danio_rerio.GRCz10.91.3.bt2  
Danio_rerio.GRCz10.91.2.bt2  Danio_rerio.GRCz10.91.4.bt2
Danio_rerio.GRCz10.91.rev.1.bt2  Danio_rerio.GRCz10.fa
Danio_rerio.GRCz10.91.rev.2.bt2  Danio_rerio.GRCz10.fa.fai</pre>


# Migration example 2: rclone <a name="e2"></a>

## A. Uploading data in Taito
Rclone is the power user tool for Allas. It is good in cases where the data does not compress much and in cases where 
the data must be stored so that each file is stored as a separate object.
Rclone provides a fast and effective way to use Allas, but you should use it carefully as rclone operations can overwrite 
and remove data both in Allas and in the local disk environment without notifying or asking for confirmation.

*    [Using Allas with rclone from Puhti and Taito](./using_allas/rclone.md)

This example uses the same data as the previous case:  in my Taito $WRKDIR I have a sub directory:
_genomes/zebrafish_  that contains eight files listed below:
<pre><b>ls $WRKDIR/genomes/zebrafish</b>
Danio_rerio.GRCz10.91.1.bt2  Danio_rerio.GRCz10.91.2.bt2  
Danio_rerio.GRCz10.91.3.bt2  Danio_rerio.GRCz10.91.4.bt2  
Danio_rerio.GRCz10.91.rev.1.bt2  Danio_rerio.GRCz10.91.rev.2.bt2  
Danio_rerio.GRCz10.fa  Danio_rerio.GRCz10.fa.fai
</pre>

To copy the content of this directory to Allas, I first login to datamangler.csc.fi and set up the Allas environment in with command:
```text
module load allas
```
Then I open connection to Allas with command `allas-conf`. The command asks for my CSC password (xxxxxxxxxxx)  and 
then lists those Allas projects that are accessible for me. In this case I select project_2001659.
<pre>[kkayttaj@datamangler03:~><b> allas-conf</b>
Please enter CSC password for account kkayttaj: 
xxxxxxxxxx
Checking projects available for your account.
Please wait.
1) project_2000982     2) project_2001659     3) project_2000136      4) abort allas_conf
Please choose a project by giving an item number form the list above: <b>2</b>

allas connection configured successfully.
Connection stays active for eight hours.
</pre>
Allas-conf procedure above defines an Allas-connection that is valid for next eightt hours. 
Next I go to the _zebrafish_ directory.
```text
cd $WRKDIR/genomes/zebrafish
```

In stead of _a-put_, that was used in the previous example, I now use command `rclone copyto` to copy all the 
files from the given directory to Allas. In the case of _rclone_ there is no default bucket. In stead I have 
to define a bucket to be used. This example I use bucket name _2001659-genomes_ and
define that each object name should have prefix _zebrafish_.

<pre>[kkayttaj@c311:genomes><b>rclone copyto zebrafish/ allas:2001659-genomes/zebrafish</b></pre>

After copying the files I use `rclone ls` to see what has been uploaded to Allas. 

<pre>[kkayttaj@c311:genomes><b>rclone ls allas:2001659-genomes/zebrafish</b>
450646234 Danio_rerio.GRCz10.91.1.bt2
334651392 Danio_rerio.GRCz10.91.2.bt2
   187325 Danio_rerio.GRCz10.91.3.bt2
334651387 Danio_rerio.GRCz10.91.4.bt2
450646234 Danio_rerio.GRCz10.91.rev.1.bt2
334651392 Danio_rerio.GRCz10.91.rev.2.bt2
1362788082 Danio_rerio.GRCz10.fa
      715 Danio_rerio.GRCz10.fa.fai</pre>

## B. Downloading the data to Puhti

Next I download the same data to Puhti.  After connecting to _puhti.csc.fi_ I go to the scratch directory of 
project_2001659 and load allas module:
```text
cd /scratch/project_2001659
module load allas
```
In this case I know that I want to use Allas with project project_2001659 so I can give the project name as an argument for `allas-conf` command: 
```text
allas-conf project_2001659
```
Now the configuration process asks just for the CSC password and then sets up the connection to Allas project project_2001659.
As the Puhti scratch directory is shared by all project members, I make a my own subdirectory (kkayttaj), if it is not yet created, and go there:
```text
mkdir kkayttaj
cd kkayttaj/
```
I can now use command `rclone lsd` to check the available buckets in Allas:

<pre>[kkayttaj@puhti-login2 kkayttaj]$<b> rclone lsd allas:</b>
  3268222761 2019-10-03 10:01:42         8 2001659-genomes
  2576778428 2019-10-03 10:01:42         4 kkayttaj-2001659-taito-WRKDIR</pre>
  
Now I can see two buckets: _2001659-genomes_ is the one that was just created in this 
example while _kkayttaj-2001659-taito-WRKDIR_ originates form the previous a-command example.  
Next we list objects in the 2001659-genomes bucket:

<pre>[kkayttaj@puhti-login2 kkayttaj]$<b> rclone ls allas:2001659-genomes</b>
450646234 zebrafish/Danio_rerio.GRCz10.91.1.bt2
334651392 zebrafish/Danio_rerio.GRCz10.91.2.bt2
   187325 zebrafish/Danio_rerio.GRCz10.91.3.bt2
334651387 zebrafish/Danio_rerio.GRCz10.91.4.bt2
450646234 zebrafish/Danio_rerio.GRCz10.91.rev.1.bt2
334651392 zebrafish/Danio_rerio.GRCz10.91.rev.2.bt2
1362788082 zebrafish/Danio_rerio.GRCz10.fa
      715 zebrafish/Danio_rerio.GRCz10.fa.fa</pre>

Finally I use `rclone copyto` command to copy the data from Allas to Puhti into new directory _zebrafish2_. 

<pre>[kkayttaj@puhti-login2 kkayttaj]$<b> rclone -P copyto allas:2001659-genomes/zebrafish zebrafish2</b>
Transferred:        3.044G / 3.044 GBytes, 100%, 323.600 MBytes/s, ETA 0s
Errors:                 0
Checks:                 0 / 0, -
Transferred:            8 / 8, 100%
Elapsed time:        9.6s

[kkayttaj@puhti-login2 kkayttaj]$<b> ls zebrafish2</b>
Danio_rerio.GRCz10.91.1.bt2  Danio_rerio.GRCz10.91.3.bt2  
Danio_rerio.GRCz10.91.2.bt2  Danio_rerio.GRCz10.91.4.bt2
Danio_rerio.GRCz10.91.rev.1.bt2  Danio_rerio.GRCz10.fa
Danio_rerio.GRCz10.91.rev.2.bt2  Danio_rerio.GRCz10.fa.fai
</pre>

# Migration example 3: Uploading large files from Taito to Allas <a name="e3"></a>

In the previous two examples the actual amount of data was rather moderate. Only some gigabytes. If the size of an individual data file is in the level on hundreds of gigabytes or more, the transport of just few files may take longer that is the life time 
of the token based Allas authentication.

In this example we use `a-put` to upload a set of large files from Taito to Allas. We use _datamangler.csc.fi_ as a platform for running the process as it provides faster connection to Allas, than Taito or Taito-shell.

First thing to do is to open a Datamagler connection that we can keep running for a long time. For that 
we have two options:

1.    Using [NoMachine virtual desktop](https://research.csc.fi/csc-guide-connecting-the-servers-of-csc#1.3.3) to connect Taito shell
2.    Using screen command ia way that resembles the Taito-shell case described [here](https://research.csc.fi/taito-faq/-/asset_publisher/ZJfZFkUtMsij/content/6-how-do-i-start-long-running-jobs-in-taito-shell-?)

In this example I have used the second alternative and opened the connection to Datamangler with commands:

```text
ssh datamangler.csc.fi
screen
```
The _screen_ command starts a virtual session in the Datamangler. You can leave this virtual screen session running in the backgound and log out from Datamangler but you should check which datamangler node (datamangler01, datamangler02, datamangler03..) your session is running, because you most log in to the very same node to re-connect your _screen_ session
later on.

In the screen session I first load _allas module_ and use `allas-conf` to establish the connection to Allas.
```text
module load allas
allas-conf -k
```
Here _allas-conf_ is used with option `-k`. This option saves the allas password to a environment variable ($OS_PASSWORD) so that
the connection to Allas can be later on automatically re-configured without need to define the password again.

After opening the Allas connection I move to directory _my_data_ where I have a set subdirectories (50, 90, 100). I list the gzip-compressed files in 
these directories: 

<pre>
[kkayttaj@datamangler03:~> <b>cd $WRKDIR/my_data</b>
[kkayttaj@datamangler03:my_data> <b>ls -lh */*.gz</b>
-rw-rwxr-x 1 kkayttaj csc  45G May  8 12:57 100/uniref100.fasta.gz
-rw-rwxr-x 1 kkayttaj csc  61G Jun  5 13:09 100/uniref100.xml.gz
-rw-rwxr-x 1 kkayttaj csc 589M Jun  5 13:09 50/uniref50.fasta.gz
-rw-rwxr-x 1 kkayttaj csc  17G Jun  5 13:09 50/uniref50.xml.gz
-rw-r-xr-x 1 kkayttaj csc 4.2G Jul  6 09:46 90/uniref90.fasta.gz
-rw-rwxr-x 1 kkayttaj csc  33G Jun  5 13:09 90/uniref90.xml.gz
</pre>

Most of the modern non-ascii file formats (i.e. binary data) that are used for large datasets, store the data in very dense format. Thus these files do not benefit from compressing the data. The same applies of course to files that have already been compressed. For this kind of data it is reasonable to use `a-put` command with the `--nc` option that skips the compression and uploads the file to Allas as it is. However, when compression is not used, `a-put` does not accept directories, only individual files. Because of that is is good to run a check, like the _ls -lh_ command above, to ensure that input will contain only files.

Next I launch the upload process. In this case I don't use the default bucket name but I assign the name to be _2000136-uniref_

```text
 a-put -b  2000136-uniref --nc  */*.gz
```
This command starts loading the files, listed above, to Allas.

I could launch the same upload alternative with `rclone copy`:

```text
for f in */*.gz
do
rclone copy $f allas:2000136-uniref
done
```
 
I can now leave the session running in the background by pressing: _Ctrl-a d_.

Now I can logout from Datamagler, but the screen session in the Datamangler node I use (in this case _datamangler03_ )and the is preserved and active.

To reattach to this session, I first connect to the Datamangler node where the screen session is running. For example:
```text
ssh datamangler03.csc.fi
```
Then,  I reattach the screen session with command:
```
screen -r
``` 


# Migration example 4: Uploading complex directory structures from Taito to Allas <a name="e4"></a>

Some workflows and software create complex direcotory structures to store and manage data. Thus you can have directories that have thousands or even millions of individual files. Copying of this kind of datasets from Taito to Allas takes time and is not
always straight forward. The most reasonable way to upload this kind of data depends on the case. This example shows some alternative ways how to upload this kind of directories.

First we open screen session in Datamangler and set up Allas connection just like in the previous example:

```text
ssh datamangler.csc.fi
screen
module load allas
allas-conf -k
```

Now lets assume that we have a directory structure that contains images of road condition cameras from ten locations with the interval of 10 minutes from years 2014-2018. The data locates in directory "road_cameras" so that each location has its' own sub-directory (10 directories). Inside this sub-directory we have directory level for each year( 5 directories) and day (365 directories), each containing 144 small image files. 

For example
```text
road_cameras/site_7/2017/day211/image_654887.jpg
```
Thus the total number of files in the _road_cameras_ directory is: 10 * 5 * 365 * 144 = 2 628 000.

In principle you could copy all the 2,6 million files as separate objects to Allas, but in that case you should split the data into multiple buckets as by default one bucket can have in maximum 1 million objects.  You could for example run a separate _rclone_ command for each _site_ directory and put data from each site to a site specific bucket. For example

```text
rclone road_cameras/site_1 allas:20000136_road_cameras_site_1/
```
Thus you would end up creating ten buckets each containing 262 800 objects. 

However it is quite probable that this approach is the most effective way for storing and re-using the data.
As another extreme, your could use _a-put_ and collect all the data into one compressed object. If you do that you
must add option _--skip-filelist_ to the _a-put_ command. By default _a-put_ collects detailed metadata of each file to the _ameta_ file. However, if you have thousands of files, collecting this information  will take a long time. If you need to know the file names, you can use _--simple-fileslist_ option to just collect the names, but no other information, of the files to the metadatafile. This already speeds up the pre-processing significantly. However, as in this case the naming has been systematic, storing of the file names to the metadata files can be just ignored (--skip-filelist), which is the fastest option.

```text
 a-put --skip-filelist road_cameras/
```
This approach would store all the 2,6 million files into one object. 

In practice the optimal way of storing the data is often between these two extremes. So instead you could apply packing in some higer level in the hierarchy.

For example command:

```text
 a-put --skip-filelist road_cameras/site_*
 ```
 Would in this case produce 10 objects, each containing all the information form one camera site.
 Alternatively, you could do the compression so that data from each year in each camera is collected to one object:
 
 ```text
 a-put --skip-filelist road_cameras/site_*/20*
 ```
 This last option would store the data into 50 objects. Day based objects for each camera might be most handy for using the data later on, but preprocessing the data into 10 * 5 * 365 = 18250 objects will probably take quite a long time.

Copying millions of files to Allas will take a long time regardless of the way you are using. If you have started the _a-put_ command inside a _screen_ session, you can detach from the virtual session by pressing `Ctrl-a-d` log out from the Datamagler and leave the upload process running for days. 









 












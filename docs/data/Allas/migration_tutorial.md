# Using Allas to migrate your data from Taito to Puhti 

Taito.csc.fi cluster will be closed at the end of 2019. If you have some data that you want 
to preserve in the directories of Taito ( including $HOME, $WRKDIR and project directories) 
you have to copy the data elsewhere before 1.1. 2020. 

The new Allas object storage service provides a platform that you can use to store your data that is currently in Taito. 

*    [Allas user guide](./index.md)

The new Puhti server, that is replacing Taito, does not provide permanent storage space for research data. Even if you would continue your work immediately in Puhti, it is good to make a more permanent copy of your data to Allas. This is done if you do the data migration from Taito to Puhti through Allas.

*    [Puhti quick start guide](../../support/tutorials/puhti_quick.md)

This tutorial provides tree examples of moving data first from Taito to Allas and then from Allas to Puhti.

1.   [The first example](#e1) uses a-commands (a-put, a-get) for moving data from Taito to Puhti
2.   [The second example](#e2) the same data is transported using rclone.
3.   [The third example](#e3) focuses in uploading large files from Taito to Allas 

The first approach is useful in cases where the data is mainly used in CSC computing environment (Taito, Puhti, Mahti). While
the second option (rclone) is good for cases where the data will be use outside CSC too.

The tutorials are based on interactively executed commands and thus they apply only for relatively small datasets ( max some hundreds of GBs).




## 1. Get access to Allas
By default the CSC computing projects do not have access to Allas. Thus the first first thing is to add 
Allas service for your project.  This is done with the [MyCSC](https://my.csc.fi) interface. 
Note that only the project manager can apply for the access. Once access is granted all project 
members can use the Allas storage area.











The default storage quota in Allas is 10 TB.  As this space is shared with all project members it is quite 
possible that this is not enough. In that case you should estimate how much space is needed and then send 
a request for more space. The request should be sent to **servicedesk@csc.fi**.
Please include to your quota request:

   *    ID/name of your project
   
   *    amount Allas space needed
   
   *    a shot description of the data to be stored 

# Migration example 1: A-commands <a name="e1"></a>

## A. Uploading data from Taito to Allas

A-commands are Allas specific help tools that allow you to have an easy start with Allas.  
A-commands pack, compress and move data automatically. This reduces the storage space needed but on
the other hand makes the storage process slower. A-commands are a good option for miscellaneous data 
that compresses well and is mostly used in CSC environment. 


In this example in my Taito $WRKDIR I have a sub directory: _genomes/zebrafish_ that contains eight files listed below:
<pre><b>ls $WRKDIR/genomes/zebrafish</b>
Danio_rerio.GRCz10.91.1.bt2  Danio_rerio.GRCz10.91.2.bt2  
Danio_rerio.GRCz10.91.3.bt2  Danio_rerio.GRCz10.91.4.bt2  
Danio_rerio.GRCz10.91.rev.1.bt2  Danio_rerio.GRCz10.91.rev.2.bt2  
Danio_rerio.GRCz10.fa  Danio_rerio.GRCz10.fa.fai
</pre>

To copy the content of this directory to Allas, I first login to Taito or Taito-shell and set up the Allas environment in with command:
```text
module load allas
```
Then I open connection to Allas with command `allas-conf`. The command asks for my CSC password (xxxxxxxxxxx)  and 
then lists those Allas projects that are accessible for me. In this case I select project_2001659.
<pre>[kkayttaj@c311:~><b> allas-conf</b>
Please enter CSC password for account kkayttaj: 
xxxxxxxxxx
Checking projects available for your account.
Please wait.
You have access to following Allas projects:
Project ID        Description
--------------------------------------------
project_2000982   Services for science Kalle Kayttaja
project_2001659   CSC user's maintenance Ossi Huikonen
project_2000136   dis Jana Poranen
Please define the Project ID of the project to be used:
<b>project_2001659</b>

allas connection configured successfully.
</pre>
Allas-conf procedure above defines an Allas-connection that is valid for next three hours. 
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
1 files from Danio_rerio.GRCz10.fa uploaded to bucket kkayttaj-2001659-taito-WRKDIR in 
Allas as one compressed file: 
kkayttaj-2001659-taito-WRKDIR/genomes/zebrafish/Danio_rerio.GRCz10.fa.zst
Upload ready
```
So in this case the file was uploaded to Allas into bucket:
   _kkayttaj-2001659-taito-WRKDIR_
as object:
  _genomes/zebrafish/Danio_rerio.GRCz10.fa.zst_ .
In this case I used the default bucket and object names assigned by _a-put_, but other bucket and object 
names coulud be defined with command line options `-b`  and `-o`.
Now command _a-list_ shows that I have one bucket in Allas and that the bucket contains one object.
<pre>[kkayttaj@c311:zebrafish><b> a-list</b>
kkayttaj-2001659-taito-WRKDIR
[kkayttaj@c311:zebrafish><b> a-list kkayttaj-2001659-taito-WRKDIR</b>
kkayttaj-2001659-taito-WRKDIR/genomes/zebrafish/Danio_rerio.GRCz10.fa.zst</pre>

Moving data to Allas file-by-file is slow and produces large amounts of objects. It is often more efficient to 
upload data to Allas one directory at a time and store the data in bigger chunks. For example to upload the 
zebrafish directory I first go to the _genomes_ directory:
```text
cd $WRKDIR/genomes
```
and then use _a-put_ to upload the whole zebrafish directory to Allas as one object.
```text
a-put zebrafish/
```
In the end of the upload process the command reports:
```text
8 files from zebrafish uploaded to bucket kkayttaj-2001659-taito-WRKDIR in Allas 
as one compressed file: 
kkayttaj-2001659-taito-WRKDIR/genomes/zebrafish.tar.zst
```
After this I have another object in kkayttaj-2001659-taito-WRKDIR bucket:
<pre>[kkayttaj@c311:genomes><b> a-list kkayttaj-2001659-taito-WRKDIR</b>
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

<pre>[kkayttaj@puhti-login2 kkayttaj]$ <b>a_list</b> 
kkayttaj-2001659-taito-WRKDIR
[kkayttaj@puhti-login2 kkayttaj]$ <b>a_list kkayttaj-2001659-taito-WRKDIR</b>
kkayttaj-2001659-taito-WRKDIR/genomes/zebrafish.tar.zst
kkayttaj-2001659-taito-WRKDIR/genomes/zebrafish/Danio_rerio.GRCz10.fa.zst</pre>

Locating my data is easy as there is just two objects in the bucket, but as more data is added to Allas, 
locating a specific file from dozens of  buckets containing hundreds of objects, may be difficult. 
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
two files whose names match Danio_rerio.GRCz10.fa ( the other file is _Danio_rerio.GRCz10.fa.fai_). Note that _a-find_ finds 
matches only from objects that were uploaded with _a-put_.

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
Rclone provides a fast and effective way to use Allas, but you should use it carefully as rclone operations overwrite 
and remove data both in Allas an in the local disk environment without notifying or asking for confirmation.

*    [Using Allas with rclone from Puhti and Taito](./using_allas/rclone.md)

This example uses the same data as the previous case:  in my Taito $WRKDIR I have a sub directory: _genomes/zebrafish_ 
that contains eight files listed below:
<pre><b>ls $WRKDIR/genomes/zebrafish</b>
Danio_rerio.GRCz10.91.1.bt2  Danio_rerio.GRCz10.91.2.bt2  
Danio_rerio.GRCz10.91.3.bt2  Danio_rerio.GRCz10.91.4.bt2  
Danio_rerio.GRCz10.91.rev.1.bt2  Danio_rerio.GRCz10.91.rev.2.bt2  
Danio_rerio.GRCz10.fa  Danio_rerio.GRCz10.fa.fai
</pre>

To copy the content of this directory to Allas, I first login to Taito or Taito-shell and set up the Allas environment in with command:
```text
module load allas
```
Then I open connection to Allas with command `allas-conf`. The command asks for my CSC password (xxxxxxxxxxx)  and 
then lists those Allas projects that are accessible for me. In this case I select project_2001659.
<pre>[kkayttaj@c311:~><b> allas-conf</b>
Please enter CSC password for account kkayttaj: 
xxxxxxxxxx
Checking projects available for your account.
Please wait.
You have access to following Allas projects:
Project ID        Description
--------------------------------------------
project_2000982   Services for science Kalle Kayttaja
project_2001659   CSC user's maintenance Ossi Huikonen
project_2000136   dis Jana Poranen
Please define the Project ID of the project to be used:
<b>project_2001659</b>

allas connection configured successfully.
</pre>
Allas-conf procedure above defines an Allas-connection that is valid for next three hours. 
Next I go to the _zebrafish_ directory.
```text
cd $WRKDIR/genomes/zebrafish
```

In stead of _a-put_, that was used in the previous example, I now use command `rclone copyto` to copy all the 
files from the given directory to Allas.  In the case of _rclone_ there is no default bucket. I stead I have 
to define a bucket to be used. This example I use bucket name _2001659-genomes_ and define that each object name  
should have prefix _zebarfish_.
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
In this case I know that I want to use Allas with project project_2001659 so I can give the project name as an argument for _allas-conf_ command: 
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

In this example we use _a-put_ to upload a set of large files from Taito to Allas. We use _taito-shell_ as a platform for running the process but you could use login nodes of Taito too.

First thing to do is to open a taito-shell connection that we can keep running for a long time. For that 
we have two options:

1.    Using [NoMachine virtual desktop](https://research.csc.fi/csc-guide-connecting-the-servers-of-csc#1.3.3) to connect Taito shell
2.    Using screen command in the login nodes of Taito as described [here](https://research.csc.fi/taito-faq/-/asset_publisher/ZJfZFkUtMsij/content/6-how-do-i-start-long-running-jobs-in-taito-shell-?)

In this example I have used the second alternative and opened the connection to taito-shell with commands:

```text
ssh taito-login3.csc.fi
screen
sinteractive
```
To use Allas I first load _allas module_ and use `allas-conf` to establish the connection to Allas.
```text
module load allas
allas-conf
```
allas-conf woks here just like in the previous examples.

Then I move to directory _my_data_ where I have a set subdirectories (50, 90, 100). I list the gzip-compressed files in these directories: 

<pre>
[kkayttaj@c311:~> <b>cd $WRKDIR/my_data</b>
[kkayttaj@c311:my_data> <b>ls -lh */*.gz</b>
-rw-rwxr-x 1 kkayttaj csc  45G May  8 12:57 100/uniref100.fasta.gz
-rw-rwxr-x 1 kkayttaj csc  61G Jun  5 13:09 100/uniref100.xml.gz
-rw-rwxr-x 1 kkayttaj csc 589M Jun  5 13:09 50/uniref50.fasta.gz
-rw-rwxr-x 1 kkayttaj csc  17G Jun  5 13:09 50/uniref50.xml.gz
-rw-r-xr-x 1 kkayttaj csc 4.2G Jul  6 09:46 90/uniref90.fasta.gz
-rw-rwxr-x 1 kkayttaj csc  33G Jun  5 13:09 90/uniref90.xml.gz
</pre>

Most of the modern non-ascii file formats (i.e. binary data) that are used for large datasets, store the data in very dense format. Thus these files do not benefit from compressing the data. The same applies of course to files that have already been compressed. For this kind of data it is reasonable to use `a-put` command with the `--nc` option that skips the compression and uploads the file to Allas as it is. However, when compression is not used, _a-put_ does not accept directories, only individual files. Because of that is is good to run a check, like the _ls -lh_ command above, to ensure that input will contain only files.

Next I launch the upload process. In this case I don't use the default bucket name but I assign the name to be _2000136-uniref_

```text
 a-put -b  2000136-uniref --nc  */*.gz
```
This command starts loading the files, listed above, to Allas. You couls

I could launch the same upload alternative with _rclone copy_:

```text
for f in */*.gz
do
rclone copy $f allas:2000136-uniref
done
```
 
I can now leave the session running in the background by pressing: _Ctrl-a d_.

Now I can logout from Taito, but the screen session in taito-login3 and the taito-shell session within it is preserved.

To reattach to this session, I first connect to the Taito login node where the screen session is running. For example:
```text
ssh taito-login3.csc.fi
```
Then,  I reattach the screen session with command:
```
screen -R
``` 






















# Persistent allas connections: s3cmd

This chapter describes how you can use the Allas Object Storage service from Taito and Puhti with s3cmd client. This client uses
S3 protocol that differs from the swift protocl that the rclone connection uses. Thus data that has been uploaded to 
Allas with rclone should not be downloaded with s3cmd an vice versa.

From user perspective one of the main differences between s3cmd and swift based rclone is that while rclone connection remains valid 
for three hours at a time but in the case of s3cmd the connection between Puhti/Taito and allas permanently open. The permanent connection
is handy in many ways, but it includes a security aspect too: if your CSC account is compromised, the object storage space is too.


## Configuring s3cmd
In Taito the s3cmd configuration process can be done by executing commands:

<pre> module load bioconda/3
source /appl/opt/allas_conf -mode s3cmd</pre>


The configuration process asks first your CSC password. Then it lists your cPouta projects and asks you to define the name of the cPouta project to be used. During the proceeding configuration steps, the system asks you about the values that will be used for the Pouta Object Storage connection. In most cases you can just accept the proposed default values, but there is two exceptions:

   1.  It is recommended that you define a password that is used to encrypt the data traffic to and from Object Storage server. This password is not connected to any other passwords in the CSC environment so you can freely define it. Note however, that this password is stored to the s3cmd configuration file in human readable format so you should not use this password elsewhere. 
   2.  As the last question the configuration process asks if the configuration is saved. The default is "no" but you should answer y (yes) so that configuration information is stored to file $HOME/.s3cfg.

This configuration needs to be defined only once. In the future s3cmd will use this Object Storage connection described in the .s3cfg file automatically. However, if you wish to change the Object Storage project that s3cmd uses, you just need to run the configuration command again.
 
##3.2 Using Object Storage with s3cmd

The syntax of the s3cmd command is:

<pre>s3cmd -options command parameters</pre>

Table 3.2 below lists the most essential s3cmd commands. For more complete list, visit the  s3cmd manual page or execute command:

<pre>s3cmd -h</pre>

Most commonly used s3cmd commands
s3cmd command 	Function
 mb 	 Make a new bucket
 rb 	 Remove a bucket
 ls 	 List objects or bukets
 la 	 List all objects in all buckets
 du 	 Show the disk usage of buckets
 put 	 Put file into a bucket
 get 	 Get file from a bucket
 setacl 	 Modify Access control list for Bucket or Files

In Object Storage the files are stored as objects that locate in buckets. The buckets resemble folders in normal file systems. There are however some differences compared to folders. Firstly, the file structure on Object Storage is flat: you can't create a bucket that is inside a bucket. Secondly, all bucket names must be unique throughout the Object Storage system. You can't use a bucket name that is already used by you or some other Object Storage user.

In the example below we store a simple dataset to Allas using s3cmd.

First we create a new bucket. The ls command shows that in the beginning we don't have any data in the object storage. After that, we use mb command to create a new bucket called "fish-bucket".

<pre>[kkayttaj@c306:~]$ <b>s3cmd ls</b>
ls

[kkayttaj@c306:~]$ <b>s3cmd mb s3://fish-bucket</b>
mb s3://fish-bucket/
Bucket 's3://fish-bucket/' created
[kkayttaj@c306:~]$ <b>s3cmd ls</b>
ls
2018-03-12 13:01  s3://fish-bucket</pre>
It is recommended to collect the data to be stored into larger units and compress the data before uploading it to the system.

In this example we will store the Bowtie2 indexes and genome of the Zebrafish (Danio rerio) to the fish-bucket. Running ls -lh shows that we have the index files available in the current directory

<pre>[kkayttaj@c306:~]$ <b>ls -lh</b>
total 3.2G
-rw------- 1 kkayttaj csc 440M Mar 12 13:41 Danio_rerio.1.bt2
-rw------- 1 kkayttaj csc 327M Mar 12 13:41 Danio_rerio.2.bt2
-rw------- 1 kkayttaj csc 217K Mar 12 13:20 Danio_rerio.3.bt2
-rw------- 1 kkayttaj csc 327M Mar 12 13:20 Danio_rerio.4.bt2
-rw------- 1 kkayttaj csc 1.3G Mar 12 13:13 Danio_rerio.GRCz10.dna.toplevel.fa
-rw------- 1 kkayttaj csc 440M Mar 12 14:03 Danio_rerio.rev.1.bt2
-rw------- 1 kkayttaj csc 327M Mar 12 14:03 Danio_rerio.rev.2.bt2
-rw------- 1 kkayttaj csc 599K Mar 12 13:13 log</pre>

The data is collected and compressed to a single file with tar command:

<pre>tar zcf zebrafish.tgz Danio_rerio*</pre>

The size of the resulting file is about 2 GB. Now the compressed file can be uploaded to the the fish-bucket with command s3cmd put:

<pre>[kkayttaj@c306:~]$ <b>ls -lh zebrafish.tgz</b>
-rw------- 1 kkayttaj csc 2.0G Mar 12 15:23 zebrafish.tgz

[kkayttaj@c306:~]$ s3cmd put zebrafish.tgz s3://fish-bucket
put zebrafish.tgz s3://fish-bucket
upload: 'zebrafish.tgz' -> 's3://fish-bucket/zebrafish.tgz'  [part 1 of 136, 15MB] [1 of 1]
 15728640 of 15728640   100% in    0s    22.49 MB/s  done
upload: 'zebrafish.tgz' -> 's3://fish-bucket/zebrafish.tgz'  [part 2 of 136, 15MB] [1 of 1]
 15728640 of 15728640   100% in    0s    23.17 MB/s  done
...
upload: 'zebrafish.tgz' -> 's3://fish-bucket/zebrafish.tgz'  [part 135 of 136, 15MB] [1 of 1]
 15728640 of 15728640   100% in    0s    24.13 MB/s  done
upload: 'zebrafish.tgz' -> 's3://fish-bucket/zebrafish.tgz'  [part 136 of 136, 3MB] [1 of 1]
 4002097 of 4002097   100% in    0s     8.96 MB/s  done>

[kkayttaj@c306:~]$ s3cmd ls s3://fish-bucket
ls s3://fish-bucket
2018-03-12 13:29 2127368497   s3://fish-bucket/zebrafish.tgz
</pre>
Uploading 2 GB of data takes some time. The uploaded file could be retrieved with command:

<pre>s3cmd get s3://fish-bucket/zebrafish.tgz</pre>

By default this bucket can be accessed only by the project members. However, with s3cmd setacl you can make the file publicly available:

First make the fish-bucket public

<pre>s3cmd setacl --acl-public s3://fish-bucket</pre>

And then make the zebrafish genome file public:

<pre>s3cmd setacl --acl-public s3://fish-bucket/zebrafish.tgz</pre>

The syntax of URL of the file is:

<pre>https://bucket-name.object.pouta.csc.fi/object_name</pre>

So in this case the file would be accessible through link:

>https://fish-bucket.object.pouta.csc.fi/zebrafish.tgz

# Using Allas with rclone from Puhti and Taito 

This is the guide how to use Allas when you are logged in to the Puhti computing environment. The first step to use Allas is to authenticate to a project in Allas.


>[user@puhti ~] source /appl/opt/allas_conf

The command above generates and stores authentication information into shell variables OS_AUTH_TOKEN and OS_STORAGE_URL. The authentication is valid for max 3 hours. Note that environment variables are available only for that login session so if you log into Puhti in another session, you need to authenticatate again there to use Allas.

Data in Allas is arranged into containers called buckets. You can simply think them as top level directories. The only drawback of buckets is that they must have unique name, you can't create a bucket if some other project has already used that bucket name. So it is a good rule of thumb to have something project or user spesific in the bucket name, for instance "2000620-raw-data".

You can use a program named rclone to handle buckets and upload data to and download data from Allas. This is how you can create a bucket and list all buckets:

>[user@puhti ~] rclone mkdir allas:2000620-raw-data

>[user@puhti ~] rclone lsd allas:

>           0 2019-06-06 14:43:40         0 2000620-raw-data

>[user@puhti ~] 

This is how you upload a file into that bucket and list the content of that bucket:

>[user@puhti ~] rclone copy file.dat allas:2000620-raw-data/

>[user@puhti ~] rclone ls allas:2000620-raw-data

>   677972 file.dat

>[user@puhti ~] 

Download the file back is done with the same copy command:

>[user@puhti ~] rclone copy allas:2000620-raw-data/file.dat .

Note that if you give a destination parameter name in the download command, rclone creates a directory where the download goes:

>[user@puhti ~] rclone copy allas:2000620-raw-data/file.dat doh

>[user@puhti ~] ls doh

>file.dat

>[user@puhti ~] ls -ld doh

>drwxr-xr-x  3 user  staff  96 Jun  6 14:58 doh

>[user@puhti ~] 

Copying a directory can be done with copy command or with sync command. An example of using sync, note that destination parameter needs mydata at the end:

>[user@puhti ~] ls -R mydata

>file4.txt       setA            setB

>

>mydata/setA:

>file1.txt

>

>mydata/setB:

>file2.txt       file3.txt

>[user@puhti ~] rclone sync mydata allas:2000620-raw-data/mydata

>[user@puhti ~] rclone ls allas:2000620-raw-data

>   677972 mydata/file4.txt

>    10927 mydata/setA/file1.txt

>     1116 mydata/setB/file2.txt

>     5075 mydata/setB/file3.txt

>[user@puhti ~] 


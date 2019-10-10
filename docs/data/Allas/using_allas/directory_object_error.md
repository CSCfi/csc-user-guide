
# Directory object error

There are no actual directories in Allas. Some client software may incorrectly create zero-sized objects and metadata or add a slash character at the end of the name.
``` bash
Content Type: application/directory
Content Type: application/x-directory
Content Type: binary/octet-stream
```
**That does not make it a directory.**

Such software is e.g. Cyberduck, Nextcloud and s3fuse. This makes sense only when all users using that data use similar tools and especially do not use _s3cmd_.

For instance, a Cyberduck-uploaded directory structure
```
data4.dat
mydata
├── data1.dat
├── data2.dat
└── subdir
    └── data3.dat
```
listed with s3cmd:

``` bash
$ s3cmd ls -r s3://idev1clitest/
ls -r s3://idev1clitest/
2019-08-20 07:25   1048576   s3://idev1clitest/data4.dat
2019-08-20 07:22         0   s3://idev1clitest/mydata
2019-08-20 07:22      1024   s3://idev1clitest/mydata/data1.dat
2019-08-20 07:22    102400   s3://idev1clitest/mydata/data2.dat
2019-08-20 07:22         0   s3://idev1clitest/mydata/subdir
2019-08-20 07:22     10240   s3://idev1clitest/mydata/subdir/data3.dat
```

There are zero-sized objects mydata and _mydata/subdir_. The problem this kind of extra objects cause is that when trying to download the structure with s3cmd, the zero-sized object is downloaded to a file, preventing the creation of a directory with the same name, and subsequently also preventing downloading the files inside the directory:

``` bash
$ s3cmd get -r s3://idev1clitest/
get -r s3://idev1clitest/
download: 's3://idev1clitest/data4.dat' -> './data4.dat'  [1 of 6]
 1048576 of 1048576   100% in    0s     9.79 MB/s  done
download: 's3://idev1clitest/mydata' -> './mydata'  [2 of 6]
 0 of 0     0% in    0s     0.00 B/s  done
ERROR: Skipping ./mydata/data1.dat: Not a directory
ERROR: Skipping ./mydata/data2.dat: Not a directory
ERROR: Skipping ./mydata/subdir: Not a directory
ERROR: Skipping ./mydata/subdir/data3.dat: Not a directory
$
```

You can download a hierarchy of this kind with _s3_ by first creating each local directory and then downloading the files by the directory level.

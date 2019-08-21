
# Directory object error

There are no real directories in Allas. Some client software incorrectly want to create zero sized objects in Allas and attach metadata like

```
Content Type: application/directory
```

or

```
Content Type: application/x-directory
```

to them. That does not make them a directory. Such software are for instance Cyberduck and s3fuse. This makes sense only when all users using that data use similar tools and especially do not use s3cmd.

For instance a Cyberduck uploaded directory structure

```
data4.dat
mydata
├── data1.dat
├── data2.dat
└── subdir
    └── data3.dat
```

listed with s3cmd looks like this

```
$ s3cmd ls -r s3://idev1clitest/
ls -r s3://idev1clitest/
2019-08-20 07:25   1048576   s3://idev1clitest/data4.dat
2019-08-20 07:22         0   s3://idev1clitest/mydata
2019-08-20 07:22      1024   s3://idev1clitest/mydata/data1.dat
2019-08-20 07:22    102400   s3://idev1clitest/mydata/data2.dat
2019-08-20 07:22         0   s3://idev1clitest/mydata/subdir
2019-08-20 07:22     10240   s3://idev1clitest/mydata/subdir/data3.dat
```

There are zero sized objects mydata and mydata/subdir. The problem those extra objects cause is that when trying to dowload that structure with s3cmd the zero sized object is downloaded to a file which then prevents creating a directory with the same name and subsequently also prevents downloading the files inside that directory:

```
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



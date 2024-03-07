# Packing and compression tools

When large data sets are stored at CSC or transported over the internet, it is
usually reasonable to *archive* (i.e., pack multiple files into a single
file) and *compress* (i.e., reduce its size without losing any data) the
data. Archiving makes file transfer easier and compressed files
require less storage space and are thus faster to move from one system
to another. In this chapter we will introduce
**tar**, **gzip**, **bzip2**, **zip**, **7zip** and **Zstandard** tools
that are frequently used for archiving and compression.

| Type                           | Extension                                 |
|--------------------------------|-------------------------------------------|
| A zip archive                  | `.zip`, `.ZIP`, or `.Z`                   |
| A gzip compressed file         | `.gz`                                     |
| A bzip2 compressed file        | `.bz2`, or `.bz`                          |
| A tar archive                  | `.tar`                                    |
| A gzip compressed tar archive  | `.tar.gz`, or `.tgz`                      |
| A bzip2 compressed tar archive | `.tar.bz2`, `.tar.bz`, `.tbz`, or `.tbz2` |
| A 7zip compressed file         | `.7z`                                     |
| A Zstandard compressed file    | `.zst`                                    |

## tar: packing several files into one file

**tar** is a computer software utility for collecting many files into
one archive file, often referred to as a *tarball*, for distribution or
backup purposes. The name is derived from **t**ape **ar**chive, as it
was originally developed to write data to sequential I/O devices with no
file system of their own. However, nowadays tar – and its GNU
version, **gtar** – are mostly used for data archiving within a normal
disk environment. The archive files created by tar contain various file
system parameters, such as name, timestamps, ownership, file access
permissions, and directory structures, which makes moving and storing
large file sets easier that trying to manage separate files.

By default, tar does not compress the data. This means that the size of
the tar archive file is the same as the sum of the sizes of the packed
files, plus some overhead metadata. If data compression is needed, you
can use compression tools like **gzip** or **bzip2** with tar.

tar and gtar are compatible with each other; if you archive your
data with tar you can unarchive it with gtar and vice versa.
Normally tar and/or gtar can be found from any Unix, Linux or macOS
system. In Windows systems you can use for example **7zip** program to
manage tar archive files.

The syntax of a `tar` command is:

```bash
tar options tar_archive file ...
```

For example, we may have a directory called `project_3`, which contains
nine files called `sample1.txt`, `sample2.txt`, ..., `sample9.txt`. To
list the contents of the directory, we could use the command `ls -lh`:

```bash
$ ls -lh project_3
total 53M
-rw-r--r--+ 1 testuser csc  16M Nov  9 10:41 sample1.txt
-rw-r--r--+ 1 testuser csc  16M Nov  9 10:41 sample2.txt
-rw-r--r--+ 1 testuser csc 1.3M Nov  9 10:41 sample3.txt
-rw-r--r--+ 1 testuser csc 1.9M Nov  9 10:41 sample4.txt
-rw-r--r--+ 1 testuser csc 1.9M Nov  9 10:41 sample5.txt
-rw-r--r--+ 1 testuser csc 3.7M Nov  9 10:42 sample6.txt
-rw-r--r--+ 1 testuser csc 4.0M Nov  9 10:42 sample7.txt
-rw-r--r--+ 1 testuser csc 3.9M Nov  9 10:42 sample8.txt
-rw-r--r--+ 1 testuser csc 3.9M Nov  9 10:42 sample9.txt
```

We can archive all the files in the `project_3` directory to a tar
archive called `project_3.tar` with tar's create (`c`) command:

```bash
tar cvf project_3.tar project_3
```

The command above creates a new tar archive file, `project_3.tar`, which
contains the directory `project_3` and all the files in it. Note that the
command does not modify or remove the original files in the source
directory:

```bash
$ ls -lh
drwxr-xr-x+ 2 testuser csc   11 Nov  9 10:44 project_3
-rw-r--r--+ 1 testuser csc  52M Nov  9 10:46 project_3.tar
```

The `tar` command does not require that you assign a certain extension,
like `.tar`, for your archive files. However, applying commonly used
file name extensions will help you and other users to select right
commands for processing the file later on. The newly created tar archive
file can now be easily moved to another directory or system and then
unarchived with the extract (`x`) command:

```bash
tar xvf project_3.tar
```

This command will create a directory called `project_3`, which contains
all the same files as the original directory did. Note that if the
extract command encounters a file that already exists in the file
system, the existing file will be overwritten by the extracted file.
This causes a potential danger: possibly a newer version of a file will
be lost if an older version of the same file (or, just a file with the
same name) exists in the tar archive that is being unarchived!

| Command    | Operation                                                              |
|------------|------------------------------------------------------------------------|
| `A`        | Append tar files to an archive (i.e. concatenate archive files)        |
| `c`        | Create a new tar archive                                               |
| `d`        | Find differences between an archive and the file system                |
| `r`        | Append files at the end of an archive                                  |
| `t`        | List the contents of an archive                                        |
| `u`        | Only append files that are newer than the existing ones in the archive |
| `x`        | Extract files from an archive                                          |
| `--delete` | Delete files from the archive                                          |

In addition to the commands above, the option `f` (file) is almost
always used as it defines the name of the tar file to read from or to
write to. The file name must follow right after the option, thus it is
commonly the last option given. Below are some frequently used tar
options.

| Option | Function                                                                    |
|--------|-----------------------------------------------------------------------------|
| `f`    | Use the given file name as the source or target archive                     |
| `v`    | Be verbose, i.e. list processed files to the screen while processing        |
| `z`    | Use gzip compression/decompression while creating or extracting an archive  |
| `j`    | Use bzip2 compression/decompression while creating or extracting an archive |

With options `z` (zip) or `j` (no meaning, it was chosen because no
meaningful letter was available) you can filter the archive
through `gzip` or `bzip2`, respectively, to (de)compress the archive on
the fly:

```bash
tar cvzf project_3.tar.gz project_3
```

Here, in this sample case, the size of the uncompressed archive file is
52 MB, but the compressed file is only 15 MB.

```bash
$ ls -lh
drwxr-xr-x+ 2 testuser csc   11 Nov  9 10:44 project_3
-rw-r--r--+ 1 testuser csc  52M Nov  9 10:46 project_3.tar
-rw-r--r--+ 1 testuser csc  15M Nov  9 10:56 project_3.tar.gz
```

Listing the contents of a tar archive file can be done with command
`t` (list):

```bash
$ tar tf project_3.tar
project_3/
project_3/sample3.txt
project_3/sample4.txt
project_3/sample5.txt
project_3/sample2.txt
project_3/sample1.txt
project_3/sample6.txt
project_3/sample8.txt
project_3/sample9.txt
project_3/sample7.txt
```

You can also retrieve just one file from the archive by specifying the
full file name to the data extraction command. For example, to extract
just file `sample2.txt` from the compressed archive `project_3.tar.gz` we
could use command:

```bash
tar xvzf project_3.tar.gz project_3/sample2.txt
```

## Compressing files

Compressing files saves storage space and makes data transport faster,
but it may take a lot of time. Data compression is CPU intensive and
compressing a data set of several terabytes can easily require overnight
computing.

There are numerous algorithms and software tools available for data
compression. Here, we will briefly show five tools that are used in
Unix/Linux systems: *gzip*, *bzip2*, *zip*, *7z* and *Zstandard*. What is
common to all these tools is that they do the compression without data
loss, i.e. when the files are uncompressed the data will be 100%
identical to the original data. Typically, a text file compressed with
one of these tools is about 20-40% of the size of the original file.
However, the compressibility of a file depends heavily on the content of
the file.

The compression time depends on the algorithm used and the type of data
to be compressed. In most cases the newer Zstandard method is
significantly faster than the older, but very widely used methods like
gzip or zip. The table below shows results for one sample case,
where a 10 GB text file (fastq-formatted sequence data) was compressed with
these five methods in the Puhti supercomputer using default command settings.

| Command | Size of the<br>compressed file<br>(original size 10GB) | Compression time | Decompression time |
|------------|--------|---------|---------|
| `zstd`     | 2.6 GB | 2 min   | 1.7 min |
| `zstd -T4` | 2.6 GB | 0.8 min | 1.7 min |
| `7z`       | 1.8 GB | 56 min  | 2.7 min |
| `gzip`     | 2.5 GB | 29 min  | 2.5 min |
| `bzip2`    | 2.0 GB | 17 min  | 9 min   |
| `zip`      | 2.5 GB | 29 min  | 2.5 min |

### gzip and gunzip

**gzip** is probably the most commonly used packing tool in Unix and
Linux systems. It uses the *Lempel-Ziv coding* (LZ77) for compressing
the data. gzip was already briefly mentioned in the tar chapter
above, but gzip can also be used as a totally separate tool. The normal
usage of gzip is straightforward. To compress a file you give the
command:

```bash
gzip file_name
```

Running this command creates a compressed file and names it using the
original file name with an extension `.gz`. When the compression is
ready, the original file is removed. If you want to preserve the original
file, you need to use redirection:

```bash
gzip < file_name > file_name.gz
```

Decompressing a gzipped file is done with command `gunzip`. In
addition to gzip-compressed files, `gunzip` can also decompress files
compressed with the `zip` command. The basic syntax of `gunzip` is analogous
to the compressing command:

```bash
gunzip file_name.gz
```

The command above removes the compressed file when decompression is
ready. If you wish the keep the compressed file, you'll need redirection
again:

```bash
gunzip < file_name.gz > file_name
```

gzip has several command line options that are not discussed here. Use
`man gzip` command to see the full list of available options. Also,
note that `gunzip` command is actually just a wrapper for the `gzip -d`
command (option `-d` instructs `gzip` to decompress, rather than
compress) so you will not find a separate manual page for that.

#### gzip example

Let's assume we are in some directory on Puhti where we
have just one file called `my_data.dat`. Let's first check the size of
that file with command `ls -lh`:

```bash
$ ls -lh
total 1.5G
-rw-r--r--+ 1 testuser csc 1.5G Nov  4 13:07 my_data.dat
```

The listing tells us that the size of the file is approximately 1.5 GB.
Next, we compress the file with `gzip` and then check the file size again.

```bash
$ gzip my_data.dat
$ ls -lh
total 834M
-rw-r--r--+ 1 testuser csc 833M Nov  4 13:07 my_data.dat.gz 
```

The original file has now been removed and replaced by the
compressed file. However, as a result we now have a compressed file that
requires only 833 MB of disk space (55% of the original size). Next, we
decompress the file:

```bash
$ gunzip my_data.dat.gz
$ ls -lh
total 1.5G
-rw-r--r--+ 1 testuser csc 1.5G Nov  4 13:07 my_data.dat 
```

The file listing now shows that the compressed file has disappeared, and
the original file is available again.

### bzip2 and bunzip2

**bzip2** is a compression program that is used very similarly compared
to gzip. The main difference between the two programs is that
bzip2 uses *Burrows-Wheeler block sorting text compression
algorithm* combined with *Huffman coding* instead of the LZ77 algorithm
used in gzip. The compression algorithm of bzip2 produces more effective
compression than gzip. However, computing the bzip2 compression
usually is more complex and takes longer (i.e., uses more CPU cycles)
than gzip compression. The usage of bzip2 is very similar to that of
gzip, but not all the command line options are identical. The basic
compression syntax is:

```bash
bzip2 file_name
bzip2 < file_name > file_name.bz2
```

Similarly, the decompression can be done with commands:

```bash
bunzip2 file_name.bz2
bunzip2 < file_name.bz2 > file_name
```

Note that a file compressed with bzip2 can not be uncompressed with
gunzip and vice versa.

In addition to the standard bzip2 and bunzip2 programs, you can also use
the parallel versions of `bzip2`
command: `pbzip2` and `pbunzip2`. When these commands are
used, the user must use option `-p` to define the number of processor
cores to be used. For example, compressing the file `my_data.dat` using
four cores can be done with command:

```bash
pbzip2 -p4 my_data.dat
```

Similarly, to decompress the file with two cores you can use command:

```bash
punbzip2 -p2 my_data.dat.bz2
```

The `pbzip2` and `pbunzip2` commands scale well for small core numbers.
Already with two cores the `pbzip2` is about as fast as `gzip`. The number
of processors used does not affect to the actual output file. Thus, a
file that has been compressed with parallel `pbzip2` can be uncompressed
with normal `bunzip2` command and vice versa.

### zip and unzip: the combined compression and file archiving tool

The **zip** program can be used for both archiving and compressing
files. Given a list of files or directories, the `zip` command archives
and compresses all the files into a single zip archive file. So, in
principle, `zip` is analogous to the combination of `tar` and `gzip`
commands. Later, the whole archive, or just certain files, can be
extracted from the archive. The basic syntax of `zip` command is:

```bash
zip -options archive_file source_name
```

The `source_name` can be a list of files, directories, or a combination
of both that will be packed in to the `archive_file`. If the
`archive_file` already exists, `zip` will replace the existing files in the
archive with new ones from the `source_name` list, or add files if they
do not exist in the `archive_file` yet. Note that unlike the `tar` command,
`zip` does not add any files from subdirectories into the archive by
default. The option `-r` is needed to recursively add all files and
subfolders from a given directory to the zip archive. Below is listed
some commonly used `zip` command options.

| Option   | Function                                                                                                                             |
|----------|--------------------------------------------------------------------------------------------------------------------------------------|
| `-d`     | Remove (delete) entries from a zip archive                                                                                           |
| `-e`     | Encrypt the contents of the zip archive using a password which is entered on the terminal in response to a prompt                    |
| `-f`     | Replace (freshen) an existing file in the archive only if it has been modified more recently than the version already in the archive |
| `-l`     | Translate the Unix end-of-line character LF into the MSDOS convention CR LF                                                          |
| `-ll`    | Translate the MSDOS end-of-line CR LF into Unix LF                                                                                   |
| `-r`     | Travel the directory structure recursively                                                                                           |
| `-u`     | Update existing entries if newer on the file system and add new files                                                                |
| `-@`     | Take the list of input files from standard input. Only one filename per line.                                                        |

Creating a zip archive does not affect the original files. Note that the
`zip` command will add the `.zip` extension to the archive file name by
default, if it is not already included.

Zip archives can be extracted and studied with the `unzip` command. To
extract files from a zip archive, use the command:

```bash
unzip archive_file_name
```

To just see the files included in the zip archive use command:

```bash
unzip -l archive_file_name
```

You can also extract just one file from an archive with command:

```bash
unzip archive_file_name file_name
```

| Option        | Function                                                                                                                  |
|---------------|---------------------------------------------------------------------------------------------------------------------------|
| `-f`          | Freshen existing files, i.e., extract only those files that already exist on disk and are newer than the ones on the disk |
| `-l`          | List the contents of an archive file                                                                                      |
| `-u`          | Update existing files and create new ones if needed                                                                       |
| `-o`          | Overwrite existing files without prompting                                                                                |
| `-p password` | Use `password` to decrypt an encrypted zip file                                                                           |

#### zip example

To archive and compress the sample directory `project_3`, which
contains the files `sample1.txt`, `sample2.txt`, ..., `sample9.txt` (the
same example that was used in the tar chapter), use the command:

```bash
$ zip -r project_3.zip project_3
  adding: project_3/ (stored 0%)
  adding: project_3/sample5.txt (deflated 71%)
  adding: project_3/sample2.txt (deflated 72%)
  adding: project_3/sample3.txt (deflated 70%)
  adding: project_3/sample4.txt (deflated 71%)
  adding: project_3/sample9.txt (deflated 71%)
  adding: project_3/sample7.txt (deflated 71%)
  adding: project_3/sample1.txt (deflated 73%)
  adding: project_3/sample6.txt (deflated 72%)
  adding: project_3/sample8.txt (deflated 71%)
```

Note that if you use the same `zip` command without the `-r` option, the
archive file will not include the sample files in the directory but just
the directory. However, in this case the `project_3` directory does not
include any subdirectories, so you could also do archiving with command:

```bash
$ zip project_3.zip project_3/*
  adding: project_3/sample1.txt (deflated 73%)
  adding: project_3/sample2.txt (deflated 72%)
  adding: project_3/sample3.txt (deflated 70%)
  adding: project_3/sample4.txt (deflated 71%)
  adding: project_3/sample5.txt (deflated 71%)
  adding: project_3/sample6.txt (deflated 72%)
  adding: project_3/sample7.txt (deflated 71%)
  adding: project_3/sample8.txt (deflated 71%)
  adding: project_3/sample9.txt (deflated 71%)
```

In the same way, you can later add a new file to an existing zip
archive, e.g.:

```bash
$ cp sample10.txt project_3/
$ zip project_3.zip project_3/sample10.txt
 adding: project_3/sample10.txt (deflated 69%)
```

You can check the contents of the zip archive with `unzip` and
option `-l`:

```bash
$ unzip -l project_3.zip
Archive:  project_3.zip
  Length     Date   Time    Name
 --------    ----   ----    ----
 16662202  11-09-09 10:41   project_3/sample1.txt
 16397702  11-09-09 10:41   project_3/sample2.txt
  1303352  11-09-09 10:41   project_3/sample3.txt
  1925824  11-09-09 10:41   project_3/sample4.txt
  1989706  11-09-09 10:41   project_3/sample5.txt
  3813333  11-09-09 10:42   project_3/sample6.txt
  4176523  11-09-09 10:42   project_3/sample7.txt
  4056375  11-09-09 10:42   project_3/sample8.txt
  4085713  11-09-09 10:42   project_3/sample9.txt
  6541306  11-10-09 13:07   project_3/sample10.txt
 --------                   -------
 60952036                   10 files
```

To extract just the file `sample3.txt` from the zip archive, use the
command:

```bash
$ unzip project_3.zip project_3/sample3.txt
Archive:  project_3.zip
replace project_3/sample3.txt? [y]es, [n]o, [A]ll, [N]one, [r]ename: y
  inflating: project_3/sample3.txt 
```

To extract all the files from the archive, use the command:

```bash
$ unzip project_3.zip
Archive:  project_3.zip
replace project_3/sample1.txt? [y]es, [n]o, [A]ll, [N]one, [r]ename:A
  inflating: project_3/sample1.txt
  inflating: project_3/sample2.txt
  inflating: project_3/sample3.txt
  inflating: project_3/sample4.txt
  inflating: project_3/sample5.txt
  inflating: project_3/sample6.txt
  inflating: project_3/sample7.txt
  inflating: project_3/sample8.txt
  inflating: project_3/sample9.txt
  inflating: project_3/sample10.txt
```

### 7zip packing and compression tool 

**7zip** is a packing and compression tool that is frequently
used especially on Windows platforms. It can be, however, used in macOS
and Linux systems too. By default, the command uses its own *7z*
compression file format, but it can utilize other compression file
formats too.

In Puhti, 7zip is launched with command `7z`. To get access to the
command, first load the required module with:

```bash
module load p7zip
```

The basic syntax of the command is:

```bash
7z command -options archive_file file_names
```

The most important 7zip options are:

- `a` add files to an archive
- `e` extract files from an archive file
- `l` list files in the archive file

To archive and compress the sample directory `project_3`, which
contains the files `sample1.txt`, `sample2.txt`, ..., `sample9.txt` (the
same example that was used in the tar chapter), use the command:

```bash
$ 7z a project_3_backup project_3/

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,16 CPUs Intel(R) Xeon(R) CPU E5-2670 0 @ 2.60GHz (206D7),ASM,AES-NI)

Scanning the drive:
1 folder, 9 files, 211442 bytes (207 KiB)

Creating archive: project_3_backup.7z

Items to compress: 10

Files read from disk: 9
Archive size: 42728 bytes (42 KiB)
Everything is Ok
```

This created a new 7z-compressed file `project_3_backup.7z`. The `7z a`
command can also be used to add a new file to an existing archive. For example,
if we would get a new sample file called `sample10.txt` to the `project_3`
directory, we could add it to the previously created
`project_3_backup.7z` file with command:

```bash
7z a project_3_backup project_3/sample10.txt
```

You can list the contents of this file with `7z l` command. For example:

```bash
$ 7z l project_3_backup.7z 

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,16 CPUs Intel(R) Xeon(R) CPU E5-2670 0 @ 2.60GHz (206D7),ASM,AES-NI)
Scanning the drive for archives:
1 file, 565592 bytes (553 KiB)

Listing archive: project_3_backup.7z

--
Path = project_3_backup.7z
Type = 7z
Physical Size = 565592
Headers Size = 341
Method = LZMA2:6m
Solid = +
Blocks = 2

   Date      Time    Attr         Size   Compressed  Name
------------------- ----- ------------ ------------  ------------------------
2018-11-08 11:02:30 D....            0            0  project_3
2018-11-08 10:57:24 ....A          446        42419  project_3/sample1.txt
2018-11-08 10:57:33 ....A        54807               project_3/sample2.txt
2018-11-08 10:57:58 ....A         3152               project_3/sample3.txt
2018-11-08 10:58:06 ....A         1633               project_3/sample4.txt
2018-11-08 10:58:21 ....A         3151               project_3/sample5.txt
2018-11-08 10:58:39 ....A          161               project_3/sample6.txt
2018-11-08 10:58:48 ....A         1556               project_3/sample7.txt
2018-11-08 10:58:59 ....A       146070               project_3/sample8.txt
2018-11-08 10:59:12 ....A          466               project_3/sample9.txt
2018-11-08 11:13:25 ....A      5679358       522832  project_3/sample10.txt
------------------- ----- ------------ ------------  ------------------------
2018-11-08 11:13:25            5890800       565251  10 files, 1 folders
```

Compressed data is extracted with command: `7z e`. You can extract just
the defined files, for example:

```bash
7z e project_3_backup.7z project_3/sample3.txt
```

Note that if you choose to extract just individual files:

1. you must use the full file path that is given in the file listing, and
2. the specified compressed file is extracted to the current directory and not
   to a directory path defined in the compressed file name. Thus, the above
   command would return a file `sample3.txt` to the directory where the
   command was executed.

The output directory of the extracted files can be defined with option
`-o`. For example, to retrieve all the compressed files to a directory
`project_3`, you should give command:

```bash
7z e -oproject_3 project_3_backup.7z
```

### Zstandard compression tool

**Zstandard** is a fairly new and very fast compression tool. In Puhti,
Zstandard compression can be done with command `zstd`. For
example, to compress file `data.txt`, give command:

```bash
zstd data.txt
```

The above command produces a compressed file named as `data.txt.zst`.
For larger data files you can speed up the compression by using multiple
computing cores (threads). The number of threads is defined with option
`-T`. In the login nodes of Puhti, it is recommended that you use just
one thread that is the default setting, but, for example, in an interactive
session you could use four threads:

```bash
zstd -T4 data.txt
```

Decompression is defined by adding option `-d` to the command:

```bash
zstd -d data.txt.zst
```

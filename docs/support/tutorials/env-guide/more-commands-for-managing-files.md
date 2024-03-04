# More commands for managing files

## Using find to locate files

The `find` command is used to locate files in the Linux file
system. The command requires two arguments:

1. the name of the directory where the file is looked for
2. the search condition

The basic syntax of the command is:

```bash
find directory search_condition 
```

The search condition is normally based on the name of the file
(`-name value`), but you can also use options that refer to dates
or access settings. The `find` command can also have a third argument
that defines what operation is performed on the found files. The
default action that is used if no command argument is given is
`-print`, which prints the path and name of the matching files.
The following sample command would look for a file called `dataset27.dat` from
the current directory. In this case, the file is found from a subdirectory
`dataset3`.

```bash
$ find ./ -name dataset27.txt
./dataset3/dataset27.txt
```

You can also use *wildcards* in the name search conditions. Note,
however, that in such case you must quote the search condition. The following
command locates from your home directory (`$HOME`) all files that have
extension `.tmp`.

```bash
find $HOME/ -name "*.tmp"
```

In the last find command examples we use `-mtime` search condition,
which picks files based on their modification date. With the following
command you can check what files have not been accessed in directory
`/scratch/project_2001234` during the last 28 days:

```bash
find /scratch/project_2001234 -mtime +28
```

Here `+28` means "more than 28 days". In the same way minus-character
(`-`) means *less than*. So to see what files have been
modified in your current directory less than 24 hours ago, you could use the
command:

```bash
find ./ -mtime -1
```

## File command tells the file type

The `file` command evaluates the type of the given file. The syntax
of the command is:

```bash
file file_name
```

The command prints the name of the file and a one-line description of
the file type. The `file` command recognizes most common text file
formats, compressed files and Linux executables. It also studies the
content of the file and tries to estimate e.g. if a normal text file
contains program code or some commonly used data formatting types like
XML. Note however that `file` often fails to classify correctly
application-specific files. If the file is a binary file that is not
recognized by the `file` command, it is reported to be a *data* file.

In the example below, file types of all the files in the current working
directory are listed.

```bash
$ file ./*
./a.out:                   ELF 64-bit MSB MIPS-IV executable, MIPS, version 1
./common.py:               a python script text executable .
/data_old.gz:              gzip compressed data, from Unix
./data.txt:                ASCII text
./instrction.html:         HTML document text
./molecule.msv:            data
./output4.jpg:             JPEG image data, JFIF standard 1.01
./outout4.png:             PNG image data, 640 x 480, 4-bit colormap
./output4.xml:             XML document text
./poster1.pdf:             PDF document, version 1.4
./report.doc:              Microsoft Office Document
```

## Count rows and characters with `wc`

Command `wc` (Word Count) is a tool that can be used to count
characters (`-m`), words (`-w`) or rows (`-l`) that a **Linux text file**
contains. The most common use of `wc` command is to quickly check
the row count of your file:

```bash
wc -l file_name
```

Another common use is checking how many rows the output of a command
contains. For example, the following command would give the number of files
with extension `.dat` in the current directory.

```bash
ls *.dat | wc -l
```

## Comparing two files with diff

The `diff` command can be used to compare two files. `diff` goes
through the files row by row and prints out lines that are not
identical. `diff` is most useful when you need to compare two nearly
identical files like two versions of the same program file. The basic
syntax of the command is:

```bash
diff file1 file2
```

## Using checksums to verify successful data storage or transfer

Checksums provide a tool to make sure that a data file is fully
conserved during storage or copying. The idea behind checksums is an
algorithm that calculates a number or a string based on the content of
the file. A checksum string is calculated and stored before the file is
moved to a storage media or copied to a new location. Later on, when the
data is retrieved from the storage or the copying process is finished, a
new checksum is computed based on the retrieved or copied files. If the
new checksum equals to the previously computed one, we can be pretty
sure that the data is fully conserved.

One of the most common checksum algorithms is *md5* that is often used
to verify the correctness of data files. For example, many scientific
data sets available on the internet are accompanied by a
list of md5 sums. The md5 sum is always a text string 32 characters
long. This string has the characteristics of a good checksum: it does
not tell anything about the actual content of the source file and any
modification to the original file produces a completely different
checksum. Other frequently used checksum algorithms include **SHA**
(*Secure Hash Algorithm*) that is often used in cryptography and **CRC**
(*Cyclic Redundancy Check*) that is common in data transfer.

The example below shows how to use **md5sum** in the CSC
environment. An md5 checksum for a file is calculated with the command:

```bash
md5sum file_name
```

For example:

```bash
$ md5sum poster1.pdf
cc494699398122a6b6d93a5a69bd2667 poster1.pdf
```

You can easily store the checksum in a file by redirecting the output of
the command to a new file with `>` character.

```bash
md5sum poster1.pdf > poster1.pdf.md5
```

The command above stores the checksum and file name to a new file called
`poster1.pdf.md5`.

Checking a set of files against an md5 sum list is done by using option
`-c`.

```bash
md5sum -c checksum_list
```

For example, to check the validity of file `poster1.pdf` with the previously
created checksum file `poster1.pdf.md5`, use command:

```bash
$ md5sum -c poster1.pdf.md5
poster1.pdf: OK
```

## Encrypting files with GPG

!!! info "Note"
    If you work with sensitive data at CSC, please see our
    [sensitive data services guide](../../../data/sensitive-data/index.md).

File encryption can be used to increase the security of your data. In normal
conditions (i.e., when not working with sensitive data), encrypting files that
locate at CSC is not needed. The files can by
default be accessed only by the user themselves. However, in principle, the
system administrators of CSC are able to read all data at the servers of
CSC. In some occasions the administrators may need to check file names
and sizes, but the administrator policy of CSC strictly prohibits
accessing the contents of user's data files. However, encryption may
be reasonable if you for example need to copy the data outside CSC or if
encryption is required by the owner of the data.

At CSC, you can use the **GPG** program to encrypt your files. GPG
is frequently used for creating *encryption key pairs* to protect emails
and other data transfer. However, in this chapter we demonstrate only
how GPG can use used to encrypt individual files.

The basic syntax for encrypting a file with `gpg` command is:

```bash
gpg -c file_name
```

The command asks the user to define a password for the file. This
password is not, and should not be, in any sense related to your CSC
password. After confirming the password, the command makes an encrypted
copy of the given file. By default, the encryption is done with CAST5
algorithm, but several other algorithms can be used too.

To open a GPG-encrypted file, give command:

```bash
gpg gpg_encrypted_file 
```

### GPG example

Say we have file a `my_file.txt` that we want to encrypt. This can be
done with command:

```bash
gpg -c my_file.txt
```

When the command is launched, the following prompt appears:

```text
Enter passphrase:
```

Now you can type in any password for the file. In this case we use
following password: `y8kIeg%a`. Once the password is typed, the programs
asks you to confirm the password:

```text
Repeat passphrase:
```

When the encryption is finished we have two files: the original
file and and its encrypted version that has an extension `.gpg`.

```bash
$ ls  -l
-rw-------+ 1 kkayttaj csc 1291176 Feb 11 15:57 my_file.txt
-rw-------+ 1 kkayttaj csc  313848 Feb 11 16:05 my_file.txt.gpg
```

Note that in this case the encrypted file is smaller than the original
one. Now we can remove the original file.

```bash
rm my_file.txt
```

Later on, for example after copying the file to some other location, you
can extract the data with command:

```bash
gpg my_file.txt.gpg
```

The program now asks for the password you used in encryption (in this
case: `y8kIeg%a`). After this, you again have two files: the encrypted file
`my_file.txt.gpg` and the original, readable file `my_file.txt`. Note
that if you forget the password of your encrypted file, there is no one
who can open the file!

## Managing access permissions of files and directories

Hundreds of users use the computing and storage environments of CSC. To
keep the files private and in order, each file and folder in the Linux
environment of CSC is owned by a certain user account. In Linux systems
each file has three user categories: *owner*, *group* and *others*. For
each or these user categories, there are three access settings:
*reading*, *writing* and *execution* permissions.

By default, only the owner of the file can read and modify (i.e. write)
the files and directories they have created.
Other users do not have any access permissions to the files. Normally,
this setting is good as it keeps your data private. However, if you wish
to share some data or execute self-written programs, the access
permissions need to be modified.

Note that the project specific-disk areas in Puhti and Mahti supercomputers 
are an exception to this rule.̣ There by default also other project members, 
belonging to the same UNIX group, have full rights to files created by other 
users.

You can check the access permissions with the command `ls -l`. Let's take
a look at the sample file listing that was previously used in the
[`ls -la` example](using-linux-in-command-line.md#basic-commands-for-using-directories).
In this file listing the characters from second to the
tenth column include the information on the access permissions.

The first three of these permission characters display the permissions of
the *owner*, next three ones display the access permissions of the
*UNIX group members* and the last three characters *all the other
users*. Below is a sample output for `ls -la` command:

    total 26914
    drwx------+  3 kkayttaj csc       10 Dec 22 09:12 .
    drwxr-xr-x  20 root     root       0 Dec 22 09:12 ..
    drwx------+ 42 kkayttaj csc      472 Dec 22 09:07 ..
    -rwxr-x---+  1 kkayttaj csc     1648 Dec 22 09:01 .cshrc
    -rw-------+  1 kkayttaj csc       93 Dec 22 09:01 .my.cnf
    -rw-------+  1 kkayttaj csc       48 Dec 22 09:05 Test.txt
    -rw-------+  1 kkayttaj csc   878849 Jan 19  2009 input.table
    drwxr-xr-x+  2 kkayttaj csc        2 Dec 22 09:11 project1
    -rw-------+  1 kkayttaj csc 26432051 Dec 22 09:08 results.out
    -rw-------+  1 kkayttaj csc       25 Mar 27  2009 sample.data
    -rw-------+  1 kkayttaj csc       49 Mar 27  2009 test.txt 

In the case of file `Test.txt` the setting is: `rw-------`. This means
that the owner of the file (`kkayttaj`) has permission to read (`r`)
and write (`w`) to the file. Other users have no permissions for
this file. In the case of file `.cshrc` the definition is: `rwxr-x---`.
In this case the owner has also execution permissions (`x`) to the file
and also the other users that belong to group `csc` have permission to
read (`r`) and execute (`x`) the file.  

### Managing access permissions using the command-line

In command-line usage, access permissions can be modified with command
**chmod**. This command needs two arguments:

1. a string that defines what changes are to be done and 
2. an argument that defines the target file or directory

As the first argument, you first define the
user category: `u` (user i.e. owner), `g` (group) or, `o`
(others). Then you define with plus or minus character if you are going
to add (`+`) or remove (`-`) permissions. Finally, you define, what
permissions are added or removed. For example, to allow all the group
members to read file `Test.txt` you should give the command:

```bash
chmod g+r Test.txt
```

You can check the effect with `ls -l` command:

```bash
$ ls -l Test.txt
-rw-r-----+  1 kkayttaj csc       48 Dec 22 09:05 Test.txt 
```

You can define several user categories and permissions at the same time.
For example,

```bash
chmod go+rwx Test.txt
```

would add all access permissions for all users to file `Test.txt`. To
remove the permissions, you should change the `+` character to `-`.

```bash
chmod go-rwx Test.txt
```

Note that by default, changing the permissions of a directory does not
change the permissions of the files and subdirectories in the target
directory. Thus, the command

```bash
chmod g+w project1
```

would not allow other group members to modify the files in directory
`project1`. You can use option `-R` to do the same permission
modification *recursively* i.e. to all files and subdirectories in the
target directory:

```bash
chmod -R g+w project1
```

You can use command `groups` to check which groups you belong to.

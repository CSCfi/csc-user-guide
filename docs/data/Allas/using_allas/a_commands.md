# a-commands, easy and safe

The Allas object storage system can be used in multiple ways and for many purposes. In many cases, using Allas efficiently requires that the user know the features of both the object storage system and the software or protocol used to manage the data in Allas.

For users who simply want to use Allas for storing data that is in the CSC computing environment, CSC provides a set of commands for managing and moving data between the CSC computing environment and Allas:
  
| a-command | Function |
| :--- | :--- |
| a-put | Upload a file or directory to Allas as one object |
| a-list | List buckets and objects in Allas |
| a-publish | Upload a file to Allas into a bucket that allows public access over the internet |
| a-flip | Upload a file temporarily to Allas into a bucket that allows public access over the internet |
| a-get | Download a stored dataset (object) from Allas |
| a-find | Search and locate data uploaded with *a-put* |
| a-delete | Delete an object in Allas |
| a-info | Display information about an object in Allas |

In addition to the above commands, there are separate tools for other purposes:

 * __allas_conf__ : Set up and open a connection to Allas
 * __allas-backup__ : Create a backup copy of a local dataset in a backup repository in Allas.
 * __allas-mount__ : Mount a bucket in allas to be used as a read-only directory in the local environment.
 
If you use a-commands outside the supercomputers, check the [allas-cli-utils documentation](https://github.com/CSCfi/allas-cli-utils/blob/master/README.md) for how to install these tools.

## Opening a connection

In order to use these tools in Puhti and Taito, first load a-commands:
```text
module load allas
```
Then open a connection to Allas:
```text
allas-conf
```
The connection remains open for eight hours. You can rerun the _allas-conf_ command at any time
to extend the validity of the connection for eight more hours or to switch to another Allas 
project. 

By default, *allas-conf* lists your projects that have access to Allas, but if you know the name of the project, you
can give it as an argument:
```text
allas-conf project_123456
```
Note that the Allas project does not need to be the same as the project you are using in Puhti or Taito.

## a-put uploads data to Allas

`a-put` is used to upload data from the disk environment of Taito and Puhti to 
the Allas storage environment. The basic syntax of the command:
```
a-put directory_or_file
```

By default, this tool performs the following operations:

1.    Ensure there is a working connection to the Allas storage service and 
define the project that will be used to store the data.

2.    In the case of a directory, the content of the directory is collected into a single file
using the `tar` command.

3.    By default, the option `--compress` (`-c`) is used. The data is compressed using the _zstdmt_ command.
This is the recommended way if you will use the data only in CSC's computing servers. If you plan to use the 
uploaded data in other servers where _zstdmt_ compression may not be available, you can disable the compression using the 
option `--nc` (`-n`).

4.    The compressed data is uploaded to Allas using `rclone` command and the _swift_ protocol.

By default, a-put uses standard bucket and object names that depend on the username, project and location
of the data uploaded:

*    a) $WRKDIR (Taito) is uploaded to the bucket _username_projectNumber_-taito-WRKDIR
*    b) $SCRATCH (Puhti) is uploaded to the bucket _projectNumber_-puhti-SCRATCH
*    c) $PROJAPPL (Puhti) is uploaded to the bucket _projectNumber_-puhti-PROJAPPL 
*    d) In other cases, the data is uploaded to _username-projectNumber_-MISC
  
For example, for the user _kkayttaj_, a member of the project _12345_, data located in the HOME directory
will be uploaded to the bucket _kkayttaj-12345-MISC_.

If you wish to use other than the standard bucket, you can define a bucket name with the option _-b_ or  
_--bucket_.

The compressed dataset is stored as one object. By default, the object name depends on the file name and location. The possible subdirectory path in Puhti or Taito is included in the object name, e.g. a file called *test_1.txt* in $WRKDIR in Taito can be stored using the commands
```text
cd $WRKDIR
a-put test_1.txt
```

In this case, the file is stored in the bucket _kkayttaj-12345-taito-WRKDIR_.
as the object *test_1.txt.zst*

If you have another file called *test_1.txt* that is located in _$WRKDIR/project2/sample3_,
you can store it using the commands
```text
cd $WRKDIR/project2/sample3
a-put test_1.txt
```
or
```text
cd $WRKDIR
a-put project2/sample3/test_1.txt
```
In this case, the file is stored in the bucket *kkayttaj-12345-taito-WRKDIR* 
as the object *project2/sample3/test_1.txt.zst*.

In addition to the actual data object, another object containing metadata is created. This metadata object has the 
same name as the main object with the extension *_ameta*. This metadata file is used by the 
other *a-commands*, and normally it is not displayed to the user, but if you examine the buckets
using tools like _swift_ or _rclone_, you will see these metadata files as well.

If you wish to use a name differing from the default object name, you can define it with the option _-o_ or  
_--object_:
```text
cd $WRKDIR
a-put project2/sample3/test_1.txt -b newbucket1 - o case1.txt -n
```
The command above would upload the file *test_1.txt* to Allas in the bucket _newbucket1_ as the object _case1.txt_.
As the option _-n_ is used, the data is stored in an uncompressed format. 

## a-list

List all buckets belonging to a project:
```text
a-list
```
Display the objects included in a bucket:
```text
a-list bucket_name
```
Typing a part of an object's name lists a subset of objects:
```text
a-list bucket_name/beginning_of_the_object
```

## a-publish 

`a-publish` copies a file to Allas in a bucket that can be publicly accessed. Thus, anyone with the address (URL) of the 
uploaded data object can read and download the data with a web browser or tools like *wget* and *curl*. 
a-publish works similarly to a-put with some differences: 
1) a-publish can upload only files, not directories. 
2) The files are not compressed but uploaded as they are. 
3) The access control of the target bucket is set so that it is available in read-only mode.

The basic syntax:
```text
a-publish file_name
```
By default, the file is uploaded to the bucket _username-projectNumber_-pub. You can define other bucket names using the option _-b_ but you should note that this command makes all data in the bucket publicly accessible, including data that has been previously uploaded to the bucket.

The public URL of a data object:
`https://a3s.fi/username-projectNumber-pub/object_name`

An object uploaded with _a-publish_ can be removed from Allas using the command _a-delete_.

A sample session with _a-publish_, uploading the document _presentation.pdf_ to the default public bucket in Allas:

```text
> **a-publish presentation.pdf** 
Files to be uploaded:  presentation.pdf
Bucket: kkayttaj-1234567-pub
Processing: presentation.pdf
Checking total size of presentation.pdf. Please wait.

Uploading data to allas.
Transferred:        4.188M / 4.188 MBytes, 100%, 7.700 MBytes/s, ETA 0s
Errors:                 0
Checks:                 0 / 0, -
Transferred:            1 / 1, 100%
Elapsed time:       500ms
Confirming upload...
presentation.pdf OK

Adding metadata for uploaded presentation.pdf
presentation.pdf uploaded to kkayttaj-1234567-pub
Publick link: https://a3s.fi/kkayttaj-1234567-pub/presentation.pdf

Upload ready
```

## a-flip

`a-flip` is a tool to make individual files temporarily available over the internet. It is intended for situations where you
want to make a copy of a file visible on the internet for a short while e.g. for copying to another platform shared with a co-worker.

a-flip copies a file to Allas into a bucket that can be publicly accessed. Thus, anyone with the address (URL) of the 
uploaded data object can read and download the data with a web browser or tools like *wget* and *curl*. 
a-flip works similarly to a-publish with some differences: 
    1) Only the predfined bucket name (_username-projectNumber_-flip) can be used.
    2) Upon execution, it checks the content of the flip bucket and deletes objects that are older than two days.

The basic syntax:
```text
a-flip file_name
```
The file is uploaded to the bucket _username-projectNumber_-flip. The URL of the uploaded object:

https://a3s.fi/username-projectNumber-flip/file_name


## a-find

The `a-find` command lists and locates data that has been uploaded to Allas using `a-put`.

The basic syntax:
```text
a-find query_term
```

The query term is compared to the names and original paths of the files that have been uploaded to
Allas, and matching objects are reported (but not downloaded). **Note:** Data uploaded 
to Allas using other tools than `a-put` is not included in this search process.

The query term is processed as a regular repression where some characters, e.g. period (.), have a special meaning.
The same regular expression syntax is used with e.g. the *grep*, *awk* and *sed* commands.
The most commonly occurring special characters:

- Period (**.**) is used to define any single character.
- **^** marks the beginning of a line.
- **$** marks the end of a line.
- **[ ]** matches any character inside the brackets. For example, [abc] would match a, b or c.
- **[^ ]** matches any character except the characters inside the brackets.   
    For example, [^abc] would select all rows that contain characters than are not a, b and c.
- ** * ** matches zero or more of the preceding characters or expressions.
    `\{n,m\}` matches n to m occurrences of the preceding characters or expressions.

Options:

- **-f**, **--files** List the names of matching files inside the objects in addition to the object name.
- **-p**,**--project _project_ID_** Search matches in the buckets of the defined project instead of the currently configured project. 
- **-b**, **--bucket _bucket_name_** By default, all default buckets used by `a-put` are searched. The option </br>*-bucket* allows you to specify a single bucket for the search. Use this option also in cases where you have stored data in a bucket with a non-standard name.
- **-s**, **-silent** Print only the object names and the number of hits. If the _-f_ option is used, print the object name and the matching file names on one row.


## a-info shows information about an uploaded dataset
                             
The command `a-info` allows you to get information about a dataset that has been uploaded to Allas using `a-put`.    
```text
a-info object_name
```                          
                             
## a-get retrieves stored data

This tool is used to download data that has been uploaded to the Allas service using the `a-put` command.
The basic syntax:
```text
a-get object_name
```

By default, the object is retrieved, uncompressed and extracted to a file or directory that was used in upload. If a directory or file with the same name already exists, you must either remove the existing file/directory or assign the downloaded data to a new directory with the `-target` option.

Options:

- **-p**, **--project _project_ID_** Retrieve data from the buckets of the defined project instead of the currently configured project. 
- **-f**, **--file _file_name_** Retrieve only a specific file or directory from the stored dataset. **Note:** Define the full path of the file or directory within the stored object.
- **-t**, **-target _dir_name_** Create a new target directory and deposit the data there.

# a_commands, easy and safe

The Allas object storage system can be used in multiple ways and for many purposes. In many cases, effective usage of Allas requires that the user knows the features of both Object Storage systems and the software or protocol that is used to manage data  in Allas.

For those users, that just want to use Allas for storing data that is in CSC computing environment, CSC provides a set of commands for moving data between CSC computing environment and Allas. The available Allas tools are:
  
- a_put : upload a file or directory to Allas as one object
- a_publish: upload a file to Allas into a bucket that allows public access over the internet
- a_get : download a stored dataset (object) from Allas
- a_find : check, what dataset(object) stored with a_put contains the file you are looking for
- a_delete : delete an object from Allas
- a_info : Display information about an object in Allas


## a_put uploads data to Allas

`a_put` is used to upload data from the disk environment of Taito or Puhti to 
Allas storage environment. The basic syntax of the command is:

```
a_put directory_or_file
```

By default, this tool performs following operations:

1. Ensure that there is a working connection to Allas storage service and 
define the project that will be used to store the data.

2. In case of directory, the content of the directory is collected into single file
(using `tar` command).

3. Data is compressed using `zstdmt` command (unless compression is skipped with `-n` option).

4. The compressed data is uploaded to Allas using `rclone` command and _swift_ protocol.

By default a_put uses standard buket and object names that depend on a username, project and the location
of the data to be uploaded. Data that locates in:
 
  - a) $WRKDIR(Taito) or $SCRATCH(Puhti) is uploaded to bucket: _username-pojectNumber_-SCRATCH
  - b) $HOME is uploaded to: _username-pojectNumber_-HOME
  - c) in other cases the data is uploaded to: _username-pojectNumber_-MISC
  
For example for user _kkaytaj_ belonging to project _12345_, data locating in HOME directory
will be uploaded to bucket: _kkayttaj-12345-HOME_.

If yuou wish to use other that the standard bucket, you can define a bukcet name with option _-b_ or _--bucket_.

The compressed dataset will be stored as one object. The by default the object name depends on the
file name and location. The logic used here is such that the possible subdirectory path in Taito is included 
in the object name. E.g. a file called *test_1.txt* in $WRKDIR can be stored with commands:

```
cd $WRKDIR
a_put test_1.txt
```

In this case the file is stored to bucket: _kkayttaj-12345-SCRATCH_
as object: *test_1.txt.zst*

If you have another file called *test_1.txt* that located in _$WRKDIR/project2/sample3_
you can store it with commands:
   
```
cd $WRKDIR/project2/sample3
a_put test_1.txt
```
  
Or commands:
```
cd $WRKDIR
a_put project2/sample3/test_1.txt
```
In this case the file is stored to bucket: *kkayttaj-12345-SCRATCH* 
as object:  *project2/sample3/test_1.txt.zst*

In addition to the actual data object a second object, containing 
metadata is created. This metadata object has the same name as the
main file with extension: *_meta*. This metadata file is used by the 
other *a_* commands and normally it is not displayed to the user.

If you wish to use some other than the default object name you can define it with option: _-o_ or _--os_name_

For example
```
cd $WRKDIR
a_put project2/sample3/test_1.txt -b newbuket1 - o case1.txt -n
```
The command abve woud upload file test_1.txt to allas into bucket _newbucket1_ as object _case1.txt_.
As option _-n_ is used the data is stored in an uncompressed format. 


## a_publish 

a_publish copies a file to Allas into a bucket that can be publicly accessed. Thus anyone, with the address (URL) of the 
uploaded data object can read and download the data with a web browser or tools like wget and curl. 
a_pubish works mostly like a_put but there are some diferences: 
1) a_publish can upload only files, not directories, 
2) files are not compressed but they uploaded as they are 
3) the access control of the target bucket is set so that it available in read-only mode to the internet.

The basic syntax of the command is:

```
a_publish file name
```
By default the file is uploaded to a bucket : _username-pojectNumber_-pub. You can define other bucket names too using option _-b_ but you should note that this command will make all data in the bucket publicly accessible, including data that has been previously uploaded to the bucket.

The pubic URL of dataobject is:

https://object.pouta.csc.fi/_username_-_projectNumber_-pub/_object_name_

An object uploaded with _a_publish_ can be removed from Allas with command _a_delete_.

Sample session with _a_public_. Uploading document prsenetation.pdf to the default public bucket in Allas


```
> **a_publish presentation.pdf** 
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
Publick link: https://object.pouta.csc.fi/kkayttaj-1234567-pub/presentation.pdf

Upload ready
```




## a_find

A_find command allows you to list and locate data that has been uploaded to Allas usinng `a_put`.
The basic syntax of the command is:
```
a_find query_term
```

The query term is compared to the names and original paths of the files that have been uploaded to
Allas and the matching objects are reported (but not downloaded). Note that data, that has been uploaded 
to Allas using other tools than `a_put` is not included in this serach process.

The query term is processed as a regular repression where some characters, for example dot (.), have a special meaning.
The same regular expression syntax is used with e.g. grep, awk and sed commands.
The most commonly occurring special characters are listed below:

- the dot (**.**) is used to define any single character.
- **^** means the beginning of a line
- **$** means the end of a line
- **[ ]** matches any of the characters inside the brackets. For example [abc] would match a,b or c.
- **[^ ]** matches any character, except the characters inside the brackets.   
    For example [^abc] would select all rows that contain also other characters
    than just a,b and c.
- ** * ** matches zero or more of the preceding character or expression  
    `\{n,m\}` matches n to m occurrences of the preceding character or expression



Options:

- **-f**, **--files**  Lists the names of the matching files inside the objects in addition to the object name.

- **-p**,**--project _project_ID_**   Search matches from the buckets of the defined project in stead of the currently configured project. 

- **-b**, **--bucket _bucket_name_**   By default all the buckets, used by `a_put`, are searched. Option -bucket allows you to specify a single bucket that will be used for the search. You should use these this option also in cases where you have stored data to buckets with non-standard name.

- **-s**, **-silent**            Output just the object names and number of hits. If _-f_ option is used too, print the object            name and matching file names on one row.


## a_info shows information about an uploaded dataset
                             
Command `a_info` allows you to get information about a dataset that has been uploaded to allas using `a_put`.    

```
a_info _object_name_
```                          
                             
## a_get retrieves the stored data

This tool is used to download data that has been uploaded to Allas service using the `a_put` command.
The basic syntax of the command is:
```
a_get _object_name_
```

By default, the object is retrieved and uncompressed. By default, the data is extracted to a file or directory that was used in uploading. If a directory or file with the same name already exists, you must either remove the existing file/directory or guide the downloaded data to new directory defined by -target option.

a_get options:

- **-p**, **--project _project_ID_**  Retrieve data form the buckets of the defined project in stead of the currently configured project. 

- **-f**, **--file _file_name_**      Retrieve just a specific file or directory from the stored dataset. Note that you need to define the full path of the file or directory within the stored object

- **-t**, **-target _dir_name_**      If this option is defined, a new target directory is created and the data is retrieved there.




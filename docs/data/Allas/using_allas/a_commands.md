# a_ commands, easy and safe

The Allas object storage system can be used in multiple ways and for many purposes. In many cases, effective usage of Allas requires that the user knows the features of both object storage system and the software or protocol that is used to manage data  in Allas.

For those users, that just want to use Allas for storing data that is in CSC computing environment, CSC provides a set of commands for managing and moving data between CSC computing environment and Allas. The available tools are:
  
|a_command | Function |
| :--- | :--- |
| a_put | Upload a file or directory to Allas as one object |
| a_list | List buckets and objects in Allas |
| a_publish | Upload a file to Allas into a bucket that allows public access over the internet |
| a_flip | Upload a file temporarily to Allas into a bucket that allows public access over the internet |
| a_get | Download a stored dataset (object) from Allas |
| a_find | Search and locate data that has been uploaded with a_put |
| a_delete | Delete an object from Allas |
| a_info | Display information about an object in Allas |

In addition to the above commands, there is separate tools for other purposes:

 * __allas_conf__ : Set up and open connection to Allas
 * __a_backup__ : Create a backup copy of a local dataset into a backup repository in Allas.
 * __allas_mount__ : Mount a bucket in allas to be used as read-only directory in your local environment.
 

If you use a_ commands outside of the Supercomputers, check the [allas-cli-utils documentation](https://github.com/CSCfi/allas-cli-utils/blob/master/README.md) for installing these tools.
	
## opening connection

In order to use these tools in Puhti and Taito, you must first load a_ commands with:
```text
module load allas
```
After that you can open connection to Allas storage service with command:
```text
allas_conf
```
The connection remains open for three hours. You can re-run the _allas_conf_ command at anytime
to continue the validity of the connection for three more hours or to switch to use another allas 
project. 

By default allas_conf lists your projects that have access to Allas, but if you know the name of the project, you
can give it as an argument. For example:

```text
allas_conf project_123456
```
Note that the Allas project don't need to be the same as the project you are using in Puhti or Taito.


## a_put uploads data to Allas

`a_put` is used to upload data from the disk environment of Taito and Puhti to 
Allas storage environment. The basic syntax of the command is:

```
a_put directory_or_file
```

By default, this tool performs following operations:

1.    Ensures that there is a working connection to Allas storage service and 
defines the project that will be used to store the data.

2.    In case of directory, the content of the directory is collected into a single file
using `tar` command.

3.    By default, option `--compress` (`-c`), is used. This means that the data is compressed using _zstdmt_ command.
This is the recommended way if you will be using the data only in CSC computing servers.  If you plan to use the 
uploaded data in other servers, where _zstdmt_ compression may not be available, you can disable compression with 
option `--nc` (`-n`).

4.    The compressed data is uploaded to Allas using `rclone` command and _swift_ protocol.

By default a_put uses standard bucket and object names that depend on username, project and the location
of the data to be uploaded. Data that locates in:

*    a) $WRKDIR (Taito) is uploaded to bucket: _username_projectNumber_-taito-WRKDIR
*    b) $SCRATCH (Puhti) is uploaded to bucket: _projectNumber_-puhti-SCRATCH
*    c) $PROJAPPL (Puhti) is uploaded to bucket: _projectNumber_-puhti-PROJAPPL 
*    d) in other cases the data is uploaded to: _username-projectNumber_-MISC
  
For example, for user _kkayttaj_, belonging to project _12345_, data locating in HOME directory
will be uploaded to bucket: _kkayttaj-12345-MISC_.

If you wish to use other than the standard bucket, you can define a bucket name with option _-b_ or  
_--bucket_.

The compressed dataset will be stored as one object. By default, the object name depends on the file name and location. The logic used here is such that the possible subdirectory path in Puhti or Taito is included in the object name, e.g. a file called *test_1.txt* in $WRKDIR in Taito can be stored with commands:

```text
cd $WRKDIR
a_put test_1.txt
```

In this case the file is stored to bucket: _kkayttaj-12345-taito-WRKDIR_
as object: *test_1.txt.zst*

If you have another file called *test_1.txt* that locates in _$WRKDIR/project2/sample3_
you can store it with commands:
   
```text
cd $WRKDIR/project2/sample3
a_put test_1.txt
```
  
Or commands:
```text
cd $WRKDIR
a_put project2/sample3/test_1.txt
```
In this case the file is stored to bucket: *kkayttaj-12345-taito-WRKDIR* 
as object:  *project2/sample3/test_1.txt.zst*

In addition to the actual data object, a second object containing metadata is created. This metadata object has the 
same name as the main object with extension: *_ameta*. This metadata file is used by the 
other *a_commands* and normally it is not displayed to the user, but if you study the buckets
with tools like _swift_ or _rclone_ you will see these metadatafiles too.

If you wish to use some other name than the default object name you can define it with option: _-o_ or  
_--object_

For example:
```text
cd $WRKDIR
a_put project2/sample3/test_1.txt -b newbuket1 - o case1.txt -n
```
The command above would upload file *test_1.txt* to Allas into bucket _newbucket1_ as object _case1.txt_.
As option _-n_ is used, the data is stored in an uncompressed format. 


## a_list

You can list all the buckets belonging to the project with command:
```text
a_list
```
Displaying the objects including to a bucket can be done with command:
```text
a_list bucket_name
```
If you can also add beginning of the object name in addition to to bucket name in order to see only certain buckets

```text
a_list bucket_name/begining_of_the_object
```



## a_publish 

`a_publish` copies a file to Allas into a bucket that can be publicly accessed. Thus, anyone with the address (URL) of the 
uploaded data object can read and download the data with a web browser or tools like *wget* and *curl*. 
a_publish works mostly like a_put but there are some differences: 
1) a_publish can upload only files, not directories. 
2) files are not compressed but they are uploaded as they are. 
3) the access control of the target bucket is set so that it is available in read-only mode to the internet.

The basic syntax of the command is:

```text
a_publish file_name
```
By default, the file is uploaded to a bucket _username-projectNumber_-pub. You can define other bucket names too using option _-b_, but you should note that this command will make all data in the bucket publicly accessible, including data that has been previously uploaded to the bucket.

The public URL to a data object is:

`https://a3s.fi/username-projectNumber-pub/object_name`

An object uploaded with _a_publish_ can be removed from Allas with command _a_delete_.

Sample session with _a_public_. Uploading document _presentation.pdf_ to the default public bucket in Allas:


```text
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
Publick link: https://a3s.fi/kkayttaj-1234567-pub/presentation.pdf

Upload ready
```

## a_flip

`a_flip` is a tool to make individual files temporarily available over the internet. It is intented for situations where you
want to make a copy of a file visible through internet for a short wile for example for copuying to another platform are sharing with a co-worker.

a_flip copies a file to Allas into a bucket that can be publicly accessed. Thus, anyone with the address (URL) of the 
uploaded data object can read and download the data with a web browser or tools like *wget* and *curl*. 
a_flip works mostly like a_publish but there are some differences: 
    1) only the predfined bucket name ( _username-projectNumber_-flip ) can be used
    2) When the command is executed, it checks the content of the flip bucket and deletes objects that are older than two days

The basic syntax of the command is:

```text
a_flip file_name
```
The file is uploaded to a bucket _username-projectNumber_-flip. The URL to the uploaded object is:

https://a3s.fi/username-projectNumber-flip/file_name


## a_find

a_find command allows you to list and locate data that has been uploaded to Allas using `a_put`.
The basic syntax of the command is:
```text
a_find query_term
```

The query term is compared to the names and original paths of the files that have been uploaded to
Allas and the matching objects are reported (but not downloaded). **Note:** Data that has been uploaded 
to Allas using other tools than `a_put` is not included in this search process.

The query term is processed as a regular repression where some characters, for example dot (.), have a special meaning.
The same regular expression syntax is used with e.g. *grep*, *awk* and *sed* commands.
The most commonly occurring special characters are listed below:

- the dot (**.**) is used to define any single character.
- **^** means the beginning of a line.
- **$** means the end of a line.
- **[ ]** matches any of the characters inside the brackets. For example, [abc] would match a, b or c.
- **[^ ]** matches any character, except the characters inside the brackets.   
    For example, [^abc] would select all rows that contain also other characters
    than just a, b and c.
- ** * ** matches zero or more of the preceding characters or expression  
    `\{n,m\}` matches n to m occurrences of the preceding characters or expression.

Options:

- **-f**, **--files** :  Lists the names of the matching files inside the objects in addition to the object name.

- **-p**,**--project _project_ID_** :   Search matches from the buckets of the defined project instead of the currently configured project. 

- **-b**, **--bucket _bucket_name_** :   By default, all the default buckets used by `a_put` are searched. Option </br>*-bucket* allows you to specify a single bucket that will be used for the search. You should use this option also in cases where you have stored data to a bucket with a non-standard name.

- **-s**, **-silent** : Outputs just the object names and number of hits. If _-f_ option is used too, prints the object            name and matching file names on one row.


## a_info shows information about an uploaded dataset
                             
Command `a_info` allows you to get information about a dataset that has been uploaded to Allas using `a_put`.    

```text
a_info object_name
```                          
                             
## a_get retrieves the stored data

This tool is used to download data that has been uploaded to Allas service using the `a_put` command.
The basic syntax of the command is:
```text
a_get object_name
```

By default, the object is retrieved and uncompressed and extracted to a file or directory that was used in uploading. If a directory or file with the same name already exists, you must either remove the existing file/directory or guide the downloaded data to a new directory defined by `-target` option.

a_get options:

- **-p**, **--project _project_ID_** :  Retrieves data from the buckets of the defined project instead of the currently configured project. 

- **-f**, **--file _file_name_** :      Retrieves just a specific file or directory from the stored dataset. **Note:** You need to define the full path of the file or directory within the stored object

- **-t**, **-target _dir_name_** :      If this option is defined, a new target directory is created and the data is retrieved there.


## a_backup

For *a_backup* documentation, see [a_backup](./a_backup.md).



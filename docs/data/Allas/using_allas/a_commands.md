# `a`-commands, easy and safe

The Allas object storage system can be used in multiple ways and for many purposes. In many cases, using Allas efficiently requires that the user knows the features of both the object storage system and the software or protocol used to manage the data in Allas.

For users who simply want to use Allas for storing data that is in the CSC computing environment, CSC provides a set of commands for managing and moving data between the CSC computing environment and Allas:


| `a`-command | Help text | Function |
| :--- | :--- | :--- |
| [`a-put`:material-arrow-down:](#a-put)| [GitHub:material-open-in-new:](https://github.com/CSCfi/allas-cli-utils/blob/master/help/a-put.md){ target=_blank}|Upload a file or directory to Allas |
| [`a-check`:material-arrow-down:](#a-check) |[GitHub:material-open-in-new:](https://github.com/CSCfi/allas-cli-utils/blob/master/help/a-check.md){ target=_blank }| Check if all the objects, that `a-put` should have created, are found in Allas |
| [`a-list`:material-arrow-down:](#a-list) |[GitHub:material-open-in-new:](https://github.com/CSCfi/allas-cli-utils/blob/master/help/a-list.md){ target=_blank }| List buckets and objects in Allas |
| [`a-publish`:material-arrow-down:](#a-publish) |[GitHub:material-open-in-new:](https://github.com/CSCfi/allas-cli-utils/blob/master/help/a-publish.md){ target=_blank }|Upload a file to Allas into a bucket that allows public access over the internet |
| [`a-flip`:material-arrow-down:](#a-flip) |[GitHub:material-open-in-new:](https://github.com/CSCfi/allas-cli-utils/blob/master/help/a-flip.md){ target=_blank }|Upload a file temporarily to Allas into a bucket that allows public access over the internet |
| [`a-get`:material-arrow-down:](#a-get) |[GitHub:material-open-in-new:](https://github.com/CSCfi/allas-cli-utils/blob/master/help/a-get.md)| Download a stored dataset (object){ target=_blank } from Allas |
| [`a-find`:material-arrow-down:](#a-find)|[GitHub:material-open-in-new:](https://github.com/CSCfi/allas-cli-utils/blob/master/help/a-find.md){ target=_blank }|Search and locate data uploaded with `a-put` |
| [`a-delete`:material-arrow-down:](#a-delete) |[GitHub:material-open-in-new:](https://github.com/CSCfi/allas-cli-utils/blob/master/help/a-delete.md){ target=_blank }| Delete an object in Allas |
| [`a-info`:material-arrow-down:](#a-info) |[GitHub:material-open-in-new:](https://github.com/CSCfi/allas-cli-utils/blob/master/help/a-info.md){ target=_blank }| Display information about an object in Allas |
| [`a-access`:material-arrow-down:](#a-access) |[GitHub:material-open-in-new:](https://github.com/CSCfi/allas-cli-utils/blob/master/help/a-access.md){ target=_blank }| Control access permissions of a bucket in Allas |
| `a-stream` |[GitHub:material-open-in-new:](https://github.com/CSCfi/allas-cli-utils/blob/master/help/a-stream.md){ target=_blank }|Stream the content of an object to standard output |
| `a-encrypt` |[GitHub:material-open-in-new:](https://github.com/CSCfi/allas-cli-utils/blob/master/help/a-encrypt.md){ target=_blank }|Make an encrypted copy of an object uploaded in Allas |

In addition to the above commands, there are separate tools for other purposes:

 * [`allas_conf`](allas-conf.md) : Set up and open a connection to Allas
 * [`allas-backup`](./a_backup.md) : Create a backup copy of a local dataset in a backup repository in Allas.
 * `allas-mount` : Mount a bucket in allas to be used as a read-only directory in the local environment.
 * `allas-health-check` : Check the integrity of over 5 GB objects in Allas.
 * [`allas-dir-to-bucket`:material-open-in-new:](https://github.com/CSCfi/allas-cli-utils/blob/master/help/allas-dir-to-bucket.md){ target=_blank } : copy a local file or directory to Allas. Parallel upload processes are used for over 5GB files.
 
If you use the `a`-commands outside the supercomputers, check the [allas-cli-utils documentation:material-open-in-new:](https://github.com/CSCfi/allas-cli-utils/blob/master/README.md){ target=_blank } for how to install these tools.

Below we discuss briefly of the most frequetly used features of `a`-commands. New features are added to `a`-commands every now and then and they may not be covered in the examples below. Use the help option `--help` to check the command specific information. For example:
```bash
a-put --help
```


## Example: Saving data from scratch directory to Allas

### Configuring a connection in supercomputers

In order to use these tools in Puhti and Mahti, first load `a`-commands:
```bash
module load allas
```

Configure Allas connection with [`allas-conf`](allas-conf.md).

```bash
allas-conf
```

### Copying data between Puhti scratch directory and Allas

Copying data from directory _/scratch/project_201234/dataset_3_ to Allas:

```bash
cd /scratch/project_201234
a-put dataset_3
```
The data in directory _dataset_3_ is stored to the default bucket _201234-puhti-SCRATCH_ as object: _dataset_3.tar_.
Available data buckets in Allas can be listed with command:

```bash
a-list
```
And the content of 201234-puhti-SCRATCH can be listed with command:

```
a-list 201234-puhti-SCRATCH
```
The directory that was stored to Allas can be retrieved back to Puhti with command:

```bash
a-get 201234-puhti-SCRATCH/dataset_3.tar
```


## `a`-commands in more detail

### `a-put`

`a-put` is used to upload data from the disk environment of Mahti and Puhti to 
the Allas storage environment. The basic syntax of the command:
```bash
a-put directory_or_file
```

By default, this tool performs the following operations:

1.    Ensure that there is a working connection to the Allas storage service and 
define the project that will be used to store the data.

2.    In the case of a directory, the content of the directory is collected as a single file
using the `tar` command. If you have a lot of data, this might not be a good option, consider then using some other [Allas client](../accessing_allas.md) that does not package files.

3.    The packed data is uploaded to Allas using the `rclone` command and the _Swift_ protocol.


By default, `a-put` uses the standard bucket and object names that depend on the username, project and location
of the data uploaded:

*    a) Data from /scratch in Puhti is uploaded to the bucket _projectNumber-puhti-SCRATCH_
*    b) Data from /scratch in Mahti is uploaded to the bucket _projectNumber-mahti-SCRATCH_
*    c) Data from /projappl in Puhti is uploaded to the bucket _projectNumber-puhti-PROJAPPL_ 
*    d) Data from /projappl in Mahti is uploaded to the bucket _projectNumber-mahti-PROJAPPL_ 
*    e) Data from $LOCAL_SCRATCH in Puhti is uploaded to the bucket _projectNumber-puhti-LOCAL_SCRATCH_
*    f) In other cases, the data is uploaded to _username-projectNumber-MISC_

For example, for the user _kkayttaj_, a member of the project _12345_, data located in the HOME directory
is uploaded to the bucket _kkayttaj-12345-MISC_.

If you wish to use other than the standard bucket, you can define a bucket name with the option _-b_ or  
_--bucket_.

The compressed dataset is stored as one object. By default, the object name depends on the file name and location. The possible subdirectory path in Puhti or Mahti is included in the object name, e.g. a file called _test_1.txt_ in /scratch/project_2012345 in Puhti can be stored using the commands:
```bash
cd /scratch/project_2012345
a-put test_1.txt
```

In this case, the file is stored in the bucket _2012345-puhti-SCRATCH_.
as the object _test_1.txt_

If you have another file called _test_1.txt_ located in _/scratch/project_2012345/kkayttaj/project2/_,
you can store it using the commands
```bash
cd /scratch/project_2012345/kkayttaj/project2/
a-put test_1.txt
```
or
```bash
cd /scratch/project_2012345/kkayttaj
a-put project2/test_1.txt
```
In this case, the file is stored in the bucket _2012345-puhti-SCRATCH_ 
as the object _kkayttaj/project2/test_1.txt_.

In addition to the actual data object, another object containing metadata is created. This metadata object has the 
same name as the main object with the extension *_ameta*. This metadata file is used by the 
other `a`-commands, and normally, it is not displayed to the user, but if you examine the buckets
using tools like _swift_ or _rclone_, you will see these metadata objects as well.

If you wish to use a name differing from the default object name, you can define it with the option _-o_ or  
_--object_:
```bash
cd /scratch/project_2012345
a-put project2/test_1.txt -b newbucket1 -o case1.txt -c
```

The command above uploads the file *test_1.txt* to Allas in the bucket _newbucket1_ as the object _case1.txt.zst_.
As the option _-c_ is used, the data is stored in zstd compressed format. 

You can give several file or directory names for `a-put` and use * as a wildcard character when naming the data to be uploaded. Note that in these cases each item (file or directory) will be stored as a separate object. For example, say that we have a directory called _job123_ that contains files _input1.txt_, _input2.txt_ and _program.py_. In addition there are directories _output_dir_1_ and _output_dir_2_ .

Command:
```bash
a-put job123/output_dir_1 jobs123/input1.txt
```
uploads content of _output_dir_1_ to object _job123/output_dir_1.tar_ and _input1.txt_ to _job123/input1.txt_.

Similarly command
```bash
a-put job123/output_dir*
```
uploads content of _output_dir_1_ to object _job123/output_dir_1.tar_ and content of _output_dir_2_ to object _job123/output_dir_2.tar_. 

During upload datasets that are larger than 5 GB will be split and stored as several objects. This is done automatically to a bucket that is named by adding extension `_segments` to the original bucket name. For example, if you would upload a large file to  bucket  _kkayttaj-12345-MISC_ the actual data would be stored as several pieces into bucket _kkayttaj-12345-MISC_segments_. The target bucket (_kkayttaj-12345-MISC_) would contain just a front object that contains information what segments make the stored dataset. Operations performed to the front object are automatically reflected to the segments. Normally users don't need to operate with the segments buckets at all and objects inside these buckets should not be deleted or modified.


### `a-check`

This command goes through the Allas object names, that a corresponding `a-put` command would create, and then checks if object with the same name already exists in Allas. The main purpose of this command is to provide a tool to check if a large `a-put` command was successfully executed. `a-check` accepts the same command line options as `a-put`.

For example, if a dataset is uploaded with command:
```bash
a-put job123/*
```
The upload can be checked with command: 
```bash
a-check job123/*
```
The _a-check_ command compares the item names to be uploaded to the matching objects in Allas.
The files or directories that don't have a target object Allas, are reported and stored to a file:
missing_bucket-name_number. If some of the objects in the sample commands above would be missing, then
`a-check` would list the missing files and directories in file `missing_job123_67889` (the number in the end is
just a random number).

This file of missing items can be used with `a-put` option --input-list, to continue the failed upload process:
```bash
a-put --input-list missing_job123_67889
```

You should note, that `a-check` does does not check if the actual contents of the object is correct. It checks only the object names, which may originate from some other sources.

In addition to checking, if upload was successful, `a-check` can be used to do a "dry-run" test for `a-put` to see, what objects will be created or replaced before running the actual `a-put` command. 


### `a-list`

`a-list` is used to show the names of buckets and objects stored to Allas. `a-list` is designed to be used for objects uploaded with `a-put` but it shows objects that have been uploaded with other tools too. However, it doesn't show the _ameta_ metadata file files created by `a-put`, to keep the object listings shorter.

#### `a-list` examples

List all buckets belonging to a project:
```bash
a-list
```
Display the objects included in a bucket:
```bash
a-list bucket_name
```
Typing a part of an object's name lists a subset of objects:
```bash
a-list bucket_name/beginning_of_the_object
```
A more detailed listing, containing object size and date can be obtained with option `-l`
```bash
a-list -l 
```
Option `-d` make `a-list` to interpret /-characters in object names as pseudofolder separators.
```bash
a-list -d 
```

### `a-publish`

`a-publish` copies a file to Allas in a bucket that can be publicly accessed. Thus, anyone with the address (URL) of the 
uploaded data object can read and download the data with a web browser or tools like _wget_ and _curl_. 
`a-publish` works similarly to a-put with some differences: 

1) `a-publish` can upload only files, not directories. 
2) The access control of the target bucket is set so that it is available for any user in read-only mode.

The basic syntax:
```bash
a-publish file_name
```
By default, the file is uploaded to the bucket _username-projectNumber_-pub. You can define other bucket names using the option _-b_. You should note that this command makes all data in the target bucket publicly accessible, including data that has been previously uploaded to the bucket.

The public URL of a data object will be:
`https://a3s.fi/username-projectNumber-pub/object_name`

An object uploaded with `a-publish` can be removed from Allas using the command `a-delete`_.

A sample session with `a-publish`, uploading the document _presentation.pdf_ to the default public bucket in Allas:

```console
$ a-publish presentation.pdf
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


### `a-flip`

`a-flip` is a tool to make individual files temporarily available over the internet. It is intended for situations where you
want to make a copy of a file visible on the internet for a short while e.g. for copying to another platform shared with a co-worker.

`a-flip` copies a file to Allas into a bucket that can be publicly accessed. Thus, anyone with the address (URL) of the 
uploaded data object can read and download the data with a web browser or tools like _wget_ and _curl_. 
`a-flip` works similarly to `a-publish` with some differences:

1. Only the predefined bucket name (_username-projectNumber_-flip) can be used.
1. Upon execution, it checks the content of the flip bucket and deletes objects that are older than two days.

The basic syntax:
```bash
a-flip file_name
```
The file is uploaded to the bucket _username-projectNumber_-flip. The URL of the uploaded object:
```text
https://a3s.fi/username-projectNumber-flip/file_name
```


### `a-find`

The `a-find` command lists and locates data that has been uploaded to Allas using `a-put`.

The basic syntax:
```bash
a-find query_term
```

The query term is compared to the names and original paths of the files that have been uploaded to
Allas, and matching objects are reported (but not downloaded).

The query term is processed as a regular repression where some characters, e.g. period (.), have a special meaning.
The same regular expression syntax is used with e.g. the _grep_, _awk_ and _sed_ commands.
The most commonly occurring special characters:

- Period (**.**) is used to define any single character.
- **^** marks the beginning of a line.
- **$** marks the end of a line.
- **[ ]** matches any character inside the brackets. For example, [abc] would match a, b or c.
- **[^ ]** matches any character except the characters inside the brackets.   
    For example, [^abc] would select all rows that contain characters than are not a, b and c.
- **\*** matches zero or more of the preceding characters or expressions.
    `\{n,m\}` matches n to m occurrences of the preceding characters or expressions.

Options:


- **-a**, **--all**  By default only the standard buckets, used by `a-put`, are searched. Option `--all` defines that all the buckets of the project will be included in the search.
- **-f**, **--files** List the names of matching files inside the objects in addition to the object names.
- **-p**,**--project _project_ID_** Search matches in the buckets of the defined project instead of the currently configured project. 
- **-b**, **--bucket _bucket_name_** By default, all default buckets used by `a-put` are searched. The option _-bucket_ allows you to specify a single bucket for the search. Use this option also in cases where you have stored data in a bucket with a non-standard name.
- **-s**, **-silent** Print only object names and the number of hits. If the _-f_ option is used, print the object name and the matching file names on one row.

### `a-info`
                             
The command `a-info` allows you to get information about a dataset that has been uploaded to Allas using `a-put`.   

```bash
a-info bucket/object_name
```           
If you execute this command without any object name, it will list basic information of all of the objects of the current project and a total summary about how much data and objects your Allas project contains.
```bash
a-info 
```   

                             
### `a-get`

This tool is used to download data that has been uploaded to the Allas service using the `a-put` command.
The basic syntax:
```bash
a-get object_name
```
By default, the object is retrieved, uncompressed and extracted to a file or directory that was used in upload. If a directory or file with the same name already exists, you must either remove the existing file or directory, or assign the downloaded data to a new directory with the `-target` option.

Options:

- **-p**, **--project _project_ID_** Retrieve data from the buckets of the defined project instead of the currently configured project. 
- **-f**, **--file _file_name_** Retrieve only a specific file or directory from the stored dataset. **Note:** Define the full path of the file or directory within the stored object.
- **-d** **--target_dir** <dir_name> If this option is defined, a new target directory is created and the data is retrieved there.
- **-t** **--target_file** <file_name> Define a file name for the object for the object to be downloaded.
- **-l** **--original_location**       Retrieve the data to the original location in the directory structure.
- **--asis**                        Download the object without unpacking tar files and uncompressing zst compressed data.
- **--s3s3cmd**                       Use S3 protocol and s3cmd command for data retrieval in stead of Swift protocol and rclone.

At the moment, `a-get` can download only one object at a time. If you need to download large number of objects you need to use loops. For example to download all the objects in bucket _bucket_123_ , you could use commands:

```bash
#make a list of objects
a-list bucket_123 > object_list_bucket123

#use the list in for loop
for ob in $(cat object_list_bucket123)
do
  a-get $ob
done  

#remove the object list
rm object_list_bucket123
```


### `a-delete`
`a-delete` is used to remove data that has been uploaded to Allas service using the `a-put` command.
The basic syntax of the command is:
```bash
a-delete object_name
```

By default `a-delete` asks user to confirm the removal of an object. This checking can be skipped with option `-f`.

If you want to remove a bucket, you can use option `--rmb`. By default `a-delete --rmb` removes only empty buckets. If you want to delete non-empty bucket, you need to add option `--FORCE` to the command.

### `a-access`

By default, only project members can read and write the data in a bucket.
Members of the project can grant read and write access to the bucket and 
the objects it contains, for other Allas projects or make the bucket publicly
accessible to the internet.

`a-access` is a tool to control access permissions (swift protocol) of a bucket in Allas.

Syntax 
```bash
a-access +/-type project_id bucket
```
Options:

- **+r**,  **+read** <project_id>        Grant read access to the bucket for the project.
- **+w**,  **+write** <project_id>       Grant write access to the bucket for the project.
- **+rw**, **+read-write**  <project_id> Grant read and write access to the bucket for the project.
- **-r**,  **-read** <project_id>        Remove read access from the bucket.
- **-w**,  **-write** <project_id>       Remove write access from the bucket.
- **-rw**, **-read-write**  <project_id> Remove read and write access from the bucket to the project.
- **+p**,  **+public**                   Give public read-only access to the bucket.
- **-p**,  **-public**                   Remove public read-only access to the bucket.

For example, to allow members of project: _project_2001234_ to have read-only access to bucket: _my_data_bucket_, you can use command:
```bash
a-access +r project_2001234  my_data_bucket
```
The access permissions are set similarly to the corresponding _segments bucket too.

Note, that bucket listing tools don't show the bucket names of other projects,
not even in cases were the project has read and/or write permissions to the bucket.

For example in this case a user, belonging to project _project_2001234_, 
don't see the _my_data_bucket_ in the bucket list produced by command:
```bash
a-list
```
but the user can still list the contents of this bucket with command:  
```bash
a-list my_data_bucket
```
And download objects from the bucket with `a-get`.

`a-access` manages the access permissions only in the project and bucket level.
Use **swift post** command for more sophisticated access control.

If you run `a-access` command for a bucket without any modification options,
it will print out the current settings of the bucket.


## Configuring your `a`-commands

A users can modify the default settings of `a`-commands by making a configuration file named as **.a_tools_conf** to their **home directory**.  In this file you can set default values for many of the functions that are defined with `a-put` command options.

For example, if you are working mostly with files that would benefit from compression, you might like to use the _--compress_ option with `a-put`. If you want this to be default setting you could create .a_tools_conf file
that contains setting:

```text
compression=1
```
Now command:
```bash
a-put my_data.b
```
will compress the data during the upload process (that would normally not be the case). However, you can still skip compression with option _--nc_.

```bash
a-put --nc my_data.b
```
 
You can check most commonly used settings from this sample [`.a_tools_conf`:material-open-in-new:](https://github.com/CSCfi/allas-cli-utils/edit/master/.a_tools_conf){ target=_blank } file. Copy the sample file to your home directory and un-comment and define the variables you wish to use.

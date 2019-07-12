# a_ Commands, Easy and safe

The Allas object storage system can be used in multiple ways and for many purposes. In many cases effective usage of Allas requires that the user knows the features of both Object Storage systems and the software or protocol that is used.

For those users, that just want to use allas for storing data that is in CSC computing eviroment, CSC provides a set of commands for moving data between CSC computing environment and Allas. The available Allas tools are:
  
* a_put : upload a file or directory to Allas as one object
* a_get : download a stored dataset (object) from Allas
* a_find : check, what dataset(object) stored with a_put contains the file you are looking for
* a_delete : delete an object from Allas
* a_info : Display information about an object in Allas


## a_put uploads data to allas.

<i>a_put</i> is used to upload data from the disk environment of Taito or Puhti to 
allas storage environmnet. The basic syntax of the command is:

>   a_put <i>directory_or_file</i>

By default this tool performs following operations:

1. Ensure that there is a working connection to Allas storage service and 
define the project that will be used to store the data.

2. In case of directory, the content of the directory is collected into single file
(using <i>tar</i> command).

3. Data is compressed using <i>zstdmt</i> command.

4. The compressed data is uploaded to Allas using <i>rclone</i> command and <i>swift</i> protocol.

The location were data is stored in allas can be defined with options
<i>-bucket</i> and <i>-os_file</i>, but defining these values is normally not needed as you should use the defaut bucket names.
 The default bucket in allas  depends on the original location of the data. Data that locates in:
 
  * a) $WRKDIR(Taito) or $SCRATCH(Puhti) is uploaded to bucket:  <i>username-poject_number</i>-SCRATCH
  * b) $HOME is uploaded to: <i>username-poject_number</i>-HOME
  * c) in other cases the data is uploaded to: <i>username-poject_number</i>-MISC

For example for user <i>kkaytaj</i> belonging in <i>project_12345</i>, data locating in HOME directory
will be uploaded to bucket: <i>kkayttaj-12345-HOME</i>.

The compressed dataset will be stored as one object. The object name depends on the
file name and location. The logic used here is such that the possible subdirectory path in Taito is included 
in the object name. E.g. a file called <i>test_1.txt</i> in $WRKDIR can be stored with commands:

>     cd $WRKDIR

>     a_put test_1.txt

In this case the file is stored to bucket: <i>kkayttaj-12345-SCRATCH</i>
as object: <i>test_1.txt.zst</i>

If you have another file called <i>test_1.txt</i> that locates in <i>$WRKDIR/project2/sample3</i>
you can store it with commands:
   
>     cd $WRKDIR/project2/sample3

>      a_put test_1.txt
  
Or commmands:
>     cd $WRKDIR

>     a_put project2/sample3/test_1.txt

In this case the file is stored to bucket: kkayttaj-12345-SCRATCH 
as object:  project2/sample3/test_1.txt.zst

In addition to the actual data object a second object, containing 
metadata is created. This metadata object has the same name as the
main file with extension: _meta. This metadata file is used by the 
other a_ commands and normally it is not dailplayed to the user.


## a_find

A_find command allows you to list and locate data that has been uploaded to Allas usinng <i>a_put</i>.
The basic syntax of the comand is:

>    a_find <i>query_term</i>

The query term is compared to the names and original paths of the files that have been uploaded to
Allas and the matching objects are reported (but not downloaded). Note that data, that has been uploaded 
to Allas using other tools than <i>a_put</i> is not included in this serach process.

The query term is procecced as a reqular repression where some characters, for example dot (.), have a special meaning.
The same regular expression syntax is used with e.g. grep, awk and sed commands.
The most commonly occurring special characters are listed below:

*the dot (<b>.</b>) is used to define any single character.
* <b>^</b> means the beginning of a line
* <b>$</b> means the end of a line
* <b>[ ]</b> matches any of the characters inside the brackets. For example [abc] would match a,b or c.
* <b>[^ ]</b> matches any character, except the characters inside the brackets. 
    For example [^abc] would select all rows that contain also other characters
    than just a,b and c.
* <b>*</b> matchs zero or more of the preceding character or expression
    \{n,m\} matches n to m occurrences of the preceding character or expression



Options:

* <b>-files</b>  Lists the names of the matching files inside the objects in addition to the object name.

* <b>-project <i>project_ID</i></b>   Search matches from the buckets of the defined project in stead of the currently configured project. 

* <b>-bucket <i>bucket_name</i></b>   By default all the buckets, used by <i>a_put</a>, are searched. Option -bucket allows you to specify a single bucket that will be used for the search. You shuould use these this option also in cases where you have stored data to buckets with non-standard name.

* <b>-silent </b>            Output just the object names and number of hits. If <i>-file<i> option is uses too, print the object name and matching file name on one row.
                             
## g_get retrieves the stored data

This tool is used to download data that has been uploaded to Allas service using the <i>a_put</i> command.
The basic syntax of the comand is:

>    a_get object_name

By default the object is retrieved and uncompressed. By default the data is extacted to a file or directory that was used in  uploading. If a directory or file with the same name already exists, you must either remove the exixting file/directory or guide the downloaded data to new directory defined by -target option.

a_get options:

* <b>-project <i>project_ID</i></b>  Retrieve data form the buckets of the defined project in stead of the currently configured project. 

* <b>-file <i>file_name</i></b>      Retrieve just a specific file or directory from the stored dataset. Note that you need to define the full path of the file or directory within the stored object

* <b>-target <i>dir_name</i></b>      If this option is defined, a new target directory is created and the data is retrieved there.




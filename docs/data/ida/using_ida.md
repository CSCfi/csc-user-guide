# Moving data between IDA and CSC computing environment

IDA is a general storage service for research data. It is part of the [Fairdata.fi]( https://www.fairdata.fi/) research data management environment and not directly linked to the CSC computing environment. Even though CSC produces and hosts the IDA service and the IDA storage space is applied to a CSC project, the storage space is granted by the home organization of the user (Finnish higher education institute or state research institute) or based on an Academy of Finland funding decision. IDA users can use the storage space from both their own computers and from the servers hosted by CSC. More information about applying for IDA storage space can be found from through IDA's website:

 * [https://www.fairdata.fi/en/ida/](https://www.fairdata.fi/en/ida/)

IDA can be used with a web browser user interface as well as with a command line client tool `ida` that is available on the computing servers hosted by CSC (Puhti and Mahti). IDA client is also available for download from [GitHub](https://github.com/CSCfi/ida2-command-line-tools).

The storage of files in IDA can be managed using the web and command line client interfaces; however, the contents of the stored files can't be modified directly. Instead, a stored file must be first retrieved from IDA to either CSC supercomputers or some other computer in order to analyse or modify the data. In that sense IDA resembles very much the [Allas storage environment](../Allas/introduction.md). However, IDA and Allas are designed to serve different use cases:

 * Allas is low-level and high-capacity storage service for utilising research data at CSC and other computing environments.          
 * IDA is designed for storing and sharing well defined and stable datasets, that are not used and modified on a daily basis. 

In a typical research project the raw data is first stored in Allas. When the research work has produced a more refined dataset from the original data, it can be stored to IDA so that metadata and persistent identifiers can be associated with the data via additional services. 

Each IDA project has two storage areas: _staging area_ and _frozen area_. The staging area is intended for collecting and organizing data in preparation for longer term storage and publication.  Data files that will not change anymore can be moved to frozen area to be stored in an immutable state. 

Files in the frozen area are visible to other Fairdata services and can be included in datasets using the [Qvain metadata tool](https://www.fairdata.fi/en/qvain/). Files in the staging area are not visible to other services and cannot be included in datasets.



## Configuring and using IDA in CSC supercomputers ##

Start by loading the IDA module:

```
module load ida
```

Before you can start using IDA client in CSC supercomputers you must set up your IDA connection by running the following command:
```text
ida_configure
```
The configuration process asks for your CSC project number, username and [application password](https://www.fairdata.fi/en/ida/user-guide/#app-passwords). 
This information can be obtained from the [security settings page of the IDA WWW-interface](https://ida.fairdata.fi/settings/user/security). The configuration is stored to your home directory, so you need to do it only once.

Once you have configured the connection, you can start using the `ida` command line client that enables data transport between the supercomputer and IDA. Data can be uploaded and downloaded from the _IDA staging area_. In the case of frozen area, only download is possible. Note that some key features of IDA, like moving data from staging area to the frozen area is possible only through the [IDA WWW interface](https://ida.csc.fi).

The basic syntax of the _ida_ commands is:
<pre>
ida <em>task</em> -<em>options target_in_ida target_in_puhti</em>
</pre>

To check the content of you staging area in IDA, use the command:
```text
ida info /
```
Adding option `-f` to the _ida_ command makes the command reference the frozen area instead of the staging area. For example the following command would give you information about the file _test2_, locating in the root of the frozen area:

<pre>
[kkayttaj@puhti-login2 ~] <b>ida info -f /test2</b>
project:    2000136
pathname:   /test2
area:       frozen
type:       file
pid:        5bc456a74ba89743214993f23695474
size:       113926178937
encoding:   application/octet-stream
modified:   2018-10-15T08:17:53Z
frozen:     2018-10-15T08:58:15Z
</pre>


Uploading and downloading files and directories between Puhti and IDA is done with the commands:

<pre>ida upload <em>target_in_ida local_file</em>
ida download <em>target_in_ida local_file</em> 
</pre>

For example in Puhti, the command:
```text
ida upload /test123/data1 test_data
```
will upload file: _test_data_ from Puhti to the IDA staging area and store the data in the directory _test123_ with the name _data1_. The
directory test123 will be automatically created to the staging area, if it does not already exist.

If you download a directory, the downloaded files are stored to a zip archive file. Thus you should define the local target file to have name extension .zip. For example:
```text
ida download /project1 project1_data.zip
```
The command above would download all the data from the IDA staging area directory _project1_ and store it to a zip archive file
_project1_data.zip_ in your current directory.

More information about using and configuring the IDA client, with additional examples, can be found from [https://github.com/CSCfi/ida2-command-line-tools](https://github.com/CSCfi/ida2-command-line-tools)


























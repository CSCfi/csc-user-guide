# Using IDA storage service in the CSC computing environment #

IDA is a general storage service for scientific data. It is part of the [Fairdata.fi]( https://www.fairdata.fi/) research data management environment and not directly linked to the CSC computing environment. Even though CSC produces and hosts the IDA service and users need to register to CSC, the storage space is granted by the home organization of the user (Finnish higher education institute, state reserach institute) or by the Academy of Finland based on a funding decision. IDA users can use the storage space from both their own computers and from the servers of CSC. More information about applying storage space from IDA can be found from through IDA's website:
    # [https://ida.fairdata.fi](https://ida.fairdata.fi)

IDA uses in-house developed www interface and client tool `ida` that is available in the computing servers of CSC.
The files that are in IDA can be managed through client interfaces but the content of the archived files can't be studied or modified. In stead, the stored file must be first retrieved back to the CSC servers or to some other computer in order to analyse or modify the dataset. In that sense IDA resembles very much the [Allas storage environment](../Allas/intoduction.md) However, IDA and Allas are designed to serve different use cases:
    # Allas is low-level and high-capacity storage service for utilising research data at CSC and other computing enviroments.         
    # IDA is desinged for storing and sharing more structured and stable datasets, that are not used and modified in daily bases. 

In a typical research project the raw data is first stored in Allas. When the research work has produced a more refined dataset form the original data, it can be stored to IDA so that metadata and persistent identifiers can be attached to the data. 


## Configuring and using IDA in Puhti ##

Each IDA project has two storage areas: _staging area_ and _frozen area_. The staging area is intended for collecting and managing data. A mature data set, that will not change anymore, can be moved to frozen area to be preserved and further linked to other Fairdata services.

The command line client of IDA, `ida`, enables data transport between Puhti and IDA. Data can uploaded and downloaded from the _IDA staging area_. In the case of frozen area, only download is possible. Note that some key features of IDA, like moving data to the frozen area of publishing data is possible only through the [IDA WWW interface](https://ida.csc.fi).

Before you can start using IDA client in Taito you must set up your IDA connection by running command.

```text
ida_configure
```

The configuration process asks for your CSC project number and [application password](https://www.fairdata.fi/en/ida/user-guide/#app-passwords). 
This information can be obtained from the [personal information page of the IDA WWW-interface](https://ida.fairdata.fi/settings/personal). 
The configuration is stored to your home directory so you need to do it only once.

Once you have configured the connection, you can start operating with IDA. The basic syntax of ida commands is:
```text
ida task -options target_in_ida target_in_taito
```

To check the content of you staging area in IDA, give command:
```text
ida info /
```
Adding option `-f` to the ida command makes the command to use the frozen area instead of staging area. For example the following command would give you information about file test2, locating in the frozen area:

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
 

Uploading and downloading files and directories between Puhti and IDA is done with commands:

<pre>ida upload <em>target_in_ida local_file</em>
ida download <em>target_in_ida local_file</em> 
</pre>

For example command:
```text
ida upload test123/data1 test_data
```
will upload file: _test_data_ from Taito to the IDA staging area and store the data there to directory _test123_ with name _data1_. The directory test123 will be automatically created to the staging area, if it does not already exist.

If your download a directory, the downloaded files are stored to Puhti as a zip archive. Thus you should define the local target file to have name extension .zip. For example:
```text
ida download project1 project1_data.zip
```
The command above would download all the data from the IDA staging area directory _project1_ and store it to a zip archive file _project1_data.zip_ in your current directory in Puhti.

More information about using and configuring IDA client can be found from https://github.com/CSCfi/ida2-command-line-tools
  

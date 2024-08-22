# Moving data between IDA and CSC computing environment

IDA is a general storage service for research data. It is part of the
[Fairdata.fi]( https://www.fairdata.fi/) research data management environment
and not directly linked to the CSC computing environment. Use of the IDA
service requires that the stored data is described as a research dataset with
Fairdata Qvain tool for others to discover. Even though CSC produces and hosts
the IDA service and the IDA storage space is applied to a CSC project, the
storage space is granted by the home organization of the user (Finnish higher
education institution or state research institute). IDA users can use the
storage space from both their own computers and from the servers hosted by CSC.
More information about applying for IDA storage space can be found at the
[IDA website](https://www.fairdata.fi/en/ida/).

IDA can be used with a web browser user interface, as well as with a
command-line client tool `ida` that is available on the computing servers
hosted by CSC (Puhti and Mahti). IDA client can also be downloaded from
[GitHub](https://github.com/CSCfi/ida2-command-line-tools).

The storage of files in IDA can be managed using the web and command-line
client interfaces. However, the contents of the stored files can't be modified
directly. Instead, a stored file must be first retrieved from IDA to either CSC
supercomputers or some other computer in order to analyze or modify the data.
In this sense IDA resembles very much the
[Allas object storage service](../Allas/introduction.md). However, IDA and
Allas are designed to serve different use cases:

* Allas is low-level and high-capacity storage service for utilizing research
  data at CSC and other computing environments.
* IDA is designed for storing and sharing well-defined and stable datasets that
  are not used or modified on a daily basis.

In a typical research project the raw data is first stored in Allas. When the
research work has produced a more refined dataset from the original data, it
can be stored in IDA so that metadata and persistent identifiers can be
associated with the data via additional services.

Each IDA project has two storage areas: _staging area_ and _frozen area_. The
staging area is intended for collecting and organizing data in preparation for
longer term storage and publication. Data files that will not change anymore
can be moved to the frozen area to be stored in an _immutable_ state.

Files in the frozen area are visible to other Fairdata services and can be
included in datasets using the
[Qvain metadata tool](https://www.fairdata.fi/en/qvain/). Files in the staging
area are not visible to other services and cannot be included in datasets.

## Configuring and using IDA in CSC supercomputers

The IDA client and configuration tools are activated with the command:

```bash
module load ida
```

When you start using the IDA client in CSC supercomputers for the first time,
you must set up your IDA connection by running the following command:

```bash
ida_configure
```

The configuration process asks for your CSC project number, username and
[application password](https://www.fairdata.fi/en/ida/user-guide/#app-passwords).
This information can be obtained from the
[security settings page of the IDA web interface](https://ida.fairdata.fi/settings/user/security).
The configuration is stored in your home directory, so you need to do it only
once.

Once you have configured the connection, you can start using the `ida`
command-line client that enables data transport between the supercomputer and
IDA. Data can be uploaded and downloaded from the IDA staging area. From the
frozen area only download is possible. Note that some key features of IDA, like
moving data from staging area to the frozen area, is possible only through the
[IDA web interface](https://ida.fairdata.fi).

The basic syntax of the `ida` commands is:

```bash
ida <task> [options] <target_in_ida> <target_in_puhti>
```

To check the contents of your staging area in IDA, use the command:

```bash
ida info /
```

Adding option `-f` to the `ida` command makes the command reference the frozen
area instead of the staging area. For example, the following command would give
you information about the file `test2` in the root of the frozen area:

```bash
[kkayttaj@puhti-login12 ~] ida info -f /test2
project:    2000136
pathname:   /test2
area:       frozen
type:       file
pid:        5bc456a74ba89743214993f23695474
size:       113926178937
encoding:   application/octet-stream
modified:   2018-10-15T08:17:53Z
frozen:     2018-10-15T08:58:15Z
```

Uploading and downloading files and directories between Puhti and IDA is done
with the commands:

```bash
ida upload <target_in_ida> <local_file>
ida download <target_in_ida> <local_file> 
```

For example in Puhti, the command:

```bash
ida upload /test123/data1 test_data
```

will upload file `test_data` from Puhti to the IDA staging area and store the
data in the directory `test123` with the name `data1`. The directory `test123`
will be automatically created in the staging area if it does not already exist.

If you download a directory, the downloaded files are stored as a zip archive
file. Thus, you should define the local target file to have the name extension
`.zip`. For example:

```bash
ida download /project1 project1_data.zip
```

The command above would download all the data from the IDA staging area
directory `project1` and store it as a zip archive file `project1_data.zip` in
your current directory.

More information about using and configuring the IDA client, including
additional examples, can be found in
[GitHub](https://github.com/CSCfi/ida2-command-line-tools).

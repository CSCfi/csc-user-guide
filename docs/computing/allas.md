# Using Allas object storage service from CSC Supercomputing environment

The disk environments of CSC supercomputers, Puhti and Mahti, are not intended for storing research data that is 
not actively used for computing. The data that needs to be stored for a longer time than just few weeks should be copied to Allas object storage service. 

Allas provides a platform that you can use to store your data as long as your CSC project is active. 
In addition to storing, Allas can be used for transporting data between different servers and sharing data
with other users.

## Getting access to Allas

By default, CSC computing projects do not have access to Allas. Thus, the first thing is to make sure that your project has access to Allas.
This can be done in the [MyCSC interface](https://my.csc.fi). Note that only the project manager can 
add new services for a project. Once Allas access is activated, all project members must visit the MyCSC and accept the terms 
of use for Allas before they can use the Allas storage area.

The default storage quota in Allas is 10 TB. As this space is shared with all project members, it is
possible that the space is not sufficient. In that case, you should estimate how much space is needed 
and request more space. The request should be sent to servicedesk@csc.fi.

## Connecting Allas 

In order to use Allas in Puhti or Mahti, first load the module _allas_:
```text
module load allas
```
Allas access for a specific project can then be enabled with command:
```text
allas-conf
```
or 
```text
allas-conf project_name
```
The _allas-conf_ command prompts for your CSC password. It lists your Allas projects and asks you to define a project (if not already defined as an argument). After that _allas-conf_ generates configuration files for several Allas clients and authenticates connection to Allas for the selected project. 

By default the _allas-conf_ activates tools that use Allas with **swift protocol**. 
You can alternatively use S3 protocol too, however in this document we 
discuss only _swift_ based Allas usage. 

Authentication is session specific and valid for eight hours at a time.
You can be connected to only one Allas project at a time in one terminal session. However, simutaneous terminal sessions
can use different Allas projects. The project you are using in Allas does not need to match the project you are using in 
Puhti or Mahti. You can refresh the authentication or change the target project at any time my running _allas-conf_ again. 


**Allas client software options for Puhti and Mahti and other linux servers**

The _allas_ module provides several tools that you can use to move data between Allas and the computing server.
You can cross-use the Allas clients as long as you access Allas with the same protocol (swift or S3).
Below is a list of the Allas clients that are most commonly used in Puhti and Mahti:

* **a-commands:** (Swift, optionally S3) [Easy and safe: a-commands](../data/Allas/using_allas/a_commands.md)
* **rclone:** (Swift, optionally S3) [Advanced tool: rclone](../data/Allas/using_allas/rclone.md)
* **swift python client:** (Swift) [Native Swift client](../data/Allas/using_allas/swift_client.md)
* **s3cmd:** (S3) [S3 client](../data/Allas/using_allas/s3_client.md#configuring-s3-connection-in-supercomputers)

More information about using Allas can be found from the Allas documentation:

* [Allas](../data/Allas/index.md)

The Allas documentation includes two tutorials that are especially designed for Puhti and Mahti users:

* [Examples for using Allas in CSC supercomputers](../data/Allas/allas-examples.md)

* [Using Allas in batch jobs](../data/Allas/allas_batchjobs.md)



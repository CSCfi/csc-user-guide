# Accessing Allas

## Gaining access

**Allas** access is based on CSC's customer projects. To be able to use Allas, you need to be a member of 
a CSC project that has the permission to use Allas. If you do not have a CSC account, you must first register as a CSC user
and join or start a computing project for which Allas has been enabled. This can be done in the
MyCSC user portal: [https://my.csc.fi]( https://my.csc.fi).

## Accessing Allas from the web

The OpenStack Horizon web interface provides easy-to-use basic functions for data management in Allas:

* [Web client – OpenStack Horizon Dashboard](./using_allas/web_client.md)

SD Connect provides sensitive data oriented web interface for Allas. By default this interface encrypts the uploaded data 
so that it can be only used in SD Desktop service. You can use it for non-sensitive data too if you switch off the encryption.

* [SD Connect](https://sd-connect.csc.fi) ([instructions](../sensitive-data/sd_connect.md))

## Accessing Allas in the CSC computing environment and other Linux platforms

In order to use Allas in Puhti or Mahti, first load the module _allas_:
```text
module load allas
```
Allas access for a specific project can then be enabled:
```text
allas-conf
```
or 
```text
allas-conf project_name
```
The _allas-conf_ command prompts for your CSC password (the same that you use to login to CSC servers). It lists your Allas projects and asks you to define a project (if not already defined as an argument). _allas-conf_ generates a _rclone_ configuration file for the Allas service and authenticates the connection to the selected project. You can only be connected to one Allas project at a time in one session. The project you are using in Allas does not need to match the project you are using in Puhti or Mahti, and you can switch to another project by running _allas-conf_ again.

Authentication information is stored in the shell variables *OS_AUTH_TOKEN* and *OS_STORAGE_URL* and is valid for up to eight hours. However, you can refresh the authentication at any time my running _allas-conf_ again. The environment variables are available only for that login session, so if you start another shell  session, you need to authenticate again in there to access Allas.

You can start using Allas with one of the following options. Note that the tools utilize two different protocols: _Swift_ and _S3_. Data uploaded using one protocol is not necessary readable with another protocol. 

**Allas client software options for Puhti and Mahti and other linux servers**

* **a-tools for basic use:** (Swift, optionally S3) [Quick and safe: a-commands](./using_allas/a_commands.md)
* **Advanced functions with rclone:** (Swift) [Advanced tool: rclone](./using_allas/rclone.md)
* **A wide range of functionalities:** (Swift) [Swift client](./using_allas/swift_client.md)
* **S3 client and persistent Allas connections:** (S3) [S3 client](./using_allas/s3_client.md#configuring-s3-connection-in-supercomputers)

The client software listed above can be used in other Linux servers as well, e.g. a virtual machine running in cPouta or your own Linux-based laptop. In that case, you need to install the client software and configure the connection to Allas yourself. Instructions: [allas-cli-utils](https://github.com/CSCfi/allas-cli-utils)

## Accessing Allas with Windows or Mac




## SD Connect service

The SD Connect WWW interface can be used upload, download, manage and share data in Allas.

* [CSC SD services](../sensitive-data/index.md)

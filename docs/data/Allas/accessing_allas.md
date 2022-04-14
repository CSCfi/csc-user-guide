# Accessing Allas

## Gaining access

**Allas** access is based on CSC's customer projects. To be able to use Allas, you need to be a member of 
a CSC project that has the permission to use Allas. If you do not have a CSC account, you must first register as a CSC user
and join or start a computing project for which Allas has been enabled. This can be done in the
MyCSC user portal: [https://my.csc.fi]( https://my.csc.fi).

Once you have Allas enabled you can access it for any machine or server that is connected to internet. This can be a your laptop, supercomputer at CSC, virtual machine in cloud or enven your phone.


## Accessing Allas from the web

At the moment CSC provides two web interfaces for Allas:

The OpenStack Horizon web interface in **cPouta** provides easy-to-use basic functions for data management in Allas:

* [Web client – OpenStack Horizon Dashboard](./using_allas/web_client.md)

**SD Connect** provides sensitive data oriented web interface for Allas. By default this interface encrypts the uploaded data 
so that it can be used in [SD Desktop](../sensitive-data/sd_desktop.md) service. You can use SD Connect for non-sensitive data too, if you switch off the encryption.

* [SD Connect](https://sd-connect.csc.fi) ([instructions](../sensitive-data/sd_connect.md))


## Accessing Allas in the CSC computing environment and other Linux platforms

Puhti and Mahti servers at CSC support many different tools for using Allas, These include

* **a-tools for basic use:** (Swift, optionally S3) [Quick and safe: a-commands](./using_allas/a_commands.md)
* **Advanced functions with rclone:** (Swift, optionally S3) [Advanced tool: rclone](./using_allas/rclone.md)
* **A wide range of functionalities:** (Swift) [Swift client](./using_allas/swift_client.md)
* **S3 client and persistent Allas connections:** (S3) [S3 client](./using_allas/s3_client.md#configuring-s3-connection-in-supercomputers)

Note that the tools listed above utilize two different protocols: _Swift_ and _S3_. Data uploaded using one protocol is not necessary compatible with another protocol. 

The software listed above can be used in other Linux servers as well, e.g. a virtual machine running in cPouta or your own Linux-based laptop. In that case, you need to install the client software and configure the connection to Allas yourself. Instructions : [allas-cli-utils](https://github.com/CSCfi/allas-cli-utils)

In Puhti and Mahti the Allas tools listed above are installed by CSC and provided through _allas_ module.
In order to use Allas in Puhti or Mahti, first load the Allas module:
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
The _allas-conf_ command prompts for your CSC password (the same that you use to login to CSC servers). It lists your Allas projects and asks you to define a project (if not already defined as an argument). _allas-conf_ generates an _rclone_ configuration file for the Allas service and authenticates the connection to the selected project. You can only be connected to one Allas project at a time in one session. The project you are using in Allas does not need to match the project you are using in Puhti or Mahti, and you can switch to another project by running _allas-conf_ again.

Authentication information is stored in the shell variables *OS_AUTH_TOKEN* and *OS_STORAGE_URL* and is valid for up to eight hours. However, you can refresh the authentication at any time my running _allas-conf_ again. The environment variables are available only for that login session, so if you start another shell session, you need to authenticate again in there to access Allas.

You can start using Allas with one of the following options. 


## Accessing Allas with Windows or Mac

In addition to the Web interfaces listed above, you can access Allas from you Windows or Mac coputer with locally installed client software. 
For example following tools can be used:
* [Cyberduck](./using_allas/cybeduck.md) provides easy to use graphical interface for moving data between local computer and Allas.
* [Rclone](./unsing_allas/rclone_local) is an command line tool that provides very effective way to use Allas.
* [a-tools](./using_allas/a_commands.md) these Allas specific commands can be installed in Mac OSX machines but not to Windows

The list above is not complete or exclusive. Any tool that supports Swift or S3 protocols can in in principle use Allas.



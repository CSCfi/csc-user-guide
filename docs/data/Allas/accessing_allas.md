# Accessing Allas

## Gaining access

**Allas** access is based on CSC's customer projects. To be able to use Allas, you need to be a member of 
a CSC project that has the permission to use Allas. If you do not have a CSC account, you must first register as a CSC user
and join or start a computing project for which Allas has been enabled. This can be done in the
MyCSC user portal: [https://my.csc.fi]( https://my.csc.fi).

## Accessing Allas from the web

The OpenStack Horizon web interface provides easy-to-use basic functions for data management in Allas:

[Web client – OpenStack Horizon Dashboard](./using_allas/web_client.md)

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

Authentication information is stored in the shell variables *OS_AUTH_TOKEN* and *OS_STORAGE_URL* and is valid for up to three hours. However, you can refresh the authentication at any time my running _allas-conf_ again. The environment variables are available only for that login session, so if you start another shell  session, you need to authenticate again in there to access Allas.

You can start using Allas with one of the following options. Note that the tools utilize two different protocols: _Swift_ and _S3_. Data uploaded using one protocol is not necessary readable with another protocol. 

**Allas client software options for Puhti and Mahti and other linux servers**

* **a-tools for basic use:** (Swift, optionally S3) [Quick and safe: a-commands](./using_allas/a_commands.md)
* **Advanced functions with rclone:** (Swift) [Advanced tool: rclone](./using_allas/rclone.md)
* **A wide range of functionalities:** (Swift) [Swift client](./using_allas/swift_client.md)
* **S3 client and persistent Allas connections:** (S3) [S3 client](./using_allas/s3_client.md#s3cmd-with-supercomputers)

The client software listed above can be used in other Linux servers as well, e.g. a virtual machine running in cPouta or your own Linux-based laptop. In that case, you need to install the client software and configure the connection to Allas yourself. Instructions: [allas-cli-utils](https://github.com/CSCfi/allas-cli-utils)

## Accessing Allas with Windows or Mac

For Windows and Mac, [Cyberduck](https://cyberduck.io/) provides a graphical user interface to Allas (note however that the above mentioned linux command line tools are available for Macs too). See the [list of functions](#cyberduck-functions) Cyberduck offers for data management.

The instructions below describe how to open a _Swift_-protocol-based Cyberduck connection to Allas. With this setup, Cyberduck is compatible with _rclone_, _Swift_ and _a-tools_ but not with _s3cmd_ based on the _S3_ protocol. More information: [Directory object error](using_allas/directory_object_error.md).


1\. Install **Cyberduck**.

2\. Navigate to the Cyberduck main menu and choose **Bookmark | New Bookmark** (_Ctrl-Shift-B_).

!["New bookmark"](./../../../img/cyberduck_bookmark.jpg)
**Figure** Creating a new bookmark

3\. In the first dropdown menu, choose _OpenStack Swift (Keysone 3)_.
    ( if your Cyberduc does not have this option available, you need to update it to a more recent version)

4\. As the **Server**, type _pouta.csc.fi_ and choose the **Port** _5001_. 

5\. In the section **Project:Domain:Username**, type (without spaces) the desired _project's name_, add "**:default:**" and your _Pouta username_ (this is the CSC user accout you use in CSC supercomputers and cPouta). Thus, it should be in the format _projectname:default:username_, e.g. *project_123456:default:john*.

6\. Type your CSC password in the **Password** field. You can close the bookmark by clicking **X** on the upper right corner of the pop-up window.

!["Entering information for a bookmark"](./../../../img/cyberduck_bookmark_info.jog)
**Figure** Entering information for a bookmark

7\. Navigate to the top left corner to the icons under _Open Connection_ and choose the **Bookmarks icon** (second from the left).
 
8\. Next, right-click the created bookmark and choose the option **Connect to server**.

!["Connecting to the server"](./../../../img/cyberduck_connect.jpg)
**Figure** Connecting to the server

Now you should be able to see the content of your project (which might be empty).

### Cyberduck functions

Cyberduck offers some basic functionalities for managing data in the object storage:

 * _Create_ buckets
 * _Upload_ objects
 * _List_ objects and buckets
 * _Download_ object and buckets
 * _Edit_ objects
 * _Edit_ metadata
 * _Share_ objects
 * _Remove_ objects and buckets

The Cyberduck user interface is quite easy to use. The data management options can be displayed by either right-clicking the bucket/object or choosing the bucket/object and then clicking the **Action** button on the menu bar. To navigate back to the previous directory, use backspace.

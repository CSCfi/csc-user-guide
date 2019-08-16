
# Accessing Allas

&nbsp;


## Getting Access to Allas

Usage of **Allas** is based on CSC customer projects. To be able to use Allas you need to be a member in 
a CSC project that has permission to use Allas. If you do not have a CSC account, you must first register as a CSC user
and join or start a computing project for which Allas has been enabled. All these steps can be done in the
MyCSC user portal: [https://my.csc.fi]( https://my.csc.fi){:target="_blank"}

The easiest way to use Allas is through the [web client](./using_allas/web_client.md){:target="_blank"} which offers basic tools for managing your data.

The following guidelines describe step by step how to establish Allas with different operating systems.

&nbsp;


## Accessing Allas with Supercomputers

The instructions for accessing and using Allas with Supercomputers can be found from [Using Allas with Supercomputers](./using_allas/common_use_cases.md#using-allas-with-supercomputers){:target="_blank"}.

&nbsp;


## Accessing Allas with Windows and Mac

With Windows and Mac we recommend the software [CyberDuck](https://cyberduck.io/){:target="_blank"}.

!!! note
    Please note that a directory uploaded with CyberDuck may not be
    downloadable with one command using some other client software
    with s3 protocol connection to Allas.

1\. Install **CyberDuck**.

2\. Navigate to the CyberDuck mainmenu and choose **Bookmark | New Bookmark** (_Ctrl-Shift-B_).

!["New bookmark"](/img/cyberduck_create_bookmark.PNG)
**Figure** Creating a new bookmark

3\. In the first drop-down menu, choose _Swift (OpenStack Object Storage)_

4\. As **Server** write _pouta.csc.fi_ and choose **Port** _5001_.

5\. In the section **Tenant ID:Access Key** type (without spaces) first the desired _project's name_, then add "**:**" and after that your _Pouta username_ (the one you use in pouta.csc.fi). Thus, it should be in form of *projectname:username*. For example, *project_123456:john*.

6\. Type your Pouta password in the **Secret Key** part. After that, you can close the bookmark by clicking X on the upper right corner of the pop-up window.

!["Filling information for a bookmark"](/img/cyberduck_bookmark_info.PNG)
**Figure** Filling the information for a bookmark

7\. Navigate to the top left corner to the icons under the _Open Connection_ and choose the **Bookmarks icon** (second from the left).
 
8\. Next, right-click with mouse the created bookmark and choose the option **Connect to server**.

!["Connecting to server"](/img/cyberduck_connect.PNG)
**Figure** connecting to server

Now you should be able to see the content of your project (which might be empty).

CyberDuck offers some basic functionalities for managing data in object storage:

 * Upload objects
 * Edit objects
 * Edit metadata
 * Share buckets
 * Remove objects

&nbsp;


## Accessing Allas with Linux


The command-line tools _Swift_, _S3_ and _s3cmd_ are already installed on Supercomputers (**Taito**, **Puhti** and **Mahti**). The best client for you depends on what you will do with the data. More information about the clients in [the next section](#protocols).


| Command-line tool | Requirements |
| :--------: | --------- |
| a_commands | Usage on Puhti. See the instructions [here](./using_allas/a_commands.md){:target="_blank"}. |
| Swift	| On Puhti you can setup the environmental variables with:</br>`source /appl/opt/allas_conf` </br>Elsewhere, download and source openrc.sh, more info [below](#openrc). |
| S3 | More info [here](./using_allas/s3_client.md){:target="_blank"}. |
| s3cmd	| Configuration file .s3cfg populated. More info [here](./using_allas/s3_client.md){:target="_blank"}. |


<a id="openrc"></a>

**Getting openrc file:**

1. Go to [pouta.csc.fi](https://pouta.csc.fi/){:target="_blank"} and **Login**

2. Navigate to **Compute | Access & Security | API Access**

3. Download the **Openstack RC File v3** from the upper right corner

!["Getting openrc file"](/img/rc-file-example20190121-b.png)
**Figure** Getting openrc file

Now you can add the environment variables by typing the following command into terminal:

```bash
source <project_name_here>-openrc.sh
```

You will be asked to type in a password. Use the password for your CSC account. Note that using Haka credentials with the command-line interface is not yet supported. After doing this, the current terminal session will have the proper environment variables for using the command-line tools. **Note:** You will need to do this again if you open a new terminal.

Now you are able to use the [Swift client](./using_allas/swift_client.md){:target="_blank"}.


**About S3:**
 
For S3 use cases, you can also store the ec2 credentials with the job, which is the recommended way of accessing objects from a compute job. When you do not need the credentials anymore you can delete them with:
```bash 
$ openstack credential delete
```
**Please note:** The ec2 credentials do not work against other OpenStack services.
 
There is also the possibility to create [Temp URLs](./using_allas/common_use_cases.md#sharing-data){:target="_blank"} for the objects you need to access and you can use those URLs to access the data from compute jobs. One benefit of using Temp URLs is that no credentials need to be stored for retrieving the object.

&nbsp;


## Accessing Allas from Web

OpenStack Horizon web interface provides easy-to-use basic functions for data management in Allas:

[Web client - OpenStack Horizon Dashboard](./using_allas/web_client.md){:target="_blank"}

&nbsp;


## Protocols


The object storage service is provided over two different protocols, _Swift_ and _S3_. From user perspective one of the main differences between S3 and Swift is in the authentication. Token based Swift authentication, used in Allas, remains valid for three hours at a time but in the key based S3 the connection can be permanently open. The permanent connection of S3 is handy in many ways, but it includes a security aspect too: if your server where you use Allas is compromised, the object storage space will be compromised too.

Because of this security concern, Swift is the recommended protocol to be used in many-user servers like Mahti and Puhti. Thus, for example, the CSC specific <i>a_ commands</i> (e.g. _a_put_ and _a_get_) as well as the standard _rclone_ configuration in Puhti are based on Swift. However, in some cases the permanent connections provided by S3 protocol may be the most reasonable option, for example, in users own virtual machine running in cPouta.

Swift and S3 protocols are <u>not</u> compatible in handling objects. Small objects, that do not need to be splitted during upload, can be cross used, but splitted objects can be used only with the protocol that was used for upload. The size limit for splitting an object depends on the settings and on the protocol. The limit is typically between 500 MB and 5 GB.

Below is a quick list of generic recommendations for selecting the protocol.
 
 * If you have a choice, use the _Swift_ protocol, it is better supported.
 * In any case, settle on one protocol. Do not mix _S3_ and _Swift_.
 * It is better to store a few large objects than a lot of small objects.

There are several different ways of accessing object storage. We support both the _Swift_ and _S3_ protocols to manage the data. Below is just a short list of tools. There are more.

| Client | Usable | Chapter | Notes |
| :-------- | :-------: | :--------: | :------- |
| web client | Yes | [Link](./using_allas/web_client.md){:target="_blank"} | Use via [https://pouta.csc.fi](https://pouta.csc.fi){:target="_blank"}. Provides basic functions. |
| a_commands | Yes | [Link](./using_allas/a_commands.md){:target="_blank"} | Provides easy-to-use tools for basic usage. Assumes data is already in CSC computing environment. Requires Swift and OpenStack. |
| python-swiftclient | Yes | [Link](./using_allas/swift_client.md){:target="_blank"}| This is the recommended Swift client. |
| s3cmd	| Yes | [Link](./using_allas/s3_client.md){:target="_blank"} | This is the recommended S3 client. Use version 2.0.2 or later. |
| python-swift-library | Yes | [Link](./using_allas/python_library.md){:target="_blank"} |	| 
| rclone | Yes | [Link](./using_allas/rclone.md){:target="_blank"} | Useful with Supercomputers. |
| libs3	| Yes | | |	 	 
| python-openstackclient | Yes | | |
|aws-cli | Yes | | aws-cli and the boto3 python library. |
|curl | Yes | | Extremely simple to use with public objects and temporary URLs. |
|wget | Yes | | Same as curl. |


Below is a rough table summarizing the available operations with four of the clients. Web client suits well for a basic user who manages with the simple basic functions. The a_commands offer easy-to-use functions for a basic user using Allas either from own computer or from supercomputer. Power users might want to consider the clients Swift and s3cmd. The table shows only the most central functions of the power clients concerning data management in Allas, but there are more.


| | &nbsp;&nbsp;&nbsp; web client | &nbsp;&nbsp;&nbsp; a_commands | &nbsp;&nbsp;&nbsp;&nbsp; swift &nbsp;| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; s3cmd &nbsp;|
| :----- | :-----: | :----: | :-----: | :----: |
| Usage | _Basic_ | _Basic_ | _Power_ | _Power_ |
| **Create buckets** | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> |
| **Upload objects** | <font color="green">&#x2714;</font>&#8226; | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> |
| **List** | | | | |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; objects | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; buckets | <font color="green">&#x2714;</font>  | <font color="green">&#x2714;</font>  | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font>  |
| **Download** | | | | |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; objects | <font color="green">&#x2714;</font>&#8226; | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; buckets | | | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> |
| **Remove** | | | | |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; objects | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; buckets | <font color="green">&#x2714;</font>&#8226;&#8226; | <font color="green">&#x2714;</font>&#8226;&#8226; | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font>&#8226;&#8226; |
| **Managing access rights** | | | | |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; public/private | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; read/write access</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; to another project | | | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; temp URLs | | | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> |
| **Move objects** | | | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> |
| **Edit metadata** | | | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> |
| **Upload large files** (over 5 GB) | | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> | <font color="green">&#x2714;</font> |
| **Download whole project** | | | <font color="green">&#x2714;</font> | |
| **Remove whole project** | | | <font color="green">&#x2714;</font> | |




<div align="right">&#8226; Only one object at a time</div>
<div align="right">&#8226;&#8226; Only empty buckets</div>







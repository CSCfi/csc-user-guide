
# Accessing Allas

&nbsp;


## Getting Access to Allas

Usage of Allas is based on CSC customer projects. To be able to use Allas you need to be a member in 
a CSC project that has permission to use Allas. If you don't have a CSC account, you must first register as CSC user
and join or start a computing project for which Allas has been enabled. All these steps can be done in the
MyCSC user portal: [https://my.csc.fi]( https://my.csc.fi){:target="_blank"}

The following guidelines describe step by step how to establish Allas with different operating systems.

&nbsp;


## Accessing Allas using

<font color="red">v---------------Still-in-progress---------------v</font>
### Windows and Mac

With Windows and Mac you can use, for example, the software [CyberDuck](https://cyberduck.io/){:target="_blank"}.

1. Install **CyberDuck**

2. Navigate to the CyberDuck mainmenu and choose **Bookmark | New Bookmark** (_Ctrl-Shift-B_).

3. In the first drop-down menu, choose _Swift (OpenStack Object Storage)_

4. As **Server** type _pouta.csc.fi_ and choose **Port** 5001

5. In the section **Tenant ID:Access Key** type your _Pouta username_ (the one you use in pouta.csc.fi)

6. Type your Pouta password in **Secret Key** part. After that, you can close the bookmark by clicking X on the upper right corner of the pop-up window

7. Now you can right-click the bookmark on the CyberDuck mainpage and choose the option _Connect to server_.

8. Type your _project's name_ in the **Tenant Name** section (for example project_2001234) and **Login**

9. Now you should be able to see the content of your project (which might be empty)

CyberDuck offers some basic functionalities to managing data in object storage:

 * Upload objects
 * Edit objects
 * Edit metadata
 * Share buckets
 * Remove object


### Linux

Get Openstack RC-file:

 * **Access & Security | API Access**

 * Edit the OpenStack password to the lowest line.

Now you can use the _Swift_ client.

### Android

With Android you can use the _Android Access_ with _OpenStack Swift_. Alternatively, you can also use the _Remote Desktop_.

 * OpenStack Swift
    * Android Access
 * Remote Desktop

### Web

 * Web client - OpenStack Horizon Dashboard

<font color="red">^---------------Still-in-progress---------------^</font>
&nbsp;

&nbsp;


## Accessing Allas from Supercomputers

The usage will strongly depend on what you will do with the data. The command-line tools _Swift_, _S3_ and _s3cmd_ are already installed on Supercomputers (**Taito**, **Puhti** and **Mahti**). More about the clients in [the next chapter](#protocols).

| Command-line tool | Requirements |
| :--------: | --------- |
| Swift	| Computing project openrc.sh file downloaded from [https://pouta.csc.fi](https://pouta.csc.fi){:target="_blank"} & sourced to shell (more info [here](./using_allas/swift_client.md){:target="_blank"}) |
| <br/><br/><br/>S3 | Following environment variables present in environment: <br/><br/> S3_ACCESS_KEY_ID <br/> S3_SECRET_ACCESS_KEY <br/> S3_HOSTNAME <br/><br/> More info [here](./using_allas/s3_client.md){:target="_blank"}. |
| s3cmd	| Configuration file .s3cfg populated (more info [here](./using_allas/s3_client.md){:target="_blank"}) |
 

You can use any of the commands to stage in the data you need to process to the project/scratch disk and process the data like you would process any other data.
 
For S3 use cases, you can also store the ec2 credentials with the job. This is the recommended way of accessing objects from a compute job. When you do not need the credentials anymore you can delete them with:
```bash 
$ openstack credential delete
```
**Please note!** The ec2 credentials do not work against other Openstack services.
 
There is also the possibility to create [temp URLs](./using_allas/swift_client.md#temp_urls){:target="_blank"} for the objects you need to access, and use those URLs to access the data from compute jobs. One benefit of using temp URLs is that no credentials need to be stored for retrieving the object.

The instructions for using Allas with Supercomputers can be found from [the Use Cases](./using_allas/common_use_cases.md#using-allas-in-supercomputers){:target="_blank"}

&nbsp;


## Protocols


The object storage service is provided over two different protocols, **Swift** and **S3**. From user perspective one of the main differences between S3 and Swift is in the authentication. Token based Swift authentication, used in Allas, remains valid for three hours at a time but in the key based S3 the connection can be permanently open. The permanent connection of S3 is handy in many ways, but it includes a security aspect too: if your server where you use Allas is compromised, the object storage space will be compromised too.

Because of this security concern, Swift is the recommended protocol to be used in many-user servers like Puhti and Mahti. Thus, for example, the CSC specific <i>a_ commands</i> (e.g. _a_put_ and _a_get_) as well as the standard _rclone_ configuration in Puhti are based on Swift. However, in some cases the permanent connections provided by S3 protocol may be the most reasonable option, for example, in users own virtual machine running in cPouta.

Swift and S3 protocols are <u>not</u> compatible in handling objects. Small objects, that don't need to be splitted during upload, can be cross used, but a splitted object can be used only with the protocol that was used for upload. The size limit for splitting an object depends on the settings and on the protocol. The limit is typically between 500 MB and 5 GB.

Data uploaded using one protocol is visible with the other protocol. Each protocol has several different tools you can use. Here is a quick list of generic recommendations.
 
 * If you have a choice, use the _Swift_ protocol, it is better supported.
 * In any case, settle on one protocol. Do not mix _S3_ and _Swift_.
 * Do not use uppercase characters or Scandic letters (&auml;, &ouml;, etc.) in the names of buckets.
 * It is better to store a few large objects than a lot of small objects.

There are several different ways of accessing object storage. We support both the _Swift_ and _S3_ protocols to manage the data. Below is just a short list of tools. There are more.

| Client | Usable | Chapter | Notes |
| :-------- | :-------: | :--------: | :------- |
| Web client | Yes | [Link](./using_allas/web_client.md){:target="_blank"} | Use via [https://pouta.csc.fi](https://pouta.csc.fi){:target="_blank"} |
| python-swiftclient | Yes | [Link](./using_allas/swift_client.md){:target="_blank"}| This is the recommended Swift client |
| s3cmd	| Yes | [Link](./using_allas/s3_client.md){:target="_blank"} | This is the recommended S3 client. Use version 2.0.2 or later|
| python-swift-library | Yes | [Link](./using_allas/python_library.md){:target="_blank"} |	| 
| a_commands | Yes | [Link](./using_allas/a_commands.md){:target="_blank"} | Provides easy-to-use tools for basic usage. Requires Swift and OpentStack |
| rclone | Yes | [Link](./using_allas/rclone.md){:target="_blank"} | Useful with Supercomputers |
| libs3	| Yes | | |	 	 
| python-openstackclient | Yes | | |
|aws-cli | Yes | | aws-cli and the boto3 python library |
|curl | Yes | | Extremely simple to use with public objects and temporary URLs |
|wget | Yes | | Same as curl |

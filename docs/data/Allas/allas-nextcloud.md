# Using Nextcloud as front end for Allas storage system

Motivation: Allas is a general purpose storage system for research data. 
It can be used with tools based on Swift and S3 protocols. However, in many cases, 
using Allas directly trough S3 or Swift is limited by the rather plain structure 
of user management and by the fact that the access is based on personal CSC user accounts.

Using Nextcloud server as a front end allows you to create and manage your own user 
base for your Allas storage area and control the access to different datasets and storage areas. 
Further, Nextcloud provides several user interfaces (including a WWW-interface and a cell phone app) 
that are often easier to use and more flexible to use that native Swift or S3 applications.

In this document we show a simple use case with the following steps:

   1. Launch a new Ubuntu18 Virtual Machine
   2. Install a Nextcloud server into the new VM
   3. Link The Nextcloud server is linked to a data bucket in Allas
   4. New Nextcloud user account is created for an external user

## 1. Launch a new Ubuntu18 Virtual Machine

First, launch a new Ubuntu18 based server in cPouta service. 
See instructions in the [cPouta documentation](../../../cloud/pouta/) and
in [tutorial video](https://www.youtube.com/watch?v=CvoN4pv0RJQ).

In most cases the combination of “standard small” flavor and Ubuntu18.04 image is sufficient.

When you create the security group for the VM, the instructions above show how 
port 22 is opened for ssh access. In this case, use the same procedure to open 
port 443 (https), too, as it will be used to access the Nextcloud server.


## 2. Setting up a Next Cloud sever in the VM

Open a terminal connection to your server (ssh or Putty) to install the Nextcloud server.
First, it is good to update the Ubuntu system:

```bash
sudo apt-get update
```
In this example we use _snap_ as it provides an easy way to install Nextcloud.
You can do the installations with just few commands.

First do the next-cloud installation with command:
```bash
sudo snap install nextcloud
```
Then, Nextcloud administration account is created. In the command below the account name is
defined to be _ncadmin_ with password _1Hu9kgFsN_.
```bash
sudo nextcloud.manual-install ncadmin 1Hu9kgFsN
```
Next you need to enable https with self signed certificate. Self signed certificates are sufficient for testing, but 
for production you should use real certificates (e.g. lets-encrypt instead of self-signed).
```bash
sudo nextcloud.enable-https self-signed
```

As a last step. add the IP-address of your Nextcloud server to the list of trusted domains. The IP-address is the Floating IP address 
that you assigned for the VM and that you used to open the terminal connection. 
For example the case of IP:86.50.252.77 the definition could be done with command:
```bash
sudo nextcloud.occ config:system:set trusted_domains 1 --value=86.50.252.77
```

Now you should be able to connect your Nextcoud server running in _https://ip-of-your-VM_

So in this example: _https://86.50.252.77_


If the connection web interface fails check that:

*   you are using the right protocol and ip address
*   port number 443 and your local IP address (not the server IP) is defined in the cPouta security group and that this security group is in use
*   your browser accepts self-signed certificates
 

Nextcloud software is modular, it can be extended with Nextcloud Apps. Once you have the
Nextcloud up and running, it is a good practice to check what Apps are enabled and how
different features are configured to work. You can do this in the Nextcloud user interface
when you are logging in as admin. If you wish, you can also start this by running a CSC
provided script that disables a few and configures some Apps in order to make the Nextcloud
less overloaded with features for this kind of Allas front end testing. The script can be
downloaded and run like this:

```bash
curl https://raw.githubusercontent.com/CSCfi/allas-cli-utils/master/nextcloud_snap/clean_nextcloud_snap >clean_nextcloud_snap
chmod +x clean_nextcloud_snap
./clean_nextcloud_snap
```


## 3. Link Nextcloud to a bucket in Allas

To be able to link Allas to your Nextcloud server, you must have a valid S3 key pair and a ready made data bucket in Allas. The bucket can be empty or it can already contain some data objects.

You can do this things for example in puhti.csc.fi with commands:

### 1. Setting up the connection:

```bash
module load allas
allas-conf --mode s3cmd
```

### 2. Creating a new empty bucket

```bash
s3cmd mb s3://your-proj-num-nextcloud
```
In this example we are using project 2001234 so
the bucket name could be:

```text
2001234-nextcloud
```

### 3. Printing out the keys

```bash
grep key $HOME/.s3cfg
```

Now return to the Nextcloud WWW-interface and log in as the admin. 
Click the round symbol on the right end of the blue menu bar and select _+Apps_ from the pop-up menu.

From the appearing application list enable _External storage support_. 

Then click the round symbol again and open _settings_ .

In the settings panel on the left side, scroll to the Administration section add select: _External storages_ .

Open the _Add storage_ menu and select : _Amazon S3_

This opens a definition menu here you need to file following parameters: 

*   Folder name: display name for the allas bucket (2001234-nextcloud)
*   Bucket: The bucket you just created  or some older bucket.
*   Host:a3s.fi
*   Port: 443
*   Region: US
*   Enable SSL
*   Access key: from the output of the grep command above
*   Secret key: from the output of the grep command above

Then go to the _External storages_ in your _Personal_ settings and click the line containing 
the external folder name just created to ensure that the storage works.

If you now move to the _Files_ tool in the main menu (blue bar on the top), 
you should see an new external storage folder named as defined above.

Now you can click this folder and start uploading and downloading data 
from and to this Allas bucket using the Nextcloud interface.

## 4. Create new Nextcloud user account for an external user

The Nextcloud admin account can create new users and user groups to the Nextcloud server. 
Click the round symbol on the right end of the blue menu bar and select _Users_ from the pop-up menu.

First we create a new user group by clicking _Add group_. Here we name the group as “users” 
and confirm the creation request by typing the password of Nextcloud admin.

Then a new user is created by  clicking _add user_ 
User name and password needs to be defined for the user and the 
new account is added to group _Users_.

Finally, we need to allow this new user to access the  _External storage_ (the bucket from Allas). 
To do that, go back to the Settings view and reopen the _External storages_ settings from the Administration tools. 

Now in the “Available for” column, click the definition field. This lists the users and user groups. 
Choose either the user or user group to allow the new user to access the Allas bucket. You can define both 
read and write permissions or you can also give just read-only access to a user or user group. 
These options are set with the menu that opens from the three dots next to the definition field.


## 5. Using Nextcloud

Once a new next cloud account is created, you can send the account information to the new user and he/she will be able to use Nextcloud 
to upload and download data to the data bucket that was linked to the Nextcloud server. Note, that this 
user doesn't need to have CSC account, a Nextcloud account is enough. I addition to the web interfaces, Nextcloud can be used by [desktop tools](https://nextcloud.com/install/) and [phone apps](https://apps.nextcloud.com/). 

Comman line usage is possible too. This can be utilized for example in cases there data download or upload needs to be automatized. Below is a sample where data is uploaded and download using `curl` command and _application password_. In this case the NextCould admin has created a user named as _ncuser1_ for this purpose. First the _ncuser1_ logs is to the next cloud server. The user opens *Settings* menu and there moves to *Security* settings.

In security section section *Devices & Sessions*, an application password is created by clicking button: *Create a new app password*. Note that you have to copy and save the application password, that was just generated, as you can't check it later on. 

In addition to user name and application password the user needs to know the IP address or server name to access the service. 
With this information available, data can be downloaded from Nextcould using curl command syntax:
```bash
curl -k -u username:app-password "https://server-ip/remote.php/webdav/nextcloudirectiory/file-name"
```

And upload can be done using syntax:
```bash
curl -k -u username:app-password -T file-to-upload "https://server-ip/remote.php/webdav/nextcloudirectiory/file-name"
```

In the commands above option `-k` is needed when the Nextcould server uses self signed certificates.

In this example the app password that user _ncuser1_  generated is: _Q34EN-Ni7pH-9oSes-ZQsF7-NdkYi_
and the IP address of the NectCloud server is 123.456.768.910. Earlier the the Nextcloud admin had linked Allas bucket _2001234-nextcloud_
to the next cloud service.

Now the _ncuser1_ is able to upload a file _image1.jpg_ to Allas bucket _2001234-nextcloud_ with command:

```bash
curl -k -u ncuser1:Q34EN-Ni7pH-9oSes-ZQsF7-NdkYi -T ./image1.jpg "https://123.456.768.910/remote.php/webdav/2001234-nextcloud/image1.jpg"
```

The same file can be downloaded with command:

```bash
curl -k -u ncuser1:Q34EN-Ni7pH-9oSes-ZQsF7-NdkYi "https://123.456.768.910/remote.php/webdav/2001234-nextcloud/image1.jpg" > image1.jpg
```

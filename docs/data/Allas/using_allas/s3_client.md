-------------------

## S3 client

To utilize the S3 API, ec2 credentials are required. These are created from the CLI with:
```bash
$ openstack ec2 credentials create
+----------------------------------+----------------------------------+----------------------------------+----------+
| Access                           | Secret                           | Project ID                       | User ID  |
+----------------------------------+----------------------------------+----------------------------------+----------+
| 00000000001                      | 5000000000000000000              | 000000000000000000022            | $username|
+----------------------------------+----------------------------------+----------------------------------+----------+
```
Instructions for installing s3cmd, making objects public with it and giving read access to a bucket for another project are listed below.

&nbsp;

* **s3cmd**

Please refer to [http://s3tools.org/download](http://s3tools.org/download){:target="_blank"} and  [http://s3tools.org/usage](http://s3tools.org/usage){:target="_blank"} for upstream documentation.
 
Fedora/RHEL derivatives:
```bash
$ sudo yum install s3cmd
```
Debian derivatives:
```bash
$ sudo apt install s3cmd
```
OSX:
```bash
$ python3 virtualenv
$ pip3 install s3cmd
$ s3cmd
```
You need to use ec2 credentials when using S3. You can create S3 credentials by sourcing your openrc file as in the instructions in Pouta documentation's [chapter 3.4.1.3](https://research.csc.fi/pouta-install-client){:target="_blank"}.
 
If you already have created ec2 credentials that you want to reuse, you can find them by issuing:
```bash
openstack ec2 credentials list
```
Once you have your ec2 credentials you will need to use the Access and Secret in the next command. The interactive command "s3cmd --configure" is good for first-time use. It creates a $HOME/.s3cfg file, adds access keys and ids from above, points to pouta object store and adds an encryption key. It is probably a good idea to create a password when you get to the option. 
 
Alternatively, you can create a working file by adding your Access and Secret to the following oneliner:
```bash
$ s3cmd --configure --access_key=YOUR_EC_ACCESS_KEY_HERE --secret_key=YOUR_EC_SECRET_KEY_HERE --host=object.pouta.csc.fi --region=US --host-bucket='%(bucket)s.object.pouta.csc.fi'
```
Then you need to verify all the settings from the created file.

&nbsp;

<a name="s3cmd_public_objects"></a>

* **s3cmd and public objects**

<pre>$ s3cmd put pictures/salmon.jpg s3://fishes/pictures/fishes.jpg -P
Public URL of the object is: http://object.pouta.csc.fi/fishes/pictures/salmon.jpg</pre>

**Note** that the above client outputs an URL which has http:// (which is not open in the object storage firewall). A URL like this needs to be manually changed to https if such a client is used.

&nbsp;

* **Giving another project read access to a bucket**

"_s3cmd setacl_" command needs to use the UUID of the project you want to grant access to.
 
The ID can be found at <a href="https://pouta.csc.fi/dashboard/identity/" target="_blank">https://pouta.csc.fi/dashboard/identity/</a> or with "_openstack project show $project_name_". You need access (membership) to the project to find out the UUID.
 
In the Pouta Web UI you only see buckets that members of your project have created. If your project has been granted project read access to a bucket with the s3cmd client, the following applies to other members of your project:
 
 * Can list and fetch files with the python-swiftclient 
 * "_swift list_" does <u>not</u> display the bucket
 * "_s3cmd ls_" does display the bucket.
 
Granting read access:
```bash
$ s3cmd setacl --acl-grant=read:$other_project_uuid s3://fishes
```
Revoking read access:
```bash
$ s3cmd setacl --acl-revoke=read:$other_project_uuid s3://fishes
```
View permissions:
```bash
$ s3cmd info s3://fishes|grep -i acl
   ACL:       other_project_uuid: READ
   ACL:       my_project_uuid: FULL_CONTROL
```

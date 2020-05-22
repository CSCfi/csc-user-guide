#How can I mount my Pouta Object Storage bucket to a VM running in cPouta

Combining cPouta cloud environment and Allas storage environment allows you to build scalable data management environments. This document shows one example how you can combine these two services by mounting a bucket from Allas to an Ubuntu 16.04 or Centos7 based virtual machine running in cPouta.

[TOC]

##Installing OpenStack, s3cmd and s3fs in Ubuntu 16.04

After launching an Ubuntu 16.04 based virtual machine in cPouta, open a terminal connection to the VM and  update it with command:

```
sudo apt-get update
```

Then install OpenStack client with commands:

```
sudo apt install python-pip python-dev
sudo apt-get install python-setuptools
sudo pip install python-openstackclient
```

Next, add  **s3cmd** and **s3fs** commands to your VM.

```
sudo apt-get install s3cmd
sudo apt-get install s3fs
```

##Installing OpenStack, s3cmd and s3fs in Centos7

After launching an Centos7 based virtual machine in cPouta, open a terminal connection to the VM and  update it with command:

    sudo yum update

OpenStack and s3cmd can then be installed with commands:

```
sudo yum install python-pip python-devel wget
sudo pip install python-openstackclient
`sudo pip install --upgrade --requirement https://raw.githubusercontent.com/platform9/support-locker/master/openstack-clients/requirements.txt --constraint https://raw.githubusercontent.com/openstack/requirements/stable/pike/upper-constraints.txt`
sudo yum install s3cmd
```

In the case of Centos7, s3fs needs to be compiled locally. To do this we need to first to intall some tools needed for compilation:

    sudo yum install automake fuse fuse-devel gcc-c++ git libcurl-devel libxml2-devel make openssl-devel

The download the s3fs-fuse from the git repository and install it:

```
git clone https://github.com/s3fs-fuse/s3fs-fuse.git
cd s3fs-fuse/
./autogen.sh
./configure
make
make  all-recursive
sudo make install
```

##Configuring and using Allas (Ubuntu and Centos)

Once you have, openstack, s3cmd and s3fs installed, download and execute the **poutaos_configure** tool to configure _s3cmd_ so that it uses your cPouta project. You can also use this tool also to switch between different Allas projects 
if you have several of them.

```
wget https://a3s.fi/tools/poutaos_configure
chmod u+x poutaos_configure
./poutaos_configure
```

The _poutaos_configure_ command asks first your CSC password. Then it lists your Allas projects and asks you to define the name of the project to be used. During the proceeding configuration steps, the system asks you about the values that will be used for the Allas connection. In most cases you can just accept the proposed default values, but there is two exceptions:  

   1. It is recommended that you define a password that is used to encrypt the data traffic to and from Object Storage server.
   2. As the last question the configuration process asks if the configuration is saved. The default is "no" but you should 
      answer y (yes) so that configuration information is stored to file _$HOME/.s3cfg_.  
      This configuration needs to be defined only once. In the future _s3cmd_ will use this 
      Object Storage connection described in the _.s3cfg_ file automatically.

After this you can use the storage area of your Allas project with _s3cmd_ command.

Lets, assume you already have a bucket called _case_1_ in your object storage and that you have some data objects (I.e files) in this bucket. Now you can see, download and upload files in this bucket with _s3cmd_

```
s3cmd ls s3://case_1
s3cmd get s3://case_1/file1.txt
s3cmd put file2.txt s3://case_1/
```

This is normally the recommended way if you wish to use Allas with S3 protocol. However, it is also possible to mount the bucket to your VM so that it is shown as  "mounted disk".

To do this, create first an empty directory to be used as a mount point. E.g.

```
mkdir os_case_1
```

Then check the UID if the user account you are using (normally it is 1000 for cloud-user)

```
id -u $(whoami)
```

then use _s3fs_ command to mount the bucket.

```
s3fs case_1 os_case_1 -o passwd_file=~/.passwd-s3fs -o url=https://a3s.fi/ -o use_path_request_style -o umask=0333,uid=1000
```

And after this you should be able to see the objects of the mounted bucket as files. Try for example command:

```
ls -l os_case_1
```

The mounting command above uses a project specific keypair that the _poutaos_configure_ command previously stored to file _.passwd-s3fs_. The uid value 1000 refers to the _cloud-user_ account and should be changed if some other user account is used.

The _umask_ value defines the read, write and execution permissions for the mounted directory. In the sample command above the bucket is mounted in read-only mode (umask=0333). In many cases this might be reasonable, because modifying the files directly in object storage is not efficient. If a file needs to be constantly modified it is better to make a local copy of it and upload only the final version of the file back to the bucket. However, if needed you can re-mount the bucket with more permissive _umask_ value. E.g.

```
sudo umount os_case_1
s3fs case_1 os_case_1 -o passwd_file=~/.passwd-s3fs -o url=https://a3s.fi/ -o use_path_request_style -o umask=0027,uid=1000
```

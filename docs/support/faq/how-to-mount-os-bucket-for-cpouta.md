# How can I mount my Allas S3 bucket to a VM running in cPouta

Combining cPouta cloud environment and Allas storage environment allows you to build scalable data management environments. This document shows one example how you can combine these two services by mounting a bucket from Allas to an Ubuntu or a Centos7 based virtual machine running in cPouta.

[TOC]

## Installing OpenStack, s3cmd and s3fs

### In Ubuntu

* After launching an Ubuntu based virtual machine in cPouta, open a terminal connection to the VM and update it with the command:

	```sh
	sudo apt update
	```

!!! warning
    Older versions of Ubuntu will have older and deprecated versions of python. It is recommended to use the latest Ubuntu version available in Pouta.

* Then install OpenStack client by:

	```sh
	sudo apt install python3-pip python3-dev python3-setuptools
	sudo pip install --upgrade pip
	sudo pip install python3-openstackclient
	```

* Next, install  **s3cmd** and **s3fs** commands to your VM.

	```sh
	sudo apt install s3cmd s3fs
	```

### In Centos7

* After launching a Centos7 based virtual machine in cPouta, open a terminal connection to the VM and update it with the command:

	```sh
	sudo yum update
	```

* OpenStack and s3cmd can then be installed by:

	```sh
	sudo yum install python-pip python-devel wget
	sudo pip install python-openstackclient
	sudo pip install --upgrade \
	    --requirement https://raw.githubusercontent.com/platform9/support-locker/master/openstack-clients/requirements.txt \
	    --constraint https://raw.githubusercontent.com/openstack/requirements/stable/pike/upper-constraints.txt
	sudo yum install s3cmd
	```

* In the case of Centos7, s3fs needs to be compiled locally. To do this we need to first to intall some tools needed for compilation:

	```sh
	sudo yum install automake fuse fuse-devel gcc-c++ git libcurl-devel libxml2-devel make openssl-devel
	```

* Then download the s3fs-fuse from the git repository and install it:

	```sh
	git clone https://github.com/s3fs-fuse/s3fs-fuse.git
	cd s3fs-fuse/
	./autogen.sh
	./configure
	make
	make  all-recursive
	sudo make install
	```

## Configuring and using Allas (in Ubuntu and Centos)

Once you have openstack, s3cmd and s3fs installed, download and execute the **poutaos_configure** tool to configure _s3cmd_ so that it uses your cPouta project. You can also use this tool to switch between different Allas projects 
if you have several of them.

```
wget https://a3s.fi/tools/poutaos_configure
chmod u+x poutaos_configure
./poutaos_configure
```

The _poutaos_configure_ command asks first your CSC password. Then it lists your Allas projects and asks you to for the project to be used. During the following configuration steps, the system asks you about the values that will be used for the Allas connection. In most cases you can just accept the proposed default values, but there are two exceptions:  

   1. It is recommended that you define a password that is used to encrypt the data traffic to and from Object Storage server.
   2. As the last question the configuration process asks if the configuration is saved. The default is "no" but you should 
      answer y (yes) so that configuration information is stored to file _$HOME/.s3cfg_.  
      This configuration needs to be defined only once. In the future _s3cmd_ will use this 
      Object Storage connection described in the _.s3cfg_ file automatically.

After this you can use the storage area of your Allas project with _s3cmd_ commands.

Now you can see, download and upload files in this bucket with _s3cmd_.

* List all your buckets:

```sh
s3cmd ls s3://
```

* Let's assume you already have a bucket called **case_1** in Allas and that you have some data objects (i.e. files) in this bucket.

```sh
s3cmd ls s3://case_1
s3cmd get s3://case_1/file1.txt
s3cmd put file2.txt s3://case_1/
```

This is the **recommended way** if you wish to use Allas with the S3 protocol. However, it is also possible to mount the bucket to your VM so that it is shown as  "mounted disk".

1. To do this, create first an empty directory to be used as a mount point. E.g.

	```sh
	mkdir os_case_1
	```

1. Then check the UID if the user account you are using (normally it is 1000 for the default user)

	```sh
	$ id -u
	1000
	```

1. Create a `.passwd-s3fs` file in your home directory. The format of the file must be: `ACCESS_KEY_ID:SECRET_ACCESS_KEY` and have 600 permissions.

	```sh
	$ openstack ec2 credentials list -f value | grep $OS_PROJECT_ID | tail -1 |\
	   awk '{print $1":"$2}' >.passwd-s3fs
	Password:
	$ chmod 600 .passwd-s3fs
	```

1. then use _s3fs_ command to mount the bucket.

	```sh
	s3fs case_1 os_case_1 -o passwd_file=~/.passwd-s3fs -o url=https://a3s.fi/ \
		-o use_path_request_style -o umask=0333,uid=1000
	```

	!!! info 
	    The uid value 1000 refers to the user id returned by `id -u`

	!!! info
	    The umask value `0333` mounts the files in read-only mode. If you want to be able to write to the files, use `0027` instead

1. And after this you should be able to see the objects of the mounted bucket as files. Try for example command:

	```sh
	ls -l os_case_1
	```

1. When you are done you can unmount the folder by:

        ```sh
	sudo umount os_case_1
	```

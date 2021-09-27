# Extending SD Desktop software environment with Singularity containers

In this tutorial we us cPouta to create a singularity conntainer that is used import missing software to SD Desktop.

## 1. Createning your own singularity workbenc to cPouta.

In order to utilize all features of singularity you must run it in an environment where you have adminstration level access rights. At CSC, you can have adminstrarot level access in virtual machines running in cPouta. Using cPouta for the building process adds a bit of extra steps into the process: you have to know how to launch and access virtual machines in cPouta. On the other hand cPouta has a fast connection to the Allas service that is used to import the ready made containers to SD Desktop.

As a first step launch virtual machine in cPouta as described in'cPouta user guide 
*  [Launching a virtual machine with the cPouta web interface](../../cloud/pouta/launch-vm-from-web-gui.md)

and for example these tutorial videos:

*  [Launching a virtual machine](https://www.youtube.com/watch?v=CvoN4pv0RJQ) and connecting to it on a local macOS laptop
*  [Creating a virtual machine in cPouta](https://www.youtube.com/watch?v=CIO8KRbgDoI) a webinar recording.

In this tutorial we use a virtual machine that was launched using:
*  Flavor: **Standard.medium**
*  Instance Boot Source: **Image**
*  Image Name: **Ubuntu-20.04 (2.2 GB)**


## 2. Installating singularity and Allas tools to Ubuntu 20.04 server

Here we start from a situation where we have logged in to our freshly started virtual machine for the first time. As preparatory steps we need to install to our virtual machine **singularity** to create new software containers and **allas tools** to upload the containers we will create to Allas.


The singularity installation is done with commands:

```text
sudo apt-get update
sudo apt-get install -y build-essential libssl-dev uuid-dev libgpgme11-dev\
squashfs-tools libseccomp-dev wget pkg-config git cryptsetup golang-go nano
wget https://github.com/sylabs/singularity/releases/download/v3.8.3/singularity-ce-3.8.3.tar.gz
tar -xzf singularity-ce-3.8.3.tar.gz
cd singularity-ce-3.8.3/
./mconfig
cd /home/ubuntu/singularity-ce-3.8.3/builddir
make
sudo make install
cd
```

After which Allas tools can be installed with:

```text
sudo apt install python3-pip python3-dev
sudo apt-get install python3-setuptools
sudo pip3 install python-openstackclient
sudo apt install python3-swiftclient
curl https://rclone.org/install.sh | sudo bash
git clone https://github.com/CSCfi/allas-cli-utils
cd 
```
Note that this installation process needs to be done only once for a virtual machine.


## 3. Creating a singularity sand box

### 3.1 Defaults file
There are many ways to create new Singularity containers. You can crate the a conntainer by creating a _sandbox_ in to which you log in and add contect by typing installation commands. Alternatively you can automatize the installation process so that you collect all the commands and settings to a _singularity definiton_ file that instucts the installation process.

Here we use a mixture of this two. We first use a simple definition file to create a new continer sandbox and then we and the actual software installations manually.

First open a new file called _ubuntu_with_inst_tools.def_ with command:

```text
nano ubuntu_with_inst_tools.def
```

And copy-paste to the new file the content from the sample definition file below:

```text
Bootstrap: library
From: ubuntu:20.04
Stage: build

%environment
export LC_ALL=C
export LC_NUMERIC=en_GB.UTF-8
export PATH="/opt/miniconda/bin:$PATH"

%help
Container based on unbuntu containing miniconda.

%runscript
# sample runscript: bamtools passing all arguments from cli: $@
# exec /opt/miniconda/bin/bamtools "$@"

%post
#commands needed to build minicvonda
apt update
apt install -y wget bzip2 git autoconf automake build-essential zlib1g-dev pkg-config

#install conda
cd /opt
rm -fr miniconda
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh  -O miniconda.sh
bash miniconda.sh -b -p /opt/miniconda
mkdir -p /opt/tools/bin
export PATH="/opt/tools/bin:/opt/miniconda/bin:$PATH"
```

## 3.2 Creating and using sandbox

Next we will use this definition file to create a new singularity sandbox

```text
sudo singularity build --sandbox sd_sandbox_1 ubuntu_with_inst_tools.def
```
When the sandbox is ready we open a shell session into it. Option _-w_ enables us to write to the sand box:

```text
sudo singularity shell -w sd_sandbox_1
```
Now we are inside the singularity sandbox and we can start installing software we need.
We have conda already available and it will provied a handy way to install many software tools.
For example, following commands install _bamtools_ and _samtools_. In the case of samtools we define 
a spcific version (1.1.3)

```text
conda install bamtools
conda install samtools=1.13
```
We could also use normal installation procedures in stead of conda. For example in stead of _conda install vcftools_
you could do vcftools installation with commands:

```text
cd /opt/tools
git clone https://github.com/vcftools/vcftools
cd vcftools/
autoreconf -i
./configure --prefix=/opt/tools
make
make install
```
When you are ready with the software installations you can exit the sanbox with command:
```text
exit
```
## 3.3 Creating a singularity image file

Now we are back in the base virtual machine. Next we convert the sandbox into a singularity image file with command:

```text
sudo singularity build sd_tools_1.sif sd_sandbox_1
```
After this, file listing (```ls -lh```) shows that out current diretory has a sandbox directory and singularity image file

```text
drwxr-xr-x. 18 root   root   4.0K Sep 27 12:56 sd_sandbox_1
-rwxr-xr-x   1 ubuntu ubuntu 419M Sep 27 13:43 sd_tools_1.sif
```




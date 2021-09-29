# Extending SD Desktop software environment with Singularity containers

In this tutorial we use cPouta to create a singularity containers to import new software to SD Desktop.

**Steps 1 ja 2** describe how to setup you own Virtual Machine with singularity environment to cPouta. This is 
not the only option and if you have already a sigularity installed elsewhere, you can skip these steps and 
use your own singularity enviroment.

**Step 3** describes one approach to how you can build your own software containers.

**Step 4** shows how a container is uploaded to Allas

## 1. Createning your own singularity workbench to cPouta.

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


## 3. Creating a singularity container

There are many ways to create new Singularity containers. You can crate the a conntainer by creating a _sandbox_ in to which you log in and add contect by typing installation commands. Alternatively you can automatize the installation process so that you collect all the commands and settings to a _singularity definiton_ file that instucts the installation process. A detailed view to the container building processes is provided by the [Singularity manual](https://sylabs.io/guides/3.8/user-guide/build_a_container.html)

Here we use a mixture of these two approaches. We first use a simple definition file to create a new continer sandbox that contains a set of tools for software installation. Then we open a shell session to the container sandbox and do the actual software installations manually.

### 3.1 Defaults file

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
#commands to help installation processes
apt update
apt install -y wget bzip2 git autoconf automake build-essential zlib1g-dev pkg-config nano

#install conda
cd /opt
rm -fr miniconda
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh  -O miniconda.sh
bash miniconda.sh -b -p /opt/miniconda
mkdir -p /opt/tools
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
Note that both the sandbox and singularity image file can be to execute the commands we just intalled. For example we can print out _bamtools_ help message with both commands below:

```text
singularity exec sd_sandbox_1 bamtools -h
singularity exec sd_tools_1.sif bamtools -h
```

## 4. Uploading container to Allas/SD Connect

In order to use the singulrity container in SD desktop, we need to upload it to Allas. As the container does not include any sensitive data, there is no need to encrypt it. Further from Allas the container can be downloaded to locations too. You can use a copy of the same container in other locations too. For example in Puhti and Mahti.

For the upload process we use the Allas tools we installed in step 2, were we installed Allas tools to directory _$HOME/allas-cli-utils_.
First we add this directory to command path:
```text
export PATH=${HOME}/allas-cli-utils:${PATH}
```
Next we open connetion to allas using the _allas_conf_ script. No that you must define your CSC user account
with _-u your-csc-account_ . Here we assume that the user account is _kkayttaj_.

```text
source ${HOME}/allas-cli-utils/allas_conf -u kkayttaj
```
The command above asks for the password of the CSC user account and then lists the Allas projects that the user account has available.
In this case we select the number that defines project _project_2000123_. After that the Allas connections to the selected project will remain active for the next eight hours.

Now we can access Allas with [a-tools](../../Allas/using_allas/a_commands.md) or [rclone](../../Allas/using_allas/rclone.md). 
Next we upload the container image we just created to Allas with command:

```text
a-put --nc sd_tools_1.sif -b 2000123_singularity -m "Contains bamtools, samtools and vcftools"
```
We don't want the compress the container, so we skip the compression with option _--nc_.  We store the container image to a bucket that contains the project number (2000123) to ensure uniquesnes. Otion _-m_ is used to add a small description to the metadata object that a-put creates.


## 5. Using singularity containers in SD Desktop

In order to use the singularity container you have created you need first donload a copy of the container to the SD Desktop. At the moment this is done with the _SD Connect downloader_ tool. First login to [SD Desktop](https://sd-desktop.csc.fi) and connect to the Virtual Desktop that you want to use. Open SD Connect downloader, navigate the to the right project (project_2000123) and bucket (2000123_singularity), and download the singularity image file (sd_tools_1.sif) to the SD Desktop.

After that open a Linux terminal in the SD Desktop. In the terminal, move the singularity file to the location you want to use it. In this example that could be done with command:
```text
mv SDCONNECTDATA/project_2000123/2000123_sigularity/sd_tools_1.sif ./
```
Now we could execute for example the samtools command that is installed in the container.

```text
singularity exec sd_tools_1.sif samtools --help
```
The command above prints out the help for samtools version 1.13 that is installed in the container.

When using the singularity container, you should note that it has its own file system that is read-only. 
By default Singularity bind mounts home diecrory (/home/$USER), /tmp, and current working directory ($PWD) 
into your container at runtime.

 

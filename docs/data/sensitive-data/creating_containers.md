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

There are many ways to create new Singularity containers. You can crate the a conntainer by creating a _sandbox_ in to which you log in and add contect by typing installation commands. Alternatively you can automatize the installation process so that you collect all the commands and settings to a _singularity definiton_ file that instucts the installation process.

Here we use a mixture of this two. We first use a simple definition file to create a new continer sandbox and then we and the actual software installations manually.

First open a new file called _ubuntu_with_conda.def_ with command:

```text
nano ubuntu_with_conda.def
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
apt install -y wget bzip2

#install conda
cd /opt
rm -fr miniconda
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh  -O miniconda.sh
bash miniconda.sh -b -p /opt/miniconda
export PATH="/opt/miniconda/bin:$PATH"
conda config --add channels defaults
conda config --add channels bioconda
conda config --add channels conda-forge
eval "$(/opt/miniconda/bin/conda  shell.bash hook)"
```
Next we will use this definition file to create a new singularity sandbox

```text
sudo singularity build --sandbox sd_sandbox_1 ubuntu_with_miniconda.def
```
When the sandbox is ready we open a shell session into it. Option _-w_ enabes us to write to the sand box:

```text
sudo singularity shell -w sd_sandbox_1
```
Now we are inside the singuleity sandbox we can start adding software.
We have conda already available and it will provied a handy way to install many software tools

Nyt voit alkaa asentamaan ohjelmia tähän konttiin. Esim.

conda install -c bioconda bamtools

Kun asennus on tehty poistu kontista komennolla:

exit


Nyt voit alkaa asentamaan ohjelmia tähän konttiin. Esim.

conda install -c bioconda bamtools

Kun asennus on tehty poistu kontista komennolla:

exit



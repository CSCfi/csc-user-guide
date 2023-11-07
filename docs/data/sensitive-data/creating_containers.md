# Extending SD Desktop software environment with your own Apptainer containers

In this tutorial we use cPouta to create Apptainer containers to import new software to SD Desktop.

**Steps 1 and 2** describe how to setup you own Virtual Machine with Apptainer environment to cPouta. This is 
not the only option and if you have already an Apptainer installed elsewhere, you can skip these steps and 
use your own Apptainer environment.

**Step 3** describes one approach to how you can build your own software containers.

**Step 4** shows how a container is uploaded to Allas.

**Step 5** describes how the software installed in a container can be used in SD Desktop.

## 1. Creating your own Apptainer workbench to cPouta

In order to utilize all features of Apptainer you must run it in an environment where you have administrator level access rights. At CSC, you can have administrator level access in virtual machines running in cPouta. Using cPouta for the building process adds a bit of extra steps into the process: you have to know how to launch and access virtual machines in cPouta. On the other hand cPouta has a fast connection to the Allas service that is used to import the ready-made containers to SD Desktop.

As a first step, launch a virtual machine in cPouta, as described in the cPouta user guide:

*  [Launching a virtual machine with the cPouta web interface](../../cloud/pouta/launch-vm-from-web-gui.md)

and for example these tutorial videos:

*  [Launching a virtual machine](https://www.youtube.com/watch?v=CvoN4pv0RJQ) and connecting to it on a local macOS laptop
*  [Creating a virtual machine in cPouta](https://www.youtube.com/watch?v=CIO8KRbgDoI) a webinar recording.

In this tutorial we use a virtual machine that was launched using:

*  Flavor: **Standard.medium**
*  Instance Boot Source: **Image**
*  Image Name: **Ubuntu-22.04**


## 2. Installing singularity and Allas tools to Ubuntu 22.04 server

Here we start from a situation where we have logged in to our freshly started virtual machine for the first time. As preparatory steps we need to install to our virtual machine **Apptainer** to create new software containers and **allas-tools** to upload the containers we will create to Allas.


The singularity installation is done with commands:

```text
sudo apt update
sudo apt install -y software-properties-common
sudo apt-get install apt-utils
sudo add-apt-repository -y ppa:apptainer/ppa
sudo apt update
sudo apt install -y apptainer
```

After which Allas tools can be installed with:

```text
sudo apt install python3-pip python3-dev
sudo apt-get install python3-setuptools
sudo pip3 install python-openstackclient
sudo apt install python3-swiftclient
curl https://rclone.org/install.sh | sudo bash
git clone https://github.com/CSCfi/allas-cli-utils
```

Note that this installation process needs to be done only once for a virtual machine.

## 3. Creating an Apptainer container

There are many ways to create new Apptainer containers. You can crate a container by creating a _sandbox_ in to which you log in and add content by typing installation commands. Alternatively you can automatize the installation process so that you collect all the commands and settings to an Apptainer _definition file_ that instructs the installation process. A detailed view to the container building can be found from the [Apptainer user guide](https://apptainer.org/docs/user/main/build_a_container.html).

Here we use a mixture of these two approaches. We first use a simple definition file to create a new container sandbox that contains a set of tools for software installation. Then we open a shell session to the container sandbox and do the actual software installations manually.

### 3.1 Definition file

First open a new file called `ubuntu_with_inst_tools.def` with command:

```text
nano ubuntu_with_inst_tools.def
```

And copy-paste to the new file the content from the sample definition file below:

```text
Bootstrap: docker
From: ubuntu:20.04
Stage: build

%environment
export TZ=Europe/Helsinki
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
ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
apt update
apt install -y wget bzip2 git autoconf automake build-essential 
apt install -y zlib1g-dev pkg-config nano

#install conda
cd /opt
rm -fr miniconda
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh  -O miniconda.sh
bash miniconda.sh -b -p /opt/miniconda
mkdir -p /opt/tools
export PATH="/opt/tools/bin:/opt/miniconda/bin:$PATH"
conda config --add channels bioconda
conda config --add channels conda-forge
conda config --set channel_priority strict
```

### 3.2 Creating and using sandbox

Next we will use this definition file to create a new Apptainer sandbox

```text
sudo apptainer build --sandbox sd_sandbox_1 ubuntu_with_inst_tools.def
```

When the sandbox is ready we open a shell session into it. Option `-w` enables us to write to the sandbox:

```text
sudo apptainer shell -w sd_sandbox_1
```

Now we are inside the Apptainer sandbox, and we can start installing the software we need.
We have already Conda available that will provide a handy way to install many software tools.
For example, following commands install _bamtools_ into Conda environment called _biotools_. 

```text
conda init bash
bash
conda create -n biotools
conda activate biotools
conda install bamtools
```

We could also use normal installation procedures instead of Conda. For example instead of `conda install vcftools`
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

New version of samtools could be installed with command:

```text
apt install samtools
```

Pip can be used to add Python modules:

```text
pip install pyhdfe
```

When you are ready with the software installations you can exit the sandbox with command:

```text
exit
```

Note: If you have launched a bash session for Conda installations, you will need to give two exit commands

### 3.3 Creating an Apptainer image file

Now we are back in the base virtual machine. Next we convert the sandbox into an Apptainer image file with command:

```text
sudo apptainer build sd_tools_1.sif sd_sandbox_1
```

After this, file listing (`ls -lh`) shows that the current directory has a sandbox directory and an Apptainer image file

```text
drwxr-xr-x. 18 root   root   4.0K Sep 27 12:56 sd_sandbox_1
-rwxr-xr-x   1 ubuntu ubuntu 419M Sep 27 13:43 sd_tools_1.sif
```

Note that both the sandbox and Apptainer image file can be used to execute the commands we just installed. For example, we can print out _samtools_ help message with both commands below:

```text
apptainer exec sd_sandbox_1 samtools 
apptainer exec sd_tools_1.sif samtools
```

## 4. Uploading container to Allas/SD Connect

In order to use the Apptainer container in SD desktop, we need to encrypt it with CSC public key and upload it to Allas. If you want to use the same container in other locations too, for example in Puhti and Mahti, you will need to upload another, non-encrypted version to Allas.

For the upload process we use the Allas tools we installed in step 2, where we installed Allas tools to directory `$HOME/allas-cli-utils`.
First we add this directory to command path:

```text
export PATH=${HOME}/allas-cli-utils:${PATH}
```

Next we open connection to Allas using the `allas_conf` script. Note that you must define your CSC user account
with `-u your-csc-account`. Here we assume that the user account is `kkayttaj`.

```text
source ${HOME}/allas-cli-utils/allas_conf -u kkayttaj
```

The command above asks for the password of the CSC user account and then lists the Allas projects that the user account has available.
In this case we select the number that defines project _project_2000123_. After that the Allas connections to the selected project will remain active for the next eight hours.

Now we can access Allas with [a-tools](../Allas/using_allas/a_commands.md) or [rclone](../Allas/using_allas/rclone.md). 
Next we upload the container image we just created to Allas with command:

```text
a-put --sdx sd_tools_1.sif -b 2000123_apptainer_sd -m "SD Compatible. Contains bamtools, samtools and vcftools."
```

In the command above option `--sdx` is used to encrypt the container with CSC public key. The encrypted container will be stored to bucket `2000123_apptainer_sd`. Here the bucket name contains the project number (2000123) to ensure uniqueness and _sd_ is used to indicate that this bucket contains SD Desktop compatible data. Option `-m` is used to add a description line to the metadata object that a-put creates.

## 5. Using Apptainer containers in SD Desktop

In order to use the apptainer container you have created you need first download a copy of the container to the SD Desktop with _Data Gateway_ tool. First login to [SD Desktop](https://sd-desktop.csc.fi) and connect to the Virtual Desktop that you want to use. Open Data Gateway, navigate then to the right project (`project_2000123`) and bucket (`2000123_apptainer_sd`), and download the Apptainer image file (`sd_tools_1.sif`) to the SD Desktop.

After that, open a Linux terminal in the SD Desktop. In the terminal, move the Apptainer file to the location you want to use it. In this example that could be done with command:

```text
cp /home/kkayttaj/Projects/SD-connect/project_2000123/2000123_apptainer_sd/sd_tools_1.sif ./
```

Now we could execute for example the samtools command that is installed in the container.

```text
apptainer exec sd_tools_1.sif samtools
```

The command above prints out the help for samtools version 1.10 that is installed in the container. Note that another version of samtools, version 1.9, is installed in the SD Desktop, so the command below would work too, but it would print help of the older samtools version:

```text
samtools --help
```

When using the Apptainer container, you should note that it has its own file system that is read-only. In addition to this static file system Apptainer mounts selected directories from the host system into the container environment. These bind mounts can be used to import data to the container, and they are also the only places into which new data can be written.

By default, Apptainer bind mounts **home directory** (`/home/$USER`), `/tmp`, and **current working directory** (`$PWD`) into your container at runtime. If you need to mount additional directories you will need to define them with singularity option `-B source-directory:target-directory`.

For example if we have input file `input_bam.bam` current working directory, it is automatically accessible for a command that is executed inside the container. But if we need also another input file `reference.bed` which locates in directory called `/data`, then we should add that directory to the list of bind-mounted directories. For example:

```text
apptainer -B /data:/data exec sd_tools_1.sif samtools depth -a -b /data/refrence.bed input_bam.bam > result.depth
```

 

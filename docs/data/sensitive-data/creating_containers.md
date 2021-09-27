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

Here we start from a situation where we have logged in to our freshly started virtual machine for the first time. As preparatory steps we need to install to our virtual machine **singularity** to create new software containers and **allas tools** to upload the containers created to Allas.

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


# How to use cPouta GPU for rendering?

If you have been granted GPU flavors, you can use GPUs for rendering. The following instructions show how to set up cPouta remote graphics environment. If you do not need an GPU accelerated environment for remote desktop here is instructions to set up a [Remote Desktop environment](how-to-use-pouta-for-remote-desktop.md). For GPU use, you need to install X, VNC, and VirtualGL servers. Once installed, the servers stay running also when you exit your SSH session. To return to using cPouta remote graphics, just open one secure SSH connection. The general procedure will be explained and some examples given. Part of the information is also available as a [video tutorial](https://youtu.be/An1e9ryS3nY).

The instructions are mainly for cPouta Ubuntu 18 image but the principles apply to the other linux distros. Ubuntu is a good choice if latest features are needed. Brief CentOS instructions are also provided at the end. These installations are minimal. Some applications require additional packages to run properly. Although cPouta CUDA images can be reconfigured for rendering, it is recommended to do the installation from scratch.

[TOC]
  
## Ubuntu installation

After launching a cPouta Ubuntu image, update package lists, install X server and Openbox windows manager

```
sudo apt-get update
sudo apt-get install xorg openbox
```

_(Skip the following driver installation if you are using a CUDA image.)_ First install linux kernel sources, which are needed for NVIDIA driver compilation to work. Then download the NVIDIA driver that is best suited to your needs. In this example a recent driver 450.51.06 is used. See NVIDIA web pages for the available linux drivers (cPouta has Tesla P100 cards).

```
sudo apt install build-essential libglvnd-dev pkg-config
sudo wget http://uk.download.nvidia.com/tesla/450.51.06/NVIDIA-Linux-x86_64-450.51.06.run
```

When you run the NVIDIA installation script, you'll get a warning that 32-bit compatibility libraries will not be installed, which is fine for most cases. If you do need 32-bit support, run first `sudo apt-get install gcc-multilib`

```
sudo sh NVIDIA-Linux-x86_64-450.51.06.run
```

_(Continue from here if you are using a CUDA image.)_ Configure X for the NVIDIA driver with **nvidia-xconfig** tool. It will find out the card's BusID address (PCI:0:5:0 in this example, replace with your query result), which will be used to create a X configuration file. Ignore the configuration file related warning.

```
nvidia-xconfig --query-gpu-info
sudo nvidia-xconfig --busid=PCI:0:5:0
```

VirtualGL middleware is needed to direct graphics to the NVIDIA card, and VNC server will stream the rendered graphics to your local VNC client. Download and install VirtualGL and TurboVNC servers. (You will also need a VNC client app on your local PC, see below.)

```
wget https://netix.dl.sourceforge.net/project/virtualgl/2.6.4/virtualgl_2.6.4_amd64.deb
wget https://kumisystems.dl.sourceforge.net/project/turbovnc/2.2.5/turbovnc_2.2.5_amd64.deb
sudo dpkg -i virtualgl_*.deb turbovnc_*.deb
```

Configure the VirtualGL server. If you are the only user on the virtual machine, answer **No** to all questions (choose: 1,n,n,n,x). More info is available at [virtualgl.org/Documentation/](https://virtualgl.org/Documentation/)

```
sudo vglserver_config
```
Reboot your cPouta virtual machine at this stage, before continuing.

After the reboot, start the VNC server. Define your virtual desktop window size by the _geometry_ parameter. Leaving it out defaults to 1240x900. The first time the VNC server is started, it will ask to create a password. When prompted, type (up to) 8 character password (twice), then reply **No** to a view-only password. You will need this TurboVNC password later, when connecting via your local PC's VNC viewer client. See **Usage** below. More info is available at [turbovnc.org/Documentation/](https://turbovnc.org/Documentation/)

```
/opt/TurboVNC/bin/vncserver -geometry 1920x1080
```

Start your X server (you need to hit _return_ twice), and set display number to 0.

```
sudo /usr/bin/X :0 &
export DISPLAY=:0
```

Now the GPU is ready to be used via your local VNC viewer, as described below. You'll need to have one secure SSH tunnel open for the VNC connection. The servers will keep on running when exiting SSH. If you reboot your virtual machine, run the last three commands above, to start the servers again.

  
## Usage - how to use cPouta remote graphics

Install TurboVNC 2.2.5 viewer to your local desktop PC from [sourceforge.net/projects/turbovnc/files/](https://sourceforge.net/projects/turbovnc/files/)

Open an encrypted SSH tunnel for the VNC connection between your PC and the virtual machine (VM). The port used by TurboVNC server is shown when TurboVNC starts: _TurboVNC started on display **name-of-VM:1**_ (name-of-VM is the instance name you have given to your virtual machine, and TurboVNC server uses the first available port). For your local PC, choose a port that is not in use already, say 5911. After the SSH tunnel is established, start your local TurboVNC viewer at the local port. See the examples below (note that other distros use *cloud-user* instead of *ubuntu* as the default username).

**Linux/Mac:**  
fill in your _vncviewer_ path, the ip number of your VM, its name, and the location and name of your key pair file. Type your TurboVNC password when prompted.

```
path/vncviewer -via ubuntu@ip-number-of-VM name-of-VM:1 -i path/private-key-file.pem
```

  
**Windows PC, at command prompt:**  
fill in your PuTTY path (PuTTY comes with TurboVNC, and the default path is used in this example), fill in the name of your VM, its ip number, and the location and name of your key pair file

```
"c:\\program files\\turbovnc\\putty.exe" -L 5911:name-of-VM:5901 ubuntu@ip-number-of-VM -i path\\private-key-file.ppk
```

**Windows PC, using PuTTY's graphical interface:**  
type the location of your key-pair file to _Private key file for authentication_ box in the _Auth_ panel of the PuTTY configuration box. Also fill in the source and destination ports ports, in the category _Connection_\-_SSH_\-_Tunnels_, _Source port:_ 5911, _Destination:_ name-of-VM:5901 (remember to click the _Add_ button). Save the session profile for further use.

After the SSH tunnel is established, open your TurboVNC viewer client. When _New TurboVNC Connection_ window opens, fill in localhost:11, click _Connect_, and type your TurboVNC password when prompted.

  
**All platforms:**  
After the TurboVNC password is accepted, an empty VNC window opens. Right-click to open a terminal. Remember to **start your apps with vglrun** command. For example, to run OpenGL test app glxspheres64, type

```
vglrun /opt/VirtualGL/bin/glxspheres64
```

When you have finished, close the VNC window by clicking the _X_ button either on the menu bar (_Disconnect_) or the top-right window corner. Do not right click the desktop and choose _exit_, since this closes the Openbox windows manager (see **Known issues** below).

  
## Useful commands

Find out TurboVNC server display number and process ID

```
/opt/TurboVNC/bin/vncserver -list
```

Close TurboVNC server running at display 1

```
/opt/TurboVNC/bin/vncserver -kill :1
```

Check if X server is running

```
ps auxw | grep X
```

Stop X server

```
sudo killall X (CentOS)
sudo killall Xorg (Ubuntu)
```

Find out glibc, NVIDIA driver versions

```
ldd --version
nvidia-smi
```

Uninstall NVIDIA driver (for example 450.51.06)

```
sudo sh NVIDIA-Linux-x86_64-450.51.06.run --uninstall
```

NVIDIA readme-file is located at _/usr/share/doc/NVIDIA_GLX-1.0/README.txt_

## Known issues

If you exit TurboVNC viewer window by right-clicking and choosing _exit_, Openbox windows manager will shut off. To start Openbox, close and restart your TurboVNC server as instructed above.

Some applications require additional packages to run properly. For example, in Ubuntu installation, ParaView needs an extra package

```
sudo apt-get install libxcb-keysyms1
```

and in CentOS

```
sudo yum install xcb-util-keysyms
```

  
##CentOS installation
----------------------

After launching a CentOS-7 image, update package lists, install X server, fonts, and Openbox windows manager

```
yum check-update
sudo yum install xorg-x11-xauth xorg-x11-server-Xorg dejavu-sans-fonts xterm openbox
```

Install linux kernel sources needed for NVIDIA driver compilation to work

```
sudo yum install kernel-devel-$(uname -r) gcc
```

Download NVIDIA driver (say version 450.51.06) install script

```
sudo wget http://uk.download.nvidia.com/tesla/450.51.06/NVIDIA-Linux-x86_64-450.51.06.run
```

Run the script. Suggested answers: **No** to _register the kernel module sources with DKMS_, and **No** to _Install NVIDIA's 32-bit compatibility libraries_. Ignore warnings.

```
sudo sh NVIDIA-Linux-x86_64-450.51.06.run
```

Configure X for the NVIDIA driver with **nvidia-xconfig** tool. It will find out the card's BusID address (PCI:0:5:0 in this example, replace with your query result), which will be used to create a X configuration file (ignore the corresponding warning).

```
nvidia-xconfig --query-gpu-info
sudo nvidia-xconfig --busid=PCI:0:5:0
```

Download VirtualGL and TurboVNC repos and install the servers

```
sudo wget --directory-prefix=/etc/yum.repos.d https://virtualgl.org/pmwiki/uploads/Downloads/VirtualGL.repo
sudo wget --directory-prefix=/etc/yum.repos.d https://turbovnc.org/pmwiki/uploads/Downloads/TurboVNC.repo
sudo yum install VirtualGL
sudo yum install turbovnc
```

Configure VirtualGL server (suggested answers: 1,n,n,n,x)

```
sudo /opt/VirtualGL/bin/vglserver_config
```

Start TurboVNC server. It will ask you to create a password. When prompted, type: 8 characters long password (twice), then reply **No** to a _view-only password_

```
/opt/TurboVNC/bin/vncserver -geometry 1920x1080
```

Edit _.vnc/xstartup.turbovnc_ file with your favorite editor. The file should include only the following two lines, delete everything else

```
#!/bin/sh
exec openbox-session
```

You need to restart TurboVNC server again, for the changes to take place. Either reboot VM or just kill and start again TurboVNC

```
/opt/TurboVNC/bin/vncserver -kill :1
/opt/TurboVNC/bin/vncserver -geometry 1920x1080
```

Start X server at display 0, and the cPouta remote graphics set-up is ready.

```
sudo /usr/bin/X :0 &
export DISPLAY=:0
```

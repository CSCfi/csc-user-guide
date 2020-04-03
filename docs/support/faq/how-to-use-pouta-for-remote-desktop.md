# How to use Pouta for Remote Desktop

This article will go through how to set up a remote desktop with noVNC and
ssh-tunnel into a non-GPU flavor in c- and ePouta. We are using noVNC because
it allows us to use our browser to access the desktop, i.e. no 
local installations needed. If you would like to have
instructions on how to use a GPU instance for rendering look
here: [How to use cPouta GPU for rendering](how-to-use-cpouta-gpu-for-rendering.md)

[TOC]

## Preparations
We will utilize the following technologies to install the remote desktop:

  - A standard-flavor, for example, _standard.medium_ 
  - CentOS-7 image (In Pouta they have already the epel-repository installed)
  - snapd to install the noVNC
  - noVNC, since it allows us to use our browser instead of a traditional VNC-client to view the desktop
  - tigervnc-server as our VNC server
  - Xfce as our Desktop environment
  - ssh-tunnel so that the VNC server is not open to the internet. This is very
important.

## Create and access your instance for remote desktop

1. Launch a standard-flavor instance with the CentOS-7 image.
2. Attach a floating IP to the instance.
3. In the security rules allow ingress ssh (port 22).
4. We will ssh into the instance with this command and create a ssh-tunnel. 
```
ssh -L2001:localhost:6081 cloud-user@YOUR-FLOATING-IP
```
This also works at least in the Windows Powershell. If you don't have
an ssh-agent running, you will need to specify also your ssh-key:
```
ssh -i C:\users\localusername\.ssh\yourkey.pem -L2001:localhost:6081 cloud-user@YOUR-FLOATING-IP
```
Note, that the port 2001 is the one that you will use with the browser later.
    
`-L2001:localhost:6081` means that we will be able to access port 6081 on the server
from our computer's local port 2001. Keep the terminal alive. The ssh-command is the only step
needed on the local computer.

## Install the required software on the VM

In this example we are using Xfce for our Desktop Environment. If you want to use
some other Desktop environment you will probably need to modify the
xstartup script.

```
sudo yum group install Xfce
```

Install snapd for noVNC and tigervnc for the vncserver (epel-release should already be installed)

```
sudo yum install -y epel-release snapd tigervnc-server
```

Start the snapd service so that we can install the noVNC

```
sudo systemctl start snapd
```

Install noVNC

```
sudo snap install novnc
```

## Configure our software

Create a base configure for the user you want to be able to use the remote desktop.

```
mkdir ~/.vnc
touch /home/cloud-user/.Xauthority
```

Configure a resolution you would like to use. 1920x1080 is a common resolution
but this have been tested to work with an resolution as big as 3840x2160 .

```
echo "geometry=1920x1080" > ~/.vnc/config
```

Configure the startup script.

```
echo '#!/bin/sh
unset SESSION_MANAGER
unset DBUS_SESSION_BUS_ADDRESS
xrdb $HOME/.Xresources
startxfce4 --display=:1 &' > ~/.vnc/xstartup
```

Add execution permission if you do not do this you will get a blank screen.

```
chmod +x /home/cloud-user/.vnc/xstartup
```

## Starting your remote desktop

Note, that with this documentation the NoVNC session will only work with ':1'.
Start vncserver

```
vncserver :1
```

The first time you start the server it will ask you to create a password. Please
do not reuse one of your other password for this, since the password is not
encrypted securely and can only be between 6 and 8 characters long. If you
forget your password you should be able change the password with the `vncpasswd`
command.

You can start the noVNC client by running

```
/var/lib/snapd/snap/bin/novnc --listen 6081 --vnc localhost:5901
```

The application location might differ based on the Linux distribution you are using.
The `--listen 6081` means on which port the service will be accessed from. The
`--vnc localhost:5901` means on what port it is expecting the vncserver to be 
accessed from. You can exit out of the noVNC session by `ctrl+c`.

You should now be able to access the noVNC session by going to this link in
your browser `http://127.0.0.1:2001/vnc.html` . Note, that the port number is the
same as the one you used with the ssh-command.

You can see your vncserver sessions by running the following command.

```
vncserver -list
```

To kill a VNC session you can run the command (change ':1' to the session number)

```
vncserver -kill :1
```

## Important information if you don't want to use the ssh-tunnel

It is of course also possible to use noVNC or VNC directly over the internet
but we strongly recommend against this. VNC is one of the easiest services to
exploit on the internet, it is not a question if your server will get hacked 
but when. If you are still going to disregard our recommendation at least be sure
that you add a good security rule to your server so that you can only access the
server from your IP.

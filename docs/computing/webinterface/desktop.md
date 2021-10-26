# Desktop
The desktop apps launches a remote desktop on the Puhti compute nodes for running graphical applications.

The desktop environment, terminal and apps launched in it are running inside a Singularity container, which means that some programs may behave differently or not work at all. 
The desktop can be launched with Mate or Xfce as desktop environment, or alternatively you can launch apps directly without a desktop environment.

Currently, only CPU rendering is supported in the graphical applications.

## Connecting
![](../../img/ood-vnc-connect.png)

The noVNC Connection tab can be used to connect to the remote desktop using your browser by selecting wanted compression and quality and then clicking Launch Desktop.

For better performance you can use a native VNC client, such as TigerVNC, to connect. Instructions for native VNC clients can be found in the Native instructions tab.

Using the browser to connect is recommended for most users.

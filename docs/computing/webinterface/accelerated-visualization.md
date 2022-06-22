# Accelerated visualization
The Accelerated visualization app enables using visualization applications with GPU acceleration on a Puhti compute node.

## Available applications
* [Abaqus CAE](../../apps/abaqus.md)
* [Ansys Workbench](../../apps/ansys.md)
* [COMSOL](../../apps/comsol.md)
* [ParaView](../../apps/paraview.md)
* [Visit](../../apps/visit.md)
* [VMD](../../apps/vmd.md)

## Launching
1. Open the `Accelerated visualization` page under Apps.
2. Specify the needed resources. One GPU will be reserved.
3. Select visualization application.
4. Launch the app.

## Connecting
There are two options for connecting to the Accelerated Visualization app:

1. **With web-browser**.
The noVNC Connection tab can be used to connect to the app using a web browser by selecting wanted compression and quality and then clicking `Launch Desktop`.
Using the browser to connect is recommended for most users.
![](../../img/ood-vnc-connect.png)
2. **With VNC client**.
For better performance you can use a native VNC client, such as RealVNC or TigerVNC.
Instructions for native VNC clients can be found in the Native instructions tab.
This requires installing the VNC client on your local machine.

## Using the app
The selected visualization application will launch automatically.

A menu with settings and a shortcut to the terminal (xterm) can be found by right clicking the background in the app session.
If the application windows do not behave as expected or menus in the application appear in the wrong place, it can usually be fixed by clicking `Restart Fluxbox` in the menu.

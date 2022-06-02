# Desktop
The desktop enables using graphical applications on a Puhti compute node.

The desktop can be launched as:

* **`Mate` or `Xfce` desktop**, where one or several applications can be started. The applications mentioned below have been tested to work. Also other graphical tools available in Puhti could work.
* **Single application**, currently are supported: [COMSOL](../../apps/comsol.md), [Grace](../../apps/grace.md), [GRASS GIS](../../apps/grass.md), [Maestro](../../apps/maestro.md), [MATLAB](../../apps/matlab.md), [ParaView](../../apps/paraview.md), [QGIS](../../apps/qgis.md), [SAGA GIS](../../apps/saga-gis.md), [SNAP](../../apps/snap.md), [Visit](../../apps/visit.md) and [VMD](../../apps/vmd.md).

At the moment, only CPU rendering is supported in the graphical applications.

## Launching
1. Open `Desktop` page under Apps 
2. Specify the needed resources. Desktop is run as [batch job](../running/getting-started.md) as anything else in Puhti, so the required resources need to be defined before launching the desktop. The recommended partiotion is [interactive](../running/interactive-usage.md), so that the job could start as soon as possible, but if more resources are needed also other partitions are available.
3. Select Desktop `Mate`, `Xfce` or 'None'. Use 'None', if starting single application.


## Connecting
There are two options for connecting to the remote desktop:

1. **With web-browser**. The noVNC Connection tab can be used to connect to the remote desktop using a web browser by selecting wanted compression and quality and then clicking `Launch Desktop`. Using the browser to connect is recommended for most users.
![](../../img/ood-vnc-connect.png)
2. **With VNC client**. For better performance you can use a native VNC client, such as RealVNC or TigerVNC. Native VNC client may also be a good alternative if experiencing issues with clipboard integration between remote desktop and local host with the browser connection. Instructions for native VNC clients can be found in the Native instructions tab. This requires installing the VNC client on your local machine.

## Using the desktop
The applications mentioned above have a direct shortcuts on desktop.

For starting any other software available in Puhti:

1. Open terminal
2. Start the software as described in [Applications section](../../apps/alpha.md), usually `module load XX` and `<start_command_for_XX>`.

(The applications menu in desktop does not include Puhti scientific applications, just basic Linux tools.)

The desktop environment, terminal and apps launched in it are running inside a Singularity container, which means that some programs may behave differently or not work at all.

The `Host Terminal` found on the desktop is a terminal running outside the container. You can use it to launch apps that launch their own Singularity container.

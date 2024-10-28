# Accelerated visualization
The Accelerated visualization app enables using visualization applications with GPU acceleration on a Puhti compute node.

## Available applications
* [Abaqus CAE](../../apps/abaqus.md)
* [Ansys Workbench](../../apps/ansys.md)
* [Blender](../../apps/blender.md)
* [CloudCompare](../../apps/cloudcompare.md)
* [COMSOL](../../apps/comsol.md)
* [ParaView](../../apps/paraview.md)
* [VisIt](../../apps/visit.md)
* [VMD](../../apps/vmd.md)

## Launching
1. Open the `Accelerated visualization` page under Apps.
2. Specify the needed resources. One GPU will be reserved.
3. Launch the app.
4. Connect to the desktop.
4. Launch the visualization application from the applications menu, found either in the top-left
   corner, or by right-clicking the desktop.

!!! Note

    Considerations about GPU partitions:
    
    * `gputest` has 15 minute time limit, but should usually be available immediately or very soon.
    * `gpu` enables longer usage of application, but might have also longer wait time in the queue.
    * GPU computing time is ~60x more expensive in billing units, so please keep the accelerated visualization application open only when you are actually using it. Use the `Delete` button on `My interactive Sessions` page to finish working.

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

The Accelerated Visualization app is used in the same way as the [Desktop app](desktop.md). However,
shortcuts for the accelerated apps will not be generated on the desktop automatically. To create
shortcuts for them, you can drag the desired application from the applications menu to the desktop.

Note that if you are running applications that do not benefit from GPU acceleration, you should use
the [Desktop app](desktop.md) instead. Only the applications suffixed with `(Accelerated)` benefit
from a GPU.

For more details about running your own applications in the Accelerated Visualization app, see the [creating containers page](../../containers/creating/#using-gpu-from-containers-in-interactive-sessions-in-puhti).

# Unsing Podman in SD Desktop

[Podman](https://podman.io/) contrainer and Pod manger is available in Ubuntu22 based SD Desktop virtual machines.
As Podman is able to use Docker containers, it can be user to replace Docker in you workflows.

As SD Desktop don't have access to software container repositories, 
you must save the container you wish to use into a file. The file needs to be uploaded to SD Connect from were is can 
be copied to a SD Desktop virtual machine.

To use the copied container, open a terminal window in your SD Dekstop virtual machine and load the container file 
to your Podman environment with command:
```text
podman image load -i your-podman-imade
```
After that you can check your readu podman images with command:
```text
podman image list
```

You must add options _--cgroup-manager cgroupfs_ When running your run a container
```text
podman run --cgroup-manager cgroupfs containe-id
```

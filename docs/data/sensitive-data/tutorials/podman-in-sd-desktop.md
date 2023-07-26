# Unsing Podman in SD Desktop

[Podman](https://podman.io/) container manger is available in Ubuntu22 based SD Desktop virtual machines.
Podman is able to use Docker containers and thus it can be used to replace Docker in your SD Desktop workflows.

As SD Desktop don't have access to software container repositories, 
you must save the container you wish to use into a _Docker archive file_ in some other environment where you have Podman or Docker.
This file must then be imported to SD Desktop through SD Connect.

For example to use _Trimmomatic_ software in SD Desktop of CSC project: _project_2000123_, you could use following procedure.

In a linux server where your have Docker available, create a Docker container file, that includes Trimmomaitc software.
This can be done with commands:
```text
sudo docker pull staphb/trimmomatic:latest
sudo docker images
sudo docker save -o trimmomatic.docker 932a84b67790
```
Here the last command uses container ID (932a84b67790) that was checked with the _docker images_ command.

The Docker file needs to be uploaded to SD Connect from were is can be copied to a SD Desktop virtual machine.
In this example the Docker file _trimmomatic.docker_ is uploaded to SD Connect using _a-put_ command:
```text
a-put --sdx trimmomatic.docker -b 2000123_docker  
```
To use the copied container, open a terminal window in your SD Desktop virtual machine. Copy the Docker file to the local disk of your SD Desktop and load the Docker container to your Podman environment. Remember to update your DataGateway connection before you try to access newly added files in SD Connect.

In the case of the Trimmomatic container you could do the container import with commands :

```text
cp Projects/SD-Connect/project_2000123/2000123_docker/trimmomatic.docker ./
podman image load -i trimmomatic.docker
podman image list 
podman image tag 932a84b67790 trimmomatic
```

In SD Desktop you must always add definitio _--cgroup-manager cgroupfs_ when running a Podman container.
For example, using the imported container to run Trimmomatic filtering for file _/media/volume/rawdata.fastq_ could be now done
with command 
 
```text
podman --cgroup-manager cgroupfs run -v /media/volume:/media/volume trimmomatic:latest trimmomatic SE /media/volume/rawdata.fastq  /media/volume/flitered.fastq MINLEN:100
```
In the command above the first part of the command is the actual podman command:
```text
podman --cgroup-manager cgroupfs run -v /media/volume:/media/volume trimmomatic:latest
```
The actula trimmomatic command, that defines the analysis, is:
```text
trimmomatic SE /media/volume/rawdata.fastq  /media/volume/flitered.fastq MINLEN:100
```

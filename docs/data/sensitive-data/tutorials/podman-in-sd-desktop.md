# Using Podman in SD Desktop

The [Podman](https://podman.io/) container manager is available in Ubuntu 22-based SD Desktop virtual machines.
Podman is able to use Docker containers and thus it can be used to replace Docker in your SD Desktop workflows.

As SD Desktop doesn't have access to software container repositories, 
you must save the container you wish to use into a _Docker archive file_ in some other environment where you have Podman or Docker.
This file must then be imported to SD Desktop through SD Connect.

For example, to use _Trimmomatic_ software in SD Desktop of CSC project `project_2000123`, you could use following procedure.

In a Linux server with Docker available, create a Docker container file that includes Trimmomatic.
This can be done with commands:

```text
sudo docker pull staphb/trimmomatic:latest
sudo docker images
sudo docker save -o trimmomatic.docker 932a84b67790
```

Here the last command uses container ID (932a84b67790) that was checked with the `docker images` command.

The Docker file needs to be uploaded to SD Connect from where it can be copied to a SD Desktop virtual machine.
In this example the Docker file `trimmomatic.docker` is uploaded to SD Connect using `a-put` command:

```text
a-put --sdx trimmomatic.docker -b 2000123_docker  
```
The command above encrypts the data (`--sdx`) and stores it to SD Connect bucket `2000123_docker`.

To use the copied container, open or refresh the Data Gateway connection in your SD Desktop virtual machine. Then open a terminal window and copy the Docker file to the local disk of your virtual machine. Now you can load the Docker container to your Podman environment. 

In the case of the Trimmomatic container you could do the container import with commands:

```text
cp Projects/SD-Connect/project_2000123/2000123_docker/trimmomatic.docker ./
podman image load -i trimmomatic.docker
podman image list 
podman image tag 932a84b67790 trimmomatic
```

In SD Desktop you must always add definition `--cgroup-manager cgroupfs` when running a Podman container.
For example, using the imported container to run Trimmomatic filtering for file `/media/volume/rawdata.fastq` could be now done
with command: 
 
```text
podman --cgroup-manager cgroupfs run -v /media/volume:/media/volume trimmomatic:latest trimmomatic SE /media/volume/rawdata.fastq  /media/volume/flitered.fastq MINLEN:100
```

In the command above the first part of the command is the actual `podman` command that defines the Podman operation (`run`), and mounting between local and container environments (`-v`).

```text
podman --cgroup-manager cgroupfs run -v /media/volume:/media/volume trimmomatic:latest
```

Rest of the command defines the actual `trimmomatic` analysis command:

```text
trimmomatic SE /media/volume/rawdata.fastq  /media/volume/flitered.fastq MINLEN:100
```

# Running Chipster in SD Desktop

Chipster is a user-friendly analysis software for high-throughput Life science data 
such as Visium, single-cell and bulk RNA-seq. Chipster provides a web interface to 
over 500 analysis tools that can be combined into workflows. 

The public Chipster server, available in [https://chipster.csc.fi](https://chipster.csc.fi) is not intended 
for processing sensitive data. This document describes how you can install your own  Chipster server to an 
SD Desktop virtual machine for analyzing sensitive data.

## Before installation

Installing a Chipster server requires significant storage resources and running it 
requires plenty of memory. Because of that you should apply for at least 1 TB volume 
for the virtual machine where you plan to install Chipster. Further, as some applications 
in Chipster require significant amount of memory the flavor of the SD Desktop virtual 
machine should medium computation or heavy computation. In SD Desktop, Chipster server used *Podman*
so the server is compatible only with SD Desktop Virtual Machines were Podman is available.


Note that all the users of the SD Desktop machine can use the same Chipster server. In these 
cases it is good practice ro assign  one user as a _Chipster manager_ that installs and 
manages the Chipster server.

## Installation

First contact CSC serviedesk to get the Chipster installation files available. 
Include the [Share ID](../sd-desktop-software.md#step-1-send-a-request) of your CSC 
project to the request.

Once you have access to the installation the actual process is simple.
Open DataGateway connection. Then use [SD Software installer](../sd-desktop-software.md#customisation-via-sd-software-installer) to install the *CSC tools* toolkit. Next open terminal and give command:

```text
chipster-installer.sh
```
Running this command starts the Chipster installation process that takes 1-2 hours and downloads nearly 200 GB of data to the Volume disk. Once the process has successfully finished you can start local Chipster server with command:

```test
start-chipster-server
```
Once the Chipstwer server is running, all users of the SD Desktop VM can use the same Chipster server. Thus this launch command should be executed only by the user that is acting as the chipster server manager. Running the command again closes the existimng server and launches a new one. In normal use the _start-chipster-server_ commans is used to start the service after reboot.


## Using chipster server

Running Chipster server can be used by opeing Firefox browser inside SD Desktop and the connecting to server address:  `http://localhost:8000`.

You can login to the local Chipster server using the dedault user name "chipster" and password "chipster" or by using your CSC username as username and password.

For more details about using Chipster service, please study the material in [Chipster home page](https://chipster.csc.fi).
Keep in mind that Chiprest features and tools that utilize external services are not functional in SD Desktop.
 


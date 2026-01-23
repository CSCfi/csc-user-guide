# Running Chipster in SD Desktop

Chipster is a user-friendly analysis software for high-throughput Life science data 
such as Visium, single-cell and bulk RNA-seq. Chipster provides a web interface to 
over 500 analysis tools that can be combided into workflows. 

The publick Chipster server, available in https://chipster.csc.fi is not intended 
for prcessing sensitive data. This document describes how you can install your own 
Chipster server to an SD Desktop virtual machine for analyzing sensitive data.

## Before installation

Installing a Chipster server requires significant storage resources and running it 
requires plenty of memory. Because of that you should apply for at least 1 TB volume 
for the virtual machine where you plan to install chipster. Further, as some applications 
in Chipster require significant amount of memory the flavor of the SD Desktop virtual 
machine should medium computation or heavy computation.

Note that all the users of a SD Desktop mechine can use the same Chipster server. In these 
cases it is good practice to assing a one user as a "Chipster managers" that install an 
manage the Chipster server.

## Installation

First contact CSC serviedesk to get the Chipster installation files available. 
Include the Share ID of your project to the request.

Once you have access to the installation the actual process is simple.
Open DataGateway connection. Then use [SD Software installer](../sd-desktop-software.md#customisation-via-sd-software-installer) to install the *CSC tools* help toolkit. Next open terminal and give command

```text
chipster-installer.sh
```
Running this command starts the chipster installation process that takes 1-2 hours and downloads nearly 200 GB of datat to the Volume disk. Once the process has successfully finished you can start local Chipster server with command:

```test
start-chipster-server
```
Once the Chipstwer server is running, all users of the SD Desktop VM can use the same Chipster server. Thus this launch command should be executed only by the users, that is acting as the chipster server manager. Running the command again closes the existimng server and launches a new one.


## Using chipster server

Running Chipster server can be used by opeing Firefox browser in SD Desktop and the connecting to server address:  `http://localhost:8000`.

You can login to the local chipster server using the dedault user name "chipster" and password "chipster" or using your CSC user name as username and  password.

For more details about using Chipster service, please study the [Chipster manual](https://chipster.2.rahtiapp.fi/manual),



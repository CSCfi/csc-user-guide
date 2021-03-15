# Pouta access through OpenStack APIs

This article introduces access to Pouta through OpenStack APIs. OpenStack 
APIs provide access to all OpenStack components and their resources, such 
as nova (compute), glance (VM images), keystone (authentication), swift 
(object storage), cinder (block storage), and neutron (networking). 

OpenStack APIs are RESTful and there are multiple ways to interact with 
them which include using the command-line tools (e.g., `openstack`) or 
using direct HTTP requests (e.g., with `curl`) or using one of the 
client libraries (e.g., the `openstacksdk`). 

In this article, we briefly look into using cURL to make direct HTTP requests 
to the OpenStack APIs  and move to check how to use the `openstacksdk` to automate 
some mundane tasks as a demonstration. 

### Pouta access through cURL

Before we can use cURL or any other client to make API requests we need 
to set some environment variables which hold our credentials to Pouta. This 
can be done by running a script that you can download from the 
[Pouta web interface] (https://pouta.csc.fi/dashboard/project/api_access/) 
after logging in. See more details from [here](install-client.md).

Once you have the script with your credentials (`<project_name>-openrc.sh`) from 
the web UI, you can add the environment variables by running the script as:

`source <project_name>-openrc.sh`

And supplying your CSC account username and password when prompted.  

### Pouta access through client libraries





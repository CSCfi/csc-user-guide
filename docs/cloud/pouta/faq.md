# Frequently asked questions about Pouta
[TOC]

## How to create default network and router in a Pouta project

Every cPouta project comes with a default network and router configuration enough for most purposes. Most often, you don't need to worry about the network or router configuration and you can create virtual machines using the defaults.

In the situation that your project is missing a default network you will not be able to create a virtual machine. And if you are missing a router, you will not be able to assign ports in your machine for example to a floating IP.

If you find yourself in the need of creating a network and or router, you can recreate the default settings via the web interface with the following instructions.

Go to the Network Topology view in cPouta web interface and review your project's Networks and Routers situation.

Create a default network

If you need to create a Network:

Go to Network \> Networks \> + Create Network and define the following settings (leave as default if not mentioned):

- Network tab
    - Network Name: <your project name, e.g. project_2001037\>
        - Admin state: UP
        - leave Create Subnet checked
- Subnet tab
    - Subnet name: <your project name, e.g. project_2001037\>
    - Network Address: 192.168.1.0/24
    - IP Version: IPv4
    - Gateway IP: 192.168.1.1
- Subnet Details tab
    - leave Enable DHPC checked
    - DNS Name Servers (one entry per line):
        193.166.4.24
        193.166.4.25

Finally, click on Create. Now you have your default project network created.

You still need to link this network to a new (or existing) router.

If you are missing a properly configured router, you will not be able to allocate IPs to ports in your virtual machines (when you click on "Associate floating IP", you will find out a message like "No ports available".

Create a default router  for your network

A default router can be created in the web interface. Go to Network \> Routers \> + Create Router
- Router Name: <your project name, e.g. project_2001037\>
- Admin State: UP
- External Network: Public

Click on Create Router.

You have now a default router that still needs to be connected to your project's network. Go to Network \> Routers view and open your router configuration by clicking its name.

In the Interfaces tab, click on Add Interface and set it up by:
- Subnet: <select your project network\>
- Click Submit

You should now have your router working.

After following these instructions you should have a working default network and router in your project and you should be able to normally create virtual machines and assign floating IPs to them.

 

And the same but with the OpenStack command line client tools :

    $ openstack network create project_2001037
    $ openstack subnet create --dns-nameserver 193.166.4.24 --dns-nameserver 193.166.4.25 \
    --network $(openstack network list -f value -c ID -c Name|grep -v public|cut -d " " -f1) \
    --subnet-range 192.168.1.0/24 --allocation-pool start=192.168.1.4,end=192.168.1.254 project_2001037
    $ openstack router create project_2001037
    $ openstack router set --external-gateway public project_2001037
    $ openstack router add subnet project_2001037 project_2001037


## How can I use FGCI grid form Pouta

cPouta environment allows you to set up your personalized computing environment at CSC. However, in cPouta you typically have only limited computing capacity available and thus cluster-like computing is not possible.

One option to mitigate the limited computing resources is to use FGCI grid for heavier computing tasks. FGCI grid provides free computing resources for Finnish academic research. The usage FGCI grid is described more in detail in the FGCI user guide.

FGCI grid is used through ARC middleware that you can install to your Virtual Machine in cPouta (or any linux or Mac OSX). Below we describe the steps for installing ARC middlieware to a Centos7 based VM running in cPouta and configuring it to use FGCI environment.

The installation process is described more in detail in the ARC middelware web site.

First thing to do is to install Grid CA certificates. For that you must add EGI-turustanchors repository to your repository list:

    cd /etc/yum.repos.d/
    sudo wget http://repository.egi.eu/sw/production/cas/1/current/repo-files/EGI-trustanchors.repo
After that the Gird CA Certificates can be installed with command:

    sudo yum install ca-policy-egi-core
Now you can install the nordugrid ARC client and its dependencies with command:

    sudo yum install nordugrid-arc-client nordugrid-arc-plugins-needed nordugrid-arc-plugins-globus ca-policy-igtf-classic ca-policy-igtf-mics ca-policy-igtf-slcs fetch-crl
Finally you must edit the ARC configuration file in: /etc/arc/client.conf so that it can locate the FGCI cluster names.

    sudo vi /etc/arc/client.conf
The content of the client.conf should look like:

**FGCI configuration:**

    [registry/index1]
    url=ldap://giis1.fgi.csc.fi:2135/Mds-Vo-name=Finland,o=grid
    registryinterface=org.nordugrid.ldapegiis
    default=yes
    [registry/index2]
    url=ldap://giis2.fgi.csc.fi:2135/Mds-Vo-name=Finland,o=grid
    registryinterface=org.nordugrid.ldapegiis
    default=yes
Now the ARC middleware client is installed and configured.

The ceritificate revocation list (CRL) needs to be updated after few days. The update is done by running command:

    sudo fetch-crl
You can add the above command to a suitable crontab process to keep the revocation list up to date automatically.

To be able to create a proxy certificate, that is needed to access FGCI environment, you must import your personal Grid Certificate the directory $HOME/.globus and set the access permissions for the certificate file correctly.

    mkdir $HOME/.globus
    cd $HOME/.globus/
    vi usercert.pem
    vi userkey.pem
    chmod 644 usercert.pem
    chmod 400 userkey.pem
In the case of FGCI grid you should also add a vomses file, describing the fgi.csc.fi Virtual Organization,to your $HOME/.arc  dierectory:

    mkdir $HOME/.arc
    echo '"fgi.csc.fi" "voms.fgi.csc.fi" "15003" "/O=Grid/O=NorduGrid/CN=host/voms.fgi.csc.fi" "fgi.csc.fi"' > $HOME/.arc/vomses
    After this you can use arcproxy command to create a proxy certificate:

    arcproxy -S fgi.csc.fi

And now you can use the ARC-client commands to use FGCI.

    arcsync -T
    arcsub fgci_job.xrsl
    arcstat -a
    arcget your_job_id
    For more effective FGCI usage, you can install arcrunner to your VM to help your with submitting and managing large amounts of FGCI jobs.





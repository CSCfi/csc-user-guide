# How to create default network and router in a Pouta project

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

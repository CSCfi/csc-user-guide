## OpenStack command line client tools for Pouta

This article describes using Pouta on the command line. If not done
already, start by [installing the OpenStack tools](install-client.md).

You can do most of the things you need in the OpenStack (Horizon)
web interface of cPouta and ePouta. However, sometimes it is handier,
or even necessary, to use command line tools. OpenStack is divided into
subcomponents that each take care of specific tasks such as managing
virtual machines, volumes or images. Each of these subcomponents has
its own API which can be accessed either programmatically or in a
terminal using the command line tools that are introduced in this
chapter.

The command line tools are used to control your use of the service, so
they should be installed either on your local laptop/desktop or
another server which you will use to manage the service.

# Using Pouta from the command line

This article lists some basic commands for some of the most common
operations in OpenStack. For each of the operations, we show a command
that uses the common OpenStack command line tool.

##### These recommended versions of the OpenStack commands should work with the current version of ePouta and cPouta (Train).

- [python-openstackclient](https://docs.openstack.org/releasenotes/python-openstackclient/)==4.0.2
- [python-cinderclient](https://docs.openstack.org/releasenotes/python-cinderclient/)==5.0.2
- [python-glanceclient](https://docs.openstack.org/releasenotes/python-glanceclient/)==2.17.1
- [python-heatclient](https://docs.openstack.org/releasenotes/python-heatclient/)==1.18.1
- [python-keystoneclient](https://docs.openstack.org/releasenotes/python-keystoneclient/)==3.21.0
- [python-neutronclient](https://docs.openstack.org/releasenotes/python-neutronclient/)==6.14.1
- [python-novaclient](https://docs.openstack.org/releasenotes/python-novaclient/)==15.1.1
- [python-swiftclient](https://docs.openstack.org/releasenotes/python-swiftclient/)==3.8.1

More information: [OpenStackClient pip module](https://pypi.org/project/python-openstackclient/)  

!!! info

    You can install the latest versions of the OpenStackClient pip module since they are backwards compatible.

##### Openstack commands and help

    openstack -h

You can get a list of the available OpenStack subcommands by appending "-h"
after the `openstack` command. If you wish to see the options for a specific
subcommand, add the command name after "help". For example:

    openstack help server create

##### Adding a keypair

    openstack keypair create --public-key <file> <name>

**The first thing you should do** is to
generate a keypair. It will be used to access virtual machines. You
can also optionally specify a public key you have previously generated,
in which case the private key is the one you generated when the
public key was generated.

Generate a key named "test" with a private key stored in "test.pem":

    openstack keypair create test > test.pem

##### List available images

    openstack image list

This command lists the images that are available for the user. This
includes public images and images that the user has added.

##### List the available flavors

    openstack flavor list

The flavor of a virtual machine defines its virtual hardware: how many
cores, how much memory, and so on.

##### Launch a virtual machine

    openstack server create --flavor <flavor> --image <image id> --key-name <key name> <name for machine>

This command has the minimum amount of information for launching a
functioning virtual machine.

!!! info

    The output of the command "openstack server create" shows also a 
    password called adminPass. You do not need to store this password as
    is not used when connecting to the virtual machine. The virtual 
    machine allows access to a user only if the user uses SSH keys.

##### Customize the virtual machine before launch

    openstack server create --flavor <flavor> --image <image id> --key-name <key name> --user-data user-data.sh <name for machine>

The `user-data.sh` file can have extra commands to be executed automatically after the instance has been launched.

Below is an example content of the script file that would add a custom user in to the flavor and giving it the `sudo` rights:

``` bash
#!/bin/sh

# Add a new user called boss
useradd -m boss

# Add the user to sudoers. No password is needed for sudo.
echo 'boss ALL=(ALL) NOPASSWD:ALL' > /etc/sudoers.d/boss
```

The script file can contain any arbitrary command, so some cautioness is recommended.

!!! Note
    Please note that the example does not contain addition of user authentication (public SSH key).

##### List instances

    openstack server list

This will give a list of the user's instances and information related
to them.

##### Terminate instances

    openstack server delete <server>

This command shuts down and removes the machine. The running virtual
machine is removed and cannot be recovered.

##### Associate public address

    openstack floating ip create public

A public address must first be allocated from a pool of addresses. At
this point, the IP address has not been assigned to any host.

    openstack server add floating ip <server> <address>

This command assigns the address that was just allocated to a virtual
machine.

When you no longer need the public address, you can release it to the
public pool by deleting it.

    openstack floating ip delete <address>

By doing this, you save billing units and maintain an efficient use of
public IPs. 

##### Authorization to connect to virtual machines

Create a new security group:

    openstack security group create <security group name>

Add a rule to this new group that allows ping from a specific
source network:

    openstack security group rule create --proto icmp --remote-ip <source network> --dst-port 0 <security group name>

Add a rule that allows SSH from a specific source network:

    openstack security group rule create --proto tcp --remote-ip <source network> --dst-port 22 <security group name>

Assign the newly created security group to your virtual server:

    openstack server add security group <server> <security group name>

By default, all connections to virtual machines are blocked. This command
allows ping and SSH access.

##### Server groups and affinity

Openstack has the option to create so-called server groups with
specific affinity and anti-affinity rules. You specify if you want to
use a specific group when launching a server.

A server group with an affinity rule guarantees that all virtual
machines launched in the group are launched on the same physical
server. A server group with an anti-affinity rule guarantees that all
servers in the group are launched on different physical servers. If no
suitable physical server is found, the virtual machine will not be
created.

    openstack server group create --policy <affinity or anti-affinity> <server group name>

After that, you can launch virtual machines in the group by
specifying the group ID in the hint parameter.

    openstack server create --flavor <flavor> --image <image id> --key-name <key name> --hint group=<server group id> <name for machine>

Check which virtual machines belong to the server group:

    openstack server group show <server group id>

### External documentation

[A more comprehensive openstack CLI reference](https://docs.openstack.org/python-openstackclient/latest/).

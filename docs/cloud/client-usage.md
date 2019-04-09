# 3.4.2 Using Pouta from the command line

This  page lists  some  basic commands  for some  of  the most  common
operations in OpenStack. For each of  the operations we show a command
that uses the common openstack command line tool. 

##### These versions of the openstack commands should work with with e- and cPouta.

    python-openstackclient==3.11.0
    python-cinderclient==2.2.0
    python-glanceclient==2.7.0
    python-heatclient==1.5.1
    python-keystoneclient==3.11.0
    python-neutronclient==6.0.0
    python-novaclient==9.0.1
    python-swiftclient==3.3.0

 

##### Openstack Commands and help

    openstack -h

You can get a list of  available openstack subcommands by appending -h
after openstack command. If you wish to see the options for a specific
subcommand, add the command name after "help". For example:

    openstack help server create

##### Adding a keypair

    openstack keypair create --public-key <file> <name>

<span style="line-height:  1.5;">The first thing  you should do  is to
generate a  keypair. It will be  used to access virtual  machines. You
can also optionally specify a  public key you've previously generated,
in which case the  private key will be the one  you generated when the
public  key was  generated.  To  generate a  key named  "test" with  a
private key stored in "test.pem", you would run the following:</span>

    openstack keypair create test > test.pem

##### List available images

    openstack image list

This will  list those  images that  are available  to the  user.  This
includes public images and images that the user had added.

##### List available flavors

    openstack flavor list

The flavor of a virtual machine defines its virtual hardware: how many
cores, how much memory and so on.

##### Launch a virtual machine

    openstack server create --flavor <flavor> --image <image id> --key-name <key name> <name for machine>

This command  has the  minimum amount of  information for  launching a
functioning virtual machine.

**Note: Do not  be alarmed by adminPass in the  output from "openstack
server create".  This is not used  when connecting only with  SSH keys
(the default on Pouta clouds).**

##### List instances

    openstack server list

This will give a list of  the user's instances and information related
to them.

##### Terminating instances

    openstack server delete <server>

This  will shut  down and  remove  the machine.   The running  virtual
machine will be removed and can't be recovered.

##### Associate public address

    openstack floating ip create public

A public address must first be  allocated from a pool of addresses. At
this point, the IP address has not been assigned to any host.

    openstack server add floating ip <server> <address>

This will  assign the  address that  was just  allocated to  a virtual
machine.

When  you don't  need the  public address  you can  release it  to the
public pool by deleting it.

    openstack floating ip delete <address>

By doing this  you save billing usage and maintain  an efficent use of
public IPs. 

##### Authorization to connect to virtual machines

You can create a new security group with the following command:

    openstack security group create <security group name>

To add  a rule  to this  new group  that allows  ping from  a specific
source network, you can run the following command:

    openstack security group rule create --proto icmp --src-ip <source network> --dst-port 0 <security group name>

To add a rule that allows SSH from a specific source network:

    openstack security group rule create --proto tcp --src-ip <source network> --dst-port 22 <security group name>

You can assign the newly created security group to your virtual server
with the following command:

    openstack server add security group <server> <security group name>

By default all connections to  virtual machines are blocked. This will
allow ping and SSH access.

##### Server groups and affinity

Openstack  has  an option  to  create  so  called server  groups  with
specific affinity and anti-affinity rules.  You specify if you want to
use a specific group when launching a server.

A  server group  with the  affinity rule  guarantees that  all virtual
machines launched  into that group  are launched on the  same physical
server. A server group with the anti-affinity rule guarantees that all
servers in the group are launched on different physical servers. If no
suitable physical  server is  found, the virtual  machine will  not be
created.

    openstack server group create --policy <affinity or anti-affinity>] <server group name>

After  that,  you can  launch  virtual  machines  into that  group  by
specifying the group ID in the hint parameter.

    openstack server create --flavor <flavor> --image <image id> --key-name <key name> --hint group=<server group id> <name for machine>

You can see what virtual machines  belong to the server group with the
following command.

    openstack server group show <server group id>

 

# External documentation

A more  comprehensive openstack CLI  reference can  be found  in [this
part of the official OpenStack documentation].

|                    | | | | |
|--------------------|-----|----------------|-----|----------------|
| [Previous chapter] |     | [One level up] |     | [Next chapter] |

 

 

  [this part of the official OpenStack documentation]: https://docs.openstack.org/python-openstackclient/latest/
  [Previous chapter]: https://research.csc.fi/pouta-install-client
  [One level up]: https://research.csc.fi/pouta-command-line-tools
  [Next chapter]: https://research.csc.fi/pouta-vm-lifecycle

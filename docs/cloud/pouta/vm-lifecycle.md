# Virtual machine lifecycle and saving billing units

This article explains the different states that virtual machine instances
can have and their effect on resource usage.

[TOC]

Similar to other cloud providers, Pouta virtual machines also have a lifecycle. 
Different states of virtual machines have different
resource requirements for the underlying hardware and are therefore
billed differently. Knowing about these different states in Pouta 
helps you make better decisions on how to maintain your infrastructure.
This could help you in saving billing units. The main states of the
virtual machines in Pouta are:

### Active
A virtual machine is said to be active when it
is in the *power on* state. It remains in the active state
irrespective of whether you are using it or not. Virtual machines in
the active state consume computing resources on one of our compute
nodes and are thus billed normally as explained in [Pouta flavors and billing].

### Shut off
The virtual machine is not running and is *powered
off*. However, a shut off virtual machine still consumes billing
units in the same way as an **active** one. This is
because active/powered off virtual machines consume the same computing
resources on one of our compute nodes as explained in [Pouta flavors and billing].

!!! warning
    A *shut off* virtual machine still consumes billing units. To stop
    consuming, select the *shelved* state.

### Pause
Pausing a virtual machine pauses all processes running
in the virtual  machine and  saves the  entire state  of the  machine
(memory, application  state, etc.) on  the host compute node.  You are
not able  to access your  virtual machine or hosted  applications when
the  virtual machine  is in  a *paused* state.  Some applications  may
suffer  from  side  effects  when   paused,  thus  this  sate  is  not
recommended for  production systems.  Some legacy  computational tasks
may benefit  from the paused  state but modern workflows  generally do
not use this state. Pausing of a virtual machine is billed in the same
way as an **Active** state virtual machine.

### Suspend
Suspending a virtual  machine saves its current  state on
the virtual machine's host compute  node. The virtual machine could be
resumed again to  the same state as it was  before the suspension, but
compute resources  (actual cores,  compute node etc.)  maybe different
from the ones which you had before suspending the virtual machine. You
are not able to access your machine when it is in a *suspended* state.
Virtual  machines   in  the   Suspended  state  are   billed  normally
as **Active** state virtual machines. Suspending is not generally used
in modern workflows.

### Shelved
Shelving  a virtual  machine  is  the  shutting  down  of
a virtual machine  and removing it from  the host compute node.  It is
like  shutting down  your home  computer and  relocating it  somewhere
new. This frees up all the computing resources which were reserved for
it. However it saves the state  of all other associated resources, for
example file system, floating ip's,  network configuration etc. in our
central storage. Shelving works best for our standard flavors that are
already backed  by our central  storage service. Shelving can  be slow
for flavors  that are using  local storage, especially  bigger flavors
since  the data  needs  to be  copied between  local  storage and  the
central storage.  Virtual machine in  the shelved state do not consume
billing units. In a rare occasion, if all of our compute resources are
being used  up, we  won't be  able to  un-shelve your  virtual machine
until someone frees up compute resources. N.B. that your floating-ips,
volumes and so on can't be  removed from the virtual machine before it
has been un-shelved.  If you have a floating-ips quota  of two and one
of them  is attached to an  shelved virtual machine you  have only one
left for  use. **Note** that ephemeral  storage in  the IO, GPU  or TB
flavor's will **not** get shelved.

### Terminate
Termination (or  deletion) removes the  virtual machine
from  your  project  and  frees  up compute  resources  that  were  in
use. These  cannot be  recovered and  all data  stored in  the virtual
machine gets deleted excluding any  attached volumes. Once the virtual
machine is deleted, you are no longer billed for that virtual machine.

The figure below  tries to illustrate state  transitions between these
states.

![Virtual machine lifecycle](/img/instance-lifecycle-1.png)

In  the  above section,  we  have  discussed  main states  of  virtual
machines in Pouta. However, theoretically  there are other states too,
full   list   of  states   and   their   behaviors  could   be   found
at [OpenStack Documentation].

# Save Your Billing Units

There are many practices which could  help you save billing units such
as:

### Automated  provisioning
Automated provisioning  and configuration
of your  virtual machines could  help you  to save billing  units. For
example, you can tear down your unused virtual machines with automatic
provisioning and  configuration when you  don't need them.  Later when
you  need   them  you   can  provision   new  virtual   machines  from
scratch. Your  data should always be  stored on a volume,  and virtual
machines should be launched when you need computation done. Here is an
example on how to automate a workflow with Heat, Ansible and Docker to
deploy Etherpad containing both  clustered database and Load balancing
in <https://github.com/CSCfi/etherpad-deployment-demo>.

### Boot from image
A  good utility in
Pouta  is creating  your  own virtual  machine  using *Boot from  image
(creates new  volume)* option. In  this case, even  if you  delete your
virtual  machine, the  entire file  system state  gets saved  into the
persistent volume in  our central storage service. You can  boot a new
virtual machine  from this  volume, it will  have the  same filesystem
state as  the previous  deleted virtual machine.  You may  attach this
volume to any other virtual machine  and access the file system of the
deleted  virtual  machine. These  are  billed  as normal  volumes  for
billing units, which is lower in  cost compared with a running virtual
machine. Creating virtual machines with this utility and deleting them
when   not  needed   will  help   you  save   on  your   billing  unit
allocation.  One great  option  is  that you  can  easily delete  your
virtual machine and  start a new virtual machine with  the same volume
and with a new flavor. This makes  it possible for you to easily scale
from a smaller  virtual machine flavor to our  biggest virtual machine
flavors.
!!! note
    This type of scaling is not recommended for IO,
    GPU  or TB  flavors  since  ephemeral storage  data  is  lost in  this
    process.

### Select suitable state of your virtual  machine
Depending upon your project  requirements you  can change the  state of  your virtual
machines for example, 

-   In  case you are going  on a long  vacation and want to  save your
    Billing Units, you can shelve your virtual machines.
-   If you  no longer require your virtual machine,  you can delete it
    after copying all essential data from it to a volume.

You can transition  between different states via  the Pouta dashboard,
command line tools or REST APIs depending upon your project setup. The
most common  states for your  virtual machines are Active,  Shut Down,
Shelved or  Deleted. There maybe  occasions when your  virtual machine
goes  into Error  state, virtual  machines  in Error  state are  still
billed. In case your virtual machine goes into Error state and you are
unable to recover it, please contact cloud-support@csc.fi.

### Resize  your virtual  machine
Resizing a virtual  machine is  a
good  utility  in  Pouta,  which   could  help  you  to  save  billing
units. Based upon  on your project requirements you could  scale up or
scale down  your virtual machine  to other flavors. Scaling  down your
virtual machine when  it has less computational workload  will free up
compute resources and  result in saving your billing  units. Later on,
depending on your computational workload you can scale up your virtual
machines. Please note  that you can only resize to  the flavors of the
same *family* only, i.e. for example  if you are using  the standard.
family flavor  you can  only resize it  to another  standard family
flavor. When the resize is  complete, the virtual machine status first
displays verify resize.  At this point,  you need to confirm  again if
your virtual machine has been  resized as expected. Resizing will have
downtime for  the virtual machine  until the whole resize  process has
been completed. Note that resizing is not as elegant as using the boot
from volume option explained above. If you know  beforehand that you want  change the
size  of the  virtual  machines  at some  point,  using the boot  from
volume when  launching   the  virtual  machine  will   give  you  more
flexibility.


  [Pouta flavors and billing]: vm-flavors-and-billing.md
  [OpenStack Documentation]: https://developer.openstack.org/api-guide/compute/server_concepts.html

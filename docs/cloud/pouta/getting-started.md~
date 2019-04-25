## Launching a virtual machine with the cPouta web interface

The  web interfaces  of the  Pouta clouds  are available  at following
addresses:

-    **<https://pouta.csc.fi> (cPouta  web interface,  accessible from
    internet)**
-    **<https://epouta.csc.fi>[ ][](ePouta  web interface,  accessible
    only  from   IPs which  you  provided  for   accessing  management
    interfaces of ePouta)**

This *OpenStack Horizon* based interface allows you do the basic cloud
computing management operations like launch  a new Virtual Machine and
manage security settings. To use this  service, you need a CSC account
and a cPouta/ePouta project at CSC.

There  are two  options for  logging  in the  cPouta's Dashboard:  CSC
username and  password or Haka  username and  password. If you  have a
Haka account, you  can use it to  login if you already  have access to
cPouta and if you  have linked it to your CSC account.  You can do the
linking by going [here] and logging in with Haka credentials. You will
be asked  to give your CSC  username and password. Note  that if after
logging in  after clicking  that link you  either get  the Scientist's
User Interface main page or an empty page, the linking has most likely
already been done.

For  ePouta  dashboard  you  can only  login using  CSC  username  and
password.

### 3.2.1 Preparatory steps

Before starting your first virtual  machine in cPouta/ePouta, you must
first  set up  an SSH  key pair  to be  used and  modify the  security
settings so that you will be able to connect to your virtual machine.

### 3.2.1.1 Setting up SSH keys

To open  a connection  to your virtual  machines in  cPouta/ePouta you
will need  to have  SSH keys. This  is the default  way to  access new
virtual machines. You only need to set up your SSH keys once.

If you are  already familiar with SSH keys, you  can use your existing
SSH keys  to access the virtual  machines. In the web  interface go to
**Access  & Security**  and  from **Key  Pairs**  select **Import  Key
Pair**.  Name  your  key,  and  paste your  public  key  (starts  with
something  like "ssh-rsa  AAFAA...." or  "ssh-dss AFAFA...")  into the
other box.

If you have not used SSH keypairs  before, you need to create one. The
web  interface  can take  care  of  this for  you.  Go  to **Access  &
Security** and  from **Key  Pairs** select  **Create Key  Pair**. Give
your  key   a  name  and  click   **Create**.  Now  you  will   get  a
"*keyname.pem*" to save. Save it under your home directory.

![][1]

**Figure  2.1** The  Access  &  Security subpage  in  the  cPouta  web
interface

To  finalize  the key  installation  in  **Linux**  and **Mac  OS  X**
environments, run the following commands in a command shell:

~~~~
cd ~
mkdir -p .ssh
chmod 700 .ssh
mv keyname.pem .ssh
~~~~

 

Before using  the newly  created key,  you need to  protect it  with a
passphrase  and  make the  key  read  only. You  can  do  so with  the
following commands:

~~~~
ssh-keygen -p -f .ssh/keyname.pem
chmod 400 .ssh/keyname.pem
~~~~

 

<span   style="line-height:    1.5;">Where   </span>*keyname.pem*<span
style="line-height: 1.5;"> is the file you downloaded.</span>

In **Windows** environments  the downloaded private key  can be loaded
for  example to  the  Putty SSH  client.  This is  done  by using  the
puttygen  tool to  load  your  private key  (.pem)  and  save it  into
(password  protected)  .ppk format  which  Putty  can use.  Putty  and
puttygen                are                available                at
[http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html]. Using
these  programs does  not  require administrator  privileges. As  with
Linux,  in Windows  it is  also important  to store  the keyfile  in a
secure location with limited permissions.

![][2]

**Figure 2.2**  Saving the  private key  into password  protected .ppk
format with puttygen

When connecting,  the private  key configuration  is found  in Putty's
Configuration menu  under **Connection \|  SSH \| Auth \|  Private key
file for authentication**. Use the  **Browse...** button to select the
proper  .ppk file.  When connecting  to the  Virtual Machine,  it will
first ask  for the  user name  (root or cloud-user)  and then  for the
password which you previously provided to puttygen. The session can be
saved for easier key access going forward.

After performing these  steps you should have what you  need to access
running instances.

### 3.2.1.2 Firewalls and security groups

Security groups are sets of firewall  rules which limit access to your
machines. <span style="color: rgb(0, 0, 0);">A virtual machine can use
one or more  security groups. </span>These firewall rules  are made on
the  *OpenStack* layer  and  you may  have  additional firewall  rules
within your virtual machine. In  the case of connectivity problems you
should make  sure both  the security group  and the  virtual machine's
internal firewall are correctly configured.

Security groups are easiest to edit  in the **Access & Security** page
of the web interface. Modifying or adding security groups is easy, but
you can  only do limited  things with  them. By default  all non-local
incoming traffic (including SSH connections)  is denied. You can allow
additional traffic by creating rules. A  rule opens a port range for a
set of IP addresses.

The  "Default"  security group  comes  with  rules  in it  that  allow
communication between virtual  machines that are all  connected to the
default  security  group.  If  you   want  your  virtual  machines  to
communicate  with each  other,  you  need to  either  add the  default
security group for them or add  similar rules to other security groups
used by your virtual machines.

As  a  practice, we  recommend  that  you  avoid using  the  "Default"
security  group  for any  other  rules.  If  your project  grows,  the
"Default" group  quickly becomes  unmanageable. We recommend  that you
create individual security groups for different purposes.

To access a virtual machine in the cPouta or ePouta services, you need
to allow SSH connections to the  machine. Do this by going to **Access
&  Security** in  the web  interface. Select  the **Security  Groups**
tab. Click  **Create  Security  Group**,  name  it  "SSH"  and  add  a
description like "Allow incoming SSH". Then click **Manage Rules** for
the SSH  security group. In  the view  that is displayed,  click **Add
Rule**.

**Note: "From port" and "To port" define a range of destination ports.
It is not possible to specify  the source port. Ingress means incoming
connections (to the  VM). Egress means outgoing  connections (from the
VM).**

If  you know  from which  subnet you  are going  to SSH  in from  e.g.
88.44.55.0/24 add a rule like this (recommended).

    Direction   IP Protocol   From Port   To port   Source Group   CIDR
    Ingress     TCP           22          22        CIDR           88.44.55.0/24

You can  also just open up  a port to a  single IP. In this  case, you
take the IP and add "/32" and add it as you would add a network:

    Direction   IP Protocol   From Port   To port   Source Group   CIDR
    Ingress     TCP           22          22        CIDR           88.44.55.77/32

If    you   don't    know    your   IP    address,    you   can    use
<http://www.myipaddress.com> to find out what it is.

You can  also open ports to  all possible IP addresses.  In that case,
you would use "0.0.0.0/0" for the network:

    Direction   IP Protocol   From Port   To port   Source Group   CIDR
    Ingress     TCP           22          22        CIDR           0.0.0.0/0

Opening up ports  this widely is not recommended and  is not necessary
in most  cases. Limiting access  to a  virtual machines to  only those
networks that actually need to access it is a good security practice.

**Please note:**

-    **Deleting  the  default  egress rules  (allow  any  protocol  to
    0.0.0.0/0  and  ::/0)  in  cPouta will  cause  disruption  to  the
    metadata service responsible  for SSH key injections.  If you want
    to  limit  egress traffic,  you  should  at least  allow  outbound
    traffic to IP 169.254.169.254, TCP  port 80 for SSH key injections
    to work.**
-   **Even though the ePouta  virtual machines are only accessible via
    the customer's  network, they  also need  to have  security groups
    configured for them. Otherwise they can not be accessed.**
-    **<span style="text-align:  justify;">It is  possible to  add and
    remove security  groups on a  running instance. This is  done from
    the instances page.</span>**

### 3.2.2 Launching a virtual machine

Once the  SSH keys  and security groups,  discussed in  Chapter 3.2.1,
have been  set, you can launch  a new virtual machine  using the Pouta
web interfaces:

 <https://pouta.csc.fi> (for  cPouta) or  <https://epouta.csc.fi> (for
ePouta)

In the  main page of the  Pouta web interface, open  the **Instances**
view. The  process to launch a  new virtual machine is  now started by
clicking the **Launch  Instance** button in the top of  the view. This
opens a  *launch instance* screen  where you define the  properties of
the new virtual machine.

 

![][3]

**Figure 2.3** Launch instance view.

In the  **Details** tab  of the *launch  instance* view,  first select
**Instance Boot  Source**. You will most  likely want to  select "Boot
from  image"   from  the   dropdown  menu.   <span  style="text-align:
justify;">In case  you want to  be more  cloud native, you  can select
"Boot from</span> image <span  style="text-align: justify;">(creates a
new volume)" option.  This option creates a new  persistent volume for
your  instance and  in an  event, if  your instance gets  accidentally
deleted by you  or goes in an unrecoverable state,  the file system of
your instance  will be saved  in this volume.  You can later  use this
volume to boot up a new instance  with the same filesystem state as of
the previous  instance.</span> **Please note:** This  approach creates
an  additional volume  which is  billed normally  as mentioned  on our
[pricing]  page.   After  selecting  instance  boot  source,  you  can
select an *Image* or a virtual machine *snapshot* you wish to use from
the **Image  Name** dropdown  menu. After that,  give your  instance a
*name* and select the *Flavor* (i.e.  size of the virtual machine, see
Table 3.1).  Under **Access &  Security** tab, choose the  keypair you
have created or added ( see Chapter 3.2.1) and the security groups you
wish to use (remember to select the security group for SSH access that
you created previously  in 3.2.1.2). Then from  the **Networking** tab
select your  own network (your  project name). Once you  have assigned
these parameters for your virtual  machine you can click **Launch** to
start the virtual machine.

### 3.2.3 Adding a public IP for the machine in cPouta

When a  virtual machine is  launched, it  only gets a  *NATed internal
network*.  This  means that  the machine can  access the  Internet and
other virtual machines  in cPouta, but you can not  access it from the
Internet.  To be able to access  your virtual machine, you need to add
a public IP address for it.

When the *Instances*  view shows that your machine is  *Active* and in
the *Running*  state, select **Associate  Floating IP** from  the drop
down menu that  shows up when you  click the arrow symbol  next to the
"Create Snapshot" button.

![][4]

**Figure 2.4** Floating IP association options

Click the plus to create a new  IP, select the IP, select your machine
under **Instance** and click **Associate**.  It will take some minutes
before  you are  able to  see the  second, public  IP address,  in the
*Instances view*. Once also the second IP is shown, your machine has a
public IP and is accessible from the Internet.

<img
src="https://research.csc.fi/documents/48467/84606/pouta-assign-ip.jpg/659543e4-9a2d-4752-bac8-83a9e2b20956?t=1431080210213"
width="551" height="258" />

**Figure 2.5** Floating IP association dialog

**Please  Note:** Starting  2018, allocated  or assigned  floating IPs
would be billed at the rate  of 0,2 BU/hr. You can additionally follow
our [blog-post] for management of floating IPs in a cPouta project.

|                    | | | | |
|--------------------|-----|----------------|-----|----------------|
| [Previous chapter] |     | [One level up] |     | [Next chapter] |

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

  [ ]: https://epouta.csc.fi
  [here]: https://sui.csc.fi/web/sui/add-services
  [1]: https://research.csc.fi/documents/48467/51198/pouta-user-guide-keypairs.png/72f5e560-8034-4d0e-b947-cffe6f84b720?t=1474022855105
  [http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html]: http://www.chiark.greenend.org.uk/%7Esgtatham/putty/download.html
  [2]: https://research.csc.fi/documents/48467/51198/Screenshot-puttygen-ppk2.png/1fdd33a6-d889-4659-8cf6-958ad62b513c?t=1441025138116
  [3]: https://research.csc.fi/documents/48467/84606/pouta-launch-instance.jpg/652a3773-90d1-4f7a-9b5e-e46ca0121720?t=1431080151386
  [pricing]: https://research.csc.fi/pricing-of-computing-services
  [4]: https://research.csc.fi/documents/48467/51198/associate-floating-ip-menu.png/361f853a-aba8-4baf-bd1c-6665e1907cab?t=1474023102486
  [blog-post]: http://pouta.blog.csc.fi
  [Previous chapter]: https://research.csc.fi/pouta-flavours
  [One level up]: https://research.csc.fi/pouta-usage
  [Next chapter]: https://research.csc.fi/pouta-connecting-a-virtual-machine

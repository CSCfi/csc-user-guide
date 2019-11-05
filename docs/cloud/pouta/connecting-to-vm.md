### Connecting to your virtual machine

This article describes several ways to connect to a running virtual machine.
Prerequisites include proper [firewall settings](../launch-vm-from-web-gui#Firewalls-and-security-groups)
and a [floating IP](../launch-vm-from-web-gui#adding-a-public-ip-for-the-machine-in-cpouta).

### Keypair based SSH connection

When your virtual machine has a  public Floating IP assigned in cPouta
cloud (or VM local  IP in case of ePouta) and  a [security group] that
allows  SSH,  you   can  open  a  remote  SSH   connection  into  your
instance. Any standard SSH client  should work.

A new  virtual machine will only  have a default user  account and the
*root*  or *administrator*  account or  in  some cases  only the  root
account. The user  account name depends on the image  used. For images
provided by  CSC it has  usually been  "cloud-user" but we  are moving
towards using the images upstream defaults  for example ubuntu 18 uses
"ubuntu". You can only log in using keypair based authentication, such
as:

    #for cPouta CentOS/ScientificLinux/Ubuntu 16.04 VMs
    ssh cloud-user@public-ip -i keyfile.pem

    #for cPouta Ubuntu 18.04 VMs
    ssh ubuntu@public-ip -i keyfile.pem

    #for ePouta CentOS/ScientificLinux/Ubuntu 16.04 VMs
    ssh cloud-user@vm-ip -i keyfile.pem

    #for ePouta Ubuntu 18.04 VMs
    ssh ubuntu@vm-ip -i keyfile.pem

With the default CSC images when you  try logging in as root, you will
get a message that tells you  what username to use instead. Some third
party  images may  use  the  root account  directly,  or a  completely
different username.

You can also use an *SSH agent*  instead of the command above. With an
*SSH agent*, you  will be able to  have one machine with  a public IP,
and connect via  SSH to the other machines from  that machine, without
having public  IPs for  all machines.  To use an  *SSH agent*  in your
local Linux or Mac OS X machine, start a shell and run commands:

    ssh-agent /bin/bash
    ssh-add ~/.ssh/keyname.pem

Now you should be able to connect  using SSH to the public Floating IP
of your VM in cPouta (or VM local IP in case of ePouta). The public IP
and private IP of your VMs are visible in the web UI if you are unsure
what they are. Once the key has  been loaded, you can use SSH agent as
follows: 

    #for cPouta VMs
    ssh -A cloud-user@public-ip

    #for ePouta VMs
    ssh -A cloud-user@vm-ip

The difference  is that you  are no  longer specifying the key  to use
using *-i*  since this  comes automatically from  the agent.  The *-A*
option stands  for *agent forwarding*. It  allows you to use  the host
with the public Floating IP as a  jump host, i.e. connect to other VMs
reachable  by the  jump host  that  allow this  particular key.  <span
style="color:#FF0000;">Please note that  key forwarding transfers your
private key  to the remote  host. This may  not be acceptable  in some
environments or security policies.</span>

Before connecting  to your virtual  machine, you can check  its status
from the *Instances* view of the cPouta/ePouta web interface.

![VM Status check](/img/Screenshot-Instances+view+-+OpenStack+Dashboard+-+Chromium.png)

**Figure** Instances view of the cPouta web interface.

Figure above shows a  sample  of  the  Instances  view in  cPouta  web
interface.   In this  case  we  can see  that  virtual machine  called
*a-dummy-instance* is  active  and running.  The  machine  has two  IP
addresses  of  which address  86.50.169.111  is  the public  one.  The
machine uses a keypair called *risto*.

ePouta web interface looks similar, but  instances in ePouta have only
one IP  address field specified  which is the virtual  machine's local
IP.

## Getting root access on a virtual machine

If you logged in using a default user account, you will be able to run
commands as root with sudo like so:

    sudo <some command>

You can also get a root shell like so:

    sudo -i

None  of the  accounts  in the  default images  provided  by CSC  have
password login enabled. In these  images, you can utilize sudo without
a password.   If accounts  that do  not have  root access  are needed,
those need to be created separately.

## Connect to a machine using the Pouta virtual console

The web interface includes a console tool that you can use to login to
your  virtual  machine directly.   However,  when  using CSC  provided
images, using the console requires you to create a user account with a
password into the virtual machine.

You  can open  a  console  session  by  clicking** Console** from  the
instance dropdown menu:

![Open console in web GUI](/img/console-button-horizon.png)

To input text into the console click the grey bar as shown:

![Input text to web console](/img/Screenshot-Instance+Details+-+OpenStack+Dashboard+-+Chromium-1.png)

After this you  can login with the user account  and password you have
created.

!!! note
    *Umlaut* *characters don't work in the virtual console for most keymaps.

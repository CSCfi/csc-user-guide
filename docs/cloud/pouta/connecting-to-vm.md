# Connecting to your virtual machine

This article describes several ways to connect to a running virtual machine.
The prerequisites include proper [firewall settings](../launch-vm-from-web-gui/#firewalls-and-security-groups)
and a [floating IP](../launch-vm-from-web-gui/#adding-a-public-ip-for-the-machine-in-cpouta).

### Keypair-based SSH connection

When your virtual machine has a public floating IP assigned in the cPouta
cloud (or VM local IP in the case of ePouta) and a [security group](../launch-vm-from-web-gui/#firewalls-and-security-groups) that
allows SSH, you can open a remote SSH connection to your
instance. Any standard SSH client should work.

A new virtual machine only has a default user account and the
*root* or *administrator* account, or in some cases, only the root
account. The user account name depends on the image used. For images
provided by CSC, it has usually been "cloud-user", but we are moving
towards using the image's upstream defaults. For example, Ubuntu 18 uses
"ubuntu". You can only log in using keypair-based authentication, such
as:

    #for cPouta CentOS/ScientificLinux/Ubuntu 16.04 VMs
    ssh cloud-user@public-ip -i keyfile.pem

    #for cPouta Ubuntu 18.04 VMs
    ssh ubuntu@public-ip -i keyfile.pem

    #for ePouta CentOS/ScientificLinux/Ubuntu 16.04 VMs
    ssh cloud-user@vm-ip -i keyfile.pem

    #for ePouta Ubuntu 18.04 VMs
    ssh ubuntu@vm-ip -i keyfile.pem

With the default CSC images, when you try logging in as root, you
get a message that tells you which username to use instead. Some third-party
images may use the root account directly or a completely
different username.

You can also use an *SSH agent* instead of the command above. With an
*SSH agent*, you are able to have one machine with a public IP
and connect via SSH to the other machines from that machine, without
having public IPs for all machines. To use a *SSH agent* in your
local Linux or Mac OS X machine, start a shell and run the following commands:

    ssh-agent /bin/bash
    ssh-add ~/.ssh/keyname.pem

Now you should be able to connect to the public Floating IP
of your VM in cPouta (or VM local IP in case of ePouta) using SSH. The public
and private IPs of your VMs are visible in the web UI if you are unsure
what they are. Once the key has been loaded, you can use the SSH agent: 

    #for cPouta VMs
    ssh -A cloud-user@public-ip

    #for ePouta VMs
    ssh -A cloud-user@vm-ip

The difference is that you are no longer specifying the key to use
using *-i* since this comes automatically from the agent. The *-A*
option stands for *agent forwarding*. It allows you to use the host
with the public floating IP as a jump host, i.e. to connect to other VMs
reachable by the jump host that allow this particular key. <span
style="color:#FF0000;">Please note that key forwarding transfers your
private key to the remote host. This may not be acceptable in some
environments or security policies.</span>

Before connecting to your virtual  machine, you can check its status
in the *Instances* view of the cPouta/ePouta web interface.

![VM Status check](/img/pouta-instance-details.png)

**Figure** The Instances view of the cPouta web interface.

The figure above shows a sample of the Instances view in cPouta web
interface. In this case, we can see that a virtual machine called
*test-instance-1* is active and running. The machine has two IP
addresses, of which the address 86.50.169.56 is the public one. The
machine uses a keypair called *skapoor*.

The ePouta web interface looks similar but the instances in ePouta have only
one IP address field specified which is the virtual machine's local IP.

## Getting root access on a virtual machine

If you logged in using a default user account, you will be able to run
commands as root with sudo:

    sudo <some command>

You can also get a root shell:

    sudo -i

None of the accounts in the default images provided by CSC have
password login enabled. In these images, you can utilize sudo without
a password. If accounts that do not have root access are needed,
they need to be created separately.

## Connect to a machine using the Pouta virtual console

The web interface includes a console tool that you can use to login to
your virtual machine directly. However, when using CSC-provided
images, using the console requires you to create a user account with a
password for the virtual machine.

You can open a console session by clicking **Console** in the
instance dropdown menu:

![Open a console in the web GUI](/img/console-button-horizon.png)

To input text in the console, click the grey bar:

![Input text to web console](/img/pouta-instances-terminal.png)

After this, you can log in with the user account and password you have
created.

!!! note
    *Umlaut* characters do not work in the virtual console for most keymaps.

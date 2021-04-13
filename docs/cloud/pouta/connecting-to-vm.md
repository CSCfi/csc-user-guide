# Connecting to your virtual machine

This article describes several ways to connect to a running virtual machine.
The prerequisites include proper [firewall settings](../launch-vm-from-web-gui/#firewalls-and-security-groups)
and, in case of cPouta, a [floating IP](../launch-vm-from-web-gui/#adding-a-public-ip-for-the-machine-in-cpouta).

## Keypair-based SSH connection

Before connecting to your virtual  machine, you can check its status
in the *Instances* view of the cPouta/ePouta web interface.

![VM Status check](/img/pouta-instance-details.png)

**Figure** The Instances view of the cPouta web interface.

The figure above shows a sample of the Instances view in cPouta web
interface. In this case, we can see that a virtual machine called
*test-instance-1* is active and running. The machine has two IP
addresses, of which the address 86.50.169.56 is the public one. The
machine uses a keypair called *skapoor*. The ePouta web interface looks 
similar but the instances in ePouta have only one IP address field 
specified which is the virtual machine's local IP.

When your virtual machine has a public floating IP assigned in the cPouta
cloud (or VM local IP in the case of ePouta) and a [security group](../launch-vm-from-web-gui/#firewalls-and-security-groups) that
allows SSH, you can open a remote SSH connection to your
instance. Any standard SSH client should work.

A new virtual machine only has a default user account and the
*root* or *administrator* account, or in some cases, only the root
account. The user account name depends on the image used. For images
provided by CSC, it has usually been "cloud-user", but we are moving
towards using the image's upstream defaults. For example, Ubuntu 18.04 
uses "ubuntu". You can only log in using keypair-based authentication, 
such as:

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

Instead of specifying the path to the key to use for the SSH connection 
each time, you can use an *SSH agent*. To use a *SSH agent* in your
local Linux or Mac OS X machine, start a shell and run the following 
commands:

    ssh-agent /bin/bash
    ssh-add ~/.ssh/keyname.pem

Now you should be able to connect to the public floating IP of your VM 
in cPouta (or VM local IP in case of ePouta) using SSH without the need 
of specifying the key:

    #for cPouta VMs
    ssh cloud-user@public-ip

    #for ePouta VMs
    ssh cloud-user@vm-ip

!!! Tip
    You can enable *agent forwarding* when connecting through SSH to a 
    virtual machine by using the *-A* flag.

        ssh -A cloud-user@public-ip

    By enabling agent forwarding, you enable the ssh agent running on 
    the virtual machine to make use of the keys which are loaded in the 
    ssh agent of your local workstation. You can use this feature to 
    reduce the number of floating IPs used in your project:
    
    1. Assign a floating IP to one of your instances
    2. ssh to the instance enabling agent forwarding
    3. You can now ssh from this instance to the other instances in the
       network using their private IP
    
    Using these steps, you need only a single public IP instead of one 
    public IP for each of the instances.

    **Warning**: using agent forwarding has some [security implications](https://blog.wizardsoftheweb.pro/ssh-agent-forwarding-vulnerability-and-alternative/#thevulnerability)
    which might be unacceptable in certain environments or for certain
    security policies.

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

The recommended way of accessing Pouta instances is through an SSH 
connection, as explained earlier. Nevertheless, if you suddenly find 
yourself experiencing issues with the SSH connection for example, the 
web interface includes a console tool that you can use to access your 
virtual machine directly.

In order to be able to use the console, **you need to set up a 
password-based user account first**. Once connected through SSH to your 
instance, you can use tools such as [useradd](https://linux.die.net/man/8/useradd)
and [passwd](https://linux.die.net/man/1/passwd) to set up this type of 
account. As indicated in our [security guidelines](../security/#disable-password-login-use-keys),
please do not enable remote login for this password-based account, but
rather use it only in case you need to access the instance though the 
console.

You can open a console session by clicking **Console** in the
instance dropdown menu:

![Open a console in the web GUI](/img/console-button-horizon.png)

To input text in the console, click the grey bar:

![Input text to web console](/img/pouta-instances-terminal.png)

After this, you can log in with the user account and password you have
created.

!!! note
    *Umlaut* characters, such as *ä* or *ö*, do not work in the virtual 
    console for most keymaps.

# Launching a virtual machine with the cPouta web interface

!!! Warning

    You should also get familiar with the security instructions and
    the terms of Pouta accounting before launching your first virtual
    machine.

This document explains a simple way to launch a virtual machine in the
Pouta service. Any CSC user with a computing project can request
access to the service as described in [Applying for Pouta access].
Please make sure you are familiar with the [concepts](../concepts.md) and
[security issues](security.md) first.  You might also want to take a
look at the webinar recording [in
YouTube](https://www.youtube.com/watch?v=CIO8KRbgDoI).

[TOC]


<!--TOC is to get the table of contents -->

The web interfaces of the Pouta clouds are available at following addresses:

| URL           | Service name           | Access |
| :------------- |:-------------| :-----|
| [https://pouta.csc.fi](https://pouta.csc.fi)       | cPouta web interface | Accessible from internet |
| [https://epouta.csc.fi](https://epouta.csc.fi)     | ePouta web interface      |  Accessible only from IPs which you provided for accessing management interfaces of ePouta |

This _OpenStack Horizon_ based interface allows you do the basic cloud computing management operations like launch a new Virtual Machine and manage security settings. To use this service, you need a CSC account and a cPouta/ePouta project at CSC.

There are two options for logging in the cPouta's Dashboard: CSC username and password or Haka username and password. If you have a Haka account, you can use it to login if you already have access to cPouta and if you have linked it to your CSC account. You can do the linking by going [here](https://sui.csc.fi/web/sui/add-services) and logging in with Haka credentials. You will be asked to give your CSC username and password. Note that if after logging in after clicking that link you either get the Scientist's User Interface main page or an empty page, the linking has most likely already been done.

For ePouta dashboard you can only login using CSC username and password.

### Preparatory steps

Before starting your first virtual machine in cPouta/ePouta, you must first set up an SSH key pair to be used and modify the security settings so that you will be able to connect to your virtual machine.

### Setting up SSH keys

To open a connection to your virtual machines in cPouta/ePouta you will need to have SSH keys. This is the default way to access new virtual machines. You only need to set up your SSH keys once.

If you are already familiar with SSH keys, you can use your existing SSH keys to access the virtual machines. In the web interface go to **Access & Security** and from **Key Pairs** select **Import Key Pair**. Name your key, and paste your public key (starts with something like "ssh-rsa AAFAA...." or "ssh-dss AFAFA...") into the other box.

If you have not used SSH keypairs before, you need to create one. The web interface can take care of this for you. Go to **Access & Security** and from **Key Pairs** select **Create Key Pair**. Give your key a name and click **Create**. Now you will get a "_keyname.pem_" to save. Save it under your home directory.

![ssh key pairs](/img/pouta-user-guide-keypairs.png)

**Figure** The Access & Security subpage in the cPouta web interface

To finalize the key installation in **Linux** and **Mac OS X** environments, run the following commands in a command shell:

```bash
cd ~
mkdir -p .ssh
chmod 700 .ssh
mv keyname.pem .ssh
```

Before using the newly created key, you need to protect it with a passphrase and make the key read only. You can do so with the following commands:

```bash
ssh-keygen -p -f .ssh/keyname.pem
chmod 400 .ssh/keyname.pem
```

Where _keyname.pem_ is the file you downloaded.

In **Windows** environments the downloaded private key can be loaded for example to the Putty SSH client. This is done by using the puttygen tool to load your private key (.pem) and save it into (password protected) .ppk format which Putty can use. Putty and puttygen are available at [http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html](http://www.chiark.greenend.org.uk/%7Esgtatham/putty/download.html). Using these programs does not require administrator privileges. As with Linux, in Windows it is also important to store the keyfile in a secure location with limited permissions.

![Screenshot puttygen](/img/Screenshot-puttygen-ppk2.png)

**Figure** Saving the private key into password protected .ppk format with puttygen

When connecting, the private key configuration is found in Putty's Configuration menu under **Connection | SSH | Auth | Private key file for authentication**. Use the **Browse...** button to select the proper .ppk file. When connecting to the Virtual Machine, it will first ask for the user name (root or cloud-user) and then for the password which you previously provided to puttygen. The session can be saved for easier key access going forward.

After performing these steps you should have what you need to access running instances.

### Firewalls and security groups

Security groups are sets of firewall rules which limit access to your machines. A virtual machine can use one or more security groups. These firewall rules are made on the _OpenStack_ layer and you may have additional firewall rules within your virtual machine. In the case of connectivity problems you should make sure both the security group and the virtual machine's internal firewall are correctly configured.

Security groups are easiest to edit in the **Access & Security** page of the web interface. Modifying or adding security groups is easy, but you can only do limited things with them. By default all non-local incoming traffic (including SSH connections) is denied. You can allow additional traffic by creating rules. A rule opens a port range for a set of IP addresses.

The "Default" security group comes with rules in it that allow communication between virtual machines that are all connected to the default security group. If you want your virtual machines to communicate with each other, you need to either add the default security group for them or add similar rules to other security groups used by your virtual machines.

As a practice, we recommend that you avoid using the "Default" security group for any other rules. If your project grows, the "Default" group quickly becomes unmanageable. We recommend that you create individual security groups for different purposes.

To access a virtual machine in the cPouta or ePouta services, you need to allow SSH connections to the machine. Do this by going to **Access & Security** in the web interface. Select the **Security Groups** tab. Click **Create Security Group**, name it "SSH" and add a description like "Allow incoming SSH". Then click **Manage Rules** for the SSH security group. In the view that is displayed, click **Add Rule**.

**Note: "From port" and "To port" define a range of destination ports. It is not possible to specify the source port. Ingress means incoming connections (to the VM). Egress means outgoing connections (from the VM).**

If you know from which subnet you are going to SSH in from e.g. 88.44.55.0/24 add a rule like this (recommended).
```bash
Direction   IP Protocol   From Port   To port   Source Group   CIDR
Ingress     TCP           22          22        CIDR           88.44.55.0/24
```
You can also just open up a port to a single IP. In this case, you take the IP and add "/32" and add it as you would add a network:
```bash
Direction   IP Protocol   From Port   To port   Source Group   CIDR
Ingress     TCP           22          22        CIDR           88.44.55.77/32
```
If you don't know your IP address, you can use [http://www.myipaddress.com](http://www.myipaddress.com) to find out what it is.

You can also open ports to all possible IP addresses. In that case, you would use "0.0.0.0/0" for the network:
```bash
Direction   IP Protocol   From Port   To port   Source Group   CIDR
Ingress     TCP           22          22        CIDR           0.0.0.0/0
```
Opening up ports this widely is not recommended and is not necessary in most cases. Limiting access to a virtual machines to only those networks that actually need to access it is a good security practice.

!!! Tip
    **Please note:**
    
    *   **Deleting the default egress rules (allow any protocol to 0.0.0.0/0 and ::/0) in cPouta will cause disruption to the     metadata service responsible for SSH key injections. If you want to limit egress traffic, you should at least allow outbound traffic to IP 169.254.169.254, TCP port 80 for SSH key injections to work.**
    *   **Even though the ePouta virtual machines are only accessible via the customer's network, they also need to have security groups configured for them. Otherwise they can not be accessed.**
    *   **It is possible to add and remove security groups on a running instance. This is done from the instances page.**

### Launching a virtual machine

Once the SSH keys and security groups, discussed in Chapter 3.2.1, have been set, you can launch a new virtual machine using the Pouta web interfaces:

[https://pouta.csc.fi](https://pouta.csc.fi) (for cPouta) or [https://epouta.csc.fi](https://epouta.csc.fi) (for ePouta)

In the main page of the Pouta web interface, open the **Instances** view. The process to launch a new virtual machine is now started by clicking the **Launch Instance** button in the top of the view. This opens a _launch instance_ screen where you define the properties of the new virtual machine.

![Launch cPouta instance](/img/pouta-launch-instance.jpg)

**Figure** Launch instance view.

In the **Details** tab of the _launch instance_ view, first select **Instance Boot Source**. You will most likely want to select "Boot from image" from the dropdown menu. In case you want to be more cloud native, you can select "Boot from image (creates a new volume)" option. This option creates a new persistent volume for your instance and in an event, if your instance gets accidentally deleted by you or goes in an unrecoverable state, the file system of your instance will be saved in this volume. You can later use this volume to boot up a new instance with the same filesystem state as of the previous instance. 

!!! Tip

   **Please note:** 
   
   This approach creates an additional volume which is billed normally as mentioned on our [pricing](https://research.csc.fi/pricing-of-computing-services) page. 
   
   
After selecting instance boot source, you can select an _Image_ or a virtual machine _snapshot_ you wish to use from the **Image Name** dropdown menu. After that, give your instance a _name_ and select the _Flavor_ (i.e. size of the virtual machine, see Table 3.1). Under **Access & Security** tab, choose the keypair you have created or added ( see Chapter 3.2.1) and the security groups you wish to use (remember to select the security group for SSH access that you created previously in 3.2.1.2). Then from the **Networking** tab select your own network (your project name). Once you have assigned these parameters for your virtual machine you can click **Launch** to start the virtual machine.

### Adding a public IP for the machine in cPouta

When a virtual machine is launched, it only gets a _NATed internal network_. This means that the machine can access the Internet and other virtual machines in cPouta, but you can not access it from the Internet. To be able to access your virtual machine, you need to add a public IP address for it.

When the _Instances_ view shows that your machine is _Active_ and in the _Running_ state, select **Associate Floating IP** from the drop down menu that shows up when you click the arrow symbol next to the "Create Snapshot" button.

![Associate floating IP menu](/img/associate-floating-ip-menu.png)

**Figure** Floating IP association options

Click the plus to create a new IP, select the IP, select your machine under **Instance** and click **Associate**. It will take some minutes before you are able to see the second, public IP address, in the _Instances view_. Once also the second IP is shown, your machine has a public IP and is accessible from the Internet.

![Assign IP](/img/pouta-assign-ip.jpg)

**Figure** Floating IP association dialog

!!! Tip
    Please Note: Allocated or assigned floating IPs are billed at the rate of 0,2 BU/hr. You can additionally follow our [blog-post](http://pouta.blog.csc.fi) for management of floating IPs in a cPouta project.


  [Applying for Pouta access]: ../../accounts/adding-service-access-for-project.md

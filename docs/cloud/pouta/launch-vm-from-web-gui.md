# Launching a virtual machine in the cPouta web interface

!!! Warning

    You should familiarize yourself with the security instructions and
    terms of Pouta accounting before launching your first virtual
    machine.

This document explains a simple way to launch a virtual machine in the
Pouta service. Any CSC user with a computing project can request
access to the service as described in [Applying for Pouta access].
To use Pouta, you need to have applied Pouta access for your project first.
Please make sure you are familiar with the [concepts](../concepts.md) and
[security issues](security.md) first. You might also want to take a
look at the [webinar](https://www.youtube.com/watch?v=CIO8KRbgDoI).

[TOC]


<!--TOC is to get the table of contents -->

The web interfaces of the Pouta clouds are available at following addresses:

| URL           | Service name           | Access |
| :------------- |:-------------| :-----|
| [https://pouta.csc.fi](https://pouta.csc.fi)       | cPouta web interface | Accessible on the internet |
| [https://epouta.csc.fi](https://epouta.csc.fi)     | ePouta web interface      |  Accessible only from IPs provided for accessing the management interfaces of ePouta |

This _OpenStack Horizon_ based interface allows you do basic cloud computing management operations such as launch a new virtual machine and manage security settings. To use this service, you need a CSC account and a cPouta/ePouta project at CSC.

There are two options for logging in the cPouta's Dashboard: CSC username and password, or Haka username and password. If needed, old accounts can be linked at [My CSC](https://my.csc.fi/) and logging in with Haka credentials. You will be asked to give your CSC username and password.

For ePouta dashboard, you can only login using the CSC username and password.

### Preparatory steps

In case you have multiple projects with Pouta access, first select the one you want to use at the menu bar on top left.

Before starting your first virtual machine in cPouta/ePouta, you must first set up a SSH key pair and modify the security settings so that you will be able to connect to your virtual machine.

### Setting up SSH keys

To open a connection to your virtual machines in cPouta/ePouta, you need SSH keys. This is the default way to access new virtual machines. You only need to set up your SSH keys once.

If you are already familiar with SSH keys, you can use your existing SSH keys to access the virtual machines. In the web interface, go to **Key Pair** section, and select **Import Public Key **. Name your key, and paste your public key (starts with something like "ssh-rsa AAFAA...." or "ssh-dss AFAFA...") into the other box.

If you have not used SSH keypairs before, you need to create one. The web interface can take care of this for you. Go to **Key Pairs** section, select **Create Key Pair**. Give your key a name and click **Create**. You get a "_keyname.pem_" to save. Save it in your home directory.

![ssh key pairs](/img/pouta-user-guide-keypairs.png)

**Figure** The _Access & Security_ subpage in the cPouta web interface

Finalize the key installation in the **Linux** and **Mac OS X** environments:

```bash
cd ~
mkdir -p .ssh
chmod 700 .ssh
mv keyname.pem .ssh
```

Before using the newly created key, you need to protect it with a passphrase and make the key read-only:

```bash
ssh-keygen -p -f .ssh/keyname.pem
chmod 400 .ssh/keyname.pem
```

_keyname.pem_ is the file you downloaded.

In **Windows** environments, the downloaded private key can be loaded, for example, in the Putty SSH client. This is done by using the _puttygen_ tool to load your private key (.pem) and save it in the (password protected) .ppk format which Putty can use. Putty and puttygen are available at [http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html](http://www.chiark.greenend.org.uk/%7Esgtatham/putty/download.html). Using these programs does not require administrator privileges. As with Linux, in Windows it is also important to store the keyfile in a secure location with limited permissions.

![Screenshot puttygen](/img/Screenshot-puttygen-ppk2.png)

**Figure** Saving the private key in the password protected .ppk format with puttygen

When connecting, the private key configuration is found in Putty's _Configuration_ menu under **Connection | SSH | Auth | Private key file for authentication**. Use the **Browse...** button to select the proper .ppk file. When connecting to the virtual machine, it first asks for the username (root or cloud-user) and then for the password which you previously provided to puttygen. The session can be saved for easier key access.

After performing these steps, you should have what you need to access the running instances.

### Firewalls and security groups

Security groups are sets of firewall rules which limit access to your machines. A virtual machine can use one or more security groups. These firewall rules are made on the _OpenStack_ layer and you may have additional firewall rules within your virtual machine. In case of connectivity problems, you should make sure both the security group and the virtual machine's internal firewall are correctly configured.

Security groups are easiest to edit on the **Access & Security** page of the web interface. Modifying and adding security groups is easy but you can only do limited things with them. By default, all non-local incoming traffic (including SSH connections) is denied. You can allow additional traffic by creating rules. A rule opens a port range for a set of IP addresses.

The "Default" security group comes with rules that allow communication between virtual machines that are all connected to the default security group. If you want your virtual machines to communicate with each other, you need to either add the default security group for them or add similar rules to other security groups used by your virtual machines.

As a practice, we recommend that you avoid using the "Default" security group for any other rules. If your project grows, the "Default" group quickly becomes unmanageable. We recommend that you create individual security groups for different purposes.

To access a virtual machine in the cPouta or ePouta services, you need to allow SSH connections to the machine. Do this by going to **Access & Security** in the web interface. Select the **Security Groups** tab. Click **Create Security Group**, name it "SSH", and add a description such as "Allow incoming SSH". Then click **Manage Rules** for the SSH security group. In the view that is displayed, click **Add Rule**.

**Note: "From port" and "To port" define a range of destination ports. It is not possible to specify the source port. "Ingress" means incoming connections (to the VM). "Egress" means outgoing connections (from the VM).**

If you know from which subnet you are going to SSH in from (e.g. 88.44.55.0/24), add a rule like this (recommended):
```bash
Direction   IP Protocol   From Port   To port   Source Group   CIDR
Ingress     TCP           22          22        CIDR           88.44.55.0/24
```
You can also just open up a port to a single IP. In this case, you take the IP and add "/32", and add it as you would add a network:
```bash
Direction   IP Protocol   From Port   To port   Source Group   CIDR
Ingress     TCP           22          22        CIDR           88.44.55.77/32
```
If you do not know your IP address, you can use [http://www.myipaddress.com](http://www.myipaddress.com) to find out what it is.

You can also open ports to all possible IP addresses. In that case, you would use "0.0.0.0/0" for the network:
```bash
Direction   IP Protocol   From Port   To port   Source Group   CIDR
Ingress     TCP           22          22        CIDR           0.0.0.0/0
```
Opening up ports this widely is not recommended and not necessary in most cases. Limiting access to a virtual machines to only those networks that actually need to access it is a good security practice.

!!! Tip
    **Please note:**

    *   **Deleting the default egress rules (allow any protocol to 0.0.0.0/0 and ::/0) in cPouta will cause disruption in the metadata service responsible for SSH key injections. If you want to limit egress traffic, you should at least allow outbound traffic to IP 169.254.169.254, TCP port 80, for SSH key injections to work.**
    *   **Even though the ePouta virtual machines are only accessible via the customer's network, they also need to have security groups configured for them. Otherwise they can not be accessed.**
    *   **It is possible to add and remove security groups on a running instance. This is done from the instances page.**

### Launching a virtual machine

Once the SSH keys and security groups, discussed in Chapter 3.2.1, have been set, you can launch a new virtual machine using the Pouta web interfaces:

[https://pouta.csc.fi](https://pouta.csc.fi) (for cPouta) or [https://epouta.csc.fi](https://epouta.csc.fi) (for ePouta)

In the main page of the Pouta web interface, open the **Instances** view. The process to launch a new virtual machine is now started by clicking the **Launch Instance** button in the top of the view. This opens a _launch instance_ screen where you define the properties of the new virtual machine.

![Launch cPouta instance](/img/pouta-launch-instance.jpg)

**Figure** Launch the instance view.

On the **Details** tab of the _launch instance_ view, first select **Instance Boot Source**. You will most likely want to select "Boot from image" in the dropdown menu. In case you want to be more cloud-native, you can select the "Boot from image (creates a new volume)" option. This option creates a new persistent volume for your instance. In the event you accidentally delete your instance or it enters an unrecoverable state, the file system of your instance will be saved in this volume. You can later use this volume to boot up a new instance with the same filesystem state as the previous instance.

!!! Tip

   **Please note:**

   This approach creates an additional volume which is billed normally as mentioned on our [pricing](https://research.csc.fi/pricing-of-computing-services) page.

After selecting the instance boot source, you can select an _image_ or a virtual machine _snapshot_ you wish to use in the **Image Name** dropdown menu. After that, give your instance a _name_ and select the _flavor_ (i.e. size of the virtual machine, see Table 3.1). Under the **Access & Security** tab, choose the keypair you have created or added (see Chapter 3.2.1) and the security groups you wish to use (remember to select the security group for SSH access that you created previously in 3.2.1.2). Then on the **Networking** tab, select your own network (your project name). Once you have assigned these parameters for your virtual machine, you can click **Launch** to start the virtual machine.

## Adding a public IP for the machine in cPouta

When a virtual machine is launched, it only gets a _NATed internal network_. This means that the machine can access the internet and other virtual machines in cPouta, but you can not access it on the internet. To be able to access your virtual machine, you need to add a public IP address for it.

When the _Instances_ view shows that your machine is _Active_ and in the _Running_ state, select **Associate Floating IP** from the drop down menu that shows up when you click the arrow symbol next to the "Create Snapshot" button.

![Associate floating IP menu](/img/associate-floating-ip-menu.png)

**Figure** Floating IP association options

Click the plus to create a new IP, select the IP, select your machine under **Instance**, and click **Associate**. It takes some minutes before you are able to see the second, public IP address in the _Instances view_. Once the second IP is shown as well, your machine has a public IP and is accessible on the internet.

![Assign IP](/img/pouta-assign-ip.jpg)

**Figure** Floating IP association dialog

!!! Tip
    Please note: Allocated and assigned floating IPs are billed at the rate of 0,2 BU/hr. You can additionally read our [blog post](http://cloud.blog.csc.fi/2017/12/floating-ip-management.html) for management of floating IPs in a cPouta project.

## Adding a security groups to the machine in cPouta

In the project, a user can manage the security group by creating or updating existing ones. A security group can be updated by adding different security rules for allowing or preventing network traffics. 

![Create a security group](/img/create_security_group.png)

**Figure** Creating and managing security groups

The new security group can be added to different virtual machines. A virtual machine can have many security groups. Different security groups can be added or removed from the existing VMs. 

![Attach a security group](/img/attach_security_group_vm.png)

**Figure** Managing security groups for virtual machine

  [Applying for Pouta access]: ../../accounts/how-to-add-service-access-for-project.md

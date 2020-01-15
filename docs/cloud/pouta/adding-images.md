# Creating, uploading and sharing virtual machine images

This article explains how to manage images in Pouta.

[TOC]

## Creating images

There are two different options for creating new virtual machine
images: creating the image from scratch, and launching a virtual machine
based on an existing image, making modifications on the running
machine and saving the changes as a new image by creating a snapshot.

### Creating an image based on an existing image

Launch a virtual machine using one of the available images either
through the Horizon web interface or through the command line
interface. 

Launching an instance on the command line:

```openstack server create --flavor <flavor> \
 --image <image uuid> \
 --key-name <key name> \
 --nic net-id=<name of network> \
 --security-group default \
 --security-group <additional security group> <name of server>
```

Login and make any necessary changes. To ensure consistent snapshots,
snapshots should only be created from instances which are powered off.
First power off your instance:

```
openstack server stop <name of vm>
```

Then create a snapshot of the machine's current state:

```
openstack server image create --name <name of snapshot to create> <name of vm>
```

It takes some time to create the snapshot. Once it is finished,
it appears as a new image. If you need the original instance, you
can power it on after the snapshot has been created.

```
openstack server start <name of vm>
```

In the web UI under **Compute \| Instances**, the instance-specific
Create Snapshot menu items work for the same effect as the CLI
command above. The snapshots created will appear in the **Compute \|
Images** section.

![Snapshot menu](/img/horizon-snapshot-menu.png)

### Creating an image from scratch

There are a number of tools for creating images from scratch. These
tools can be categorized into tools that involve running an operating
system in a virtual machine for setting up the image and tools
that take a base image and make modifications to it without running a
virtual machine. We will call these "installation-based tools" and
"base image tools".

<table> <colgroup> <col style="width: 33%" /> <col style="width: 33%"
/> <col style="width: 33%" /> </colgroup> <thead> <tr class="header">
<th> </th> <th>Installation-based tools</th> <th>Base image tools</th>
</tr> </thead> <tbody> <tr class="odd"> <td>Pros</td> <td><ul>
<li>Easy to use and understand</li> <li>Familiar workflow for anyone
familiar with manual OS installation</li> </ul></td> <td><ul>
<li>Fast</li> <li>Possible to automate</li> <li>Produces small
images</li> <li>Produces images suitable for clouds without
modification</li> </ul></td> </tr> <tr class="even"> <td>Cons</td>
<td><ul> <li>Slow</li> <li>Upgrades are cumbersome</li> <li>Care must
be taken to make images cloud-ready after the initial installation</li>
<li>Images produced can be quite large</li> </ul></td> <td><ul>
<li>May be difficult to customize images</li> </ul></td> </tr> <tr
class="odd"> <td>Examples</td> <td><a
href="http://linux.die.net/man/1/virt-install">virt-install</a>, <a
href="https://virt-manager.org/">virt-manager</a>, <a
href="https://www.virtualbox.org/">VirtualBox</a></td> <td><a
 href="https://github.com/openstack/diskimage-builder">diskimage-builder</a>,
<a href="http://libguestfs.org/virt-builder.1.html">virt-builder</a></td>
</tr> </tbody> </table>

The generic workflow when using installation-based tools:

1. Obtain an installation media or a network installation link.
2. Start a virtual machine and point it to the installation media or
 network installation link.
3. Go through the installer.
 - This step can optionally be automated using e.g. [Kickstart].
4. After the installation is finished, shut down the VM and use
 additional tools to prepare the image for cloud use.

The generic workflow when using base image tools:

1. Optionally customize configuration files that are used to generate
 the final image.
2. Determine the suitable customization parameters.
3. Run a command to generate the final image.

You can get more information about creating images in the very
thorough [OpenStack virtual machine image guide]. In particular, see
the chapters on [creating images manually] and [tool support for creating
images].

#### Caveats to keep in mind when creating images from scratch

These caveats usually only need to be considered when using
installation-based methods of image creation. The tools that use base
images are usually specifically designed to create images for clouds,
so they take care of these caveats for you. If you decide to use an
installation-based method of image creation, you should look into the
excellent [virt-sysprep] tool that takes care of most
modifications necessary for cloud use with a single command line
command. This chapter lists some of the caveats that need to be
handled before an image is ready for clouds.

#### cloud-init

There is a tool called [cloud-init] that must be installed on any
images that are to be used in Pouta clouds. It is used for certain
tasks that need to be run when a virtual machine first boots up
such as **generating SSH host keys and adding
user SSH public keys.**

#### User accounts (can be done with [virt-sysprep])

Cloud images should only have a minimal set of user accounts. Most
likely, they should only have one regular generic user account (e.g.
"cloud-user" on the default images provided by CSC) and the root user
account.

#### SSH host keys (can be done with [virt-sysprep])

Images used in the cloud must not contain any SSH host keys, as having
them in the image would mean that every server launched using the
image would have the same identity from the point of view of SSH. It
is also a security risk, as anyone with access to the image file would
be able to personate any server launched using that image file. Fresh
SSH host keys need to be generated by _cloud-init_ (see above) when a
virtual machine first boots up.

#### Network interface ordering (can be done with [virt-sysprep])

The _udev_ device manager in the Linux kernel has a function that 
pins a specific network interface name to a specific MAC address. This
is not good if several virtual machines are to be created from an
image, as all virtual machines will have different MAC
addresses. It is also not good if you create a snapshot out of a
virtual machine and try to use that snapshot to launch a virtual
machine, as it will remember the MAC address of the old virtual
machine that was used to create the snapshot. The best way to do this
is to use _virt-sysprep_.

#### Partitioning

When partitioning a Linux image, you should make sure the root
partition is the first and only partition. During the virtual machine
bootup process, OpenStack inserts SSH keys on the first partition
under the /root/.ssh directory, which means this partition must be the
root partition and not e.g. /boot. Logging in is not be possible
without the root password unless the keys are correctly inserted.

#### ACPI daemon

The ACPI daemon is used to receive commands to manage the power state
of a virtual machine. You should install an ACPI daemon on the machine
images to allow proper power down/reboot in the cloud interface.

#### Hotplug

To be able to use volumes, you need to have *ACPI hotplug*
enabled. This is on by default in CentOS 6 and newer, but for Ubuntu,
you need to add the line "*acpiphp*" to */etc/modules*. For other
distros, please check how to load *acpiphp* on boot from the distro
documentation.

## Uploading images

You can upload images either using the web interface or the
_openstack_ command line tool.

Before uploading, you need to know what format the image you are
uploading is. The most likely options are _qcow2_ and _raw_. You can
find out the type of the image using the _file_ command. This is what
a qcow2 image looks like:

~~~~
$ file images/Ubuntu-15.10-Phoronix.qcow2
images/Ubuntu-15.10-Phoronix.qcow2: Qemu Image, Format: Qcow (v3), 10737418240 bytes
~~~~

And this is what a raw image looks like:

~~~~
$ file images/Ubuntu-14.04-old.raw
images/Ubuntu-14.04-old.raw: x86 boot sector; partition 1: ID=0x83, active, starthead 0, startsector 16065, 20948760 sectors, code offset 0x63
~~~~

Upload using the command line:

```
openstack image create --disk-format <disk format> --private --file <image file to upload> <name of image to create>
```

This should upload the image. It takes a while before the image is usable.

If you prefer to use the web interface instead, you can upload images
in the **Compute \| Images** section by clicking the **Create
Image** button:

![Image upload](/img/horizon-image-upload2.png)

You will be presented with this dialog:

![Image upload dialog](/img/horizon-image-upload-dialog.png)

In this dialog, for example, we are creating an image called
_Alpine-linux_. You can optionally add an **Image Description** for
the image, if you need it for your reference. Due to security
concerns, we support image uploads only via your local machine, and
image upload via public URLs is disabled. In this example, we have
thus selected an image we want to upload from our local machine via the
**Browse** button. In this example, our image is an ISO image, so we
have selected that in the **Format** drop-down menu. All remaining
fields other than **Image Sharing \| Visibility** can keep their
default values. In the **Image Sharing \| Visibility** checkbox, please
make sure that you have set the visibility of the image as
_Private_. It is not possible for normal users to create public images
due to security reasons. In case you attempt to upload an image and
set its visibility as _Public_, you will get an error message. Setting
your image visibility to _Private_ will make your uploaded image
private to your particular OpenStack project, and only the members
of your project can access it.

## Sharing images between Pouta projects

You can share images between different Pouta projects using the "[glance]"
command line tool. Image sharing between projects is currently not
supported using the Pouta web interface. Once shared, the image will be
visible in both projects, i.e. between the donor and acceptor
projects.

Please note that image sharing works within the same cloud environment, i.e. you
can share images from one cPouta project to another but not between a
cPouta project and ePouta project or vice versa. 

To begin with, you need to add the acceptor project as a member of the image
to be shared by executing the following _glance_ command in the donor
project: 

```
glance member-create <your-image-UUID> <acceptor-project-ID> 
```

Then the acceptor project needs to accept this membership. To do so,
you or your colleague needs to execute the following glance command in the
acceptor project:

```
glance member-update <your-image-UUID> <acceptor-project-ID> accepted
```

* [GitHub page](https://github.com/CSC-IT-Center-for-Science/diskimage-builder-csc-automation)
* [Kickstart](https://github.com/rhinstaller/pykickstart/blob/master/docs/kickstart-docs.rst)
* [OpenStack virtual machine image guide](http://docs.openstack.org/image-guide/index.html)
* [creating images manually](http://docs.openstack.org/image-guide/create-images-manually.html)
* [tool support for creating images](http://docs.openstack.org/image-guide/create-images-automatically.html)
* [virt-sysprep](http://libguestfs.org/virt-sysprep.1.html)
* [cloud-init](https://cloudinit.readthedocs.org/en/latest/)
* [glance](https://research.csc.fi/pouta-install-client)

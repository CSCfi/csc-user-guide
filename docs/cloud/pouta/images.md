# Basic information about images

[TOC]

CSC provides a set of standard images that are well suited for cloud
use. In most cases, you can use these images instead of creating your
own. The images are created automatically using _diskimage-builder_. 
If you are interested in the details of how
these images are created, see this [GitHub page]. The images are
updated at regular intervals so that they contain the latest security
updates at the time virtual machines are launched.

It is possible that for some use cases the automatically created
images are not suitable. In this case, it is possible to create your
own images and use them instead. However, there are some caveats 
to consider when creating your own images that you would not
need to consider when using the default images. For more information,,
see [Advanced images](../adding-images)

## The main features of the images provided by CSC

The images provided by CSC are mostly the same as upstream.

* Most of the images come with the pre-configured username `cloud-user`,
though there are some exceptions to this rule.
* We make sure that the images are updated before releasing them,
so that we are sure that they work.
* The `-Cuda` images come preinstalled with the latest CUDA drivers.
* We enable automatic updates.
* We disable password login.
* We sometimes add some nice-to-have packages such as _vim_ or _ntp_. We try to
keep the additional packages at a minimum.

## Images

|Image|Username|Modified <br/>|
|--- |:---:|:---:|
|CentOS-8   |cloud-user | yes|
|CentOS-7   |cloud-user | yes|
|CentOS-7-cuda   |cloud-user |yes|
|ScientificLinux-7   |cloud-user | yes|
|Ubuntu-20.04   |**ubuntu** | no |
|Ubuntu-18.04   |**ubuntu** | no |
|Ubuntu-16.04   |cloud-user | yes|
|Ubuntu-16.04-Cuda   |cloud-user | yes|

### CentOS-8
Currently in a *tech preview* because we have found some
[minor issues](https://bugs.centos.org/view.php?id=16948) with it.

At the moment we are making these changes to it:
 - we change the username to "cloud-user" instead of centos
 - we have removed the 192.168.122.1 resolver in /etc/resolv.conf

CentOS is the community version of Red Hat Enterprise Linux (RHEL).

Another difference is that this image does not have automatic updates enabled.

### CentOS-7
CentOS is the community version of Red Hat Enterprise Linux (RHEL). CentOS-7
is the distribution that the Pouta admins are the most accustomed to. 
This is the second-newest major release of CentOS.

### CentOS-7-Cuda
This is the same as CentOS-7 but comes with preinstalled NVIDIA drivers.
These are useful in combination with the GPU flavors since you do not need
to download the drivers yourself. We try to always have the latest NVIDIA
drivers installed, but sometimes we are lagging a bit behind. These images
are huge, so you should use the normal CentOS-7 image if you are not
using a GPU-flavor VM.

### ScientificLinux-7
Basically CentOS-7 but with a slightly different topping. Some
research organizations use ScientificLinux. If you are unsure, you
should prefer CentOS-7.

### Ubuntu-20.04 LTS
Ubuntu-20.04 LTS image, included in Pouta, another one from Ubuntu image family for
those who do not want to use CentOS. Note that like Ubuntu-18.04, Ubuntu 20.04 also 
has `ubuntu` as the default username instead of `cloud-user`.
This is the another image type we started to provide directly from the upstream after Ubuntu-18.04.

### Ubuntu-18.04 LTS
Some like chocolate, some like strawberry. This is the choice for those that
do not want to use CentOS. Note that Ubuntu-18.04 has `ubuntu` as the default 
username instead of `cloud-user`, since it was the first image type we started 
to provide directly from the upstream.

### Ubuntu-16.04 LTS
If you for some reason need an older version of Ubuntu.

### Ubuntu-16.04-Cuda
Similar to CentOS-7-Cuda, comes with NVIDIA drivers preinstalled. There
is very little reason to use this if you are not using the GPU flavors.

## Snowflake images
These images you should probably not use without a really good
reason. You might be better off [creating your own image](../adding-images)

If there any images that you think we should add, do not hesitate to contact
[Service Desk](mailto:servicedesk@csc.fi).

### cirros
This is a really small image which can be used to boot an instance really fast.
This can be useful for doing tests in Pouta, such as testing if the network works or
how fast you can launch an instance. You should not use this for persistent
VMs, and you should always delete the instance when you are done with
testing. There is very little reason for end-users using this image, and if
you are unsure, CentOS and Ubuntu are better choices 99% of the time. 

[GitHub page]: https://github.com/CSC-IT-Center-for-Science/diskimage-builder-csc-automation

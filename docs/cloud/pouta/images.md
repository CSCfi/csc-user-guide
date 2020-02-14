# Basic information about images

[TOC]

CSC provides a set of standard images that are  well suited for cloud
use. In most cases you can use these images instead of creating your
own. These images are created automatically using a tool called
diskimage-builder. If you are interested in the details about how
these images are created, see this [GitHub page]. These images are
updated at regular intervals so that they contain the latest security
updates at the time virtual machines are launched.

It is possible that for some use cases the automatically created
images are not suitable. In this case it is possible to create your
own images and use them instead. However, there are some caveats that
you need to consider when creating  your own images that you would not
need to consider when using the default images. For more information
you can look in our [advanced images page](../adding-images)

/* openstack image list --public */

## What is the main differences between the images that CSC provides?
The images provided by CSC are mostly the same as upstream.

* Most of the images comes with the pre-configured username `cloud-user`,
though there are some exceptions to this rule.
* We are making sure that the images are updated before releasing them
so that we are sure that they work.
* The `-Cuda` images come pre-installed with the latest CUDA drivers.
* We enable automatic updates.
* We disable password login.
* We sometimes add some nice to have packages like vim or ntp. We try to
keep additional packages at a minimum.

## Images

|Image|Username|Modified <br/>|
|--- |:---:|:---:|
|CentOS-8   |**centos** | no |
|CentOS-7   |cloud-user | yes|
|CentOS-7-cuda   |cloud-user |yes|
|Ubuntu-18.04   |**ubuntu** | no |
|Ubuntu-16.04   |cloud-user | yes|
|Ubuntu-16.04-Cuda   |cloud-user | yes|

### CentOS-8
Currently in a *tech preview* because we have found some
[minor issues](https://bugs.centos.org/view.php?id=16948) with it.

CentOS is the community version of Red Hat Enterprise Linux (RHEL).
This image is exactly as provided by CentOS and we have not modified it
in any way.

Note that CentOS-8 has `centos` as default username.
If you attempt to login as the root user there will be a helpful message telling
you which user has your key installed.
Another difference is that this image does not have automatic updates enabled.

### CentOS-7
This is the distribution that the Pouta admins are most accustomed to, at least
when it comes to work. This is the second newest major release of CentOS.
At the time of writing we are still waiting for CentOS-8 cloud images to be
released before we start providing CentOS-8 as well.

### CentOS-6
This is the oldest version of CentOS that we provide in Pouta. You should
probably not use this version if you don't have a really good reason why.
We will remove our pre-made CentOS-6 images once CentOS-6 is at end of life
November 2020.

### CentOS-7-Cuda
This is the same as CentOS-7 but it comes with pre-installed NVIDIA drivers.
These are useful in combination with the GPU-flavors since you don't need
to download the drivers yourself. We try to always have the latest NVIDIA
drivers installed, but sometimes we are lagging a bit behind. These images
are quite huge, so you should use the normal CentOS-7 image if you are not
using a GPU-flavor VM.

### ScientificLinux-7 and ScientificLinux-6
These are basically CentOS-7/CentOS-6 but with a bit different topping. Some
research organizations are using ScientificLinux. If you are unsure you
should prefer CentOS-7.


### Ubuntu-18.04 LTS
Some like chocolate, some like strawberry. This is the choice for those that
don't want to use CentOS. Note that Ubuntu-18.04 is that one image that
has `ubuntu` as default username instance of `cloud-user`, since it was the
first image type we started to provide directly from upstream.

### Ubuntu-16.04 LTS
If you for some reason need an older version of Ubuntu.

### Ubuntu-16.04-Cuda
Similar to CentOS-7-Cuda, comes with NVIDIA drivers pre-installed. There
is very little reason to use this if you are not using GPU-flavors.

## Snowflake images
These images you should probably not use if you don't have a really good
reason. You might be better of [creating your own image](../adding-images)

Is there any images that you think we should add don't hesitate contacting
servicedesk@csc.fi

### cirros
This is a really small image which can be used to boot instance really fast.
This can be useful to doing tests in Pouta, like does the network work or
how fast can one launch an instances. You should not use this for persistent
VMs, and you should always delete the instance when you are done with
testing. There is very little reason for end-users using this image and if
you are unsure, CentOS and Ubuntu are a better choice 99% of the time.

### Ubuntu-14.04
Ubuntu-14.04 has been at End of Standard Support for some time and will go
EOL in 2022. We recommend to use newer Ubuntu images.

### Fedora-Atomic-25
You probably don't want to use this if you are not sure. We will most likely
remove this image in the near future since it is getting quite out of date.

[GitHub page]: https://github.com/CSC-IT-Center-for-Science/diskimage-builder-csc-automation

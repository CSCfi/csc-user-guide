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
Most of the images that are provided by CSC is mostly the same as upstream.

* Most of the images comes with the pre-configured username `cloud-user`
there are some exceptions to this rule.
* We are making sure that the images are updated before releasing them
so that we are sure that they work.
* The `-Cuda` images that comes pre-installed with that latest CUDA drivers.
* We enable automatic updates.
* We disable password login
* We sometimes add some nice to have package like vim,ntp. We try to keep
them at a minimum.

## Images

### CentOS-7
CentOS is the community version of Red Hat Enterprise Linux (RHEL). CentOS-7
is the distribution that the Pouta admins are most accustomed to, at least
when it comes to work. This is the second newest major release of CentOS 
as of writing we are still waiting for CentOS-8 cloud images to be released
before we start providing CentOS-8 as well.

### CentOS-6
This is the oldest version of CentOS that we provide in Pouta. You should
probably not use this version if you don't have a really good reason why.
We will remove our pre-made CentOS-6 images once CentOS-6 is end of life
November 2020

### CentOS-7-Cuda
This is the same as CentOS-7 but it comes with pre-installed NVIDIA drivers
these are useful in combination with the GPU-flavors since you don't need
to download the drivers yourself. We try to always have the latest NVIDIA
drivers installed but sometimes we are lagging a bit behind. These are
quite huge so you can get by well with the normal CentOS-7 image if you
are not using a GPU-flavor.

### ScientificLinux-7 and ScientificLinux-6
These are basically CentOS-7/CentOS-6 but a bit of different topping. Some
research organizations are using ScientificLinux. If you are unsure you
probably prefer CentOS-7


### Ubuntu-18.04
Some like chocolate some like strawberry this is the choice for those that
don't want to use CentOS. Note that Ubuntu-18.04 is that one image that
has `ubuntu` as default username instance of `cloud-user`.

### Ubuntu-16.04
If you for some reason needs an older version of Ubuntu then this is the one
that have long time support.

### Ubuntu-16.04-Cuda
Similar to CentOS-7-Cuda, comes with NVIDIA drivers pre-installed but there
are very little reason to use it if you are not using GPU-flavors.

## Snowflakes images
These images you should probably not use if you don't have a really good
reason. You might be better of [creating your own image](../adding-images)

Is there any images that you think we should add don't hesitate contacting
servicedesk@csc.fi

### cirros
This is a really small image which can be used to boot instance really fast.
This can be useful to doing tests in Pouta, like does the network work or
how fast can one launch an instances. You should not use these for long
times and you should always delete the instance when you don't need it
anymore. There are very little reason for using this image and if you are
unsure CentOS and Ubuntu are 98% of the time a better choice.

### Ubuntu-14.04
Ubuntu-14.04 has been end of life for some time we have not gotten around
to remove it since we have not noticed since we are usually only using
CentOS-7.

### Fedora-Atomic-25
You probably don't want to use this if you are not sure. We will most likely
remove this image in the near future since it is getting quite out of date.

[GitHub page]: https://github.com/CSC-IT-Center-for-Science/diskimage-builder-csc-automation

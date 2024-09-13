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
|CentOS-9-Stream |**cloud-user** |no  |
|AlmaLinux-8     |**almalinux**  |no  |
|AlmaLinux-9     |**almalinux**  |no  |
|Ubuntu-18.04    |**ubuntu**     |no  |
|Ubuntu-20.04    |**ubuntu**     |no  |
|Ubuntu-22.04    |**ubuntu**     |no  |
|Ubuntu-24.04    |**ubuntu**     |no  |

### CentOS-9-Stream

The CentOS community is now actively maintaining CentOS-9-Stream, which is the upstream branch for RHEL.
Given that updates and changes are first tested in CentOS and only subsequently deployed for Red Hat Enterprise Linux (RHEL), the resulting operating system is possibly less stable compared to its previous version, i.e., when RHEL was the upstream for CentOS.
The CentOS community [emphasizes](https://blog.centos.org/2020/12/future-is-centos-stream/)
that the Stream version is nevertheless extremely close in terms of stability
to the corresponding RHEL version.
Note that this is the upstream version of the image, i.e., we do not perform
any change to the image before making it available on our services. The default
username is `cloud-user`.

### AlmaLinux-8 and AlmaLinux-9

AlmaLinux is a linux distribution created in response to the termination
of CentOS-8 project and the fundamental change of CentOS building process, due
to which CentOS' traditional stability was impacted. AlmaLinux aims to be fully
binary-compatible with RedHat Enterprise Linux, and by doing so the linux
distribution effectively takes the role that CentOS used to have before the
switch to the -Stream versions. Note that these are the upstream versions of the
AlmaLinux images, and their default username is `almalinux` instead of `cloud-user`.

### Ubuntu-24.04, 22.04, 20.04 and 18.04 LTS
Some like chocolate, some like strawberry. This is the choice for those that
do not want to use CentOS. Note that these are the upstream versions of the
Ubuntu images, and their default username is `ubuntu` instead of `cloud-user`.

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

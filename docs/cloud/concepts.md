# Concepts of cloud computing

This document introduces some terminology and how cloud resources
differ from traditional HPC.
**cPouta** is an  *Infrastructure as a Service* (IaaS)  cloud. In IaaS
cloud environments,  users can quickly  setup virtual machines  with a
set  amount of  resources,  attach  various types  of  storage to  the
machines and  connect them using  virtual networks. The user  does not
need to  buy hardware,  network it and  install operating  systems, as
this has  already been  handled by  the cloud  administrators.

[TOC]

## Comparing the cloud to traditional hosted services

Traditional  hosted  services  typically  rely   on  a  set  of  fixed
resources.  Users  get access to physical  servers, firewalls, storage
and so  on, or a virtualized  representation of the same.   Storage in
hosted services is provided by onboard disks, disk arrays or a Storage
Area Network  (SAN) depending on performance,  multi-tenancy or backup
requirements. Quite often hosted services utilize proprietary software
for  specialized tasks  such as  live migration  or live  backups, and
resiliency is  provided by duplicating  or clustering each  element so
the  service  can do  failover  to  the  remaining healthy  ones  when
disaster strikes. Often this simply means physical level redundancy: A
new box will claim the responsibility  of the old one. This happens in
addition  to the  redundancy  on other  levels  e.g.  multiple  disks,
multiple  network links  and so  on.  In  other words  everything from
individual elements  of the hosting  infrastructure to the  hosts that
end users are running are considered - if not irreplaceable - at least
precious. In  terms of  scaling the end  user application  or service,
growth in  utilization is  typically projected  for longer  periods of
time such as  months or years, and extensions in  capacity are planned
based on these projections.

In contrast, applications or services running on top of cloud IaaS are
almost designed from the very premise that any or all of the hosts can
fail at any time. If this occurs, new hosts are simply built on demand
to  replace the  old  ones,  drawing from  what  can  be considered  a
semi-infinite pool of  resources. Every possible element  of the cloud
service  is  typically  virtualized   so  dependencies  to  bare-metal
components are minimized. The storage backend of a cloud service needs
to provide a good amount of  I/O per second (IOPS), resiliency against
failures,  as well  as good  scalability  whenever there  is a  sudden
increase in demand.  Traditional storage solutions may  not meet these
requirements  so  new  types  of Open  Source  Storage  solutions  are
increasingly  used  for  cloud  storage,  allowing  use  of  commodity
hardware and a mix between  various hardware vendors. Features such as
live  migration support  are often  directly  built in  to these  open
solutions.

Cloud  services also  utilize many  forms of  Configuration Management
(CM).   Of  course,  CM  can  also be  used  with  traditional  hosted
services,  but operating  a  cloud service  almost  mandates that  the
underlying  system  configurations  are   stored  and  utilized  in  a
consistent manner. This  goes for any application or  service that the
user  is operating,  too.  Once a  configuration of  any  part of  the
service is written  down with a CM tool of  choice, that configuration
can be replicated  to any number of additional nodes  or promptly used
when  rebuilding  a  faulty  one.   Furthermore,  this  decouples  the
replaceable from the irreplaceable very effectively. Frontend servers,
application servers, caches and so  on can always be rebuilt utilizing
CM, but databases  and other elements where state and  data are stored
can't. So while working in a cloud mindset it certainly becomes easier
to  recover a  system  by rebuilding  most parts  of  it, any  element
holding  irreplaceable  information  should  still  be  backed  up  to
external systems and protected against failure.

In terms of scaling, a good way to operate services in the cloud is to
set a baseline  capacity (X load balancers, Y web  servers, Z database
servers...) and  increase it based  on trending demand. This  goes for
scaling  the  system  down,  too. Whenever  cloud  resources  are  not
required, the proper thing to do is to destroy them, freeing resources
to the pool. In this way scaling  a user application or service in the
cloud is much different than  with traditional hosted services, but it
also  adds to  the  benefit  of the  user  since  by terminating  idle
instances they are consuming less Billing Units for idle cycles.

## Comparing the cloud to traditional HPC environments

A comparison against the  traditional HPC (High-Performance Computing)
services that CSC also provides is presented in the following table.

Comparing the cloud to traditional HPC environments:

|                                | Traditional HPC environment                                                                                            | Cloud environment virtual machine                                                                |
|--------------------------------|------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| Operating system               | Same for all: CSC's cluster OS                                                                                         | Chosen by the user                                                                               |
| Software installation          | Done by cluster administrators, customers can only install software to their own directories, no administrative rights | Installed by the user, the user has admin rights                                                 |
| User accounts                  | Managed by CSC's user administrator                                                                                    | Managed by the user                                                                              |
| Security e.g. software patches | CSC administrators manage the common software and the OS                                                               | User has more responsibility: e.g. patching of running machines                                  |
| Running jobs                   | Jobs need to be sent via the cluster's Batch Scheduling System (BSS)                                                   | The user is free to use or not use a BSS                                                         |
| Environment changes            | Changes to SW (libraries, compilers) happen.                                                                           | The user can decide on versions.                                                                 |
| Snapshot of the environment    | Not possible                                                                                                           | Can save as a Virtual Machine image                                                              |
| Performance                    | Performs well for a variety of tasks                                                                                   | Very small virtualization overhead for most tasks, heavily I/O bound and MPI tasks affected more |


## cPouta related terms and concepts

#### OpenStack

<a href="http://www.openstack.org/"
class="external-link">OpenStack</a> is  the free open  source software
that has been  used to build the cPouta cloud  environment.  It offers
components   for   managing   virtual  machines   (*Nov*a),   networks
(*Neutron*), identity (*Keystone*),  virtual machine images (*Glance*)
and  persistent  volume  storage  (*Cinder*).  There  is  also  a  web
interface for managing most of the other components (*Horizon*).

**Infrastructure-as-a-Service (IaaS)**

IaaS  provides users  with virtualised  servers, storage  and networks
through  a self-service  interface. Users  have flexibility  to choose
many  aspects of  their environment,  but they  must also  support the
operating system, middleware, software and data themselves.

![cloud-stack][cloud-stack]

Industry  standard definition IaaS and  the other cloud terms.

#### Platform-as-a-Service (PaaS)

PaaS provides  a higher level service  to users, but with  less choice
about the  underlying platform. CSC's  regular HPC service  (i.e. Mahti
and Puhti)  is   in  some   ways  PaaS 
although HPC  applications typically use  a very
wide  mixture  of  interfaces,  non-standard API's  and  command  line
tools. Mainstream  PaaS providers offer  a framework which  provides a
documented common API for all aspects of the service.

#### Software-as-a-Service (SaaS)

In SaaS applications are delivered  over the Internet.  There are many
examples of  this in common  use including  web based email  and cloud
file  storage.   An  example  of  SaaS from  CSC  would  be  the  **<a
href="http://chipster.csc.fi"     class="external-link">Chipster</a>**
analysis software for high-throughput data. Chipster is an easy to use
graphical interface  that contains  over 240  analysis tools  for next
generation sequencing (NGS), microarray and proteomics data.

#### Virtual machine

A virtual machine  is a computer simulated in software  that runs as a
process on a host  machine. It exposes a part of  the resources of the
underlying machine to a guest  operating system. This approach is more
flexible compared  to using just  physical servers, as a  single large
physical  server  can be  partitioned  into  isolated smaller  virtual
machines.

#### Virtual network

One  or   more  virtual  networks   can  run  on  the   same  physical
network. This  helps prevent  users from  seeing each  others' network
traffic in a shared infrastructure.  In IaaS services virtual networks
are assigned to specific users or  groups of users to provide security
and ensure fair use of shared network links.

#### Virtual machine image

A large  file containing a  complete state  of a virtual  machine. The
majority of a virtual machine image  is the simulated hard disk of the
virtual machine. As such virtual machine images vary in size depending
on  the  configuration  of  the  virtual  machine  and  the  installed
applications.   Virtual  machine images  are  the  starting point  for
creating  new  virtual  machines  and   they  can  be  easily  cloned,
snapshotted, backed up and managed.

  [cloud-stack]: /img/cloud-stack.png

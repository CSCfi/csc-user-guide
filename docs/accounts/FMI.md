## Puhti FMI partition specific instructions

The Puhti FMI partition is available only for users from FMI using projects with access to it. The FMI users, however, can also use the general Puhti system and CSC's other services using normal CSC projects.


### Projects: Puhti-FMI vs. Puhti and CSC:s other services

A project can only use either the FMI partition or the general partition and CSC's other services, not both. That is, a project can have *either*
* Puhti-FMI (and optionally Allas when it becomes available) 
*or* (this is an exclusive or)
* e.g Puhti and cPouta (or any other service available for all research institute projects) and *not* Puhti-FMI

as included services.Hence, if an FMI project manager wants use both the general partition/CSC's other services and the FMI partition, he or she must create separate projects.

However, all the data is available across the projects.

A project for the general partition and CSC's other services is created as described in [Creating new project](https://docs.csc.fi/accounts/creating-new-project/) page. For project type please choose Academic and add Puhti and/or other services as needed as described in [Adding service access for project](https://docs.csc.fi/accounts/adding-service-access-for-project/) page.

A project for the FMI partition is created similarly, but for the service Puhti-FMI is chosen. 

For the time being, an additional step is required: The project manager must send an email with the project identifying number to servicedesk@csc.fi and ask that Puhti-FMI is added to the project. Jobs can be submitted to the FMI partition only after servicedesk has confirmed the access.

### Puhti FMI partition

Puhti FMI partition comprises of an additional 240 nodes with 192 GB of memory. These are on top of those listed in [system description](../computing/system.md). The nodes have identical specifications as the normal nodes in Puhti.

### Storage areas

FMI partition projects can access the /fmi/ folder in puhti. This folder has a global quota of 750 TiB. 

### Usage

At the moment the fmi partition is acceessed using the normal puhti login nodes. This is a temporary solution, before the puhti-fmi login node is installed.

Puhti usage is similar to the normal Puhti system, the main difference is that fmi projects use the fmi partition instead of the normal partitions (small, large, etc.).



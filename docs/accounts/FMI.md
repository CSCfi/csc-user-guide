## Puhti FMI partition specific instructions

The Puhti FMI partition is available only for users from FMI using projects with access to it. The FMI users, however, can also use the general Puhti system and CSC's other services using normal CSC projects.


### Projects: Puhti-FMI vs. Puhti and CSC:s other services

A project can only use either the FMI partition or the general partition and CSC's other services, not both. That is, a project can have **either**
* Puhti-FMI (and optionally Allas when it becomes available) 

**or** (this is an exclusive or)
* e.g Puhti and cPouta (or any other service available for all research institute projects) and **not** Puhti-FMI

as included services. Hence, if an FMI project manager wants use both the general partition/CSC's other services and the FMI partition, he or she must create separate projects.

However, all the data is available across the projects.

A project for the general partition and CSC's other services is created as described in [Creating new project](https://docs.csc.fi/accounts/creating-new-project/) page. For project type choose Academic and add Puhti and/or other services as needed as described in [Adding service access for project](https://docs.csc.fi/accounts/adding-service-access-for-project/) page.

A project for the FMI partition is created similarly, but for the service Puhti-FMI is chosen. 

For the time being, an additional step is required: The project manager must send an email with the project identifying number to servicedesk@csc.fi and ask that Puhti-FMI is added to the project. Jobs can be submitted to the FMI partition only after servicedesk has confirmed the access.

### Puhti FMI partition

Puhti FMI partition comprises of an additional 240 nodes with 192 GB of memory. These are on top of those listed in [system description](../computing/system.md). The nodes have identical specifications as the normal nodes in Puhti. There are two queues on the FMI partition: `fmi` and `fmi_test`. The maximum job size for `fmi` is 100 nodes with a maximum runtime of 6 days and the maximum job size for `fmi_test` is 2 nodes with a maximum runtime of 30 minutes.   

### Storage areas

FMI partition projects can access the `/fmi/` folder in Puhti. This folder has a global quota of 750 TiB. Project folders for FMI projects are located at
`/fmi/projappl/<projectname>` and `/fmi/scratch/<projectname>` respectively. The command `csc-workspaces` can be used to list the project folders. The global quota is divided 
between __projappl__ and __scratch__ as follows: 
```text
/fmi/projappl    50 TiB
/fmi/scratch    700 TiB
```

!!! Note
    All FMI project share the same global quota and should therefore strive to keep up to good practice in data storage.
    Per project usage will be tracked, and per project quotas may be imposed at a later date.


**A cleaning script is run periodically on `/fmi/scratch`. The cleaning removes any unused files older than 90 days.** 

### Usage

At the moment the fmi partition is acceessed using the normal puhti login nodes. This is a temporary solution, before the puhti-fmi login node is installed.

Puhti usage is similar to the normal Puhti system, the main difference is that fmi projects use the `fmi` and `fmi_test` partitions instead of the normal partitions (small, large, etc.).



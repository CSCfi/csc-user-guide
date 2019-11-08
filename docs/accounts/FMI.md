## Specific instructions for the Puhti FMI partition 

The Puhti FMI partition is only available for FMI users in projects that have been granted access. FMI users can also use the general Puhti system and CSC's other services using normal CSC projects.


### Projects: Puhti FMI vs. Puhti and CSC's other services

A project can only use either the FMI partition or the general partition and CSC's other services, not both. That is, a project can have **either**

* Puhti FMI (and optionally Allas) 

**or** (this is an exclusive or)

* e.g Puhti and cPouta (or any other service available for all research institute projects) and **not** Puhti FMI

as the included services. Hence, if a FMI project manager wants use both the general partition/CSC's other services and the FMI partition, they must create separate projects.

However, all data is available across the projects.

A project for the general partition and CSC's other services is created as described in [Creating new project](how-to-create-new-project.md) page. As the project type, choose _Academic_ and add Puhti and other services as needed as described in [Adding service access for project](how-to-add-service-access-for-project.md).

A project for Puhti FMI partition is created similarly by choosing _FMI_ as the project type. Only Puhti FMI, Allas and IDA are available as services for FMI projects.

### Puhti FMI partition

The Puhti FMI partition comprises an additional 240 nodes with 192 GB of memory. These are on top of those listed in the [system description](../computing/system.md). The nodes have specifications identical to the regular nodes in Puhti. There are two queues in the FMI partition: `fmi` and `fmi_test`. The maximum job size for `fmi` is 100 nodes with a maximum runtime of six days. The maximum job size for `fmi_test` is two nodes with a maximum runtime of 30 minutes.

### Storage areas

The FMI partition projects can access the `/fmi/` folder in Puhti. This folder has a global quota of 750 TiB. The project folders of the FMI projects are located in `/fmi/projappl/<projectname>` and `/fmi/scratch/<projectname>` respectively. The command `csc-workspaces` lists the project folders. The global quota is divided 
between __projappl__ and __scratch__: 
```text
/fmi/projappl    50 TiB
/fmi/scratch    700 TiB
```

!!! Note
    All FMI projects share the same global quota and should therefore strive to good practices in data storage.
    Per project usage is tracked, and per project quotas may be imposed at a later date.

**A cleaning script is run periodically on `/fmi/scratch`. The cleaning removes any unused files older than 90 days.** 

### Usage

The FMI partition is accessed using regular Puhti login nodes. This is a temporary solution before the Puhti FMI login node is installed.

Puhti FMI works similarly to the regular Puhti system, the main difference being that FMI projects use the `fmi` and `fmi_test` partitions instead of the regular partitions (small, large, etc.).

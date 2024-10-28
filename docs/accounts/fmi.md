# Specific instructions for the Puhti FMI partition

The Puhti FMI partition is only available for FMI users in projects that have been granted access. FMI users can also use the general Puhti system and CSC's other services using normal CSC projects.


## Projects: Puhti FMI vs. Puhti and CSC's other services

A project can only use either the FMI partition or the general partition and CSC's other services, not both. That is, a project can have **either**

* Puhti FMI (and optionally Allas)

**or** (this is an exclusive or)

* e.g Puhti and cPouta (or any other service available for all research institute projects) and **not** Puhti FMI

as the included services. Hence, if a FMI project manager wants use both the general partition/CSC's other services and the FMI partition, they must create separate projects.

However, all data is available across the projects.

A project for the general partition and CSC's other services is created as described in [Creating new project](how-to-create-new-project.md) page. As the project type, choose _Academic_ and add Puhti and other services as needed as described in [Adding service access for project](how-to-add-service-access-for-project.md).

A project for Puhti FMI partition is created similarly by choosing _FMI_ as the project type. Only Puhti FMI and Allas are available as services for FMI projects.

## Puhti FMI partition

The Puhti FMI partition comprises an additional 240 nodes with 192 GB of memory. These are on top of those listed in the [system description](../computing/systems-puhti.md). The nodes have specifications identical to the regular nodes in Puhti. There are two queues in the FMI partition: `fmi` and `fmitest`. The maximum job size for `fmi` is 100 nodes with a maximum runtime of six days. The maximum job size for `fmitest` is two nodes with a maximum runtime of 30 minutes.

## Storage areas

The FMI partition projects can access the `/fmi/` folder in Puhti. This folder has a global quota of 750 TiB. The project folders of the FMI projects are located in `/fmi/projappl/<projectname>` and `/fmi/scratch/<projectname>` respectively. The command `csc-workspaces` lists the project folders. The global quota is divided
between __projappl__ and __scratch__:
```text
/fmi/projappl   150 TiB
/fmi/scratch    600 TiB
```

!!! Note
    All FMI projects share the same global quota and should therefore strive to good practices in data storage.
    Per project usage is tracked. If you need to adjust your FMI project quotas, please contact Lasse Jalava (CC Matti Keränen) at FMI either with email or in FMI's Slack channel 'fmi-computing'.

**A cleaning script is run periodically on `/fmi/scratch` (FMI projects) the same way as on `/scratch` (Academic projects). The cleaning removes any unused files older than 180 days. You can ask for white listing your project's `/fmi/scratch` directory. Automatic cleaning is convenient, so ask white listing only if really necessary.**

## Usage

The FMI customers can use both the regular Puhti login nodes `puhti.csc.fi`, and FMI specific login nodes `puhti-login1.fmi.fi` and `puhti-login2.fmi.fi`.

Puhti FMI works similarly to the regular Puhti system, the main difference being that

1. the FMI projects use the `fmi` and `fmitest` partitions instead of the regular partitions (small, large, etc.),
2. the FMI login nodes are networked through FMI's internal network, making network access somewhat different, and
3. the FMI compute nodes have simultaneous multithreading (SMT/hyper threading) enabled, thus most tools, such as `htop`,
   show 80 logical cpus instead of 40, `seff` CPU efficiency report is computed with 80 logical cpus, etc. The configuration
   and the usage is similar to Mahti, see
   [Hybrid jobs with SMT](/computing/running/creating-job-scripts-mahti/#hybrid-batch-jobs-with-simultaneous-multithreading-smt).

In addition to the regular CSC's user support, [servicedesk@csc.fi](mailto:servicedesk@csc.fi), FMI specific support is available in the internal wiki pages [FMI Puhti Guide](https://wiki.fmi.fi/display/VTUKI/FMI+Puhti+guide), and in the very active FMI's Slack channel 'fmi-computing'.

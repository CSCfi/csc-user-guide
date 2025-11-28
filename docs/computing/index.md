# Overview

!!! warning "Puhti and Mahti retirement in 2026"
    Puhti and Mahti will be decommissioned in 2026 and replaced by Roihu, CSC's
    next-generation supercomputer offering enhanced performance and
    capabilities.

    * Puhti computing services will be shut down one month after Roihu general
      availability in spring 2026.
    * Puhti storage will remain accessible at least until the end of June 2026.
    * Mahti will be shut down in August 2026.

    [Learn more about Roihu :material-arrow-right:](systems-roihu.md)

Puhti and Mahti are CSC's supercomputers. Puhti has been available for CSC users
since 2 September 2019 and Mahti has been available since 26 August 2020. LUMI is
one of the pan-European pre-exascale supercomputers, located in CSC's data
center in Kajaani. The CPU partition of LUMI (LUMI-C) has been available since
early 2022, and the full system with the large LUMI-G partition has been available since early 2023.

Puhti contains CPU nodes with a range of memory sizes as well as a large GPU
partition (Puhti AI), while Mahti contains homogeneous CPU nodes and is meant
for larger jobs (minimum 128 CPU-cores). Mahti also contains a GPU partition
since 2021 (Mahti AI) with Nvidia Ampere GPUs. See [specifications](available-systems.md)
for details on the systems and [this page for an outline of differences between LUMI-C and
Mahti](lumi-vs-mahti.md).

Puhti and Mahti will be replaced in 2026 by CSC's next national supercomputer
called **Roihu**. [Read more about Roihu here](systems-roihu.md).

CSC supercomputers use the Linux operating system and we recommend that you are familiar with
basics of [Linux command line usage](../support/tutorials/env-guide/index.md) before starting.

!!! note
    For an overview of the LUMI supercomputer, see
    [the LUMI documentation](https://docs.lumi-supercomputer.eu/hardware/).


## Accessing Puhti and Mahti

To be able to use CSC's supercomputers, you need to have a CSC user account that
belongs to a computing project which has access to the respective supercomputers.
CSC user accounts and projects are managed in the [MyCSC portal](https://my.csc.fi).
Further instructions are provided in the [Accounts section](../accounts/index.md)
of this user guide.

!!! Note
    To access the LUMI supercomputer, you need to [create a LUMI-specific
    project](../accounts/how-to-create-new-project.md#creating-a-lumi-project-and-applying-for-resources).
    For more details on getting started with LUMI, see the [LUMI
    documentation](https://docs.lumi-supercomputer.eu/firststeps/getstarted/).

## Connecting to the supercomputers

--8<-- "auth-update-ssh.md"

Connect using an SSH client:

```bash
ssh yourcscusername@puhti.csc.fi
```

or

```bash
ssh yourcscusername@mahti.csc.fi
```

This will connect you to one of the login nodes. If you need to connect
to a specific login node, use the command:

```bash
ssh yourcscusername@puhti-login[11-12,14-15].csc.fi
```

or

```bash
ssh yourcscusername@mahti-login[11-12,14-15].csc.fi
```

Where `yourcscusername` is the username you get from CSC.

For more details, see the [connecting](connecting/index.md) page.

Puhti and Mahti can also be accessed via their respective
[web interfaces](webinterface/index.md) available at
[www.puhti.csc.fi](https://www.puhti.csc.fi) and
[www.mahti.csc.fi](https://www.mahti.csc.fi).

### Scalability

Don't allocate more resources to your job than it can use efficiently. This
needs to be verified for each new code and job type (different input) by a
scaling test. The policy is that the job should be **at least 1.5 times faster**
when you double the resources (cores). [Instructions for performing a scalability
test](../support/tutorials/cmdline-handson.md#scaling-test-for-an-mpi-parallel-job).
Please also consider [other important factors related to performance.](performance.md)

## Projects and quotas

Working in CSC supercomputers is based on projects. The computing and storage
resources are allocated to projects and when you start a batch job, you must
always define the project that the job belongs to.

Projects are managed in the [MyCSC portal](https://my.csc.fi), where you can add
services, resources and users to your CSC projects.

In CSC supercomputers, you can check your currently active projects with the
command:

```text
csc-projects
```

This command shows information for all your CSC projects. You can select just
one project to be reported with the `-p` option. For example:

```bash
[kkayttaj@puhti-login11 ~]$ csc-projects -p project_2012345
-----------------------------------------------------------------
Project: project_2012345        Owner: Kalle Käyttäjä
Title: "Ortotopology modeling"
Start: 2019-08-20 End: 2029-10-23 Status: open
Billing units      Budget        Used      Remain
-------------      ------        ----      ------
CPU BU:             60000          20       59980
GPU BU:              1000          30         970
Storage BU:        300000          40      299960
Cloud BU:             400          10         390
Latest resource grant: 2025-01-31
-----------------------------------------------------------------
Project info updated: 2025-09-02 15:12
```

The command reports the owner of the project, title, start and end dates. In
addition the command prints out the budgeting information for the project: how
many Billing Units of each type have been granted to your project, how many have
been used and how many still remain.

The [disk areas](disk.md) of your projects can be checked with the command:

```text
csc-workspaces
```

## Using Puhti and Mahti

* [Systems](available-systems.md): What computational resources are available
* [Usage policy](usage-policy.md): Usage policy of CSC supercomputers
* [Connecting](connecting/index.md): How to connect to  CSC supercomputers
* [Puhti web interface](webinterface/index.md): How to connect to Puhti using the web
  interface
* [Disk areas](disk.md): What places are there for storing data on CSC
  supercomputers
* [Modules](modules.md): How to find the programs you need
* [Applications](../apps/index.md): Application specific instructions.
* [Running jobs](running/getting-started.md): How to run programs on the
  supercomputers
* Installing and compiling your applications:
    * [Installing software](installing.md)
    * [Compiling on Puhti](compiling-puhti.md)
    * [Compiling on Mahti](compiling-mahti.md)
* [Debugging applications](debugging.md): How to debug your applications
* [Performance analysis](performance.md): How to understand the performance of
  your applications

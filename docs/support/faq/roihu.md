# Frequently asked questions about Roihu

[TOC]

## 1. When will Roihu be available?

Installation of new supercomputers is a complex process. Thus, it is hard to
provide an exact date for when Roihu will be generally available.

The Roihu pilot phase started in April 2026. The
general availability of the system should happen around end of June 2026.
Please observe that delays are still possible.

[Read more about the tentative schedule here](../../computing/systems-roihu.md#schedule).

## 2. When will Puhti/Mahti be shut down?

Puhti compute resources will be shut down one month after Roihu general
availability, by 31 July 2026. After this, jobs can no longer be submitted on
Puhti. Puhti storage and login nodes are planned to remain accessible until
15 October 2026.

Mahti compute resources will be shut down on 31 August 2026. Mahti storage and
login nodes are planned to remain accessible until 15 October 2026.

We strongly encourage users to move any required data by the end of August
2026, as Mahti and Puhti storage services will not be covered by service contracts between
September and October, and availability cannot be fully guaranteed.

[Read more about the tentative schedule here](../../computing/systems-roihu.md#schedule).

## 3. I heard that Puhti will be donated for continued use. Can I apply for hardware?

Individual researchers or research groups cannot apply for Puhti hardware.
Instead, CSC has directly contacted organizations in scope of
[CSC's free-of-charge use policy](https://research.csc.fi/free-of-charge-use),
i.e. Finnish universities, universities of applied science, and state research
institutes, with the details on how they may apply for Puhti hardware. Notably,
each organization may only submit at most one (1) application.

The deadline for the applications was in March 2026.

## 4. Will current CSC accounts and projects be automatically migrated to Roihu? How do I add Roihu as a service?

CSC accounts and projects are not tied to specific services. In other words,
the same CSC account and projects can be used for different CSC services,
including Roihu.

Once Roihu is available, you can add it as a service to your existing project(s) in MyCSC, similarly to Puhti or Mahti.
The existing billing units can be used on Roihu. Scratch/projappl space will be available there automatically, but data is NOT transferred automatically.

To be able to use Roihu, you will need to
[add Roihu service access for your project](../../accounts/how-to-add-service-access-for-project.md).

Additionally, you should have at least a **medium** level of identity assurance
(LoA) to be able to access Roihu, i.e., you need to have been authenticated with strong authentication.
You can view your current level of identity
assurance in [MyCSC](https://my.csc.fi) (select _Profile_ and scroll down to
_Level of Identity Assurance_).

Users with no or low LoA should read the
[instructions on how to elevate their assurance level](../../accounts/strong-identification.md).

## 5. Will existing disk quota extensions on Puhti/Mahti automatically apply on Roihu as well?

No, all projects will start with default quotas. Any quota extensions must be
applied for separately and the needs properly motivated.

Storage BUs from an existing project can be used, when you add Roihu as a service into that project.

The default disk quotas in Roihu are as follows:

|            |Capacity|Number of files|
|------------|--------|---------------|
|**home**    |15 GiB  |150 000 files  |
|**projappl**|15 GiB  |150 000 files  |
|**scratch** |250 GiB |500 000 files  |

Do note that the default quotas in Roihu are more restrictive than on Mahti and Puhti. Only apply for more quota if you strictly need to.

See documentation on [increasing disk quotas.](../../computing/disk.md#increasing-quotas)

## 6. Will users' data be automatically migrated to Roihu? How should I migrate my data from Puhti/Mahti?

No, users will have to move their data to Roihu themselves, if needed.

With data migration, the main take-home message of the guide is to only move
data that you truly need. Dumping everything from Puhti and/or Mahti scratch to
Roihu "just in case" is not acceptable. Roihu will implement a similar data
cleanup cycle as Puhti and, as stated above, prior quota extensions on Puhti
and/or Mahti will not be carried over to Roihu.

Migration of data should primarily happen directly from Puhti/Mahti to Roihu, between July and August 2026.
Mahti and Puhti storage will be fully shut down 15 October 2026.

You can already familiarize yourself with the [data migration guide](https://csc-guide-preview.2.rahtiapp.fi/origin/roihu/support/tutorials/roihu-data/#14-transfer-your-data-directly-from-puhtimahti-to-roihu), before Roihu becomes available.

Short talk: Roihu data migration tips:

* [Slides](https://kannu.csc.fi/s/2ezpNEC77H4SttC)
* [Recording](https://video.csc.fi/media/t/0_9ylmo5py)

## 7. What kind of hardware will Roihu have?

The Roihu system is described in detail
[here](../../computing/systems-roihu.md).

Notably, Roihu will have different CPU architectures on the AMD Turin-based CPU
nodes (x86) and NVIDIA Grace-Hopper GH200-based GPU nodes (ARM). Accordingly,
there will also be two different login node flavors for users targeting the CPU
or GPU partitions, respectively:

* `roihu-cpu.csc.fi` (x86, AMD Turin), and
* `roihu-gpu.csc.fi` (ARM, NVIDIA Grace)

Software built on the x86 login nodes will only run on the CPU compute nodes,
while software built on the ARM login nodes will only run on the GPU nodes.
Similarly, CPU and GPU Slurm jobs can only be submitted from the x86 and ARM
login nodes, respectively.

## 8. What operating system will Roihu have?

The operating system of Roihu will be Red Hat Enterprise Linux (RHEL) 9.

## 9. Will Roihu have pre-installed applications available like Puhti and Mahti?

Yes, we intend to provide a comprehensive pre-installed stack of scientific
software on Roihu like we currently do on Puhti and Mahti. However, please note
that some older and less used module versions may be deprecated.

As before, missing software can be requested to be installed by CSC, and if
there is enough demand, we will consider creating a system-wide installation.
We cannot, however, promise to install everything that users might want.

## 10. Will Tykky be available on Roihu?

Yes, [Tykky](../../computing/containers/tykky.md) (tool for creating
containerized Conda etc. environments with wrapper scripts) will also be
available on Roihu.

## 11. Will there be a web interface for Roihu like Puhti and Mahti have?

Yes. The Roihu web interface will provide easy access to the computing and
storage resources of Roihu. Like the current web interfaces, the Roihu web
interface will be particularly aimed at interactive workloads and running
graphical applications like Jupyter Notebooks, RStudio, etc.

Roihu web interface will become available at www.roihu.csc.fi, similarly to Mahti, Puhti and LUMI.

See documentation on the [web interface](../../computing/webinterface/index.md).

## 12. Sensitive data and Roihu: What is the Roihu-integration with SD Desktop and how will it work?

Roihu will eventually support a secure workflow for sensitive data processing. The technical implementation will include the capability to submit jobs from the SD Desktop to Roihu. However, setting up the workflow specific for secure sensitive data processing service for Roihu will take several months. As a result, this functionality is expected to become available only towards the end of 2026 or the beginning of 2027.

## 13. Do I need to migrate data from Allas to Roihu?

Allas is not affected in this update. You can keep your current data there.
If you have your data in Allas, you can access that data from Roihu too. That data does not need to be migrated, as Allas service will stay available also after Roihu comes.

It is not recommended to transfer data to from Mahti/Puhti to Roihu via Allas or your local workstation. Instead, CSC recommends using command-line based tools such as [`rsync`](https://csc-guide-preview.2.rahtiapp.fi/origin/roihu/support/tutorials/roihu-data/#2-recommended-data-migration-methods)
to directly transfer data from Puhti/Mahti/LUMI to Roihu.

## 14. Is it fine to run the rsync on login nodes, or should we use the computation nodes to do the transfer?

It is ok to use rsync on the Mahti/Puhti login nodes. Please read the [data migration guide](https://csc-guide-preview.2.rahtiapp.fi/origin/roihu/support/tutorials/roihu-data/#14-transfer-your-data-directly-from-puhtimahti-to-roihu)
carefully, and consider compressing your data before transferring it, to save time and resources
used in the migration. Only move data that you truly need.

## 15. Will logging in to Roihu be different than for Puhti/Mahti?

In addition to SSH keys, a signed SSH certificate is required to connect to Roihu over SSH.

[Read the instructions for getting and using SSH certificates here](https://csc-guide-preview.2.rahtiapp.fi/origin/roihu/computing/connecting/ssh-keys/#signing-public-key).

Short talk: SSH authentication changes to Roihu

* [Slides](https://a3s.fi/media/SSH_CA_USER_COFFEE-20260422.pdf)
* [Recording](https://video.csc.fi/media/t/0_el9fzv7f)

Roihu will also support a web interface for connecting, similarly to Mahti and Puhti, at www.roihu.csc.fi.

## 16. Is there a list of pre-installed software/modules available?

The target is to provide the same software as on Puhti and Mahti as far as possible.
Some commercial software for which the vendor does not provide ARM (aarch64) support will not work on the Roihu GPU side as it uses the NVIDIA Grace ARM CPUs.
Examples of such software that have previously been installed on Puhti/Mahti include Desmond and CryoSPARC.
We're working to provide alternative ways for users to use those software. 

The goal is to have similar module support as in Puhti and Mahti, with some necessary changes in e.g.
version numbers of some supported applications and modules.
Some modules will change names, for example pytorch → python-pytorch.

A list of installed software is not yet available in the documentation, but will be added at Roihu's general availability.

## 17. Will Roihu partitions have the same memory/time limits as on Mahti and Puhti?

There will be some changes in the available partition names and the corresponding hardware. You can already see the available partitions and the corresponding limits in the [work in progress documentation for Roihu](https://csc-guide-preview.2.rahtiapp.fi/origin/roihu/computing/running/batch-job-partitions/#roihu-partitions).

## 18. Will Roihu have a longrun partition? What will be the maximum runtime?

There will be a longrun partition on Roihu. The maximum time for a job in the Roihu longrun partition will be 10 days.
The small partion for partial or single nodes has a time limit of 72 hours.

## 19. I did not find an answer to my question here. Who should I contact?

Please send email to [CSC Service Desk](../contact.md). We are happy to help!

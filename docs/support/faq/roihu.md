# Frequently asked questions about Roihu

[TOC]

## 1. When will Roihu be available?

Installation of new supercomputers is a complex process. Thus, it is hard to
provide an exact date for when Roihu will be generally available.

However, based on the current progress of the installation, CSC estimates that
the Roihu pilot phase will be able to start at the end of March 2026.
Subsequently, the general availability of the system will be at the end of
April 2026. Please observe that delays are still possible.

[Read more about the tentative schedule here](../../computing/systems-roihu.md#schedule).

## 2. When will Puhti/Mahti be shut down?

Puhti compute resources will be shut down one month after Roihu general
availability. This means that jobs can no longer be submitted. The storage
will, however, remain accessible at least until August 2026 to allow sufficient
time for data migration, if needed.

Mahti (both compute and storage) will be shut down in August 2026.

[Read more about the tentative schedule here](../../computing/systems-roihu.md#schedule).

## 3. I heard that Puhti will be donated for continued use. Can I apply for hardware?

Individual researchers or research groups cannot apply for Puhti hardware.
Instead, CSC has directly contacted organizations in scope of
[CSC's free-of-charge use policy](https://research.csc.fi/free-of-charge-use),
i.e. Finnish universities, universities of applied science, and state research
institutes, with the details on how they may apply for Puhti hardware. Notably,
each organization may only submit at most one (1) application.

## 4. Will current CSC accounts and projects be automatically migrated to Roihu?

CSC accounts and projects are not tied to specific services. In other words,
the same CSC account and projects can be used for different CSC services,
including Roihu.

To be able to use Roihu, you will need to
[add Roihu service access for your project](../../accounts/how-to-add-service-access-for-project.md).
Additionally, all users of the project should have at least a **medium** level
of identity assurance (LoA) to be able to access Roihu. You can view your
current level of identity assurance in [MyCSC](https://my.csc.fi) (select
_Profile_ and scroll down to _Level of Identity Assurance_).

Users with no or low LoA should read the
[instructions on how to elevate their assurace level](../../accounts/strong-identification.md).

## 5. Will existing disk quota extensions on Puhti/Mahti automatically apply on Roihu as well?

No, all projects will start with default quotas. Any quota extensions must be
applied for separately and the needs properly motivated.

## 6. Will users' data be automatically migrated to Roihu?

No, users will have to move their data to Roihu themselves, if needed.

To support data migration, CSC will provide a guide for transferring data
efficiently to Roihu. The main take-home message of the guide is to only move
data that you truly need. Dumping everything from Puhti and/or Mahti scratch to
Roihu "just in case" is not acceptable.

Roihu will implement a similar data cleanup cycle as Puhti and, as stated
above, prior quota extensions on Puhti and/or Mahti will not be carried over to
Roihu.

You can already now familiarize with the
[different tools available for moving data to/from/between CSC services](../../data/moving/index.md).

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
there is enough demand, we will consider creating a system-wise installation.
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

## 12. I did not find an answer to my question here. Who should I contact?

Please send email to [CSC Service Desk](../contact.md). We are happy to help!

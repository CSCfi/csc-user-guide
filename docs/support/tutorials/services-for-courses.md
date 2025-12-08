# Using CSC services for courses

CSC services can be used for educational purposes in accordance with our
[free-of-charge use policy](https://research.csc.fi/free-of-charge-use/). This
guide outlines how to organize a course using [Noppe](#noppe) and
[CSC supercomputers Puhti and Mahti](#puhti-and-mahti), including advice on how
to select the right service for your needs.

## Noppe

### Instructions

#### Teacher

#### Student

## Puhti and Mahti

!!! info "Puhti and Mahti will be retired in 2026"
    Puhti and Mahti will be decommissioned in 2026 and replaced by Roihu, CSC's
    next-generation supercomputer offering enhanced performance and
    capabilities. Please take this into account when planning courses for 2026.

    [Learn more about Roihu :material-arrow-right:](../../computing/systems-roihu.md)

### Overview

CSC supercomputers Mahti and Puhti are ideal platforms for organizing courses
that benefit from HPC resources or aim to teach how to use and run computations
on supercomputing platforms. This includes cases where the course participants
need access to GPUs or larger CPU resources, and cases where the existing
software stack is used for the course assignments.

The systems support both traditional command-line
[batch processing compute tasks](../../computing/running/getting-started.md), as well as
web-based tools such as Jupyter Notebooks and RStudio via the
[web interfaces](../../computing/webinterface/index.md). Course organizers are
even able to create customized Jupyter Notebook environments for their course
using the
[Jupyter for Courses](../../computing/webinterface/jupyter-for-courses.md) app.

Please note that courses using CSC supercomputers can have **at maximum 50
students**. Ideally, teachers should target a smaller number of around 25
participants. For larger courses the free resources and allowed resource
reservations may not support the requested amount of users.

!!! warning "Service breaks"
    Please note that the first Tuesday and Wednesday of each month are reserved
    for regular maintenance breaks. You should never rely on the services being
    available on those days.

### Prerequisites

#### Teacher

1. [Create a CSC user account](../../accounts/how-to-create-new-user-account.md).
2. [Create a CSC Course project](../../accounts/how-to-create-new-project.md#course).
3. [Add Puhti and/or Mahti service access to the project](../../accounts/how-to-add-service-access-for-project.md).
4. Invite students to the project either by
    * [using an invitation link](../../accounts/how-to-add-members-to-project.md#using-invitation-link) (recommended)
    * [or directly](../../accounts/how-to-add-members-to-project.md#adding-members-directly).

#### Student

1. [Create a CSC user account](../../accounts/how-to-create-new-user-account.md).
2. Join the course project:
    1. If you've been sent a project invitation link, [accept the invitation in MyCSC](../../accounts/how-to-add-members-to-project.md#member).
    2. If you've been added directly to the course project, no actions are required.

### Advance resource reservation

Course projects are subject to the same Slurm job priority policies as regular
computing projects, meaning that **course participants may need to queue for
resources** if the system is under heavy use. To ensure the availability of
resources at the time of the course session(s), we recommend requesting for an
_advance resource reservation_.

* The resource reservation must be requested **at least 14 days** before
  the start of the course via [CSC Service Desk](../contact.md).
* The request should be motivated and include
    1. the number of participants,
    2. the resources planned for the course,
    3. timetable showing the schedule of the course.
* The maximum amount and type of reservable resources are outlined in the
  table below.

    | System | Approval | CPU limit | GPU limit | Max. daily time window | Max. course days in total |
    |--------|------------------|-------------------|-----------|--------------------|----------------|
    | Puhti  | Automatic | 2 nodes (80 cores) | 0 | 08:00–17:00 | 5 |
    |        | CSC Resource Allocation Group | 5 nodes (200 cores) | 4 nodes (16 GPUs) | Up to 12 hrs (e.g., 08:00–20:00 or 12:00–24:00) | 10 |
    | Mahti  | Automatic | 2 nodes (256 cores) | 14 [GPU slices](../../computing/running/batch-job-partitions.md#gpu-slices) | 08:00–17:00 | 5 |
    |        | CSC Resource Allocation Group | 8 nodes (1024 cores) | 56 [GPU slices](../../computing/running/batch-job-partitions.md#gpu-slices) | Up to 12 hrs (e.g., 08:00–20:00 or 12:00–24:00) | 10 |

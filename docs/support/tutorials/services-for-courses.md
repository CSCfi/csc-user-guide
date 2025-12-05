# CSC Services for Courses

This guide will explain how to use the course project type with CSC's
high-performance computing (HPC) and cloud services.

Staff members from higher education institutions and state research 
institutes can create a MyCSC course project. The procedure is as follows:

   1. Have a [CSC account](../../accounts/how-to-create-new-user-account.md)
   2. Create a [MyCSC course project](../../accounts/how-to-create-new-project.md)
   3. Activate wanted [service](../../accounts/how-to-add-service-access-for-project.md)

!!! tip "Noppe"
    You don't need a MyCSC project to use the Noppe service.
    [Who and how can Noppe be used?](../../cloud/noppe/index.md#who-and-how-can-noppe-be-used)

## Available services

The following services are available to support you in delivering your course.
All services except Noppe require an active MyCSC project with the relevant
service enabled.

Applying for more quota depends on the services; see the
details below. The medium (M) billing unit package is the default package
granted for course projects. This should cover most use cases.

The services are listed in alphabetical order.

### Allas

### cPouta

### Mahti and Puhti (HPC)

!!! info "Next HPC: Roihu"

    CSC's next national supercomputer Roihu, a BullSequana XH3000 hybrid system,
    will replace the Puhti and Mahti supercomputers. More information about
    [Roihu](../../computing/systems-roihu.md).


The course project can host a maximum of 50 students at a time. Please note that
course projects are subject to the same Slurm job priority policies as regular
computing projects, meaning that course participants may need to queue for resources
if the system is under heavy use.

To ensure the availability of resources at the time of the course session(s)
and thus avoid queuing, an _advance resource reservation_ may be requested for
the course. In this case, please
[contact CSC Service Desk](../../support/contact.md) **at least 14 days beforehand**.

The request should be motivated and include:

1. the number of participants,
2. the resources planned for the course,
3. and a timetable showing the schedule of the course.

The guidelines for booking Puhti and Mahti services for a course are given below.

| System | Reservation Type | CPU Limit | Memory per Node | GPU Limit | Daily Time Window | Max Total Days |
|--------|------------------|-----------|------------------|-----------|--------------------|----------------|
| Puhti | Typical | 2 nodes (2×40 cores) | 192 GB | – | 08:00–17:00 | 5 |
| | Maximum | 5 nodes (200 cores) | 192 GB | 4 GPU nodes | Up to 12 hrs (e.g., 08:00–20:00 or 12:00–24:00) | 10 |
| Mahti | Typical | 2 M-nodes (2×128 cores) | 256 GB | 14 GPU slices (1 node) | 08:00–17:00 | 5 |
| | Maximum | 8 M-nodes (8×128 cores) | 256 GB | 28 GPU slices (1 node) | Up to 12 hrs (e.g., 08:00–20:00 or 12:00–24:00) | 10 |

You can find the services' documentation here: [Computing](../../computing/index.md).

### Noppe

### Pukki DBaaS

### Rahti

### SD Desktop



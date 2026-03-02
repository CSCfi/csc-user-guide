---
hide:
  - toc
---

# How to organize a course using CSC resources

CSC services can be used for educational purposes in accordance with our
[free-of-charge use policy](https://research.csc.fi/free-of-charge-use/).

There is a dedicated project category for educational usage – the
[CSC Course project](../../accounts/how-to-create-new-project.md#course). The
maximum lifetime of a CSC Course project, including all its enabled services,
is six months. It is not possible to extend or transfer an existing CSC Course
project.

This guide outlines service-specific details on how to organize courses using
the services in scope of the CSC Course project type:

* [Allas](#allas)
* [cPouta](#cpouta)
* [Puhti & Mahti](#puhti-and-mahti)
* [Pukki](#pukki)
* [Rahti](#rahti)
* [SD Services](#sd-services)

The [Noppe](#noppe) service, using which does not require a CSC project, is
also covered.

If you're unsure which services would be suitable for your course,
[see the table below](#which-services-are-suitable-for-my-course).

## Which services are suitable for my course?

| My course needs ... | [Allas](#allas) | [cPouta](#cpouta) | [Noppe](#noppe) | [Puhti & Mahti](#puhti-and-mahti) | [Pukki](#pukki) | [Rahti](#rahti) | [SD Services](#sd-services) |
|-|-|-|-|-|-|-|-|
| Computing resources | &#10060; | &#9989; | &#9989; | &#9989; | &#10060; | &#9989; | &#9989; |
| **Lots** of computing resources | &#10060; | &#10060; | &#10060; | &#9989; | &#10060; | &#10060; | &#10060; |
| *File* storage resources | &#10060; | &#9989; | &#9989; | &#9989; | &#10060; |  &#9989; | &#9989; |
| *Object* storage resources | &#9989; | &#9989; | &#10060; | &#10060; | &#10060; |  &#9989; | &#9989; |
| A database | &#10060; | &#9989; | &#10060; | &#10060; | &#9989; | &#9989; | &#10060; |
| Access to pre-installed (scientific) software | &#10060; | &#10060; | &#9989; | &#9989; | &#10060; | &#10060; | &#9989; |
| To process or store sensitive data | &#10060; | &#10060; | &#10060; | &#10060; | &#10060; | &#10060; | &#9989; |
| A multipurpose service allowing flexible course setups | &#10060; | &#9989; | &#10060; | &#9989; | &#10060; | &#9989; | &#10060; |
| A purpose-built service focusing on specific use cases | &#9989; | &#10060; | &#9989; | &#10060; | &#9989; | &#10060; | &#9989; |

## Service-specific instructions

=== "Allas"

    !!! info
        Please note that the data will only be available for the duration of
        the CSC Course project.

    [Allas](../../data/Allas/introduction.md) is a Ceph-based object storage
    system. It is designed for storing and sharing large volumes of data. Data
    can be accessed from other CSC services, such as cPouta, Puhti and Mahti,
    or directly via the [Allas web interface](https://allas.csc.fi).

    Data can be accessed using tools and programming languages based on S3 or
    Swift interfaces.

    ## Instructions

    ### Teacher

    1. [Create a CSC user account](../../accounts/how-to-create-new-user-account.md).
    2. [Create a CSC Course project](../../accounts/how-to-create-new-project.md#course).
    3. [Add Allas service access to the project](../../accounts/how-to-add-service-access-for-project.md#project-manager).
    4. If you need to restrict access to data to students only, invite them to
       the project:
        1. [using an invitation link](../../accounts/how-to-add-members-to-project.md#using-invitation-link)
           (recommended)
        2. [or directly](../../accounts/how-to-add-members-to-project.md#adding-members-directly).
    5. Prepare the course content.
        1. [Consult the documentation](../../data/Allas/index.md).
        2. [Contact CSC Service Desk if you need support](../contact.md).

    ### Student

    If the course-related data is not publicly available, but is shared only
    with course project members:

    6. [Create a CSC user account](../../accounts/how-to-create-new-user-account.md).
    7. Join the course project:
        1. If you've been sent a project invitation link,
           [accept the invitation in MyCSC](../../accounts/how-to-add-members-to-project.md#member).
        2. If you've been added directly to the course project, no further
           actions are required to join the course project.
    8. [Accept the relevant terms of service in MyCSC](../../accounts/how-to-add-service-access-for-project.md#member).

=== "cPouta"

    !!! info
        Please note that the resources will only be available for the duration
        of the CSC Course project. Also if each student needs to manage own
        virtual infrastructure, they should create a CSC Student project and
        activate the cPouta service within that project.

    [cPouta](../../cloud/pouta/index.md) is an Infrastructure-as-a-Service
    (IaaS) platform based on OpenStack technology. It is ideal for use cases
    requiring an internet-accessible Linux server.

    A variety of virtual machine options are available, ranging from small
    machines to I/O-intensive or GPU-enabled ones. These virtual machines can
    be accessed from the internet via a public IPv4 address. If your course
    requires substantial computing resources, the HPC platforms
    [Puhti and Mahti](#puhti-and-mahti) are recommended instead.

    The OpenStack platform can be administered either through the web interface
    or using command-line tools.

    ## Instructions

    ### Teacher

    1. [Create a CSC user account](../../accounts/how-to-create-new-user-account.md).
    2. [Create a CSC Course project](../../accounts/how-to-create-new-project.md#course).
    3. [Add cPouta service access to the project](../../accounts/how-to-add-service-access-for-project.md#project-manager).
    4. Based on the nature of your course:
        1. In case of a shared infrastructure with few machines, use Linux's
           own tools to create accounts for students.
           [See a tutorial here](../../support/faq/how-can-I-give-access-to-other-people-to-my-vm-in-pouta.md).
        2. If each student needs their own virtual infrastructure, ask them to
           create a [student project](../../accounts/how-to-create-new-project.md#student).
        3. If students need to modify a shared infrastructure, invite them to
           the project:
            1. [using an invitation link](../../accounts/how-to-add-members-to-project.md#using-invitation-link)
               (recommended)
            2. [or directly](../../accounts/how-to-add-members-to-project.md#adding-members-directly).
    5. Prepare the course content.
        1. [Consult the documentation](../../cloud/pouta/index.md).
        2. [Contact CSC Service Desk if you need support](../contact.md).

    !!! warning "Sufficient quota"
        If you end up using a shared cPouta virtual infrastructure with a large
        number of students, please ensure that the project quota is sufficient.
        If not, either [request an increase to the quota](../contact.md) or ask
        the students to create their own
        [CSC Student projects](../../accounts/how-to-create-new-project.md#student)
        instead.

    ### Student

    6. In case of a shared virtual infrastructure:
        1. [Connect to it following the instructions](../../cloud/pouta/connecting-to-vm.md).
    7. If access to the OpenStack control plane of the teacher's CSC Course
       project is required:
        1. [Create a CSC user account](../../accounts/how-to-create-new-user-account.md).
        2. Join the course project:
            1. If you've been sent a project invitation link,
               [accept the invitation in MyCSC](../../accounts/how-to-add-members-to-project.md#member).
            2. If you've been added directly to the course project, no further
               actions are required to join the course project.
        3. [Accept the relevant terms of service in MyCSC](../../accounts/how-to-add-service-access-for-project.md#member). 
    8. In case each student sets up their own cPouta virtual infrastructure:
        1. [Create a CSC user account and student project following these instructions](student_quick.md).
        2. [Add cPouta service to the student project](../../accounts/how-to-add-service-access-for-project.md#project-manager).

=== "Noppe"

    The [Noppe service](../../cloud/noppe/index.md) is a cloud platform that
    gives users easy access to web applications such as JupyterLab, RStudio and
    VS Code Server. The applications provide consistent, installation-free
    environments tailored for educational usage in particular.

    !!! info
        Note that you do **not** need a CSC project to use the Noppe service!

    ## Instructions

    Educators can create workspaces and use their own teaching materials.
    Students can then either join these workspaces or access the self-learning
    web applications.

    ### Teacher

    [Please see the guide for teachers](../../cloud/noppe/guide_for_teachers.md)
    for more detailed instructions.

    ### Student

    [Please see the guide for student](../../cloud/noppe/guide_for_students.md)
    for more detailed instructions.

=== "Puhti and Mahti"

    !!! info
        Puhti and Mahti will be decommissioned in 2026 and replaced by Roihu,
        CSC's next-generation supercomputer offering enhanced performance and
        capabilities. Please take this into account when planning courses for
        2026.

        [Learn more about Roihu :material-arrow-right:](../../computing/systems-roihu.md)

    [CSC supercomputers Mahti and Puhti](../../computing/index.md) are ideal
    platforms for organizing courses that benefit from HPC resources or aim to
    teach how to use and run computations on supercomputing platforms. This
    includes cases where the course participants need access to GPUs or larger
    CPU resources, and cases where the
    [existing software stack](../../apps/index.md) is used for the course
    assignments.

    The systems support both traditional command-line
    [batch processing compute tasks](../../computing/running/getting-started.md),
    as well as web-based tools such as Jupyter Notebooks and RStudio via the
    [web interfaces](../../computing/webinterface/index.md). Course organizers
    are even able to create customized Jupyter Notebook environments for their
    course using the
    [Jupyter for Courses](../../computing/webinterface/jupyter-for-courses.md)
    app.

    Please note that courses using CSC supercomputers can have **at maximum 50
    students**. Ideally, teachers should target a smaller number of around 25
    participants. For larger courses the free resources and allowed resource
    reservations may not support the requested amount of users.

    It is also recommended to request an advance resource reservation for
    courses to guarantee the availability of resources.
    [Read more below](#advance-resource-reservation).

    !!! warning
        Please note that the first Tuesday and Wednesday of each month are
        reserved for regular maintenance breaks. You should never rely on the
        services being available on those days.

    ## Instructions

    ### Teacher

    1. [Create a CSC user account](../../accounts/how-to-create-new-user-account.md).
    2. [Create a CSC Course project](../../accounts/how-to-create-new-project.md#course).
    3. [Add Puhti and/or Mahti service access to the project](../../accounts/how-to-add-service-access-for-project.md#project-manager).
    4. Invite students to the project either by
        1. [using an invitation link](../../accounts/how-to-add-members-to-project.md#using-invitation-link)
           (recommended)
        2. [or directly](../../accounts/how-to-add-members-to-project.md#adding-members-directly).
    5. [Request an advance resource reservation](#advance-resource-reservation).
    6. Prepare the course content.
        1. [Consult the documentation](../../computing/index.md).
        2. [Contact CSC Service Desk if you need support](../contact.md).

    ### Student

    7. [Create a CSC user account](../../accounts/how-to-create-new-user-account.md).
    8. Join the course project:
        1. If you've been sent a project invitation link,
           [accept the invitation in MyCSC](../../accounts/how-to-add-members-to-project.md#member).
        2. If you've been added directly to the course project, no further
           actions are required to join the course project.
    9. [Accept the relevant terms of service in MyCSC](../../accounts/how-to-add-service-access-for-project.md#member).

    ## Advance resource reservation

    Course projects are subject to the same Slurm job priority policies as
    regular computing projects, meaning that **course participants may need to
    queue for resources** if the system is under heavy use. To ensure the
    availability of resources at the time of the course session(s), we
    recommend requesting for an _advance resource reservation_.
    
    **Please note**:

    * The resource reservation must be requested **at least 14 days** before
      the start of the course via [CSC Service Desk](../contact.md).
    * The request should be motivated and include
        1. The course project number,
        2. the number of participants,
        3. the resources planned for the course,
        4. timetable showing the schedule of the course.
    * The maximum amount and type of reservable resources are outlined in the
      table below.

        | System | Approval | CPU limit | GPU limit | Max. daily time window | Max. course days in total |
        |--------|----------|-----------|-----------|------------------------|---------------------------|
        | Puhti  | Automatic | 2 nodes (80 cores) | 0 | 08:00–17:00 | 5 |
        |        | CSC Resource Allocation Group | 5 nodes (200 cores) | 4 nodes (16 GPUs) | Up to 12 hrs (e.g., 08:00–20:00 or 12:00–24:00) | 10 |
        | Mahti  | Automatic | 2 nodes (256 cores) | 14 [GPU slices](../../computing/running/batch-job-partitions.md#gpu-slices) | 08:00–17:00 | 5 |
        |        | CSC Resource Allocation Group | 8 nodes (1024 cores) | 56 [GPU slices](../../computing/running/batch-job-partitions.md#gpu-slices) | Up to 12 hrs (e.g., 08:00–20:00 or 12:00–24:00) | 10 |

    A granted advance resource reservation will be visible in the form for
    launching an interactive session in the Puhti and Mahti web interfaces.
    Note that the option will be greyed out until the start of the reservation.

    In batch job scripts, the advance resource reservation is activated using
    the Slurm directive:

    ```bash
    #SBATCH --reservation=<reservation name>
    ```

    Please note that the project number and partition must match what has been
    specified for the advance resource reservation.

=== "Pukki"

    [Pukki](../../cloud/dbaas/what-is-dbaas.md) is a Database-as-a-service
    (DBaaS), where you can launch a database "with a simple click". Pukki
    automates away the database maintenance and administrative tasks of other
    services so that the teacher can focus on using/teaching the actual topic
    of databases.

    Instead of manually setting up your own database that you have to maintain
    yourself, you can use DBaaS to manage the tedious tasks of provisioning,
    configuring, maintaining, updating, documenting and backing up your
    database.

    ## Instructions

    !!! info
        If each student needs their own Pukki DBaaS instance, they should
        create a
        [CSC Student project](../../accounts/how-to-create-new-project.md#student)
        and activate the Pukki service within that project.

    ### Teacher

    1. [Create a CSC user account](../../accounts/how-to-create-new-user-account.md).
    2. [Create a CSC Course project](../../accounts/how-to-create-new-project.md#course).
    3. [Add Pukki service access to the project](../../accounts/how-to-add-service-access-for-project.md#project-manager).
    4. Based on the nature of your course:
        1. In case only one database is needed, use its tools to create
           accounts for students.
            1. [Instructions for PostgreSQL](../../cloud/dbaas/postgres-permissions.md).
            2. [Instructions for MariaDB](../../cloud/dbaas/mariadb-permissions.md).
        2. If each student needs their own database, ask them to create a
           [student project](../../accounts/how-to-create-new-project.md#student).
    5. Prepare the course content.
        1. [Consult the documentation](../../cloud/dbaas/index.md).
        2. [Contact CSC Service Desk if you need support](../contact.md).

    ### Student

    6. If a shared database is used, access it following the appropriate
       instructions:
        1. [Instructions for PostgreSQL](../../cloud/dbaas/postgres-accessing.md).
        2. [Instructions for MariaDB](../../cloud/dbaas/mariadb-accessing.md).
    7. In case each student needs their own database:
        1. [Create a CSC user account and student project following these instructions](student_quick.md).
        2. [Add Pukki service to the student project](../../accounts/how-to-add-service-access-for-project.md#project-manager).

=== "Rahti"

    [Rahti](../../cloud/rahti/index.md) is an orchestration service for
    containers that runs on OKD. Educators can launch services to be used on a
    course, or Rahti can form a part of the course itself. The service is, for
    example, useful for teaching CI/CD pipelines.

    Like cPouta, Rahti offers similar multipurpose technology, but without the
    burden of having to maintain the operating system yourself. A variety of
    ready-made templates can be used with just one click, saving you the
    trouble of installing services as you would in cPouta.

    ## Instructions

    !!! info
        If students should **not** have access to others' Rahti environments,
        they should use a
        [CSC Student project](../../accounts/how-to-create-new-project.md#student)
        instead.

    ### Teacher

    1. [Create a CSC user account](../../accounts/how-to-create-new-user-account.md).
    2. [Create a CSC Course project](../../accounts/how-to-create-new-project.md#course).
    3. [Add Rahti service access to the project](../../accounts/how-to-add-service-access-for-project.md#project-manager).
    4. Based on the nature of your course:
        1. If each student needs an isolated Rahti namespace environment, ask
           them to create a
           [student project](../../accounts/how-to-create-new-project.md#student).
        2. If students sharing and seeing each other's environments is not a 
           problem, invite students to the course project either by:
            1. [using an invitation link](../../accounts/how-to-add-members-to-project.md#using-invitation-link)
               (recommended)
            2. [or directly](../../accounts/how-to-add-members-to-project.md#adding-members-directly).
    5. Prepare the course content.
        1. [Consult the documentation](../../cloud/rahti/index.md).
        2. [Contact CSC Service Desk if you need support](../contact.md).

    ### Student

    6. If each student requires an isolated Rahti namespace environment:
        1. [Create a CSC user account and student project following these instructions](student_quick.md).
        2. [Add Rahti service to the student project](../../accounts/how-to-add-service-access-for-project.md#project-manager).
    7. If access to a shared container environment setup by the teacher is
       required:
        1. [Create a CSC user account](../../accounts/how-to-create-new-user-account.md).
        2. Join the course project:
            1. If you've been sent a project invitation link,
               [accept the invitation in MyCSC](../../accounts/how-to-add-members-to-project.md#member).
            2. If you've been added directly to the course project, no further
               actions are required to join the course project.
        3. [Accept the relevant terms of service in MyCSC](../../accounts/how-to-add-service-access-for-project.md#member).

=== "SD Services"

    [Sensitive Data (SD) Desktop](../../data/sensitive-data/sd_desktop.md)
    allows you to analyze sensitive research data from your web browser
    securely. With this user interface, you can easily manage a virtual
    computer (here called desktop, technically defined as virtual machine). SD
    Desktop is designed for managing sensitive data from any research field and
    for diverse purposes.

    [SD Connect](../../data/sensitive-data/sd_connect.md) is a simple user
    interface for storing and sharing sensitive data. Data in SD Connect can be
    analyzed in SD Desktop.

    ## Instructions

    ### Teacher

    1. [Create a CSC user account](../../accounts/how-to-create-new-user-account.md).
    2. [Create a CSC Course project](../../accounts/how-to-create-new-project.md#course).
    3. [Add SD Desktop and/or SD Connect service access to the project](../../accounts/how-to-add-service-access-for-project.md#project-manager).
    4. Invite students to the project either by
        1. [using an invitation link](../../accounts/how-to-add-members-to-project.md#using-invitation-link)
           (recommended)
        2. [or directly](../../accounts/how-to-add-members-to-project.md#adding-members-directly).
    5. Prepare the course content.
        1. [Consult the documentation](../../data/sensitive-data/sd_desktop.md).
        2. [Contact CSC Service Desk if you need support](../contact.md).

    ### Student

    6. [Create a CSC user account](../../accounts/how-to-create-new-user-account.md).
    7. Join the course project:
        1. If you've been sent a project invitation link,
           [accept the invitation in MyCSC](../../accounts/how-to-add-members-to-project.md#member).
        2. If you've been added directly to the course project, no further
           actions are required to join the course project.
    8. [Accept the relevant terms of service in MyCSC](../../accounts/how-to-add-service-access-for-project.md#member).

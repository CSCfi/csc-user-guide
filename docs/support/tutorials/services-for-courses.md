# How to organize a course using CSC resources

CSC services can be used for educational purposes in accordance with our
[free-of-charge use policy](https://research.csc.fi/free-of-charge-use/).

The maximum lifetime of a CSC Course project, including all its enabled services,
is six months. It is not possible to extend or transfer an existing CSC Course project.

This guide outlines how to organize a course using [Allas](#allas), [cPouta](#cpouta),
[Noppe](#noppe), [CSC supercomputers Puhti and Mahti](#puhti-and-mahti), [Pukki](#pukki),
[Rahti](#rahti) and [SD Desktop](#sensitive-data-sd-desktop). The guide also includes advice on
[how to select the most suitable service for your needs](#which-service-should-i-choose).

=== "Allas"

    !!! info
        Please note that the data will only be available for the duration of
        the CSC Course project.

    Allas is a Ceph-based object storage system. It is designed for storing and sharing large
    volumes of data. Data can be accessed from other CSC services, such as cPouta, Puhti and
    Mahti, or directly via the website: <https://allas.csc.fi>.

    Data can be accessed using tools and programming languages based on S3 or Swift interfaces.

    ## Instructions

    ### Teacher

    1. [Create a CSC user account](../../accounts/how-to-create-new-user-account.md).
    2. [Create a CSC Course project](../../accounts/how-to-create-new-project.md#course).
    3. [Add Allas service access to the project](../../accounts/how-to-add-service-access-for-project.md#project-manager).
    4. If you need to restrict access to data to students only, invite them to the project:
        1. [using an invitation link](../../accounts/how-to-add-members-to-project.md#using-invitation-link) (recommended)
        2. [or directly](../../accounts/how-to-add-members-to-project.md#adding-members-directly).
    5. Prepare the course content.
        1. [Consult the documentation](../../data/Allas/index.md).
        2. [Contact CSC Service Desk if you need support](../contact.md).

    ### Student

    If the course-related data is not publicly available but is shared:

    1. [Create a CSC user account](../../accounts/how-to-create-new-user-account.md).
    2. Join the course project:
        1. If you've been sent a project invitation link, [accept the invitation in MyCSC](../../accounts/how-to-add-members-to-project.md#member).
        2. If you've been added directly to the course project, no further actions are required to join the course project.
    3. [Accept the relevant terms of service in MyCSC](../../accounts/how-to-add-service-access-for-project.md#member).

=== "cPouta"

    !!! info
        Please note that the resources will only be available for the duration of
        the CSC Course project. Also if each student needs to manage own virtual
        infrastructure, they should create a CSC Student project and activate
        the cPouta service within that project.

    cPouta is an infrastructure-as-a-service (IaaS) platform based on OpenStack technology.
    It is ideal for use cases requiring an internet-accessible Linux server.

    A variety of virtual machine options are available, ranging from small machines to
    I/O-intensive or GPU-enabled ones. These virtual machines can be accessed from
    the internet via a public IPv4 address.

    The OpenStack platform can be administered either through the web interface or
    using command line tools.

    ## Instructions

    ### Teacher

    1. [Create a CSC user account](../../accounts/how-to-create-new-user-account.md).
    2. [Create a CSC Course project](../../accounts/how-to-create-new-project.md#course).
    3. [Add cPouta service access to the project](../../accounts/how-to-add-service-access-for-project.md#project-manager).
    4. Based on the nature of your course:
        1. In case of an infrastructure with few machines and an access, use Linux's own
           tools to create accounts for students.
        2. If each student needs their own virtual infrastructure, ask them to create a student project.
        3. If students need to modify shared infrastructure, invite them to the project:
            1. [using an invitation link](../../accounts/how-to-add-members-to-project.md#using-invitation-link) (recommended)
            2. [or directly](../../accounts/how-to-add-members-to-project.md#adding-members-directly).
    5. Prepare the course content.
        1. [Consult the documentation](../../cloud/pouta/index.md).
        2. [Contact CSC Service Desk if you need support](../contact.md).

    !!! warning "Sufficient quota"
        If you end up using a shared cPouta virtual infrastructure with a large number of students,
        please ensure that the project quota is sufficient. If not, either request an increase
        to the quota (<servicedesk@csc.fi>) or ask the students to create their own CSC Student projects instead.

    ### Student

    1. In case of an own cPouta virtual infrastructure, follow these instructions to find out how to create
       a student project: [Getting started with CSC services for students](student_quick.md). Then, add cPouta service to that project.
    2. If access to the teacher's CSC Course project's OpenStack control plane is required:
        1. [Create a CSC user account](../../accounts/how-to-create-new-user-account.md).
        2. Join the course project:
            1. If you've been sent a project invitation link, [accept the invitation in MyCSC](../../accounts/how-to-add-members-to-project.md#member).
            2. If you've been added directly to the course project, no further actions are required to join the course project.
        3. [Accept the relevant terms of service in MyCSC](../../accounts/how-to-add-service-access-for-project.md#member).

=== "Noppe"

    Motivation why to use Noppe here.

    ## Instructions

    ### Teacher

    [Please see the guide for teachers](../../cloud/noppe/guide_for_teachers.md).

    ### Student

    [Please see the guide for student](../../cloud/noppe/guide_for_students.md).

=== "Puhti and Mahti"

    !!! info "Puhti and Mahti will be retired in 2026"
        Puhti and Mahti will be decommissioned in 2026 and replaced by Roihu, CSC's
        next-generation supercomputer offering enhanced performance and
        capabilities. Please take this into account when planning courses for 2026.

        [Learn more about Roihu :material-arrow-right:](../../computing/systems-roihu.md)

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

    It is also recommended to request an advance resource reservation for courses
    to guarantee the availability of resources.
    [Read more below](#advance-resource-reservation).

    !!! warning "Service breaks"
        Please note that the first Tuesday and Wednesday of each month are reserved
        for regular maintenance breaks. You should never rely on the services being
        available on those days.

    ## Instructions

    ### Teacher

    1. [Create a CSC user account](../../accounts/how-to-create-new-user-account.md).
    2. [Create a CSC Course project](../../accounts/how-to-create-new-project.md#course).
    3. [Add Puhti and/or Mahti service access to the project](../../accounts/how-to-add-service-access-for-project.md#project-manager).
    4. Invite students to the project either by
        1. [using an invitation link](../../accounts/how-to-add-members-to-project.md#using-invitation-link) (recommended)
        2. [or directly](../../accounts/how-to-add-members-to-project.md#adding-members-directly).
    5. [Request an advance resource reservation](#advance-resource-reservation).
    6. Prepare the course content.
        1. [Consult the documentation](../../computing/index.md).
        2. [Contact CSC Service Desk if you need support](../contact.md).

    ### Student

    1. [Create a CSC user account](../../accounts/how-to-create-new-user-account.md).
    2. Join the course project:
        1. If you've been sent a project invitation link, [accept the invitation in MyCSC](../../accounts/how-to-add-members-to-project.md#member).
        2. If you've been added directly to the course project, no further actions are required to join the course project.
    3. [Accept the relevant terms of service in MyCSC](../../accounts/how-to-add-service-access-for-project.md#member).

    ## Advance resource reservation

    Course projects are subject to the same Slurm job priority policies as regular
    computing projects, meaning that **course participants may need to queue for
    resources** if the system is under heavy use. To ensure the availability of
    resources at the time of the course session(s), we recommend requesting for an
    _advance resource reservation_. Please note:

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
    launching an interactive session in the web interfaces. Note that the option
    will be greyed out until the start of the reservation.

    In batch job scripts, the advance resource reservation is activated using the
    Slurm directive:

    ```bash
    #SBATCH --reservation=<reservation name>
    ```

    Please note that the project number and partition must match what has been
    specified for the advance resource reservation.

    ## Which service should I choose?

    The following table compares Noppe vs. Puhti and Mahti in order to help
    selecting the most suitable service for your course.

    | Feature | | Noppe | Puhti | Mahti |
    |---------|---------|:-----:|:-----:|:-----:|
    | Prerequisites | | | | |
    | | CSC Course project required | &#10060; | &#9989; | &#9989; |
    | | Teacher needs CSC account | &#9989; | &#9989; | &#9989; |
    | | Students need CSC accounts | &#10060; | &#9989; | &#9989; |
    | User interface | | | | |
    | | Web interface | &#9989; | &#9989; | &#9989; |
    | | Command-line interface | &#10060; | &#9989; | &#9989; |
    | Graphical apps | | | | |
    | | Jupyter Notebooks | &#9989; | &#9989; | &#9989; |
    | | RStudio | &#9989; | &#9989; | &#9989; |
    | | MATLAB | &#10060; | &#9989; | &#9989; |
    | | TensorBoard | &#10060; | &#9989; | &#9989; |
    | | MLflow | &#10060; | &#9989; | &#9989; |
    | | VS Code | &#10060; | &#9989; | &#9989; |
    | | Remote desktop | &#10060; | &#9989; | &#9989; |
    | | Remote desktop with GPU acceleration | &#10060; | &#9989; | &#10060; |
    | Resources | | |
    | | CPU | &#9989; | &#9989; | &#9989; |
    | | GPU | &#10060; | &#9989; | &#9989; |
    | | Shared storage quota | 20 GiB | 1 TiB | 1 TiB |

=== "Pukki"

    Pukki is a Database-as-a-service (DBaaS), where you can launch a new database
    "with a simple click". Pukki automates away the database maintenance and
    administrative tasks of other services so that the teacher can focus on using/teaching
    the actual topic of databases.

    Instead of manually setting up your own database that you have to maintain yourself,
    you can use DBaaS to manage the tedious tasks of provisioning, configuring, maintaining,
    updating, documenting and backing up your database.

    ## Instructions

    !!! info
        If each student needs their own Pukki DBaaS instance, they should create
        a CSC Student project and activate the Pukki service within that project.

    ### Teacher

    1. [Create a CSC user account](../../accounts/how-to-create-new-user-account.md).
    2. [Create a CSC Course project](../../accounts/how-to-create-new-project.md#course).
    3. [Add Pukki service access to the project](../../accounts/how-to-add-service-access-for-project.md#project-manager).
    4. Based on the nature of your course:
        1. In case of one database, use its tools to create accounts for students.
        2. If each student needs their own database, ask them to create a student project.
    5. Prepare the course content.
        1. [Consult the documentation](../../cloud/dbaas/index.md).
        2. [Contact CSC Service Desk if you need support](../contact.md).

    ### Student

    1. Follow these instructions to find out how to create a student project: [Getting started with CSC services for students](student_quick.md)
        2. Then, add Pukki service to that project.

=== "Rahti"

    Rahti is an orchestration service for containers that runs on OKD. Educators
    can launch services to be used on a course, or Rahti can form part of the course itself.
    The service is for example useful for teaching CI/CD pipelines.

    Like cPouta, Rahti offers similar multipurpose technology, but without the burden
    of having to maintain the operating system yourself. A variety of ready-made templates
    can be used with just one click, saving you the trouble of installing services as you
    would in cPouta.

    ## Instructions

    !!! info
        If students should **not** have access to others' Rahti environments,
        they should use a CSC Student project instead.

    ### Teacher

    1. [Create a CSC user account](../../accounts/how-to-create-new-user-account.md).
    2. [Create a CSC Course project](../../accounts/how-to-create-new-project.md#course).
    3. [Add Rahti service access to the project](../../accounts/how-to-add-service-access-for-project.md#project-manager).
    4. Based on the nature of your course:
        1. If each student needs isolated Rahti namespace environment, ask them to create a student project.
        2. If students sharing and seeing each other's environments is not a problem,
           invite students to the project either by
            1. [using an invitation link](../../accounts/how-to-add-members-to-project.md#using-invitation-link) (recommended)
            2. [or directly](../../accounts/how-to-add-members-to-project.md#adding-members-directly).
    5. Prepare the course content.
        1. [Consult the documentation](../../cloud/rahti/index.md).
        2. [Contact CSC Service Desk if you need support](../contact.md).

    ### Student

    1. If an isolated Rahti namespace environment is required, follow these instructions
    to find out how to create a student project: [Getting started with CSC services for students](student_quick.md)
        1. then, add Rahti service to that project.
    2. Or if an access to a shared container environment is required:
        1. [Create a CSC user account](../../accounts/how-to-create-new-user-account.md).
        2. Join the course project:
            1. If you've been sent a project invitation link, [accept the invitation in MyCSC](../../accounts/how-to-add-members-to-project.md#member).
            2. If you've been added directly to the course project, no further actions are required to join the course project.
        3. [Accept the relevant terms of service in MyCSC](../../accounts/how-to-add-service-access-for-project.md#member).

=== "SD Desktop"

    Sensitive Data (SD) Desktop allows you to analyze sensitive research data from
    your web browser securely. With this user interface, you can easily manage
    a virtual computer (here called desktop, technically defined as virtual machine).

    ## Instructions

    ### Teacher

    1. [Create a CSC user account](../../accounts/how-to-create-new-user-account.md).
    2. [Create a CSC Course project](../../accounts/how-to-create-new-project.md#course).
    3. [Add Sensitive Data (SD) Desktop service access to the project](../../accounts/how-to-add-service-access-for-project.md#project-manager).
    4. Invite students to the project either by
        1. [using an invitation link](../../accounts/how-to-add-members-to-project.md#using-invitation-link) (recommended)
        2. [or directly](../../accounts/how-to-add-members-to-project.md#adding-members-directly).
    5. Prepare the course content.
        1. [Consult the documentation](../../data/sensitive-data/sd_desktop.md).
        2. [Contact CSC Service Desk if you need support](../contact.md).

    ### Student

    1. [Create a CSC user account](../../accounts/how-to-create-new-user-account.md).
    2. Join the course project:
        1. If you've been sent a project invitation link, [accept the invitation in MyCSC](../../accounts/how-to-add-members-to-project.md#member).
        2. If you've been added directly to the course project, no further actions are required to join the course project.
    3. [Accept the relevant terms of service in MyCSC](../../accounts/how-to-add-service-access-for-project.md#member).

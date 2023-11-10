# Projects and quota

## OpenShift projects and CSC computing projects

!!! info

    Projects in OpenShift are separate from CSC computing projects. A single CSC
    computing project can have access to multiple projects in OpenShift.
    Each CSC computing project with access to Rahti receives a *group* in
    OpenShift.

All projects in OpenShift must be mapped to a CSC computing project. This
mapping is used to determine which CSC computing project a given resource
belongs to for billing and other purposes. You need to
specify which of them to use. You have to specify which project to map by entering `csc_project:` followed
by the name or number of your CSC computing project in the _Description_ field
when creating a new project in OpenShift. You can also enter other text in the
description field if you want to have a human-readable description for
the project you are creating.

For example, if you have Rahti access via *project_1000123*, you would
enter the following in the _Description_ field:

```yaml
csc_project: 1000123
```

You can also enter a human-readable description for the project, in which case
the field could look like this:

```yaml
This project is used for hosting the Pied Piper web application.

csc_project: 1000123
```

This would make it so that any usage within that OpenShift project is billed
to the billing unit quota of project_1000123. Note that project_1000123 must
have Rahti access and you must be a member of that computing project,
or the OpenShift project creation will fail.

If you would like to know which CSC computing projects you are a member of, you
can view a list in the [My Projects
tool](https://my.csc.fi/projects) of MyCSC. You can also set a default 
billing project by going to [Your Profile page](https://my.csc.fi/profile). 

If you would like to know which CSC computing project an OpenShift project is
associated with, you can do so using the _oc_ command line tool. You can find
instructions for setting up oc in the [command line tool usage
instructions ](cli.md). For example, if your OpenShift project is called
*my-openshift-project*, you would run:

```bash
oc get project my-openshift-project -o yaml
```

This should produce the following output:

```yaml
apiVersion: project.openshift.io/v1
kind: Project
metadata:
  annotations:
    ...
  creationTimestamp: 2018-11-22T12:27:05Z
  labels:
    csc_project: "1000123"
  name: my-openshift-project
  resourceVersion: "72557736"
  selfLink: /apis/project.openshift.io/v1/projects/my-openshift-project
  uid: df4970e2-abd7-4417-adbf-531293c68cd6
spec:
  finalizers:
  - openshift.io/origin
  - kubernetes
status:
  phase: Active
```

In the output above, you can find the associated CSC computing project under
`metadata.labels.csc_project`. In this case, the project is `1000123`.
Unfortunately, this information is not available via a web interface yet.

!!! info

    It is not possible for normal users to change the *csc_project* label
    after a project has been created. If you would like to change the label for
    an existing project, please [contact the support](../../../support/contact.md). You can also create
    a completely new project if you want to use a different label.

## Creating a project

First, click this [link](https://landing.2.rahti.csc.fi/) to access the homepage of Rahti and click **Login Page** under *OpenShift 4.11*.  

After being logged in, click the blue "Create Project" button to create a project, and you will be presented with the following view:

![OpenShift new project dialog](../../img/new_project_dialog_4.png)

1. You *need* to pick a **unique name** that is not in use by any other project
in the system.
1. You *can* also enter a **human-readable display name** and.
1. You *have to* also enter a **CSC computing project** in the _Description_ field. It must be a currently valid CSC project, that your account has access to. In order to view to which CSC projects you have access to, please check <https://my.csc.fi>. If you have access to no CSC project, you will not be able to create any Rahti project. If you have Rahti access via project_1000123, you would enter the following in the Description field:

> csc_project: 1000123

![OpenShift Create Project](../../img/create_project_dialog_4.png)

See the section about [accounts](../../../accounts/index.md).

Once you have filled in the fields, click "Create", and you will see the application
catalog where you can pick an application template or import your
own one.

For more information about using the web interface, refer to the
[official OpenShift documentation](https://docs.okd.io/) (our current version is 4.11). You can find out which version of the documentation to look at in the web interface by
clicking the question mark symbol in the top bar and selecting "About".

## Project quotas

Each project has its own quota. Initial quota is the following:

| Resource                         | Default |
|----------------------------------|---------|
| Virtual cores                    | 4       |
| RAM                              | 16 GiB  |
| Storage                          | 100 GiB |
| Number of image streams (images) | 20      |
| Size of each registry images     | 5 GiB   |

This means that your project can use up to 4 cores and 16GiB in total, it can be 1 Pod using the whole 4 cores and 16 GiB, 8 pods each using half a core and 2 GiB, etc...

You can find the resource usage and quota of a project in the project view in
the web interface under **Administration -> ResourceQuota** and **Administration -> LimitRanges** in the `Administrator` menu.

Alternatively, you can use the oc command line tool:

```bash
oc describe quota
oc describe limitranges
```

If you need to create more projects or you need more resources in a project for
your application, you can apply for more quota by contacting the Rahti
support. See the [Contact page](../../../support/contact.md) for instructions. Quota requests are
handled on a case-by-case basis depending on the currently available resources
in Rahti and the use case.

### Default Pod resource limits

Every Pod needs to have lower and upper limits regarding resources, specifically for CPU and memory. The lower are called `requests`, and the upper are called `limits`. The `requests` sets the minimum resources needed for a  Pod to run, and a Pod is not allowed to use more resources than the specified in `limits`.

The user can set the limits explicitly within the available quota, but if no limit is set by the user, the defaults are used:

|Type|CPU|Memory|
|:-:|:-:|:-:|
|limits|500m|1Gi|
|requests|50m|500Mi|

Note: `m` stands for milicores. `500m` will be the equivalent of 0.5 cores, or in other words half of the time of a CPU core.

Rahti will enforce a maximum limit/request ratio of 5. This means that the CPU or memory `limits` cannot be more than 5 times the `request`. So if the CPU request is 50m, the CPU limit cannot be higher than 500m. And if we wanted to increase the CPU limit to 1, we will have to increase as well the request to at least 100m.

## Sharing projects with other users

OpenShift has a flexible role-based access control system that allows you to
give access to projects you have created to other users and groups in the system.
You can give e.g. full admin, basic user, edit or read only access to other
users and groups in the system for collaboration.

You can edit project memberships in the web interface via **User Management ->
RoleBindings**, in the `Administrator` menu. You can either give access rights to individual users, groups or Service Accounts by selecting either the _Users_,  _Groups_ or ServiceAccount.

![Create Role Binding](../../img/Create_role_binding.png)

Note that it is important to use correct usernames when sharing projects
with others. OpenShift allows you to freely enter any username and will not notify
you for having entered a non-existent username. Usernames are also case-sensitive.
You can find out your username in OpenShift via the command line, by using the command `oc whoami`.

## Deleting a project

In order to delete a project, you need to go to the main landing page and click in the 3 vertical dots next to the name of the project. In the drop down menu, you will see the option "Delete Project"

![Delete drop down](../../img/delete_project_menu.png)

Then you will be asked to input the name of the project to prevent accidental deletions.

!!! warning

    After the project has been confirmed for deletion, all resources will be deleted and there will be no way to restore them, including the data stored in the persistent volumes.

![Project name dialog](../../img/delete_project_name.png)

After that, Rahti will start to delete all the resources of the project. It could take only few seconds or up to a minute, it depends of amount of resources the project had. After that Rahti will liberate the project name, and it will be possible to create an empty project with the same name.

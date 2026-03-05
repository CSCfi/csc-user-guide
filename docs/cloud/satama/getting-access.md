
# Getting Access to Satama

## Login Using a CSC Account

In order to use the Satama container registry with a CSC account, you need:

1. A CSC user account. You can check which is your "CSC username" in [MyCSC profile page](https://my.csc.fi/profile). You can also change the password from there. If you don't have a CSC account already, you can create one by following [Create a new CSC user account](../../accounts/how-to-create-new-user-account.md)

Multi Factor Authentication (MFA) is required when login. For more information, visit the [Multi-Factor Authentication (MFA) Guide](../../accounts/mfa.md)

2. A CSC project with Satama service enabled. To create a new CSC project, follow [Create a new CSC project](../../accounts/how-to-create-new-project.md) or ask to be added to an existing project. The project should have Satama service enabled to access. Follow [Apply for Satama access](../../accounts/how-to-add-service-access-for-project.md) to enable Satama in your CSC project.

Please contact [servicedesk@csc.fi](mailto:servicedesk@csc.fi) in case you
need assistance.

## Add Individual Members to Project

If you have project admin role, you can add individual users to an existing project and assign a role to them. Satama enforces role-based access control to ensure that only authorized users can perform specific actions.

The user must be added to MyCSC project and should login to Satama platform once. This will automatically create a username at Satama. This username can be used to give access to your Satama project. 

To add user, click on your project and click on **Members** tab

![Add Member](img/add_member.png)

A pop window will open. You can add the username of the member in project and add role of that member.

![Add Role](img/add_role.png)

The primary roles are Limited Guest, Guest, Developer, Maintainer, and Project Admin.

* **Limited Guest** can pull images but cannot push, and they cannot see logs or the other members of a project.
* **Guest** has read-only permission, they can only retag and pull images.
* **Developer** can both push and pull images.
* **Maintainer** have extended rights, such as the ability to scan images, view replications jobs, and delete images and helm charts.
* **Project Admin** can manage project members, assign roles, configure project settings and starting a vulnerability scan.

If you find that you cannot perform certain actions, such as pushing an image or initiating a scan, it’s likely due to insufficient permissions. In such cases, you should contact your project administrator to adjust your role or confirm your access level. You can check detail permission of the role [here](https://goharbor.io/docs/2.14.0/administration/managing-users/user-permissions-by-role/). 

It is also possible to have read-only access to public projects when user is not logged in. That type of user is known as **Anonymous user**. 
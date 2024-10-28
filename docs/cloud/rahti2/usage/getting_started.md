# Using the web interface

All applications launched in OpenShift run within **projects** that can be
created by any authenticated user. Each project has its own private virtual
network and it is isolated from other projects. Users can only see projects
they have created themselves or that have been shared with them. Any
containers, volumes and other resources created by users are always created
within a project. You might need to wait a few hours after your access application is accepted, before you can 
authenticate to Rahti 2.

You can either select applications to run in the application catalog that is
visible when first logging in or launch any applications using the
primitives described in the [background](../concepts.md) chapter.

Log in at <https://rahti.csc.fi/>.

!!! Warning "User not found"
    If you get an error message similar to this please read through the article [Getting access](../access.md).
    ![Error_no_user](../../img/openshift_error_no_user.png)  


Choose the RAHTI-2 environment and click the 'Login page' button.

After logging in you should see a page like this:

![OpenShift main page](../../img/openshift_main_page_4.png)

Proceed to [create a project](projects_and_quota.md) for running your applications.

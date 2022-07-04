<style>
.admonition-title { background-color: rgba(255, 145, 0, 0.1) !important; }
.admonition { background-color: white !important; }
</style>
!!! Attention "⚠️ Rahti 3 is deprecated"

    This page is about a deprected version of Rahti, please consult the [updated documentation article](../../../rahti4/usage/getting_started/)

# Using the web interface

All applications launched in OpenShift run within **projects** that can be
created by any authenticated user. Each project has its own private virtual
network and is isolated from other projects. Users can only see projects
they have created themselves or that have been shared with them. Any
containers, volumes and other resources created by users are always created
within a project.

You can either select applications to run in the application catalog that is
visible when first logging in or launch any applications using the
primitives described in the [background](/cloud/rahti/concepts/) chapter.

Log in at <https://rahti.csc.fi:8443> (see [Getting access](/cloud/rahti/access)
for instructions). After logging in, you should see a page like this:

![OpenShift main page](img/openshift_main_page_3.7.png)

Proceed to [create a project](/cloud/rahti/usage/projects_and_quota/) for running your applications.

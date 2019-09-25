# Getting started

All applications launched in OpenShift run inside **projects** that can be
created by any authenticated user. Each project has its own private virtual
network and is isolated from other projects. Users can only see those projects
that they've created themselves or that have been shared with them. Any
containers, volumes and other resources created by users are always created
inside a project.

You can either select applications to run from the application catalog that is
visible when first logging in or launch any applications that you like using the
primitives described in the [background chapter ](/cloud/rahti/introduction/background).

## Using the web interface

You can login at \env{OSO_WEB_UI_URL} (see [Getting access](../introduction/access)
for instructions). After logging in, you should see a page like this:

![OpenShift main page](img/openshift_main_page_3.7.png)

After logging in, you should proceed to [create a
project ](/cloud/rahti/usage/projects_and_quota/) in which to run your application(s).

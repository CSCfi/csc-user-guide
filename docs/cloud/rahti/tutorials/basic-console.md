<style>
.admonition-title { background-color: rgba(255, 145, 0, 0.1) !important; }
.admonition { background-color: white !important; }
</style>
!!! Attention "⚠️ Rahti 3 is deprecated"

    This page is about a deprecated version of Rahti, please consult the [updated documentation article](../../../rahti4/tutorials/basic-console/)

# Static web server

How to set up a static web server in Rahti.

1. Create a project. [Instructions](../../usage/projects_and_quota/)

2. In the catalog view, select _Apache HTTP Server_.
    ![Select-httpd](img/select-http.png)

3. Type in the source Git repository containing the content to be
    served. Here, the sample content is used, and the application
    is created in the project _http-test-project_.
    ![type-in-git](img/type-git.png)

4. Click _Create_. Navigate to the newly created
    project: ![new-project](img/click-project.png)

    Select _Overview_ in the menu on the left.

5. Now, the OpenShift dashboard should display information about the application.
    This application is available at
    [httpd-example-http-test-project.rahtiapp.fi](http://httpd-example-http-test-project.rahtiapp.fi)
    ![new-app-info](img/new-app-info.png)

OpenShift processed a template that provisioned
various objects, such as _Pods_, _Services_, _Routes_, _DeploymentConfigs_, and
_Builds_ into the container cloud, and as a result, a web server emerged.

For deeper insight in to the created objects, please see:

* [Core objects](elemental_tutorial.md) for introduction to the fundamental objects on
  which OpenShift/Kubernetes applications are built upon.
* Kubernetes and OpenShift [Concepts](../concepts.md) for how managing applications in
  OpenShift/Kubernetes is further streamlined using higher abstraction level objects.

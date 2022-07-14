# Static web server

How to set up a static web server in Rahti.

1. Create a project. [Instructions](../../usage/projects_and_quota/)

2. Select Helm -> Install a Helm Chart from the developer catalog -> Developer Catalog, search for _Apache HTTP Server_ and Click _Instantiate Template_ on the pop-up window on the right.
    ![Select-httpd](img/select-http.png)
    ![Instantiate-template](img/click-template.png)

3. Type in the source Git repository containing the content to be
    served. Here, the sample content is used, and the application
    is created in the project _http-test-project_.
    ![type-in-git](img/type-git.png)

4. Click _Topology_. to Navigate to the newly created
    project and Click name of the project _DeploymentConfigs_:
    ![new-project-deployment-config](img/click-deploymentConfig.png)

    Select _Details_ on the pop-up window on the right.
    click-deploymentConfig

5. Now, the OpenShift dashboard should display information about the application.
    ![new-project](img/click-project-details.png)
    This application is available at Select _Resources_ on the pop-up window on the right.
    [httpd-example-http-test-project.apps.rahti4-qa.csc.fi](http://httpd-example-http-test-project.apps.rahtiapp.fi)
    ![new-app-info](img/new-app-info.png)

OpenShift processed a template that provisioned
various objects, such as _Pods_, _Services_, _Routes_, _DeploymentConfigs_, and
_Builds_ into the container cloud, and as a result, a web server emerged.

For deeper insight in to the created objects, please see:

* [Core objects](elemental_tutorial.md) for introduction to the fundamental objects on
  which OpenShift/Kubernetes applications are built upon.
* Kubernetes and OpenShift [Concepts](../concepts.md) for how managing applications in
  OpenShift/Kubernetes is further streamlined using higher abstraction level objects.

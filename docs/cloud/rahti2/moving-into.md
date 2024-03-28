## When to migrate to Kubernetes

When considering migrating your services from Pouta to Kubernetes (k8s), it’s important to consider the relative
strengths of each platform. Both Pouta and Kubernetes-based platforms, such as Rahti 2, are Cloud
Computing platforms, but there are some important differences. OpenStack-based services, like
cPouta, are classified as Infrastructure-as-a-Service (IaaS) cloud services where users can provision their own 
infrastructure as Virtual Machine. Rahti 2, on the other hand is classifies as a Platform-as-a-Service (PaaS), where users can deploy
their container-based platforms in shared Kubernetes cluster that was hardened to support multi-tenancy.

The primary difference between IaaS and PaaS services is that with IaaS the user is responsible
for managing the operating system and potentially multiple applications whereas with PaaS, the
user is only responsible for managing the application and the data. You can read more about cloud
computing concepts [here](concepts.md).

Containers have certain advantages over traditional Virtual machines. Container images are typically
smaller and lighter in memory and CPU usage than Virtual machine images. Launching new containers is
fast, which gives them potential for great scalability. Since container deployment also tends to be
relatively easy, continuous deployment and integration practices work very well with container based
approaches.

Using a container orchestration service like Rahti 2 that is built on top of Kubernetes, makes the
deployment of applications easy. In Rahti 2 you can manage your applications directly using a web
interface accessible through a web browser. Rahti 2 provides a platform for you to host your own applications
and make them accessible over the web. Rahti 2 can run many different kinds of applications and workloads, from web servers
and databases to data analysis pipelines.

Some example use cases that are well suited for Rahti 2 include:

* Hosting an interactive web application or a regular website. Rahti 2 comes with many of the most common
features needed for web based applications
* Complex prepackaged application like Apache Spark. It’s also easy to scale up applications for multiple
users.
* Deploying from a catalog with many commonly used application templates with just one command.

In other words, in cases where scalability is needed, or you only want to manage a single application, container
orchestration service might be the way to go.

Containers are inherently not as secure as Virtual machines. With container orchestration services like
Rahti 2 and Openshift containers are not allowed to run with root access, which may provide some limitations
in certain circumstances and requires further customization to the images. For sensitive data processing tasks, 
it is better to consider other CSC service like ePouta which is always be the preferred platform. It
is specifically designed for high performance and high security tasks for sensitive data handling with variety
of available resources.

### Additional information

[What is Rahti 2?](rahti-what-is.md)

[Container clouds fundamentals](https://rahti-course.a3s.fi/basic.html#1)

[Why use containers vs. VMs? | VMware](https://www.vmware.com/topics/glossary/content/vms-vs-containers.html)

[Containers vs. Virtual Machines (VMs): What’s the Difference? | IBM](https://www.ibm.com/cloud/blog/containers-vs-vms)

[Migrate a service from Kubernetes to OpenShift | IBM](https://developer.ibm.com/learningpaths/migrate-kubernetes-openshift/)

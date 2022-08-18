## When to migrate to Kubernetes

When considering migrating your services from Pouta to Kubernetes (k8s), it’s important to consider the relative
strengths of each platform. Both Pouta and Kubernetes-based platforms, such as Rahti, are Cloud
Computing platforms, but there are some important differences. Virtual machine based services, like
cPouta, are classified as Infrastructure-as-a-Service (IAAS) cloud services. Kubernetes on the other
hand provides a container cloud orchestration service. You can deploy services just by using
Kubernetes, but typically it provides building blocks for developer platforms such as Rahti or
OpenShift OKD, which are a Platform-as-a-Service (PAAS) systems.

The primary difference between IAAS and PAAS services is that with IAAS the user is responsible
for managing the operating system and potentially multiple applications whereas with PAAS, the
user is only responsible for managing the application and the data. You can read more about cloud
computing concepts [here](/cloud/concepts/).

Containers have certain advantages over traditional Virtual machines. Container images are typically
smaller and lighter in memory and CPU usage than Virtual machine images. Launching new containers is
fast, which gives them potential for great scalability. Since container deployment also tends to be
relatively easy, continuous deployment and integration practices work very well with container based
approaches.

Using a container orchestration service like Rahti, that is built on top of Kubernetes, makes the
deployment of applications easy. In Rahti you can manage your applications directly using a web
interface accessible through a web browser. Rahti provides a platform for you to host your own applications
and make them accessible over the web. Rahti can run many different kinds of applications from web servers
and databases to data analysis pipelines.

Some example use cases that are well suited for Rahti include:

* Hosting an interactive web application or a regular website. Rahti comes with many of the most common
features needed for web based applications
* Complex prepackaged application like Apache Spark. It’s also easy to scale up applications for multiple
users.
* Deploying from a catalog with many commonly used application templates with just one command.

In other words, in cases where scalability is needed or you only want to manage a single application, container
orchestration service might be the way to go.

Containers are inherently not as secure as Virtual machines. With container orchestration services like
Rahti and Openshift OKD containers aren’t allowed to run with root access, which may provide  some limitations
in certain circumstances. For sensitive data processing tasks ePouta should always be the preferred platform. It
is specifically designed for high performance and high security tasks for sensitive data handling with variety
of available resources.

### Additional information

[What is Rahti?](/cloud/rahti/rahti-what-is/)

[Container clouds fundamentals](https://rahti-course.a3s.fi/basic.html#1)

[Why use containers vs. VMs? | VMware](https://www.vmware.com/topics/glossary/content/vms-vs-containers.html)

[Containers vs. Virtual Machines (VMs): What’s the Difference? | IBM](https://www.ibm.com/cloud/blog/containers-vs-vms)

[Migrate a service from Kubernetes to OpenShift | IBM](https://developer.ibm.com/learningpaths/migrate-kubernetes-openshift/)

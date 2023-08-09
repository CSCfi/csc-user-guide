# Application development practices (in Pouta)

This article discusses the best practices for developers
to follow while creating or deploying their application in
Pouta, and how Pouta can help on following them. Pouta clouds ([cPouta] and [ePouta]), like other IaaS clouds, offer more flexibility than traditional bare metal computing environments do.

The recommendations listed below are focused on what Pouta provides to you and how your applications can profit from it. Is not an exhaustive list of all best practices. You can additionally follow a larger set of [practices] as mentioned by the Cloud Native Computing Foundation, various online literature on
OpenStack such as its technical blogs, user guides, user stories etc. In real scenarios, some of these practices may not be applicable to your application, but applying practices that are suitable is the key takeaway of this article.

## Stateless and disposable Virtual Machine nodes

If possible, try to develop your application in the form of distributed
stateless _microservices_ that are responsible for independent computational sub-tasks and communicate among each other through a well defined interface. This is largely possible by the fact that you can create new VMs in a matter of a couple of minutes.

The data, which in most situations is irreplaceable, needs to be stored in separate data storage services that are persistent in nature. In Pouta clouds, we
offer _Object storage_ ([Allas]) and _Volume storage_ ([Cinder]).

This approach is sometimes more complex, as you will need to use a suitable design that allows distributed computing. A load  balancer will also be needed.

The application will be more **resilient**. Running stateless VMs helps you to
minimize the impact of failures. If the underlining hardware suddenly fails, data will not be lost. This removes single points of failure (SPoF). When data is stored in services like [Cinder] or [Allas], it will be **safer**. As it is stored in redundant hardware, that is is managed by a dedicated team of professionals.

![Stateless VM](../../../img/stateless_VM.drawio.png)

## Readily scalable (horizontal v vertical)

If an application follows the _microservice_ approach, it will allow easy **horizontal** scaling, i.e. add or remove replicas of the same VM.

It will be then less complex to horizontally **scale up and down** the application. If the computing and the data are not hardly coupled, the design will allow adding or removing Virtual machine replicas. Having more replicas also allows to spread the computation nodes across the computer center and minimizes (even more) the impact of individual failures, again lowering the number of SPoF.

For applicastions that do not allow the _microservice_ approach, Pouta allows easy **vertical** scaling, i.e. *VM resize* to change the VM [flavor] and add or remove compute resources (CPUs, RAM, disk etc.). It is very fast as it requires only a short reboot. The software running in the VM will transparently see more resources after the reboot. It is not necessary to reinstall the software. This is a complement (or alternative) to horizontal scaling (replication).

![scale](../../../img/scale.drawio.png)

!!! info "auto scale"
    In Pouta clouds, you could also programmatically scale your Heat stack using [OpenStack Heat resources] like *OS::Heat::ResourceGroup*,*OS::Heat::AutoScalingGroup* and *OS::Heat::ScalingPolicy*.

## Isolated deployments for testing and production

You **must** have several isolated deployment environments, at least **testing** and **production**. Even though the names might vary, and more environments might be suitable. The **testing** environment will be used by you and your team to experiment with changes and validate that they work as designed. **Production** is the one dedicated to your users. Issues should be found and solved in **testing** before they can get to **production**. Pouta llows you to request several computing projects that will be isolated among themselves by contruction. Other common deployment types include:

* **Pre-production**, which is in between test and production where a stable copy of production is kept but no users have access to it. Changes will go through pre-production before they arrive to production. This is useful to make a last and integrated test of a bunch of individual changes togethers. The environment will normally be freezed for some time before the changes are applied to production. It is common that a sub-community of friendly users (like the development team) might be using this environment so a real life test can be done (eat your own dog food).

* **Development**, where each team or developer will have its own playground to break and test individual changes. There are normally several of these environments and they are disposable.

## Backups

Backups are critical to any application. They protect data against _accidental deletion_, _hardware failure_, _corruption_, _ransomware_ and more. There are several data backup strategies. Depending on the application and the data it contains, the backup strategy might vary. Factors like cost, complication to setup, and reproducibility of the data, affect the strategy to follow. Pouta clouds do not provide a backup solution, but help setting up one by providing advanced storage solutions like [Cinder] and [Allas].

One common backup strategy is the 3-2-1 rule. 3 copies of the data (including the original production one), 2 different media of storage and 1 offsite backup. Other basic backup principle is that copies cannot be deleted or corrupted from the original source (this is to prevent accidents and ransomware). Using a dedicated backup tool is recommended, these tools allow to easily create immutable copies that are properly dated and scheduled. They also facilitate other secondary aspects like encryption and older backups deletion. It is also very important to validate that the backups are indeed valid and that it is possible to recover the data as intended.

![3-2-1](../../../img/3-2-1.drawio.png)

## Devops tools

### Use Infrastructure as Code tools

Infrastructure as Code (IaC) tools are very useful, as they allow to specify complex application infrastructures (VM, networking, storage, ...) using text files (code) known as templates. Then the tool will use the API of the cloud provider to automatically create/configure/delete the corresponding infrastructure. Some IaC tools which are stable and widely used are:

* **Terraform** is a very known IaC tool. It is dedicated to only being an IaC tool. It is cloud agnostic thanks to the use of "providers", like the [OpenStack provider]. See the example [terraform-openstack-example].
* **Heat** is the tool integrated by OpenStack. See the example [heat-openstack-example].
* **Ansible** has some modules that provide IaC functionality. See the example [ansible-openstack-example].

You can see above three examples, one for for each tool. All of them aim to get the same result: One or more VMs with nginx installed and few local files deployed. In order to choose which one to use, you will need to consider the up and downs of the tools and use the one that fits more your use case. For example, if you think about support. Both Heat and Ansible are developed by the OpenStack team and the Terraform provider is a community written software. In addition, Heat is provided together with OpenStack and can  be used via command line or the web interface. Finally Heat is the only one that the Pouta team fully supports. On the other hand, Terraform is more widely used and will be easier to find examples and help than the other two tools.

![Heat webUI](../../../img/heat-web-ui.png)

_Heat web UI_

!!! warning "Tools evolve"
    Keep in mind that the situations for these (and most) tools evolve over time, support may get better or dropped altogether.

### Configuration management

Every application you build has some dependencies in the form of software libraries and their specific versions.
In order for your application to work, these dependencies should be explicitly defined and installed automatically. A configuration management tool like **Ansible** or **Puppet** is the best way to achieve this. Using a configuration management tool to define and install dependencies automatically makes the deployments more reproducible and predictable. In the Ansible example below, a task called "Install dependencies" will install few tools:

```yaml
- name: Install dependencies
  become: yes
  package:
   name:
     - gzip
     - git
     - curl
   state: present
```

When all dependencies are declared, Ansible will make sure that they are installed in the deployment environment before the actual application is
deployed. You should never install any dependencies
manually, instead automate their installation. This helps reproducibility (all systems will be installed in the same way) and the system will be self-documented (it will be clear what needs to be installed). It is also possible to specify versions of software to make the installation much more stable.

These principles also apply to configuration. When possible, you should use upstream modules to handle the configuration of the software installed. Modules often isolate you from platform and version differences, i.e. you will write the same configuration definition for different versions of the software and different flavors of the operating systems and the module will translate that for you.

Configuration management tools integrate very well with Pouta clouds. As they are able to read and use specific deployment values of the VMs, like IP addresses, host names, etc...  This means that these variables do not need to be hardwired into the system and will always be kept up to date. For example, we have a load balancer and few worker nodes, the load balancer needs to have a list of worker node IPs. A configuration management tool will be able to generate automatically the load balancer configuration using the information it gets from OpenStack's API. The final product is hands-off installation and upgrade process, where the configuration management does all the work and no manual work is necessary.

### Version control tools

The application you develop, the IaC code that deploys its infrastructure, and the configuration management code that configures it, should be tracked by a version control system of your choice, the most popular and de facto standard is GIT. This is not something related with cloud computing, but a general good practice that everyone should follow. This helps you to:

* collaborate with others,
* track code base changes,
* have a backed up copy of the code,
* easily coordinate and deploy multiple environments (test/pre-production/production).

And much more.

![Git](../../../img/git.drawio.png)

### Use Continuous Integration and Continuous Delivery

Once the code of the application is in Version control, the next step is to use Continuous  Integration (CI) and Continuos Delivery (CD).

CI is when each change committed to your codebase is automatically built and tested. This allows to automatically find errors and to add static code analysis tools like linters. There  are some well known CI services online such as [Travis CI], [Circle CI] and [Github actions], that have a very low barrier of entry and give right away added value.

CD is when the validation and labeling of specific versions of the software is done automatically. And more importantly, the deployment/release of those validated versions is also automatic. So if a change passes both all the tests and the reviews of other members of the coding team, the change is deployed automatically. This degree of automation also requires a solid deployment process that do not require downtime.


  [practices]: https://12factor.net/
  [code repositories]: https://github.com/CSCfi
  [code repository]: http://https://github.com/CSCfi/etherpad-deployment-demo
  [Etherpad code example]: https://github.com/CSCfi/etherpad-deployment-demo
  [OpenStack Heat resources]: https://docs.openstack.org/heat/queens/template_guide/openstack.html
  [Ansible playbooks]: https://github.com/CSCfi/spark-openstack
  [Travis CI]: https://travis-ci.org
  [Circle CI]: https://circleci.com/
  [Github actions]: https://github.com/features/actions
  [cPouta]: https://pouta.csc.fi
  [ePouta]: http://epouta.csc.fi
  [Allas]: /data/Allas/
  [Cinder]: /cloud/pouta/persistent-volumes/
  [ansible-openstack-example]: https://github.com/cscfi/ansible-openstack-example
  [heat-openstack-example]: https://github.com/cscfi/heat-openstack-example
  [terraform-openstack-example]: https://github.com/cscfi/terraform-openstack-example
  [flavor]: https://docs.csc.fi/cloud/pouta/vm-flavors-and-billing/
  [OpenStack provider]: https://registry.terraform.io/providers/terraform-provider-openstack/openstack/latest/docs
  [Cisa]: https://www.cisa.gov/sites/default/files/publications/data_backup_options.pdf

## Application development practices in Pouta

This article discusses the best practices for developers
to follow while creating or deploying their application in
Pouta. Pouta clouds, like other IaaS clouds, offer tons of flexibility
compared to traditional computing environments but are also
susceptible to failures that any large computing environment may
face.

[TOC]

Best practices to build your application on Pouta are all about
leveraging the flexibilities of IaaS cloud computing, code management,
automation, orchestration, wise data management and dealing with
underlying cloud environment failures. Some of these practices which
could be easily followed by developers considering to build and deploy
their application in Pouta cloud environments are illustrated in
the figure below.

![Application development in Pouta](/img/pouta_application_development_1.png)

The above practices are only a small set.
You can additionally follow a larger set of [practices] as mentioned
by the Cloud Native Computing Foundation, various online literature on
OpenStack such as its technical blogs, user guides, user stories etc. In
real scenarios, some of these practices may not be applicable to your
application, but applying practices that are applicable to
your application development is the key takeaway of this section. Now,
let us discuss in detail the practices illustrated above with
code examples wherever applicable.

### Stateless and disposable application

If possible, try to develop your application in the form of distributed
stateless processes/modules that are responsible for computation.
Important data that needs to persist should be stored in separate
backing services that are persistent in nature. In Pouta clouds, we
have a backing service in the form of our _Object and volume
storage_. Running stateless processes on your VMs for computation and
storing important data in the persistent storage can help you to
minimize the impact in case your VMs are accidentally terminated or enter
an inaccessible state. This also gives you the flexibility for
scaling up and down your services at any time as processes do not have
a state to convey before scaling, which maximizes the robustness of
your application and provides an option for graceful disposability of
your application. The disposability of your application should be
complemented by a fast bootstrap, which brings added agility to your
application development and small startup cycles in case of application
failures.

### Code management

The application you develop should be tracked by version
control software of your choice, such as GIT, SVN, DCVS, Mercurial etc.
This helps you to make a code base which is backed up and can be
used for multiple staging/testing version deployments in your
production or test environments. We at CSC use GIT for our code
management. You can, for example, have a look at one of our public
[code repositories] to see how we manage our code base. You should
preferably also have automation and orchestration code for your
application in the same code repository. For example, one of our [code repositories]
that deploys an Etherpad application on
Pouta has all of its automation, orchestration and application code in
the same code repository.

Another flexibility modern code repositories provide is code sharing
and reuse. For example, you could fork one publicly available code
repository in GitHub and try to reuse some parts of the code that suits
your application. If you encounter any issues or happen to enhance the
base code, you could even contribute back to the community by reporting
an issue or generating a pull request to make your changes available
for everybody. This approach can prevent you from reinventing
the wheel, shorten your development cycle and allow you to
concentrate on the actual service features of your application.

### Dependency management and isolation

Every application you build has some dependencies in the form of
software packages and their specific versions. In order for your
application to work, these dependencies should be preinstalled in the
deployment environment. While building an application, you should
follow the golden rule: _Never rely on the deployment environment to
have your application dependencies preinstalled on it_. Therefore, you
should explicitly define your application dependencies and your
automation code should install them in the deployment environment
before deploying the actual application. Let us consider our [Etherpad code example].
   In this example, we have explicitly listed the application
dependencies in the Ansible task "Install dependencies"
under *etherpad-deployment-demo/roles/etherpad/tasks/main.yml*::

~~~~
- name: Install dependencies
  become: yes
  apt:
   name:
     - gzip
     - git
     - curl
     .
     .
     .
   state: present
~~~~

This task ensures all dependencies for the application are installed
in the deployment environment before the actual application is
deployed. As a best practice, you should never install any dependencies
manually, instead automate their installation. This will additionally
help you to keep track of your dependencies and replicate their
installation easily on new platforms. As a preferred  practice, you
should also isolate your dependencies from the base installations in the
deployment environment to avoid dependency conflicts. You could
easily do it with the help of tools such as _VirtualEnv_ (for Python
dependencies), Docker containers (for overall application isolation)
etc.

### Configuration management

Try to develop an application which manages its configuration
information itself. It is likely that the underlying  deployment
environment have different configuration information, for example, IP
addresses, VM hostname, credentials etc. when moving to a new VM or
deployment environment. Maintaining a dynamic inventory to store
application configurations is thus recommended for the applications
which get executed in cloud environments. The above Etherpad
example uses a dynamic ansible inventory
at *etherpad-deployment-demo/playbooks/templates/etherpad\_inventory.j2*
for application deployment.

~~~~
[etherpad]
~~~~

~~~~
etherpad_node ansible_ssh_host={{ hostvars['etherpad_node']['ansible_ssh_host'] }}

[galera]
{% for node in groups['galera'] %}
{{ node }} ansible_ssh_host={{ hostvars[node]['ansible_ssh_host'] }}
{% endfor %}
~~~~

You could optionally generate an inventory file which has details of
the dynamic inventory once the application deployment is complete. This
dynamic inventory file could be useful for application troubleshooting
purposes at a later stage. In the above Etherpad example, the
application generates an etherpad\_inventory file once its deployment
is complete. This inventory file is generated by following a simple
task in *etherpad-deployment-demo/playbooks/build-heat-stack.yml*
playbook:

~~~~
hosts: localhost
  gather_facts: no
  connection: local
  tasks:
    - name: Generate an inventory file
      template: src=templates/etherpad_inventory.j2 dest=../etherpad_inventory
~~~~

#### Readily scalable

Try to build an application which can be readily scaled up or down
based on your requirements. You could go for vertical scaling with
the easy-to-use *VM resize* option in Pouta. In this case, you could
resize your VM with a flavor suitable for your load i.e. flavor with
more or less compute resources (CPUs, RAM, disk etc.). Vertical
scaling works fine within the same family of flavors in Pouta. If
vertical scaling is not suitable for your load, you may consider a more
complex scaling option: horizontal scaling. In horizontal scaling, you
design an application capable of running on any number of
worker VMs which could be scaled  as per  your requirements.  If you
consider going for  horizontal scaling, you should  also self-deploy a
load  balancer which  could  distribute the  load  across your  worker
VMs. In Pouta clouds, you  could also programmatically scale your Heat
stack using [OpenStack Heat resources] like *OS::Heat::ResourceGroup,
OS::Heat::AutoScalingGroup and OS::Heat::ScalingPolicy.*

### Leverage from Automation & Orchestration

There are many automation & orchestration tools which could be used to
automate your application deployment inside Pouta clouds. ***Heat*** &
***Ansible*** are two such tools which are stable, widely used and are
supported  by Pouta  clouds.   With Heat,  you  could specify  complex
application deployment using text files known as templates. Ansible is
the  IT automation  tool  which can  ease up  the  deployment of  your
application in  Pouta by taking  care of configuration  and dependency
management, software provisioning etc..  Ansible also uses simple text
files  known   as  playbooks  for  deployment   and  orchestration  of
applications. Ansible's OpenStack cloud  module can  also be  used for
orchestrating  virtual resources  and  application deployments  inside
Pouta. Both Heat & Ansible can  be used in conjunction with each other
for example as used to deploy above [Etherpad code example] in Pouta, or in
a  standalone setting  for  example as  Ansible playbooks used  for
deploying Spark cluster in Pouta.

If you think these modern tools are difficult and not your cup of tea,
please    have   a    look    at   following    Heat   task    snippet
from* etherpad-deployment-demo/files/etherpad-heat-stack.yml*    which
programmatically deploys a  VM, attaches it to a security  group and a
virtual network.

~~~~
 etherpad_node:
    type: OS::Nova::Server
    properties:
      name: etherpad_node
      flavor: { get_param: etherpad_node_flavor }
      image: { get_param: etherpad_node_image }
      key_name: { get_param: ssh_key_name }
      security_groups:
        - { get_resource: frontend_secgroup }
      networks:
        - network: { get_param: etherpad_network }
      metadata: { 'ansible_group': 'etherpad' }
~~~~

 

### Exclusive Development Stages (Build, Release, Run)

As  a better  software  application development  practice, you  should
follow three stages  in your development cycle: Build,  Release & Run.
These stages  should have  strict separation between  themselves.  You
could even apply for different Pouta projects for these stages in case
you want  exclusive separations between them.   In **Build** stage you
make  a  distribution   of  your  code,  it  could   be  anything  for
ex. a GitHub tag,  Python EGG,  DEB or whatever  is suitable  for your
application. **Release**  stage involves making  your new  application
version available to its users.  Every release should have a unique ID
associated  with it  for example  incrementing version  numbers (v0.1,
v0.2..) or  Timestamps (2018-04-17-10:32:17).  You could also  rely on
Continuous  Integration   (CI)  practice  at  this   stage.  Under  CI
practices,  each change  committed to  your codebase  is automatically
tested, before  it could be merged  with the codebase. There  are some
well known  CI services online  such as  [Travis CI], [Circle CI] and
many more,  you could  choose one  suitable for  you.  You  could also
follow Continuous Delivery (CD) practices  in the release stage, which
ensures  availability  of   working  version  of  your   code  at  any
time. In Run stage,  you deploy your latest release  on the deployment
environment and have fun with  newly reported issues, feature request,
user   reports  etc.    You  could   sneak  into   our  public   
[code repositorie] and see our practices
for GitHub tags, versioning and reported issues.

### Practices in action

Finally, let's briefly summarise  our [Etherpad code example] and see how these practices are implemented in it.

-   In this  example, we have relied on Galera  cluster backend, where
    all Galera nodes are stateless at the application level.
-   Git repository is being used  as a code repository, changes in the
    code can be tracked by  informative commit messages. As code reuse
    principles,    we    have    relied    on    readymade opensourced
    paulczar/percona-galera docker  container   image  & etherpad-lite
    source  code  for  launching   Galera  cluster  &  Etherpad  nodes
    respectively.
-   All the application dependencies  are installed by the code itself
    through  the set  of Ansible  tasks. Application  achieves overall
    isolation through launching separate  docker containers for Galera
    nodes.
-    The application  maintains a  dynamic Ansible  inventory for  its
    configuration management.
-      And    finally,    Heat     and    Ansible    are    used    in
    conjunction for deployment and configuration of the application.

Installation      of     application      starts     from      Ansible
playbook *etherpad-deployment-demo/site.yml*    which   calls    three
different Ansible playbooks:

***etherpad-deployment-demo/playbooks/build-heat-stack.yml*** playbook has
tasks for building  up Heat stack (VMs for Etherpad  & Galera cluster,
Security  groups, Assigning  public  IPs, attaching  VMs to  project's
virtual  network  etc.)  depending  upon parameters  supplied  the  by
developer  in *etherpad-deployment-demo/playbooks/my-heat-params.yml*.
This playbook  uses dynamic inventory and  generates dynamic inventory
file  (etherpad\_inventory)  for  the  deployed  stack.  Execution  of
playbook completes when Etherpad frontend  VM & Galera cluster VMs are
set up in Pouta and are accessible via SSH.

***etherpad-deployment-demo/playbooks/configure-galera.yml*** playbook
has  tasks for  configuring  Galera cluster  VMs  and starting  Galera
cluster nodes (in the form of docker container) on these VMs.

***etherpad-deployment-demo/playbooks/configure-etherpad.yml*** playbook
has tasks for creating and  configuring front-end HA proxy, installing
dependencies  for Etherpad  on VM,  creating a  database for  Etherpad
application, configuring and launching the Etherpad node.

We  recommend that  you try  out  this Etherpad example or  something
similar in Pouta cloud environments. These examples will assist you in
understanding these practices better and how to apply them in your own
application development.

  [practices]: https://12factor.net
  [code repositories]: https://github.com/CSCfi
  [code repository]: http://https://github.com/CSCfi/etherpad-deployment-demo
  [Etherpad code example]: https://github.com/CSCfi/etherpad-deployment-demo
  [OpenStack Heat resources]: https://docs.openstack.org/heat/queens/template_guide/openstack.html
  [Ansible playbooks]: https://github.com/CSCfi/spark-openstack
  [Travis CI]: https://travis-ci.org
  [Circle CI]: https://circleci.com/

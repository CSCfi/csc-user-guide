# Container orchestration with Magnum

!!! note
    Magnum is currently a technology preview feature available
    only in  cPouta. Some  functionality may be  incomplete or  not work
    correctly. Kubernetes on top of Fedora Atomic is currently the only
    supported platform. Docker Swarm may also work.


This article explains how to use the OpenStack tool 
*Magnum* for  creating container  orchestration
engine (COE) deployments.  It can deploy Kubernetes,  Docker Swarm and
Mesos (currently only Kubernetes in  cPouta). All resources created by
Magnum are normal  OpenStack resources. Magnum simply  makes it easier
to create a  complete COE deployment compared to doing  it manually by
creating the necessary instances, networks, storage and so on. Billing
is also  exactly the same as  if the resources created  by Magnum were
created manually.

[TOC]


## Container orchestration basics


| Term                             | Meaning                                                                                                                                   |
|--------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| container orchestration engine (COE) | a platform that provides management of containers with features like health checks, replication and routing of traffic to container instances |
| cluster                              | an instance of a container orchestration engine like Kubernetes                                                                               |
| cluster template                     | a template with configuration options for a cluster                                                                                           |
| K8s                                  | another term for Kubernetes - the container orchestration engine originally developed at Google                                               |
| master node                          | the node in a cluster that provides an API through which the cluster can be controlled and other controller services                          |
| slave or worker node                 | a node that is used to run containers - managed by the master node                                                                            |
| minion node                          | (Kubernetes term) same as a slave/worker node                                                                                                 |



While Docker containers can be useful on their own, if all you have is
a bunch of Linux machines with Docker installed you still have to do a
lot of work yourself to make an application fault tolerant, to make it
discoverable from the outside world,  to make sure the containers stay
healthy and to  enable containers to communicate with  each other. You
also have  to manage the  Linux machines themselves by  installing and
configuring  packages and  doing  other  normal administrative  tasks.
Container  orchestration engines  do a  lot of  this work  for you  by
providing common abstractions around replication, routing, storage and
other aspects of running a containerized application.

A  container  orchestration  engine  typically  runs  as  a  clustered
application on  multiple servers. The  servers are separated  into two
categories:  master  nodes  and  slave nodes.  The  master  nodes  are
responsible  for receiving  commands via  an API  and acting  on these
commands to  start and manage  containerized applications that  run on
the slave nodes.  Fault tolerance can be achieved  by running multiple
copies of an application on multiple  slave nodes and the COE provides
abstractions that make this easy.

![Container orchestration](/img/container-orchestration.png)

## Installing the Magnum command line tool

Magnum can currently  only be used via the command  line.  To do this,
you will  need to install  **python-magnumclient** in addition  to the
other command line clients. See [instructions for installing OpenStack
command line tools].  With cPouta  you should use version **2.3.1** of
the tool.   Newer versions are  not compatible.  You will  most likely
need to  use pip for installation  to get the right  version.  You can
find  more detailed  instructions  on  pip in  the  command line  tool
chapter linked  above.  This  is how you  install the  correct version
using pip:

    pip install python-magnumclient==2.3.1

As with the  other command line tools,  you can output a  help text by
typing **magnum -h** and get instructions for an individual command by
typing **magnum help &lt;command name&gt;**, for example **magnum help
cluster-create**.

## Installing kubectl

Kubernetes can be controlled using  the kubectl command line tool that
connects to the API of a Kubernetes server. You can find [installation
instructions] in the Kubernetes documentation.

## Basic Magnum commands

Listing existing clusters:

    magnum cluster-list

Creating a cluster template:

    magnum cluster-template-create

Creating a cluster:

    magnum cluster-create

Show information about a cluster:

    magnum cluster-show

Deleting a cluster:

    magnum cluster-delete

## Creating a Kubernetes cluster

!!! note
    The version  of Kubernetes that is used by  the cluster is
    1.5.3. If you look for  Kubernetes documentation, you should look at
    documentation specific to this version.

It  is  assumed  that  you  already  have  your  terminal  environment
configured for OpenStack and a key pair associated with your OpenStack
account. If not,  see the instructions for  [configuring your terminal
environment  for  OpenStack](../command-line-tools) and instructions for 
[creating a key pair](../connecting-to-vm).

You will first need to create a cluster template that contains various
configuration  options for  the  cluster  to be  created.  Here is  an
example command for creating one:

    magnum cluster-template-create \
    --name k8s \
    --image Fedora-Atomic-25 \
    --external-network public \
    --dns-nameserver 193.166.4.25 \
    --network-driver flannel \
    --flavor io.70GB \
    --master-flavor io.70GB \
    --coe kubernetes \
    --volume-driver cinder \
    --keypair-id <your keypair's name>

This creates a cluster template called "k8s" (--name) that uses Fedora
Atomic 25  as the operating system  (--image) for both the  master and
the minion  nodes. Clusters will be  connected to the Internet  via an
external network called public  (--external-network) and name services
will    be    provided     by    Funet's    193.166.4.25    nameserver
(--dns-nameserver).  Container  networking is  provided by  an overlay
network driver called flannel  (--network-driver). The flavor used for
slave nodes is io.70GB (--flavor) while the flavor used for the master
node is  also io.70GB  (--master-flavor). The  container orchestration
engine to be deployed is Kubernetes  (--coe). An OpenStack key pair is
associated with  the template  (--keypair-id) and  Cinder is  used for
creating volumes for container persistent storage (--volume-driver).

With the template ready, you can create a cluster:

    magnum cluster-create \
    --name k8s-cluster \
    --cluster-template k8s \
    --master-count 1 \
    --node-count 1

This will  create a Kubernetes  cluster based on the  template defined
above.  It  will  have  one  master  (--master-count)  and  one  slave
(--node-count) node. It will take a few minutes to create the cluster.
You  can see  if  the  deployment is  finished  with the  cluster-show
command:

    magnum cluster-show k8s-cluster

Once the  cluster is  up and  running, you  will need  to set  up your
environment to use it:

    mkdir myclusterconfig
    $(magnum cluster-config k8s-cluster --dir myclusterconfig)

After this is done you can start using Kubernetes with kubectl. To see
if  everything is  working correctly,  you  can run  a simple  example
application.  You  can   find  instruction  for  doing   that  in  the
[Kubernetes documentation].

!!! note
    When running  kubectl  commands,  your working  directory
    should   be    the   one    that   contains    the   myclusterconfig
    directory. Otherwise kubectl is unable to find the configuration for
    connecting to the Kubernetes cluster.

By default, only ports 22, 6443  and 30000-32767 are opened on a newly
created Kubernetes  cluster. Port  22 is  for accessing  the cluster's
servers via SSH, 6443 is the  Kubernetes API that listens for commands
on  the master  node  and the  port range  is used  by Kubernetes  for
NodePort resources that  expose services. If you wish  to expose other
ports, you will need to edit the security groups for the cluster after
it has been created.

## Persistent storage for Kubernetes containers

Persistent  storage is  used  for storing  data  for containers.   For
example, a  database application could create  a PersistentVolumeClaim
in Kubernetes to  get a persistent volume on which  to store its data.
It is  provided using  OpenStack Cinder  volumes that  are dynamically
created as requested  by the Kubernetes cluster. In order  to use this
feature you  will first need to  create a storage class  in Kubernetes
that corresponds to Cinder storage.

First create a file called  cinder-storageclass.yaml. You can copy the
following command and paste it into a terminal to create this file:

    cat > cinder-storageclass.yaml << EOF
    ---
    kind: "StorageClass"
    apiVersion: "storage.k8s.io/v1beta1"
    metadata:
      name: "standard"
      annotations:
        storageclass.beta.kubernetes.io/is-default-class: "true"
    provisioner: "kubernetes.io/cinder"
    parameters:
      type: "standard"
      availability: "nova"
    EOF

Once you have  this file, you can  use it to create  the storage class
using kubectl create:

    kubectl create -f cinder-storageclass.yaml

Once  the  storage  class is  in  place,  you  can  use it  to  create
PersistentVolumeClaims.   Kubernetes  will   automatically  create   a
corresponding  Cinder volume  to be  used as  backing storage  for the
PersistentVolumeClaim.

Here is an example YAML file for creating a PersistentVolumeClaim (you
can copy and paste the command again):

    cat > cinder-persistentvolumeclaim.yaml << EOF
    ---
    kind: PersistentVolumeClaim
    apiVersion: v1
    metadata:
      name: myvolume
    spec:
      accessModes:
        - ReadWriteOnce
      resources:
        requests:
          storage: 1Gi
    EOF

Now you can create a PersistentVolumeClaim:

    kubectl create -f cinder-persistentvolumeclaim.yaml

You  should be  able to  see that  the PersistentVolumeClaim  has been
created and bound to a Cinder volume by running "kubectl get pvc":

    kubectl get pvc
    NAME       STATUS    VOLUME                                     CAPACITY   ACCESSMODES   STORAGECLASS   AGE
    myvolume   Bound     pvc-0091714a-80e4-11e7-8cd2-fa163ee59413   1Gi        RWO           standard       3s

When the PersistentVolumeClaim  is deleted, the Cinder  volume is also
deleted. You will also be able to see the Cinder volume via OpenStack.
See [the  documentation for  persistent volumes] for  more information
about that. Note that you should only manage the volume via Kubernetes
if it is created via Kubernetes. Managing the volume via OpenStack may
cause unexpected behavior of the PersistentVolumeClaim in Kubernetes.

## Limitations

The clusters  deployed by Magnum  in Pouta come with  some limitations
that mean that you probably should not use them for running production
services.

-    You can  only launch  Kubernetes clusters  for now.  Docker Swarm
    clusters are  also seemingly  created correctly (the  cluster goes
    into  CREATE\_COMPLETE  state),  but  they do  not  seem  to  work
    properly  after that.  Creation  of Mesos  clusters would  require
    support  for the  AWS CloudFormation  API  in Heat,  which is  not
    enabled in the cloud platform at this time.
-   Uses self-signed certificates: the  certificates used for APIs and
    services running the cluster are self-signed
-   Only single master deployments are supported: the master node is a
    single point of failure
-   Slave nodes  are not scheduled using an  anti-affinity host group:
    it is  possible for  multiple slave  nodes to end  up on  the same
    physical server, which  means failure of that  physical server can
    take down multiple slave nodes at once
-    LoadBalancer resources  cannot be  created in  Kubernetes as  the
    underlying cloud  platform does not  have this feature  enabled at
    this time.

## Further reading

-   [Magnum User Guide]
-   [Official Kubernetes documentation]
-   [Kubernetes By Example] -  a  useful  resource  for  Kubernetes examples
-   [awesome-kubernetes] - a long list of links related to Kubernetes

  [instructions for installing OpenStack command line tools]: install-client.md
  [installation instructions]: https://kubernetes.io/docs/tasks/tools/install-kubectl/
  [creating a key pair]: launch-vm-from-web-gui.md#setting-up-ssh-keys
  [Kubernetes documentation]: https://kubernetes.io/docs/tasks/access-application-cluster/service-access-application-cluster/
  [the documentation for persistent volumes]: persistent-volumes.md
  [Magnum User Guide]: https://docs.openstack.org/magnum/latest/user/
  [Official Kubernetes documentation]: https://kubernetes.io/docs/home/
  [Kubernetes By Example]: http://kubernetesbyexample.com/
  [awesome-kubernetes]: https://github.com/ramitsurana/awesome-kubernetes

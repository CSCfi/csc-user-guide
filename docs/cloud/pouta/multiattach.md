# Multi-attach Cinder volumes

!!! warning    
    By default the quota is set to 0, you must request it by sending an email to servicedesk@csc.fi

It is possible to attach and mount the same _cinder_ volume into more that one VM at the same time. This means that each of the VMs will be able to read and write to the same block device. This is similar to what a SAN will allow you to achieve.

![Multi attach](../img/multi-attach.drawio.svg)

This feature has several advantages and disadvantages. On one hand it allows to share files among VMs without any kind of intermediary server that you will need with solutions like `NFS` or `GlusterFS`. This reduces the number of VMs needed, thus less maintenance and less single points of failure. On the other hand, it is necessary to run what is called a [clustered file system](https://en.wikipedia.org/wiki/Clustered_file_system#SHARED-DISK) like [Oracle Cluster File System 2 (ocfs2)](https://en.wikipedia.org/wiki/OCFS2), or Red Hat [Global File System (GFS2)](https://en.wikipedia.org/wiki/GFS2). These systems need a cluster of connected daemons that will coordinate the read and write operations of the files. Other file systems like **ext4** or **xfs** do not support this use case and their use might lead to read errors or even data corruption, their use is unadvised. Each VM runs a copy of the daemon and there is no master, but a quorum based system. The choice between the two file systems depends on the use case and preferences based on vendors. In our tests GFS2 seems to be more suitable to Redhat based systems and OCFS2 to Debian ones, but your mileage might vary.

!!! Warning
    The configuration, maintenance and operations of these file systems are **not a trivial task**. The guides below are as a **starting point** and do not cover all possibilities, for more comprehensive information, please check the upstream documentation.

## Create and attach a volume

!!! Info "quota"
    Make sure that you have available quota for this kind of Volume

### WebUI

1. Go to the [Volume page](https://pouta.csc.fi/dashboard/project/volumes/) of Pouta.

1. Click in "+Create Volume"

1. Create a volume as you would do for any other **Type** of volume. Set the **Volume Name** and **Size (GiB)** as desired.

1. Change the **Type** to `standard.multiattach`.

1. Click in "Create Volume".

![Create Volume Multiattach](../img/create-volume-multiattach.png)

!!! Warning "not supported"
    You cannot attach a volume to multiple VMs from the WebUI, only see its status. You can only attach a volume to multiple VMs using the CLI.

### CLI

Before doing this, you need to [install the openstack client](../install-client/):

1. Create a multi attach volume:

    ```sh
    openstack volume create --size <size_in_GB> --type standard.multiattach <volume_name>
    ```
    You need to replace `<volume_name>` by the name you want to give to the volume, and the `<size_in_GB>` by the size in Gigabytes you want the volume to have.

1. Attach the volume to a VM node:

    ```sh
    openstack --os-compute-api-version 2.60 server add volume "<VM_name>" <volume_name>
    ```
    You need to replace the `<volume_name>` by the name of the volume you created in the previous step, and the `<VM_name>` by the name of the VM node. When doing this for a cluster of VMs, you need to run the command once per VM.

## GFS2 as an example

The Global file system or (GFS2 in short) is a file system currently developed by Red Hat. It uses [dlm](https://en.wikipedia.org/wiki/Distributed_lock_manager) to coordinate file system operations among the nodes in the cluster. The actual data is read and written directly to the shared block device.

!!! Warning
    GFS2 supports up to 16 nodes connected to the same volume. 

![GFS2 with DLM](../img/GFS2.drawio.svg)

### GFS2 ansible install

We have written a small ansible [cinder-multiattach](https://github.com/lvarin/cinder-multiattach/) playbook, that installs a cluster of nodes and installs a shared GFS2 file system on them. The playbook is intended as a guide and demo, it is not production ready. For example, there is a manual step, attach the volume in each node. The Ansible playbook will create a cluster of VMs and install the requested file system on them. The end result will be the same volume mounted in every VM. The quick start commands are these:  

```sh
$> source ~/Downloads/project_XXXXXXX-openrc.sh
Please enter your OpenStack Password for project project_XXXXXXX as user YYYYYYYY: 

$> ansible-playbook main.yml -e fs='gfs2' -e csc_username='johndoe' -e csc_password='easyaccess'

$> for i in $(seq 1 16);
do
    openstack --os-compute-api-version 2.60 server add volume "cinder-gfs2-$i" multi-attach-test-gfs2
done

$> ansible-playbook main.yml -e fs='gfs2'
```

*`csc_username` and `csc_password` can also be added in the `all.yaml`* file.  
*It can be a [robot account](../../accounts/how-to-create-new-user-account.md#getting-a-machine-to-machine-robot-account)*

You need to run Ansible twice due to a bug in the `openstack.cloud.server_volume` which can only attach the volume to a single VM and fails with the other ones.

If you already have a cluster of VMs, or want to manually create them, it is still possible to use the `gfs2` Ansible role. The steps are simple:

1. Create and attach the volume. See the manual [Create and attach a volume](#create-and-attach-a-volume) from above.

1. Create a standard Ansible inventory like this one:

    ```ini
    [all]
    <VM_name> ansible_host=192.168.1.XXX ansible_user=<user>
    # ...
    [all:vars]
    ansible_ssh_common_args='-J <jumphost>'
    ```

    In the example above you need to replace `<VM_name>` by the name of the VM, the IP `192.168.1.XXX` must be the correct IP of the VM, and finally the `<user>` has to also be replaced by the corresponding one. You need to have a line per VM node that you want to include in the cluster. Finally, if you are using a Jump Host, you need to replace `<jumphost>` by its connection information, like `ubuntu@177.51.170.99` 

1. Create a playbook like this one:

    ```yaml
    ---

    - name: Configure VMs
      hosts: all
      gather_facts: true
      become: true
      roles:
        - role: hosts
        - role: gfs2
    ```

    This will run two roles, the `hosts` one if to create a `/etc/hosts` file in every VM with the IPs and names of every VM. The `gfs2` role installs and configures the cluster.

1. And run it:

    ```sh
    $> ansible-playbook main-gfs2.yml -i inventory.ini
    ```

### GFS2 manual install

In order to install GFS2, you need to follow few steps:

1. Install the VM nodes. There is no special consideration on this step, other than making sure the nodes can see each other in the Network (it is the default behaviour of VM nodes created in the same Pouta project), and that they are installed with the same distribution version. We have tested this with `AlmaLinux-9`, other distributions and versions might also work, but we have not tested them.

1. Create and attach the volume. See the manual [Create and attach a volume](#create-and-attach-a-volume) from above.

1. For AlmaLinux and other RedHat based distributions you just need enable two collections and install few packages **on every node:**

    ```sh
    $> dnf config-manager --enable  highavailability resilientstorage
    $> dnf install pacemaker corosync pcs dlm gfs2-utils lvm2-lockd
    ```

#### Cluster setup
!!! warning "root user"
    The following commands are executed as the root user  
    It will be specified throughout this tutorial if the commands must be run on a single or every node.

1. Run the following commands **on every node:**

    ```sh
    $> systemctl start pcsd.service
    $> systemctl enable pcsd.service
    ```

1. When you install `pacemaker`, it creates a user named `hacluster`. You need to set a password to this user:
   
    ```sh
    $> passwd hacluster
    ```

1. Make sure that every node **domain name** can be resolved in every other node. In Pouta, the simplest way is to use [/etc/hosts](https://en.wikipedia.org/wiki/Hosts_(file)), where each host has a line similar to:

    ```sh
    <ip> <vm_name>
    ```

1. Run the following commands **only on one node**:

    ```
    $> pcs host auth node1 node2 node3 ...
    Username: hacluster
    Password: *******
    $> pcs cluster setup <cluster_name> node1 node2 node3 ...
    $> pcs cluster start --all
    ```

1. You can check the status by running the commands:

    ```sh
    $> pcs cluster status
    $> pcs status corosync
    ```

By default, `corosync` and `pacemaker` services are disabled:

    $> pcs status
    Daemon Status:
      corosync: active/disabled
      pacemaker: active/disabled
      pcsd: active/enabled
    
According to [pacemaker docs](https://clusterlabs.org/pacemaker/doc/2.1/Clusters_from_Scratch/html/verification.html):

    requiring a manual start of cluster services gives you the opportunity 
    to do a post-mortem investigation of a node failure 
    before returning it to the cluster.

That means, if a node crash and restart, you have to run the command `pcs cluster start [<NODENAME> | --all]` to start the cluster on it.  
You can enable them if you wish with `pcs`:

    $> pcs cluster enable [<NODENAME> | --all]
    

#### Fencing setup
!!! warning "root user"
    The following commands are executed as the root user.  
    It will be specified throughout this tutorial if the commands must be run on a single or every node.

1. Run the following commands **on every node:**

    ```sh
    $> setenforce 0
    $> sed -i.bak "s/SELINUX=enforcing/SELINUX=permissive/g" /etc/selinux/config
    $> dnf install -y fence-agents-openstack pip
    $> pip install python-openstackclient python-novaclient
    ```

1. Since we install `python-openstackclient` with the root user, you must add `/usr/local/bin` in the PATH:

    ```sh
    $> vim ~/.bashrc
    export PATH=/usr/local/bin:$PATH
    ```

1. Create a folder named `openstack` in `/etc`. Then, create a file named `clouds.yaml` in `/etc/openstack`. The YAML file must be like this:

    ```yaml
    clouds:
      ha-example:
        auth:
          auth_url: https://pouta.csc.fi:5001/v3
          project_name: project_xxxxxxx
          username: <username>
          password: <password>
          user_domain_name: Default
          project_domain_name: Default
    <. . . additional options . . .>
      region_name: regionOne
      verify: False
    ```

1. Run the following commands **only on one node:**

    ```sh
    $> pcs property set stonith-enabled=true
    ```

1. Check the value:
   
    ```sh
    $> pcs property
    ```

1. Create fencing for the HA cluster. First, you have to determine the UUID for each node in your cluster. You can run the command:
   
    ```sh
    $> openstack server list
    ```

    Then:

    ```
    $> pcs stonith create <fence_name> fence_openstack pcmk_host_map="node1:node1_UUID;node2:node2_UUID;node3:node3_UUID" power_timeout="240" pcmk_reboot_timeout="480" pcmk_reboot_retries="4" cloud="ha-example"
    ```
    Substitute `cloud="ha-example"` with the name of the cloud you specified in the `clouds.yaml` file.

1. You can view the available options with the following command:

    ```sh
    $> pcs stonith describe fence_openstack
    ```

1. You can test fencing by running these commands:
   
    ```sh
    $> pcs stonith fence node2
    $> pcs status
    $> pcs cluster start node2
    ```

!!! info "Tip"  
    If you want to start (or restart) the fence, you can use this command:
    ```sh
    $> pcs stonith cleanup <fence_name>
    ```
    Useful if you apply a new `clouds.yaml` configuration for example.


#### GFS2 setup
!!! warning "root user"
    The following commands are executed as the root user.  
    It will be specified throughout this tutorial if the commands must be run on a single or every node.

1. Run the following command **on every node:**

    ```sh
    $> sed -i.bak "s/# use_lvmlockd = 0/use_lvmlockd = 1/g" /etc/lvm/lvm.conf
    ```

1. Run the following commands **only on one node:**

    ```sh
    $> pcs property set no-quorum-policy=freeze
    ```

1. Set up a dlm (Distributed Lock Manager) resource:

    ```sh
    $> pcs resource create dlm --group locking ocf:pacemaker:controld op monitor interval=30s on-fail=fence
    ```

1. Clone the resource for the others nodes:

    ```sh
    $> pcs resource clone locking interleave=true
    ```

1. Set up a lvmlockd resource part of the locking resource group:

    ```sh
    $> pcs resource create lvmlockd --group locking ocf:heartbeat:lvmlockd op monitor interval=30s on-fail=fence
    ```

1. Check the status:

    ```sh
    $> pcs status --full
    ```

1. Still **only on one node**, create one shared volume groups:

    ```sh
    $> vgcreate --shared shared_vg1 /dev/vdb
    ```

1. **On the other nodes**, add the shared device to the device file:

    ```sh
    $> lvmdevices --adddev /dev/vdb
    ```

1. Start the lock manager:

    ```sh
    $> vgchange --lockstart shared_vg1
    ```

1. **On one node**, run:

    ```sh
    $> lvcreate --activate sy -L <size>G -n shared_lv1 shared_vg1
    $> mkfs.gfs2 -j <number_of_nodes> -p lock_dlm -t ClusterName:FSName /dev/shared_vg1/shared_lv1
    ```
    ClusterName is the name of the cluster (you can retrieve the information with the command `pcs status`)  
    FSName is the file system name (i.e: gfs2-demo)

1. Create an LVM-activate resource to automatically activate that logical volume on all nodes:

    ```sh
    $> pcs resource create sharedlv1 --group shared_vg1 ocf:heartbeat:LVM-activate lvname=shared_lv1 vgname=shared_vg1 \
        activation_mode=shared vg_access_mode=lvmlockd
    ```

1. Clone the new resource group:

    ```sh
    $> pcs resource clone shared_vg1 interleave=true
    ```

1. Configure ordering constraints to ensure that the locking resource group that includes the dlm and lvmlockd resources starts first:

    ```sh
    $> pcs constraint order start locking-clone then shared_vg1-clone
    ```

1. Configure a colocation constraints to ensure that the vg1 resource groups start on the same node as the locking resource group:

    ```sh
    $> pcs constraint colocation add shared_vg1-clone with locking-clone
    ```

1. Verify on the nodes in the cluster that the logical volume is active. There may be a delay of a few seconds:

    ```sh
    $> lvs
        LV         VG         Attr       LSize   Pool Origin Data%  Meta%  Move Log Cpy%Sync Convert
        shared_lv1 shared_vg1 -wi-a----- <size>g
    ```

1. Create a file system resource to automatically mount the GFS2 file system.  
   Do not add it to the /etc/fstab file because it will be managed as a Pacemaker cluster resource:

    ```sh
    $> pcs resource create sharedfs1 --group shared_vg1 ocf:heartbeat:Filesystem device="/dev/shared_vg1/shared_lv1" \
        directory="/mnt/gfs" fstype="gfs2" options=noatime op monitor interval=10s on-fail=fence
    ```

1. You can verify if the GFS2 file system is mounted:

    ```sh
    $> mount | grep gfs2
    $> pcs status --full
    ```


### GFS2 FAQ

* **How to add more nodes?**

    It is possible to add new nodes to a GFS2 cluster. The supported **limit** is **16** nodes.

    First you need to make sure there are enough journal entries. Use `gfs2_edit` to get the total number of journals:

    ```sh
    sudo gfs2_edit -p jindex /dev/vdb | grep journal
    ```

    If it is not enough, you can easily add more with `gfs2_jadd`: 

    ```sh
    $> sudo gfs2_jadd -j 1 /mnt
    Filesystem: /mnt
    Old journals: 15
    New journals: 16
    ```

    Secondly, create the new node, install the required software and attach the volume using openstack API. The process is described above.

    Then you need to edit the file `/etc/corosync/corosync.conf` in every node and add an entry for the new one:

    ```json
    node {
     ring0_addr: cinder-gfs2-16
     nodeid: 16
    }
    ```

    Once the file is updated, you need to stop the mount and restart the dlm and corosync daemons in every node in the cluster.

    Finally, you just need to mount the volume:

    ```sh
    $> pcs resource create sharedfs1 --group shared_vg1 ocf:heartbeat:Filesystem device="/dev/shared_vg1/shared_lv1" directory="/mnt/gfs" fstype="gfs2" options=noatime op monitor interval=10s on-fail=fence
    ```

* **What happens if a VM gets disconnected?**

    This covers two different use cases, a temporal and/or unexpected disconnection, and a permanent one.

    For a temporal and unexpected disconnection, the cluster should be able to deal with this kind of issues automatically. After the node is back, you need to check that all came back to normal. In some cases the automatic mount of the volume can fail, if so mount the volume as explained above.

    If it is temporal but expected, like to update the kernel version. Umount the volume in the node before rebooting the node. It is not required, but recommended.

    For a permanent disconnection of a VM, one need to do the inverse process of adding a new node. Umount the volume, remove the entry for this VM in the `/etc/corosync/corosync.conf` file of every node, and finally restart the daemons in every node. This needs to be done as it affects the quorum count for the cluster.

* **Is it possible to mount a node as read-only?**

    Yes, GFS2 has the "spectator mode":

    ```
    spectator
       Mount  this filesystem using a special form of read-only mount.  The mount does not
       use one of the filesystem's journals. The node is unable to  recover  journals  for
       other nodes.

    norecovery
       A synonym for spectator
    ```

    So, just run this command:

    ```sh
    $> pcs resource create sharedfs1 --group shared_vg1 ocf:heartbeat:Filesystem device="/dev/shared_vg1/shared_lv1" directory="/mnt/gfs" fstype="gfs2" options=noatime,spectator op monitor interval=10s on-fail=fence
    ```
    `fstype="gfs2"` is not strictly necessary, as mount can detect the file system type, but it is recommended to avoid mounting the wrong file system.
    Then double check that the mount went as expected by:

    ```sh
    $ mount | grep /mnt
    /dev/vdb on /mnt type gfs2 (ro,relatime,spectator,rgrplvb)
    ```

### GFS2 Links

- [Pacemaker docs](https://clusterlabs.org/pacemaker/doc/2.1/Clusters_from_Scratch/html/cluster-setup.html)
- [GFS2 on Amazon EBS Multi-Attach](https://aws.amazon.com/blogs/storage/clustered-storage-simplified-gfs2-on-amazon-ebs-multi-attach-enabled-volumes/)
- [Getting start with Pacamaker](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_and_managing_high_availability_clusters/assembly_getting-started-with-pacemaker-configuring-and-managing-high-availability-clusters#proc_learning-to-use-pacemaker-getting-started-with-pacemaker)
- [Configuring a Red Hat High Availability cluster on Red Hat OpenStack Platform](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_a_red_hat_high_availability_cluster_on_red_hat_openstack_platform/index)
- [GFS2 file systems in a cluster](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_gfs2_file_systems/assembly_configuring-gfs2-in-a-cluster-configuring-gfs2-file-systems#proc_configuring-gfs2-in-a-cluster.adoc-configuring-gfs2-cluster)

## OCFS2 as a second example

The [Oracle Cluster File System](https://en.wikipedia.org/wiki/OCFS2) version 2 is a shared disk file system developed by Oracle Corporation and released under the GNU General Public License. Meanwhile it is a different code base developed by a different vendor. The approach is the same as GFS2:

![OCFS2](../img/OCFS2.drawio.svg)

A single volume attached to a cluster of VM nodes, allowing the data reads and writes to be done directly, and a daemon running in each VM node that coordinates the read and write operations.

### OCFS2 ansible install

Like with GFS2, the Ansible playbook will create a cluster of VMs and install the requested file system on them. The end result will be the same volume mounted in every VM. It is very similar than the instructions for GFS2. The quick start commands are these:

```sh
$ source ~/Downloads/project_XXXXXXX-openrc.sh
Please enter your OpenStack Password for project project_XXXXXXX as user YYYYYYYY: 

$ ansible-playbook main.yml -e fs='ocfs2'

$ for i in $(seq 1 16);
do
    openstack --os-compute-api-version 2.60 server add volume "cinder-ocfs2-$i" multi-attach-test-ocfs2
done

$ ansible-playbook main.yml -e fs='ocfs2'
```

You need to run Ansible twice due to a bug in the `openstack.cloud.server_volume` which can only attach the volume to a single VM and fails with the other ones.

If you already have a cluster of VMs, or want to manually create them, it is still possible to use the ocfs2 Ansible role. The steps are simple:

1. Create and attach the volume. See the manual [Create and attach a volume](#create-and-attach-a-volume) from above.

1. Create a standard Ansible inventory like this one:

    ```ini
    [all]
    <VM_name> ansible_host=192.168.1.XXX ansible_user=<user>
    # ...
    [all:vars]
    ansible_ssh_common_args='-J <jumphost>'
    ```

    In the example above you need to replace `<VM_name>` by the name of the VM, the IP `192.168.1.XXX` must be the correct IP of the VM, and finally the `<user>` has to also be replaced by the corresponding one. You need to have a line per VM node that you want to include in the cluster. Finally, if you are using a Jump Host, you need to replace `<jumphost>` by its connection information, like `ubuntu@177.51.170.99`

1. Create a playbook (`main-ocfs2.yml` in this example) like this one:

    ```yaml
    ---

    - name: Configure VMs
      hosts: all
      gather_facts: true
      become: true
      roles:
        - role: hosts
        - role: ocfs2
    ```

    This will run two roles, the hosts one if to create a `/etc/hosts` file in every VM with the IPs and names of every VM. The `ocfs2` role installs and configures the cluster.

1. And run it:

    ```sh
    $ ansible-playbook main-ocfs2.yml -i inventory.ini

    ```

### OCFS2 manual install

In order to install OCFS2, you need to follow few steps:

1. Install the VM nodes. There is no special consideration on this step, other than making sure the nodes can see each other in the Network (it is the default behaviour of VM nodes created in the same Pouta project), and that they are installed with the same distribution version. We have tested this with `Ubuntu v22.04` and `AlmaLinux-9`, other distributions and versions might also work, but we have not tested them. This guide will use **Ubuntu** as an example.  
AlmaLinux requires to install an specific [Oracle kernel](https://support.oracle.com/knowledge/Oracle%20Linux%20and%20Virtualization/1253272_1.html). More information in the [FAQ](#ocfs2-faq)

1. Create and attach the volume. See the manual [Create and attach a volume](#create-and-attach-a-volume) from above.

1. Install the OCFS2 software:

    ```sh
    ocfs2-tools linux-modules-extra-<kernel_version> linux-image-$(uname -r)
    ```
    We have tested this with `<kernel_version>` == `6.5.0-21-generic`, but newer versions should work as well or better.

1. Make sure that every node domain name can be resolved in every other node. In Pouta, the simplest way is to use [/etc/hosts](https://en.wikipedia.org/wiki/Hosts_(file)), where each host has a line similar to:

    ```sh
    <ip> <vm_name>
    ```

1. Enable ocfs2 in every node using:

    ```sh
    sudo dpkg-reconfigure ocfs2-tools
    ```

1. Create the file system. You need to do this in **only one** of the VM nodes.

    ```sh
    mkfs.ocfs2 -N <number_instances> /dev/vdb
    ```

    Replace `<number_instances>` by the number of VM nodes in the cluster. Pay also attention and double check that `/dev/vdb` is the proper volume name. In principle `vdb` is going to be the first attached volume to a VM, but this might not be true in all cases.

1. Generate the file `/etc/ocfs2/cluster.conf`. A minimal working example would follow this template:

    ```
    {% for host in groups['all'] %}
    node:
      ip_port = 7777
      ip_address = {{ hostvars[host]['ansible_host'] }}
      number = {{ groups['all'].index(host)+1 }}
      name = {{ host }}
      cluster = ocfs2
    {% endfor %}
    cluster:
      node_count = {{ number_instances }}
      name = ocfs2
    ```

1. Reboot so the kernel you installed is taken into use. Make sure that the `ocfs2` service is up and running (`systemctl status ocfs2`).

1. Finally mount the volume in each node:

    ```sh
    sudo mount /dev/vdb /mnt
    ```
    As the device may change in any moment, it is recommended to use the `UUID` for any serious deployment. You can get the `UUID` by using the command `blkid`:

    ```sh
    $ sudo blkid /dev/vdb
    /dev/vdb: UUID="785134b8-4782-4a1f-8f2a-40bbe7b7b5d2" BLOCK_SIZE="4096" TYPE="ocfs2"
    ```
    In this case the command will be `sudo mount -U 785134b8-4782-4a1f-8f2a-40bbe7b7b5d2 /mnt`


### OCFS2 FAQ

- **How to add more nodes?**

    It is possible to add more nodes to a ocfs2 cluster, but it requires a downtime.

    First you need to increase the number of slots, using `tunefs.ocfs2`. Before that, you need to umount the volume in every VM node. These are the two commands you need to run. The second one only needs to be executed in a single node:

    ```sh
    sudo umount /mnt
    sudo tunefs.ocfs2 -N 25 /dev/vdb
    ```

    Secondly, create the new node, install the required software and attach the volume using openstack API. The process is described above.

    Then you need to edit the file `/etc/ocfs2/cluster.conf` in every node and add an entry for the new one:

    ```yaml
    node:
      ip_port = 7777
      ip_address = <ip_address>
      number = <number>
      name = <vm_name>
      cluster = ocfs2
    ```

    Replace `<ip_address>` by the address of the new server, `<vm_name>` by its name, and finally `<number>` is the node id number. It has to be unique for every node, ideally consecutive numbers.

    Once the file is updated, you need to stop the mount and restart the `ocfs2` in every node in the cluster. Lastly, remount the volume in every VM node.

* **What happens if a VM gets disconnected?**

    This covers two different use cases, a temporal and/or unexpected disconnection, and a permanent one. It is very similar to the GFS2 situation.

    For a temporal and unexpected disconnection, the cluster should be able to deal with this kind of issues automatically. After the node is back, you need to check that all came back to normal. In some cases the automatic mount of the volume can fail, if so mount the volume as explained above.

    If it is temporal but expected, like to update the kernel version. Umount the volume in the node (`sudo umount /mnt`) before rebooting the node. It is not required, but recommended.

    For a permanent disconnection of a VM, one need to do the inverse process of adding a new node. Umount the volume (`sudo umount /mnt`), remove the entry for this VM in the `/etc/ocfs2/cluster.conf` file of every node, and finally restart the daemons in every node. This needs to be done as it affects the quorum count for the cluster.

* **Is it possible to mount a node as read-only?**

    Yes, it is possible to mount the volume as read-only. It is as simple as:

    ```sh
    sudo mount /dev/vdb /mnt -o ro
    ```

    After that, you can check that it was indeed mounted as read-only by:

    ```sh
    mount | grep /mnt
    /dev/vdb on /mnt type ocfs2 (ro,relatime,_netdev,heartbeat=local,nointr,data=ordered,errors=remount-ro,atime_quantum=60,coherency=full,user_xattr,acl)
    ```
    Also, as you can see in the output above, the default behaviour is that when any error occurs, to remount it as read only (`errors-remount-ro`). See `mount.ocfs2` for more options.

* **I want to install Oracle Kernel on a RedHat 9 distro**  

    You can find more information [here](https://yum.oracle.com/getting-started.html#red-hat-enterprise-linux-centos) on how to install the Oracle Linux repo. Once set, you can install the Oracle UEK kernel with these commands:

    First
    ```sh
    sudo dnf install oraclelinux-release-el9
    ```

    And then
    ```sh
    sudo dnf install kernel-uek
    ```

## Upstream documentation

- GFS2: 
    - <https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_gfs2_file_systems/index>
- OCFS2: 
    - <https://ocfs2.wiki.kernel.org/>
    - <https://public-yum.oracle.com/>
    - <https://docs.oracle.com/en/operating-systems/oracle-linux/9/shareadmin/shareadmin-ManagingtheOracleClusterFileSystemVersion2inOracleLinux.html#about-ocfs2>
    - <https://docs.oracle.com//en/learn/ocfs2_cluster_linux_8/#introduction>
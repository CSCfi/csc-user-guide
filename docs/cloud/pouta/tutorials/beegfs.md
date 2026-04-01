# Set up BeeGFS 8.3 file system

In this section will learn how to install BeeGFS file system on Pouta.

This deployment guide has been tested on **AlmaLinux 9**.

## What is [BeeGFS](https://doc.beegfs.io/latest/overview/overview.html)

Developed with a strong focus on performance and designed for ease of use, simple installation, and management, BeeGFS is one of the leading parallel file systems that continues to grow and gain significant popularity in the community. BeeGFS has evolved into a world-wide valued filesystem offering maximum performance, scalability, high flexibility, and robustness.

BeeGFS is available free of charge for end-users. For enterprise systems, professional commercial support is also available, typically in cooperation with our international turn-key solution partners.

### Key Benefits

- Distributed File Contents and Metadata

One of the most fundamental concepts of BeeGFS is the strict avoidance of architectural bottlenecks. Striping file contents across multiple storage servers is only one part of this concept. Another important aspect is the distribution of file system metadata (e.g., directory information) across multiple metadata servers. Large systems and metadata intensive applications, in general, can greatly profit from the latter feature.

- HPC Technologies

BeeGFS is built on highly efficient and scalable multithreaded core components with native RDMA support. File system nodes can serve RDMA (InfiniBand, Omni-Path, RoCE) and TCP/IP network connections at the same time and automatically switch to a redundant connection path in case any of them fails.

- Easy to Use

BeeGFS requires no kernel patches (the client is a patchless kernel module, the server components are userspace daemons), comes with graphical cluster installation tools and allows you to add more clients and servers to the running system whenever you want it.

- Optimized for Highly Concurrent Access

Simple remote file systems like NFS do not only have serious performance problems in case of highly concurrent access, they can even corrupt data when multiple clients write to the same shared file, which is a typical use-case for cluster applications. BeeGFS was specifically designed with such use-cases in mind to deliver optimal robustness and performance in situations of high I/O load.

- Client and Server on any Machine

No specific enterprise Linux distribution or other special environment is required to run BeeGFS. BeeGFS client and servers can even run on the same machine to enable performance increases for small clusters or networks. BeeGFS requires no dedicated file system partition on the servers - It uses existing partitions, formatted with any of the standard Linux file systems, e.g., XFS, ext4 or ZFS. For larger networks, it is also possible to create several distinct BeeGFS file system partitions with different configurations.

## System Requirements

Check out the [official documentation](https://doc.beegfs.io/latest/system_design/system_requirements.html)

We will install the metadata on a separate volumes. Like [mentioned](https://doc.beegfs.io/latest/system_design/system_requirements.html#metadata-nodes) in the documentation:

> As a rule of thumb, 500GB of metadata capacity are sufficient for about 150 million files
> Note that while ext4 is generally recommended for metadata storage because of its performance advantages for BeeGFS metadata workloads compared to other local Linux file systems, XFS has the advantage of using a dynamic number of inodes, meaning new inodes can be created as long as there is free disk space

## Quick Start Guide

The [BeeGFS documentation](https://doc.beegfs.io/8.3/) is very rich and instructive on how to install BeeGFS 8.3.

In this tutorial, we use the following:

- Software: AlmaLinux 9

- Host Services:  
    - `beegfs-meta`: Metadata server with a 500 Gb volume attached
    - `beegfs-mgmt`: Management server
    - `beegfs-storage-1`: Storage server 1 with a 1000 Gb volume attached
    - `beegfs-storage-2`: Storage server 2 with two 1000 Gb volumes attached
    - `beegfs-storage-3`: Storage server 3 with a 1000 Gb volume attached
    - `beegfs-client-1`: Client 1
    - `beegfs-client-2`: Client 2

### [Package download and installation](https://doc.beegfs.io/latest/quick_start_guide/quick_start_guide.html#step-1-package-download-and-installation)

You can find the different packages from this address: [https://www.beegfs.io/release/](https://www.beegfs.io/release/)

For AlmaLinux 9, run these commands with `root` user on every nodes:

```sh
yum install -y epel-release wget vim
yum update -y
rpm --import https://www.beegfs.io/release/beegfs_8.3/gpg/GPG-KEY-beegfs
wget https://www.beegfs.io/release/beegfs_8.3/dists/beegfs-rhel9.repo -O /etc/yum.repos.d/beegfs.repo
```

Then, depending on the node, run this command with `root` user:

- `beegfs-mgmt` node:

```sh
yum install -y beegfs-mgmtd libbeegfs-license
```

- `beegfs-meta` node:

```sh
yum install -y beegfs-meta
```

- `beegfs-storage` nodes:

```sh
yum install -y beegfs-storage
```

- `beegfs-client` nodes:

```sh
yum install -y kernel-devel-$(uname -r) beegfs-client beegfs-tools beegfs-utils
```

## Configuration

### [Management service](https://doc.beegfs.io/latest/quick_start_guide/quick_start_guide.html#management-service)

To initialize the database for a new BeeGFS installation run on the `beegfs-meta` node with `root` user:

```sh
/opt/beegfs/sbin/beegfs-mgmtd --init
```

Edit the file `/etc/beegfs/beegfs-mgmtd.toml`

By default, the management service requires configuring TLS. You can disable it by setting `tls-disable = true`

We recommend to change the log-level to debug `log-level = debug`

Save and exit. Restart the service:

```sh
systemctl restart beegfs-mgmtd
```

### [Metadata service](https://doc.beegfs.io/latest/quick_start_guide/quick_start_guide.html#metadata-service)

Earlier, we presented the different Host Services. In this tutorial, we consider the server `beegfs-meta` with a 500 Gb volume attached.

First, we need to prepare the volume. We have a [documentation](../persistent-volumes.md#using-attached-volumes) on how to use an attached volume.

Here are the detailed instructions for our case:

- List the volumes:

  ```sh
  sudo parted -l
  ```

- Assuming that the attached volume is `/dev/vdb`, format it:

  ```sh
  sudo mkfs.xfs /dev/vdb
  ```

- Create the folder `/mnt/beegfs_meta`:

  ```sh
  sudo mkdir -p /mnt/beegfs_meta
  ```

- Mount the volume:

  ```sh
  sudo mount -o noatime /dev/vdb /mnt/beegfs_meta
  ```

- Edit `/etc/fstab` and add this entry:

  ```
  /dev/vdb                /mnt/beegfs_meta                          xfs     defaults        0 0
  ```

Once the volume is attached and mounted, we can proceed with the initialisation of the metadata service (with the `root` user).

The metadata service needs to know where it can store its data and where the management service is running. Typically, you will have multiple metadata services running on different machines. In our case, we only use one.

Optionally, you can also define a custom numeric metadata service ID (range 1..65535). We will pick number 2 as metadata service ID here.

```sh
/opt/beegfs/sbin/beegfs-setup-meta -p /mnt/beegfs_meta -s 2 -m IP_ADDRESS_MGMT_NODE
```

_Replace IP_ADDRESS_MGMT_NODE by the internal IP of your `beegfs-mgmt` server_

Last thing to check, edit the file `/etc/beegfs/beegfs-meta.conf` and verify that `storeClientXAttrs=true`

### [Storage service](https://doc.beegfs.io/latest/quick_start_guide/quick_start_guide.html#storage-service)

Earlier, we presented the different Host Services. In this tutorial, we consider:

- `beegfs-storage-1` with a 1000 Gb volume attached.

- `beegfs-storage-2` with two 1000 Gb volumes attached.

- `beegfs-storage-3` with a 1000 Gb volume attached.

The instructions to prepare the volumes are the same as [previously](#metadata-service) for the Metadata service. You can also check our [documentation](../persistent-volumes.md#using-attached-volumes)

The storage service needs to know where it can store its data and how to reach the management server.

Typically, you will have multiple storage services running on different machines and/or multiple storage targets (e.g., multiple RAID volumes) per storage service.

Optionally, you can also define a custom numeric storage service ID and numeric storage target ID (both in range 1..65535). As this service is running on a server with name `beegfs-client-1` in our example, we will pick number 1 as ID for this storage service and we will use 101 as storage target ID to show that this is the first target (01) of storage service 1.

With the `root` user, run:

```sh
/opt/beegfs/sbin/beegfs-setup-storage -p /mnt/beegfs_storage-1 -s 1 -i 101 -m IP_ADDRESS_MGMT_NODE
```

_Replace IP_ADDRESS_MGMT_NODE by the internal IP of your `beegfs-mgmt` server_

The node `beegfs-storage-2` has two 1000 Gb volumes attached. You can use this command to add the two volumes in the same service ID:

```sh
/opt/beegfs/sbin/beegfs-setup-storage -p /mnt/beegfs_storage-1 -s 2 -i 201 -m IP_ADDRESS_MGMT_NODE
/opt/beegfs/sbin/beegfs-setup-storage -p /mnt/beegfs_storage-2 -s 2 -i 202
```

### [Client](https://doc.beegfs.io/latest/quick_start_guide/quick_start_guide.html#client)

The clients need to know where the management service is running.

With the `root` user, run:

```sh
/opt/beegfs/sbin/beegfs-setup-client -m IP_ADDRESS_MGMT_NODE
```

_Replace IP_ADDRESS_MGMT_NODE by the internal IP of your `beegfs-mgmt` server_

The client mount directory is defined in a separate configuration file. This file will be used by the beegfs-client service startup script. By default, BeeGFS will be mounted to `/mnt/beegfs`. Thus, you need to perform this step only if you want to mount the file system to a different location.

```sh
vim /etc/beegfs/beegfs-mounts.conf
```

The first entry defines the mount directory. The second entry refers to the corresponding configuration file for this mount point.

Last thing to check, edit the file `/etc/beegfs/beegfs-client.conf` and verify that `sysSELinuxEnabled=true`

### [Authentication](https://doc.beegfs.io/latest/advanced_topics/authentication.html)

It is highly recommended to secure your BeeGFS installation by enabling connection-based authentication using a shared secret.

For our case, we will distribute a shared secret to all nodes and setting the `connAuthFile` parameter for each service/client configuration. By default, services and clients expect the secret at `/etc/beegfs/conn.auth`

!!! important "Authentication disable - NOT RECOMMENDED"  
    You can disable the authentication by setting `connDisableAuthentication=true` in all service and configuration files (located in `/etc/beegfs/*.conf`) and setting `auth-disable=true` in the Management Service configuration (`etc/beegfs/beegfs-mgmtd.toml`). The services need to be restarted for the changes to take effect.

1. Create a file which contains a shared secret

```sh
dd if=/dev/random of=/etc/beegfs/conn.auth bs=128 count=1
```

2. Ensure the file is only readable by the root user:

```sh
chown root:root /etc/beegfs/conn.auth
chmod 400 /etc/beegfs/conn.auth
```

Copy the file to all hosts in the cluster (mgmtd, meta, storage, client).

If this is a new BeeGFS 8 installation, the default configuration files for all services and clients will already have the authentication file path set to /etc/beegfs/conn.auth.

If you are enabling connection authentication for the first time, in your management configuration file set `auth-file = "/etc/beegfs/conn.auth"` and for all other clients and servers set `connAuthFile=/etc/beegfs/conn.auth`.

Restart the services so the change takes effect:

```sh
systemctl restart beegfs-mgmtd.service
systemctl restart beegfs-meta.service
systemctl restart beegfs-storage.service
systemctl restart beegfs-client.service
systemctl restart beegfs-mon.service
```

After all services have correctly restarted no client without the shared secret file can connect the cluster. Without the shared secret file, the management daemon will log the following when `log-level = "debug"`:

```
Received message from unauthenticated stream from 192.168.1.7:36082
```

You can change the secret on an already configured/secured cluster. Just replace the file `conn.auth` on all nodes with a new one.

### Service startup

BeeGFS services can be started in arbitrary order by using the corresponding systemctl service scripts. By default all services log to the system journal (use the -u <service> to filter logs for a particular service).

With the `root` user, run:

```sh
systemctl start beegfs-mgmtd
systemctl start beegfs-meta
systemctl start beegfs-storage # repeat this operation for all storage nodes
systemctl start beegfs-client # repeat this operation for all client nodes
```

!!! note  
    BeeGFS clients have a mount sanity check and cancel a mount operation if servers are unreachable. If you want to mount even with unreachable servers, set `sysMountSanityCheckMS=0` in the file `/etc/beegfs/beegfs-client.conf`.

Congratulations, your parallel file system is now up and running!

### Check connectivity

Setup your client node to interact with BeeGFS using the new beegfs tool.

The new tool does not use a configuration file, but rather uses flags and/or environment variables for configuration. This means if you want persistent configuration for the tool it can be set in your ~/.bashrc file (or equivalent for your shell).

If you followed the recommendations in the quick start guide no additional configuration is required, and the tool will work out of the box. Below is common configuration to be aware of in case you deviated from the guide.

If you choose to use a self-signed TLS certificate and enable connection authentication, as long as the TLS certificate and secret are already at `/etc/beegfs/cert.pem` and `/etc/beegfs/conn.auth` on the machine where you are running the tool, then no configuration is needed. If you choose to disable TLS and/or connection authentication you will also need to specify those options on the client nodes:

```sh
echo "export BEEGFS_TLS_DISABLE='true'" >> ~/.bashrc
source ~/.bashrc
```

Once you have the correct configuration in place, on the client nodes, check the detected network interfaces and transport protocols with the following commands (with the `root` user):

```sh
beegfs node list --with-nics
beegfs health net            # Display connections the client is actually using.
beegfs health df             # Display free space and inodes on metadata and storage targets.
beegfs health check          # Check for common issues.
```

If you intend to use the BeeGFS community edition you will have seen warnings when running commands that the system is unlicensed. Run `beegfs license` and follow the steps to obtain a license.

## [Licensing](https://doc.beegfs.io/latest/advanced_topics/licensing.html)

### Obtaining licenses

To obtain a community license upgrade to BeeGFS 8.3+ and run `beegfs license`. This will generate a system specific URL that automatically provides limited information about the deployment including the storage capacity, number of metadata and storage services, and the network protocol.

### Configuring licensing

These steps can be followed to enable licensing on a new or existing BeeGFS install:

1. Install the `libbeegfs-license` package on all machines that may run the BeeGFS management service. If the BeeGFS management service can run on multiple machines, this package should be installed everywhere the BeeGFS management service can run. Starting with BeeGFS 8.3 this package will automatically be installed on all machines where the management package is installed.

    !!! note  
        without the management service running on the same machine, installing this package has no effect, so it is safe to install anywhere it might be needed.

2. On all machines where the BeeGFS management service can run, download your license file to `/etc/beegfs/license.pem`.

3. Perform one of the following options to reload the license:

    - If this is a new install simply start the management service. The following will be logged if the license verification library and license are installed correctly:
        
        ```
        [2024-12-05T14:49:31Z INFO ] Successfully initialized certificate verification library.
        [2024-12-05T14:49:31Z INFO ] Successfully loaded license certificate: TMP-513679565
        ```

    - If this is an existing deployment, from a machine with the `beegfs-tools` package installed run `beegfs license --reload` to install a new license without requiring any downtime. The license details will be returned on success.

Optionally verify the details of the installed license with `beegfs license`.

### Renewing or updating a license

If the license ever needs to be updated, for example when extending support contract duration or adding additional servers, simply place the new license file at the path configured in the management service and run the `beegfs license --reload` command. The new license will be applied immediately and without the need for a restart of the management service.

## About the license

- You can **freely use BeeGFS Community Edition** for your projects without paying.
- There are **no fees or mandatory constraints on usage** for either personal or commercial use.
- Redistribution and modification have some restrictions under the Community License.
- For **enterprise needs, support, or advanced features**, you’d consider the paid Enterprise Edition.

The BeeGFS Community Edition is governed by the BeeGFS Community License, which you accept by using the software. If you do not agree to the license terms, you should not install, copy, or use BeeGFS.

Key points from the license include:

- The license allows you to use the software freely, but it comes with terms you must comply with.
- Redistribution and modification are restricted; you cannot redistribute modified versions without explicit permission.
- The software is provided "as-is," meaning there is no warranty or guarantee for its performance or suitability.
- The license is designed to protect the intellectual property of the BeeGFS creators while allowing free use for both personal and commercial purposes.

## Migrate the metadata nodes

If you have deployed your metadata on the local disk, you won't be able to extend the volume.

You can easily migrate the metadata for `/` to a mounted volume. The best way to accomplish this is to run `rsync`

Once your volume has been formatted and mounted, you can run these commands (with `root` user):

```sh
systemctl stop beegfs-meta
rsync -aHAX --numeric-ids /data/beegfs/beegfs_meta/ /mnt/beegfs_meta/
systemctl start beegfs-meta
```

!!! important  
    **DO NOT** re-register the metadata service with `/opt/beegfs/sbin/beegfs-setup-meta -p /data/beegfs/beegfs_meta -s 2 -m IP_ADDRESS_MGMT_NODE` The management service will be confused because it will generate a new registration token and won't be able to start the service

## [Benchmark](https://doc.beegfs.io/latest/advanced_topics/benchmark.html)

BeeGFS comes with a tool that allows you to benchmark the storage

The commands below are run the `root` user.

The following example starts a write benchmark on all targets of all BeeGFS storage servers with an IO blocksize of 512 KB, using 10 threads (i.e., simulated client streams) per target, each of which will write 200 GB of data to its own file.

```sh
beegfs benchmark start --block-size=512KiB --size=200GiB --num-tasks=10
```

To query the benchmark status/result of all targets, execute the command below.

```sh
beegfs benchmark status
```

You can use the watch flag for repeating the query in a given interval in seconds, as shown below:

```sh
beegfs benchmark status --watch=1s
```

The generated files will not be automatically deleted when a benchmark is complete. You can delete them by using the following command.

```sh
beegfs benchmark cleanup
```

More details about the storage benchmark and its options are available in the help of the beegfs tool, as follows.

```sh
beegfs benchmark --help
beegfs benchmark start --help
beegfs benchmark status --help
```

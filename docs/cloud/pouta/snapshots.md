## Snapshots

This article describes how to use Snapshots to capture and store 
the file system state of a Pouta virtual machine.

### Types of snapshots

There are two types of snapshots used in OpenStack: image (instance)
snapshots and volume snapshots. Both snapshot types can be utilized
when creating a new instance. Image snapshots are more common.

![Snapshot types](/img/Screenshot-Horizon-Instances-Bootsource.png)

Image snapshots hold the state of a given instance's root disk, and
can typically be used as bootable images. **Please note** that
if the instance has an ephemeral disk, the contents of the ephemeral
disk are **not** captured in the snapshot.

Image snapshots are managed in **Compute \| Images** in the web UI.
For instructions on creating image snapshots, please see the section
*Creating an image based on an existing image* in the [next chapter].

Volume snapshots capture the state of a persistent volume. They can be
used e.g. for a one-time backup before an upgrade operation that
touches the volume contents. Volume snapshots are managed in **Compute
\| Volumes** in the web UI.

### General considerations

There is presently one [known issue] related to
snapshots, to be fixed in a future IaaS upgrade.

We recommend powering off the instance before taking a snapshot of it.
This is the best way to make sure the file system is captured in a
consistent state.

Please note that snapshots may not always be the optimal method of
getting an instance into a predefined state. For longer term cloud
usage, configuration automation tools should be considered. These
mostly replace snapshots by starting from scratch and then
automatically setting up the relevant software and
configurations. Ansible and Puppet are such tools. 
Using these tools, you can use the automatization benefits of
the cloud more efficiently and benefit from the latest security updates upon
instance creation (as long as CSC-built images are used).

!!! note
    Note to CSC: add links above to the configuration automation tools.

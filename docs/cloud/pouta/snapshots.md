## Snapshots

This article describes how to use Snapshots to capture and store 
filesystem state of a Pouta virtual machine.

### Types of snapshots

There are two  types of snapshots used in  OpenStack: image (instance)
snapshots and  volume snapshots. Both  snapshot types can  be utilized
when creating  a new instance,  image snapshots being the  more common
use case for this.

![Snapshot types](/img/Screenshot-Horizon-Instances-Bootsource.png)

Image snapshots  hold the state of  a given instance's root  disk, and
thus can typically  be used as a bootable image.  **Please note** that
if the instance  has an ephemeral disk, the contents  of the ephemeral
disk are **not** captured into the snapshot.

Image snapshots are managed under **Compute \| Images** in the web UI.
For  instructions  on  creating  image snapshots  please  see  section
*Creating an image based on an existing image* in the [next chapter].

Volume snapshots capture the state of a persistent volume. They can be
used for example for one-time  backup before an upgrade operation that
touches volume contents. Volume  snapshots are managed under **Compute
\| Volumes** in the web UI.

### General Considerations

At  the  time  of  writing  there is  one  [known  issue]  related  to
snapshots, to be fixed in a future IaaS upgrade.

We recommend powering off an instance  before taking a snapshot of it.
This is  the best way to  make sure the  file system is captured  in a
consistent state.

Please note  that snapshots may  not always  be the optimal  method of
getting an  instance into  a predefined state.  For longer  term cloud
usage,  configuration automation  tools  should  be considered.  These
mostly  replace   using  snapshots  by  starting   from  scratch  then
automatically      setting      up     relevant      software      and
configurations. Examples  of these  tools are  Ansible and  Puppet. By
using these tools  one can get more of the  automatization benefits of
the  cloud,  and get  the  benefit  of  latest security  updates  upon
instance creation (as long as CSC built images are used).

!!! note
    Note to CSC: add links above to configuration automation tools

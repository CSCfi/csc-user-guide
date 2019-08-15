## Billing
For Puhti a new billing scheme is introduced. Taito billing is not changed.
### Puhti compute billing
Puhti is a heterogenous system with CPU, GPU and IO nodes and nodes with varying amount of memory. Moreover, it is possible to use only a fraction of a node and its various resources. The billing scheme tries to charge the billing units (BUs) in fair way based on the reserved amount of node resources.

In the billing scheme the BU consumption rate of a compute job depends linearly on the number of requested cores and GPUs and the amount of requested memory (per core). More precisely,
* each reserved core consumes **5** BUs per hour
* each starting 10 GiB block of reserved memory consumes **5** BUs per hour
* each reserved GPU consumes **30** BUs per hour
and the total BU consumption per hour is the sum of the above terms:

We plan to introduce similar billing for the fast local NVME disks.

### Storage billing
#### Lustre/work disk billing
#### Allas object storage billing

# How fast is the Pouta network?

The network is a mix of 40 Gb/s and 10 Gb/s Ethernet. Machines launched using HPC flavors will have 40 Gb/s network access while standard flavors will have 10 Gb/s. For more information, see the chapter about virtual machine flavors: [Virtual machine flavors and quotas](/cloud/pouta/vm-flavors-and-billing)

Some limitations are imposed by virtualisation:

   - For intra node and external connectivity some overhead is introduced because of virtualization. This will impact latency and bandwidth, but we have no benchmark data to share at this time.
   - Applications sensitive to network latency may perform significantly worse than using a cluster (like Puhti) natively.
   - Overhead is introduced by the necessity to use Ethernet for virtual machine connectivity and compatibility.

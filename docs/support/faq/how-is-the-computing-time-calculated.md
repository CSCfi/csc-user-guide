# How is the computing time calculated?

The pricing of HPC CPU, HPC GPU, cloud and storage resources is based on CPU,
GPU, Cloud and Storage Billing Units (BUs), respectively. Hourly rate of BU
consumption depends on the BU flavor and service, as described in more detail
in our [billing models](../../accounts/billing.md).

See how to
[apply for more Billing Units](../../accounts/how-to-apply-for-billing-units.md).

## Batch job resource usage

The billing is calculated based on the resources that have been granted to your
batch job. For example, if you ask for 24 hours and 4 cores, but the job ends
after two hours, your project will be billed 2 x 4 core hours. Even if you ask
for 24 hours from the queuing system, you will not be billed 24 hours as the
resources become available for other users when your job ends. However, note
that the billing is not based on actual CPU usage, so if your code is using
only little CPU, e.g. due to inefficient parallelization, all resources that
have been allocated to your job will still be billed for.

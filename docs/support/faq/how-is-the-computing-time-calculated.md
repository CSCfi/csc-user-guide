# How is the computing time calculated?

The pricing of computing, cloud and storage services is based on billing units
(BUs). Hourly rate of BU consumption depends on the service, as described in
more detail in our [billing models](../../accounts/billing.md).

You can use the
[billing unit calculator](https://research.csc.fi/billing-units#buc) to
estimate your billing unit usage in different scenarios.

See how to
[apply for more billing units](../../accounts/how-to-apply-for-billing-units.md).

## Batch job resource usage

The billing is calculated based on the resources that have been granted to your
batch job. For example, if you ask for 24 hours and 4 cores, but the job ends
after two hours, your project will be billed 2 x 4 core hours. Even if you ask
for 24 hours from the queuing system, you will not be billed 24 hours as the
resources become available for other users when your job ends. However, note
that the billing is not based on actual CPU usage, so if your code is using
only little CPU, e.g. due to inefficient parallelization, all resources that
have been allocated to your job will still be billed for.

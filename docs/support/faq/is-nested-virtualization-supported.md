# Is nested virtualization supported on Pouta?

No, for the time being nested virtualization is not enabled in Pouta. Nested virtualization disables live migrations, and at this moment we consider that Live migration is a much more useful feature for our user than nested virtualization.

!!! Info "Nested virtualization"
    Nested virtualization is a feature that allows you to run virtual machines (VMs) inside other VMs. This is useful for testing and development purposes

!!! Info "Live migration"
    Live migration is the process of moving a running virtual machine between different physical machines without rebooting or shuting down the virtual machine. There might be a short downtime during the migration, but the processes running on the virtual machine do not perceive this downtime.

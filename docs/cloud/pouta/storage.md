# Pouta storage

This article introduces the storage options available in CSC's
cloud environment. Using the storage requires
an account, a project, and a virtual machine.

There is at least one type of storage available on every  irtual
machine: the file system defined by the virtual machine image. This is
the primary disk of the virtual machine. In addition, it may have a
certain amount of additional local disk space called **ephemeral
storage** in the OpenStack terminology defined by the flavor. This storage
is visible on the machine as a second hard disk.

This storage is only available while the
machine is running. When you terminate the machine, the data is lost. You should
not store any persistent data there, and the storage should not be
considered reliable. For persistent storage, you can use volumes and
the object storage as introduced below.

!!! note
    The Pouta object storage and Allas are separate services at least for now.
    So, there might be need for a Pouta object storage subsection in the main
    object storage article, which also describes Allas.

## [Ephemeral storage](ephemeral-storage.md)
## [Persistent volumes](persistent-volumes.md)

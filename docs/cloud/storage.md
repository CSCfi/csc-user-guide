# Storage in Pouta

This article collects the different storage options available in CSC
cloud environment. In order to utilize the storage options, you'll need
to have an account, a project and a virtual machine.

There  is at  least one  type of  storage available  on every  virtual
machine: the file system defined by the virtual machine image. This is
the primary  disk of the virtual  machine. In addition, it  may have a
certain  amount  of additional  local  disk  space called  **ephemeral
storage** in OpenStack terminology defined by the flavor. This storage
is visible on the machine as a second hard disk.

This  storage  is   only  available  for  as  long  as   you  run  the
machine. When you terminate the  machine, the data is lost. You should
not store  any persistent  data here, and the storage should  not be
considered reliable. For persistent storage you can use volumes and
Object storage as introduced below.

## [Ephemeral storage](ephemeral-storage.md)

## [Persistent volumes](persistent-volumes.md)

## [Snapshots](snapshots.md)

## [Object Storage](object-storage-main.md)
### [Using object Storage](using-object-storage.md)

!!! note
    Pouta object storage and Allas are separate services for at least some time
    So, there might be need for pouta object storage subsection in main
    object storage article, which also describes Allas